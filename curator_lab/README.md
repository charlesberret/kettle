# Curator lab

Curator lab is product quality tooling for Kettle's local-first review desk. It
simulates curator UX frameworks, scores their observable artifacts with
`docs/reference/curator-scoring.md`, and produces repeatable reports for product
iteration.

The lab is conceptually named `curator-lab`, but the importable Python package is
`curator_lab` so it can be run with `python3 -m curator_lab.harness`.

This is **not** kettle-core runtime code. The repository remains product-home;
fixtures and simulator output are local benchmark artifacts only.

## What it evaluates

Each framework runs against every fixture and emits:

- founding interview transcript turns;
- charter fields and decision rules;
- queue/batch selection with source evidence;
- entry briefs;
- tags;
- chat sample;
- sweep insights;
- efficiency and cognitive-load metrics.

The automated scorer maps those artifacts to the rubric surfaces:

1. interview;
2. batch selection;
3. briefs;
4. tags;
5. chat;
6. sweep reasoning;
7. UX quality.

The composite formula is the rubric's weighted surface score multiplied by the
fixture efficiency multiplier. Critical failures suppress the composite.

## Frameworks

- `charter_first`: strong founding charter, weaker adaptation to expert/dense
  inputs.
- `signal_first`: fast artifact triage, weaker founding interview and durable
  tags/sweep memory.
- `hybrid_desk_notebook`: adaptive charter plus local desk notebook behavior;
  intended reference direction.

## Fixtures

Fixtures live under `fixtures/*/fixture.yaml` with fake raw agent outputs under
`agent_output/`. The YAML files are JSON-compatible so the harness is
dependency-free and runs with Python's standard library.

## Run

From the repository root:

```sh
python3 -m curator_lab.harness run --all
python3 -m curator_lab.harness run --framework hybrid_desk_notebook --fixture coding_novice_sparse_bugfix
python3 -m curator_lab.harness report
```

Generated outputs go to `curator_lab/results/latest/`:

- `scores.json`: machine-readable matrix scores;
- `report.md`: markdown report;
- `runs/*.json`: full run artifacts;
- `worksheets/*-independent-blank.yaml`: blank secondary scoring worksheets;
- `worksheets/*-independent-auto-draft.yaml`: automated scorer draft worksheets.

Committed baseline samples live in `curator_lab/results/baseline/`.

## Benchmark goal

The rubric's ambitious target is:

```text
matrix mean overall score >= 4.2
```

Use the baseline as a comparison point for curator UX optimization rounds, not
as a runtime acceptance gate for kettle-core.
# Curator lab

Product-quality evaluation laboratory for Kettle's curator agent frameworks.

This package is **not** kettle-core runtime. It lives in the product-home
repository so we can research, simulate, and score curator UX before (and while)
core implements the recommended Hybrid Desk Notebook behavior.

## What it contains

| Path | Role |
|---|---|
| `frameworks/` | Charter-First, Signal-First, Hybrid Desk Notebook policies + system specs |
| `fixtures/` | Persona × project demo scenarios with answer keys |
| `harness/` | Deterministic simulator, rubric scorer, IRR helpers, CLI |
| `prototypes/hybrid_desk_notebook/` | Reference memory schema, interview/promotion policies, templates |
| `results/latest/` | Latest matrix run artifacts |
| `results/baseline/` | Committed baseline snapshot for comparison |
| `tests/` | Unit tests for formula, simulation surfaces, hybrid ranking |

## Run

From the repository root:

```sh
python3 -m curator_lab.harness list
python3 -m curator_lab.harness run --all
python3 -m curator_lab.harness report
python3 -m unittest discover -s curator_lab/tests -v
```

Single cell:

```sh
python3 -m curator_lab.harness run \
  --framework hybrid_desk_notebook \
  --fixture coding_novice_sparse_bugfix
```

## Scoring

Automated scores follow
[`docs/reference/curator-scoring.md`](../docs/reference/curator-scoring.md):

- Surface weights: interview 15%, batch 20%, briefs 20%, tags 10%, chat 15%,
  sweep 15%, UX 5%.
- Efficiency multiplier bands: 1.00 / 0.95 / 0.90 / 0.80.
- Ambitious matrix mean overall goal: **≥ 4.2** (stretch **≥ 4.5**).

Each run writes:

- `run.json` — observable artifacts
- `score.automated.json` — heuristic scorer
- `score.independent.blank.json` — worksheet for a second human/agent scorer
- `transcript.txt` — founding interview transcript

## Framework expectation

On the baseline matrix, **Hybrid Desk Notebook** should lead mean overall score.
Charter-First stays stronger on thorough interviews but weaker on adaptation.
Signal-First stays cheaper/faster but weaker on founding interview, tags, and
continuity.
