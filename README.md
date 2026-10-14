# Kettle

**A local-first review desk that promotes careful attention to projects coded and written with agents.*

Agents can work very quickly, but the more they accomplish, the harder it is to keep track new material that calls for direct editing and verification before it becomes entrenched as project dogma.

Kettle gathers your coding agent's work and curates it inbatches with contextual briefs worth reading. When you review, edit, and approve a batch, the Kettle agent records your rulings, learning more about you and your projects through the changes you make each round.

Kettle is free software available as a command line utility, standalone desktop app for Mac, and plugin for Cursor, Herdr, and VS Code.

```text
agent work  →  queue  →  edit, comment, approve  →  sweep
                                      human judgment
```

Kettle keeps its Desk in ordinary files inside your project. A local Python core serves the same queue to the terminal, desktop app, browser, and plugins.

## Status

Kettle is a **pre-release project being prepared for a public open-source preview**. Its GitHub repositories are currently private while the first release is assembled. 

The core, VS Code/Cursor extension, and desktop shell are implemented and tested from source. Package registries, the Visual Studio Marketplace, code signing, and notarization are still ahead.

The current preview is best suited to contributors and curious folks who are comfortable with a local Python installation.

## Try the core

Kettle requires Python 3.11 or newer and a supported agent CLI with its own authentication already configured.

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

The CLI ships with `kettle-core`; there is no separate CLI package. Obsidian and MCP adapters are ideas for later, not empty products presented as shipped.

Core is the single authority for product semantics. Adapters consume its versioned localhost contract and do not fork the Desk or its migrations. See [`docs/explanation/architecture.md`](./docs/explanation/architecture.md) for the boundary. Documentation is organized with [Diátaxis](./docs/README.md) (tutorials, how-tos, reference, explanation).

## What Kettle protects

- **Human judgment stays explicit.** Approving a file  records a ruling, but does not silently apply or publish changes to your work.
- **The Desk stays inspectable.** Queue, memory, policy, and staged egress are files under the project.
- **Outbound actions are staged.** Email, Slack, webhooks, and launches are prepared for review rather than transmitted by surprise.
- **Provider credentials stay with provider tools.** Kettle does not collect or store API keys.
- **Adapters stay thin.** The terminal, browser, editor, and desktop shell see the same core state.

## Documentation

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
