#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# shellcheck source=tools/qft_python_env.sh
source "$ROOT/tools/qft_python_env.sh"

resolved_python="$(qft_resolve_python "$ROOT")"
"$resolved_python" -c 'import h5py, mpmath, numpy, sympy'

QFT_PYTHON="$resolved_python" tools/run_calculation_checks.sh --python-only --only check_utils_checks >/dev/null
QFT_PYTHON="$resolved_python" tools/run_qft_scripts_smoke.sh --only benchmark_manifest_consistency >/dev/null

bad_dir="$(mktemp -d "${TMPDIR:-/tmp}/qft_bad_python.XXXXXX")"
trap 'rm -rf "$bad_dir"' EXIT
bad_python="$bad_dir/python"
{
  printf '#!/usr/bin/env bash\n'
  printf 'if [[ "${1:-}" == "-c" ]]; then\n'
  printf '  echo "fake verification python intentionally lacks required packages" >&2\n'
  printf '  exit 1\n'
  printf 'fi\n'
  printf 'exec "%s" "$@"\n' "$resolved_python"
} > "$bad_python"
chmod +x "$bad_python"

assert_runner_fails_before_suite() {
  local label="$1"
  shift
  local output status

  set +e
  output="$(QFT_PYTHON="$bad_python" "$@" 2>&1)"
  status=$?
  set -e

  if ((status == 0)); then
    echo "[python-runner-audit] FAILED: ${label} accepted a Python that lacks required packages." >&2
    return 1
  fi
  if [[ "$output" != *"tools/bootstrap_verification_python.sh"* || "$output" != *"QFT_PYTHON"* ]]; then
    echo "[python-runner-audit] FAILED: ${label} did not print the public setup/override guidance." >&2
    printf '%s\n' "$output" >&2
    return 1
  fi
}

assert_runner_fails_before_suite "calculation-check runner" \
  tools/run_calculation_checks.sh --python-only --only check_utils_checks
assert_runner_fails_before_suite "qft_scripts smoke runner" \
  tools/run_qft_scripts_smoke.sh --only benchmark_manifest_consistency

echo "[python-runner-audit] canonical runner Python selection is clean: ${resolved_python}"
