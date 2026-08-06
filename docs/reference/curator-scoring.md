# Curator agent UX scoring rubric

This rubric scores Kettle's curator agent UX for a local-first review desk:
agent work -> curated queue -> read/edit/comment/approve -> sweep.

Use it for automated demo runs, comparative model/provider runs, and manual
review sessions. Score observable behavior only: prompts shown, entries queued,
briefs, tags, chat transcript, approvals/comments, sweep output, timings, and
token logs. Do not give credit for intent that is not visible in artifacts.

## Score scale conventions

All surface areas are scored independently from 0 to 5.

| Score | Meaning |
|---:|---|
| 0 | Missing, unusable, unsafe, or actively misleading. |
| 1 | Present but brittle; requires substantial human repair. |
| 2 | Partly useful; important gaps, noise, or inconsistency remain. |
| 3 | Usable baseline; supports the workflow with tolerable friction. |
| 4 | Strong; accurate, economical, and reliable across common cases. |
| 5 | Excellent; anticipatory, calibrated, and consistently improves curator judgment. |

Half-points are allowed when evidence sits between adjacent descriptors. Record
the reason in scoring notes.

## 1. Interview: founding interview quality

Measures how well the initial curator interview establishes a project charter,
review norms, priorities, and desk behavior.

| Score | Descriptor |
|---:|---|
| 0 | No founding interview, or it fabricates charter facts without user input. |
| 1 | Asks generic questions that do not map to Kettle decisions; misses project purpose, audience, risk, or review standards. |
| 2 | Captures some facts but leaves major ambiguities; over-asks low-value questions; produces an incomplete or weakly grounded charter. |
| 3 | Establishes a usable charter covering purpose, audience/user, desired outputs, review criteria, exclusions, and first queue shape. |
| 4 | Efficiently elicits high-signal information, confirms assumptions, resolves conflicts, and produces a charter that directly governs queue, briefs, tags, and sweep. |
| 5 | Feels like an expert setup partner: adapts question depth to the user, surfaces hidden tradeoffs, captures decision rules with examples/non-examples, and creates a charter the user rarely needs to revise. |

Scoring notes:

- Reward concise questions that change later behavior.
- Penalize interview length when answers are not used downstream.
- Penalize leading questions that bias the user toward a specific workflow.
- Check charter traceability: at least 80% of queue/tag/brief decisions should
  be explainable from charter fields or explicit user follow-up at scores 4-5.
- A score above 3 requires both elicitation quality and a usable resulting
  charter, not just pleasant conversation.

## 2. Batch selection: what enters and how the queue is shaped

Measures the curator's ability to select, order, group, and size queue entries
from available agent output.

| Score | Descriptor |
|---:|---|
| 0 | Queue is empty when useful work exists, includes unrelated/harmful material, or loses source traceability. |
| 1 | Queue is mostly a dump of raw agent output; many duplicates, stale items, or wrong-granularity entries. |
| 2 | Selects some relevant entries but misses important work, overloads the user, or mixes incompatible review intents in one batch. |
| 3 | Produces a workable queue with relevant entries, understandable ordering, limited duplication, and a batch size a curator can review. |
| 4 | Shapes the batch around priority, risk, dependencies, novelty, and user capacity; separates approve-now items from investigate/edit/comment items. |
| 5 | Curates like a senior desk editor: maximizes review value per item, explains omissions, preserves optional depth, and adapts batch strategy from prior approvals/comments. |

Scoring notes:

- Evaluate precision, recall, ordering, and granularity separately before
  assigning the single score.
- Penalize hidden filtering: omitted high-risk or user-requested work must be
  named or discoverable.
- Good batches are not always small. They are sized to the fixture's curator
  capacity and item complexity.
- For coding fixtures, include risky diffs, tests, migrations, config, generated
  artifacts, and unresolved CI failures when relevant.
- For writing fixtures, include thesis changes, factual claims, tone decisions,
  structure, source gaps, and publication blockers when relevant.

## 3. Briefs: entry brief quality

Measures whether each queue entry gives the curator enough context to decide,
edit, comment, or approve without re-reading all raw agent output.

