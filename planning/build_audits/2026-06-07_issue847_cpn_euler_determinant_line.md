# Issue #847 Projective Determinant-Line Audit

## Scope

- Added a degree-one `P^{N-1}` Euler-sequence determinant-line example to
  Volume VII Chapter 09.
- The new calculation pulls back
  `0 -> O -> O(1)^N -> phi^* T P^{N-1} -> 0`, computes the
  `H^0(O(1)^N)/H^0(O)` tangent zero-mode quotient, and records the inherited
  complex determinant-line orientation.
- It separates three direct-instanton factors that were previously only named
  in the residual budget: common-rescaling removal, paired nonzero-mode
  cancellation, and the finite incidence Jacobian.

## Quality Audit

- This pass moves the Hori--Vafa projective-instanton lane toward physical
  measure/fluctuation content rather than adding another mirror-coordinate
  identity.
- It does not claim the full continuum Hori--Vafa operator map, vortex
  compactness theorem, or uniform regulator limit.  The result is a retained
  finite-window calculation that the direct A-model measure side must pass
  before the mirror residue is used as a comparison.
- The companion rejects the shortcuts most relevant to the monograph standard:
  forgetting the homogeneous gauge quotient, flipping the determinant-line
  orientation, replacing the paired nonzero-mode determinant by an arbitrary
  scalar, or omitting an obstruction Euler factor.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `rg -n "claude|review|directive|monitor|issue #|GitHub|planning/build_audits" monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  returned no matches.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`
