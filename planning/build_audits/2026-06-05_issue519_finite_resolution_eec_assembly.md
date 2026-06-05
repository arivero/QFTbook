# 2026-06-05 Issue #519 Finite-Resolution EEC Assembly Audit

## Scope

- Targeted issue #519, energy correlators as physical detector observables.
- Added `ca:finite-resolution-eec-observable-assembly` to Ch19b after the
  calorimetric-coordinate theorem.
- Extended `energy_correlator_sum_rule_checks.py` with a finite-resolution
  detector map, exact binned-versus-unbinned smeared EEC difference, Lipschitz
  binning bound, and residual-budget negative control.

## Substance Audit

- This pass is physics-facing architecture, not a new isolated finite identity:
  it separates coordinate completeness from a QCD prediction for measured EEC
  bins.
- The new text requires the detector-binned positive energy measure, contact
  and endpoint conventions, short-distance light-ray or hard/jet/soft
  coefficient chart, nonperturbative lift, and residual ledger to be specified
  together.
- The companion check exercises the detector-resolution and residual-budget
  claims with exact rational data, including the failure of a budget that omits
  detector binning.

## Planned Verification

- Focused Python check for `energy_correlator_sum_rule_checks.py`.
- Focused monograph audits for theorem form, display labels, negative-scope
  prose, and style density on Ch19b.
- Chapter dossier and calculation-evidence audits.
- Full monograph build before commit.
