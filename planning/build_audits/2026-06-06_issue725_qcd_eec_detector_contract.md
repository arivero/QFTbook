# Issue #725/#519 QCD EEC Detector-Contact Contract Pass

Date: 2026-06-06

## Scope

- Promoted `calculation-checks/energy_correlator_sum_rule_checks.py` to an
  extended evidence contract.
- Added a finite-event negative control separating the projected one-variable
  EEC contact atom at \(\zeta=1\) from the bin-resolved diagonal detector
  contact measure.
- Clarified in Volume II Chapter 19b that finite calorimeter-cell response and
  covariance data require contact atoms before the opening-angle pushforward.

## Quality Re-Audit

- Physics depth: this is detector-observable architecture, not a new
  perturbative factorization theorem.  Its value is to prevent global moment
  closure or a scalar endpoint repair from being overread as a measured
  detector-bin prediction.
- Coherence: the inserted prose belongs at the smeared detector-functional
  definition and the measured response/covariance contract, where the
  pushforward from \(S^2\times S^2\) to \(\zeta\) is operational.
- Scope guard: the monograph prose carries only the physics distinction; issue,
  audit, and directive language stays in planning files.

## Verification Target

- Focused Python companion and manifest audit.
- Chapter-level theorem/display/style audits for the touched TeX.
- Full Python calculation-check suite and full monograph build.
