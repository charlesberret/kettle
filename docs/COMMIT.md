# Commit conventions (Kettle family)

**Status:** settled for the family (2026-07). Same rules in `kettle`, `kettle-core`,
`kettle-vscode`, desktop, and later adapters unless a repo documents an exception.

## Message format

```text
<optional-type>: <imperative subject>

<body — why, not every file list>

<footer — optional trailers>
```

### Subject

- **Imperative mood**, present tense: “Add…”, “Fix…”, “Document…”, not “Added” / “Fixes”
- **≤72 characters** (soft); hard fail if **>100**
- **Capitalize** first letter; **no trailing period** on the subject line
- One logical change per commit when practical

### Optional type prefix (recommended)

Conventional-commits–style, lowercase, optional scope:

| Type | Use |
|------|-----|
| `feat` | User-visible capability |
| `fix` | Bug fix |
| `docs` | Docs / briefs / README only |
| `chore` | Tooling, ignore rules, scaffolding |
| `refactor` | No intended behavior change |
| `test` | Tests only |
| `ci` | CI / release gates / hooks |
| `style` | Formatting only |

Examples:

```text
docs: add release gates and workflow

chore(vscode): ignore .local for ops notes

fix(core): prefer .kettle desk path over legacy

feat(cli): add --json to queue listing
```

Bare subjects without a type are still OK for early scaffolding:

```text
Initial Kettle scaffold
```

### Body

- Separate from subject with a **blank line**
- Wrap ~72–100 chars; explain **why** and any migration/compatibility notes
- Bullet lists fine

### Footers (optional)

```text
Brief: 01
Gate: G-core-test
Co-authored-by: …
```

Link work packages and release gates when the commit is meant to move them.

## What not to do

- Commit secrets, `.local/`, or machine paths that shouldn’t be public  
- Mix unrelated refactors with a feature fix  
- “WIP” / “fix stuff” as the final message on `main` (amend or squash first)  
- Force-push `main` without an explicit human ask  

## Automation

Install the family **commit-msg** hook (validates subject length, forbids subject
trailing period when using a type prefix, blocks empty messages):

```sh
# from any family repo that vendors scripts/git-hooks/
./scripts/install-git-hooks.sh
```

Or point Git at shared hooks (this home repo):

```sh
git config core.hooksPath /path/to/kettle/scripts/git-hooks
```

(`commit-msg` must be executable; see `scripts/git-hooks/README.md`.)

CI may later run the same checks on PR titles; the hook is the day-to-day enforcer.

## Agents

When creating commits for Charles:

1. Follow this file  
2. Prefer `type: subject` + short body  
3. HEREDOC in the shell so newlines survive  
4. Never update git config or force-push unless asked  

See also [`WORKFLOW.md`](./WORKFLOW.md).
