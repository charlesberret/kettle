# How to install Kettle git hooks

**Goal:** Enable the family `commit-msg` hook so commit messages match
[commit conventions](../reference/commit-conventions.md).

## From product home

```sh
cd /path/to/kettle
./scripts/install-git-hooks.sh
```

This sets `core.hooksPath` to `scripts/git-hooks` for **this** repository.

## Point another family repo at the shared hooks

```sh
cd /path/to/kettle-vscode   # or kettle-core, kettle-desktop, …
git config core.hooksPath /path/to/kettle/scripts/git-hooks
```

Hooks must be executable (`commit-msg` is shipped `chmod +x`).

## Skip once

```sh
git commit --no-verify …
```

Prefer fixing the message.

## Related

- Fleet message shape: `~/cloud/sync/system/commit-conventions.md`  
- [Reference: commit conventions](../reference/commit-conventions.md)  
