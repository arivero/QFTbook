# Issue 554 SymTFT And Condensation Development Audit

## Scope

This pass addresses the finite and theorem-level parts of GitHub issue #554:

- finite five-dimensional `Z_N` one-form symmetry TQFT;
- boundary fixed/summed interpretation of one-form gauging;
- finite higher-gauging condensation defect and its fusion calculation;
- relationship to four-dimensional noninvertible condensation defects;
- source-lineage boundary for noninvertible chiral defects in abelian gauge
  theory;
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
- Added a quoted theorem boundary for noninvertible chiral defects in abelian
  gauge theory, explicitly stating that the regulator-level construction is not
  yet supplied in the monograph.
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

## Issue Status

Issue #554 should remain open after this pass.  The finite SymTFT and
condensation-defect mechanism have been developed and proved at the cochain
level, but the issue also asks for an explicit noninvertible chiral-defect
operator construction in QED.  The chapter now records the known theorem
boundary and the missing regulator-level construction; it does not yet provide
that construction as a self-contained monograph proof.
