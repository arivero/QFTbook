# QFT Companion Scripts

This directory contains small reader-facing finite-regulator demonstrations
for the monograph.  They are distinct from `calculation-checks/`: calculation
checks certify signs and formulae used directly in the text, while companion
scripts illustrate numerical regulator frameworks.

Quick smoke run:

```bash
tools/run_qft_scripts_smoke.sh
```

Individual examples:

```bash
python3 qft_scripts/ising2d_metropolis.py --smoke
python3 qft_scripts/tcsa_ising_energy_benchmark.py --smoke
python3 qft_scripts/thooft_dlcq.py --smoke
```

The scripts use Python 3 and NumPy.  Their output is JSON so that future
notebooks or CI checks can consume the results without scraping prose.

## Scripts

- `ising2d_metropolis.py`: finite two-dimensional Ising Metropolis sampler
  with periodic boundary conditions.  It demonstrates detailed balance and
  autocorrelation diagnostics at finite volume.
- `tcsa_ising_energy_benchmark.py`: exactly solvable Hamiltonian truncation
  benchmark for the Ising thermal deformation, written as finite Majorana
  Bogoliubov blocks.
- `thooft_dlcq.py`: finite harmonic-resolution matrix for the large-\(N\)
  two-dimensional QCD meson equation.  It is a DLCQ-style principal-value
  regulator, not a proof of the continuum spectrum.
