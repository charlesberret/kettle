# Curator memory research

Kettle's curator is not a publisher, an autonomous merge bot, or a general
assistant. It is a local-first review desk: agent work becomes entries, entries
get briefs and tags, the reviewer reads, edits, comments, approves, and later
sweeps. Memory should improve that loop without hiding control.

The hard design problem is therefore not "how do we remember everything?" It is:
how does the curator become familiar enough to reduce repeated explanation while
keeping every consequential preference visible, revisable, and grounded in the
ordinary files of the Desk?

This brief compares approaches for the opening interview and for familiarity
over time. It recommends a hybrid for Kettle: artifact scan plus short Socratic
interview, durable charter plus ephemeral sitting memory, and evidence-backed
preference learning with promotion gates.

For scoring, use the separate
[curator scoring rubric](../reference/curator-scoring.md). This document explains
why the memory design should take that shape; it does not replace the benchmark.

## Design pressure

Kettle has several pressures that are easy to satisfy individually and hard to
satisfy together:

- **Local-first trust.** The Desk is ordinary inspectable files. Memory should be
  explainable as files, not only as provider-side state.
- **Low setup burden.** Founding a Desk should not feel like filling in an
  enterprise questionnaire.
- **Review leverage.** Memory is only useful when it changes batch selection,
  briefs, tags, chat, or sweep reasoning.
- **Reversibility.** A learned preference can be wrong. The user must be able to
  inspect, accept, edit, or reject it.
- **No publish confusion.** Approval records a local ruling. Memory may improve
  future review, but it must not imply outward execution.

These pressures make pure chat memory too implicit and pure structured setup too
heavy. Kettle needs a designed memory surface.

## Patterns worth borrowing

### MemGPT / Letta: two-tier memory and self-editing

