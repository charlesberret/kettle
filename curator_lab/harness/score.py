"""Rubric scoring and composite formula for curator lab runs."""

from __future__ import annotations

from statistics import mean
from typing import Any

from .models import SURFACE_NAMES, SURFACE_WEIGHTS, Fixture, RunResult, ScoreSheet, SurfaceScore

BENCHMARK_GOAL = "matrix mean overall score >= 4.2"


def clamp_score(value: float) -> float:
    return max(0.0, min(5.0, round(value * 2) / 2))


def surface_weighted_score(surface_scores: dict[str, float]) -> float:
    """Apply the exact rubric surface weights before the efficiency multiplier."""

    return sum(surface_scores[name] * SURFACE_WEIGHTS[name] for name in SURFACE_NAMES)


def efficiency_multiplier(
    efficiency: dict[str, Any],
    fixture_targets: dict[str, Any],
    cognitive_load: dict[str, Any] | None = None,
) -> float:
    """Return the rubric multiplier for fixture target-band misses."""

    cognitive_load = cognitive_load or {}
    if int(efficiency.get("blocked_wait_events", 0)) > 0:
        return 0.80

    misses = 0
    checks = (
        ("turns_to_useful_charter", "turns_to_useful_charter_max"),
        ("time_to_first_queue_ms", "time_to_first_queue_ms_max"),
        ("redundant_token_rate", "redundant_token_rate_max"),
    )
    for metric_key, target_key in checks:
        if float(efficiency.get(metric_key, 0)) > float(fixture_targets[target_key]):
            misses += 1

    load_checks = (
        ("manual_correction_count", "manual_correction_count_max"),
        ("perceived_load_1_7", "perceived_load_1_7_max"),
    )
    for metric_key, target_key in load_checks:
        if float(cognitive_load.get(metric_key, 0)) > float(fixture_targets[target_key]):
            misses += 1

    if misses == 0:
        return 1.00
    if misses == 1:
        return 0.95
    return 0.90


def composite_score(
    surface_scores: dict[str, float],
    efficiency: dict[str, Any],
    fixture_targets: dict[str, Any],
    cognitive_load: dict[str, Any] | None = None,
    critical_failures: dict[str, bool] | None = None,
) -> dict[str, Any]:
    """Compute rubric composite, returning null overall when critical failures exist."""

    critical_failures = critical_failures or {}
    if any(critical_failures.values()):
        return {
            "efficiency_multiplier": None,
            "surface_weighted_score": None,
            "overall_score_0_5": None,
            "computed_by": "script",
            "notes": "Composite omitted because one or more critical failures are present.",
        }

    weighted = surface_weighted_score(surface_scores)
    multiplier = efficiency_multiplier(efficiency, fixture_targets, cognitive_load)
    return {
        "efficiency_multiplier": multiplier,
        "surface_weighted_score": round(weighted, 3),
        "overall_score_0_5": round(weighted * multiplier, 3),
        "computed_by": "script",
        "notes": "Rubric formula from docs/reference/curator-scoring.md.",
    }


def score_run(run: RunResult, fixture: Fixture) -> ScoreSheet:
    surfaces = {
        "interview": _score_interview(run),
        "batch_selection": _score_batch_selection(run, fixture),
        "briefs": _score_briefs(run, fixture),
        "tags": _score_tags(run, fixture),
        "chat": _score_chat(run),
        "sweep_reasoning": _score_sweep(run, fixture),
        "ux_quality": _score_ux(run),
    }
    numeric = {name: surface.score for name, surface in surfaces.items()}
    composite = composite_score(
        numeric,
        run.efficiency_metrics,
        fixture.efficiency_targets,
        run.cognitive_load,
        run.critical_failures,
    )
    adaptability = {
        "project_type": fixture.project["type"],
        "user_expertise": fixture.persona["expertise"],
        "agent_output_density": fixture.density,
        "flags": run.adaptability_flags,
        "notes": "Flags are derived from visible adaptation markers in the simulated artifacts.",
    }
    return ScoreSheet(
        run_id=run.run_id,
        framework_id=run.framework_id,
        fixture_id=run.fixture_id,
        fixture_version=run.fixture_version,
        phase="resolved",
        surface_scores=surfaces,
        efficiency=run.efficiency_metrics,
        cognitive_load=run.cognitive_load,
        adaptability=adaptability,
        critical_failures=run.critical_failures,
        composite=composite,
        freeform_notes="Automated heuristic score; use worksheets for independent secondary scoring.",
    )


def score_matrix(runs: list[RunResult], fixtures: dict[str, Fixture]) -> list[ScoreSheet]:
    return [score_run(run, fixtures[run.fixture_id]) for run in runs]


