# 2026-06-05 Issue #725 Evidence Independence Repair

## Scope

- Target: two concrete calculation-companion independence failures named in
  issue #725.
- Files repaired:
  - `calculation-checks/hydrodynamic_modes_checks.py`
  - `calculation-checks/finite_temperature_path_integral_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_x/chapter05_hydrodynamics_from_ward_identities.md`
  - `planning/chapter_dossiers/volume_x/chapter02_finite_temperature_path_integrals.md`

## Re-Audit Notes

- `check_retarded_singularity_taxonomy()` now constructs a finite
  Gibbs/Lehmann retarded response from a three-level system and derives its
  real transition lines before testing open-upper-half-plane analyticity.
  The negative control is an actual denominator-root list with an
  open-upper-half-plane pole.
- `check_finite_sum_rule_preserving_instability()` no longer certifies
  positivity from a sampled frequency grid.  It uses the support-wide bound
  \(|h_\epsilon|\le \eta_\ast+\sum_j|c_j(\epsilon)|\), the monotone lower
  bound of the smooth reference spectrum on the whole perturbation support,
  and an amplitude chosen from that analytic margin.
- The monograph claims did not require TeX changes; the repair is to the
  companion evidence and the planning/dossier evidence ledger.

## Verification

- `python3 -m py_compile calculation-checks/hydrodynamic_modes_checks.py calculation-checks/finite_temperature_path_integral_checks.py`
- `python3 calculation-checks/hydrodynamic_modes_checks.py`
- `python3 calculation-checks/finite_temperature_path_integral_checks.py`
- `tools/run_calculation_checks.sh --python-only --only hydrodynamic_modes`
- `tools/run_calculation_checks.sh --python-only --only finite_temperature_path_integral`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`

All commands passed on 2026-06-05.
