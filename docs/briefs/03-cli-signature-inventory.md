---
id: 03
title: CLI inventory and signature spine with agent chat
phase: P1
status: ready
repo: core
labels: [phase:P1, repo:core, surface:cli, surface:chat, agent-ok]
---

# 03 — CLI × chat signature inventory

## Goal

Document current CLI surface vs north-star, and list **shared spine** fixes
(protocol, copy, status) that improve **both** CLI and plugin agent chat.

## Paths

- Core CLI: setsweep-core / kettle-core `cli.py` (or equivalent)
- Plugin chat: kettle-vscode Desk stream
- Product notes: home `docs/ROADMAP.md`; local planning `cli.md` / `agent-surfaces.md` if present

## Non-goals

- Implementing the entire north-star CLI in one PR
- MCP server
- TUI clone of the three-pane web app

## Acceptance

- [ ] Written inventory table: command → status (ok / gap / missing)
- [ ] Prioritized list of spine fixes (top 5) that lift CLI **and** Desk chat
- [ ] At least one small spine or CLI fix merged **or** filed as follow-up issues with acceptance
- [ ] No behavior that invents CLI-only rituals the Desk cannot express

## Start

After or in parallel with brief 01. Prefer landing inventory under
`kettle-core/docs/` or `kettle/docs/briefs/` as `03-inventory-results.md`.
