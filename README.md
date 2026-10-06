# Kettle

**A local-first review desk for work made with coding and writing agents.**

Agents can prepare a great deal of work very quickly. Kettle gives that work a
place to wait, a brief worth reading, and a clear human ruling before anything
moves outward.

```text
agent work  →  curated queue  →  read, edit, comment, approve  →  sweep
                                      human judgment
```

Kettle keeps its Desk in ordinary files inside your project. A local Python
core serves the same queue to the terminal, browser, VS Code, Cursor, and a
small macOS shell.

## Status

Kettle is a **pre-release project being prepared for a public open-source
preview**. Its GitHub repositories are currently private while the first
release is assembled. The core, VS Code/Cursor extension, and desktop shell are
implemented and tested from source; package registries, the Visual Studio
Marketplace, code signing, and notarization are still ahead.

The current preview is best suited to contributors and curious early users who
are comfortable with a local Python installation.

## Try the core

Kettle requires Python 3.11 or newer and a supported agent CLI with its own
authentication already configured.

```sh
git clone https://github.com/charlesberret/kettle-core.git
cd kettle-core
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/kettle doctor
.venv/bin/kettle-web
```

Open [http://127.0.0.1:4242](http://127.0.0.1:4242), add a project folder, and
complete the founding interview. Terminal users can start with:

```sh
kettle add ~/path/to/project
kettle queue <project>
kettle chat <project>
```

For editor installation, build
[`kettle-vscode`](https://github.com/charlesberret/kettle-vscode) and install
its VSIX.

## The Kettle family

Each repository is an independent release unit with a narrow owner:

| Repository | Owns | Current state |
|---|---|---|
| **[`kettle`](https://github.com/charlesberret/kettle)** | Product home, public roadmap, family navigation | This repository |
| **[`kettle-core`](https://github.com/charlesberret/kettle-core)** | Desk format, API, runtime, CLI, kits, reference web UI | Source preview |
| **[`kettle-vscode`](https://github.com/charlesberret/kettle-vscode)** | VS Code and Cursor viewport | VSIX builds from source |
| **[`kettle-desktop`](https://github.com/charlesberret/kettle-desktop)** | Thin macOS Electron shell and packaging | Development build, unsigned |

The CLI ships with `kettle-core`; there is no separate CLI package. Obsidian
and MCP adapters are ideas for later, not empty products presented as shipped.

Core is the single authority for product semantics. Adapters consume its
versioned localhost contract and do not fork the Desk or its migrations. See
[`docs/explanation/architecture.md`](./docs/explanation/architecture.md) for the
boundary. Documentation is organized with
[Diátaxis](./docs/README.md) (tutorials, how-tos, reference, explanation).

## What Kettle protects

- **Human judgment stays explicit.** Approve records a ruling; it does not
  silently apply or publish work.
- **The Desk stays inspectable.** Queue, memory, policy, and staged egress are
  files under the project.
- **Outbound actions are staged.** Email, Slack, webhooks, and launches are
  prepared for review rather than transmitted by surprise.
- **Provider credentials stay with provider tools.** Kettle does not collect or
  store model API keys.
- **Adapters stay thin.** The terminal, browser, editor, and desktop shell see
  the same core state.

## From Setsweep to Kettle

Kettle is the continuation of Setsweep. The rename does not strand existing
work:

- new projects use `.kettle/`;
- an existing `.setsweep/` Desk is used in place until an explicit migration;
- `kettle` is canonical, while legacy `setsweep` command aliases remain
  temporarily available;
- branding alone does not change the API or Desk-schema contract versions.

New public copy and new state use Kettle. Legacy names remain only where they
provide deliberate compatibility or preserve historical attribution.

## Project documents

Documentation uses [Diátaxis](./docs/README.md):

- [Docs map](./docs/README.md)
- [Architecture](./docs/explanation/architecture.md)
- [Roadmap](./docs/explanation/roadmap.md)
- [Release gates](./docs/reference/release-gates.md)
- [First sitting (tutorial)](./docs/tutorials/first-sitting.md)
- [Contributing](./CONTRIBUTING.md)
- [Security policy](./SECURITY.md)

Run the local family gates with sibling checkouts:

```sh
./scripts/release-ready.sh
./scripts/release-ready.sh --strict
```

## License

[MIT](./LICENSE)
