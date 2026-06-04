#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# shellcheck source=tools/qft_python_env.sh
source "$ROOT/tools/qft_python_env.sh"

export PYTHONPATH="$ROOT/qft_scripts:$ROOT${PYTHONPATH:+:$PYTHONPATH}"

usage() {
  cat <<'USAGE'
Usage: tools/run_qft_scripts_smoke.sh [options]

Runs public qft_scripts smoke checks with the same verification Python used by
tools/run_calculation_checks.sh.

Options:
  --list              List selected smoke checks without running them.
  --only PATTERN      Select checks whose label, path, or basename contains PATTERN.
                      May be supplied more than once.
  -h, --help          Show this help.
USAGE
}

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
        echo "[qft-scripts] FAILED: --only requires a pattern." >&2
        exit 2
      fi
      only_patterns+=("$1")
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "[qft-scripts] FAILED: unknown option $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

matches_only_patterns() {
  local label="$1"
  local path="$2"
  local base="${path##*/}"
  local pattern

  if ((${#only_patterns[@]} == 0)); then
    return 0
  fi

  for pattern in "${only_patterns[@]}"; do
    if [[ "$label" == *"$pattern"* || "$path" == *"$pattern"* || "$base" == *"$pattern"* ]]; then
      return 0
    fi
  done

  return 1
}

QFT_PYTHON_RESOLVED="$(qft_resolve_python "$ROOT")"
export QFT_PYTHON="$QFT_PYTHON_RESOLVED"
export QFT_HDF5_PYTHON="$QFT_PYTHON_RESOLVED"

selected_count=0

run_python_smoke() {
  local quiet_output=0
  if [[ "${1:-}" == "--quiet-output" ]]; then
    quiet_output=1
    shift
  fi

  local label="$1"
  local path="$2"
  shift 2

  if ! matches_only_patterns "$label" "$path"; then
    return 0
  fi

  selected_count=$((selected_count + 1))
  if ((list_only)); then
    echo "[qft-scripts] ${label}"
    return 0
  fi

  echo "[qft-scripts] ${label}"
  if ((quiet_output)); then
    "$QFT_PYTHON" "$path" "$@" >/dev/null
  else
    "$QFT_PYTHON" "$path" "$@"
  fi
}

run_python_smoke "ising2d_metropolis --smoke" qft_scripts/ising2d_metropolis.py --smoke
run_python_smoke "phi4_2d_metropolis --smoke" qft_scripts/phi4_2d_metropolis.py --smoke
run_python_smoke "z2_gauge_3d_metropolis --smoke" qft_scripts/z2_gauge_3d_metropolis.py --smoke
run_python_smoke "su2_gauge_4d_metropolis --smoke" qft_scripts/su2_gauge_4d_metropolis.py --smoke
run_python_smoke "su2_gauge_4d_heatbath_overrelaxation --smoke" qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py --smoke
run_python_smoke "su3_gauge_4d_metropolis_hdf5 --smoke" qft_scripts/su3_gauge_4d_metropolis_hdf5.py --smoke
run_python_smoke "su3_wilson_flow_hdf5 --smoke" qft_scripts/su3_wilson_flow_hdf5.py --smoke
run_python_smoke "su3_ape_smearing_hdf5 --smoke" qft_scripts/su3_ape_smearing_hdf5.py --smoke
run_python_smoke "su3_topological_charge_diagnostics_hdf5 --smoke" qft_scripts/su3_topological_charge_diagnostics_hdf5.py --smoke
run_python_smoke "hmc_rhmc_finite_demo --smoke" qft_scripts/hmc_rhmc_finite_demo.py --smoke
run_python_smoke "autocorrelation_resampling --smoke" qft_scripts/autocorrelation_resampling.py --smoke
run_python_smoke "static_potential_from_wilson_loops --smoke" qft_scripts/static_potential_from_wilson_loops.py --smoke
run_python_smoke "glueball_gevp_from_correlators --smoke" qft_scripts/glueball_gevp_from_correlators.py --smoke
run_python_smoke --quiet-output "cluster su3_sweep_grid" qft_scripts/cluster/su3_sweep_grid.py --betas 5.7,5.9 --seeds 11,13 --task-id 3 --format json
run_python_smoke "cluster chain_ensemble_summary --smoke" qft_scripts/cluster/chain_ensemble_summary.py --smoke
run_python_smoke "tcsa_ising_energy_benchmark --smoke" qft_scripts/tcsa_ising_energy_benchmark.py --smoke
run_python_smoke "sine_gordon_zero_mode_truncation --smoke" qft_scripts/sine_gordon_zero_mode_truncation.py --smoke
run_python_smoke "sine_gordon_tcsa_vertex --smoke" qft_scripts/sine_gordon_tcsa_vertex.py --smoke
run_python_smoke "phi4_hamiltonian_truncation --smoke" qft_scripts/phi4_hamiltonian_truncation.py --smoke
run_python_smoke "phi4_dlcq --smoke" qft_scripts/phi4_dlcq.py --smoke
run_python_smoke "tffsa_ising_spin_connected --smoke" qft_scripts/tffsa_ising_spin_connected.py --smoke
run_python_smoke "tffsa_ising_spectral_flow --smoke" qft_scripts/tffsa_ising_spectral_flow.py --smoke
run_python_smoke "e8_ising_mass_ratios --smoke" qft_scripts/e8_ising_mass_ratios.py --smoke
run_python_smoke "thooft_dlcq --smoke" qft_scripts/thooft_dlcq.py --smoke
run_python_smoke "thooft_dlcq_extrapolation --smoke" qft_scripts/thooft_dlcq_extrapolation.py --smoke
run_python_smoke "finite_regulator_extrapolation --smoke" qft_scripts/finite_regulator_extrapolation.py --smoke
run_python_smoke "benchmark_manifest_consistency --smoke" qft_scripts/benchmark_manifest_consistency.py --smoke

if ((selected_count == 0)); then
  echo "[qft-scripts] FAILED: no smoke checks selected." >&2
  exit 1
fi

if ((list_only)); then
  echo "[qft-scripts] selected smoke checks: ${selected_count}"
else
  echo "[qft-scripts] all smoke checks passed"
fi
