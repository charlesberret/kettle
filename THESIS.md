# Kettle

Status: accepted

## Claim

Kettle is a local-first review desk. Agent work waits in ordinary files inside a project. A person records a ruling through core — comment, approve, sweep — before anything moves outward. Approve, at kettle-core `3bab46b`, sets `status` to `approved` in the desk queue and appends `approvals.log`. It does not apply or publish the work. Sweep, not approve, stages an approved inbox entry. One core owns desk semantics. The reference web UI and the editor are the viewports on the public-preview bar. See [README.md](README.md) and [docs/explanation/architecture.md](docs/explanation/architecture.md).

The desk does not yet tell a person's ruling from one written by a same-user agent. Any process that can write `.kettle/queue.json` can set `status` to `approved`, and sweep selects on that field. That gap is in Risks. Closing it means a ruling written by core that carries a digest of the brief and the diff, which sweep refuses on mismatch. That check is not in `3bab46b`, and this preview does not add it.

## Motivation and value

This is for someone who already runs a coding or writing agent and wants a place to judge its output on their own machine before it leaves. Success, for a later sitting, is a stored run, not a green word. On the maintainer's machine, `./scripts/release-ready.sh --strict --require-live` exits 0, and [docs/reference/preview-record.md](docs/reference/preview-record.md) holds that run's stdout (the `Summary:` line and every gate row), the host, `kettle --version`, the SHA of the tree that binary was installed from, and the four pinned SHAs. The live gate accepts `"app": "kettle"` only. See [scripts/release-ready.sh](scripts/release-ready.sh) and [docs/reference/release-gates.md](docs/reference/release-gates.md).

The manual half of that record is two steps, named in Plan. The cue that approve moved nothing is `git status` of the project showing no change outside `.kettle/`. Until the pre-flip step is written, the repositories stay private. [README.md](README.md) states that status.

## Prior art and alternatives

