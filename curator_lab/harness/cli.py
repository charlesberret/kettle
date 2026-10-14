"""Command-line interface for the curator lab harness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .report import DEFAULT_RESULTS_DIR, render_markdown_report, write_results
from .score import score_matrix
from .simulate import list_fixture_ids, list_framework_ids, load_fixture, simulate_matrix


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python3 -m curator_lab.harness")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run deterministic simulations and score them")
    run_parser.add_argument("--all", action="store_true", help="Run every framework against every fixture")
    run_parser.add_argument("--framework", help="Framework id to run")
    run_parser.add_argument("--fixture", help="Fixture id to run")
    run_parser.add_argument("--output", type=Path, default=DEFAULT_RESULTS_DIR, help="Output directory")

    report_parser = subparsers.add_parser("report", help="Print or regenerate a markdown report")
    report_parser.add_argument("--input", type=Path, default=DEFAULT_RESULTS_DIR / "scores.json")
    report_parser.add_argument("--write", action="store_true", help="Rewrite report.md next to scores.json")

    list_parser = subparsers.add_parser("list", help="List frameworks and fixtures")
    list_parser.set_defaults(command="list")

    args = parser.parse_args(argv)
    if args.command == "run":
        return _run(args)
    if args.command == "report":
        return _report(args)
    if args.command == "list":
        print("frameworks:", ", ".join(list_framework_ids()))
        print("fixtures:", ", ".join(list_fixture_ids()))
        return 0
    raise AssertionError(f"Unhandled command {args.command}")


def _run(args: argparse.Namespace) -> int:
    if args.all:
        framework_ids = list_framework_ids()
        fixture_ids = list_fixture_ids()
    else:
        if not args.framework or not args.fixture:
            raise SystemExit("--framework and --fixture are required unless --all is used")
        framework_ids = [args.framework]
        fixture_ids = [args.fixture]

    runs = simulate_matrix(framework_ids, fixture_ids)
    fixtures = {fixture_id: load_fixture(fixture_id) for fixture_id in fixture_ids}
    scores = score_matrix(runs, fixtures)
    payload = write_results(runs, scores, fixtures, args.output)
    summary = payload["summary"]
    print(f"Wrote {len(scores)} run(s) to {args.output}")
    print(f"Benchmark goal: {summary['benchmark_goal']}")
    print(f"Matrix mean overall: {summary['matrix_mean_overall']}")
    for framework_id, value in summary["by_framework_mean_overall"].items():
        print(f"{framework_id}: {value}")
    return 0


def _report(args: argparse.Namespace) -> int:
    if not args.input.exists():
        raise SystemExit(f"No scores file found at {args.input}. Run the lab first.")
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    markdown = _report_from_payload(payload, args.input)
    if args.write:
        report_path = args.input.parent / "report.md"
        report_path.write_text(markdown, encoding="utf-8")
        print(f"Wrote {report_path}")
    else:
        print(markdown)
    return 0


def _report_from_payload(payload: dict, scores_path: Path) -> str:
    report_path = scores_path.parent / "report.md"
    if report_path.exists():
        return report_path.read_text(encoding="utf-8")

    class _Surface:
        def __init__(self, score: float):
            self.score = score

    class _Score:
        def __init__(self, data: dict):
            self.framework_id = data["framework_id"]
            self.fixture_id = data["fixture_id"]
            self.composite = data["composite"]
            self.surface_scores = {name: _Surface(value["score"]) for name, value in data["surface_scores"].items()}

    return render_markdown_report([_Score(item) for item in payload["scores"]], payload["summary"])


if __name__ == "__main__":
    raise SystemExit(main())
