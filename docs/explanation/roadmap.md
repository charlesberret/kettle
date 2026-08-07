# Kettle roadmap

Kettle is already a working review instrument. The immediate work is to make
the current system safe, installable, understandable, and pleasant for people
outside its original workshop.

## Current baseline

- Kettle-branded core, CLI, localhost API, kits, and reference web UI
- non-destructive fallback for existing Setsweep registries and Desks
- VS Code and Cursor extension with a packageable VSIX
- thin macOS desktop shell with clean-core provenance checks
- independent repositories joined by explicit API and Desk contracts

## Now: trustworthy public preview

- Verify editable and wheel installs on supported Python releases.
- Finish Host and Origin validation for the localhost HTTP surface.
- Add a per-boot local authentication design before widening integrations.
- Run a stranger-path dogfood pass: install, found a Desk, review an entry,
  comment, approve, and sweep without maintainer-only knowledge
  ([checklist](../how-to/stranger-path-qa.md)).
- Define curator excellence around the recommended
  [Hybrid Desk Notebook](./curator-frameworks.md) and run improvement work
  against the [curator scoring benchmark](../reference/curator-scoring.md).
- Finish repository descriptions, topics, issue routing, and private
  vulnerability reporting.
- Make the source repositories public only when their cross-repository links
  and clone instructions work without authentication.

## Next: dependable distribution

- Publish the core through a repeatable Python package channel.
- Publish the VS Code/Cursor extension after live-host smoke testing.
- Add signed and notarized macOS builds only when desktop updates are
  operationally supportable.
- Add an explicit, dry-run-first migration command for Setsweep registries and
  `.setsweep/` Desks.
- Stabilize API and Desk contracts at version `1` after real adapter use.

## Later: evidence-led adapters

- Improve file watching with native notifications.
- Extract a shared client only when a second TypeScript adapter needs it.
- Build an Obsidian adapter when a concrete writing workflow is ready to
  dogfood.
- Add a narrow MCP bridge only for model-host tools that benefit from the same
  Desk. It should not replace the CLI or a full sitting.
- Consider remote or multi-user use only after a separate threat model.

## Permanent constraints

1. The Desk is ordinary, inspectable files.
2. Approve records a ruling; it is not outward execution.
3. Sweep applies rulings under explicit policy.
4. Egress stages; Kettle does not silently transmit.
5. Core owns semantics and adapters remain thin.
6. Breaking contracts advance versions and ship with migrations.
7. New repositories need a real implementation and release path.

## Soft release channels

For package-name reservations, marketplace accounts, dogfood-vs-announce
criteria, and where to post once installable, see
[soft release](./soft-release.md).
