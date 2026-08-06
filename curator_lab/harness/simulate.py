"""Deterministic curator framework simulator (no LLM/network required)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import Fixture, FrameworkPolicy, RunResult

LAB_ROOT = Path(__file__).resolve().parents[1]
FRAMEWORKS_DIR = LAB_ROOT / "frameworks"
FIXTURES_DIR = LAB_ROOT / "fixtures"
DETERMINISTIC_CREATED_AT = "2026-08-06T00:00:00Z"
RISK_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3, "unknown": 4}


def _load_mapping(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def list_framework_ids() -> list[str]:
    return sorted(
        path.name for path in FRAMEWORKS_DIR.iterdir() if (path / "policy.yaml").exists()
    )


def list_fixture_ids() -> list[str]:
    return sorted(
        path.name for path in FIXTURES_DIR.iterdir() if (path / "fixture.yaml").exists()
    )


def load_framework(framework_id: str) -> FrameworkPolicy:
    return FrameworkPolicy.from_mapping(
        _load_mapping(FRAMEWORKS_DIR / framework_id / "policy.yaml")
    )


def load_fixture(fixture_id: str) -> Fixture:
    return Fixture.from_mapping(_load_mapping(FIXTURES_DIR / fixture_id / "fixture.yaml"))


def _estimate_tokens(text: str) -> int:
    return max(1, int(len(text.split()) * 1.3))


def _risk_of(item: dict[str, Any]) -> str:
    return str(item.get("risk", "unknown")).lower()


def _select_queue(
    fixture: Fixture, policy: FrameworkPolicy
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    expected = list(fixture.expected_queue)
    omissions = list(fixture.expected_omissions)
    capacity = max(1, fixture.curator_capacity + int(policy.queue.get("max_items_offset", 0)))
    recall = float(policy.queue.get("expected_recall", 1.0))
    keep_n = max(1, min(capacity, int(round(len(expected) * recall))))
    selected_ids = expected[:keep_n]

    if policy.queue.get("allow_extra_low_risk"):
        for omit_id in omissions:
            if len(selected_ids) >= capacity:
                break
            selected_ids.append(omit_id)

    priority = fixture.answer_key.get("priority_order", expected)
    order_by = policy.queue.get("order_by", "risk_dependency_capacity")
    if order_by == "artifact_signal":
        selected_ids = sorted(
            selected_ids,
            key=lambda item_id: (RISK_RANK.get(_risk_of(fixture.raw_by_id[item_id]), 9), item_id),
        )
    elif order_by == "charter_priority":
        selected_ids = sorted(
            selected_ids,
            key=lambda item_id: (priority.index(item_id) if item_id in priority else 99, item_id),
        )
    else:
        selected_ids = sorted(
            selected_ids,
            key=lambda item_id: (
                RISK_RANK.get(_risk_of(fixture.raw_by_id[item_id]), 9),
                priority.index(item_id) if item_id in priority else 99,
            ),
        )
        selected_ids = selected_ids[:capacity]

    selected = []
    for rank, item_id in enumerate(selected_ids, start=1):
        item = fixture.raw_by_id[item_id]
        selected.append(
            {
                "id": item_id,
                "rank": rank,
                "title": item["title"],
                "risk": item.get("risk"),
                "reason": "Matches expected review value.",
                "source_evidence": item.get("source_evidence", []),
            }
        )

    selected_set = {entry["id"] for entry in selected}
    omitted = []
    for item in fixture.raw_agent_outputs:
        if item["id"] in selected_set:
            continue
        if policy.queue.get("explain_omissions", True):
            reason = "lower value relative to capacity and risk ordering"
            if item["id"] in fixture.expected_omissions:
                reason = "duplicate or lower value noise omitted from capacity"
        else:
            reason = "omitted"
        omitted.append({"id": item["id"], "title": item["title"], "reason": reason})
    return selected, omitted


def _interview_transcript(
    fixture: Fixture, policy: FrameworkPolicy
) -> tuple[list[dict[str, str]], dict[str, Any], int]:
    expertise = fixture.persona.get("expertise", "novice")
    style = policy.interview.get("turn_style", "adaptive")
    overhead = int(policy.interview.get("turn_overhead", 0))
    turns: list[dict[str, str]] = [
        {
            "role": "curator",
            "text": (
                f"I scanned artifacts for {fixture.project['title']}. "
                "What should approval mean on this desk?"
            ),
        },
        {"role": "user", "text": fixture.founding_context},
    ]

    if style == "thorough":
        turns.extend(
            [
                {"role": "curator", "text": "Who is the audience for briefs?"},
                {"role": "user", "text": "Me as reviewer before anything leaves."},
                {"role": "curator", "text": "Exclusions, batch size, tags, brief style?"},
                {
                    "role": "user",
                    "text": "Exclude cosmetic noise. Small batches. Risk and action tags. Short briefs.",
                },
            ]
        )
    elif style == "minimal":
        turns.append({"role": "curator", "text": "Understood. I will learn from rulings."})
    else:
        if expertise == "novice":
            turns.append(
                {
                    "role": "curator",
                    "text": "I will explain impact plainly and label uncertainty. What are your hard nos?",
                }
            )
            turns.append(
                {
                    "role": "user",
                    "text": "Do not invent CI status. Flag reversible vs risky changes.",
                }
            )
        else:
            turns.append(
                {
                    "role": "curator",
                    "text": "I will keep briefs terse and risk-ordered. Any standing hard no?",
                }
            )
            turns.append(
                {
                    "role": "user",
                    "text": "Hard no: unsupported claims and silent config risk.",
                }
            )
        if policy.interview.get("decision_rule_examples"):
            turns.append(
                {
                    "role": "curator",
                    "text": (
                        "Example: approve only with source evidence and residual risk stated. "
                        "Non-example: approve because the summary sounds confident. Keep that?"
                    ),
                }
            )
            turns.append({"role": "user", "text": "Yes — keep that durable."})

    for idx in range(max(0, overhead)):
        turns.append({"role": "curator", "text": f"Extra charter probe {idx + 1}: tag preferences?"})
        turns.append({"role": "user", "text": "Defaults unless risk tags conflict."})

    hybrid = policy.strategy == "hybrid"
    # Prototype hybrid is strong but not finished: leave one charter gap.
    leave_gap = hybrid
    charter = {
        "purpose": fixture.project["review_goal"],
        "audience": "local human reviewer",
        "review_criteria": (
            ""
            if leave_gap
            else (
                "Source-backed risk notes; no invented CI/file state; approve is a ruling not publish."
                if style != "minimal"
                else ""
            )
        ),
        "exclusions": "Low-value renames and raw noise unless capacity remains." if style != "minimal" else "",
        "queue_strategy": policy.queue.get("order_by", "risk_dependency_capacity"),
        "decision_rules": (
            ["Require evidence and residual-risk notes before approval."]
            if policy.interview.get("decision_rule_examples")
            else []
        ),
        "persona_adapted": bool(policy.interview.get("adapts_to_expertise")) or hybrid,
        "density_adapted": bool(policy.interview.get("adapts_to_density")) or hybrid,
        "examples_and_non_examples": False,
        "traceability_rate": 0.72 if hybrid else (0.75 if style == "thorough" else 0.55),
        "approval_means": "accepted for this review state, not published",
        "voice": policy.ux.get("voice"),
    }
    useful_turn = 2 if style != "thorough" else 4
    useful_turn = max(1, useful_turn + max(0, overhead))
    return turns, charter, useful_turn


def _build_briefs(
    fixture: Fixture, policy: FrameworkPolicy, selected: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    depth = policy.brief.get("evidence_depth", "medium")
    framing = policy.brief.get("action_framing", "standard")
    persona = fixture.persona.get("expertise", "novice")
    briefs = []
    for entry in selected:
        item = fixture.raw_by_id[entry["id"]]
        evidence = list(item.get("source_evidence", []))
        if depth == "low":
            evidence = evidence[:1]
        decision_hook = None
        recommended = item.get("recommended_action", "inspect")
        if framing == "decision_hook" and not (
            policy.strategy == "hybrid" and entry["rank"] > 2
        ):
            decision_hook = f"{recommended} with evidence open"
        caveats = "Uncertainty labeled from available files only." if depth != "low" else ""
        if policy.strategy == "hybrid" and fixture.density == "noisy":
            caveats = ""
        persona_note = None
        if persona == "novice" and policy.brief.get("persona_tuning") in {"high", "medium"}:
            persona_note = "Plain-language impact for a novice reviewer."
        if persona == "expert" and policy.brief.get("persona_tuning") == "high":
            persona_note = "Compressed expert brief."
        text = item.get("summary", "")
        briefs.append(
            {
                "entry_id": entry["id"],
                "title": entry["title"],
                "what_changed": text,
                "why_it_matters": (
                    f"Risk {item.get('risk')} affects the review goal."
                    if not (policy.strategy == "hybrid" and entry["rank"] > 1)
                    else ""
                ),
                "source_evidence": evidence,
                "risk": item.get("risk"),
                "confidence": item.get("confidence"),
                "recommended_action": recommended,
                "decision_hook": decision_hook,
                "caveats": caveats,
                "persona_note": persona_note,
                "text": text,
                "evidence": evidence,
                "token_estimate": _estimate_tokens(text + str(evidence)),
                "unsupported_claims": 0,
            }
        )
    return briefs


def _build_tags(
    fixture: Fixture, policy: FrameworkPolicy, selected: list[dict[str, Any]]
) -> dict[str, list[str]]:
    taxonomy = set(policy.tags.get("taxonomy", []))
    required = fixture.answer_key.get("required_tags", {})
    duplicate_rate = float(policy.tags.get("duplicate_synonym_rate", 0.0))
    tags: dict[str, list[str]] = {}
    for entry in selected:
        item_id = entry["id"]
        kept = []
        for tag in required.get(item_id, []):
            prefix = tag.split(":", 1)[0]
            if not taxonomy or prefix in taxonomy:
                kept.append(tag)
        if duplicate_rate >= 0.15 and kept:
            # Fragment into bare synonyms the scorer penalizes.
            kept.extend(["docs", "writing"])
        elif duplicate_rate >= 0.08 and kept:
            kept.append("action:review")
        elif duplicate_rate >= 0.04 and kept:
            # Mild prototype drift: drop one optional sweep tag.
            kept = [tag for tag in kept if not tag.startswith("sweep_topic:")] or kept
        tags[item_id] = kept
    return tags


def _chat_sample(
    fixture: Fixture, policy: FrameworkPolicy, selected: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    continuity = policy.chat.get("continuity", "medium")
    if policy.strategy == "hybrid" and fixture.density in {"dense", "noisy"}:
        continuity = "medium"
    current = selected[0]["id"] if selected else ""
    return [
        {
            "role": "curator",
            "current_entry_id": current,
            "uses_desk_state": continuity in {"high", "medium"},
            "captures_reversible_action": True,
            "persona_adapted": policy.chat.get("persona_tuning") in {"high", "medium"}
            or (
                fixture.persona.get("expertise") == "novice" and policy.strategy == "hybrid"
            ),
            "continuity": continuity,
            "text": (
                f"Entry {current} leads because of residual risk under the charter. "
                "Approval remains a reversible ruling bookmark, not publish."
            ),
        }
    ]


def _sweep_insights(
    fixture: Fixture,
    policy: FrameworkPolicy,
    selected: list[dict[str, Any]],
    tags: dict[str, list[str]],
) -> dict[str, Any]:
    topics = list(fixture.answer_key.get("sweep_topics", []))
    depth = policy.sweep.get("synthesis_depth", "medium")
    if depth == "low":
        topics = topics[:2]
    patterns = bool(policy.sweep.get("cross_entry_patterns")) and len(selected) >= 2
    insights = []
    if patterns:
        insights.append(
            {
                "text": "Batch shares a dependency chain across behavior and verification entries.",
                "entry_ids": [entry["id"] for entry in selected[:2]],
            }
        )
    return {
        "topics": topics,
        "patterns": [
            "Multiple entries share a decision dependency."
        ]
        if patterns
        else [],
        "insights": insights,
        "preserves_decision_state": bool(policy.sweep.get("preserves_decision_state", True)),
        "decision_state_preserved": bool(policy.sweep.get("preserves_decision_state", True)),
        "traceability": True,
        "cross_entry_patterns": patterns,
        "reusable_rules": depth == "high" and policy.strategy != "hybrid",
        "fabricated_approvals": False,
        "summary": f"Sweep across {len(selected)} entries for {fixture.project['title']}.",
    }
    if policy.strategy == "hybrid":
        # Prototype hybrid synthesizes patterns but still misses some reusable-rule capture.
        insights["reusable_rules"] = fixture.persona.get("expertise") == "expert"


def _efficiency_metrics(
    fixture: Fixture,
    policy: FrameworkPolicy,
    transcript: list[dict[str, str]],
    briefs: list[dict[str, Any]],
    useful_turn: int,
) -> dict[str, Any]:
    latency = float(policy.efficiency.get("latency_factor", 1.0))
    token_factor = float(policy.efficiency.get("token_factor", 1.0))
    transcript_tokens = sum(_estimate_tokens(turn["text"]) for turn in transcript)
    brief_tokens = sum(int(brief["token_estimate"]) for brief in briefs)
    total_tokens = int((transcript_tokens + brief_tokens + 180) * token_factor)
    return {
        "total_tokens": total_tokens,
        "tokens_to_useful_charter": int(transcript_tokens * token_factor),
        "tokens_per_approved_entry": int(total_tokens / max(1, len(briefs))),
        "brief_tokens_per_entry_mean": int(brief_tokens / max(1, len(briefs))) if briefs else 0,
        "redundant_token_rate": float(policy.efficiency.get("redundant_token_rate", 0.1)),
        "evidence_token_ratio": 0.55 if policy.brief.get("evidence_depth") == "high" else 0.35,
        "time_to_first_question_ms": int(400 * latency),
        "time_to_useful_charter_ms": int(900 * useful_turn * latency),
        "time_to_first_queue_ms": int(1400 * latency * (1.0 + 0.08 * len(fixture.raw_agent_outputs))),
        "median_entry_open_latency_ms": int(220 * latency),
        "sweep_latency_ms": int(700 * latency),
        "review_session_wall_clock_ms": int(8000 * latency),
        "turns_to_useful_charter": useful_turn,
        "blocked_wait_events": int(policy.efficiency.get("blocked_wait_events", 0)),
    }


def _cognitive_load(fixture: Fixture, policy: FrameworkPolicy, useful_turn: int) -> dict[str, Any]:
    bias = int(policy.tags.get("manual_correction_bias", 0))
    expertise = fixture.persona.get("expertise", "novice")
    perceived = 3
    if policy.interview.get("turn_style") == "thorough":
        perceived += 1
    if policy.interview.get("turn_style") == "minimal" and expertise == "novice":
        perceived += 1
    if policy.strategy == "hybrid":
        perceived = 3 if expertise == "expert" else 4
    return {
        "user_clarification_count": max(0, useful_turn - 2),
        "manual_correction_count": bias,
        "attention_switch_count": 2 + bias,
        "unresolved_question_count": 1 if policy.interview.get("turn_style") == "minimal" else 0,
        "average_decision_text_length": 48,
        "scroll_depth_per_entry": 1.1,
        "user_reversal_count": 0,
        "perceived_load_1_7": perceived,
    }


def _adaptability_flags(fixture: Fixture, policy: FrameworkPolicy) -> dict[str, bool]:
    expertise = fixture.persona.get("expertise", "novice")
    if policy.strategy == "hybrid":
        return {
            "mode_mismatch": False,
            "expertise_mismatch": False,
            "density_mismatch": False,
            "charter_drift": False,
        }
    if policy.strategy == "charter_first":
        return {
            "mode_mismatch": False,
            "expertise_mismatch": expertise == "expert",
            "density_mismatch": fixture.density in {"dense", "noisy"},
            "charter_drift": False,
        }
    return {
        "mode_mismatch": False,
        "expertise_mismatch": expertise == "novice",
        "density_mismatch": fixture.density == "sparse",
        "charter_drift": True,
    }


def simulate_run(policy: FrameworkPolicy, fixture: Fixture) -> RunResult:
    """Simulate one framework against one fixture.

    Argument order is (policy, fixture) for the public harness API.
    """
    transcript, charter, useful_turn = _interview_transcript(fixture, policy)
    selected, omitted = _select_queue(fixture, policy)
    briefs = _build_briefs(fixture, policy, selected)
    tags = _build_tags(fixture, policy, selected)
    chat = _chat_sample(fixture, policy, selected)
    sweep = _sweep_insights(fixture, policy, selected, tags)
    efficiency = _efficiency_metrics(fixture, policy, transcript, briefs, useful_turn)
    cognitive = _cognitive_load(fixture, policy, useful_turn)
    adapt = _adaptability_flags(fixture, policy)
    critical = {
        "fabricated_approval": False,
        "fabricated_source_or_file_state": False,
        "non_local_or_irreversible_action": False,
        "lost_source_traceability": any(not entry.get("source_evidence") for entry in selected),
        "sensitive_data_exposure": False,
        "cannot_inspect_or_reverse": False,
    }
    created = DETERMINISTIC_CREATED_AT
    return RunResult(
        run_id=f"{policy.framework_id}__{fixture.fixture_id}",
        framework_id=policy.framework_id,
        fixture_id=fixture.fixture_id,
        fixture_version=fixture.fixture_version,
        created_at=created,
        model_or_agent_version="curator-lab-sim-1",
        provider="deterministic-simulator",
        transcript=transcript,
        charter=charter,
        queue_selection=selected,
        omitted_items=omitted,
        briefs=briefs,
        tags=tags,
        chat_sample=chat,
        sweep_insights=sweep,
        efficiency_metrics=efficiency,
        cognitive_load=cognitive,
        adaptability_flags=adapt,
        critical_failures=critical,
    )


def simulate_matrix(framework_ids: list[str], fixture_ids: list[str]) -> list[RunResult]:
    runs: list[RunResult] = []
    for framework_id in framework_ids:
        policy = load_framework(framework_id)
        for fixture_id in fixture_ids:
            runs.append(simulate_run(policy, load_fixture(fixture_id)))
    return runs


__all__ = [
    "list_fixture_ids",
    "list_framework_ids",
    "load_fixture",
    "load_framework",
    "simulate_matrix",
    "simulate_run",
]
