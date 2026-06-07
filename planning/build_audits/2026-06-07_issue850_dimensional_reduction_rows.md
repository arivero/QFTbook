# Issue #850 Dimensional-Reduction Row Audit

## Scope

- Extended the Volume VII Chapter 08 Higgs background-field development with a
  lower-dimensional row audit for the same rank-one Higgs patch.
- The new example separates the reduced connection
  \(A_M=(A_\mu,\sigma_I)\), identifies the \(4-d\) reduced vector-multiplet
  scalar rows, and displays their square-completion contact
  \(C_{\rm red}^{(d)}\).
- The pass makes explicit that the \(d+(4-d)+2+4-2-8=0\) balance is only an
  inventory diagnostic after the reduced scalar row contacts have been kept.
- It also separates the two-dimensional symmetric metric channel from a possible
  antisymmetric \(B\)-field/Wess--Zumino channel.

## Quality Audit

- This targets the #850 dimensional-reduction objection directly: a fixed
  four-component gauge-field entry is no longer allowed to hide lower-dimensional
  reduced vector-scalar determinant rows.
- The companion now checks that omitting reduced vector-scalar row contacts in
  3d/2d leaves a trace-log residual, while 4d has no such reduced row.
- The pass does not claim the all-order Higgs-metric theorem or a complete
  continuum determinant proof; it closes another component-level obligation
  inside the explicit background-field calculation.

## Verification

- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_moduli_space_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_moduli_space`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `rg -n "claude|review|directive|monitor|issue #|GitHub|planning/build_audits" monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
  returned no matches.
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_theorem_form.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`
