# Contributing to Kettle

Thanks for taking an interest in Kettle.

## Choose the owning repository

| Change | Repository |
|---|---|
| Product story, roadmap, or family navigation | `kettle` |
| Desk, API, runtime, CLI, kits, or reference web UI | `kettle-core` |
| VS Code or Cursor behavior | `kettle-vscode` |
| Electron lifecycle or macOS packaging | `kettle-desktop` |

Read [`docs/explanation/architecture.md`](./docs/explanation/architecture.md) before a cross-repository change. Core contracts land first; adapters follow. Doc map (Diátaxis): [`docs/README.md`](./docs/README.md). Expanded steps: [`docs/how-to/contribute.md`](./docs/how-to/contribute.md).

## Proposing work

- Search existing issues before opening a new one.
- Use a bug report for reproducible behavior.
- Open a discussion issue before a substantial feature, new adapter, contract break, or Desk migration.
- Keep pull requests focused and include tests or explicit manual evidence.

Each implementation repository contains its own development commands. From the product home, run:

```sh
python3 scripts/check-docs.py
./scripts/release-ready.sh
```

By contributing, you agree that your contribution is licensed under the [MIT License](./LICENSE). Participation is governed by the [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).
