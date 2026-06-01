# EEC endpoint resolution shift pass

Date: 2026-06-01.

Issue context: GitHub #519, energy-correlator light-ray OPE and endpoint
contact bookkeeping.

## Scope

Volume II, Chapter 19 already defined the small-angle EEC endpoint plus
distribution and the finite \(\delta(\rho)\) contact coordinate.  This pass
adds the missing resolution-scale identity: changing the endpoint boundary is
itself a distributional operation that moves an ordinary separated-angle
annulus into a compensating coincident-detector contact coordinate.

## Manuscript change

For \(0<\rho_a<\rho_b\), the chapter now defines
\[
  D_{\rho_*}=\left[\frac{\Theta(\rho_*-\rho)}{\rho}\right]_+
\]
and derives
\[
  D_{\rho_b}
  =
  D_{\rho_a}
  +
  \frac{\mathbf 1_{\rho_a<\rho<\rho_b}}{\rho}
  -
  \log\frac{\rho_b}{\rho_a}\delta(\rho).
\]
The identity makes precise that endpoint contact conventions are not optional
language: a separated angular annulus and a compensating delta coordinate must
be transformed together for constant tests and the EEC moment ledger to stay
unchanged.

## Calculation check

`calculation-checks/energy_correlator_light_ray_ope_checks.py` now verifies
the identity on polynomial endpoint tests by exact rational arithmetic.  The
nonconstant powers check the ordinary annular integral, and the constant term
checks coefficient-wise cancellation against the logarithmic contact shift.

This narrows #519.  It does not close the issue: the complete all-order
renormalized light-ray OPE/mixing theorem and higher-loop/frontier
energy-correlator program remain open.
