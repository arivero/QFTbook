# Issue 494 DLCQ Extrapolation Pass

## Scope

This pass strengthens the Volume XI numerical-methods infrastructure around
Hamiltonian truncation and DLCQ benchmarks.  It addresses a remaining gap in
the large-N two-dimensional QCD example: the previous companion script built a
finite matrix and checked positivity, but did not expose a reproducible
large-`K` extrapolation diagnostic.

## Changes

- Added `qft_scripts/thooft_dlcq_extrapolation.py`, a reader-facing script
  that computes finite DLCQ spectra at several harmonic resolutions and fits
  fixed eigenvalue labels to a polynomial in `K^{-omega}`.
- Added residual, condition-number, and intercept-remainder-amplification
  diagnostics to the script output so that a finite fit is not mistaken for a
  continuum theorem.
- Extended
  `calculation-checks/hamiltonian_truncation_dlcq_checks.py` to verify the
  parser, exact-polynomial intercept recovery, constant-sequence recovery, and
  finite positivity of the diagnostic run.
- Added the script to `tools/run_qft_scripts_smoke.sh` and documented it in
  `qft_scripts/README.md`.
- Expanded
  `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`
  with a finite least-squares theorem proving the explicit remainder
  amplification bound for the fitted intercept.
- Updated the chapter dossier to record the new notation, claims, and
  companion scripts.

## Mathematical Status

The new theorem is finite-dimensional linear algebra.  It proves that if a
fixed finite-regulator sequence satisfies a declared polynomial-in-`K^{-omega}`
model plus a bounded remainder on the sampled resolutions, the fitted
intercept error is bounded by the row-`l1` norm of the least-squares left
inverse times the largest remainder.  The pass deliberately does not claim a
continuum large-N QCD spectrum.  Such a claim still requires endpoint,
zero-mode, and large-`K` remainder estimates.

## Verification

Verification for this pass should include:

- `python3 qft_scripts/thooft_dlcq_extrapolation.py --smoke`
- `python3 calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `python3 -m py_compile qft_scripts/thooft_dlcq_extrapolation.py calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `tools/run_qft_scripts_smoke.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
