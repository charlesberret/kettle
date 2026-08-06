# Curator optimization frameworks

Kettle can optimize the curator in several plausible ways. The choice matters
because it determines what the opening interview feels like, what memory is
allowed to become durable, and how the review surfaces improve over time.

This document compares three frameworks:

- **A. Charter-First**: structured interview -> durable charter -> light
  learning.
- **B. Signal-First**: minimal interview -> aggressive learning from rulings and
  edits -> proposed memory updates.
- **C. Hybrid Desk Notebook**: artifact scan plus short Socratic interview ->
  dual-layer memory -> evidence-backed learning with promotion gates -> optional
  voice calibration.

The recommendation is **C. Hybrid Desk Notebook**. It gives Kettle the strongest
path to excellent curator behaviour while preserving the local-first, ordinary
file, approve-is-not-publish constraints.

For measurement, use the
[curator scoring rubric](../reference/curator-scoring.md). This document maps
each framework to that benchmark; it does not restate the formula.

## A. Charter-First

Charter-First treats founding as the main design moment. The curator asks a
structured set of questions, writes a durable charter, and then uses that charter
as the primary source of later behaviour. Learning from rulings exists, but it is
conservative and usually limited to proposed edits to the charter.

### Founding flow

1. Show a short explanation of the review loop: queue, brief, tag, comment,
   approve, sweep.
2. Ask structured questions:
   - project purpose;
   - intended audience or user;
   - reviewer role;
   - acceptable output;
   - high-risk material;
   - exclusions;
   - preferred batch size;
   - tag dimensions;
   - brief style;
   - sweep goal.
3. Generate a charter and ask the user to confirm or edit it.
4. Build the first batch only after charter acceptance.

This is easy to explain and easy to score. It risks making setup feel heavier
than the first review sitting.

### Memory model

```text
.kettle/
  curator/
    charter.md
    tag-taxonomy.md
    brief-style.md
    voice.md
    memory-proposals/
      0001-prefer-risk-first-batches.md
    sittings/
      2026-08-06.md
```

The durable charter is the primary memory. Sitting notes summarize what happened
but do not automatically change standing behaviour. Memory proposals are rare
and framed as charter amendments.

### Surface behaviour

| Surface | Behaviour |
|---|---|
| Interview | Strongest surface. The interview is explicit, structured, and produces a clear charter. |
| Batch | Uses charter fields for inclusion, ordering, grouping, and batch size. Slow to adapt if the first charter was wrong. |
| Briefs | Consistent because brief style is declared up front. May miss learned nuance from later edits. |
| Tags | Stable taxonomy from founding. Low synonym drift, but can be overfit to early assumptions. |
| Chat | Answers from the charter and current sitting. Usually asks before revising memory. |
| Sweep | Summarizes against charter goals. Good traceability, weaker emergent insight. |

### Token profile

Charter-First spends more tokens before the first queue. Later sittings are
economical because the charter is compact and stable. The risk is wasted setup
tokens when the user gives sparse answers or when the first artifacts would have
revealed better questions.

### Failure modes

- The interview asks many questions that do not change downstream behaviour.
- The user confirms a vague charter to get moving, causing weak batch decisions.
- The curator over-trusts the charter and underuses actual rulings.
- The system feels bureaucratic for expert users who already have visible
  artifacts.

### Fit to user types

Charter-First fits users who want explicit control, predictable behaviour, and a
clear setup artifact before review begins. It is weaker for users who prefer to
start from visible work, teach by correction, or run short exploratory sittings.

## B. Signal-First

Signal-First minimizes founding. The curator asks one or two questions, starts a
batch quickly, and treats approvals, comments, edits, tag corrections, skipped
entries, and reversals as the main source of learning. It proposes memory updates
frequently.

### Founding flow

1. Scan available artifacts and agent output.
2. Ask only a small number of questions:
   - "What should this sitting optimize for?"
   - "Anything I should exclude or treat as high risk?"
3. Create the first queue immediately.
4. Watch rulings closely and infer candidate preferences from them.
5. After enough evidence, propose memory updates.

This produces value quickly. It also puts more pressure on later governance
because early behaviour is intentionally under-specified.

### Memory model

```text
.kettle/
  curator/
    observed-signals.jsonl
    inferred-preferences.md
    memory-proposals/
      0001-risk-tags-from-corrections.md
      0002-terse-briefs-from-edits.md
    sittings/
      2026-08-06/
        ephemeral.md
        rulings.jsonl
        sweep-notes.md
```

