#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

for check in calculation-checks/*_checks.py; do
  echo "[calculation-checks] python ${check}"
  python3 "$check"
done

find_wolframscript() {
  if [[ -n "${WOLFRAMSCRIPT:-}" && -x "${WOLFRAMSCRIPT:-}" ]]; then
    printf '%s\n' "$WOLFRAMSCRIPT"
    return 0
  fi

  if command -v wolframscript >/dev/null 2>&1; then
    command -v wolframscript
    return 0
  fi

  local mac_app="/Applications/Wolfram.app/Contents/MacOS/wolframscript"
  if [[ -x "$mac_app" ]]; then
    printf '%s\n' "$mac_app"
    return 0
  fi

  local mathematica_app
  for mathematica_app in /Applications/Mathematica.app/Contents/MacOS/wolframscript \
    /Applications/Wolfram\ Mathematica.app/Contents/MacOS/wolframscript; do
    if [[ -x "$mathematica_app" ]]; then
      printf '%s\n' "$mathematica_app"
      return 0
    fi
  done

  return 1
}

if [[ "${QFT_SKIP_WOLFRAM:-0}" == "1" ]]; then
  echo "[calculation-checks] QFT_SKIP_WOLFRAM=1; skipped Wolfram Language checks"
elif WOLFRAMSCRIPT="$(find_wolframscript)"; then
  echo "[calculation-checks] wolfram checks via $WOLFRAMSCRIPT"
  # Wolfram Language checks in this repository should be lightweight symbolic
  # convention checks.  Computationally heavy or numerical checks belong in
  # Python so that they are fast, batch-friendly, and easy for agents to run.
  WOLFRAM_TIMEOUT="${QFT_WOLFRAM_TIMEOUT:-90s}"
  for check in calculation-checks/*_checks.wl; do
    echo "[calculation-checks] wolfram ${check}"
    if command -v timeout >/dev/null 2>&1; then
      timeout -k 5s "$WOLFRAM_TIMEOUT" "$WOLFRAMSCRIPT" -file "$check"
    else
      "$WOLFRAMSCRIPT" -file "$check"
    fi
  done
else
  echo "[calculation-checks] wolframscript not found; skipped Wolfram Language checks" >&2
fi
