# Issue #850 Rank-One Row-Jacobian Audit

## Scope

- Added a Ch08 component-row derivation for the rank-one \(U(1)\), two-hyper
  Higgs patch.
- The new example derives the real moment-map, complex moment-map,
  background-gauge-fixing, and Yukawa row Jacobians from the gauge-fixed
  component Lagrangian.
- It separates the heavy row projector from the quotient tangent zero mode and
  identifies the row-contact seagull required when the Higgs background moves.

## Quality Audit

- This is a physics-side determinant increment, not a moduli-space or
  multiplicity-ledger addition.
- The result closes one residual gap left by the abstract heavy \(Q\)-complex:
  the rank-one rows now have an explicit component-Lagrangian origin.
- It still does not prove the all-order Higgs-branch metric theorem or the full
  continuum trace-log calculation.  The remaining obligations are the complete
  gauge-fixed heavy complex, regulator action on that complex, and the
  Ward/local-counterterm argument.

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
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_theorem_form.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`