A monorepo was rejected. Separate repositories let package versions move on their own. The cost is drift across trees, paid by explicit API and desk contracts rather than one checkout. The price of that drift is the number of commits and sittings from the pinned set in Plan to the first `--strict --require-live` exit 0, written in [docs/reference/preview-record.md](docs/reference/preview-record.md) when the run happens. That number is not known today. `kettle-mcp`, `kettle-obsidian`, and `kettlekit.xyz` are outside the family until each is a git repository with an implementation and a release path. See [docs/explanation/architecture.md](docs/explanation/architecture.md) and [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

Approve-as-apply was rejected. If the ruling itself published or executed the work, the human step would be a side effect. At `3bab46b`, approve only records the ruling. Sweep stages every approved inbox entry to `.kettle/outbound/`. Nothing in that commit makes sweep refuse an item. "Under explicit policy" is roadmap constraint 3, and it is not implemented. See [README.md](README.md) and [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

Remote or multi-user use now was rejected. The roadmap leaves it until a separate threat model exists. See [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

Shipping an Obsidian adapter or a general MCP bridge as a current product was rejected. Those wait for a concrete workflow to dogfood. An empty adapter is not a viewport. See [docs/explanation/roadmap.md](docs/explanation/roadmap.md) and [docs/explanation/architecture.md](docs/explanation/architecture.md).

Outside the house, five tools share the shape of a review step before agent work moves. Each is real competition. The trade-off that keeps kettle is in parentheses.

- crt: approval is a watermark on what changed since the last approval. Kettle's approve records a ruling. Sweep then stages it to `.kettle/outbound/`.
- Stage: the agent splits its branch into chapters and opens a local browser review before a pull request exists. Kettle's queue is the desk of ordinary files, not a chapter split of a branch.
- Parley: GitHub-style review, local, in a terminal. Kettle's reference sitting is the web desk. The terminal is not a public-preview gate. See [docs/reference/release-gates.md](docs/reference/release-gates.md).
- AgentClick: a browser review layer between "agent proposes" and "agent executes," and the agent continues after approval. Kettle's approve does not continue the agent.
- OACP: a plain-file review queue whose states are review request, feedback, addressed, and lgtm. This is the closest analogue to a `.kettle/` desk. Kettle keeps one core as the authority for those semantics, and sweep stages to `.kettle/outbound/` rather than stopping at an agent-to-agent lgtm. It does not apply a refusing policy. See [docs/explanation/architecture.md](docs/explanation/architecture.md).

## Design

Core owns product semantics, desk format and migrations, the localhost API, the CLI, kits, and the reference web UI. The editor owns activation and packaging. Adapters do not fork the desk format. A cross-repository change lands in core first, with a compatible contract, then in the adapters that need it. New projects store the desk in `.kettle/`. `desk_dir` in kettle-core `kettle/server.py` at `3bab46b` returns `.kettle` when it exists, and otherwise an existing `.setsweep` desk. Both use the same queue. The fallback carries a legacy `approved` entry forward until something resets it to `pending`. The code does not reset it.

What sweep checks today is `status == "approved"` on an inbox entry. It then stages that entry to `.kettle/outbound/`. No policy gates that step. `settings.egress.routes` overlays route hints. It does not make sweep refuse an item. Kettle's guarantee ends at `.kettle/outbound/`. The pickup past that directory is unowned. A refusing policy is Later, which is roadmap constraint 3 in [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

Bets on a single user: the localhost API, one `.kettle/` directory per project, and one ruling recorded per item. What still holds if a second reviewer is on the same machine: the desk stays ordinary files, approve stays a record, and sweep still stages to `.kettle/outbound/`. What does not hold is a shared remote desk.

Localhost safety, on this bar, is Host, Origin, and token checks against other origins. `check_request_guards` in `kettle/server.py` at `3bab46b` runs on every `/api/` POST, including `/api/approve`, with the token required. It does not fence a process running as the same user. The gate row is in [docs/reference/release-gates.md](docs/reference/release-gates.md).

## Evidence

The claim and the private-preview status are in [README.md](README.md). Commit [6337dea](6337dea) named that private preview. `origin/main` at the base of this branch is [0fcfb42](0fcfb42). The thesis revision is on `defend/2026-10-11`.

The code these statements rest on is kettle-core `3bab46b`: `check_request_guards` and `/api/approve` in `kettle/server.py`, and `stage_inbox_approved` called from `kettle/sweepkit.py` on the close path. That SHA is not yet a clean ship set. `G-clean` fails on the maintainer's machine for the four worktrees named in Plan. The three guard tests in the kettle-core working tree (`test_api_post_without_token_forbidden`, `test_foreign_origin_forbidden`, `test_evil_host_forbidden`) are not cited against `3bab46b`. `git grep` on that commit did not find them.

The preview bar and the manual dogfood list are in [docs/reference/release-gates.md](docs/reference/release-gates.md). The gate script is [scripts/release-ready.sh](scripts/release-ready.sh). It fails `G-approve-scope` until core contains `test_approve_writes_only_queue`. The passing stdout is not in this tree yet. It will live in [docs/reference/preview-record.md](docs/reference/preview-record.md). The stranger pass uses `kettle --web`, the README command on `0fcfb42`. The tutorial's `.venv/bin/kettle --web` is the drift named in Risks.

This repository does not contain a written record that the manual dogfood has been walked. The preview is not claimed ready here.

## Risks and open questions

An agent that can write `.kettle/queue.json` can set `status` to `approved`. Sweep will stage that entry. The ruling carries no digest of the brief or the diff. This sinks the sentence that a person recorded the ruling. What closes it is a core-written ruling carrying that digest, refused by sweep on mismatch. The preview may ship before that exists, because the one-pass appetite does not include inventing it. The token in `~/.cache/kettle/server.json` fences a browser that does not have that file. It does not fence an agent running as the same user.

`settings.json` beside the project registry is writable by that same agent. Sweep does not read it as a permission. Kettle's guarantee ends at `.kettle/outbound/`. The pickup past that directory is unowned.

A legacy `.setsweep` desk uses the same queue. An old `approved` entry stays live on first sweep. It should become `pending` on first Kettle read. The code does not do that.

The live gate must see `"app": "kettle"`. [scripts/release-ready.sh](scripts/release-ready.sh) now requires that. The preview record must carry `kettle --version` and the SHA of the tree the binary was installed from. I don't know whether `/api/ping` returns a commit, or whether today's `~/.local/bin/kettle` is `3bab46b`.

Brief quality is untested. The preview bar proves the loop runs, not that a person can judge from the brief. The word for the human act is "ruling". The tutorial still says "bookmark" at [docs/tutorials/first-sitting.md](docs/tutorials/first-sitting.md). Install copy has drifted: `kettle --web` on `0fcfb42`, `.venv/bin/kettle --web` in the tutorial, and `kettle-web` on the dirty checkout `695f25b`. Palette drift between the reference sitting and the editor webview is an open question. LAB-43 is the owner decision. No check fails when the palettes diverge.

Unknown: whether a person remains the default reviewer. If next year's users want an agent to make the routine rulings, a desk that requires a human ruling on every item becomes the exception queue. The answer that keeps the claim is that the human ruling stays the default. The evidence that would decide it is a dogfood count of rulings a human marked trivial. That count is not in this repository.

## Scope

In: the public-preview bar in [docs/explanation/roadmap.md](docs/explanation/roadmap.md) (Now) and [docs/reference/release-gates.md](docs/reference/release-gates.md). That is install, a stored strict live run, a stranger dogfood on the two steps in Plan, docs, and staying private until the pre-flip step is written. Viewports on that bar: the reference web UI, and VS Code and Cursor. Localhost safety is in, and it means Host, Origin, and token checks against other origins. It does not mean protection from a same-user process. The gate row is in the release definition.

Out, for this bar: the macOS shell. It sits on Next, beside packaging, a marketplace listing, code signing, and notarization. `npm test` in kettle-desktop is evidence for that later bar, not for public preview. No sitting of Kettle.app is recorded, and an unsigned shell is the viewport a stranger is least able to open. Obsidian, a general MCP bridge, and remote or multi-user use are Later. An experimental terminal viewport is not a row in the public-preview gate table. A versioned sitting-judge is not on that table either. A refusing sweep policy is Later.

## Plan

The order is the roadmap order: Now (trustworthy public preview), then Next (dependable distribution), then Later (evidence-led adapters). See [docs/explanation/roadmap.md](docs/explanation/roadmap.md).

Progress starts by bringing four worktrees clean, owned by coord-kettle: product-home `d94d5df` (parent `0fcfb42`), kettle-core `3bab46b`, kettle-vscode `05d03d9`, kettle-desktop `origin/main` `280f488`. Not the unmerged desktop fix branch. `G-clean` fails on the maintainer's machine for that set today. The measure, once they are clean, is `./scripts/release-ready.sh --strict --require-live` on the maintainer's machine, with stdout committed to [docs/reference/preview-record.md](docs/reference/preview-record.md). [docs/reference/release-gates.md](docs/reference/release-gates.md) requires that file. The core pytest run includes `test_approve_writes_only_queue`. [scripts/release-ready.sh](scripts/release-ready.sh) runs that test by node id and fails `G-approve-scope` when it is missing, skipped, xfailed, or does not pass exactly once.

The stranger pass is two steps. (1) Pre-flip: Charles, on the maintainer's machine, in a fresh user account, installs those SHAs from the written instructions. The source reaches that account by a collaborator grant on the private repositories. That is not the public path. The install command is `kettle --web`. The pre-flip pass diffs the README and tutorial install lines. I don't know a grant that exists for that account today. (2) Post-flip: within seven days, coord-kettle, on the maintainer's machine, in a fresh user account that is not logged in to GitHub, runs `git -c credential.helper= clone` of the same SHAs and `kettle doctor`. `gh auth status` in that account must fail before the clone. If the clone or `kettle doctor` fails, the repositories go back to private. Going back to private does not recall clones already taken, so the public-surface check belongs in step 1.

There is no cap that stops the project. The appetite stops the public flip only. One maintainer pass is step 1. It is not a price for every item under Now, and it is not the fifteen minutes of the first-sitting lesson. If that pass is spent without the preview record, the repositories stay private and other work may continue. The desk is already a private instrument.

The plan assumes next year is still a local single-user desk with thin viewports. The record in this repository for that assumption is none. [docs/explanation/roadmap.md](docs/explanation/roadmap.md) puts a hosted multi-user product on Later, and it does not name a second person who has ruled on one desk. Tripwire: a second person records a ruling on one desk during dogfood, or a stranger's issue asks to share a desk. Either event reopens the assumption before Later. Design sorts the bets. Localhost, one `.kettle/` directory, and one ruling per item are single-user bets. Ordinary files, approve-as-record, and sweep-to-`outbound/` still hold for a second reviewer on the same machine. A shared remote desk does not. This repository does not contain a threat model for that other assumption.

## Evaluation record

Date: 2026-10-12
Chair: director
Advisor: scholar (Futurist)
Committee: security (Skeptic), operator (Operator), designer (Designer), builder (Economist)
Candidate: live owner
Result: Pass
Points: green 3 · yellow 0 · red 0
Positions: green 12 · yellow 0 · red 0
Count: procedural, not cryptographic (one uid on this house)
Ballot: sha256 dc7f2049c17019de5537e4857ab7d70555f206c09070237578999cd49c923d61
Open questions: 26 (ids added when courier files them)
