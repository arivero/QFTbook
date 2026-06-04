#!/usr/bin/env bash

qft_python_required_modules() {
  printf '%s\n' numpy mpmath sympy h5py
}

qft_python_setup_command() {
  printf '%s\n' 'tools/bootstrap_verification_python.sh'
}

qft_python_probe() {
  local python_bin="$1"
  local modules_csv
  modules_csv="$(qft_python_required_modules | paste -sd, -)"
  "$python_bin" -c '
import importlib
import sys

missing = []
for name in sys.argv[1].split(","):
    try:
        importlib.import_module(name)
    except Exception as exc:
        missing.append(f"{name} ({exc.__class__.__name__}: {exc})")
if missing:
    print("missing required Python module(s): " + ", ".join(missing), file=sys.stderr)
    raise SystemExit(1)
' "$modules_csv" >/dev/null
}

qft_fail_python_setup() {
  local reason="$1"
  local modules_display
  local setup_command
  modules_display="$(qft_python_required_modules | paste -sd, - | sed 's/,/, /g')"
  setup_command="$(qft_python_setup_command)"
  {
    echo "[qft-python] FAILED: ${reason}"
    echo "[qft-python] Need one Python interpreter that imports: ${modules_display}."
    echo "[qft-python] From the repository root, create/update the public verification environment with:"
    echo "[qft-python]   ${setup_command}"
    echo "[qft-python] Or use an explicit nonstandard interpreter override:"
    echo "[qft-python]   QFT_PYTHON=/absolute/path/to/python tools/run_calculation_checks.sh --python-only"
    echo "[qft-python] Legacy QFT_HDF5_PYTHON is accepted as an alias only when QFT_PYTHON is unset; the selected interpreter is used for every Python check."
  } >&2
}

qft_resolve_python() {
  local root="${1:?repository root required}"
  local override="${QFT_PYTHON:-}"
  local legacy_override="${QFT_HDF5_PYTHON:-}"
  local candidate
  local candidates=()

  if [[ -z "$override" && -n "$legacy_override" ]]; then
    override="$legacy_override"
  fi

  if [[ -n "$override" ]]; then
    if [[ ! -x "$override" ]]; then
      qft_fail_python_setup "QFT_PYTHON override is not executable: $override"
      return 1
    fi
    if qft_python_probe "$override"; then
      printf '%s\n' "$override"
      return 0
    fi
    qft_fail_python_setup "QFT_PYTHON override lacks required verification dependencies: $override"
    return 1
  fi

  candidates+=("$root/.venv/bin/python")
  candidates+=("$root/.venv/bin/python3")
  candidates+=("$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3")
  if command -v python3 >/dev/null 2>&1; then
    candidates+=("$(command -v python3)")
  fi

  for candidate in "${candidates[@]}"; do
    if [[ -x "$candidate" ]] && qft_python_probe "$candidate" 2>/dev/null; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done

  qft_fail_python_setup "no usable public verification Python was found"
  return 1
}
