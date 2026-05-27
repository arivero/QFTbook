# 2026-05-27 Volume I Local-Field Covariance Formalization

## Scope

Issue #615 calls for the early formalization spine to be upgraded from
descriptive prose to definition/proposition/proof level statements.  This pass
targets Volume I, Chapter 3, where local field multiplets, Poincare covariance,
microcausality, and Wightman distributions first interact.

## Manuscript Changes

- Added a named definition of a common invariant field domain, making explicit
  the domain needed for finite products of unbounded smeared fields.
- Added a distributional-matrix-element proposition to fix the logic from
  continuous smeared products to point-field notation.
- Promoted Poincare covariance of field multiplets to a named definition.
- Proved that field covariance plus vacuum invariance implies covariance of
  all Wightman distributions, including the precise pullback convention
  \(f_g(y)=f(g^{-1}y)\).
- Promoted smeared microcausality to a named definition and proved the
  adjacent spacelike exchange relation with the Koszul sign.

## Companion Checks

- Added `calculation-checks/local_field_covariance_checks.py`.
- The check verifies the mostly-plus Lorentz interval convention, the
  transformed-test-function composition order \((f_g)_h=f_{hg}\), the graded
  exchange signs, and the tensor-product ordering of component covariance
  factors.
- Updated `calculation-checks/README.md` and the Volume I Chapter 3 dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/local_field_covariance_checks.py`
- `python3 -m py_compile calculation-checks/local_field_covariance_checks.py`
- `git diff --check`
- weak-language audit on the edited chapter, dossier, audit, and companion
  check
- `tools/build_monograph.sh`

The final build produced `monograph/tex/main.pdf` with 2103 pages.
