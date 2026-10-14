# Hybrid brief template

```markdown
## {entry_title}

**What changed:** {source-grounded summary}

**Why it matters:** {behavior, claim, tone, config, causality, or docs/code impact}

**Evidence:** {local file, diff, log, note, or section pointers}

**Risk/confidence:** {risk} risk, {confidence} confidence

**Lowest-friction action:** {approve | comment | edit | inspect | investigate | defer}

**Caveat:** {uncertainty, missing source, unresolved test, mismatch, or none}

**Tags:** {compact taxonomy tags}
```

Rules:

- Keep expert briefs terse and evidence-linked.
- Add plain-language "why this matters" for novice fixtures.
- Do not claim CI, source state, or approvals not visible in local artifacts.
- Every brief should answer: "What am I approving?", "What could be wrong?", and "What is the next reversible action?"
# Brief template

```markdown
# {entry_title}

**Decision hook:** {approve | inspect | edit | defer | reject}
**Risk:** {level} — {one residual-risk sentence}
**Evidence:** {paths / entry ids; never invent}

{plain_or_terse_impact_sentence}

## Why it is in this batch
{dependency or risk reason}

## What would change my mind
{missing evidence or open question}
```

## Style rules

- Lead with the decision, not praise.
- Cite evidence paths that exist on the Desk.
- Match persona: novice → plain language; expert → compressed.
- Label uncertainty instead of filling gaps.
