# How to contribute a change

**Goal:** Land a focused change in the correct Kettle repository.

## 1. Choose the owner

| Change | Repository |
|--------|------------|
| Product story, docs map, roadmap, release definition | `kettle` (this repo) |
| Desk, API, runtime, CLI, kits, reference web UI | `kettle-core` |
| VS Code / Cursor behavior | `kettle-vscode` |
| Electron / macOS packaging | `kettle-desktop` |

Read [architecture](../explanation/architecture.md) before a cross-repo change.
**Core contracts land first;** adapters follow.

## 2. Branch and implement

- Keep the PR focused.  
- Match [commit conventions](../reference/commit-conventions.md).  
- Include tests or explicit manual evidence.

## 3. Check before you open a PR

From product home (with siblings present as needed):

```sh
python3 scripts/check-docs.py
./scripts/release-ready.sh
```

Run the owning repo’s test suite as well (`pytest`, `npm test`, …).

## 4. Open the PR

- Search existing issues first.  
- Use a bug report for reproducible failures.  
- Discuss substantial features, new adapters, or contract breaks before a large PR.

## Related

- Root [`CONTRIBUTING.md`](../../CONTRIBUTING.md)  
- [Code of conduct](../../CODE_OF_CONDUCT.md)  
- [Release gates](../reference/release-gates.md)  
