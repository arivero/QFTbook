# Issue #729 Observable-Output Backreaction Pass

## Scope

- Volume XII, Chapter 11:
  `ca:semiclassical-retained-metric-observable-output`.
- Companion evidence: `calculation-checks/semiclassical_backreaction_checks.py`.
- Dossier/inventory updates: Ch11 dossier and calculation-check README.

## Substance

- Added the physical readout layer after the nonlinear retained backreaction
  chart.  The controlled calculation now has to turn the mean metric and
  Einstein-Langevin covariance into a retained metric observable.
- The observable chart keeps the linear response, quadratic deterministic
  response, fluctuation bias `1/2 tr(Q^X C_h)`, observable covariance, and a
  signal-to-noise test in the same Ward-clean sector.
- The text rejects three overstatements: treating a gauge coordinate of `h` as
  an observable, dropping the fluctuation bias while keeping quadratic metric
  response, and using a projected or partial covariance to overstate the
  precision of a semiclassical prediction.
- Scope remains finite retained-sector control.  This pass does not construct
  the interacting stress tensor, prove an interacting Hadamard state theorem,
  or solve the infinite-dimensional stochastic semiclassical equation.

## Verification

Completed:

- `python3 -m py_compile calculation-checks/semiclassical_backreaction_checks.py`
- `python3 calculation-checks/semiclassical_backreaction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only semiclassical_backreaction`
- focused Ch11 theorem/display/scope/style audits:
  `audit_theorem_form.py`, `audit_unnumbered_display_labels.py`,
  `audit_negative_scope_prose.py --fail`, and
  `audit_style_density.py --fail --limit 20`
- metadata-leak scan for tracker/review/directive language in touched
  monograph and check files; the only hit was ordinary chapter prose
  containing the word "issue"
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- full `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` (clean build/log scan, 3378 pages)
