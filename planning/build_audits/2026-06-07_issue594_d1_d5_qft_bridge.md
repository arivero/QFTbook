# 2026-06-07 Issue #594 D1--D5 QFT Bridge Pass

## Scope

- Target issue: #594, conformal-manifold worked examples and the missing
  intrinsic D1--D5 QFT bridge to the symmetric-product CFT point.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`.
- Added `rem:d1-d5-coulomb-throat-higgs-bridge` after the ADHM/D1--D5 Higgs
  branch example.

## Quality Audit

- This pass is physics-depth work, not an additional ADHM or moduli-space
  dimension cell.  It supplies the QFT branch data that the latest #594 review
  identified as missing: the rank-one Coulomb throat, torsion flux, positive-FI
  lift of the empty-framing Coulomb locus, and conditional operator-map bridge
  to the symmetric-product blow-up tangent.
- The bridge keeps the protected Higgs metric, quantum-corrected Coulomb
  metric, torsion/\(B\)-field data, FI lifting, and global IR CFT
  identification as separate inputs.
- The companion check rejects the dimension-only shortcut: two D1--D5 rank
  pairs can have the same Higgs-branch dimension while carrying different
  Coulomb-throat flux data.
- The addition does not claim a full proof of the D1--D5 IR SCFT relation, a
  global hyperkahler quotient theorem, or all-order factorization of the
  noncompact throat.

## Verification

- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_moduli_space_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_moduli_space`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --window 120 --stride 60 --fail --limit 20`
- Process-language scan of the target TeX file for `claude`, `review`,
  `directive`, `monitor`, `issue #`, `GitHub`, and `planning/build_audits`:
  clean.
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
