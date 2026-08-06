# Hybrid Desk Notebook memory schema

Reference layout for local `.kettle` memory files used by the hybrid prototype.
These are product artifacts for evaluation, not kettle-core schema migrations.

```text
.kettle/
  curator/
    charter.yaml
    decision-rules.yaml
    queue-memory.yaml
    sweep-memory.yaml
    source-index.yaml
```

## `charter.yaml`

- `project_type`: coding, writing, hybrid, operations, or other.
- `persona_expertise`: novice or expert.
- `purpose`: user's stated review goal.
- `audience`: who the work serves.
- `review_criteria`: source traceability, risk, action, exclusions.
- `queue_strategy`: current batch shaping rule.
- `adaptation_notes`: sparse/dense/expertise constraints.

## `decision-rules.yaml`

Stores examples and non-examples:

- `approve_when`;
- `comment_when`;
- `edit_when`;
- `investigate_when`;
- `omit_when`.

## `queue-memory.yaml`

Tracks selected and omitted entries with local source pointers, risk, action,
confidence, and reason.

## `sweep-memory.yaml`

Captures approved decisions, deferred items, reusable rules, unresolved
questions, and next-agent handoff notes.

## `source-index.yaml`

Maps queue entries to raw local files, diffs, notes, logs, or docs. Source
traceability is mandatory; losing it is a rubric critical failure.
# Hybrid Desk Notebook — memory schema

Reference layout for the recommended curator framework. These are ordinary
files under the project Desk. kettle-core should treat them as inspectable
state, not opaque profile blobs.

```text
.kettle/
  curator/
    charter.md                 # confirmed project purpose, approval semantics, review criteria
    voice.md                   # optional briefing stance / length / tone
    tags.yaml                  # standing tag taxonomy
    preferences.yaml           # confirmed user preferences
    artifact-index.json        # lightweight scan index with source paths
    ruling-ledger.jsonl        # one JSON object per approve/comment/edit/reject
    sittings/
      YYYY-MM-DD-<id>.md       # ephemeral sitting summary (or promoted excerpts)
    proposals/
      NNNN-slug.md             # memory promotions awaiting human accept/reject
    examples/
      approved/                # optional exemplar entries
      rejected/
```

## Memory item fields

Every durable claim should carry:

| Field | Purpose |
|---|---|
| `status` | `confirmed` \| `inferred` \| `proposed` \| `deprecated` |
| `confidence` | `high` \| `medium` \| `low` |
| `source` | founding interview, artifact scan, ruling, user edit, sitting summary |
| `refs` | sitting ids, entry ids, file paths |
| `last_confirmed` | date of human confirmation |
| `supersedes` | prior memory id when replacing |

## Dual-layer rule

- **Durable**: charter, preferences, tags, confirmed voice, promoted proposals.
- **Ephemeral**: current queue, open chat turns, temporary comparisons. Summarize
  or discard at sitting end unless promoted through `proposals/`.
