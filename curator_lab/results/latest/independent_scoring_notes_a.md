# Independent scoring notes - Scorer A

Scorer: `scorer_a`  
Role: product  
Phase: independent

| Fixture | Overall | Surface weighted | Efficiency multiplier | Main reason |
|---|---:|---:|---:|---|
| `coding_novice_sparse_bugfix` | 3.675 | 3.675 | 1.00 | Strong interview/queue traceability and source-grounded coding briefs; deductions for terse briefs and generic sweep depth. |
| `writing_novice_dense_launch` | 3.125 | 3.125 | 1.00 | Relevant risk-ordered launch copy queue, but weak channel taxonomy and generic/coding-flavored sweep synthesis. |
| `operations_expert_noisy_incident` | 3.450 | 3.450 | 1.00 | Good expert/noisy interview and queue signal extraction; tags and sweep lack incident-specific owner/severity/causality synthesis. |

## Calibration notes

- I treated the artifacts in `run.json` as observable desk state and `transcript.txt` as the visible founding conversation. I did not use `score.automated.json` for scoring.
- The simplified `score.independent.blank.json` schema has fewer evidence subfields than the rubric's YAML template, so precision/recall/tag correction details are summarized in each surface's `notes`.
- I used half-points where a surface met the usable-baseline descriptor and had some strong structure, but still had generic simulator copy or missing domain-specific judgment hooks.
- I assigned an efficiency multiplier of 1.00 for all three runs because the recorded metrics show no blocked waits, quick useful-charter/queue times, and no obvious major efficiency miss. The rubric does not define fixture-specific numeric target bands, so this remains a calibration area.
- I did not mark categorical `mode_mismatch` for writing or operations because the queue/brief/tag surfaces mostly match the project type. I captured the coding-flavored sweep phrase ("behavior and verification entries") as a surface-score deduction instead.
- Sweep scoring was the hardest calibration point: the artifacts expose flags for traceability and decision-state preservation, but the actual insight text is short and generic. I weighted visible synthesis quality more heavily than the boolean fields.
