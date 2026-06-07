# 2026-06-07 Issue #850 Supercharge-Factorization Pass

## Scope

- Target issue: #850, replacing the Higgs-metric multiplicity ledger with a
  genuine background-field determinant mechanism.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`.
- Companion target: `calculation-checks/susy_moduli_space_checks.py`.

## Substance

- Added `ex:higgs-branch-supercharge-factorization` after the mass-curvature
  Ward-pair cell.
- The new cell explains how the matched second-variation vertices arise from an
  off-shell regulated heavy complex:
  \(O_B(s)=Q(s)^\dagger Q(s)\), \(O_F(s)=Q(s)Q(s)^\dagger\).
- It derives the generated \(X,Y\) vertices from
  \(Q(s)=Q_0+sQ_1+s^2Q_2/2+\cdots\), including the
  \(2Q_1^\dagger Q_1\) and \(2Q_1Q_1^\dagger\) contacts.
- The companion finite check verifies spectral trace-log pairing and a
  dropped-contact negative control.

## Quality Audit

- This pass is physics-depth work inside the fluctuation determinant.  It
  explains why auxiliary completion and a supersymmetry-preserving regulator are
  part of the Higgs-metric calculation rather than optional notation.
- It does not add ADHM, quotient, or dimension-counting material.
- The TeX addition is reader-facing physics content and contains no review
  directives, GitHub/process language, automation instructions, or planning
  text.

## Verification

- `python3 calculation-checks/susy_moduli_space_checks.py`
- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`
- `python3 calculation-checks/scet_factorization_checks.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail --limit 40`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex --fail --limit 40`
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
