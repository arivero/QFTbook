# 2026-06-05 Issue #626 CP A-Model Zero-Mode Bridge

## Scope

- Target: Volume VII Chapter 09, the \(2D\) \(\mathcal N=(2,2)\)
  GLSM/Hori--Vafa/projective-space protected observable lane.
- Objective: deepen the worldsheet/vortex-instanton discussion as a QFT
  observable calculation, not a mirror-formula or stable-map-count shortcut.
- Boundary: this pass does not claim a continuum GLSM proof, a full
  Hori--Vafa equivalence theorem, or a derivation of the vortex determinant
  spectra.  It records the finite-regulator bridge that must be supplied.

## Changed Artifacts

- `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `calculation-checks/susy_2d_lg_glsm_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`
- `planning/build_audits/2026-06-05_issue626_cpn_amodel_zero_mode_bridge.md`

## Re-Audit Notes

- Added `ca:cpn-degree-one-amodel-zero-mode-measure-bridge` before the
  degree-one residual template.
- The new block separates the supplied vortex-normalized fugacity, bosonic
  collective-coordinate density, nonzero-mode determinant-line element, and
  A-twisted Berezin zero-mode coefficient.
- The point is to prevent the line count or the Hori--Vafa residue from being
  treated as the physical correlator before determinant orientation,
  zero-mode saturation, compactification/contact data, and operator matching
  have been supplied in the same regulator.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`

All commands passed on 2026-06-05.
