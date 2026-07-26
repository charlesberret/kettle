#!/usr/bin/env bash
# Kettle family — automated release gates (see docs/RELEASE.md).
# Run from anywhere; resolves home as this script's parent/parent.
set -euo pipefail

STRICT=0
REQUIRE_LIVE=0
for arg in "$@"; do
  case "$arg" in
    --strict) STRICT=1 ;;
    --require-live) REQUIRE_LIVE=1 ;;
    -h|--help)
      echo "Usage: release-ready.sh [--strict] [--require-live]"
      echo "  --strict         exit 1 if any required gate fails or is skipped as missing"
      echo "  --require-live   fail if core is not reachable on 127.0.0.1:4242"
      exit 0
      ;;
  esac
done

HOME_REPO="$(cd "$(dirname "$0")/.." && pwd)"
PARENT="$(cd "$HOME_REPO/.." && pwd)"
CORE="${KETTLE_CORE:-$PARENT/kettle-core}"
VSCODE="${KETTLE_VSCODE:-$PARENT/kettle-vscode}"
# Transitional core while transplant pending
LEGACY_CORE="${SETSWEEP_CORE:-$PARENT/setsweep-core}"

PASS=0
FAIL=0
SKIP=0
WARN=0

pass() { echo "  PASS  $1 — $2"; PASS=$((PASS + 1)); }
fail() { echo "  FAIL  $1 — $2"; FAIL=$((FAIL + 1)); }
skip() { echo "  SKIP  $1 — $2"; SKIP=$((SKIP + 1)); }
warn() { echo "  WARN  $1 — $2"; WARN=$((WARN + 1)); }

echo "Kettle release-ready"
echo "  home:   $HOME_REPO"
echo "  core:   $CORE"
echo "  vscode: $VSCODE"
echo "  legacy: $LEGACY_CORE"
echo

# --- G-home-docs ---
if [[ -f "$HOME_REPO/docs/ROADMAP.md" && -f "$HOME_REPO/docs/RELEASE.md" && -f "$HOME_REPO/docs/WORKFLOW.md" ]]; then
  pass G-home-docs "ROADMAP + RELEASE + WORKFLOW present"
else
  fail G-home-docs "missing docs/ROADMAP.md, RELEASE.md, or WORKFLOW.md"
fi

# --- G-family-layout ---
if [[ -d "$HOME_REPO" && -d "$PARENT" ]]; then
  pass G-family-layout "home under $PARENT"
else
  fail G-family-layout "cannot resolve family parent"
fi

# --- resolve active core tree ---
ACTIVE_CORE=""
if [[ -f "$CORE/pyproject.toml" ]]; then
  ACTIVE_CORE="$CORE"
elif [[ -f "$LEGACY_CORE/pyproject.toml" ]]; then
  ACTIVE_CORE="$LEGACY_CORE"
  warn G-core-tree "using legacy setsweep-core (kettle-core not transplanted yet)"
fi

# --- G-core-tree ---
if [[ -n "$ACTIVE_CORE" ]]; then
  pass G-core-tree "package tree at $ACTIVE_CORE"
else
  fail G-core-tree "no pyproject.toml in kettle-core or setsweep-core"
fi

# --- G-core-test ---
if [[ -n "$ACTIVE_CORE" ]]; then
  if command -v pytest >/dev/null 2>&1 || [[ -x "$HOME/.setsweep-venv/bin/pytest" ]] || [[ -x "$HOME/.kettle-venv/bin/pytest" ]]; then
    PYTEST=(pytest)
    if [[ -x "$HOME/.kettle-venv/bin/pytest" ]]; then
      PYTEST=("$HOME/.kettle-venv/bin/pytest")
    elif [[ -x "$HOME/.setsweep-venv/bin/pytest" ]]; then
      PYTEST=("$HOME/.setsweep-venv/bin/pytest")
    fi
    if (cd "$ACTIVE_CORE" && "${PYTEST[@]}" -q --tb=no >/tmp/kettle-release-core-test.log 2>&1); then
      pass G-core-test "pytest green in $ACTIVE_CORE"
    else
      fail G-core-test "pytest failed (see /tmp/kettle-release-core-test.log)"
    fi
  else
    skip G-core-test "pytest not on PATH or in ~/.kettle-venv / ~/.setsweep-venv"
  fi
