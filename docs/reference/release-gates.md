# Kettle release definition

A Kettle release is a named bar with automated evidence and a short manual
dogfood record. Source-ready does not mean a package or marketplace listing
already exists.

Run the local automated gates from this repository with sibling checkouts:

```sh
./scripts/release-ready.sh
./scripts/release-ready.sh --strict
```

## Public preview

The first public preview is ready when:

| Gate | Evidence |
|---|---|
| Home documents are internally linked | `python3 scripts/check-docs.py` |
| Core behavior is green | full `pytest` suite |
| Canonical and legacy CLI names start | isolated editable-install smoke |
| Editor behavior is green | `npm test` in `kettle-vscode` |
| Editor package is buildable | `npm run package` |
| Shared visible copy has not drifted | `npm run check-ui-copy` |
| Desktop shell logic is green | `npm test` in `kettle-desktop` |
| Repositories agree on contracts | `kettle-core/tools/check_family.py` |
| Release inputs are reproducible | all publishable Git worktrees clean |
| Source is publicly reachable | family links and clone commands work without authentication |

Manual release evidence (executable checklist:
[stranger-path QA](../how-to/stranger-path-qa.md)):

- install from the public instructions on a clean machine or user account;
- found or open a real Desk;
- review, edit, comment, and approve an entry;
- verify approval does not itself apply or transmit work;
- sweep and confirm the resulting Desk and Git state;
- inspect the packaged VSIX in VS Code or Cursor;
- verify repository descriptions, topics, issue forms, licenses, and private
  vulnerability reporting on GitHub;
- confirm public copy does not claim unsigned or unpublished artifacts exist.

## Distribution bars

| Bar | Additional evidence |
|---|---|
| Core package | wheel contents, clean virtual-environment install, supported Python matrix |
| Editor marketplace | live activation, declared permissions, icon and listing, rollback plan |
| macOS application | exact core provenance, packaged smoke, signing, notarization, update plan |

Viewport package versions do not need to match. Compatibility is governed by
the API and Desk-schema contracts published by core and declared by adapters.

## Compatibility removal

Setsweep command aliases, process identity, registry lookup, and `.setsweep/`
fallback must remain until:

1. an explicit migration command exists;
2. its dry-run and rollback behavior are tested;
3. supported adapters read the migrated state;
4. a deprecation window has been published.
