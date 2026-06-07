# Issue #696 Source-Ward Normalization Re-Audit

## Scope

- Re-audited the Volume II Chapter 20 source-Ward cubic anomaly proposition
  after the external critique that the effective-action coefficient was being
  identified too directly with the raw group-theory cubic trace.
- Repaired the proposition to separate:
  - the raw Cartan symmetric trace tensor \(\mathsf T_{ijk}\);
  - the Cartan anticommutator cancellation tensor
    \(\mathsf G_{i;jk}=2\mathsf T_{ijk}\) on the commuting chart;
  - the Euclidean effective-action Ward coefficient
    \(C_{(ijk)}=\kappa_{\rm anom}\mathsf T_{ijk}\), with
    \(\kappa_{\rm anom}=2\pi i/[6(2\pi)^3]\) in the index normalization;
  - the representative-dependent single-current contact \(D_{i;jk}=2C_{i;jk}\).
- Updated the anomaly-polynomial companion so the source-Ward check has a
  negative control rejecting raw-trace/effective-coefficient equality before
  the anomaly normalization is applied.

## Quality Audit

- This pass keeps the physical source-Ward contact calculation, but narrows the
  claim to the scheme-independent polarized class coordinate.
- The individual current contact is now explicitly representative-dependent
  and not a separated-point observable.
- The repair strengthens the anomaly proof-debt track without importing a new
  BRST cohomology theorem or pretending to prove nonperturbative chiral-gauge
  existence.

## Verification

- `python3 -m py_compile calculation-checks/anomaly_polynomial_descent_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/anomaly_polynomial_descent_checks.py`
- `tools/run_calculation_checks.sh --python-only --only anomaly_polynomial_descent`
- Focused Chapter 20 theorem-form, display-label, negative-scope, style-density,
  strict text, and process-language leakage audits.
- `python3 tools/audit_theorem_form.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
