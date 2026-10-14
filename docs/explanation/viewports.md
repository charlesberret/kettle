# Viewport coordination

Kettle is one review instrument. Several hosts attach to it. They must not
grow a second product surface.

This is the family rule that keeps sitting work moving together. Implementation
detail lives in [kettle-core/docs/PLATFORMS.md](https://github.com/charlesberret/kettle-core/blob/main/docs/PLATFORMS.md)
and [UI-STRUCTURE.md](https://github.com/charlesberret/kettle-core/blob/main/docs/UI-STRUCTURE.md).

## Who owns what

| Repository | Owns | Does not own |
|------------|------|----------------|
| **kettle-core** | Desk semantics, HTTP API, CLI, kits, **reference sitting** (`static/index.html`), theme packs, `ui-copy.js` | Electron lifecycle, VS Code activation |
| **kettle-desktop** | Window, menu, hidden-inset titlebar, sidecar spawn/attach, packaging | A sitting, theme, type system, or founding flow |
| **kettle-vscode** | Host editor, Explorer queue, Desk webview, commands | A second palette brand, desk format, or ritual meaning |
| **kettle** (this repo) | Public story, family map, this contract | Runtime or adapter code |

Desktop is a **frame**. VS Code is a **host-adapted projection**. Neither is a
fork of the sitting.

## How a change travels

| You changed | Land it here first | Then |
|-------------|--------------------|------|
| Layout, chrome, light/dark, chat ink, Appearance | `kettle-core/static/index.html` (+ `themes.js` / `static/themes/`) | Desktop inherits. Packaged `.app` needs a sidecar rebuild. |
| User-visible sitting strings | `kettle-core/static/ui-copy.js` | In `kettle-vscode`: `npm run sync-ui-copy` and commit `src/uiCopy.ts`. |
| Marquee palette / iface / slots | `kettle-core/static/kettle-palette.json` and `themes.js` | In `kettle-vscode`: `npm run sync-palette`. CLI reads `theme_catalog`. |
| Region jobs, ritual, founding modes | `kettle-core/docs/UI-STRUCTURE.md` | Reference sitting, then Desk webview. Never invent a peer ritual. |
| HTTP or desk schema | `kettle-core/API.md` + contract tests | Adapter `kettle-compatibility.json`. |

If a viewport wants a behavior the others lack, **add it to the reference
sitting** (or to UI-STRUCTURE) — do not grow a parallel UI in the adapter.

## What already enforces this

- Core `tests/test_viewport_sync.py` — sibling desktop must load the sidecar
  sitting; this file’s “same core web UI” sentence must stay in PLATFORMS.
- Core `tests/test_ui_copy.py` / `tests/test_palette.py` — copy and marquee
  hexes stay aligned; VS Code snapshot matches when the tree is present.
- Desktop `test/sitting-shell.test.js` — `main.js` loads `http://127.0.0.1:<port>/`,
  not a local `app/index.html`.
- VS Code `npm run check-ui-copy` / `check-palette` — snapshots have not drifted.

A July 2026 desktop sitting fork (`app/`) is parked in
`kettle-desktop/legacy/v2-scaffold/`. Do not revive it.

## Adding a viewport

Same bar as PLATFORMS: a real host workflow, a compatibility manifest, attach
before write, a mapping onto UI-STRUCTURE regions, and no second desk store.
