#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "[qft-scripts] ising2d_metropolis --smoke"
python3 qft_scripts/ising2d_metropolis.py --smoke

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

echo "[qft-scripts] autocorrelation_resampling --smoke"
python3 qft_scripts/autocorrelation_resampling.py --smoke

echo "[qft-scripts] static_potential_from_wilson_loops --smoke"
python3 qft_scripts/static_potential_from_wilson_loops.py --smoke

echo "[qft-scripts] tcsa_ising_energy_benchmark --smoke"
python3 qft_scripts/tcsa_ising_energy_benchmark.py --smoke

echo "[qft-scripts] tffsa_ising_spin_connected --smoke"
python3 qft_scripts/tffsa_ising_spin_connected.py --smoke

echo "[qft-scripts] thooft_dlcq --smoke"
python3 qft_scripts/thooft_dlcq.py --smoke

echo "[qft-scripts] thooft_dlcq_extrapolation --smoke"
python3 qft_scripts/thooft_dlcq_extrapolation.py --smoke

echo "[qft-scripts] all smoke checks passed"
