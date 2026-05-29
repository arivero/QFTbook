# 2026-05-27 Issue #615 Chapter 4 Formalization Pass

## Scope

- Addressed Volume I Chapter 4 from the live #615 issue body after checking
  that it still had only two formal environments.
- Preserved the chapter's logic: ordinary Hamiltonian quantum mechanics first,
  finite time-slicing as the regulated object, Euclidean Wiener measure only
  under stated Schrödinger hypotheses, and no use of Borel measure as a general
  foundation for QFT path integrals.

## Manuscript Changes

- Added definitions for regular classical Lagrangian data, the Schrödinger
  representation, position/momentum rigging, Kato Schrödinger data, regulated
  phase-space path-integral data, and finite-slice sources.
- Added propositions with proofs for the finite phase-space time-sliced
  kernel, a limit-circle failure of formal Hamiltonian data, Gaussian
  elimination of quadratic momenta, and trace-induced periodic Euclidean
  boundary conditions; the Euclidean long-time projection step is now recorded
  as spectral-projection prose rather than theorem-family content.
- Classified the Trotter product formula and Faris--Lavine criterion as
  quoted theorems, because the chapter uses these functional-analytic results
  rather than proving them from first principles.
- Kept the existing Feynman--Kac theorem and proof as the main measure-level
  result in the chapter.

## Verification

- `python3` edited-file long-line scan for the chapter, dossier, and audit
  passed.
- `git diff --check -- <edited paths>` passed.
- `tools/build_monograph.sh` passed with a clean strict text audit and clean
  LaTeX log scan.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported `Pages: 2132`.
