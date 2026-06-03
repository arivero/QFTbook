#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export PYTHONPATH="$ROOT/calculation-checks:$ROOT/qft_scripts:$ROOT${PYTHONPATH:+:$PYTHONPATH}"
if [[ -z "${QFT_HDF5_PYTHON:-}" ]]; then
  QFT_HDF5_PYTHON="$(command -v python3)"
  export QFT_HDF5_PYTHON
fi
if [[ -z "${PYTHONWARNINGS:-}" ]]; then
  export PYTHONWARNINGS="error::RuntimeWarning"
fi

shopt -s nullglob

usage() {
  cat <<'USAGE'
Usage: tools/run_calculation_checks.sh [options]

Runs public calculation-check scripts explicitly.  This runner is intentionally
not part of the default monograph build; use it when a chapter edit touches
formulae or conventions covered by the relevant scripts.

Options:
  --list              List selected checks without running them.
  --only PATTERN      Select checks whose path or basename contains PATTERN.
                      May be supplied more than once.
  --python-only       Run/list only Python checks.
  --wolfram-only      Run/list only Wolfram Language checks.
  --skip-wolfram      Alias for QFT_SKIP_WOLFRAM=1 for this invocation.
  -h, --help          Show this help.
USAGE
}

include_python=1
include_wolfram=1
list_only=0
only_patterns=()

while (($#)); do
  case "$1" in
    --list)
      list_only=1
      ;;
    --only)
      shift
      if (($# == 0)); then
        echo "[calculation-checks] FAILED: --only requires a pattern." >&2
        exit 2
      fi
      only_patterns+=("$1")
      ;;
    --python-only)
      include_python=1
      include_wolfram=0
      ;;
    --wolfram-only)
      include_python=0
      include_wolfram=1
      ;;
    --skip-wolfram)
      include_wolfram=0
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "[calculation-checks] FAILED: unknown option $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

matches_only_patterns() {
  local check="$1"
  local base="${check##*/}"
  local pattern

  if ((${#only_patterns[@]} == 0)); then
    return 0
  fi

  for pattern in "${only_patterns[@]}"; do
    if [[ "$check" == *"$pattern"* || "$base" == *"$pattern"* ||
      "$check" == $pattern || "$base" == $pattern ]]; then
      return 0
    fi
  done

  return 1
}

python_checks=()
wolfram_checks=()

if ((include_python)); then
  for check in calculation-checks/*.py; do
    if matches_only_patterns "$check"; then
      python_checks+=("$check")
    fi
  done
fi

if ((include_wolfram)); then
  for check in calculation-checks/*.wl; do
    if matches_only_patterns "$check"; then
      wolfram_checks+=("$check")
    fi
  done
fi

if ((list_only)); then
  echo "[calculation-checks] selected Python checks: ${#python_checks[@]}"
  if ((${#python_checks[@]})); then
    printf '%s\n' "${python_checks[@]}"
  fi
  echo "[calculation-checks] selected Wolfram Language checks: ${#wolfram_checks[@]}"
  if ((${#wolfram_checks[@]})); then
    printf '%s\n' "${wolfram_checks[@]}"
  fi
  exit 0
fi

if ((${#python_checks[@]} + ${#wolfram_checks[@]} == 0)); then
  echo "[calculation-checks] FAILED: no checks selected." >&2
  exit 1
fi

if ((${#python_checks[@]})); then
  for check in "${python_checks[@]}"; do
    echo "[calculation-checks] python ${check}"
    python3 "$check"
  done
fi

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

if ((include_wolfram == 0)); then
  echo "[calculation-checks] Wolfram Language checks not selected"
elif [[ "${QFT_SKIP_WOLFRAM:-0}" == "1" ]]; then
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
  if ((${#wolfram_checks[@]})); then
    for check in "${wolfram_checks[@]}"; do
      echo "[calculation-checks] wolfram ${check}"
      run_wolfram_file "$check"
    done
  fi
elif WOLFRAMSCRIPT="$(find_wolframscript)"; then
  WOLFRAM_LABEL="$WOLFRAMSCRIPT -file"
  WOLFRAM_CMD=("$WOLFRAMSCRIPT" -file)
  echo "[calculation-checks] wolfram checks via $WOLFRAM_LABEL"
  # Wolfram Language checks in this repository should be lightweight symbolic
  # convention checks.  Computationally heavy or numerical checks belong in
  # Python so that they are fast, batch-friendly, and easy for agents to run.
  WOLFRAM_TIMEOUT="${QFT_WOLFRAM_TIMEOUT:-90s}"
  probe_wolfram_backend
  if ((${#wolfram_checks[@]})); then
    for check in "${wolfram_checks[@]}"; do
      echo "[calculation-checks] wolfram ${check}"
      run_wolfram_file "$check"
    done
  fi
else
  echo "[calculation-checks] FAILED: ${#wolfram_checks[@]} Wolfram Language check(s) exist, but no Wolfram backend was found." >&2
  echo "[calculation-checks] Install or expose WolframKernel/wolframscript, or set QFT_SKIP_WOLFRAM=1 only for an explicitly Python-only pass." >&2
  exit 1
fi
