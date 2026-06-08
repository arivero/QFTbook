# Issue #850 Higgs Two-Jet Field-Redefinition Quotient Audit

## Scope

- Added `ex:higgs-branch-field-redefinition-two-jet-quotient` in Volume VII
  Ch08 after the metric-source transport projection.
- Worked the rank-one zero-cotangent \(\mathbb P^1\) slice with
  \(g_\zeta=\zeta(1-2r+3r^2+\cdots)\,dz\,d\bar z\) and a local
  Higgs-coordinate vector field \(v^z=(a+br)z\).
- Derived
  \(J^2(\mathcal L_v g_\zeta)=\zeta(2a,-8a+4b,18a-12b)\), separated the FI
  source direction \(S=(1,-2,3)\) from the independent field-redefinition
  direction \(B_{\rm fr}=(0,4,-12)\), and exposed the intrinsic residual
  \(k_2+3k_1+3k_0\).

## Architecture Re-Audit

- Old interrupted route: the chapter said the trace-log kernel must be
  quotiented by field redefinitions and FI/mass transport, but the finite
  companion only removed the FI-source direction explicitly.
- New canonical route: the heavy determinant output is first reduced by source
  transport and Higgs-coordinate Lie-derivative directions; only the residual
  two-jet class is treated as a local branch-metric datum.
- Physics-depth check: this is an extraction step from determinant data to the
  sigma-model observable, not another component inventory.  It prevents both
  source-only overcounting of coordinate artifacts and point-metric-only
  undercounting of curvature residuals.
- Unresolved theorem boundary: this pass does not prove the all-order
  Higgs-branch metric theorem, construct the full continuum elliptic complex,
  or evaluate all continuum mixed diagrams.  It tightens the local metric
  projection used by those obligations.

## Verification

- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_moduli_space_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_moduli_space`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
