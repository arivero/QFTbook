#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export PYTHONPATH="$ROOT/qft_scripts:$ROOT${PYTHONPATH:+:$PYTHONPATH}"
if [[ -z "${QFT_HDF5_PYTHON:-}" ]]; then
  QFT_HDF5_PYTHON="$(command -v python3)"
  export QFT_HDF5_PYTHON
fi

echo "[qft-scripts] ising2d_metropolis --smoke"
python3 qft_scripts/ising2d_metropolis.py --smoke

echo "[qft-scripts] phi4_2d_metropolis --smoke"
python3 qft_scripts/phi4_2d_metropolis.py --smoke

echo "[qft-scripts] z2_gauge_3d_metropolis --smoke"
python3 qft_scripts/z2_gauge_3d_metropolis.py --smoke

echo "[qft-scripts] su2_gauge_4d_metropolis --smoke"
python3 qft_scripts/su2_gauge_4d_metropolis.py --smoke

echo "[qft-scripts] su2_gauge_4d_heatbath_overrelaxation --smoke"
python3 qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py --smoke

echo "[qft-scripts] su3_gauge_4d_metropolis_hdf5 --smoke"
python3 qft_scripts/su3_gauge_4d_metropolis_hdf5.py --smoke

echo "[qft-scripts] su3_wilson_flow_hdf5 --smoke"
python3 qft_scripts/su3_wilson_flow_hdf5.py --smoke

echo "[qft-scripts] su3_ape_smearing_hdf5 --smoke"
python3 qft_scripts/su3_ape_smearing_hdf5.py --smoke

echo "[qft-scripts] su3_topological_charge_diagnostics_hdf5 --smoke"
python3 qft_scripts/su3_topological_charge_diagnostics_hdf5.py --smoke

echo "[qft-scripts] hmc_rhmc_finite_demo --smoke"
python3 qft_scripts/hmc_rhmc_finite_demo.py --smoke

echo "[qft-scripts] autocorrelation_resampling --smoke"
python3 qft_scripts/autocorrelation_resampling.py --smoke

echo "[qft-scripts] static_potential_from_wilson_loops --smoke"
python3 qft_scripts/static_potential_from_wilson_loops.py --smoke

echo "[qft-scripts] glueball_gevp_from_correlators --smoke"
python3 qft_scripts/glueball_gevp_from_correlators.py --smoke

echo "[qft-scripts] cluster su3_sweep_grid"
python3 qft_scripts/cluster/su3_sweep_grid.py --betas 5.7,5.9 --seeds 11,13 --task-id 3 --format json >/dev/null

echo "[qft-scripts] cluster chain_ensemble_summary --smoke"
python3 qft_scripts/cluster/chain_ensemble_summary.py --smoke

echo "[qft-scripts] tcsa_ising_energy_benchmark --smoke"
python3 qft_scripts/tcsa_ising_energy_benchmark.py --smoke

echo "[qft-scripts] sine_gordon_zero_mode_truncation --smoke"
python3 qft_scripts/sine_gordon_zero_mode_truncation.py --smoke

echo "[qft-scripts] sine_gordon_tcsa_vertex --smoke"
python3 qft_scripts/sine_gordon_tcsa_vertex.py --smoke

echo "[qft-scripts] phi4_hamiltonian_truncation --smoke"
python3 qft_scripts/phi4_hamiltonian_truncation.py --smoke

echo "[qft-scripts] phi4_dlcq --smoke"
python3 qft_scripts/phi4_dlcq.py --smoke

echo "[qft-scripts] tffsa_ising_spin_connected --smoke"
python3 qft_scripts/tffsa_ising_spin_connected.py --smoke

echo "[qft-scripts] tffsa_ising_spectral_flow --smoke"
python3 qft_scripts/tffsa_ising_spectral_flow.py --smoke

echo "[qft-scripts] e8_ising_mass_ratios --smoke"
python3 qft_scripts/e8_ising_mass_ratios.py --smoke

echo "[qft-scripts] thooft_dlcq --smoke"
python3 qft_scripts/thooft_dlcq.py --smoke

echo "[qft-scripts] thooft_dlcq_extrapolation --smoke"
python3 qft_scripts/thooft_dlcq_extrapolation.py --smoke

echo "[qft-scripts] finite_regulator_extrapolation --smoke"
python3 qft_scripts/finite_regulator_extrapolation.py --smoke

echo "[qft-scripts] benchmark_manifest_consistency --smoke"
python3 qft_scripts/benchmark_manifest_consistency.py --smoke

echo "[qft-scripts] all smoke checks passed"
