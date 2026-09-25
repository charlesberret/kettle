# Chat signature inventory

**Information-oriented.** Point-in-time gap list for [LAB-38](https://linear.app/isruna/issue/LAB-38/cli-plugin-chat-signature-gap-inventory-protocolcopyerrors). Not a CLI
manual and not a contract. Implementation facts live in `kettle-core`
(`API.md`, `cli.py` or equivalent) and `kettle-vscode` (Desk stream).

**Dated:** 2026-08-24. **Scope:** protocol, copy, errors — not a full CLI
rewrite, MCP, or a TUI clone of the three-pane web sitting.

## North star

CLI and plugin agent chat are paired craft. Improve the core spine so both
get better. Adapters stay thin.

| Principle | Meaning |
|-----------|---------|
| One stream | Shell `kettle chat` and plugin Desk chat are viewports on the same core stream, not two products. |
| Core owns the spine | Protocol, copy, status, and errors land in `kettle-core` first; vscode/web render them. |
| Honest phases | Activity, phase, and errors in plugin chat match CLI honesty (`doctor`, exits, stream drop). |
| No private rituals | Do not invent CLI-only recovery or chat commands the Desk cannot express. |
| Porcelain where it matters | Stable exits; `--json` for machine-readable status/chat where a second viewport needs the same facts. |

Sources (public, reconstructed — workshop `.local/agent-surfaces.md` is
gitignored and was not available in this pass):

- [Architecture: CLI and plugin chat](../explanation/architecture.md#cli-and-plugin-chat)
- First sitting: shell and web describe the same Desk
- Historical P1 (2026-07-25): “Plugin Desk chat: activity, phase, errors match CLI honesty”
- Historical brief 03: inventory table + top spine fixes; do not boil the ocean in one PR

## Method and limits

This inventory is **docs-and-history scoped**. This environment can read
`charlesberret/kettle` only. `kettle-core` and `kettle-vscode` were not
cloneable, so rows are **not** source-verified against `cli.py`, `API.md`, or
the vscode Desk stream client.

| Can claim | Cannot claim |
|-----------|--------------|
| What product-home docs currently say | Exact event names, status codes, or string catalogs in core |
| Divergence among README, tutorial, and stranger-path | Whether vscode already consumes the core stream |
| Follow-ups that match the north star and historical P1 | That a listed gap is still a bug in tree |

Re-verify each follow-up in `kettle-core` / `kettle-vscode` before implementing.

## Documented command surface

Status is vs the north star **as published in this repo**, not vs unreadable
source.

| Command / control | Where documented | Chat-spine role | Status |
|-------------------|------------------|-----------------|--------|
| `kettle doctor` | README, first sitting, stranger-path | Error honesty; “proud doctor” | **ok** in docs |
| `kettle --web` | README, first sitting, stranger-path | Host for web agent pane | **ok** in docs |
| `kettle add` | README, first sitting, stranger-path | Desk identity | **ok** in docs |
| `kettle queue` | README, first sitting, stranger-path | Sitting companion | **ok** in docs |
| `kettle chat` | README; stranger-path (optional); first sitting (optional, this change) | CLI viewport on the agent stream | **gap**: protocol unpublished here; still optional in QA |
| `kettle projects` | First sitting, stranger-path | Identity | **gap**: omitted from README |
| `kettle found` | Stranger-path only | Founding interview = chat | **gap**: omitted from README / first sitting |
| `kettle open` | Stranger-path only | Entry companion | **gap**: omitted from README / first sitting |
| `kettle sweep-status` | Stranger-path only | Status honesty | **gap**: omitted from README / first sitting |
| `kettle --help` | Stranger-path | Discovery | **ok** in docs |
| `kettle --json` / porcelain | Historical P1 / 0.2 sketch only | Shared facts for plugin + scripts | **missing** from current public docs |
| Plugin: Kettle Ping Core | Stranger-path | Attach to core | **ok** in QA checklist; source unverified |
| Plugin: `kettle.command` | Stranger-path | Path when auto-start fails | **ok** in QA; must stay documented, not a hidden ritual |
| Plugin: queue / comment / approve / sweep | Stranger-path, first sitting (web) | Desk rituals | **ok** as sitting path |
| Plugin: agent pane / founding interview | First sitting, stranger-path | Plugin/web chat | **gap**: no public activity/phase/error contract |

## Gaps (protocol / copy / errors)

| ID | Area | Gap vs north star | Evidence in this repo | Likely owner |
|----|------|-------------------|------------------------|--------------|
| G1 | Protocol | No public stream contract for activity, phase, and terminal events that both CLI and plugin must consume. Product-home defers to `kettle-core/API.md` and `docs/PLATFORMS.md` “when present”; neither is in this tree. | [Architecture sources of truth](../explanation/architecture.md); [explanation index](../explanation/README.md) | `kettle-core` |
| G2 | Protocol | Plugin chat is described as an “agent pane” / founding interview, while CLI chat is a separate optional command. Nothing states they are the same event stream. | First sitting vs stranger-path `kettle chat` | `kettle-core` then `kettle-vscode` |
| G3 | Copy | Status vocabulary is not catalogued. `doctor`, `sweep-status`, plugin attach, and chat phase lines can drift independently. | Commands documented in different guides with no shared names | `kettle-core` (string catalog) |
| G4 | Copy | README, tutorial, and stranger-path disagree on which shell commands exist. That is copy drift on the CLI viewport itself. | Table above | `kettle` (docs) / `kettle-core` (`--help` as authority) |
| G5 | Errors | North star: plugin errors match CLI honesty. Host/Origin work is called Done in Linear (LAB-23); public docs do not say how chat surfaces the same failure classes (core down, missing curator auth, stream drop, Origin reject). | Roadmap Host/Origin; stranger-path doctor “public terms”; no chat error map | `kettle-core` + thin adapter |
| G6 | Errors | Stranger-path: if doctor fails in a way public docs do not explain, that is a product-docs bug. Chat/plugin failures have no equivalent rule. | [Stranger-path QA](../how-to/stranger-path-qa.md) | `kettle` docs after core catalog exists |
| G7 | Porcelain | Historical P1 asked for stable exits and `--json` where it matters. Current public docs never mention JSON/porcelain for chat or status. | Old ROADMAP P1 / release 0.2 sketch (git history); absent from current [roadmap](../explanation/roadmap.md) | `kettle-core` |

## Top follow-ups

Do not boil the ocean in one PR. File these in Linear (Kettle project,
milestone **Dependable distribution / Next** unless noted). Implementation
lands in core first.

### 1. Chat stream contract (protocol)

- **Title:** Chat stream: one activity/phase/error schema for CLI and plugin
- **Repo:** `kettle-core`
- **Why:** Paired craft fails if vscode and `kettle chat` speak different events.
- **Do:** Document the Desk/agent stream in `API.md` (activity, phase, error,
  terminal). Add contract tests. CLI and plugin consume that schema; no
  plugin-only status protocol.
- **Mode:** agent · **Diff:** M
- **Acceptance:**
  - [ ] Event types and payload fields named in `API.md`
  - [ ] Contract tests cover happy path, stream drop, and at least one auth failure
  - [ ] `kettle chat` and vscode Desk stream share the types (adapter may wrap, not fork)

### 2. Shared status copy (copy)

- **Title:** Shared chat/CLI status copy owned by core
- **Repo:** `kettle-core`
- **Why:** Phase names and activity verbs that differ by viewport feel like two products.
- **Do:** One catalog for phase names, activity verbs, empty states, and
  attach/idle copy. Plugin and CLI render those strings.
- **Mode:** agent · **Diff:** S–M
- **Acceptance:**
  - [ ] Catalog lives in core (module or documented table), not duplicated in vscode
  - [ ] Same desk state produces the same words in CLI and plugin (golden test or fixture)

### 3. Chat error honesty (errors)

- **Title:** Chat errors match CLI and doctor honesty
- **Repo:** `kettle-core` (strings + mapping); thin `kettle-vscode` render
- **Why:** Plugin must not swallow failures the CLI prints, or invent a recovery ritual the Desk cannot express.
- **Do:** Map failure classes — core unreachable, curator CLI missing/unauthenticated,
  Host/Origin reject, stream drop — to the same user-visible error class in
  `doctor`, `kettle chat`, and plugin chat.
- **Mode:** agent · **Diff:** M
- **Acceptance:**
  - [ ] Failure-class table in core docs
  - [ ] Each class has a CLI reproduction and a plugin reproduction with matching class (wording may wrap for the host)
  - [ ] No plugin-only “repair” that mutates PATH, auth, or Desk files silently

### 4. Porcelain for chat and status

- **Title:** Stable exits and `--json` for chat/status
- **Repo:** `kettle-core`
- **Why:** A second viewport (plugin, scripts, tests) should read the same facts the human sees.
- **Do:** Stable exit codes for chat/status/doctor; `--json` (or existing equivalent)
  for the states the stream contract already names. Do not add a parallel JSON dialect in vscode.
- **Mode:** agent · **Diff:** M
- **Depends on:** follow-up 1
- **Acceptance:**
  - [ ] Documented exits for success, usage error, core unreachable, curator unavailable
  - [ ] `--json` (or named equivalent) emits the stream/status fields tests already use
  - [ ] Plugin does not define a second status JSON shape

### 5. Viewport parity matrix

- **Title:** Publish `PLATFORMS.md` viewport parity (CLI / web / vscode chat)
- **Repo:** `kettle-core` (`docs/PLATFORMS.md`); product-home already points here
- **Why:** Product-home cites a parity matrix that is “when present.” Strangers cannot see pairing without it.
- **Do:** Table of sitting actions and chat states across CLI, web, and vscode.
  Mark ok / gap / n/a. Keep it factual; do not duplicate `API.md`.
- **Mode:** hybrid · **Diff:** S
- **Milestone:** can sit on **Now** (stranger-path honesty) once follow-up 1 exists, or ship a stub that says “unverified”
- **Acceptance:**
  - [ ] `kettle-core/docs/PLATFORMS.md` exists and is linked from core README
  - [ ] Chat activity/phase/error rows exist even if some cells are “unverified”
  - [ ] Product-home explanation index can drop the “when present” hedge

## Out of scope (this inventory)

- Implementing the north-star CLI in one PR
- MCP bridge (separate Later work)
- TUI clone of the three-pane web app
- Burning the rest of the transcript-recon pile
- Source-level command audit (blocked on `kettle-core` access)

## Close LAB-38 when

- [x] Written inventory (this file): documented commands + protocol/copy/error gaps
- [x] Prioritized spine follow-ups with acceptance (five above)
- [x] One small pairing fix in product-home (architecture north star + optional `kettle chat` in first sitting)
- [ ] Follow-ups filed as Linear issues (bodies above; Linear MCP was unauthenticated in this agent run)
- [ ] No CLI-only ritual introduced (none added; plugin called out as the same stream)

Linear remains the plan. This file is the public mirror so the pairing is not
only in `.local/` or a chat transcript.
