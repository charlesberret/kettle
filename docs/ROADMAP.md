# Kettle roadmap

Product sequencing for the Kettle family. Execution detail lives in GitHub Issues
(when remotes exist) and in [`briefs/`](./briefs/). Release gates:
[`RELEASE.md`](./RELEASE.md). Workflow: [`WORKFLOW.md`](./WORKFLOW.md).

## North star

**Kettle** — a review instrument for working with coding and writing agents.  
Agents prepare and propagate; you read and rule. The desk is files under the
project; every UI is a viewport on a localhost core (default port **4242**).

| Principle | Meaning |
|-----------|---------|
| CLI first-class | Shell is a primary viewport, not a server sidecar |
| CLI × plugin chat | Signature craft — improve core spine so both get better |
| One repo per host | `kettle-vscode`, later `kettle-obsidian`; no empty plugin monorepo |
| Desktop exists | Built (legacy name OK); low attention; no Electron-only founding |
| MCP optional | Narrow model bridge later — not a product pillar |

## Phases (do not invert)

```text
P0  Core transplant + dual-read desks
P1  CLI × agent-chat signature (core protocol + copy)
P2  kettle-vscode dogfood
P3  Release 0.1 candidate (see RELEASE.md)
P4  Desktop rename / quiet maintenance
P5  Obsidian / MCP / Marketplace — on demand
```

### P0 — Core identity

- Land runnable core in **`kettle-core`** (from setsweep-core)
- Keep `api_version` / `desk_schema_version` stable across rename
- Dual-read desks: prefer `.kettle/`, fall back `.setsweep/`
- CLI dual-stack: `kettle` with transitional `setsweep` as needed

### P1 — Signature craft

- CLI: stable exits, `--json` where it matters, proud `doctor`
- Plugin Desk chat: activity, phase, errors match CLI honesty
- Prefer fixes in core (protocol, copy, rituals) over one-off chrome

### P2 — Editor dogfood

- `kettle-vscode` daily driver on Cursor/VS Code
- Founding + one full sitting on a real desk
- Chat/stream polish counts as signature work

### P3 — Release 0.1

- All automated gates in [`RELEASE.md`](./RELEASE.md) green
- One human dogfood checkbox
- Public remotes optional but recommended before “released”

### P4 — Desktop (quiet)

- Rename setsweep-desktop → kettle-desktop when convenient
- Point at kettle-core; no feature race with vscode
- Signing/notarization parked until P3 is boring

### P5 — Later

- Obsidian, MCP, Homebrew, Marketplace polish, other hosts — only with a written use case

## Non-goals (for now)

- Desktop-only founding UI  
- Multi-host adapter monorepo  
- Breaking API version for branding  
- Multi-user / remote multi-tenant server  
- Perfect history rewrite of all legacy remotes  

## Family

| Tree | Role |
|------|------|
| **kettle** (this repo) | Product home, docs, star target, release orchestration |
| **kettle-core** | Desk, API, kits, CLI, reference web UI |
| **kettle-vscode** | VS Code + Cursor (one VSIX) |
| **kettle-desktop** | macOS shell (exists as setsweep-desktop) |
| **kettle-obsidian** | Later |

## Tick when true

- [ ] kettle-core runnable (`kettle` or transitional CLI)
- [ ] kettle-vscode daily driver for one real desk
- [ ] `scripts/release-ready.sh` green for Release 0.1
- [ ] Home README family links accurate
- [ ] Desktop documented or renamed without new features

---

*Update when phase gates flip. Private scratch may live in local `planning/` (gitignored).*
