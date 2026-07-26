# Kettle work workflow

How roadmapping, work division, agents, and release checks stay orderly.

## Three layers

| Layer | System | Owns |
|-------|--------|------|
| **Story** | [`ROADMAP.md`](./ROADMAP.md), [`briefs/`](./briefs/) | Sequence, non-goals |
| **Execution** | GitHub Issues + one Project (when remotes exist); briefs until then | Who does what |
| **Gates** | [`RELEASE.md`](./RELEASE.md) + [`scripts/release-ready.sh`](../scripts/release-ready.sh) | Done / ship |

Private design scratch may stay in local `.local/` (gitignored). Durable process
belongs here under `docs/`.

## Phases → board

Use the same phase ids everywhere:

`P0` core · `P1` signature · `P2` dogfood · `P3` release · `P4` desktop · `P5` later

Project columns (suggested):

`Backlog` → `Ready` → `In progress` → `In review` → `Done`

**WIP:** prefer at most **two** `In progress` agent tasks at once.

## Labels (vocabulary)

Create these on each GitHub repo (or org-wide):

| Label | Purpose |
|-------|---------|
| `repo:home` `repo:core` `repo:vscode` `repo:desktop` | Where code changes |
| `surface:cli` `surface:chat` `surface:desk` `surface:web` | Signature craft |
| `phase:P0` … `phase:P5` | Sequencing |
| `gate:ci` `gate:manual` `gate:dogfood` | How Done is proved |
| `agent-ok` | Safe for an agent with HANDOFF + acceptance checks |
| `blocked` | Waiting on another issue or human |

Signature work that improves shell **and** Desk chat should carry **both**
`surface:cli` and `surface:chat` (or the epic notes the spine fix in core).

## Issues

### Agent task

Use template **Agent task**. Required sections:

- Goal  
- Repo / paths  
- Non-goals  
- Acceptance (checkbox; prefer gate IDs from RELEASE.md)  
- Out of scope  

Agents **only** take issues labeled `Ready` + `agent-ok`.

### Release gate

Use template **Release gate** for a single `G-*` or `M-*` id. Link the script
row or manual procedure.

## Agents

1. Read product home `README` + `docs/ROADMAP.md` (and local `.local/HANDOFF.md` if present).  
2. Claim one `Ready` + `agent-ok` issue.  
3. Implement; run local checks listed in Acceptance.  
4. Open PR in the **repo that owns the code**.  
5. CI + human review; move card on merge.  

Do not free-roam the whole roadmap. Do not archive legacy remotes or force-push
without an explicit human ask.


## Local `.local/` directories

Every Kettle-family checkout ignores a top-level **`.local/`** directory (dotfile = ops / machine-local only):

| Path | In git? | Use |
|------|---------|-----|
| `docs/` | yes | Durable public / shared process |
| **`.local/`** | **no** | Ops notes, agent handoffs, design scratch |

Dot-directory marks “not product source.” Do not commit secrets. Promote cleaned facts into `docs/` when they should be shared.

## Until GitHub remotes exist

- Track work as briefs under [`briefs/`](./briefs/) (`status: ready | in_progress | done`)  
- Still run `./scripts/release-ready.sh` for automated gates  
- When remotes land: open Issues from briefs; keep brief IDs in issue bodies for continuity  

## Cross-repo rules

- Contract changes land in **kettle-core** first (with tests), then viewports  
- CLI × chat signature → prefer core protocol/copy, then thin UI adapters  
- Desktop does not invent product UI  

## Commands

```sh
# From kettle home
./scripts/release-ready.sh
./scripts/release-ready.sh --strict
./scripts/release-ready.sh --require-live   # also demand core on :4242
```
