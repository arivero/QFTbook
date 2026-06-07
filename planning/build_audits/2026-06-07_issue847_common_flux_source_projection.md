# Issue #847 Common-Flux Source-Projection Repair

Date: 2026-06-07
Target: `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`

## Scope

This pass addresses the remaining Hori--Vafa common-flux/operator-map concern:
the original GLSM has one compact gauge-flux sector, while the index `i` labels
a source or dual disorder projection.  The product of projected mirror
coefficients is a mirror-coordinate assembly, not automatically the physical
amplitude of one original-theory gauge-flux event.

## Repairs

- Added an explicit boundary that the displayed product formulae are ordinary
  `U(1)^s` formulae.  For `U(1)^s/Gamma`, one must propagate the cocharacter
  flux lattice, theta character, allowed dual characters, and residual mirror
  orbifold.
- Added the finite-regulator source-projection interface
  `hat c_i^orig = Pi_i(A_{1,Lambda})`, with physical observable amplitudes
  written as separate projections `Pi_O(A_{1,Lambda})`.
- Clarified that `prod_i c_i^{Q_i^a}` and
  `exp(T_a) prod_i c_i^{Q_i^a}` are normalized mirror-coordinate assemblies
  until an observable-comparison or source-factorization theorem identifies
  them with a direct original-sector amplitude and supplies residual bounds.
- Added explicit warnings at the all-rank FI-coordinate proposition and the
  `P^{N-1}` residue setup that `q_phys` is a mirror/FI coordinate, not by
  definition a direct common original-flux amplitude.

## Companion Evidence

`calculation-checks/susy_2d_lg_glsm_checks.py` now computes projected
coefficients and a direct common observable amplitude from separate finite
linear functionals on one common source functional.  It rejects:

- treating the projected product as an automatic common amplitude;
- arbitrary projected coefficients even after an assembly map has been fixed;
- flavor-labelled flux sectors under equal-charge relabelling;
- reusing the ordinary `U(1)` flux/product formula on a quotient flux lattice.

The finite cell is still a gate, not a proof of the continuum operator map or a
source-factorization theorem.

## Residual Debt

Still open: construct the actual continuum original-to-dual operator map,
derive source-factorization or observable-comparison theorems for the relevant
protected observables, and propagate nontrivial global-form data through the
full mirror construction rather than restricting to the covering torus.
