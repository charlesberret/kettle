# Independent scoring notes - scorer B

Scorer: `scorer_b`  
Role: engineering  
Phase: independent  
Artifacts used: each run's `run.json` and `transcript.txt`; automated score files were not used as ground truth.

## Overall scores

| Fixture | Interview | Batch | Briefs | Tags | Chat | Sweep | UX | Efficiency multiplier | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `coding_novice_sparse_bugfix` | 3.5 | 4.0 | 3.5 | 4.0 | 3.0 | 3.5 | 3.5 | 1.00 | 3.575 |
| `writing_novice_dense_launch` | 3.0 | 4.0 | 3.5 | 3.0 | 3.0 | 2.5 | 2.5 | 1.00 | 3.200 |
| `operations_expert_noisy_incident` | 3.5 | 4.0 | 4.0 | 3.0 | 3.0 | 3.0 | 3.5 | 1.00 | 3.500 |

## Cross-run calibration points

- Efficiency multiplier 1.00 for all three runs (quick charter/queue, no blocked waits).
- Chat capped near 3 because only one post-founding sample is visible.
- Tags scored lower where taxonomy is accurate but too generic for fixture-specific filtering.
- Shared gap with Scorer A: empty `review_criteria` and generic sweep synthesis keep Hybrid below the 4.2 independent ambition.
