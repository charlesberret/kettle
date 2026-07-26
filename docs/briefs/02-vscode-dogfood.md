---
id: 02
title: kettle-vscode dogfood sitting
phase: P2
status: ready
repo: vscode
labels: [phase:P2, repo:vscode, surface:desk, surface:chat, agent-ok, gate:dogfood]
---

# 02 — VS Code / Cursor dogfood

## Goal

`kettle-vscode` can be installed and used for a real founding or founded sitting
against a live core (setsweep core OK during transition).

## Paths

- `../kettle-vscode` — extension 0.1.0 scaffold
- Core: live `:4242` via setsweep or kettle-core when available

## Non-goals

- Perfect rebrand of all user-visible strings in core
- Obsidian / desktop work
- Marketplace listing

## Acceptance

- [ ] `npm test` and `npm run compile` green (`G-vscode-test`, `G-vscode-compile`)
- [ ] VSIX builds (`npm run package`)
- [ ] Extension activates; attaches to core (`app` kettle or setsweep)
- [ ] Manual: one sitting path exercised (`M-dogfood-sit`) — document what was done
- [ ] File issues only for blockers; no drive-by architecture rewrite

## Start

```sh
cd ../kettle-vscode && npm test && npm run package
# cursor --install-extension kettle-0.1.0.vsix --force
```