| Score | Descriptor |
|---:|---|
| 0 | Briefs absent, wrong, or detached from the queued artifact. |
| 1 | Briefs restate titles or raw output with little decision context; frequent hallucinated claims. |
| 2 | Briefs include useful context but are incomplete, verbose, inconsistent, or weak on evidence and risks. |
| 3 | Each brief states what changed, why it matters, source/evidence, likely curator decision, and known caveats. |
| 4 | Briefs are concise, source-grounded, decision-oriented, and tailored to the entry type; they expose uncertainty and next action clearly. |
| 5 | Briefs materially improve judgment: they frame tradeoffs, identify hidden dependencies, offer precise edit/comment hooks, and remain faithful under dense or messy input. |

Scoring notes:

- Sample at least 10 briefs or all briefs if fewer than 10.
- Penalize unsupported certainty, especially for code behavior, factual claims,
  external references, and inferred user intent.
- A score above 3 requires source pointers or evidence labels sufficient for a
  reviewer to verify the brief quickly.
- Strong briefs should answer: "What am I approving?", "What could be wrong?",
  and "What is the lowest-friction next action?"

## 4. Tags

Measures tag taxonomy, accuracy, consistency, and usefulness for filtering,
batch shaping, and sweep synthesis.

| Score | Descriptor |
|---:|---|
| 0 | No tags, unusable tags, or tags that obscure important review state. |
| 1 | Tags are ad hoc, inconsistent, redundant, or mostly decorative. |
| 2 | Tags capture some useful categories but have weak definitions, poor coverage, or frequent misclassification. |
| 3 | Tags consistently encode review-relevant dimensions such as domain, risk, action, status, and confidence. |
| 4 | Tag set is compact, well-defined, accurate, and useful for filtering, prioritizing, and sweep reasoning. |
| 5 | Tags become an operating system for the desk: stable taxonomy, calibrated confidence/risk, good cross-entry grouping, and low manual correction rate. |

Scoring notes:

- Prefer few high-value tags over many vague tags.
- Measure tag correction rate: score 4-5 usually requires less than 10% manual
  corrections on fixture runs.
- Penalize synonyms that fragment filters, such as `docs`, `documentation`, and
  `writing` when they mean the same thing.
- Useful tag dimensions commonly include `domain`, `artifact_type`, `risk`,
  `action_needed`, `confidence`, `source`, and `sweep_topic`.
- Tags should not leak provider internals unless those internals affect review.

## 5. Chat: ongoing curator conversation

Measures how the curator agent behaves after founding while the user reads,
edits, comments, approves, asks questions, and changes priorities.

| Score | Descriptor |
|---:|---|
| 0 | Chat is unavailable, ignores user input, or makes unsafe changes without confirmation. |
| 1 | Chat answers are generic, lose context, interrupt the workflow, or conflict with visible desk state. |
| 2 | Chat can answer simple questions but struggles with continuity, specificity, brevity, or translating decisions into desk updates. |
| 3 | Chat is useful for common curator moves: explain an entry, compare options, capture a comment, revise tags/briefs, and clarify next steps. |
| 4 | Chat maintains context across the sitting, asks targeted questions only when needed, reflects approvals/comments accurately, and keeps the user oriented. |
| 5 | Chat feels like a calm co-curator: anticipates likely needs, supports reversible decisions, adapts to expertise, and reduces cognitive load without hiding control. |

Scoring notes:

- Reward continuity with current entry, charter, prior comments, approvals, and
  sweep readiness.
- Penalize unsolicited broad rewrites, excessive reassurance, and modal chatter
  that blocks the review loop.
- The chat should state uncertainty and propose local, reversible actions.
- A score above 3 requires correct use of visible desk state, not just a good
  standalone answer.

## 6. Sweep reasoning and insights

Measures how well the final sweep uses approvals, edits, comments, rejected
items, and desk context to produce faithful reasoning and useful synthesis.

| Score | Descriptor |
|---:|---|
| 0 | Sweep reasoning absent, fabricates decisions, or contradicts approved desk state. |
| 1 | Sweep mostly lists items; weak link to approvals/comments; misses blockers or applies wrong conclusions. |
| 2 | Sweep summarizes some decisions but loses nuance, overgeneralizes, or fails to distinguish approved, deferred, and rejected work. |
| 3 | Sweep faithfully summarizes what was approved/commented, explains main reasoning, identifies remaining work, and preserves traceability. |
| 4 | Sweep synthesizes cross-entry patterns, risks, and next actions while staying grounded in curator decisions. |
| 5 | Sweep produces durable desk intelligence: high-signal insights, reusable decision rules, unresolved questions, and a clean handoff for the next agent/user loop. |