def matrix_summary(scores: list[ScoreSheet]) -> dict[str, Any]:
    overall_values = [
        sheet.composite["overall_score_0_5"]
        for sheet in scores
        if sheet.composite["overall_score_0_5"] is not None
    ]
    by_framework: dict[str, list[float]] = {}
    by_surface: dict[str, list[float]] = {name: [] for name in SURFACE_NAMES}
    for sheet in scores:
        overall = sheet.composite["overall_score_0_5"]
        if overall is not None:
            by_framework.setdefault(sheet.framework_id, []).append(overall)
        for name, surface in sheet.surface_scores.items():
            by_surface[name].append(surface.score)

    return {
        "benchmark_goal": BENCHMARK_GOAL,
        "matrix_mean_overall": round(mean(overall_values), 3) if overall_values else None,
        "by_framework_mean_overall": {
            framework_id: round(mean(values), 3)
            for framework_id, values in sorted(by_framework.items())
        },
        "by_surface_mean": {
            name: round(mean(values), 3)
            for name, values in by_surface.items()
            if values
        },
        "run_count": len(scores),
    }


def _score_interview(run: RunResult) -> SurfaceScore:
    charter = run.charter
    required_fields = (
        "purpose",
        "audience",
        "review_criteria",
        "exclusions",
        "queue_strategy",
        "decision_rules",
    )
    coverage = sum(1 for field in required_fields if charter.get(field)) / len(required_fields)
    adaptation = 0.0
    if charter.get("persona_adapted"):
        adaptation += 0.5
    if charter.get("density_adapted"):
        adaptation += 0.4
    if charter.get("examples_and_non_examples"):
        adaptation += 0.4
    traceability = 0.4 if float(charter.get("traceability_rate", 0)) >= 0.80 else 0.0
    excess_turn_penalty = 0.3 if len(run.transcript) > 4 and not charter.get("persona_adapted") else 0.0
    score = clamp_score(1.8 + coverage * 1.7 + adaptation + traceability - excess_turn_penalty)
    return SurfaceScore(
        score=score,
        notes="Scored from charter field coverage, persona/density adaptation, examples, and traceability.",
        evidence=[f"charter fields={coverage:.0%}", f"transcript_turns={len(run.transcript)}"],
    )


def _score_batch_selection(run: RunResult, fixture: Fixture) -> SurfaceScore:
    selected = [item["id"] for item in run.queue_selection]
    expected = fixture.expected_queue
    selected_set = set(selected)
    expected_set = set(expected)
    precision = len(selected_set & expected_set) / max(len(selected_set), 1)
    recall = len(selected_set & expected_set) / max(len(expected_set), 1)
    order_score = _order_similarity(selected, fixture.answer_key["priority_order"])
    capacity_fit = 1.0 if len(selected) <= fixture.curator_capacity else 0.65
    omission_explained = _omission_explanation_rate(run, fixture)
    raw = (precision * 1.25) + (recall * 1.35) + (order_score * 1.0) + (capacity_fit * 0.55) + (omission_explained * 0.85)
    score = clamp_score(raw)
    return SurfaceScore(
        score=score,
        notes="Precision, recall, ordering, capacity fit, and omission explanation are measured separately then combined.",
        evidence=[
            f"precision={precision:.2f}",
            f"recall={recall:.2f}",
            f"order={order_score:.2f}",
            f"omissions_explained={omission_explained:.2f}",
        ],
    )


def _score_briefs(run: RunResult, fixture: Fixture) -> SurfaceScore:
    if not run.briefs:
        return SurfaceScore(0.0, "No briefs emitted.", [])
    per_brief = []
    unsupported = 0
    expected_ids = set(fixture.expected_queue)
    for brief in run.briefs:
        points = 0
        points += 1 if brief.get("what_changed") else 0
        points += 1 if brief.get("why_it_matters") else 0
        points += 1 if brief.get("source_evidence") else 0
        points += 1 if brief.get("risk") and brief.get("confidence") else 0
        points += 1 if brief.get("recommended_action") or brief.get("decision_hook") else 0
        points += 1 if brief.get("caveats") is not None else 0
        points += 1 if brief.get("entry_id") in expected_ids else 0
        if brief.get("persona_note"):
            points += 0.5
        unsupported += int(brief.get("unsupported_claims", 0))
        per_brief.append(points / 7.5)
    score = clamp_score(mean(per_brief) * 5)
    if unsupported:
        score = min(score, 2.0)
    return SurfaceScore(
        score=score,
        notes="Briefs are scored for change, importance, evidence, risk, action framing, caveats, and answer-key relevance.",
        evidence=[f"sampled_count={len(run.briefs)}", f"unsupported_claims={unsupported}"],
    )


