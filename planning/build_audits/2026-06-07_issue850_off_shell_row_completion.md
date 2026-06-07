# Issue #850 Off-Shell Row-Completion Pass

## Scope

- Continued the Volume VII Chapter 08 Higgs-metric background-field repair.
- Added a row-resolved criterion for deriving the heavy \(Q\)-complex from the
  rank-one gauge-fixed quadratic Lagrangian.
- Extended the finite companion so a missing auxiliary/Yukawa row contact leaves
  the predicted trace-log residual.

## Substance Audit

- Physics depth: this pass moves from abstract spectral pairing to the actual
  sources of the fluctuation operator: kinetic-frame, gauge-fixing/ghost,
  moment-map auxiliary, and Yukawa rows.
- Scope boundary: the chapter still treats smooth Higgs-metric protection as a
  theorem-boundary input; this is not promoted to an all-order proof.
- Failure mode exposed: deleting a row before assembling the determinant is only
  allowed if the Schur-complement contact is retained.
- Coherence check: the old long-multiplet balance remains after the determinant
  mechanism, and only as a diagnostic.

## Verification

- `python3 calculation-checks/susy_moduli_space_checks.py`
- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_moduli_space`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail --limit 40`
- TeX planning-language leakage scan for `claude|review|directive|monitor|issue #|GitHub|planning/build_audits`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