Scoring notes:

- Faithfulness is a gate: hallucinated approvals or changed user intent cap the
  score at 2.
- Reward insight density, not length.
- Good sweep reasoning distinguishes evidence, inference, and recommendation.
- For code, sweep should mention tests/CI, risks, file areas, and follow-up
  changes. For writing, it should mention thesis, factual risk, tone, structure,
  publication state, and source gaps.

## Efficiency metrics

Efficiency scores do not replace the six surface scores. Record them alongside
surface scores and use them to explain deltas between runs.

### Token metrics

| Metric | Definition | Preferred direction |
|---|---|---:|
| `total_tokens` | Sum of input, output, tool, and cached-context tokens for the sitting. | Lower for same quality |
| `tokens_to_useful_charter` | Tokens until the first charter that a scorer rates at least 3 for interview quality. | Lower |
| `tokens_per_approved_entry` | `total_tokens / max(approved_entries, 1)`. | Lower |
| `brief_tokens_per_entry` | Mean brief token count per queued entry. | Calibrated |
| `redundant_token_rate` | Estimated percent of repeated or non-decision-bearing text in agent messages. | Lower |
| `evidence_token_ratio` | Tokens that cite or summarize source evidence divided by total brief+sweep tokens. | Higher until concise |

Notes:

- Do not reward token minimization that lowers surface scores.
- Briefs below useful context should be penalized through the Briefs score, not
  celebrated as efficient.
- Track p50/p90 tokens per fixture family; regressions above 20% require an
  explanation or quality gain.

### Wall-clock metrics

| Metric | Definition | Preferred direction |
|---|---|---:|
| `time_to_first_question_ms` | Page ready to first high-signal founding question. | Lower |
| `time_to_useful_charter_ms` | Start of founding to first charter rated at least 3. | Lower |
| `time_to_first_queue_ms` | Charter acceptance to first usable queue. | Lower |
| `median_entry_open_latency_ms` | Median latency to open an entry with brief/tags. | Lower |
| `sweep_latency_ms` | Sweep request to usable sweep result. | Lower |
| `review_session_wall_clock_ms` | Full demo run duration, excluding scorer deliberation. | Lower for same quality |

Report p50 and p90. A run that blocks the curator without visible progress for
more than 10 seconds should record a `blocked_wait_event`.

### Turns-to-useful-charter

`turns_to_useful_charter` is the count of user-agent exchanges from first
founding prompt to the first charter that independently scores at least 3 on the
Interview rubric.

Targets:

- 1-2 turns: excellent when user input is already dense.
- 3-5 turns: acceptable for ambiguous projects.
- More than 5 turns: inspect whether questions were redundant, low-signal, or
  better handled as defaults with confirmation.

### Cognitive load proxies

Record these because cognitive load is hard to measure directly:

| Proxy | Definition | Preferred direction |
|---|---|---:|
| `user_clarification_count` | Times the user had to explain what the agent should already know from visible context. | Lower |
| `manual_correction_count` | Edits to charter, queue membership, briefs, tags, or sweep caused by curator error. | Lower |
| `attention_switch_count` | Required switches to raw logs, files, external tabs, or unrelated panels to make one decision. | Lower |
| `unresolved_question_count` | Open questions left without ownership or next action. | Lower |
| `average_decision_text_length` | Mean characters the user must read per approve/comment decision, including brief and chat. | Calibrated |
| `scroll_depth_per_entry` | Mean screens scrolled before decision. | Lower for same quality |
| `user_reversal_count` | Times the user reverses a decision after discovering missed context. | Lower |
| `perceived_load_1_7` | Optional scorer/user rating, 1 = effortless, 7 = exhausting. | Lower |

## Adaptability evaluation

Score adaptability as an annotation for each run, then inspect whether any
surface score systematically drops for specific fixture axes.

### Project type: coding vs writing

Coding projects should show:

