# Chapter 15: Quantum Spectral Curve and Hexagon Form Factors

## Source Position

This chapter follows mirror TBA and records the compressed QSC formulation of
the spectral problem, together with the separate hexagon framework for
three-point functions.

## Notation Inventory

- `P_a`: QSC P-functions.
- `mu_ab`: antisymmetric QSC matrix.
- `tilde`: analytic continuation through the short cut.
- `chi^{ab}`: fixed antisymmetric tensor used to raise P-indices.
- `Q(u)`: weak-coupling Baxter polynomial.
- `T(u)`: transfer polynomial in the Baxter limit.
- `f(lambda)`: cusp anomalous dimension scaling function.
- `H`: hexagon form factor.
- `ell_ij`: bridge lengths between three single-trace operators.
- `A_i`: leading QSC asymptotic coefficients.
- `S`: Lorentz spin in the `SL(2)` QSC asymptotic conditions.
- `W_MW(C,theta)`: Maldacena-Wilson line.
- `B(lambda)`: planar Bremsstrahlung function.
- `D(t)`: displacement operator on the line defect.

## Claim Ledger

- Defines the Pmu system, periodicity, cuts, and charge-carrying asymptotics.
- Adds explicit `SL(2)` QSC large-`u` asymptotics and algebraic coefficient
  constraints.
- States the QSC spectral claim as a quoted theorem inside the planar
  integrability framework.
- Derives the one-loop Baxter equation from the weak-coupling QSC
  degeneration under explicit assumptions.
- Records the cusp anomalous dimension and Konishi as benchmark outputs, and
  adds the small-spin QSC expansion through the Bessel-ratio formula.
- Defines the hexagon partition of planar three-point functions and states the
  proof boundary for deriving it from the gauge-theory path integral.
- Adds Maldacena-Wilson line, cusp, displacement-operator, radiated-power, and
  planar Bremsstrahlung function material with localization/QSC status labels.

## Figure Ledger

No figure is included in this pass.  Future figures should show the QSC cut
structure and the pair-of-pants-to-hexagons cut.

## Calculation Checks

- The Baxter-limit algebra is paired with the finite Bethe-root checks in
  `calculation-checks/planar_n4_integrability_checks.py`.
- The Bremsstrahlung weak-series coefficient is checked in
  `calculation-checks/planar_n4_integrability_checks.py`.
