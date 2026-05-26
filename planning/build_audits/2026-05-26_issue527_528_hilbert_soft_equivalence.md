# Issue #527/#528 Hilbert Soft-Equivalence Pass

Date: 2026-05-26.

Scope: Volume IV, Chapter 5, charged-sector Haag--Ruelle and dressed LSZ.

## Mathematical Additions

- Added a definition of Hilbert-equivalent soft dressings at fixed ultraviolet
  cutoff: two infrared-regulated soft profiles are equivalent precisely when
  their difference converges in the photon one-particle Hilbert space.
- Proved that Hilbert-equivalent soft changes are inner Weyl coordinate
  changes.  The proof checks the Weyl generator identity, extends it to finite
  Weyl polynomials, proves strong convergence of the implementing Weyl
  unitaries on coherent vectors, and derives the nonzero limiting coherent
  overlap.
- Connected the criterion to the existing velocity-separation theorem:
  velocity-changing Coulomb tails fail Hilbert equivalence because their
  one-particle norm difference diverges logarithmically.

## Verification

- Updated `calculation-checks/charged_flux_dressing_checks.py` to test the
  characteristic-functional transformation under a finite Hilbert soft change,
  the coherent-vector overlap formula, and finite-dimensional strong
  continuity of Weyl implementers on coherent vectors.
- Ran `python3 calculation-checks/charged_flux_dressing_checks.py`; it passed.
- Ran `tools/build_monograph.sh`; XeLaTeX produced
  `monograph/tex/main.pdf` with 1533 pages.  The wrapper returned failure only
  because of an unrelated overfull box in the already-present uncommitted
  2D-BCFT chapter at lines 94--103.  The final `main.log` had no undefined
  references or TeX errors from the charged-sector edits.

## Remaining Boundary

This pass does not claim the full charged-sector Haag--Ruelle theorem.  The
large-time estimate for noncompact charged dressings and the construction of
the asymptotic dressed charged Hilbert space remain the open core of
Issues #527 and #528.
