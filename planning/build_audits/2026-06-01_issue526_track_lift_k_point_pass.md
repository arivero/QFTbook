# Track-Lift K-Point Pass

Date: 2026-06-01.

Scope:

- Continued GitHub issue #526 without closing it.
- Expanded the track-function part of Volume II Chapter 19b from the displayed
  two-point lift to the exact finite \(k\)-point lift of an energy-measure
  polynomial.
- Added the map formula
  \[
    \sum_{\alpha:\{1,\ldots,k\}\to\{1,\ldots,n\}}
    \prod_r E_{\alpha(r)}
    f(y_{\alpha(1)},\ldots,y_{\alpha(k)})
    \prod_{a\in{\rm im}\alpha}m_{i_a}^{(|\alpha^{-1}(a)|)}.
  \]
- Added the three-point decomposition into all-distinct, partial-diagonal,
  and full-diagonal terms, making explicit where second and third track
  moments enter.

Calculation checks:

- Extended `calculation-checks/track_observable_lift_checks.py` with exact
  rational enumeration of a nontrivial three-point track lift.
- The check verifies the general map formula against direct enumeration and
  confirms that replacing every track variable by its first moment gives the
  wrong lifted observable when diagonal terms are present.

Status:

- This pass closes a finite-algebra gap in the track-based substructure layer:
  higher track moments are now part of the displayed observable definition,
  not an afterthought.  The broader modern jet-substructure issue remains
  open for additional measured-observable factorization examples, continuum
  factorization estimates, and boosted/electroweak regimes beyond the current
  scalar Sudakov chart.
