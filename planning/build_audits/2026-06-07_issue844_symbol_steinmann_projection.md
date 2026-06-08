# Issue #844 Symbol Steinmann Projection Re-Audit

## Scope

- Repaired the Volume II Chapter 6 "Symbol-level Steinmann check for
  transported masters" hotspot named in the semantic `controlledapproximation`
  audit.
- Demoted the finite residue/projection model from `controlledapproximation` to
  the construction `constr:symbol-steinmann-projection-test`.
- Inserted an explicit physical extraction bridge before the construction:
  first fix the regulated amplitude or infrared-finite remainder, master basis,
  coefficient projection, Euclidean boundary constants, lower-sector
  completion, Feynman sheet, and regulator/subtraction data; only then can an
  ordered symbol word be interpreted as an ordered physical discontinuity.
- Strengthened the companion finite check so a symbol-only Steinmann budget is
  rejected when boundary-distribution, rational-prefactor, lower-sector, and
  regulator/subtraction data are omitted.

## Re-Audit Notes

- This is an argument-architecture repair, not only a label change.  The
  reader-facing flow now runs from physical boundary values and causal
  Steinmann hypotheses to the exact symbol projection test, rather than making
  a finite symbol matrix look like a controlled approximation to a loop
  amplitude.
- The construction remains useful: it keeps overlapping single cuts nonzero,
  kills both overlapping ordered double words under the physical projection,
  allows a compatible sequential word to survive, and rejects projections that
  pass all single-cut tests but violate Steinmann ordered-word constraints.
- The pass does not claim to prove Steinmann relations for all massless,
  regulator-limit, anomalous-threshold, or extended-Steinmann settings.  Those
  remain under the later quoted theorem, warning, and open scope boundaries.

## Checks

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
- `tools/build_monograph.sh`
- `git diff --check`

All selected checks passed.  Wolfram Language checks were not selected.
