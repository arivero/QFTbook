#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "[qft-scripts] ising2d_metropolis --smoke"
python3 qft_scripts/ising2d_metropolis.py --smoke

echo "[qft-scripts] z2_gauge_3d_metropolis --smoke"
python3 qft_scripts/z2_gauge_3d_metropolis.py --smoke

echo "[qft-scripts] tcsa_ising_energy_benchmark --smoke"
python3 qft_scripts/tcsa_ising_energy_benchmark.py --smoke

echo "[qft-scripts] thooft_dlcq --smoke"
python3 qft_scripts/thooft_dlcq.py --smoke

echo "[qft-scripts] all smoke checks passed"
