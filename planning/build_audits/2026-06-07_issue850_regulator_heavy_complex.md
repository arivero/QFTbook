# Issue #850 Regulator-Compatible Heavy-Complex Audit

## Scope

- Added a Chapter 08 example specifying how a Wilsonian or Pauli--Villars
  regulator acts on the nonzero Higgs heavy \(Q\)-complex.
- The new cell keeps the same regulated spectral function on the paired
  bosonic and fermionic nonzero spectra and states the local regulator moment
  conditions needed for the two-derivative coefficient.
- Extended `susy_moduli_space_checks.py` with exact rational tests for paired
  regulator cancellation, unpaired regulator masses, tangent-dependent
  regulator vertices, and unprojected zero modes.
- Added the companion to the evidence-contract manifest and updated the README
  and Chapter 08 dossier.

## Quality Audit

- This is a determinant/regulator layer of the #850 background-field repair,
  not a component-count wrapper.
- It advances the physical calculation by forcing the regulator to act on the
  same supersymmetric heavy complex used by the trace-log argument.
- It does not prove the full all-order Higgs-branch metric
  nonrenormalization theorem, construct the continuum elliptic complex, or
  settle singular/mixed-branch global questions.

## Verification

- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_moduli_space_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_moduli_space`
- Focused Chapter 08 theorem/display/negative-scope/style/text audits.
- Chapter 08 TeX scan for review/directive/planning language.
- JSON, evidence-contract, inventory, dossier, whitespace, full Python
  calculation-check, and full monograph-build audits.
