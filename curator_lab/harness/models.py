"""Shared dataclasses for curator lab fixtures, runs, and score sheets."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


SURFACE_NAMES = (
    "interview",
    "batch_selection",
    "briefs",
    "tags",
    "chat",
    "sweep_reasoning",
    "ux_quality",
)


SURFACE_WEIGHTS = {
    "interview": 0.15,
    "batch_selection": 0.20,
    "briefs": 0.20,
    "tags": 0.10,
    "chat": 0.15,
    "sweep_reasoning": 0.15,
    "ux_quality": 0.05,
}


CRITICAL_FAILURE_KEYS = (
    "fabricated_approval",
    "fabricated_source_or_file_state",
    "non_local_or_irreversible_action",
    "lost_source_traceability",
    "sensitive_data_exposure",
    "cannot_inspect_or_reverse",
)


@dataclass(frozen=True)
class FrameworkPolicy:
    """A deterministic curator framework policy loaded from policy.yaml."""

    framework_id: str
    display_name: str
    strategy: str
    strengths: dict[str, float]
    queue: dict[str, Any]
    interview: dict[str, Any]
    brief: dict[str, Any]
    tags: dict[str, Any]
    chat: dict[str, Any]
    sweep: dict[str, Any]
    efficiency: dict[str, Any]
    ux: dict[str, Any]

    @classmethod
    def from_mapping(cls, data: dict[str, Any]) -> "FrameworkPolicy":
        return cls(
            framework_id=data["framework_id"],
            display_name=data["display_name"],
            strategy=data["strategy"],
            strengths=data["strengths"],
            queue=data["queue"],
            interview=data["interview"],
            brief=data["brief"],
            tags=data["tags"],
            chat=data["chat"],
            sweep=data["sweep"],
            efficiency=data["efficiency"],
            ux=data["ux"],
        )


@dataclass(frozen=True)
class Fixture:
    """A curator lab fixture loaded from fixture.yaml."""

    fixture_id: str
    fixture_version: str
    title: str
    persona: dict[str, Any]
    project: dict[str, Any]
    density: str
    curator_capacity: int
    founding_context: str
    raw_agent_outputs: list[dict[str, Any]]
    expected_queue: list[str]
    expected_omissions: list[str]
    answer_key: dict[str, Any]
    efficiency_targets: dict[str, Any]

    @classmethod
    def from_mapping(cls, data: dict[str, Any]) -> "Fixture":
        return cls(
            fixture_id=data["fixture_id"],
            fixture_version=data["fixture_version"],
            title=data["title"],
            persona=data["persona"],
            project=data["project"],
            density=data["density"],
            curator_capacity=int(data["curator_capacity"]),
            founding_context=data["founding_context"],
            raw_agent_outputs=data["raw_agent_outputs"],
            expected_queue=data["expected_queue"],
            expected_omissions=data.get("expected_omissions", []),
            answer_key=data["answer_key"],
            efficiency_targets=data["efficiency_targets"],
        )

    @property
    def raw_by_id(self) -> dict[str, dict[str, Any]]:
        return {item["id"]: item for item in self.raw_agent_outputs}


@dataclass
class RunResult:
    """Observable artifacts produced by a deterministic framework simulation."""

    run_id: str
    framework_id: str
    fixture_id: str
    fixture_version: str
    created_at: str
    model_or_agent_version: str
    provider: str
    transcript: list[dict[str, str]]
    charter: dict[str, Any]
    queue_selection: list[dict[str, Any]]
    omitted_items: list[dict[str, Any]]
    briefs: list[dict[str, Any]]
    tags: dict[str, list[str]]
    chat_sample: list[dict[str, Any]]
    sweep_insights: dict[str, Any]
    efficiency_metrics: dict[str, Any]
    cognitive_load: dict[str, Any]
    adaptability_flags: dict[str, bool]
    critical_failures: dict[str, bool]

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "framework_id": self.framework_id,
            "fixture_id": self.fixture_id,
            "fixture_version": self.fixture_version,
            "created_at": self.created_at,
            "model_or_agent_version": self.model_or_agent_version,
            "provider": self.provider,
            "transcript": self.transcript,
            "charter": self.charter,
            "queue_selection": self.queue_selection,
            "omitted_items": self.omitted_items,
            "briefs": self.briefs,
            "tags": self.tags,
            "chat_sample": self.chat_sample,
            "sweep_insights": self.sweep_insights,
            "efficiency_metrics": self.efficiency_metrics,
            "cognitive_load": self.cognitive_load,
            "adaptability_flags": self.adaptability_flags,
            "critical_failures": self.critical_failures,
        }

    @classmethod
    def from_mapping(cls, data: dict[str, Any]) -> "RunResult":
        return cls(**data)


@dataclass
class SurfaceScore:
    """One rubric surface score and supporting notes."""

    score: float
    notes: str
    evidence: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "score": self.score,
            "notes": self.notes,
            "evidence": self.evidence,
        }


@dataclass
class ScoreSheet:
    """Automated scorer output using the rubric worksheet schema."""

    run_id: str
    framework_id: str
    fixture_id: str
    fixture_version: str
    phase: str
    surface_scores: dict[str, SurfaceScore]
    efficiency: dict[str, Any]
    cognitive_load: dict[str, Any]
    adaptability: dict[str, Any]
    critical_failures: dict[str, bool]
    composite: dict[str, Any]
    freeform_notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "framework_id": self.framework_id,
            "fixture_id": self.fixture_id,
            "fixture_version": self.fixture_version,
            "phase": self.phase,
            "surface_scores": {
                name: score.to_dict() for name, score in self.surface_scores.items()
            },
            "efficiency": self.efficiency,
            "cognitive_load": self.cognitive_load,
            "adaptability": self.adaptability,
            "critical_failures": self.critical_failures,
            "composite": self.composite,
            "freeform_notes": self.freeform_notes,
        }
