# 2026-06-01 Soft-drop mass radiator pass

## Scope

Advanced GitHub issue #526 by adding a measured-observable resummation
calibration to Volume II, Chapter 19b.

## Manuscript changes

- Added a fixed-coupling soft-collinear groomed jet-mass radiator after the
  measured-mMDT functional discussion.
- Introduced the logarithmic variables
  \(t=\log(1/\theta^2)\), \(u=\log(1/z)\),
  \(L_\rho=\log(1/\rho)\), and \(L_z=\log(1/z_{\rm cut})\).
- Derived the veto-region area
  \(A_\beta=\int du\,dt\,1_{u+t<L_\rho}1_{u<L_z+\beta t/2}\).
- Displayed the closed-form area below the grooming transition and the mMDT
  single-log limit \(A_0=L_\rho L_z-L_z^2/2\).
- Kept the status as a `controlledapproximation`: fixed coupling,
  one-emission soft-collinear measure, no finite splitting functions,
  running coupling, recoil, non-global effects, clustering logarithms, or
  hadronization.

## Calculation companion

Extended `calculation-checks/soft_drop_irc_checks.py` with exact rational
checks of:

- the ungroomed triangular area when grooming is inactive;
- the mMDT single-log area and its linear growth in \(L_\rho\);
- the positive-\(\beta\) closed-form area for a sample point;
- continuity at the grooming transition.

## Status

This is a concrete #526 improvement, not a closure.  A complete physical
soft-drop mass prediction still requires the renormalized factorization
datum, running-coupling resummation, finite splitting functions, matching,
non-global/clustering effects when present, and a nonperturbative
hadronization coordinate.