- diff-aware batch selection by risk, dependency, tests, and config impact;
- briefs with file paths, behavior claims, test status, and unresolved failures;
- tags for area, change type, risk, confidence, and action needed;
- sweep that preserves what was approved versus what still requires CI/manual
  verification.

Writing projects should show:

- selection by thesis impact, section structure, factual risk, tone, audience,
  and publication blockers;
- briefs with claim/evidence status, intended reader effect, and edit hooks;
- tags for section, topic, claim risk, tone, source status, and action needed;
- sweep that synthesizes argument shape, style decisions, source gaps, and next
  editorial moves.

### User expertise: novice vs expert

Novice users need:

- fewer assumptions, more explanations of Kettle concepts, and reversible
  recommendations;
- visible "why this matters" in briefs;
- lower jargon density and clearer next actions.

Expert users need:

- shorter prompts, denser briefs, precise controls, fewer confirmations, and
  access to raw evidence;
- respect for project-specific terminology;
- chat that answers direct questions without tutorializing.

### Agent-output density: sparse vs dense

Sparse agent output requires:

- uncertainty labels;
- targeted follow-up questions;
- conservative queue inclusion;
- clear distinction between absence of evidence and negative evidence.

Dense agent output requires:

- aggressive deduplication;
- grouping by decision/risk;
- summaries that preserve traceability;
- surfaced conflicts and hidden dependencies.

Adaptability flags:

- `mode_mismatch`: UX treats coding as writing or writing as coding.
- `expertise_mismatch`: UX over-explains to experts or under-explains to novices.
- `density_mismatch`: UX either invents detail for sparse output or overwhelms
  the user with dense output.
- `charter_drift`: later behavior ignores founding preferences.

## Charm, consistency, and UX quality

This subjective dimension is recorded separately as `ux_quality_0_5`. It should
not hide functional defects in the six surface scores.

| Score | Descriptor |
|---:|---|
| 0 | Hostile, confusing, erratic, or trust-breaking. |
| 1 | Awkward and inconsistent; visible copy or behavior regularly distracts from review. |
| 2 | Serviceable but bland, noisy, or uneven; occasional tone/control mismatch. |
| 3 | Clear and steady; copy, controls, and interaction rhythm support the loop. |
| 4 | Polished and distinctive; local-first control, calm pacing, and terminology feel coherent. |
| 5 | Memorable without being cute; every detail reinforces trust, agency, and desk craft. |

Scoring notes:

- Evaluate charm as disciplined product feel, not entertainment.
- Penalize personality that obscures decisions or makes errors harder to see.
- Consistency includes terminology: queue entry, brief, tag, comment, approve,
  sweep, charter, and desk should not drift across surfaces.

### Intercoder reliability protocol

Use at least two independent scorers per benchmark run.

1. Both scorers receive the same artifacts, fixture definition, scoring sheet,
   and rubric. They score independently before discussion.
2. For each 0-5 surface score, record both raw scores and notes.
3. Agreement is counted when scores differ by no more than 1 point.
4. Target simple percent agreement: at least 85% of scored fields within 1 point.
5. For categorical flags such as `mode_mismatch`, `density_mismatch`, and
   `critical_failure`, target Cohen's kappa >= 0.70.
6. Resolve disagreements by reviewing evidence, not preference. The final score
   is the average of independent scores unless a documented artifact error or
   rubric misread is found.
7. If any surface differs by 2 or more points after discussion, keep both notes
   and mark `needs_rubric_calibration: true`.

## Overall composite score

Compute the composite from independently scored dimensions. Do not compute a
composite when any critical failure is present.

Critical failures:

- fabricated user approval, source evidence, file state, or sweep result;
- non-local or irreversible action without explicit user approval;
- queue loses source traceability;
- private or sensitive data is exposed outside the local review context;
- user cannot inspect or reverse curator decisions.

Weights:

| Component | Weight |
|---|---:|
| Interview | 15% |
| Batch selection | 20% |
| Briefs | 20% |
| Tags | 10% |
| Chat | 15% |
| Sweep reasoning / insights | 15% |
| Charm / consistency / UX quality | 5% |

Formula:

