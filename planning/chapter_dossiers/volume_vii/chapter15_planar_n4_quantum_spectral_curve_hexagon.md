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
- `Q_i`, `omega_ij`: dual QSC variables in the `Qomega` system.
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
- Adds a QSC Riemann-Hilbert datum definition: spectral plane, single-cut
  `P_a`, antisymmetric `mu_ab`, fixed `chi`, tilde continuation, regularity,
  large-`u` charge asymptotics, gluing data, and cyclic single-trace
  constraints.
- Adds the Pfaffian normalization and proves its preservation under the
  rank-two Pmu discontinuity update.
- Proves the one-step `mu(u+i)` monodromy recursion from pseudo-periodicity,
  the discontinuity equation, and `tilde P_a = mu_ab P^b`.  The proof also
  states the boundary: the recursion is algebraic and does not itself prove
  physical existence/uniqueness.
- Adds explicit `SL(2)` QSC large-`u` asymptotics and algebraic coefficient
  constraints.
- States the QSC spectral claim as a quoted theorem inside the planar
  integrability framework.
- Adds a status boundary after the quoted theorem separating local derivations
  in the chapter from QSC framework inputs: existence of single-short-cut
  functions, the normalized discontinuity coefficient, physical gluing, and
  equivalence to the exact planar gauge-theory spectrum.
- Adds the dual `Qomega` system and explains the analytic-gauge status of
  short and long cuts.
- Derives the one-loop Baxter equation from the weak-coupling QSC
  degeneration under explicit assumptions.
- Adds a weak-coupling `SL(2)` QSC regularity assumption specifying the
  leading `P_1`, `P_2 P_3`, polynomial `P_4/P_1`, polynomial `Q`, and
  collapsed-cut singularity data of `mu_12`.
- Proves the one-loop dimension extraction formula from the weak QSC:
  the singular part of the `g^2` correction to `mu_12` is fixed by the
  collapsed short cuts, has the displayed digamma form, and its large-`u`
  logarithm gives
  `Delta = J + S + 2 i g^2 d_u log(Q^+/Q^-)|_{u=0} + O(g^4)`.
- Adds the twist-two spin-two Konishi Baxter polynomial example.
- Adds the full twist-two Baxter-polynomial family
  `Q_S(u) = 3F2(-S,S+1,1/2-iu;1,1;1)`, its finite-difference equation,
  endpoint/cyclicity values, and the one-loop dimension
  `Delta_{J=2,S}=2+S+8g^2 H_S+O(g^4)` for physical even spin.
- Records the cusp anomalous dimension and Konishi as benchmark outputs, and
  adds the small-spin QSC expansion through the Bessel-ratio formula.
- Defines the hexagon partition of planar three-point functions and states the
  proof boundary for deriving it from the gauge-theory path integral.
- Adds the elementary scalar hexagon factor `h(u,v)` and its crossing-path
  caveat.
- Adds Maldacena-Wilson line, cusp, displacement-operator, radiated-power, and
  planar Bremsstrahlung function material with localization/QSC status labels.

## Figure Ledger

No figure is included in this pass.  Future figures should show the QSC cut
structure and the pair-of-pants-to-hexagons cut.

## Calculation Checks

- The Baxter-limit algebra is paired with the finite Bethe-root checks in
  `calculation-checks/planar_n4_integrability_checks.py`.
- The same script now checks the explicit Konishi Baxter polynomial and the
  Pmu Pfaffian rank-two update.
- The same script checks the sign convention in the `mu(u+i)` monodromy
  recursion against the rank-two discontinuity update and verifies
  antisymmetry of the shifted matrix.
- The same script checks the twist-two QSC Baxter-polynomial family for
  spins `S=1,...,8`: finite-difference equation, endpoint sign/cyclicity
  pattern, and the logarithmic-derivative energy identity `4 H_S`.
- The Bremsstrahlung weak-series coefficients through four displayed orders
  are checked in
  `calculation-checks/planar_n4_integrability_checks.py`.

## External References Used In Current Pass

- Stringbook source:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, around
  the `Pmu` asymptotic conditions and weak-coupling QSC block.
- Downloaded local study copy:
  `references/planar_n4_integrability/qsc/1305.1939_src/PRL_paper.tex`.
  It was used to check the original compact `Pmu` weak-coupling argument and
  regularity assumptions.  The monograph text expands the argument rather
  than citing it as authority.
