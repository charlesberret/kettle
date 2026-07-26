---
id: 01
title: Transplant setsweep-core into kettle-core
phase: P0
status: in_progress
repo: core
labels: [phase:P0, repo:core, agent-ok, gate:ci]
---

# 01 — Core transplant

## Goal

`~/cloud/git-projects/kettle-core` is a runnable Kettle-family core (package +
tests), dual-reading `.kettle/` and `.setsweep/` desks, with transitional CLI
name support as needed.

## Paths

- Source: `../setsweep-core` (canonical until flip)
- Dest: `../kettle-core` (empty dir today)
- Contract: do **not** bump `api_version` / `desk_schema_version` for rename only

## Non-goals

- Full purge of “Setsweep” strings in all kits
- Desktop rebrand
- Marketplace publish
- Breaking API changes

## Acceptance

- [ ] `kettle-core` has `pyproject.toml` and imports/tests green (`G-core-tree`, `G-core-test`)
- [ ] Desk path prefer `.kettle/`, fallback `.setsweep/`
- [ ] `kettle --help` and/or transitional `setsweep --help` works after install (`G-cli-help`)
- [ ] `../kettle/scripts/release-ready.sh` improves (core gates no longer “missing tree”)
- [ ] Short note in kettle-core README: dual-stack + link to product home

## Start

Read home `docs/ROADMAP.md` P0 and local `.local/rename-from-setsweep.md` if present.
Prefer one transplant session over gradual half-copies.
