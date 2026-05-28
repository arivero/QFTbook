# Issue 494 TFFSA Spectral-Flow Pass

## Scope

This pass addresses the remaining need for richer nonintegrable
Hamiltonian-truncation benchmarks in Issue 494.  The previous connected Ising
TFFSA script assembled one finite matrix and checked Hermiticity.  This pass
adds a finite spectral-flow diagnostic, with a theorem-level explanation of
what the finite slopes certify.

## Changes

- Added `qft_scripts/tffsa_ising_spectral_flow.py`, which diagonalizes the
  finite connected Ising TFFSA block across a grid of magnetic couplings.
- The script computes the perturbing matrix `W`, Hellmann-Feynman slopes at a
  separated finite spectral point, centered finite-difference slopes, the
  trace-slope identity error, and the minimum finite spectral gap on the grid.
- Extended
  `calculation-checks/hamiltonian_truncation_dlcq_checks.py` to verify the
  exact affine matrix derivative, the Hellmann-Feynman finite-difference
  comparison, the trace identity, and smoke-run diagnostics.
- Added the script to `tools/run_qft_scripts_smoke.sh` and documented it in
  `qft_scripts/README.md`.
- Expanded Volume XI, Chapter 10 with a finite Hellmann-Feynman proposition
  for affine Hermitian matrix families, proved from the Riesz projection and
  the finite spectral gap.
- Updated the Chapter 10 dossier with the new notation, claim, and companion
  script.

## Mathematical Status

The added proposition is a finite-dimensional theorem.  It proves that a
simple finite eigenvalue branch of `H(h)=H_0+hW` has derivative
`<u,Wu>` under an explicit spectral-gap hypothesis, and that the sum of slopes
equals `tr W` when all eigenvalues are simple.  The theorem certifies the
finite TFFSA block only.  It does not assert the continuum magnetic-Ising
spectrum or the `E_8` mass ratios without cutoff, finite-volume,
diagonal-form-factor, and counterterm estimates.

## Verification

Verification for this pass should include:

- `python3 qft_scripts/tffsa_ising_spectral_flow.py --smoke`
- `python3 calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `python3 -m py_compile qft_scripts/tffsa_ising_spectral_flow.py calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `tools/run_qft_scripts_smoke.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
