# Kettle documentation

Kettle is a local-first review desk for work made with coding and writing
agents. The product story is [explanation/product-home](./explanation/product-home.md).
A first pass is [tutorials/first-sitting](./tutorials/first-sitting.md).

The rest of this tree follows **[Diátaxis](https://diataxis.fr/)**: four
kinds of documentation for four needs. Keep them distinct — do not mix a
tutorial’s hand-holding with reference tables, or turn an explanation into a
command dump.

```text
                 tutorials          how-to guides
              (learning-oriented)  (goal-oriented)
                      │                   │
                      └─────────┬─────────┘
                                │
                      ┌─────────┴─────────┐
                      │                   │
                 explanation           reference
             (understanding)         (information)
```

| Kind | Need | In this tree |
|------|------|----------------|
| **[Tutorials](./tutorials/)** | “Take me through a first success” | Learning path: first sitting |
| **[How-to guides](./how-to/)** | “I need to achieve X” | Concrete tasks: release check, stranger-path QA, hooks, contribute |
| **[Reference](./reference/)** | “What are the facts / gates / names?” | Release gates, commit conventions, curator scoring |
| **[Explanation](./explanation/)** | “Why is it built this way?” | Architecture, product home, roadmap, curator design, soft release |

## Quick links

| I want to… | Start here |
|------------|------------|
| Understand what this repo is for | [explanation/product-home](./explanation/product-home.md) |
| See how the family fits together | [explanation/architecture](./explanation/architecture.md) |
| Keep viewports in sync | [explanation/viewports](./explanation/viewports.md) |
| Learn by doing a first pass | [tutorials/first-sitting](./tutorials/first-sitting.md) |
| Dogfood the stranger path (manual QA) | [how-to/stranger-path-qa](./how-to/stranger-path-qa.md) |
| Understand the curator memory direction | [explanation/curator-frameworks](./explanation/curator-frameworks.md) |
| Score curator quality | [reference/curator-scoring](./reference/curator-scoring.md) |
| See curator benchmark targets | [reference/curator-benchmark](./reference/curator-benchmark.md) |
| Run the curator evaluation lab | [how-to/run-curator-eval](./how-to/run-curator-eval.md) |
| Check whether we can ship a preview | [how-to/check-release-readiness](./how-to/check-release-readiness.md) |
| Know commit message shape | [reference/commit-conventions](./reference/commit-conventions.md) |
| See CLI × plugin chat gaps | [reference/chat-signature-inventory](./reference/chat-signature-inventory.md) |
| See sequencing | [explanation/roadmap](./explanation/roadmap.md) |
| Understand a later MCP bridge (not a sitting) | [explanation/mcp-bridge](./explanation/mcp-bridge.md) |
| Plan a soft release (names, channels, buzz) | [explanation/soft-release](./explanation/soft-release.md) |

## Writing rules (short)

| Kind | Do | Don’t |
|------|-----|--------|
| Tutorial | Lead a newcomer step by step to a known good end | Branch into every option |
| How-to | Assume competence; solve one problem | Teach from zero |
| Reference | Be complete and neutral; name facts | Narrate a story |
| Explanation | Discuss why, trade-offs, context | Become an install recipe |

Implementation detail (API, CLI flags, Desk layout) lives with **code** —
especially [`kettle-core`](https://github.com/charlesberret/kettle-core). This
home repo owns the **public story, family map, and release definition**.

## Local ops notes

Machine-local handoffs and design scratch: **`.local/`** (gitignored), not under
`docs/`.

## Checks

```sh
python3 scripts/check-docs.py
./scripts/release-ready.sh
```
