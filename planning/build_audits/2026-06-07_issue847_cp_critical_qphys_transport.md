# Issue #847 CP Critical Qphys Transport Audit

## Scope

- Rewrote the first \(\mathbb P^{N-1}\) Hori--Vafa critical-point example in
  Volume VII Ch09 so the algebraic torus uses transported mirror coordinates
  \(\widehat X_i=c_i e^{-Y_i}\).
- Made the root equation use
  \(q_{\rm phys}=e^T\prod_i c_i\) at first appearance, rather than using bare
  \(e^T\) and repairing the coordinate only in the later residue proposition.
- Added a companion finite check that rejects untransported bare-FI roots and
  residues after vortex-determinant/operator coefficient transport.

## Architecture Re-Audit

- Old interrupted route: the normalization section correctly introduced
  \(q_{\rm phys}\), but the next projective-space critical-point example still
  displayed \(X_i^N=e^T\) before the later residue proposition switched to
  \(q_{\rm phys}\).
- New canonical route: vortex coefficients first define the transported torus
  variables; the CP root equation, the residue trace, and the quantum-product
  comparison all use the same \(q_{\rm phys}\).
- Material merged or relocated: no physics claim was removed.  The bare chart
  is retained as the special case \(c_i=1\), while the general critical-point
  statement now carries the determinant/operator normalization.
- Independent evidence retained: Coulomb determinant sign, compact
  FI-periodicity, vortex-normalization FI-character transport, common-flux
  projection, CP residue trace, stable-map representative independence, and
  direct vortex-observable residual budgeting.
- Unresolved theorem boundary: the finite vortex coefficients, continuum
  vortex regulator limit, nonzero-mode determinant, and full original-to-mirror
  operator map remain supplied inputs rather than proved theorems.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
