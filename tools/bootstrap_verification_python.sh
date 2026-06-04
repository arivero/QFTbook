#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

candidate_pythons=()

append_python_candidate() {
  local candidate="$1"
  local resolved

  if [[ "$candidate" == */* ]]; then
    resolved="$candidate"
  elif command -v "$candidate" >/dev/null 2>&1; then
    resolved="$(command -v "$candidate")"
  else
    return 0
  fi

  if [[ ! -x "$resolved" ]]; then
    return 0
  fi

  local existing
  if ((${#candidate_pythons[@]})); then
    for existing in "${candidate_pythons[@]}"; do
      if [[ "$existing" == "$resolved" ]]; then
        return 0
      fi
    done
  fi
  candidate_pythons+=("$resolved")
}

python_can_bootstrap_venv() {
  local python_bin="$1"
  "$python_bin" - <<'PY' >/dev/null 2>&1
import ensurepip
import sys
import venv
import xml.parsers.expat

if sys.version_info < (3, 10):
    raise SystemExit(1)
PY
}

if [[ -n "${QFT_BOOTSTRAP_PYTHON:-}" ]]; then
  append_python_candidate "$QFT_BOOTSTRAP_PYTHON"
else
  append_python_candidate python3.13
  append_python_candidate python3.12
  append_python_candidate python3.11
  append_python_candidate python3.10
  append_python_candidate python3
  append_python_candidate /usr/bin/python3
fi

selected_python=""
if ((${#candidate_pythons[@]})); then
  for candidate in "${candidate_pythons[@]}"; do
    if python_can_bootstrap_venv "$candidate"; then
      selected_python="$candidate"
      break
    fi
  done
fi

if [[ -z "$selected_python" ]]; then
  echo "[qft-python-bootstrap] FAILED: no Python >= 3.10 with venv, ensurepip, and pyexpat was found." >&2
  echo "[qft-python-bootstrap] Install Python 3.12 or set QFT_BOOTSTRAP_PYTHON=/absolute/path/to/python." >&2
  exit 1
fi

echo "[qft-python-bootstrap] creating/updating .venv with ${selected_python}"
"$selected_python" -m venv "$ROOT/.venv"
"$ROOT/.venv/bin/python" -m pip install --upgrade pip
"$ROOT/.venv/bin/python" -m pip install -r "$ROOT/requirements-verification.txt"
"$ROOT/.venv/bin/python" -c 'import h5py, mpmath, numpy, PIL, sympy'
echo "[qft-python-bootstrap] verification Python ready: $ROOT/.venv/bin/python"
