#!/usr/bin/env bash
# Local, network-free validation for sibling Kettle-family checkouts.
set -euo pipefail

STRICT=0
REQUIRE_LIVE=0
for arg in "$@"; do
  case "$arg" in
    --strict) STRICT=1 ;;
    --require-live) REQUIRE_LIVE=1 ;;
    -h|--help)
      echo "Usage: release-ready.sh [--strict] [--require-live]"
      echo "  --strict         exit 1 when a required gate fails"
      echo "  --require-live   require a compatible core on 127.0.0.1:4242"
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

HOME_REPO="$(cd "$(dirname "$0")/.." && pwd)"
FAMILY_PARENT="$(cd "$HOME_REPO/.." && pwd)"
CORE_REPO="${KETTLE_CORE:-$FAMILY_PARENT/kettle-core}"
VSCODE_REPO="${KETTLE_VSCODE:-$FAMILY_PARENT/kettle-vscode}"
DESKTOP_REPO="${KETTLE_DESKTOP:-$FAMILY_PARENT/kettle-desktop}"
REPORT_DIR="$(mktemp -d "${TMPDIR:-/tmp}/kettle-release.XXXXXX")"

cleanup() {
  rm -rf "$REPORT_DIR"
}
trap cleanup EXIT

PASS=0
FAIL=0
SKIP=0

pass() {
  echo "  PASS  $1 - $2"
  PASS=$((PASS + 1))
}

fail() {
  echo "  FAIL  $1 - $2"
  FAIL=$((FAIL + 1))
}

skip() {
  echo "  SKIP  $1 - $2"
  SKIP=$((SKIP + 1))
}

run_gate() {
  local gate="$1"
  local message="$2"
  local log="$REPORT_DIR/$gate.log"
  shift 2
  if "$@" >"$log" 2>&1; then
    pass "$gate" "$message"
  else
    fail "$gate" "failed; command output follows"
    sed -n '1,80p' "$log" | sed 's/^/        /'
  fi
}

echo "Kettle release-ready"
echo "  home:    $HOME_REPO"
echo "  core:    $CORE_REPO"
echo "  vscode:  $VSCODE_REPO"
echo "  desktop: $DESKTOP_REPO"
echo

run_gate G-home-docs "relative Markdown links resolve" \
  python3 "$HOME_REPO/scripts/check-docs.py"

if [[ -f "$CORE_REPO/pyproject.toml" &&
      -f "$VSCODE_REPO/package.json" &&
      -f "$DESKTOP_REPO/package.json" ]]; then
  pass G-family-layout "core, VS Code, and desktop sibling trees exist"
else
  fail G-family-layout "expected sibling implementation repositories are missing"
fi

if [[ -f "$CORE_REPO/pyproject.toml" ]]; then
  if python3 -c "import pytest" >/dev/null 2>&1; then
    run_gate G-core-test "full core test suite is green" \
      bash -c 'cd "$1" && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider' \
      _ "$CORE_REPO"
  else
    fail G-core-test "pytest is not available to python3"
  fi
  run_gate G-cli-help "source CLI responds as Kettle" \
    bash -c 'cd "$1" && python3 kettle_main.py --help' _ "$CORE_REPO"
else
  fail G-core-test "kettle-core/pyproject.toml is missing"
  fail G-cli-help "kettle-core source tree is missing"
fi

if [[ -f "$VSCODE_REPO/package.json" ]]; then
  if [[ -d "$VSCODE_REPO/node_modules" ]]; then
    run_gate G-vscode-test "editor unit suite is green" \
      npm --prefix "$VSCODE_REPO" test
    run_gate G-ui-copy "generated editor copy matches core" \
      env KETTLE_SRC="$CORE_REPO" npm --prefix "$VSCODE_REPO" run check-ui-copy
    run_gate G-vscode-package "VSIX packages from local dependencies" \
      npm --prefix "$VSCODE_REPO" run package
  else
    fail G-vscode-test "node_modules is missing; run npm ci in kettle-vscode"
    fail G-ui-copy "node_modules is missing"
    fail G-vscode-package "node_modules is missing"
  fi
else
  fail G-vscode-test "kettle-vscode/package.json is missing"
  fail G-ui-copy "kettle-vscode source tree is missing"
  fail G-vscode-package "kettle-vscode source tree is missing"
fi

if [[ -f "$DESKTOP_REPO/package.json" ]]; then
  if [[ -d "$DESKTOP_REPO/node_modules" ]]; then
    run_gate G-desktop-test "desktop shell suite is green" \
      npm --prefix "$DESKTOP_REPO" test
  else
    fail G-desktop-test "node_modules is missing; run npm ci in kettle-desktop"
  fi
else
  fail G-desktop-test "kettle-desktop/package.json is missing"
fi

if [[ -f "$CORE_REPO/tools/check_family.py" ]]; then
  run_gate G-contracts "family manifests and clean worktrees agree" \
    python3 "$CORE_REPO/tools/check_family.py" \
      --core "$CORE_REPO" \
      --desktop "$DESKTOP_REPO" \
      --vscode "$VSCODE_REPO" \
      --require-clean
else
  fail G-contracts "kettle-core family checker is missing"
fi

DIRTY=0
for repo in "$HOME_REPO" "$CORE_REPO" "$VSCODE_REPO" "$DESKTOP_REPO"; do
  if [[ ! -d "$repo/.git" ]]; then
    echo "        not a Git worktree: $repo"
    DIRTY=1
  elif [[ -n "$(git -C "$repo" status --porcelain)" ]]; then
    echo "        dirty: $repo"
    DIRTY=1
  fi
done
if [[ "$DIRTY" -eq 0 ]]; then
  pass G-clean "publishable repositories have clean worktrees"
else
  fail G-clean "one or more publishable repositories are dirty"
fi

PING_JSON="$REPORT_DIR/ping.json"
if curl -sf --max-time 2 \
  "http://127.0.0.1:4242/api/ping" \
  -o "$PING_JSON" 2>/dev/null; then
  if python3 -c \
    'import json,sys; data=json.load(open(sys.argv[1])); assert data.get("app") == "kettle"' \
    "$PING_JSON" 2>/dev/null; then
    pass G-core-ping "compatible live core found on port 4242"
  else
    fail G-core-ping "port 4242 responded with an incompatible identity"
  fi
elif [[ "$REQUIRE_LIVE" -eq 1 ]]; then
  fail G-core-ping "no compatible live core on port 4242"
else
  skip G-core-ping "live core not required for source validation"
fi

APPROVE_OUT="$REPORT_DIR/approve-scope.txt"
if bash -c 'cd "$1" && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest kettle/tests/test_server.py::test_approve_writes_only_queue -rs -p no:cacheprovider' \
  bash "$CORE_REPO" >"$APPROVE_OUT" 2>&1; then
  if grep -E -q 'SKIPPED|XFAIL' "$APPROVE_OUT"; then
    fail G-approve-scope "test_approve_writes_only_queue was skipped or xfailed"
  elif grep -E -q '^1 passed' "$APPROVE_OUT"; then
    pass G-approve-scope "test_approve_writes_only_queue passed once"
  else
    fail G-approve-scope "test_approve_writes_only_queue did not pass exactly once"
  fi
else
  fail G-approve-scope "test_approve_writes_only_queue did not pass"
fi

echo
echo "Summary: $PASS pass, $FAIL fail, $SKIP skip"
echo "Manual preview gates remain in docs/reference/release-gates.md."

if [[ "$STRICT" -eq 1 && "$FAIL" -gt 0 ]]; then
  exit 1
fi
exit 0
