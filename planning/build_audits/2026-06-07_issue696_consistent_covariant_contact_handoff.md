# Issue #696 Consistent-Covariant Contact Handoff Audit

## Scope

- Added a Cartan source-contact handoff proposition in Volume II Chapter 20.
- The new proposition requires a counterterm-shifted consistent current contact
  to be projected to the polarized class \(S_{ijk}=C_{(ijk)}\) before applying
  the Bardeen--Zumino factor-three map to the covariant current.
- Extended the anomaly-polynomial companion with an exact finite model and
  negative controls rejecting factor-three application before polarization and
  rejecting a one-unit Bardeen--Zumino shortcut.

## Quality Audit

- This is a local anomaly-mechanism increment, not another detached coefficient
  cell: it connects source Ward contacts, counterterm dependence, the
  consistent-current representative, the Bardeen--Zumino current, and the
  covariant-current representative in one finite chain.
- It directly supports the #696 standard by keeping QFT anomaly conclusions in
  the monograph's own source-functional conventions.
- It does not prove the full local BRST cohomology classification, the analytic
  index theorem, global determinant/Pfaffian-line holonomies, or the existence
  of a nonperturbative chiral gauge regulator.

## Verification

- `python3 -m py_compile calculation-checks/anomaly_polynomial_descent_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/anomaly_polynomial_descent_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`
- `tools/run_calculation_checks.sh --python-only --only anomaly_polynomial_descent`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `rg -n "claude|review|directive|monitor|issue #|GitHub|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
  returned no matches.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
