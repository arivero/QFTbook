# 2026-05-26 Twist-Field Conformal-Perturbation RG Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass expands the
twist-field deformation section of Volume V, Chapter 11 from a one-line
quadratic obstruction to a self-contained cutoff-shell derivation of the
second-order conformal-perturbation beta function.

## Substantive Edits

- Added a proposition deriving the annular OPE contribution to the
  length-scale Wilsonian beta function for spinless twist-field
  perturbations.
- Recorded the relation between the length-scale beta function and the
  energy-scale beta function, fixing the sign of the quadratic OPE term.
- Added the quadratic contact-term/coupling-coordinate scheme-shift law and
  identified the resonant channels where the coefficient is scheme-invariant.
- Explained the marginal twist-field obstruction as a projection to
  dimension-two nonredundant primaries, rather than as a bare monodromy
  statement.
- Added `calculation-checks/conformal_perturbation_rg_checks.py` for exact
  rational checks of the cutoff-power cancellation, second-order \(\pi\)
  factor, sign convention, and scheme-shift formula.
- Updated the calculation-check inventory, Chapter 11 dossier, stringbook
  crosswalk, and this build audit note.

## Verification

Final verification for this pass:

- `python3 calculation-checks/conformal_perturbation_rg_checks.py`
- `python3 -m py_compile calculation-checks/conformal_perturbation_rg_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The post-rebase TeX build completed cleanly at 1827 pages.
