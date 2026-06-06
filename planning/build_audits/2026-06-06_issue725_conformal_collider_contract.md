# 2026-06-06 Issue #725 Conformal-Collider Contract Pass

## Scope

- Targeted `calculation-checks/conformal_collider_checks.py`, the Volume III
  Chapter 10 ANEC/conformal-collider companion.
- Promoted the companion to an extended evidence contract in
  `calculation-checks/evidence_contracts.json`.
- Kept reader-facing TeX focused on physics exposition: the finite
  Hofman--Maldacena diagonalization starts only after ANEC detector positivity
  and the stress-tensor one-point normal form have been supplied.

## Substance Added

- Added an evidence contract spelling out target claims, independent
  construction, imported physics assumptions, negative controls, scope
  boundary, derivation/verification routes, conventions, domain assumptions,
  and remaining conditional inputs.
- Added finite adversarial tests showing that:
  - the fixed total-energy normalization checks only the zeroth angular moment;
  - omitting any one of the helicity-2, helicity-1, or helicity-0 inequalities
    can leave a normalized stress-tensor profile with negative detector flux;
  - a right-cut modular monotonicity check without the complementary cut can be
    compatible with a negative full null integral.
- Updated the chapter prose to separate the analytic ANEC/detector bridge and
  Wightman/Ward normal-form inputs from the finite helicity diagonalization.

## Quality Re-Audit Notes

- This is infrastructure rather than a new proof of ANEC or the light-ray
  operator domain theorem.
- The physics depth comes from clarifying the chain of implications:
  Lorentzian positivity theorem and detector-measure construction first,
  stress-tensor flux normal form second, finite helicity positivity third.
- The finite companion now blocks two self-confirming shortcuts that could
  make a collider positivity claim look stronger than the algebra establishes.