```text
surface_weighted_score =
  0.15 * interview +
  0.20 * batch_selection +
  0.20 * briefs +
  0.10 * tags +
  0.15 * chat +
  0.15 * sweep_reasoning +
  0.05 * ux_quality

efficiency_multiplier =
  1.00                       if efficiency is within fixture target bands
  0.95                       if one major efficiency metric misses target
  0.90                       if two or more major efficiency metrics miss target
  0.80                       if the run is functionally usable but routinely stalls

overall_score_0_5 = surface_weighted_score * efficiency_multiplier
```

Justification:

- Batch selection and briefs carry the most weight because they define the
  curator's day-to-day review leverage.
- Interview is important because it governs setup and later behavior, but it is
  episodic.
- Chat and sweep reasoning are each high-impact but should not compensate for a
  poor queue or poor briefs.
- Tags receive less weight because they are enabling structure; severe tag
  failures should still appear through batch, brief, chat, and sweep scores.
- Charm/consistency is included to protect product quality, but it cannot mask
  functional failure.
- Efficiency is a multiplier so slow or wasteful behavior can lower an otherwise
  competent experience without rewarding terse low-quality output.

## Benchmark goals

Run the benchmark matrix on every continuous improvement round. Compare against
the same fixture set, scorer pool, and instrumentation.

### Baseline assumption: mediocre first prototype

Expected profile:

- Interview: 2.0-3.0. Captures basics but asks too much and underuses answers.
- Batch selection: 2.0-3.0. Relevant queue, weak prioritization/deduplication.
- Briefs: 2.0-3.0. Helpful summaries, uneven evidence and action framing.
- Tags: 1.5-2.5. Inconsistent taxonomy and correction rate above 20%.
- Chat: 2.0-3.0. Answers questions but loses desk continuity.
- Sweep reasoning: 2.0-3.0. Summarizes items, limited synthesis.
- UX quality: 2.0-3.0. Clear enough but not yet distinctive.
- Overall composite after efficiency multiplier: 2.3-3.0.

### Excellent curator target

Ambitious but achievable continuous-improvement goal:

- Every critical fixture scores at least 3.5 overall.
- Matrix mean overall score >= 4.2.
- No surface-area mean below 4.0.
- No individual surface score below 3.0 unless a fixture intentionally withholds
  required evidence.
- `turns_to_useful_charter` p50 <= 3 and p90 <= 5.
- `time_to_first_queue_ms` p90 within the fixture target band.
- Tag manual correction rate <= 10%.
- Brief hallucination rate <= 2% of sampled briefs.
- Simple scorer agreement >= 85% within 1 point; categorical Cohen's kappa >=
  0.70.

Stretch goal for "excellent curator":

- Matrix mean overall score >= 4.5.
- p90 `perceived_load_1_7` <= 3.
- At least 80% of sweep outputs contain one or more scorer-validated insights
  that were not explicitly listed in a single source item but are traceable to
  multiple approved/commented entries.

## Demo scenario matrix

Use at least these six persona x project fixtures for automated demo runs. Each
fixture should include founding inputs, raw agent output, expected high-value
queue inclusions, expected omissions, and scorer answer keys.

| Fixture ID | Persona | Project | Agent output density | Primary stress | Expected curator behavior |
|---|---|---|---|---|---|
| `coding_novice_sparse_bugfix` | Novice maintainer | Small Python CLI bugfix | Sparse | Needs explanation and uncertainty handling | Ask clarifying founding questions, queue risky files/tests, brief behavior impact plainly, avoid inventing CI status. |
| `coding_expert_dense_refactor` | Expert staff engineer | TypeScript refactor with tests/config | Dense | Deduplication and risk ordering | Group related diffs, surface config/test risk, keep briefs terse, expose raw evidence and unresolved failures. |
| `coding_novice_dense_dependency` | Novice founder | Web app dependency/security update | Dense | Jargon control and safety | Prioritize security/runtime risk, explain lockfile/config effects, tag migration risk, preserve reversible decisions. |
| `writing_expert_sparse_strategy` | Expert operator | Strategic memo revision | Sparse | Missing evidence and concise editorial judgment | Identify claim gaps, ask few targeted questions, avoid padding, tag thesis/source/tone risks. |
| `writing_novice_dense_launch` | Novice marketer | Product launch copy package | Dense | Audience/tone consistency | Group by channel/audience, brief tone and claim risks, explain approval choices, sweep into launch-ready checklist. |
| `hybrid_expert_dense_docs_code` | Expert open-source maintainer | Docs plus code examples | Dense | Cross-artifact consistency | Link code changes to docs claims, tag examples/API risk, catch mismatch between implementation and prose. |
| `hybrid_novice_sparse_research` | Novice researcher | Notebook plus narrative report | Sparse | Distinguishing evidence from inference | Queue result claims separately from prose edits, label uncertainty, ask for source priority, sweep unresolved validation steps. |
| `operations_expert_noisy_incident` | Expert SRE | Incident review and runbook update | Dense/noisy | Signal extraction from logs and notes | Prioritize timeline/causal claims/action items, tag ownership and severity, avoid false causality in sweep. |

