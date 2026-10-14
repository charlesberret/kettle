# Product-home charter

This repository is the public home and star target for Kettle. It owns the
product story, family navigation, public roadmap, release definition, and
community documents. It does not contain runtime or adapter code.

Implementation belongs in the repository that releases it:

- [`kettle-core`](https://github.com/charlesberret/kettle-core) for the Desk,
  contracts, runtime, CLI, kits, and reference web UI;
- [`kettle-vscode`](https://github.com/charlesberret/kettle-vscode) for VS Code
  and Cursor host behavior;
- [`kettle-desktop`](https://github.com/charlesberret/kettle-desktop) for the
  Electron lifecycle and macOS packaging (the sitting is core’s).

How those stay in lockstep: [viewports](./viewports.md).

The canonical family boundary is
[architecture](./architecture.md). Docs in this repo follow
[Diátaxis](../README.md). Each implementation repository should link back rather
than restating the public product strategy.
