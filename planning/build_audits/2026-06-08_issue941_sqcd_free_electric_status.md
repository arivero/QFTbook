# Issue #941 SQCD Free-Electric Status Audit

## Scope

- Volume VII, Chapter 6 SQCD infrared-comparison hypotheses.
- Central SQCD Seiberg-duality conjecture and free-electric continuation.
- SQCD infrared range synthesis.
- `calculation-checks/susy_n1_sqcd_duality_checks.py` and inventory entry.
- Volume VII Chapter 6 dossier.

## Physics Repair

- Restricted the central SQCD Seiberg-duality conjecture to the
  electric-asymptotically-free range `N_c+2 <= N_f < 3N_c`.
- Added a separate free-electric continuation for `N_f >= 3N_c`, with
  `N_f=3N_c` as a Gaussian edge and strict `N_f>3N_c` requiring one of three
  declared electric-side statuses: finite-cutoff EFT, specified UV completion,
  or emergent infrared variables defined through the magnetic continuum
  theory.
- Declared the limit order for the finite-cutoff electric formulation:
  thermodynamic limit at fixed electric cutoff, then the infrared limit with
  `p/Lambda_el -> 0`, and only then any UV-completion-independent statement
  for protected observables.
- Kept NSVZ, anomaly, charge, rank, and deformation arithmetic as evidence
  ledgers while restricting fixed-point and superconformal-dimension
  interpretation to the interacting conformal window.
- Reconciled the phase synthesis with separate free-magnetic, lower-edge,
  interacting-conformal, Gaussian-edge, and strict free-electric entries.

## Regression Guard

- `susy_n1_sqcd_duality_checks.py` now has a range-status classifier.
- The free-electric negative control samples `N_f=3N_c+1`: rank,
  baryon-charge, and local anomaly arithmetic still pass, but the standard
  continuum-pair statement and fixed-point-dimension tests are rejected by
  the range status.

## Re-Audit Notes

- The added mathematics is only range and regulator bookkeeping needed to
  make the physics claim honest.
- The repair avoids turning algebraic identities into a continuum-definition
  theorem.
- Process notes remain in planning files, not in monograph TeX.
