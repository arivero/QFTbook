# 2026-05-27 Kontsevich--Segal Positive-Energy Depth Pass

## Scope

The K-S chapter already contained the allowability criterion, functorial
datum, reflection positivity, OS comparison, OPE from sewing, and construction
ledger.  This pass deepens the positive-energy mechanism and the analytic
target data needed before Hilbert completion.

## Manuscript Changes

- Added a one-dimensional holomorphic-semigroup model of positive energy,
  with a proposition proving that a reflected contraction semigroup has a
  unique self-adjoint generator \(H\ge0\) and unitary imaginary-boundary
  values.
- Made collared admissible complex-metric bordisms a labeled definition and
  added the locally convex target category needed for sewing before Hilbert
  completion.
- Added a theorem proving that K-S reflection positivity and cylinder sewing
  produce a positive-energy Hamiltonian on the reflected boundary Hilbert
  space, once null-quotient invariance, strong continuity, and cylinder
  normalization are part of the construction.
- Expanded the Gaussian example from a generic status comment into a finite
  harmonic-oscillator Mehler-kernel model, separating theorem-level finite
  mode composition from the still-open continuum free-scalar K-S functor.

## Companion Checks

- Added `calculation-checks/ks_semigroup_checks.py`.
- The script checks Mehler-kernel coefficient composition for finite
  oscillator modes and checks the contraction-to-unitary boundary-value
  behavior of \(e^{-zH}\) for a finite positive spectrum.
- Updated the calculation-check README and the K-S chapter dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/ks_allowability_checks.py`
- `python3 calculation-checks/ks_semigroup_checks.py`
- `python3 -m py_compile calculation-checks/ks_semigroup_checks.py`
- edited-file long-line scan
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2127 pages.
- `rg -n "undefined|Rerun|Warning" monograph/tex/main.log | tail -n 40`
  showed no live warning or rerun request, only the package-identification
  line for `rerunfilecheck`.
