# MCP bridge — threat, use, and scope

This is a **Later** boundary note, not a ship plan. It exists so a Model
Context Protocol (MCP) adapter cannot quietly become a second product.

Kettle already has a sitting (web, CLI, editor, desktop) and a first-class
CLI in `kettle-core`. An MCP bridge is justified only when a **model-host
tool** needs the **same Desk** the human will sit with later. It is not a
replacement for `kettle` commands, and it is not a sitting.

Linear: [LAB-34](https://linear.app/isruna/issue/LAB-34/mcp-bridge-narrow-desk-aligned-not-a-sitting-replacement).
Sequencing: [roadmap](./roadmap.md). Family rules: [architecture](./architecture.md).

## Use that would justify work

The only use that survives the product constraints:

A model-host session (Cursor, Claude Code, VS Code Copilot Chat, or similar)
is already producing agent work against a **registered project**. It needs to
land that work on the Desk the reviewer will open, or to read just enough
queue and charter state to format that handoff. The human still sits
elsewhere.

Concrete operations that fit:

| Operation | Why it is desk-aligned |
|---|---|
| Enqueue or stage an entry from host output | Agent work waits on the Desk; the sitting is unchanged |
| Read queue, entry status, or brief | The host can avoid duplicate entries and match Desk conventions |
| Read a short charter or policy excerpt | The host writes toward standing rules, not a parallel memory |
| Attach a path already inside a registered root | Evidence stays in ordinary project files |

That is a **handoff adapter**, not a review surface.

### Uses that do not justify work

- Sitting inside the model host (approve, comment-as-ruling, sweep, founding
  interview, curator chat).
- Replacing the CLI for humans (`kettle queue`, `kettle add`, `kettle
  doctor`).
- Remote or multi-user queues (separate [threat model](./roadmap.md)).
- Autopilot: the producing agent reviewing or applying its own work.
- A public remote MCP (Linear-style hosted HTTP) in front of a local Desk.
- Wrapping provider CLIs or holding model API keys.

If the only demand is “let the agent sit instead of the human,” **cancel**
the adapter. The sitting is the product.

## Threat note

MCP is a tool protocol for model hosts. A Kettle bridge would sit next to
the Desk and, if it used HTTP, next to the localhost API. That is a new
confused-deputy surface: the host calls tools with the user's ambient
authority, and tool results often leave the machine into a remote model
context.

Official MCP guidance treats local servers as ordinary child processes, not
a sandbox, and calls out confused-deputy, local-server compromise, and
stdio-proxy escalation
([security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)).
STDIO launch-from-config is a known supply-chain and RCE pattern when the
command string is untrusted.

| Threat | Why it matters here | Refusal or mitigation |
|---|---|---|
| **Sitting replacement** | Approve, sweep, or curator chat as tools lets the producer mark its own work done | Never expose approve, reject, sweep, found, interview, or sitting chat |
| **CLI replacement** | A tool catalog that mirrors the CLI makes MCP the product surface | Ship only the handoff verbs above; keep `kettle` canonical for humans |
| **Confused deputy** | The host acts as the reviewer without a sitting | Write tools enqueue or annotate only; they do not record a human ruling |
| **Privilege / egress** | Sweep or transmit tools would silently apply or send staged work | No apply, execute, or egress-send tools. Approve remains a bookmark |
| **Desk exfiltration** | Queue, briefs, comments, and staged egress are project-private | Default to the smallest read set; never dump the whole Desk into model context |
| **Forked Desk** | Direct file writes bypass core semantics and migrations | All mutations go through `kettle-core` (same functions or localhost contract) |
| **Unauthenticated second door** | An MCP process that talks to core without the planned per-boot local auth widens the HTTP surface | Write tools wait on that auth design ([roadmap](./roadmap.md) Now). Host/Origin already applies to any HTTP client |
| **Remote MCP** | Streamable HTTP or OAuth-hosted MCP moves the Desk off loopback | Local stdio only, spawned by an already-trusted host on the same machine. No bind on `0.0.0.0`, no hosted MCP |
| **Untrusted spawn** | `npx -y …` / workspace-supplied command strings are an RCE path | Blessed launch is a pinned `kettle` (or venv) binary plus fixed args. No one-click remote config as the install story |
| **Tool poisoning** | Hidden instructions in tool descriptions steer the host | Keep descriptions short and literal; no “you must also…” prose; review them like code |
| **Cross-root access** | A tool that takes an arbitrary path escapes registered projects | Same root fence as core. No raw filesystem tools |
| **Provider credentials** | MCP hosts often inherit the user environment | Kettle still does not collect or store API keys |
| **Proxy stdio escalation** | A local HTTP proxy that spawns stdio servers turns XSS into RCE | Do not add a spawn-proxy. The host starts the server; Kettle does not |

Remote and multi-user serving stay out of scope until authentication, tenant
isolation, and session ownership are designed together
([architecture](./architecture.md)). This note is not that threat model.

## Scope sketch

Do not implement until a named model-host workflow has been dogfooded and
cannot be done well with the CLI or ordinary files.

### In

- A **thin kit inside `kettle-core`**, in the same spirit as the CLI: one
  process, core-owned semantics, no forked Desk format.
- **Local stdio** transport only. The model host already trusted on the
  machine spawns it.
- Talk to the Desk through core (in-process APIs or the versioned localhost
  contract). If HTTP is used, Host/Origin and the future per-boot local
  token apply; MCP is another client, not a bypass.
- Tool surface, first cut:

  | Tool | Direction | Notes |
  |---|---|---|
  | `list_projects` / current Desk | read | Registered projects only |
  | `queue_list` / `entry_get` / `brief_get` | read | Enough to hand off, not a sitting UI |
  | `charter_excerpt` | read | Short, explicit fields — not “dump memory” |
  | `enqueue_entry` | write | Stage agent work; never approve |
  | optional `attach_path` | write | Path must already sit under the registered root |

- Compatibility via the existing API and Desk-schema integers, not a
  parallel schema.
- A new repository only if the kit later needs a distinct host lifecycle
  **and** it has a concrete workflow, an owner, and a release path
  ([architecture](./architecture.md)).

### Out

- Approve, reject, sweep, found, interview, curator chat.
- Egress transmit, apply, execute, merge, or “land this PR.”
- Arbitrary file read/write, shell, or provider-CLI wrappers.
- Remote / Streamable HTTP MCP, OAuth proxy, or marketplace “connect
  Kettle” hosted server.
- A TUI or web sitting hosted behind MCP.
- An empty `kettle-mcp` product presented as shipped.
- Blocking public preview or dependable distribution on this work
  ([soft release](./soft-release.md)).

### Prerequisites before any write tool

1. Host/Origin validation on the localhost HTTP surface (preview work).
2. The per-boot local authentication design on the Now roadmap.
3. One written dogfood story: which host, which handoff, why CLI or files
   failed, and confirmation that a human sitting still happened in web,
   CLI, or editor.

### Ownership

| Fact | Authority |
|---|---|
| Whether to build at all | This note + a dogfood record in Linear |
| Semantics, Desk, contract | `kettle-core` |
| Host spawn / MCP client UX | The model host, not Kettle |
| Public story | This repository |

Core never imports an adapter. If a contract change is required, it lands
in core first.

## Cancel, keep Later, or build

| Signal | Action |
|---|---|
| Demand is only “sit in the host” or “approve from the model” | **Cancel** the adapter |
| No named host workflow after preview | Stay **Later**; do not open a repo |
| Handoff-from-host is real, CLI/files are awkward, sitting stays human | **Build** the kit above, still not a sitting |

This issue is satisfied by the note. Implementation is a later Linear issue
with a dogfood pointer, not a follow-on in the same sitting.
