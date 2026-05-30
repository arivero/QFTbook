# Distributional Edge-Of-The-Wedge Status Pass

Date: 2026-05-30

Related issue: #695

## Scope

This pass answered the local audit question about the distributional
edge-of-the-wedge theorem.  The theorem is present in Volume I, Chapter 11 and
is used in the OS reconstruction and analyticity chapters, but it is a quoted
complex-analysis/distribution theorem rather than a monograph-internal QFT
theorem.

## Changes

- Added a paragraph immediately after
  `thm:distributional-edge-of-the-wedge` explaining its role as analytic
  infrastructure from several complex variables and distribution theory.
- Identified the proof mechanism at the level needed for honest status:
  polynomial tube bounds give distributional boundary values, equality on the
  real edge removes the analytic obstruction, and local holomorphic
  representatives glue in the envelope of holomorphy.
- Separated this pure analytic theorem from the QFT-specific work: verifying
  tube holomorphy/growth from spectral support and equality of boundary
  distributions from locality or Euclidean permutation symmetry.
- Updated the Volume II analyticity chapter so its local
  edge-of-the-wedge form explicitly points back to the distributional theorem.
- Updated the Volume I, Chapter 11 dossier.

## Status

This pass does not close #695.  It clarifies the theorem-boundary status of the
distributional edge-of-the-wedge input.  A complete proof of the several
complex variables theorem may be added later as analytic background, but the
core QFT proof obligation is now localized to the hypotheses used at each
application.
