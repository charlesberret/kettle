# Soft release plan

A soft release is not a launch campaign. It is: claim the quiet infrastructure
slots we will need, keep public copy honest, dogfood until a stranger can
succeed, then publish packages and make a small, targeted noise.

This page is the channel checklist. Product sequencing lives in the
[roadmap](./roadmap.md); the hard bars live in
[release gates](../reference/release-gates.md).

## Decision bar

| Question | If no | If yes |
|---|---|---|
| Can a stranger install from **public** instructions and complete [stranger-path QA](../how-to/stranger-path-qa.md)? | Keep dogfooding. Do not announce. | Source preview is allowed. |
| Do family repos, clone URLs, and docs work **without auth**, with no claims about unpublished artifacts? | Fix home/docs first ([release gates](../reference/release-gates.md)). | Okay to point people at GitHub. |
| Is core installable from a **published** Python package (not only editable source)? | Soft source preview only; say so in the README. | Okay to pitch “pip install”. |
| Is the editor extension live on a **marketplace** (or Open VSX) with smoke-tested activation? | Ship VSIX-from-source only; no marketplace posts. | Okay to pitch editor install. |
| Do we have bandwidth to answer issues for a week after a post? | Post nowhere public yet. | One small post is fine. |

**Rule of thumb:** reserve names and accounts early; publish packages when the
matching distribution bar in [release gates](../reference/release-gates.md)
passes; announce only what a stranger can actually install today.

Do **not** treat a green `./scripts/release-ready.sh` as permission to shout.
That script covers automated family gates, not marketplace truth or stranger
success.

## Do now

Cheap, mostly reversible prep. None of this requires a public buzz.

### Names and accounts

- [ ] Confirm and reserve the **PyPI** project name for core (and any deliberate
  redirects/aliases you intend to own).
- [ ] Create / verify the **Visual Studio Marketplace** publisher and the
      planned extension ID for `kettle-vscode`.
- [ ] Create / verify an **Open VSX** publisher (Cursor and other hosts often
      resolve here).
- [ ] List any other IDs you care about (GitHub Topics, future Homebrew tap or
      cask name, npm scope if you ever publish shared TS clients) — reserve only
      what you will maintain; skip empty shells.
- [ ] Keep macOS signing certificates and notarization identity documented
      privately; do not announce desktop downloads until that bar is real.

### Public surface (quiet)

- [ ] Make the family repositories public only when clone links and cross-repo
      docs work unauthenticated (roadmap “trustworthy public preview”).
- [ ] Finish GitHub descriptions, topics, issue templates, SECURITY contact, and
      license on each repo.
- [ ] Keep README **Status** accurate: source preview vs pip vs marketplace vs
      signed app — never imply a channel that does not exist yet.
- [ ] Prefer this product-home repo as the star/README target; implementation
      repos link back here.

### Dogfood before buzz

- [ ] Run [stranger-path QA](../how-to/stranger-path-qa.md) on a clean machine
      or account; record pass/fail outside the workshop lore.
- [ ] Recruit a small private circle (maintainers + a few agent-toolchain users)
      to use Kettle on real work for more than one sitting.
- [ ] File the friction that blocks strangers as issues in the owning repo;
      fix those before any public post.

## Do when ready

Only after the matching row in the decision bar is yes.

### Publish

- [ ] Publish **kettle-core** to PyPI with a repeatable release path (wheel,
      supported Python matrix, clean venv install).
- [ ] Publish **kettle-vscode** to Marketplace and/or Open VSX after live-host
      smoke (activation, permissions, icon, listing, rollback).
- [ ] Update product-home and core install docs to the published commands;
      remove “build from source only” language where it no longer applies.
- [ ] Cut a named preview (tag + short notes) so people can cite a version.

### Tell people (small circle first)

Post **once**, with the install path that works today, and stay for questions.
Prefer communities where agent review / local-first tooling is already the
topic — not generic “Show everything” spam.

| Channel | When it fits |
|---|---|
| Private / invite circle | Always first; learn what breaks. |
| Own blog / short note linked from GitHub | When source or packages are public and honest. |
| Show HN or similar | After stranger-path **PASS** and a one-command (or clearly documented) install. |
| Cursor / VS Code extension communities | After marketplace or Open VSX listing is live. |
| Python packaging / local-tools lists | After PyPI install works on a clean machine. |
| Agent-toolchain Discords, forums, newsletters | Soft pointer, not a launch thread — and only if you will answer. |

Skip or defer: paid ads, large Twitter/LinkedIn blasts, Product Hunt-style
launches, and any post that demos desktop until signing/notarization and
updates are supportable.

## Later

Do not block the soft release on these.

- Signed and notarized **kettle-desktop** distribution and auto-update.
- Homebrew (or similar) once desktop or a stable CLI bottle is worth supporting.
- Obsidian / MCP adapters — only with a real dogfood workflow
  ([roadmap](./roadmap.md); MCP threat and scope: [MCP bridge](./mcp-bridge.md)).
- Broad press or multi-channel launch week.
- Remote / multi-user stories (separate threat model).

## Related

- [Roadmap](./roadmap.md) — product sequencing
- [Release gates](../reference/release-gates.md) — preview and distribution bars
- [Check release readiness](../how-to/check-release-readiness.md) — automated gates
- [Stranger-path QA](../how-to/stranger-path-qa.md) — manual dogfood checklist
