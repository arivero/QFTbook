# 2026-05-25 Issue 568: TQFT Boundaries, Defects, and Categories

## Scope

Issue #568 flagged Volume VIII Chapter 9 as too abstract: the chapter had no
labeled environments and did not work through concrete boundary or defect
examples.

## Edits

- Rewrote the chapter around explicit finite-dimensional models rather than
  general prose.
- Added a definition and proof that one-dimensional interval gluing produces
  categorical composition.
- Added finite `BF_2` boundary states as primitive central idempotents in
  `Z(C[G])`, with proof from Schur orthogonality and the regular
  representation.
- Added finite-gauge codimension-one defects as bisets, junction spaces as
  equivariant maps, and a proof that balanced-product defect fusion is
  associative.
- Added modular tensor category data and tied the `SU(2)_k` line data to the
  Chern-Simons modular-data chapter.
- Added abelian Chern-Simons Lagrangian subgroups, the associated commutative
  separable boundary algebra, and the toric-code electric/magnetic boundary
  examples.
- Added a quoted theorem boundary for the Crane-Yetter / Walker-Wang
  four-dimensional boundary principle.
- Updated the Volume VIII Chapter 9 dossier.

## Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The first build attempt correctly caught use of `\mathscr`, which is not
defined by the manuscript preamble.  The text was corrected to `\mathcal`.
The subsequent monograph build and log scan completed cleanly.  The rebuilt
PDF has 1294 pages.
