# 2026-06-06 issue #725/#526/#630 track-function contract pass

## Scope

- Promoted `calculation-checks/energy_correlator_track_checks.py` to an
  extended evidence contract and manifest entry.
- Added the finite charged-track measured-test residual
  \(B_{\rm tr}^{(m)}(\mathcal F\,|\,C)\) to Vol II Ch19b.
- Added an exact rational negative control: two probability measures on
  \([0,1]\) match normalization and moments through cubic order, agree on
  low-degree polynomial track-EEC tests, but disagree on a finite high
  charged-track bin and its Bernoulli covariance.

## Quality Re-Audit

- Physics depth: the addition is tied to charged-track collider observables,
  detector bins, response vectors, and covariance comparisons.
- Scope control: no new continuum factorization theorem, universality claim,
  or detector-calibration claim is asserted.
- Monograph hygiene: issue numbers and process language stay in planning
  files; the TeX states only the physics and approximation boundary.
- Anti-wrapper check: the new finite check rejects a concrete false
  interpretation of track functions as low-moment or average-charged-fraction
  replacements.

## Verification Target

- Focused companion run for `energy_correlator_track_checks.py`.
- Evidence-contract audit with the strict backlog reduced by one.
- Ch19b theorem/display-label/style audits.
- Full Python calculation suite and full monograph build before commit.
