#!/usr/bin/env bash
# Install Kettle family git hooks for the current repository.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS="$ROOT/scripts/git-hooks"

if [[ ! -d "$ROOT/.git" ]]; then
  echo "install-git-hooks: not a git checkout: $ROOT" >&2
  exit 1
fi

if [[ ! -x "$HOOKS/commit-msg" ]]; then
  chmod +x "$HOOKS/commit-msg"
fi

# Repo-local hooksPath (relative paths work when cwd is repo root; Git resolves
# hooksPath relative to the work tree when not absolute).
rel="scripts/git-hooks"
git -C "$ROOT" config core.hooksPath "$rel"

echo "install-git-hooks: core.hooksPath=$rel"
echo "  commit-msg → $HOOKS/commit-msg"
echo "  See docs/reference/commit-conventions.md"
