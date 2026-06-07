# Issue #850 Two-Dimensional Torsion-Boundary Audit

## Scope

- Restricted the Volume VII Chapter 08 smooth Higgs-metric protection input to
  the torsion-free \(2d\ \mathcal N=(4,4)\) class when it is used as a pure
  hyperkahler metric theorem.
- Rewrote the torsionful \(2d\) case as a coupled HKT/bi-Hermitian local
  counterterm problem for \((\delta g,\delta B,\delta\Phi)\) and the torsionful
  connections, rather than as an independent antisymmetric side channel.
- Updated the D1--D5 discussion so the positive-FI smooth Higgs stratum uses the
  torsion-free metric statement, while Coulomb-throat and \(H\)-flux data require
  the coupled two-dimensional branch treatment.

## Quality Audit

- This targets the latest #850 review concern directly: symmetrizing a
  two-index trace-log kernel is no longer presented as a supersymmetric
  classification when \(H=dB\) is allowed.
- The companion now has a finite adversarial check showing that a metric-only
  projection drops the required \(B\), dilaton/source, and torsionful connection
  slots of a torsionful \((4,4)\) counterterm.
- Scope boundary retained: this is a theorem-boundary repair, not the all-order
  Higgs-metric theorem and not a full continuum determinant evaluation.

## Verification

- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_moduli_space_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_moduli_space`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- TeX process-language leakage scan over the edited chapter returned no matches
  for directive/review/planning/monitor terms.
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/tmp/qft_evidence_contracts_issue850.json`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
