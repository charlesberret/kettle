# Curator benchmark snapshot

Baseline matrix from the product-home `curator_lab` deterministic simulator
(2026-08-06). Live kettle-core curator runs should replace this snapshot once
core is available to the evaluation environment.

## Ambitious goals

| Goal | Target |
|---|---|
| Continuous-improvement benchmark | Hybrid Desk Notebook matrix mean overall **≥ 4.2** |
| Stretch | Hybrid mean overall **≥ 4.5**; no surface mean below 4.0 |
| Intercoder | ≥85% surface agreement within 1 point; Cohen's κ ≥ 0.70 on flags |

See the full rubric in [curator-scoring.md](./curator-scoring.md).

## Prototype matrix (automated heuristic)

| Framework | Mean overall | vs 4.2 | vs 4.5 |
|---|---:|---|---|
| `hybrid_desk_notebook` | **4.417** | meets (auto) | short of stretch |
| `charter_first` | 3.539 | misses | misses |
| `signal_first` | 3.377 | misses | misses |

Cross-framework matrix mean: 3.777 (not the product KPI — the KPI is the
recommended framework's mean).

Automated secondary-scorer IRR on this run:

- agreement within 1 point: 1.00
- Cohen's κ on adaptability flags: 0.934

## Independent dual scoring (Hybrid sample)

Two scorers graded three Hybrid runs from artifacts only (`run.json`,
`transcript.txt`):

| Fixture | Scorer A (product) | Scorer B (engineering) | Surfaces ≤1pt |
|---|---:|---:|---:|
| `coding_novice_sparse_bugfix` | 3.675 | 3.575 | 7/7 |
| `writing_novice_dense_launch` | 3.125 | 3.200 | 7/7 |
| `operations_expert_noisy_incident` | 3.450 | 3.500 | 7/7 |

Pooled independent mean: **3.42**. Surface agreement within 1 point: **100%**.

Independent scores sit well below the automated heuristic (4.417). Treat **4.2**
as the goal for reconciled independent scoring — the auto lab is useful for
relative framework ranking, not as the final quality claim.
## Surface emphasis for the next improvement round

Hybrid already clears 4.2 as a simulated prototype. The stretch to 4.5 should
focus on:

1. **Tags** — restore sweep-topic coverage without synonym drift.
2. **Interview** — close the remaining charter-field gap (`review_criteria`)
   without returning to Charter-First over-questioning.
3. **Batch recall** — recover the occasional missed expected entry on dense
   queues while keeping capacity discipline.
4. **Briefs** — keep decision hooks on every queued entry, not only the top ranks.
5. **Chat continuity** — keep high continuity on dense/noisy sittings without
   token bloat.

## How to regenerate

```sh
python3 -m curator_lab.harness run --all
python3 -m curator_lab.harness report
```

Artifacts: `curator_lab/results/latest/` and committed
`curator_lab/results/baseline/`.

## Independent scoring

Use worksheet blanks under each run directory or
`curator_lab/results/latest/worksheets/`. Two scorers should grade independently
before reconciliation per the rubric's IRR protocol.
