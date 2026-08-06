"""Unit tests that import loaders from simulate (canonical)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from curator_lab.harness.irr import agreement_within_one, cohens_kappa
from curator_lab.harness.models import SURFACE_NAMES, SURFACE_WEIGHTS
from curator_lab.harness.score import efficiency_multiplier, score_run, surface_weighted_score
from curator_lab.harness.simulate import (
    list_fixture_ids,
    list_framework_ids,
    load_fixture,
    load_framework,
    simulate_run,
)


class ScoreFormulaTests(unittest.TestCase):
    def test_surface_weights_sum_to_one(self) -> None:
        self.assertAlmostEqual(sum(SURFACE_WEIGHTS.values()), 1.0)
        self.assertEqual(set(SURFACE_NAMES), set(SURFACE_WEIGHTS))

    def test_weighted_score(self) -> None:
        scores = {name: 5.0 for name in SURFACE_NAMES}
        self.assertEqual(surface_weighted_score(scores), 5.0)

    def test_efficiency_multiplier_bands(self) -> None:
        fixture = load_fixture("coding_novice_sparse_bugfix")
        good = {
            "turns_to_useful_charter": 2,
            "time_to_first_queue_ms": 1000,
            "redundant_token_rate": 0.05,
            "blocked_wait_events": 0,
        }
        cognitive = {"manual_correction_count": 0, "perceived_load_1_7": 2}
        self.assertEqual(
            efficiency_multiplier(good, fixture.efficiency_targets, cognitive),
            1.0,
        )


class SimulatorTests(unittest.TestCase):
    def test_all_surfaces_present(self) -> None:
        fixture = load_fixture("coding_novice_sparse_bugfix")
        policy = load_framework("hybrid_desk_notebook")
        run = simulate_run(policy, fixture)
        self.assertTrue(run.transcript)
        self.assertTrue(run.charter)
        self.assertTrue(run.queue_selection)
        self.assertTrue(run.briefs)
        sheet = score_run(run, fixture)
        self.assertIsNotNone(sheet.composite["overall_score_0_5"])

    def test_hybrid_beats_charter_on_matrix_mean(self) -> None:
        means = {}
        for framework_id in list_framework_ids():
            policy = load_framework(framework_id)
            scores = []
            for fixture_id in list_fixture_ids():
                fixture = load_fixture(fixture_id)
                run = simulate_run(policy, fixture)
                sheet = score_run(run, fixture)
                overall = sheet.composite["overall_score_0_5"]
                self.assertIsNotNone(overall)
                scores.append(float(overall))
            means[framework_id] = sum(scores) / len(scores)
        self.assertGreater(means["hybrid_desk_notebook"], means["charter_first"])
        self.assertGreater(means["hybrid_desk_notebook"], means["signal_first"])


class IRRTests(unittest.TestCase):
    def test_agreement_and_kappa(self) -> None:
        self.assertEqual(agreement_within_one([4, 4, 3], [4, 5, 2]), 1.0)
        self.assertGreater(
            cohens_kappa([True, False, True, False], [True, False, True, True]),
            0.0,
        )


if __name__ == "__main__":
    unittest.main()
