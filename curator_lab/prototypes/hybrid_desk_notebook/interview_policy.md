# Hybrid interview policy

The interview adapts question depth to persona expertise, project type, and raw agent-output density.

## Defaults

Ask one opening question that establishes:

- review goal;
- audience or user;
- risk tolerance;
- desired first queue shape;
- exclusions.

## Novice behavior

- Explain what a queue entry, brief, comment, approve, and sweep mean only when the fixture indicates novice expertise.
- Prefer reversible recommendations.
- Use "why this matters" in briefs.

## Expert behavior

- Keep prompts short.
- Ask for ranking preferences and raw evidence needs.
- Do not tutorialize Kettle concepts.

## Sparse output

- Ask whether uncertainty labels should outrank speed.
- Preserve absence-of-evidence caveats.

## Dense or noisy output

- Confirm deduplication and risk-first ordering.
- Ask whether omissions should be listed in the sweep.

## Stop condition

Move to queue generation as soon as the charter can govern at least 80% of queue, brief, tag, and sweep decisions.
# Hybrid Desk Notebook — interview policy

## Opening move

1. Scan local artifacts (README, tree, existing desk files, queue candidates).
2. Present a short inferred briefing with uncertainties labeled.
3. Ask **4–6** high-value questions only:
   - project purpose;
   - what approval means in this desk;
   - quality bar / hard nos;
   - common agent failure modes;
   - briefing preference (terse / explanatory / coaching);
   - known tags or batch habits.
4. Write a draft charter and ask for correction, not completion.
5. Offer skip: “learn from my rulings.”

## Expertise adaptation

| User | Behavior |
|---|---|
| Novice | Plain-language impact, examples of good/bad rulings, fewer jargon tags |
| Expert | Terse probes, show inferred charter first, skip obvious questions |

## Density adaptation

| Agent output | Behavior |
|---|---|
| Sparse | Interview carries more weight; label unknowns; do not invent CI/file state |
| Dense / noisy | Scan-first clustering; ask only about judgment criteria and omissions |

## Hard constraints

- Never treat approve as publish/ship.
- Never fill charter slots with unsupported guesses marked as confirmed.
- Cap founding interview; familiarity is earned across sittings.
