# 2026-05-27 Volume I Spinor Conventions Formalization

## Scope

Issue #615 flags the spinor-convention section as substantial but formally
unstructured.  This pass converts the convention layer into labeled
definitions and propositions, because later spinorial LSZ, QED, anomaly,
supersymmetry, and two-dimensional CFT calculations all depend on the same
sign data.

## Manuscript Changes

- Added a labeled definition of the four-dimensional mostly-plus
  Weinberg-compatible gamma basis, Dirac adjoint, Dirac density, and current.
- Proved the slash-square, beta-pairing, Dirac-adjoint, and current
  Hermiticity identities.
- Added a labeled spin-representation and chirality definition and proved
  spin covariance, beta-pairing invariance, chirality identities, and the
  \(4\ii\epsilon^{\mu\nu\rho\sigma}\) trace normalization.
- Proved the two-component rho-block sign relation and contraction identity.
- Added a labeled Majorana-conjugation proof, including the infinitesimal
  conjugation sign needed for Lorentz covariance.
- Proved the same-metric Wess-Bagger phase translation.
- Distinguished the two-dimensional Dirac-anomaly basis from the two-dimensional
  Majorana basis used to connect to two-dimensional CFT components, and proved
  their explicit similarity relation.
- Proved the three-dimensional Clifford/symmetric-block identities and the
  even-dimensional Euclidean Clifford recursion.

## Companion Checks

- Added `calculation-checks/spinor_convention_checks.py`.
- The script checks the finite Clifford algebra, beta-pairing, spin-generator
  commutators, \(\gamma_5\) trace, two-component rho signs, Majorana
  conjugation, Wess-Bagger phase translation, \(D=2\) and \(D=3\) Lorentzian
  conventions, the chiral-component light-cone gamma components, and Euclidean
  Clifford recursion.
- Updated the calculation-check README and added the Chapter 16a dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/spinor_convention_checks.py`
- `python3 -m py_compile calculation-checks/spinor_convention_checks.py`
- `python3 calculation-checks/gamma_trace_checks.py`
- edited-file long-line scan
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2125 pages.
- `rg -n "undefined|Rerun|Warning" monograph/tex/main.log | tail -n 40`
  showed no live warning or rerun request, only the package-identification
  line for `rerunfilecheck`.
