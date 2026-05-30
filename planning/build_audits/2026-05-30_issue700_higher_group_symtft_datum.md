# Issue #700: Higher-Group Symmetry-TQFT Datum

## Target

Volume IX, Chapter 11 was listed as a remaining partial definition-locality
gap in #700.  The chapter already contained a finite triangulated higher
gauging definition and a substantive finite cochain fusion theorem, but the
central object "QFT with finite higher-group symmetry and symmetry-TQFT
presentation" was not aggregated before the background, anomaly, and
condensation constructions.

## Edit

- Added `hyp:higher-group-symmetry-tft-datum` near the chapter opening.
- The datum collects the QFT, finite two-group
  \(\mathbb G=(G_0,A,\rho,\beta)\), background higher groupoids,
  anomaly-line functor, one-higher-dimensional symmetry TQFT, QFT boundary
  condition, topological defect system, and anomaly-trivialization /
  counterterm data.
- Rewrote the two-group-background and symmetry-TQFT entry points to refer
  back to the named datum.
- Updated the Chapter 11 dossier.

## Scope

The existing finite cochain theorem and QED defect construction remain
downstream consequences after the datum is supplied.  The construction of the
continuum interacting QFT, its symmetry-TQFT boundary, and its full defect
system remains the open problem already labeled in the chapter.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- Output: `monograph/tex/main.pdf`
- Page count: 2682
