# Issue #700: Seiberg-Witten Coulomb-Branch Datum

## Target

Volume VII, Chapter 7 was listed as a partial issue #700 gap: the chapter had
definitions for argument-status labels, ADHM data, Nekrasov factors, cusp
models, and local confining strings, but no opening block aggregating the
central Seiberg-Witten object.

## Edit

- Added `hyp:seiberg-witten-coulomb-branch-datum` near the chapter opening.
- The hypothesis now collects the assumed four-dimensional `N=2` local QFT,
  the Coulomb branch, discriminant locus, smooth Abelian locus, electromagnetic
  charge local system, integral Dirac pairing, period section, local
  prepotential, Abelian Wilsonian action, singularity data, BPS normalization,
  and optional curve realization.
- Rewrote the Coulomb-coordinate, special-coordinate, and period-data entry
  points to refer back to this datum.
- Updated the Chapter 7 dossier.

## Scope

The edit does not claim a regulator-level construction of four-dimensional
Seiberg-Witten theories.  The new block is deliberately a hypothesis, and the
construction problem remains `op:theorem-level-seiberg-witten-construction`.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh` (clean; `main.pdf` has 2676 pages)
