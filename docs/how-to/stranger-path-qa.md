# How to run a stranger-path dogfood pass

**Goal:** Prove a newcomer can install Kettle from public instructions, found a Desk, review an entry, comment, approve, and sweep — without maintainer-only knowledge, private workshop notes, or unpublished tooling.

**Audience:** Contributors preparing a public preview, or anyone verifying the roadmap’s stranger-path bar.

**Not this guide:** A first lesson ([tutorial: first sitting](../tutorials/first-sitting.md)) or automated family gates ([check release readiness](./check-release-readiness.md)). This is a **manual checklist**. Record pass/fail and notes; do not treat a green `release-ready.sh` as a substitute.

**Port note:** Starting the web sitting binds `127.0.0.1:4242`. Run that step yourself on your machine. Do **not** start servers on port 4242 from agent or CI automation.

---

## Prerequisites (public only)

Use only what a stranger can clone and read:

| Need | Where |
|------|--------|
| Python 3.11+ | Local install |
| Supported curator CLI, already authenticated | [kettle-core INSTALL](https://github.com/charlesberret/kettle-core/blob/main/INSTALL.md) (default: `claude`) |
| Public clone of **kettle-core** | [github.com/charlesberret/kettle-core](https://github.com/charlesberret/kettle-core) |
| Product story / family map (optional context) | This repo’s [docs map](../README.md) |

Do **not** rely on: shared workshop machines, private `.local/` notes, pre-seeded registries, or hand-copied Desk trees from a maintainer.

Pick a **throwaway project folder** under your home directory that you do not mind Kettle writing Desk files into (`.kettle/`, or an existing `.setsweep/` if you are exercising legacy fallback).

---

## 1. Clean install (editable + canonical venv)

Follow the durable install in [kettle-core `INSTALL.md`](https://github.com/charlesberret/kettle-core/blob/main/INSTALL.md) (preferred over a one-off repo `.venv` when dogfooding “installable”).

```sh
git clone https://github.com/charlesberret/kettle-core.git
cd kettle-core
python3 -m venv ~/.kettle-venv
~/.kettle-venv/bin/pip install -e .
```

Optional PATH shim (exactly one winner — see INSTALL for hygiene):

```sh
ln -sf ~/.kettle-venv/bin/kettle ~/.local/bin/kettle   # dir must be on PATH
hash -r
which -a kettle   # expect a single path pointing at the venv binary
```

If you skip the shim, use `~/.kettle-venv/bin/kettle` for every command below.

Checklist:

- [ ] Clone and editable install succeeded with no private credentials
- [ ] `kettle` (or the venv binary) starts and prints help (`kettle --help`)
- [ ] You did not need unpublished packages or workshop-only steps

---

## 2. `kettle doctor`

```sh
kettle doctor
```

Checklist:

- [ ] Doctor runs and reports which `kettle` wins on `PATH`
- [ ] Doctor reports the install is usable (or clearly states what to fix in    public terms — PATH hygiene, reinstall after `py-modules` change)
- [ ] Doctor never deletes PATH entries or “repairs” the machine silently

If doctor fails in a way public docs do not explain, that is a **product docs bug** — file it (see [Reporting failures](#reporting-failures)).

---

## 3. Register a project and found a Desk

Register a real folder (not a fictional path):

```sh
kettle add ~/path/to/a-real-project
kettle projects
```

**Founding** creates the Desk charter and content queue. Prefer the path a stranger sees first:

1. Start the web sitting **yourself** (user-run only):

   ```sh
   kettle --web
   ```

   Open [http://127.0.0.1:4242](http://127.0.0.1:4242).

2. Select the project and complete the **founding interview** in the agent pane until you accept a proposal and found the Desk.
3. Confirm Desk files appear under the project (`.kettle/` for new desks; existing `.setsweep/` remains in place until an explicit migration).

Terminal-only alternative (if the CLI surface is what you are validating):

```sh
kettle found <project>
```

Use `kettle <cmd> --help` for flags; do not invent workshop shortcuts.

Checklist:

- [ ] Project appears in `kettle projects`
- [ ] Founding interview / `found` completes without maintainer coaching
- [ ] Desk notes / charter files are present and readable on disk
- [ ] A content queue exists after founding (or the UI clearly says what is next)

---

## 4. Review, comment, approve, sweep

Work one queue entry end-to-end. Shell companions:

```sh
kettle queue <project>
kettle open <project> <id>    # opens in $EDITOR when configured
kettle chat <project> [id]    # optional; curator must already be authenticated
kettle sweep-status <project>
```

In the sitting UI (web, or an optional adapter below):

1. Open a queue entry and read the **brief**.
2. Edit the file if the brief warrants it.
3. Leave a **comment** for the sweep (at least one sentence).
4. **Approve** when your ruling is done.
5. Run a **sweep** and confirm Desk / queue state afterward.

Hard product rules to verify (not optional flavor):

| Rule | What “pass” looks like |
|------|-------------------------|
| Approve is a bookmark | Approving records a ruling; it does **not** by itself apply work, push Git, or transmit egress |
| Sweep applies under policy | Sweep is an explicit step; afterward queue / Desk files reflect the sitting |
| Desk stays inspectable | You can point at ordinary files under `.kettle/` (or legacy `.setsweep/`) that match what the UI showed |

Checklist:

- [ ] Entry brief is understandable without prior workshop context
- [ ] Comment is stored and visible on a later open (or in Desk files)
- [ ] Approve succeeds and does **not** silently publish or apply
- [ ] Sweep runs and Desk / Git (or staged) state matches what public docs claim
- [ ] `kettle sweep-status <project>` (or the UI equivalent) is coherent after the pass

---

## 5. Optional viewport checks

Core CLI + browser are enough to pass the stranger-path bar. Adapters are extra evidence for a fuller preview.

### Web sitting (`:4242`) — user-run only

- [ ] `kettle --web` serves the UI on [http://127.0.0.1:4242](http://127.0.0.1:4242)
- [ ] Same project / queue / rulings as the CLI for that Desk
- [ ] No agent or CI process was used to bind port 4242

### VS Code / Cursor

From public [kettle-vscode README](https://github.com/charlesberret/kettle-vscode):

```sh
git clone https://github.com/charlesberret/kettle-vscode.git
cd kettle-vscode
npm ci
npm test
npm run package
code --install-extension kettle-0.1.0.vsix --force   # or cursor --install-extension …
```

- [ ] Extension installs from the built VSIX
- [ ] **Kettle: Ping Core** succeeds (auto-start or attach to a healthy local core)
- [ ] If auto-start cannot find the CLI, setting `kettle.command` to    `~/.kettle-venv/bin/kettle` (absolute path) is documented and works
- [ ] Queue, comment, approve, and sweep are usable against the same Desk

### Desktop (macOS)

From public [kettle-desktop README](https://github.com/charlesberret/kettle-desktop):

```sh
git clone https://github.com/charlesberret/kettle-desktop.git
cd kettle-desktop
npm ci
npm test
npm start
```

- [ ] App attaches to a healthy core on `:4242`, or starts an owned sidecar
- [ ] Sitting shows queue · editor · desk ritual (Approve · Comment · Sweep)
- [ ] Quit does not kill a core process the app did not start

---

## Pass criteria (summary)

You may mark the stranger-path dogfood **PASS** when all of the following are true from public docs alone:

- [ ] Clean editable install + usable `kettle doctor`
- [ ] Real project registered; Desk founded with interview notes / charter on disk
- [ ] One entry reviewed with comment + approve + sweep
- [ ] Approve-vs-sweep semantics hold (ruling ≠ outward execution)
- [ ] Failures, if any, are reportable via public channels below

Optional adapter checks may be **SKIP** for a core-only pass; note that explicitly when filing release evidence ([release gates](../reference/release-gates.md)).

---

## Reporting failures

| Kind | Where |
|------|--------|
| Suspected vulnerability | Private advisory — root [`SECURITY.md`](../../SECURITY.md) (links each family repo) |
| Code-of-conduct / community harm | Same private channel; identify as a conduct matter ([`CODE_OF_CONDUCT.md`](../../CODE_OF_CONDUCT.md)) |
| Product bug or docs gap (stranger blocked) | Public issue on the **owning** repo — see [contribute](./contribute.md) |
| Release-bar evidence | Attach this checklist’s pass/fail notes when cutting a preview |

When filing a stranger-path failure, include: OS, Python version, commit or clone date of kettle-core, exact public command sequence, and where public docs were silent or wrong. Do not paste private project contents unless essential.

---

## Related

- [Tutorial: first sitting](../tutorials/first-sitting.md) — gentler first success
- [How to check release readiness](./check-release-readiness.md) — automated gates
- [Reference: release gates](../reference/release-gates.md) — manual dogfood bar
- [Explanation: roadmap](../explanation/roadmap.md) — “trustworthy public preview”
- Core install: [INSTALL.md](https://github.com/charlesberret/kettle-core/blob/main/INSTALL.md)