def _score_tags(run: RunResult, fixture: Fixture) -> SurfaceScore:
    if not run.tags:
        return SurfaceScore(0.0, "No tags emitted.", [])
    recalls = []
    synonym_penalty = 0
    for item_id, required in fixture.answer_key["required_tags"].items():
        if item_id not in run.tags:
            continue
        actual = set(run.tags[item_id])
        recalls.append(len(actual & set(required)) / len(required))
        if "docs" in actual or "writing" in actual:
            synonym_penalty += 1
    coverage = mean(recalls) if recalls else 0.0
    correction_rate = run.cognitive_load["manual_correction_count"] / max(len(run.tags), 1)
    score = clamp_score((coverage * 4.6) + (0.4 if correction_rate <= 0.25 else 0.0) - (0.25 * synonym_penalty))
    return SurfaceScore(
        score=score,
        notes="Tag score compares required taxonomy dimensions and penalizes synonym fragmentation/corrections.",
        evidence=[f"coverage={coverage:.2f}", f"manual_correction_rate={correction_rate:.2f}"],
    )


def _score_chat(run: RunResult) -> SurfaceScore:
    if not run.chat_sample:
        return SurfaceScore(0.0, "No chat sample emitted.", [])
    sample = run.chat_sample[0]
    points = 1.0
    points += 1.2 if sample.get("uses_desk_state") else 0.0
    points += 1.0 if sample.get("captures_reversible_action") else 0.0
    points += 1.0 if sample.get("persona_adapted") else 0.0
    points += 0.8 if sample.get("continuity") == "high" else (0.4 if sample.get("continuity") == "medium" else 0.0)
    return SurfaceScore(
        score=clamp_score(points),
        notes="Chat is scored for visible desk state, reversible action, persona adaptation, and continuity.",
        evidence=[f"current_entry_id={sample.get('current_entry_id')}", f"continuity={sample.get('continuity')}"],
    )


def _score_sweep(run: RunResult, fixture: Fixture) -> SurfaceScore:
    sweep = run.sweep_insights
    if sweep.get("fabricated_approvals"):
        return SurfaceScore(2.0, "Fabricated approval caps sweep score at 2.", [])
    topics = set(sweep.get("topics", []))
    expected_topics = set(fixture.answer_key["sweep_topics"])
    topic_recall = len(topics & expected_topics) / max(len(expected_topics), 1)
    points = topic_recall * 2.0
    points += 1.0 if sweep.get("preserves_decision_state") else 0.0
    points += 1.0 if sweep.get("traceability") else 0.0
    points += 0.7 if sweep.get("cross_entry_patterns") else 0.0
    points += 0.3 if sweep.get("reusable_rules") else 0.0
    return SurfaceScore(
        score=clamp_score(points),
        notes="Sweep is scored for topic coverage, decision-state faithfulness, traceability, patterns, and reusable rules.",
        evidence=[f"topic_recall={topic_recall:.2f}", f"insight_count={len(sweep.get('insights', []))}"],
    )


def _score_ux(run: RunResult) -> SurfaceScore:
    cognitive = run.cognitive_load
    score = 3.0
    if not run.adaptability_flags.get("expertise_mismatch"):
        score += 0.6
    if not run.adaptability_flags.get("density_mismatch"):
        score += 0.5
    if cognitive.get("perceived_load_1_7", 7) <= 3:
        score += 0.5
    if cognitive.get("manual_correction_count", 9) <= 1:
        score += 0.4
    if run.adaptability_flags.get("charter_drift"):
        score -= 0.6
    return SurfaceScore(
        score=clamp_score(score),
        notes="UX quality is scored separately from function using consistency, adaptation, perceived load, and drift.",
        evidence=[
            f"perceived_load={cognitive.get('perceived_load_1_7')}",
            f"manual_corrections={cognitive.get('manual_correction_count')}",
        ],
    )


def _order_similarity(selected: list[str], expected_order: list[str]) -> float:
    selected_expected = [item for item in selected if item in expected_order]
    if not selected_expected:
        return 0.0
    positions = {item_id: index for index, item_id in enumerate(expected_order)}
    inversions = 0
    comparisons = 0
    for left_index, left in enumerate(selected_expected):
        for right in selected_expected[left_index + 1 :]:
            comparisons += 1
            if positions[left] > positions[right]:
                inversions += 1
    if comparisons == 0:
        return 1.0
    return 1.0 - (inversions / comparisons)


def _omission_explanation_rate(run: RunResult, fixture: Fixture) -> float:
    expected_omissions = set(fixture.expected_omissions)
    if not expected_omissions:
        return 1.0
    explained = 0
    for item in run.omitted_items:
        is_expected_omission = item["id"] in expected_omissions
        has_explanation = (
            "duplicate" in item["reason"]
            or "lower value" in item["reason"]
            or "capacity" in item["reason"]
        )
        if is_expected_omission and has_explanation:
            explained += 1
    return min(1.0, explained / len(expected_omissions))
