# 2026-05-25 Issue #494 Numerical Scripts Pass

GitHub issue: #494, numerical methods with lattice Monte Carlo, Hamiltonian
truncation/TCSA, DLCQ, and actual Python scripts.

## Manuscript Changes

- Expanded Volume XI, Chapter 6 with a finite periodic Ising Metropolis
  theorem:
  - finite spin configuration space and Boltzmann probability;
  - single-spin proposal and local energy difference;
  - detailed-balance proof;
  - irreducibility and aperiodicity conditions, including the degenerate
    \(J=h=0\) lazy-chain caveat.
- Expanded Volume XI, Chapter 10 with two finite Hamiltonian-regulator
  benchmarks:
  - Ising thermal-deformation Majorana Bogoliubov block and exact finite-mode
    eigenvalue proof;
  - large-\(N\) two-dimensional QCD DLCQ-style principal-value matrix and
    positivity proof for the finite quadratic form.

## Code Infrastructure

- Added `planning/14_code_policy.md` to distinguish:
  - `calculation-checks/` as fast deterministic algebra/convention checks;
  - `qft_scripts/` as reader-facing finite-regulator numerical examples.
- Added `qft_scripts/README.md`.
- Added `qft_scripts/ising2d_metropolis.py`.
- Added `qft_scripts/tcsa_ising_energy_benchmark.py`.
- Added `qft_scripts/thooft_dlcq.py`.
- Added `tools/run_qft_scripts_smoke.sh`.

## Verification

- `tools/run_qft_scripts_smoke.sh` passed.

## Remaining Scope

This pass should not close #494 by itself.  The monograph now has public
finite-regulator scripts and theorem-level finite checks, but full closure
still requires deeper production-grade examples, continuum extrapolation
studies, and richer TCSA/DLCQ applications such as nonintegrable TCSA spectra
and more systematic large-\(K\) DLCQ analysis.
