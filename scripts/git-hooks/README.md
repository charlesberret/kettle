# Git hooks (Kettle family)

| Hook | Role |
|------|------|
| `commit-msg` | Enforce [`docs/COMMIT.md`](../../docs/COMMIT.md) message shape |

## Install (this repo)

```sh
cd /path/to/kettle
./scripts/install-git-hooks.sh
```

Uses `git config core.hooksPath scripts/git-hooks` (repo-local).

## Install for another family repo

```sh
# Option A — point at the home repo hooks (shared)
cd /path/to/kettle-vscode
git config core.hooksPath /path/to/kettle/scripts/git-hooks

# Option B — copy hooks into that repo and run its installer if present
```

Hooks must be executable (`chmod +x commit-msg`).

## Skip once (escape hatch)

```sh
git commit --no-verify -m "..."
```

Prefer fixing the message over skipping.
