# Issue 554 SymTFT And Condensation Development Audit

## Scope

This audit covers the finite SymTFT, condensation-defect, and abelian
noninvertible chiral-defect work for GitHub issue #554:

- finite five-dimensional `Z_N` one-form symmetry TQFT;
- boundary fixed/summed interpretation of one-form gauging;
- finite higher-gauging condensation defect and its fusion calculation;
- relationship to four-dimensional noninvertible condensation defects;
- explicit compact-QED noninvertible chiral defects, including fractional Hall
  dressing, half-space magnetic gauging, fusion, and action on 't Hooft lines;
- categorical-level warning for fusion two-category truncations.

## Edits

- Expanded
  `monograph/tex/volumes/volume_ix/chapter11_higher_group_symmetry_symmetry_tft.tex`
  with an explicit cochain action `b cup delta c` for the finite one-form
  SymTFT and a closed-manifold gauge-invariance proof.
- Added a finite electric/magnetic line-charge example with the finite Dirac
  pairing, while avoiding the incorrect statement that arbitrary loop pairs in
  four Euclidean dimensions have a topological pairwise braiding invariant.
- Added a triangulated higher-gauging condensation defect as a closed
  two-cochain sum and proved the finite fusion mechanism producing a
  three-dimensional finite two-form gauge-theory factor.
- Added a quoted theorem boundary for four-dimensional condensation defects:
  the finite cochain mechanism is proved in the chapter, while the continuum
  construction of surface operators and junctions remains a separate QFT input.
- Replaced the previous quoted theorem boundary for noninvertible chiral
  defects with an explicit compact-QED construction: the rational axial wall is
  dressed by the three-dimensional \(\mathcal A_{N,p}\) Hall theory, with
  compact \(B_A=[F/(2\pi)]\bmod N\) coupling.
- Proved the topological cancellation for \(D_{N,1}\), described the general
  \(p/N\) cancellation by the Pontryagin-square one-form anomaly, and added the
  half-space magnetic gauging construction with compact fields \(b,c\).
- Added the action on local fermions, Wilson lines, and renormalized 't Hooft
  lines, and proved noninvertibility through orientation-reverse fusion into a
  magnetic condensation defect.
- Added a rigorous renormalized 't Hooft-line definition in
  `monograph/tex/volumes/volume_ix/chapter03_line_surface_domain_wall_operators.tex`
  as a tubular-neighborhood boundary condition with cocharacter magnetic
  charge, boundary-preserving gauge transformations, and local line
  counterterms in a specified regulator or constructive framework.
- Added a higher-categorical truncation section distinguishing the full
  four-dimensional defect object from fusion two-category truncations.
- Added a cross-reference in
  `monograph/tex/volumes/volume_ix/chapter09_categorical_symmetry_and_defect_fusion.tex`
  from the categorical framework to the Chapter 11 finite one-form SymTFT
  construction.
- Updated the Chapter 9 and Chapter 11 dossiers.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean after replacing all new `\over`
  fractions with `\frac`, shortening an overfull quoted-theorem title, and
  making the local comparison ledger unnumbered so the table of contents does
  not create an overfull section number.
- Follow-up build after the QED defect and 't Hooft-line additions:
  `tools/build_monograph.sh` clean; `pdfinfo monograph/tex/main.pdf` reports
  1305 pages.

## Issue Status

Issue #554 can now be closed.  The finite cochain SymTFT mechanism is proved,
the compact-QED noninvertible chiral defect is constructed explicitly as a
path-integral defect, and the text states the remaining theorem boundary
honestly: a fully axiomatic version would still require a nonperturbative
reconstruction of compact QED, its charged line sectors, and the associated
defect Hilbert spaces.
