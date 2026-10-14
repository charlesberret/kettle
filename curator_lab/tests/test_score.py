import unittest

from curator_lab.harness.score import composite_score, surface_weighted_score


class ScoreFormulaTests(unittest.TestCase):
    def test_surface_weighted_score_uses_rubric_weights(self):
        surfaces = {
            "interview": 4.0,
            "batch_selection": 5.0,
            "briefs": 4.0,
            "tags": 3.0,
            "chat": 4.0,
            "sweep_reasoning": 5.0,
            "ux_quality": 2.0,
        }

        self.assertAlmostEqual(
            surface_weighted_score(surfaces),
            0.15 * 4.0
            + 0.20 * 5.0
            + 0.20 * 4.0
            + 0.10 * 3.0
            + 0.15 * 4.0
            + 0.15 * 5.0
            + 0.05 * 2.0,
        )

    def test_composite_applies_efficiency_multiplier(self):
        surfaces = {
            "interview": 4.0,
            "batch_selection": 4.0,
            "briefs": 4.0,
            "tags": 4.0,
            "chat": 4.0,
            "sweep_reasoning": 4.0,
            "ux_quality": 4.0,
        }
        efficiency = {
            "turns_to_useful_charter": 6,
            "time_to_first_queue_ms": 5000,
            "redundant_token_rate": 0.10,
            "blocked_wait_events": 0,
        }
        targets = {
            "turns_to_useful_charter_max": 3,
            "time_to_first_queue_ms_max": 4000,
            "redundant_token_rate_max": 0.15,
            "manual_correction_count_max": 2,
            "perceived_load_1_7_max": 4,
        }

        composite = composite_score(
            surfaces,
            efficiency,
            targets,
            {"manual_correction_count": 1, "perceived_load_1_7": 3},
            {},
        )

        self.assertEqual(composite["efficiency_multiplier"], 0.90)
        self.assertEqual(composite["overall_score_0_5"], 3.6)

    def test_critical_failure_blocks_composite(self):
        surfaces = {name: 5.0 for name in (
            "interview",
            "batch_selection",
            "briefs",
            "tags",
            "chat",
            "sweep_reasoning",
            "ux_quality",
        )}

        composite = composite_score(
            surfaces,
            {"blocked_wait_events": 0},
            {
                "turns_to_useful_charter_max": 3,
                "time_to_first_queue_ms_max": 4000,
                "redundant_token_rate_max": 0.15,
                "manual_correction_count_max": 2,
                "perceived_load_1_7_max": 4,
            },
            {},
            {"fabricated_approval": True},
        )

        self.assertIsNone(composite["overall_score_0_5"])


if __name__ == "__main__":
    unittest.main()
