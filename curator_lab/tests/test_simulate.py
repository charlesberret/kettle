import unittest

from curator_lab.harness.models import SURFACE_NAMES
from curator_lab.harness.score import matrix_summary, score_matrix, score_run
from curator_lab.harness.simulate import (
    list_fixture_ids,
    load_fixture,
    load_framework,
    simulate_matrix,
    simulate_run,
)


class SimulatorTests(unittest.TestCase):
    def test_simulator_produces_all_required_surfaces(self):
        fixture = load_fixture("coding_novice_sparse_bugfix")
        policy = load_framework("hybrid_desk_notebook")
        run = simulate_run(policy, fixture)

        self.assertTrue(run.transcript)
        self.assertTrue(run.charter)
        self.assertTrue(run.queue_selection)
        self.assertTrue(run.briefs)
        self.assertTrue(run.tags)
        self.assertTrue(run.chat_sample)
        self.assertTrue(run.sweep_insights)
        self.assertTrue(run.efficiency_metrics)

        sheet = score_run(run, fixture)
        self.assertEqual(set(sheet.surface_scores), set(SURFACE_NAMES))
        self.assertIsNotNone(sheet.composite["overall_score_0_5"])

    def test_hybrid_beats_charter_first_on_matrix_mean(self):
        fixture_ids = list_fixture_ids()
        runs = simulate_matrix(["charter_first", "hybrid_desk_notebook"], fixture_ids)
        fixtures = {fixture_id: load_fixture(fixture_id) for fixture_id in fixture_ids}
        scores = score_matrix(runs, fixtures)
        summary = matrix_summary(scores)

        self.assertGreater(
            summary["by_framework_mean_overall"]["hybrid_desk_notebook"],
            summary["by_framework_mean_overall"]["charter_first"],
        )


if __name__ == "__main__":
    unittest.main()
