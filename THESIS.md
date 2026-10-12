# Kettle

Status: proposed

## Claim

Kettle is a local-first review desk. Agent work waits in ordinary files inside a project. A person reads a brief and records a ruling — comment, approve, sweep — before anything moves outward. Approve records the ruling. It does not apply or publish the work. One core owns desk semantics. The browser, the editor, and a thin desktop shell are viewports on that core. See [README.md](README.md) and [docs/explanation/architecture.md](docs/explanation/architecture.md).

## Motivation and value

This is for someone who already runs a coding or writing agent and wants a place to judge its output on their own machine before it leaves. Success, for a later sitting, is the public-preview bar in [docs/reference/release-gates.md](docs/reference/release-gates.md): [scripts/release-ready.sh](scripts/release-ready.sh) is green, and a written manual record shows that a stranger installed from the public instructions, founded or opened a desk, reviewed, commented, approved, and swept, and that approval did not itself apply or transmit work. Until that record exists, the repositories stay private. [README.md](README.md) states that status.

## Prior art and alternatives

A monorepo was rejected. Separate repositories let package versions move on their own. The cost is drift across trees, paid by explicit API and desk contracts rather than one checkout. See [docs/explanation/architecture.md](docs/explanation/architecture.md).

Approve-as-apply was rejected. If the ruling itself published or executed the work, the human step would be a side effect. The desk keeps the ruling as a record and lets sweep apply it under policy. See [README.md](README.md) and the permanent constraints in [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

Remote or multi-user use now was rejected. The roadmap leaves it until a separate threat model exists. See [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

Shipping an Obsidian adapter or a general MCP bridge as a current product was rejected. Those wait for a concrete workflow to dogfood. An empty adapter is not a viewport. See [docs/explanation/roadmap.md](docs/explanation/roadmap.md) and [docs/explanation/architecture.md](docs/explanation/architecture.md).

Outside the house, five tools share the shape of a review step before agent work moves. Each is real competition. The trade-off that keeps kettle is in parentheses.

- crt: approval is a watermark on what changed since the last approval. Kettle's approve records a ruling, and sweep applies it under policy.
- Stage: the agent splits its branch into chapters and opens a local browser review before a pull request exists. Kettle's queue is the desk of ordinary files, not a chapter split of a branch.
- Parley: GitHub-style review, local, in a terminal. Kettle's reference sitting is the web desk. The terminal is not a public-preview gate. See [docs/reference/release-gates.md](docs/reference/release-gates.md).
- AgentClick: a browser review layer between "agent proposes" and "agent executes," and the agent continues after approval. Kettle's approve does not continue the agent.
- OACP: a plain-file review queue whose states are review request, feedback, addressed, and lgtm. This is the closest analogue to a `.kettle/` desk. Kettle keeps one core as the authority for those semantics, and sweep is the apply step, not an agent-to-agent lgtm. See [docs/explanation/architecture.md](docs/explanation/architecture.md).

## Design

Core owns product semantics, desk format and migrations, the localhost API, the CLI, kits, and the reference web UI. The editor owns activation and packaging. The desktop shell owns Electron lifecycle and sits on the core's web UI. Adapters do not fork the desk. A cross-repository change lands in core first, with a compatible contract, then in the adapters that need it. New projects store the desk in `.kettle/`. During the Setsweep window, core prefers `.kettle/` and falls back to an existing `.setsweep/` desk. It does not create two writable desks for one project. See [docs/explanation/architecture.md](docs/explanation/architecture.md).

Bets on a single user: the localhost API, one `.kettle/` directory per project, and one ruling recorded per item. What still holds if a second reviewer is on the same machine: the desk stays ordinary files, approve stays a record, and sweep still applies under policy. See [docs/explanation/roadmap.md](docs/explanation/roadmap.md). What does not hold is a shared remote desk. That stays on Later.

## Evidence

The claim and the private-preview status are in [README.md](README.md). Commit [6337dea](6337dea) named that private preview. `origin/main` at the base of this branch is [0fcfb42](0fcfb42).

The preview bar and the manual dogfood list are in [docs/reference/release-gates.md](docs/reference/release-gates.md). The local gate script is [scripts/release-ready.sh](scripts/release-ready.sh). The first-sitting lesson is [docs/tutorials/first-sitting.md](docs/tutorials/first-sitting.md): install, run `kettle doctor`, start the server on port 4242, register a folder.

This repository does not contain the core test suite, the editor suite, or a written record that the manual dogfood has been walked. The gates name that evidence. The passing output is not in this tree. The preview is not claimed ready here.

## Risks and open questions

The claim fails if approve starts to apply or transmit work. The roadmap forbids that. See [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

A green install check is not a live server. The tutorial runs `kettle doctor` and then starts the server. See [docs/tutorials/first-sitting.md](docs/tutorials/first-sitting.md). These docs do not treat a green doctor as proof that port 4242 answered.

Publishing the repositories before the manual dogfood record exists, and before clone links work without authentication, would ship a preview the release definition says is not ready. See [docs/reference/release-gates.md](docs/reference/release-gates.md) and [README.md](README.md).

Unknown: whether an experimental terminal viewport is part of the product. This thesis leaves it outside the preview bar. If there is no desk without it, the scope below is wrong.

Unknown: whether a person remains the default reviewer. The claim is that a person reads the brief and records the ruling before anything moves outward. If next year's users want an agent to make the routine rulings, a desk that requires a human ruling on every item becomes the exception queue, and the claim loses its user. The answer that keeps the claim is that the human ruling stays the default, and an agent reviewer would be a later adapter, not a replacement. The evidence that would decide it is a dogfood count of rulings a human marked trivial. That count is not in this repository.

The single-user assumption, the missing record behind it, and the tripwire that reopens it are in Plan.

## Scope

In: the public-preview bar in [docs/explanation/roadmap.md](docs/explanation/roadmap.md) (Now) and [docs/reference/release-gates.md](docs/reference/release-gates.md). That is install, localhost safety, a stranger dogfood, docs, and staying private until links work without authentication. Viewports on that bar: the reference web UI, VS Code and Cursor, and the thin macOS shell.

Out: package registries, a marketplace listing, code signing, and notarization. Those are Next on the roadmap. Obsidian, a general MCP bridge, and remote or multi-user use are Later. An experimental terminal viewport is not a row in the public-preview gate table. A versioned sitting-judge is not on that table either.

## Plan

The order is the roadmap order: Now (trustworthy public preview), then Next (dependable distribution), then Later (evidence-led adapters). See [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

Progress is [scripts/release-ready.sh](scripts/release-ready.sh) plus the manual dogfood record in [docs/reference/release-gates.md](docs/reference/release-gates.md). These product-home docs set no calendar date for the preview.

Appetite: one maintainer pass through that manual record before any repository is made public. The lesson in [docs/tutorials/first-sitting.md](docs/tutorials/first-sitting.md) is about fifteen minutes. The stranger pass in the release definition is the longer check. If that record is not written, the appetite is spent and the repositories stay private. Wheels, a marketplace listing, and notarization do not start in place of that record.

The plan assumes next year is still a local single-user desk with thin viewports. The record in this repository for that assumption is none. [docs/explanation/roadmap.md](docs/explanation/roadmap.md) puts a hosted multi-user product on Later, and it does not name a second person who has ruled on one desk. Tripwire: a second person records a ruling on one desk during dogfood, or a stranger's issue asks to share a desk. Either event reopens the assumption before Later. Design sorts the bets. Localhost, one `.kettle/` directory, and one ruling per item are single-user bets. Ordinary files, approve-as-record, and sweep-under-policy still hold for a second reviewer on the same machine. A shared remote desk does not. This repository does not contain a threat model for that other assumption.
