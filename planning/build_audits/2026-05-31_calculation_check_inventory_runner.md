# 2026-05-31 Calculation-Check Inventory and Runner Pass

Scope: GitHub issue #707, `calculation-checks/`, `tools/run_calculation_checks.sh`,
and `planning/12_strict_writing_harness.md`.

What changed:
- Added `calculation-checks/INDEX.md` to state the calculation-check operating
  contract: exact active inventory is available from the runner, detailed
  per-script descriptions live in `calculation-checks/README.md`, and full
  calculation-check sweeps are explicit batch operations rather than default
  build gates.
- Extended `tools/run_calculation_checks.sh` with `--list`, `--only`,
  `--python-only`, `--wolfram-only`, and `--skip-wolfram`.  The runner now
  selects all `calculation-checks/*.py` and `calculation-checks/*.wl`, so
  companion scripts such as `conformal_block_companion.py` and
  `sw_su2_periods.py` are visible to the inventory.
- Updated `calculation-checks/README.md` with the four missing active-script
  ledger entries found by an inventory-vs-README scan:
  `cft_correlator_kinematics_checks.py`, `cluster_sweep_grid_checks.py`,
  `renormalizability_counterterm_checks.py`, and
  `tomita_standard_form_checks.py`.
- Tightened the strict writing harness: relevant calculation scripts must be
  run deliberately when formulae or convention families change, while
  `tools/build_monograph.sh` remains a TeX/manuscript-structure gate and does
  not run the whole calculation suite.

Verification:
- `bash -n tools/run_calculation_checks.sh`
- `tools/run_calculation_checks.sh --list`
- targeted runner samples for the four ledger-repair scripts
- inventory-vs-README scan showing no active `.py` or `.wl` script missing
  from the README ledger
- `git diff --check`

No monograph TeX source was changed in this pass, so no LaTeX rebuild was
needed.