Minimum matrix coverage:

- at least 3 coding or hybrid fixtures;
- at least 3 writing or hybrid fixtures;
- at least 3 novice fixtures;
- at least 3 expert fixtures;
- at least 2 sparse-output fixtures;
- at least 3 dense or noisy-output fixtures.

## Machine-readable scoring worksheet template

Use this YAML template for each scorer's independent pass. Store final resolved
scores in a separate file or mark `phase: resolved`.

```yaml
schema_version: 1
product: kettle
rubric: curator_agent_ux
phase: independent # independent | resolved
run:
  run_id: ""
  fixture_id: ""
  fixture_version: ""
  created_at: ""
  model_or_agent_version: ""
  provider: ""
  commit_sha: ""
  scorer_id: ""
  scorer_role: "" # product | engineering | design | research | other

artifacts:
  transcript_uri: ""
  desk_snapshot_uri: ""
  token_log_uri: ""
  timing_log_uri: ""
  raw_agent_output_uri: ""
  notes_uri: ""

surface_scores:
  interview:
    score: null # 0..5, half-points allowed
    evidence:
      - ""
    notes: ""
  batch_selection:
    score: null
    precision_notes: ""
    recall_notes: ""
    ordering_notes: ""
    granularity_notes: ""
    evidence:
      - ""
    notes: ""
  briefs:
    score: null
    sampled_count: 0
    hallucinated_or_unsupported_count: 0
    evidence:
      - ""
    notes: ""
  tags:
    score: null
    sampled_count: 0
    manual_correction_count: 0
    evidence:
      - ""
    notes: ""
  chat:
    score: null
    evidence:
      - ""
    notes: ""
  sweep_reasoning:
    score: null
    evidence:
      - ""
    notes: ""
  ux_quality:
    score: null
    evidence:
      - ""
    notes: ""

efficiency:
  total_tokens: null
  tokens_to_useful_charter: null
  tokens_per_approved_entry: null
  brief_tokens_per_entry_mean: null
  redundant_token_rate: null
  evidence_token_ratio: null
  time_to_first_question_ms: null
  time_to_useful_charter_ms: null
  time_to_first_queue_ms: null
  median_entry_open_latency_ms: null
  sweep_latency_ms: null
  review_session_wall_clock_ms: null
  turns_to_useful_charter: null
  blocked_wait_events: 0

cognitive_load:
  user_clarification_count: 0
  manual_correction_count: 0
  attention_switch_count: 0
  unresolved_question_count: 0
  average_decision_text_length: null
  scroll_depth_per_entry: null
  user_reversal_count: 0
  perceived_load_1_7: null

adaptability:
  project_type: "" # coding | writing | hybrid | operations | other
  user_expertise: "" # novice | expert
  agent_output_density: "" # sparse | moderate | dense | noisy
  flags:
    mode_mismatch: false
    expertise_mismatch: false
    density_mismatch: false
    charter_drift: false
  notes: ""

critical_failures:
  fabricated_approval: false
  fabricated_source_or_file_state: false
  non_local_or_irreversible_action: false
  lost_source_traceability: false
  sensitive_data_exposure: false
  cannot_inspect_or_reverse: false
  notes: ""

composite:
  efficiency_multiplier: null # 1.00 | 0.95 | 0.90 | 0.80
  surface_weighted_score: null
  overall_score_0_5: null
  computed_by: "" # scorer | script
  notes: ""

intercoder:
  paired_scorer_id: ""
  agreement_within_one_point: null
  categorical_agreement_notes: ""
  cohens_kappa_for_flags: null
  needs_rubric_calibration: false

freeform_notes: ""
```
