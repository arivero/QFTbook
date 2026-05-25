# Build Audit: Issue 580 OS Reconstruction Gap Pass

Date: 2026-05-25

## Scope

Partial but substantive pass on GitHub issue #580 in
`monograph/tex/volumes/volume_iv/chapter02_osterwalder_schrader_reconstruction.tex`.

## Mathematical Changes

- Added an explicit Klein--Landau failure-mode remark: OS-I hypotheses do not
  ensure that positive Euclidean time translation is bounded on the
  reflection-positive quotient.
- Expanded the self-adjointness verification for the Euclidean time
  semigroup directly from the OS-II quotient symmetry condition.
- Added a proposition proving closability of ordered Euclidean field
  insertions from an explicit adjoint-insertion matrix-element identity.
- Added a separate OS Lorentzian boundary-value package defining the
  holomorphic tube, tempered boundary-value, permutation/Jost-domain, and
  graded-sign inputs used by reconstruction.
- Proved that this boundary-value package gives tempered Wightman
  distributions, spacelike graded commutativity by edge-of-the-wedge, and
  recovery of the original off-diagonal Schwinger functions by uniqueness of
  analytic continuation.
- Revised the reconstruction theorem proof to refer to these displayed
  mechanisms rather than compressing them into informal phrases.
- Added the GNS-style uniqueness proof for two reconstructions from the same
  Schwinger hierarchy.

## Status

This improves gaps #2--#7 and makes the analytic continuation input explicit.
It does not yet close the deepest remaining part of #580: a self-contained
derivation that the chosen OS-II linear-growth estimate by itself proves the
Lorentzian boundary-value package.  The issue should remain open until that
Laplace--Bochner/tube-domain derivation is supplied or the theorem is
deliberately kept with the boundary-value package as a named hypothesis.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` built cleanly.
- `pdfinfo monograph/tex/main.pdf` reports 1262 pages.
