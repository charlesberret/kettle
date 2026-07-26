# Kettle release definition

An **ideal release** is a named bar (e.g. **0.1**) defined by **gates** — checks
that are automated where possible and explicit when human.

Orchestration lives in this home repo. Implementation lives in sibling checkouts.

Run automated gates:

```sh
./scripts/release-ready.sh          # report
./scripts/release-ready.sh --strict # exit 1 if any required gate fails
```

## Release 0.1 — “Family usable”

**Intent:** You can install Kettle-named editor chrome, talk to a live core, run a
shell-first path, and complete one sitting. Legacy Setsweep names may still appear
in dual-stack form.

### Automated gates (`gate:ci` / script)

| ID | Gate | How |
|----|------|-----|
| `G-home-docs` | Home docs present | ROADMAP, RELEASE, WORKFLOW exist |
| `G-core-tree` | kettle-core is a real package tree | `pyproject.toml` + entry module or transitional layout |
| `G-core-test` | Core tests green | `pytest` in kettle-core (or documented fallback) |
| `G-vscode-test` | Extension unit tests green | `npm test` in kettle-vscode |
| `G-vscode-compile` | Extension compiles | `npm run compile` |
| `G-compat` | Compatibility manifests parse | kettle-compatibility.json (and core contract if present) |
| `G-family-layout` | Sibling paths resolvable | home, core, vscode under same parent |

### Hybrid gates (`gate:ci` + light smoke)

| ID | Gate | How |
|----|------|-----|
| `G-cli-help` | CLI responds | `kettle --help` or transitional `setsweep --help` |
| `G-core-ping` | Core reachable (if running) | optional: ping `:4242`; skip if not up unless `--require-live` |

### Manual gates (`gate:manual` / `gate:dogfood`)

| ID | Gate | Who |
|----|------|-----|
| `M-dogfood-sit` | One founding or founded sitting in kettle-vscode | Human |
| `M-cli-queue` | `queue` / status readable for a real project | Human or agent with desk |
| `M-approve-ne-apply` | Approve does not apply outward | Human checklist |
| `M-readme-honest` | READMEs don’t claim unshipped desktop/Marketplace | Human |

### Explicit non-goals for 0.1

- Notarized Mac app  
- Obsidian  
- MCP server  
- Full purge of the word “Setsweep” from kits  
- PyPI/Marketplace public listing (optional stretch)

## Later releases (sketch)

| Release | Adds |
|---------|------|
| **0.2** | Stronger CLI JSON/porcelain; chat/CLI copy parity; desk migrate command |
| **0.3** | Branding pass; optional public Marketplace; Homebrew formula draft |
| **1.0** | Stable CLI + contract; dual-read removable; desktop distribution decision |

## Mapping to issues

- Each automated gate can be an issue labeled `gate:ci` + `phase:release`  
- Use issue template **Release gate**  
- Agent work that moves a gate: template **Agent task** with `Acceptance` listing gate IDs  

## Versioning note

Viewport versions (VSIX, CLI package) need not match. Compatibility is
`api_version` + `desk_schema_version`, not marketing versions.