MemGPT framed the context window as limited "main memory" and external stores as
longer-term memory, with the agent using functions to move information between
tiers ([MemGPT paper](https://arxiv.org/abs/2310.08560)). Letta's current
documentation keeps the same distinction in product terms: editable in-context
memory blocks, files, archival memory, and external retrieval stores
([Letta archival memory](https://docs.letta.com/guides/core-concepts/memory/archival-memory/),
[Letta context hierarchy](https://docs.letta.com/guides/core-concepts/memory/context-hierarchy/)).

Kettle should borrow the tiering, not the opacity. The curator needs a small
working set in prompt context, but durable project memory should live as Desk
files with provenance. A memory update is not just a vector insert; it is a
reviewable change to how the Desk will behave.

### Cursor rules: committed, scoped instructions

Cursor project rules are version-controlled `.mdc` files under `.cursor/rules`,
with frontmatter controlling whether a rule is always applied, matched by glob,
selected by description, or manually invoked
([Cursor rules](https://cursor.com/docs/rules)). The useful pattern is not the
file extension. It is the split between stable project guidance and contextual
loading.

For Kettle, durable curator memory should be similarly scoped. A project-wide
charter should always be available. Narrow preferences can be scoped to domains,
artifact types, or sweep topics so they do not pollute every decision.

### Claude Projects: instructions plus knowledge

Claude Projects combine project instructions, chat history, and a project
knowledge base. Anthropic's help docs describe projects as self-contained
workspaces with uploaded context and project-specific instructions; when project
knowledge approaches context limits, paid plans can use RAG to load relevant
content
([Claude Projects](https://support.anthropic.com/en/articles/9517075-what-are-projects),
[project management](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects)).

The Kettle lesson is separation of roles: instructions govern behaviour;
knowledge grounds answers. A curator charter should not become a dumping ground
for every artifact summary. Keep standing review rules separate from source
material and session notes.

### PROJECTMEM: local-first event-sourced judgment

PROJECTMEM describes a local-first, event-sourced memory and judgment layer for
AI coding agents. It stores issues, attempts, fixes, decisions, and notes in an
append-only plain-text event log, then projects compact summaries for agents and
uses deterministic gates to warn before repeated failed actions
([PROJECTMEM paper](https://arxiv.org/abs/2606.12329v1),
[projectmem.dev](https://projectmem.dev/)).

Kettle should borrow the event-sourced posture. Approval, comment, edit, tag
correction, and sweep are already events in spirit. Preference learning should
derive from those events, with provenance back to actual rulings, instead of
being treated as free-floating memory.

### Agentic memory in 2026: typed memory, not one bucket

Recent memory work separates episodic, semantic, and procedural memory and
emphasizes management loops that decide what to store, merge, prune, and recall.
AdMem, for example, describes a bi-level short-term/long-term memory system with
semantic, episodic, and procedural memories
([AdMem](https://arxiv.org/html/2606.06787v1)). A 2026 survey frames agent
memory around representation and management stages, including construction,
update, and query
([LLM Agent Memory survey](https://doi.org/10.20944/preprints202603.0359.v1)).

Kettle's memory types map naturally:

- **Episodic:** this sitting's approvals, comments, reversals, ignored entries,
  and unresolved questions.
- **Semantic:** durable facts about the project, audience, domain, exclusions,
  and source material.
- **Procedural:** how this reviewer wants batches shaped, briefs written, tags
  assigned, conflicts escalated, and sweeps summarized.

The mistake to avoid is mixing all three into one semantic index. A recent
approval is not the same kind of thing as a project fact or a standing rule.

### RAG versus structured memory

RAG is strong for searching broad unstructured material. It is weak as the only
memory system because it is usually stateless, approximate, and poor at temporal
or procedural reasoning. Current comparisons describe RAG as lookup over a
corpus, while memory systems add a write path for preferences, events, policies,
and state
([Oracle: RAG to memory systems](https://blogs.oracle.com/developers/from-rag-to-memory-systems-building-stateful-ai-architecture),
[Atlan: memory system vs RAG](https://atlan.com/know/ai-memory-system-vs-rag/)).

Kettle should use retrieval for artifacts and supporting evidence, but structured
files for things the reviewer has effectively decided. "The reviewer rejected
three low-evidence tone rewrites" is not just another chunk to embed. It is
evidence for a possible procedural preference, and it needs confidence,
provenance, and promotion rules.

## Opening interview approaches

### Structured charter

A structured charter asks for explicit fields: project purpose, audience,
reviewer role, acceptable output, risk tolerance, exclusions, tag preferences,
brief style, batch size, and sweep intent.

The advantage is clarity. It creates an inspectable artifact early, and it maps
well to later decisions. The cost is startup drag. If the charter asks for too
much before showing value, the user feels like they are configuring software
rather than beginning a review sitting.

Kettle should keep the charter, but make it the output of founding, not the
whole interaction.

### Socratic progressive disclosure

A Socratic interview asks only questions that change downstream behaviour. It
starts broad, follows uncertainty, and stops when the next action is safe enough.

This fits Kettle's tone: calm, precise, and review-oriented. It also avoids
pretending the user already knows every preference. The risk is hidden
incompleteness. A charming conversation can still fail to produce a durable
charter that governs queue, briefs, tags, and sweep.

Kettle should use Socratic questions to fill the charter, then show the charter
for confirmation.

### Artifact-first scan

An artifact-first scan reads visible Desk material before asking much: project
files, existing `.kettle/` state, agent output, diffs, notes, headings, previous
approvals, and sweep history. It then asks questions around observed ambiguity:
"These entries look like risky configuration changes; should risk outrank
chronology in the first batch?"

This lowers the burden on experienced users and makes questions more specific.
The risk is over-inference. The curator must label inferred facts, avoid
fabricating intent, and ask for confirmation where a guess would materially
shape review.

Kettle should scan first, but treat scan results as draft evidence, not truth.

### Preference learning from rulings

Rulings are high-signal: approvals, comments, edits, tag corrections, skipped
entries, reversals, and sweep edits. They reveal what the reviewer values under
real decision pressure.

Learning from rulings can make batches sharper and briefs shorter over time. The
risk is premature personalization. One approval does not prove a stable
preference. A preference should be proposed only after repeated evidence, and it
should carry examples and counterexamples.

Kettle should learn from rulings, but with promotion gates:

1. observe a pattern in events;
2. summarize the evidence;
3. propose a memory update;
4. let the user accept, edit, reject, or defer;
5. write only accepted durable memory.

### Dual-layer durable and ephemeral memory

The curator needs two layers:

- **Durable memory** survives sittings. It contains confirmed charter fields,
  accepted preferences, stable tag definitions, voice notes, and standing
  exclusions.
- **Ephemeral sitting memory** exists for the current review. It contains current
  batch hypotheses, temporary user mood or bandwidth, unresolved questions,
  transient constraints, and recent chat context.

This mirrors the MemGPT/Letta distinction between in-context and external memory,
but in Kettle the durable layer is inspectable Desk state. The advantage is
token economy and lower drift. The cost is more memory governance: promotion,
expiry, conflict handling, and display.

Kettle should make this split explicit in the file layout and UI language.

### Persona and voice calibration

Kettle needs a consistent voice: calm, specific, and oriented toward review
decisions. Some users will also want project-specific voice calibration for
briefs, chat, and sweep: terse engineering review, editorial desk, product
strategy, legal risk, or teaching tone.

Voice calibration is useful when it makes decisions easier. It is harmful when it
turns the curator into a character or lets tone mask uncertainty. Voice memory
should therefore be optional, small, and subordinate to evidence.

The right question is not "what personality should the curator have?" It is
"what copy rhythm helps this reviewer decide without friction?"

## Recommendation: Hybrid Desk Notebook

Kettle should use a hybrid:

1. **Scan artifacts first.** Build a tentative picture from visible project and
   Desk files.
2. **Ask a short Socratic interview.** Ask only questions that affect queue,
   brief, tag, chat, or sweep behaviour.
3. **Write a durable charter.** Store confirmed project purpose, audience,
   review criteria, exclusions, batch defaults, tag rules, and sweep intent.
4. **Maintain ephemeral sitting memory.** Keep current batch state, recent
   decisions, unresolved questions, and temporary constraints separate from the
   charter.
5. **Learn from rulings with promotion gates.** Derive candidate preferences from
   actual approvals, comments, edits, tag corrections, and reversals. Do not make
   them durable without review.
6. **Use retrieval for evidence, not governance.** Search artifacts and logs to
   support a decision; keep accepted memory structured and inspectable.
7. **Offer optional voice calibration.** Let the user tune brevity, tone, and
   decision framing after the first useful batch.

The product shape is a Desk Notebook under `.kettle/`: durable charter, accepted
preferences, event log, sitting summaries, candidate memory updates, and voice
notes. It should feel ordinary because the files are ordinary.

This design fits Kettle's constraints better than either a long setup wizard or
invisible personalization. It preserves local-first trust, gives the curator
enough continuity to improve, and creates concrete artifacts that the scoring
benchmark can inspect.

## Tradeoffs

The hybrid is more complex than a pure charter. It needs promotion rules,
conflict handling, and UI affordances for proposed memory updates. That
complexity is justified because the curator's quality depends on behaviour over
time, not only setup.

The hybrid is also more deliberate than a pure learning system. It will reject
some useful-but-uncertain inferences. That is acceptable. In a review desk,
trustworthy memory beats fast personalization.

Finally, the hybrid requires discipline about token budgets. Durable memory must
be compact, typed, and selectively loaded. Ephemeral memory must expire. Artifact
retrieval must bring evidence into context only when it can change the next
decision.

If Kettle gets this right, the curator becomes familiar in the way a good desk
editor becomes familiar: not by claiming to know the user, but by remembering
what has been decided, showing its work, and asking fewer better questions.
