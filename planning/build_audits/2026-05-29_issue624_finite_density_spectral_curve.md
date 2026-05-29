# Issue #624: Finite-Density Spectral Curve Opening

## Scope

This pass starts the finite-gap/algebraic-curve development on the
gauge-theory side, directly from finite-density Bethe roots.  It does not yet
claim to be the full classical finite-gap apparatus; it establishes the
root-measure, Cauchy-transform, jump, quasimomentum, and one-cut spectral
curve infrastructure needed for later deeper passes.

## Manuscript Changes

- Added Section `sec:planar-n4-finite-density-spectral-curves` to Volume VII,
  Chapter 13.
- Defined a finite-density Bethe-root curve as the data of:
  - a weak limit of scaled empirical Bethe-root measures;
  - a Cauchy transform on the complement of finitely many analytic arcs;
  - a compact Riemann surface obtained by gluing sheets across the cuts;
  - a meromorphic differential and filling periods.
- Proved the Plemelj jump statement connecting the Cauchy transform to the
  continuum logarithmic Bethe equation and the quasimomentum gluing condition
  `p_+ + p_- = 2 pi n_a`.
- Identified the large-spin one-loop cusp resolvent as the simplest one-cut
  spectral curve:

  `y^2=4z^2-1`,

  with sheet exchange `y -> -y` sending `exp(iG)` to `exp(-iG)`.

## Calculation Check

- Added `check_one_cut_spectral_curve_bookkeeping()` to
  `calculation-checks/planar_n4_integrability_checks.py`.
- The check verifies:
  - the hyperelliptic equation `y^2=4z^2-1`;
  - inversion of `exp(iG)` under sheet exchange;
  - the branch endpoints at `z=+-1/2`.

## Remaining Issue #624 Items

This is the first finite-gap layer, not the endpoint.  Remaining work includes
the full multi-cut algebraic curve, period quantization, relation to the QSC
cut data, Pohlmeyer reduction, and TBA-to-QSC equivalence.