The event stream is central. The charter may be thin or generated only after the
first sitting. Candidate preferences are more prominent than standing project
rules.

### Surface behaviour

| Surface | Behaviour |
|---|---|
| Interview | Short and low-friction. Can under-elicit purpose, audience, exclusions, or risk. |
| Batch | Improves rapidly when the user makes many rulings. Starts weaker on sparse input. |
| Briefs | Learns from edits and comments. Can chase local style corrections too aggressively. |
| Tags | Adapts from tag corrections. Vulnerable to taxonomy churn and overfitting. |
| Chat | Highly responsive to recent behaviour. May claim familiarity before it is earned. |
| Sweep | Can synthesize fresh patterns well, but may confuse transient sitting signals with durable decisions. |

### Token profile

Signal-First has the lowest tokens to first queue. It can spend more tokens later
explaining inferred preferences, resolving contradictions, and asking whether to
promote memory. Poor governance can make the total sitting more expensive than
Charter-First.

### Failure modes

- Premature personalization from too little evidence.
- Hidden preference drift when proposals are accepted casually or not shown.
- Recency bias: the last correction outweighs the project purpose.
- Noisy event logs that are hard for humans to inspect.
- Inconsistent tags and briefs while the system is still learning.

### Fit to user types

Signal-First fits expert users who want momentum, generate many rulings, and are
comfortable teaching the system by correction. It is risky for novices, sparse
projects, high-stakes review, or any user who expects the curator to explain its
decision rules before acting.

## C. Hybrid Desk Notebook

Hybrid Desk Notebook starts from artifacts, asks a short Socratic interview,
writes a durable charter, keeps ephemeral sitting memory separate, and learns
from rulings through explicit promotion gates. It optionally calibrates voice
after the user has seen at least one useful batch.

This is the recommended framework.

### Founding flow

1. Scan visible project and Desk artifacts:
   - existing `.kettle/` state;
   - agent output;
   - diffs or files under review;
   - prior approvals, comments, tag corrections, and sweeps when present.
2. Form tentative assumptions with evidence labels.
3. Ask a short Socratic interview:
   - confirm purpose and audience;
   - resolve high-risk ambiguity;
   - ask what the first sitting should optimize for;
   - confirm exclusions and review boundaries;
   - ask only enough about brief/tag style to make the first queue useful.
4. Write a durable charter and show it as an editable Desk artifact.
5. Create the first batch.
6. During review, keep ephemeral sitting memory for current constraints and
   unresolved questions.
7. After repeated evidence, propose durable preference updates with examples.
8. Offer voice calibration only when it can improve briefs, chat, or sweep.

### Memory model

```text
.kettle/
  curator/
    charter.md
    preferences.md
    tag-taxonomy.md
    voice.md
    events/
      2026-08.jsonl
    sittings/
      2026-08-06/
        ephemeral.md
        queue-hypotheses.md
        rulings.jsonl
        sweep.md
    memory-proposals/
      0001-risk-first-when-config-changes.md
      0002-briefs-should-include-source-gaps.md
```

The layout separates durable and ephemeral memory:

- `charter.md` holds confirmed project purpose, audience, review criteria,
  exclusions, batch defaults, and sweep intent.
- `preferences.md` holds accepted procedural preferences with evidence links.
- `tag-taxonomy.md` defines compact tag dimensions and examples.
- `voice.md` is optional and small.
- `events/*.jsonl` records inspectable event history.
- `sittings/*/ephemeral.md` expires or is summarized after the sitting.
- `memory-proposals/*` contains candidate updates waiting for user action.

### Surface behaviour

| Surface | Behaviour |
|---|---|
| Interview | Uses artifact evidence to ask fewer, better questions; produces a charter the user can inspect and edit. |
| Batch | Combines charter rules, artifact evidence, and recent sitting constraints; adapts from accepted preferences without hiding omissions. |
| Briefs | Grounds each brief in source evidence and known review criteria; adjusts style only through confirmed preference or current sitting constraint. |
| Tags | Starts with a compact taxonomy, then learns corrections through promotion gates to avoid synonym drift. |
| Chat | Maintains current sitting context while distinguishing durable memory, fresh evidence, and speculation. |
| Sweep | Uses rulings and comments to synthesize cross-entry insights, propose memory updates, and preserve traceability. |

