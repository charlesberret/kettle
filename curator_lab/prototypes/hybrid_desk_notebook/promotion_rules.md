# Hybrid promotion rules

Promotion means turning a local observation into durable desk memory for the
next sitting. It never applies non-local or irreversible actions.

Promote when:

- a user approves, rejects, comments on, or edits a queue entry;
- a recurring decision rule appears in two or more entries;
- a source gap blocks approval;
- a tag correction changes future filtering;
- a sweep insight is traceable to multiple reviewed entries.

Do not promote when:

- the observation is unsupported by local artifacts;
- it reveals private data outside the local review context;
- the user cannot inspect or reverse the decision;
- the item is duplicate noise with no future filtering value.

Promotion record:

```yaml
id: ""
source_entries: []
decision_state: approved # approved | commented | deferred | rejected
rule: ""
evidence: []
next_action: ""
expires_when: ""
```
# Hybrid Desk Notebook — promotion rules

Promote a memory item from sitting residue to durable Desk memory only when one
of these gates passes:

1. User explicitly says “remember this.”
2. The same pattern appears in **≥2** sittings or **≥3** entries with consistent
   rulings.
3. The change would alter future batch, brief, tag, chat, or sweep behavior.
4. The item corrects a contradicted durable claim.

## Do not promote

- One-off frustration or temporary project phase notes.
- Ambiguous approvals (approve ≠ global endorsement).
- Raw chat turns without summarization.
- Inferred publication or correctness claims.
- Speculative causal claims from noisy ops/logs without uncertainty labels.

## Proposal format

```markdown
# Proposal: flag unsupported claims

Status: proposed
Confidence: medium
Source: sitting 2026-08-06-a; entries entry-014, entry-022
Suggested durable text: Briefs should flag factual claims lacking citations,
tests, or source artifacts.
Exceptions: Brainstorming drafts may speculate if labeled.
```

Human accepts, edits, or rejects. Accepted proposals update `preferences.yaml`
or `charter.md` with `last_confirmed`.
