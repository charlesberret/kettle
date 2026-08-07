# Independent scoring summary

Rubric: `docs/reference/curator-scoring.md`

Scope: scored only each target run's `run.json` and `transcript.txt`, with fixture efficiency targets from `curator_lab/fixtures/<id>/fixture.yaml`. `score.automated.json` was not used as ground truth.

Scorers:

- Scorer A: product
- Scorer B: engineering

## Surface scores

| Fixture | Scorer | Interview | Batch selection | Briefs | Tags | Chat | Sweep reasoning | UX quality |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| coding_novice_sparse_bugfix | A | 3.0 | 2.5 | 2.5 | 2.5 | 3.0 | 2.5 | 3.0 |
| coding_novice_sparse_bugfix | B | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| writing_novice_dense_launch | A | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 |
| writing_novice_dense_launch | B | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 | 2.0 | 2.5 |
| operations_expert_noisy_incident | A | 3.0 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 |
| operations_expert_noisy_incident | B | 3.5 | 3.0 | 3.0 | 3.0 | 3.0 | 2.5 | 3.0 |

## Overall composites

All major efficiency metrics were within the fixture target bands, so each scorer used an efficiency multiplier of `1.00`.

| Fixture | A surface weighted | A multiplier | A overall | B surface weighted | B multiplier | B overall | Mean overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| coding_novice_sparse_bugfix | 2.675 | 1.00 | 2.675 | 3.000 | 1.00 | 3.000 | 2.838 |
| writing_novice_dense_launch | 2.000 | 1.00 | 2.000 | 2.425 | 1.00 | 2.425 | 2.213 |
| operations_expert_noisy_incident | 2.575 | 1.00 | 2.575 | 3.000 | 1.00 | 3.000 | 2.788 |

## Agreement within 1 point

Agreement is counted across the seven scored surface fields.

| Fixture | Fields within 1 point | Agreement | Max delta | Needs rubric calibration | Notes |
|---|---:|---:|---:|---|---|
| coding_novice_sparse_bugfix | 7 / 7 | 100% | 0.5 | No | Product was stricter on the missed README/docs entry and generic sweep; engineering gave more credit for source-traceable core coding entries. |
| writing_novice_dense_launch | 7 / 7 | 100% | 0.5 | No | Both scorers capped the run for writing-mode mismatch; product weighted the novice launch-copy terminology drift more heavily. |
| operations_expert_noisy_incident | 7 / 7 | 100% | 0.5 | No | Both scorers penalized omission of action owners; engineering credited the concise expert interview and causal caution more strongly. |

## Calibration notes

| Theme | Note |
|---|---|
| Efficiency multiplier | All three runs met their fixture targets for turns_to_useful_charter, time_to_first_queue_ms, redundant_token_rate, manual_correction_count, and perceived_load_1_7, so no efficiency penalty was applied. |
| Shared queue limiter | Each run omitted one expected queue item while capacity remained: README usage note for coding, email tone mismatch for writing, and action owners for operations. This capped batch selection and downstream sweep quality. |
| Template drift | The writing run shows the clearest mode mismatch: CI language appears in the transcript and "behavior and verification entries" appears in the sweep insight. Operations also has generic behavior/verification language in the sweep. |
| Scorer lens difference | Scorer A applied a stricter product-fit lens to persona, terminology, and launch/incident workflow coherence. Scorer B gave more credit where source traceability, risk ordering, and compact technical structure were present. |
| Calibration threshold | No surface score differed by 2 or more points, so none of these runs requires rubric calibration under the intercoder protocol. |
