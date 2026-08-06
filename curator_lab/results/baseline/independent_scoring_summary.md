# Independent scoring summary

Two independent scorers graded three Hybrid Desk Notebook runs from `run.json` and `transcript.txt` only.

| Fixture | Scorer A (product) | Scorer B (engineering) | Δ | Surfaces within 1pt |
|---|---:|---:|---:|---:|
| `coding_novice_sparse_bugfix` | 3.675 | 3.575 | 0.100 | 7/7 |
| `writing_novice_dense_launch` | 3.125 | 3.2 | 0.075 | 7/7 |
| `operations_expert_noisy_incident` | 3.45 | 3.5 | 0.050 | 7/7 |

Mean overall — Scorer A: **3.417**; Scorer B: **3.425**; pooled mean: **3.421**
Surface agreement within 1 point: **21/21 (100%)**

## Calibration notes

- Independent scores are materially below the automated heuristic (Hybrid auto mean 4.417).
- Shared deductions: empty `review_criteria`, thin/generic sweep synthesis, chat limited to one sample, tags too generic on writing/ops.
- Ambition **4.2** remains the goal for reconciled independent scoring; stretch **4.5**.
- Detailed notes: `independent_scoring_notes_a.md`, `independent_scoring_notes_b.md`.
