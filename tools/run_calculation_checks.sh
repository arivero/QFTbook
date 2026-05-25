#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

shopt -s nullglob

python_checks=(calculation-checks/*_checks.py)
wolfram_checks=(calculation-checks/*_checks.wl)

for check in "${python_checks[@]}"; do
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

find_wolframkernel() {
  if [[ -n "${WOLFRAMKERNEL:-}" && -x "${WOLFRAMKERNEL:-}" ]]; then
    printf '%s\n' "$WOLFRAMKERNEL"
    return 0
  fi

  if command -v WolframKernel >/dev/null 2>&1; then
    command -v WolframKernel
    return 0
  fi

  local mac_app="/Applications/Wolfram.app/Contents/MacOS/WolframKernel"
  if [[ -x "$mac_app" ]]; then
    printf '%s\n' "$mac_app"
    return 0
  fi

  local mathematica_app
  for mathematica_app in /Applications/Mathematica.app/Contents/MacOS/WolframKernel \
    /Applications/Wolfram\ Mathematica.app/Contents/MacOS/WolframKernel; do
    if [[ -x "$mathematica_app" ]]; then
      printf '%s\n' "$mathematica_app"
      return 0
    fi
  done

  return 1
}

run_wolfram_check() {
  if command -v timeout >/dev/null 2>&1; then
    timeout -k 5s "$WOLFRAM_TIMEOUT" "$@"
  else
    "$@"
  fi
}

reject_wolfram_parse_hazards() {
  local check="$1"
  local hazards
  hazards="$(grep -nE '^[[:space:]]+[-+*/]' "$check" || true)"
  if [[ -n "$hazards" ]]; then
    echo "[calculation-checks] FAILED: ${check} contains Wolfram Language line continuations that begin with an arithmetic operator." >&2
    echo "$hazards" >&2
    echo "[calculation-checks] Put the binary operator at the end of the preceding line, or wrap the full right-hand side in parentheses." >&2
    return 1
  fi
}

probe_wolfram_backend() {
  local probe_file output status
  probe_file="$(mktemp "${TMPDIR:-/tmp}/qft_wolfram_probe.XXXXXX.wl")"
  printf 'Print["QFT_WOLFRAM_BACKEND_PROBE_OK"];\n' > "$probe_file"

  set +e
  output="$(run_wolfram_check "${WOLFRAM_CMD[@]}" "$probe_file" 2>&1)"
  status=$?
  set -e
  rm -f "$probe_file"

  if (( status != 0 )); then
    echo "[calculation-checks] FAILED: Wolfram backend probe failed via ${WOLFRAM_LABEL}" >&2
    printf '%s\n' "$output" >&2
    return 1
  fi
  if [[ "$output" != *"QFT_WOLFRAM_BACKEND_PROBE_OK"* ]]; then
    echo "[calculation-checks] FAILED: Wolfram backend probe via ${WOLFRAM_LABEL} did not print the probe marker." >&2
    printf '%s\n' "$output" >&2
    return 1
  fi
}

run_wolfram_file() {
  local check="$1"
  local output status

  reject_wolfram_parse_hazards "$check"

  set +e
  output="$(run_wolfram_check "${WOLFRAM_CMD[@]}" "$check" 2>&1)"
  status=$?
  set -e

  printf '%s\n' "$output"
  if (( status != 0 )); then
    echo "[calculation-checks] FAILED: ${check} exited with status ${status} via ${WOLFRAM_LABEL}" >&2
    return 1
  fi
  if [[ "$output" != *"All Wolfram Language"* || "$output" != *"passed."* ]]; then
    echo "[calculation-checks] FAILED: ${check} did not print the required Wolfram success marker." >&2
    echo "[calculation-checks] Each committed .wl check must print a line of the form: All Wolfram Language ... passed." >&2
    return 1
  fi
}

if [[ "${QFT_SKIP_WOLFRAM:-0}" == "1" ]]; then
  echo "[calculation-checks] QFT_SKIP_WOLFRAM=1; skipped Wolfram Language checks"
elif ((${#wolfram_checks[@]} == 0)); then
  echo "[calculation-checks] no Wolfram Language checks found"
elif WOLFRAMKERNEL="$(find_wolframkernel)"; then
  WOLFRAM_LABEL="$WOLFRAMKERNEL -script"
  WOLFRAM_CMD=("$WOLFRAMKERNEL" -script)
  echo "[calculation-checks] wolfram checks via $WOLFRAM_LABEL"
  # Prefer WolframKernel -script when it is available.  On some macOS
  # installations wolframscript -file can stall before evaluating even
  # elementary local code, while the kernel script entrypoint runs directly.
  WOLFRAM_TIMEOUT="${QFT_WOLFRAM_TIMEOUT:-90s}"
  probe_wolfram_backend
  for check in "${wolfram_checks[@]}"; do
    echo "[calculation-checks] wolfram ${check}"
    run_wolfram_file "$check"
  done
elif WOLFRAMSCRIPT="$(find_wolframscript)"; then
  WOLFRAM_LABEL="$WOLFRAMSCRIPT -file"
  WOLFRAM_CMD=("$WOLFRAMSCRIPT" -file)
  echo "[calculation-checks] wolfram checks via $WOLFRAM_LABEL"
  # Wolfram Language checks in this repository should be lightweight symbolic
  # convention checks.  Computationally heavy or numerical checks belong in
  # Python so that they are fast, batch-friendly, and easy for agents to run.
  WOLFRAM_TIMEOUT="${QFT_WOLFRAM_TIMEOUT:-90s}"
  probe_wolfram_backend
  for check in "${wolfram_checks[@]}"; do
    echo "[calculation-checks] wolfram ${check}"
    run_wolfram_file "$check"
  done
else
  echo "[calculation-checks] FAILED: ${#wolfram_checks[@]} Wolfram Language check(s) exist, but no Wolfram backend was found." >&2
  echo "[calculation-checks] Install or expose WolframKernel/wolframscript, or set QFT_SKIP_WOLFRAM=1 only for an explicitly Python-only pass." >&2
  exit 1
fi
