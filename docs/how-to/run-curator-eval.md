# Run the curator evaluation lab

Use this guide to run Kettle curator UX benchmark simulations from product-home. The lab is product quality tooling only; it does not execute kettle-core runtime.

## Run the full matrix

```sh
python3 -m curator_lab.harness run --all
```

Outputs are written to `curator_lab/results/latest/`:

- `report.md`;
- `scores.json`;
- `runs/*.json`;
- `worksheets/*-independent-blank.yaml`;
- `worksheets/*-independent-auto-draft.yaml`.

## Run one framework and fixture

```sh
python3 -m curator_lab.harness run --framework hybrid_desk_notebook --fixture coding_novice_sparse_bugfix
```

## Print the latest report

```sh
python3 -m curator_lab.harness report
```

## Interpret scores

The scorer implements `docs/reference/curator-scoring.md`:

- seven independent surface scores from 0 to 5;
- critical failure checks that suppress the composite;
- the weighted composite formula;
- the efficiency multiplier;
- independent scorer worksheet fields.

The ambitious benchmark goal is:

```text
matrix mean overall score >= 4.2
```

Committed baseline samples live in `curator_lab/results/baseline/`. Regenerated latest outputs are ignored by git so local experiments do not churn commits.
# How to run curator evaluation

**Goal:** Compare curator frameworks on a fixed fixture matrix and score them with the product rubric.

**Audience:** Contributors optimizing founding interview, familiarity, briefs, tags, chat, and sweep quality.

## Prerequisites

- Python 3.11+
- This repository checkout (no kettle-core install required for the lab)

## Steps

1. List frameworks and fixtures:

   ```sh
   python3 -m curator_lab.harness list
   ```

2. Run the full matrix:

   ```sh
   python3 -m curator_lab.harness run --all
   ```

3. Read the report:

   ```sh
   python3 -m curator_lab.harness report
   # or open curator_lab/results/latest/report.md
   ```

4. Optional: fill independent scorer worksheets under `curator_lab/results/latest/<fixture>/<framework>/score.independent.blank.json` using [`docs/reference/curator-scoring.md`](../reference/curator-scoring.md).

5. Run unit tests:

   ```sh
   python3 -m unittest discover -s curator_lab/tests -v
   ```

## Pass criteria for a lab round

- Hybrid Desk Notebook leads mean overall score.
- No critical failures in hybrid runs.
- Matrix report records the ambitious benchmark goal (**4.2**) and stretch (**4.5**).
- Independent scorers aim for ≥85% agreement within 1 point on surface scores.

## Related

- [Curator frameworks](../explanation/curator-frameworks.md)
- [Curator memory research](../explanation/curator-memory-research.md)
- [Curator scoring rubric](../reference/curator-scoring.md)
- Lab README: [`curator_lab/README.md`](../../curator_lab/README.md)
