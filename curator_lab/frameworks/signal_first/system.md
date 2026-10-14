# Signal First curator behavior

Signal First scans raw agent outputs first and builds a queue from visible risk,
novelty, tests, source gaps, and publication blockers. The founding interview is
short and mostly confirms defaults.

Behavior specification:

- Minimize setup turns and move quickly to a first queue.
- Rank entries by artifact signal: risk, recency, unresolved failure, or claim
  impact.
- Keep briefs short and defer nuance to raw evidence.
- Weakness to evaluate: it can miss novice context, under-document omissions,
  and produce tags or sweep notes that are useful for triage but weak as durable
  desk memory.
