# Issue #844 Controlled-Approximation Data-Title Re-Audit

## Scope

- Repaired the status surface for `controlledapproximation` blocks whose titles
  made exact data packages or proof-obligation vectors look like approximation
  regimes.
- Demoted the exact four-point color--kinematics comparison and the two-master
  threshold/boundary-constant package in Volume II Chapter 6 from
  `controlledapproximation` to `construction`.
- Demoted the BCFT boundary-observable vector package in Volume V Chapter 14
  from `controlledapproximation` to `construction`.
- Kept genuine controlled regimes in place but retitled them away from data
  package language: large-\(N_c\) spectral pole window, charged external-sector
  ray--velocity matching, and weak-scalar 2PI/Kadanoff--Baym regime.
- Tightened `tools/audit_theorem_form.py` and the strict writing harness so
  future `controlledapproximation` titles containing `data` or `datum` are
  rejected unless the material is moved to an ordinary construction, example,
  remark, or proof-obligation map.

## Re-Audit Notes

- This is a semantic-status repair, not a claim that issue #844 is closed.  It
  fixes one machine-auditable class called out by the review: exact finite
  comparison/data packages should not be advertised as controlled
  approximations.
- The pass also caught a real downstream consequence of the Ch19 title edit:
  the SCET factorization occurrence ledger uses source-derived line anchors, so
  the shortened large-\(N_c\) title shifted later Ch19 factorization review rows.
  Those anchors were updated and rechecked with the SCET occurrence-ledger
  script.
- No planning directive, issue metadata, or review language was inserted into
  monograph TeX.

## Checks

- `python3 -m py_compile tools/audit_theorem_form.py calculation-checks/generalized_unitarity_reduction_checks.py calculation-checks/charged_flux_dressing_checks.py`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- Focused companion scripts:
  `generalized_unitarity_reduction_checks.py`,
  `charged_flux_dressing_checks.py`, `large_n_topology_checks.py`,
  `bcft_cardy_checks.py`, and `kinetic_theory_checks.py`.
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction --only charged_flux_dressing --only large_n_topology --only bcft_cardy --only kinetic_theory`
- `python3 calculation-checks/scet_factorization_checks.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`

All selected checks passed.  Wolfram Language checks were not selected.
