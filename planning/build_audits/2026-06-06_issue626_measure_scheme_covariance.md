# 2026-06-06 Issue #626 Measure-Scheme Covariance Re-Audit

## Scope

- Target: Volume VII Chapter 09, the \(2D\) \(\mathcal N=(2,2)\)
  GLSM/Hori--Vafa/projective-space protected observable lane.
- Objective: re-audit the degree-one instanton-observable bridge so finite
  vortex-measure normalization changes cannot be hidden by a mirror-coordinate
  rescaling.
- Boundary: this pass still does not derive the vortex determinant spectra,
  prove compactness of the vortex sector, or prove Hori--Vafa equivalence as a
  full continuum QFT statement.

## Changed Artifacts

- `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `calculation-checks/susy_2d_lg_glsm_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`
- `planning/source_inventory/stringbook_crosswalk.md`
- `planning/build_audits/2026-06-06_issue626_measure_scheme_covariance.md`

## Re-Audit Notes

- Added `ca:cpn-degree-one-measure-scheme-covariance` between the A-model
  zero-mode bridge and the degree-one residual template.
- The new block treats the retained coefficient as
  `q_Lambda * int Omega_{Lambda,1}`, not as any separate vortex coefficient,
  zero-mode measure, determinant density, or Hori--Vafa coordinate.
- The companion check verifies exact invariance under simultaneous transport of
  vortex coefficient rescalings, the inverse FI-coordinate shift, retained-chart
  Jacobians, determinant/Berezin densities, and orientation/operator signs.
- The negative controls reject stale FI coordinates, missing inverse Jacobians,
  and untransported orientation signs.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`

All commands passed on 2026-06-06.