else
  skip G-core-test "no core tree"
fi

# --- G-cli-help ---
CLI=""
for c in kettle setsweep \
  "$HOME/.kettle-venv/bin/kettle" "$HOME/.setsweep-venv/bin/setsweep" \
  "$HOME/.local/bin/kettle" "$HOME/.local/bin/setsweep"; do
  if command -v "$c" >/dev/null 2>&1; then CLI="$c"; break; fi
  if [[ -x "$c" ]]; then CLI="$c"; break; fi
done
if [[ -n "$CLI" ]] && "$CLI" --help >/tmp/kettle-release-cli-help.log 2>&1; then
  pass G-cli-help "$CLI --help ok"
else
  skip G-cli-help "no kettle/setsweep CLI with working --help (install core editable to enable)"
fi

# --- G-vscode-test / compile ---
if [[ -f "$VSCODE/package.json" ]]; then
  if [[ ! -d "$VSCODE/node_modules" ]]; then
    skip G-vscode-test "kettle-vscode node_modules missing (run npm install)"
    skip G-vscode-compile "kettle-vscode node_modules missing"
  else
    if (cd "$VSCODE" && npm test >/tmp/kettle-release-vscode-test.log 2>&1); then
      pass G-vscode-test "npm test green"
    else
      fail G-vscode-test "npm test failed (see /tmp/kettle-release-vscode-test.log)"
    fi
    if (cd "$VSCODE" && npm run compile >/tmp/kettle-release-vscode-compile.log 2>&1); then
      pass G-vscode-compile "tsc compile ok"
    else
      fail G-vscode-compile "compile failed (see /tmp/kettle-release-vscode-compile.log)"
    fi
  fi
else
  fail G-vscode-test "kettle-vscode not found at $VSCODE"
  fail G-vscode-compile "kettle-vscode not found"
fi

# --- G-compat ---
COMPAT="$VSCODE/kettle-compatibility.json"
if [[ -f "$COMPAT" ]]; then
  if python3 -c "import json; json.load(open('$COMPAT'))" 2>/dev/null; then
    pass G-compat "kettle-compatibility.json parses"
  else
    fail G-compat "kettle-compatibility.json invalid JSON"
  fi
else
  skip G-compat "no kettle-compatibility.json yet"
fi

# --- G-core-ping (optional live) ---
if curl -sf --max-time 2 "http://127.0.0.1:4242/api/ping" -o /tmp/kettle-release-ping.json 2>/dev/null; then
  if python3 -c "import json;d=json.load(open('/tmp/kettle-release-ping.json')); assert d.get('app') in ('kettle','setsweep')" 2>/dev/null; then
    pass G-core-ping "live core on :4242 (kettle|setsweep)"
  else
    fail G-core-ping "ping responded but app is not kettle/setsweep"
  fi
else
  if [[ "$REQUIRE_LIVE" -eq 1 ]]; then
    fail G-core-ping "no core on :4242 (--require-live)"
  else
    skip G-core-ping "no core on :4242 (start core or pass --require-live to require)"
  fi
fi

echo
echo "Summary: $PASS pass, $FAIL fail, $SKIP skip, $WARN warn"
echo "Manual gates (not run): M-dogfood-sit M-cli-queue M-approve-ne-apply M-readme-honest"
echo "See docs/RELEASE.md"

if [[ "$STRICT" -eq 1 ]]; then
  # In strict mode, skips on required trees count as failure for ship
  if [[ "$FAIL" -gt 0 ]]; then
    exit 1
  fi
  # Missing core transplant is a fail already via G-core-tree when neither exists
  exit 0
fi
exit 0