### Token profile

Hybrid has moderate setup cost and better long-run economy. The artifact scan
reduces generic interview tokens. The charter keeps standing context compact.
Ephemeral memory prevents the whole sitting transcript from being loaded on every
turn. Promotion gates add some tokens, but those tokens buy inspectability and
reduce later correction costs.

Important efficiency targets should come from the scoring rubric:
`turns_to_useful_charter`, `tokens_to_useful_charter`,
`tokens_per_approved_entry`, tag correction rate, brief hallucination rate, and
blocked waits.

### Failure modes

- The artifact scan over-infers user intent from file shape or previous agent
  output.
- The charter and preferences drift apart if accepted updates are not reconciled.
- Promotion prompts become noisy if every minor correction creates a proposal.
- Ephemeral memory is retained too long and becomes stale durable context.
- Voice calibration becomes personality instead of decision support.

These are governance problems, not reasons to avoid the framework. The remedies
are explicit evidence labels, proposal thresholds, expiry rules, and compact
files.

### Fit to user types

Hybrid fits the broadest range:

- **Novices** get visible explanations, reversible decisions, and a charter they
  can understand.
- **Experts** get artifact-aware questions, fewer setup turns, and concise
  controls.
- **Sparse projects** get conservative assumptions and targeted questions.
- **Dense projects** get deduplication, risk grouping, and traceable omissions.
- **Writing projects** get thesis, tone, source, and publication-state memory.
- **Coding projects** get diff, test, risk, config, and migration memory.

## Recommendation

Use **C. Hybrid Desk Notebook** as the product direction.

Charter-First is safer than Signal-First, but it spends too much of the user's
patience before the Desk has proved useful. Signal-First is exciting in demos,
but it asks the user to trust inferred familiarity before Kettle has earned it.

Hybrid gives Kettle a better bargain:

- setup questions are grounded in visible artifacts;
- the charter remains a durable, inspectable source of truth;
- current sitting state stays separate from long-term memory;
- preference learning compounds from real rulings;
- proposed memory updates are evidence-backed and reversible;
- optional voice calibration improves readability without becoming the product.

That shape also matches Kettle's public constraints. The Desk remains ordinary
files. Approve remains a local ruling, not publishing. The curator becomes more
familiar by showing its evidence and asking for promotion, not by silently
personalizing.

## Scoring map

All three frameworks should be evaluated with
[curator-scoring.md](../reference/curator-scoring.md). The comparison should use
the same fixture set, scorer pool, token logs, and artifacts for each framework.

| Rubric component | What to compare across frameworks |
|---|---|
| Interview | Turns to useful charter, question specificity, hidden assumption handling, and whether the resulting charter governs later surfaces. |
| Batch selection | Precision, recall, ordering, grouping, omission visibility, and adaptation from accepted preferences. |
| Briefs | Evidence grounding, decision orientation, brevity, uncertainty labels, and learned style without hallucination. |
| Tags | Taxonomy compactness, correction rate, synonym drift, confidence/risk usefulness, and promotion of corrected rules. |
| Chat | Continuity across the sitting, distinction between durable and ephemeral memory, and safe translation of user input into Desk updates. |
| Sweep reasoning / insights | Faithful use of approvals/comments, cross-entry synthesis, unresolved questions, and proposed memory updates with provenance. |
| Charm / consistency / UX quality | Whether the curator feels calm, local-first, and review-oriented across interview, queue, brief, tag, chat, and sweep. |
| Efficiency multiplier | Tokens to useful charter, tokens per approved entry, time to first queue, blocked waits, and repeated-context overhead. |

Expected scoring profile:

- **Charter-First** should score well on Interview and consistency, but may lose
  points on efficiency and adaptation.
- **Signal-First** should score well on time to first queue and adaptation after
  many rulings, but may lose points on Interview, Tags, and trust failures.
- **Hybrid Desk Notebook** should have the best path to the excellent curator
  target: no surface-area mean below 4.0, matrix mean overall score at least 4.2,
  low tag correction rate, low brief hallucination rate, and compact tokens per
  approved entry.

The benchmark should treat memory errors as product errors. If a framework
fabricates approval, loses source traceability, exposes private data outside the
local review context, or prevents inspection and reversal, it has hit a critical
failure regardless of charm or speed.
