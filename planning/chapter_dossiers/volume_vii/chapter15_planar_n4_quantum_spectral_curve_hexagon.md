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
- `G, bar G, rho`: one-row T-gauge Cauchy transforms and discontinuity
  density used before passing to the magic-sheet T-hook gauge.
- `hat G, hat T`: magic-sheet continuations through the Zhukovsky cut.
- `x_f(u)`: fermionic-node large-`u` Zhukovsky sheet with
  `x_f(u)=g/u+O(u^-3)`.
- `R_Q(u,v)`: fermionic-node mirror scattering ratio whose large-`u`
  expansion fixes the QSC energy exponent.
- `Q_i`, `omega_ij`: dual QSC variables in the `Qomega` system.
- `Q_{a|i}`: auxiliary Q-system matrix bridging the `Pmu` and `Qomega`
  gauges.
- `eta^{ij}`: fixed antisymmetric tensor used to raise Q-indices.
- `Q(u)`: weak-coupling Baxter polynomial.
- `T(u)`: transfer polynomial in the Baxter limit.
- `f(lambda)`: cusp anomalous dimension scaling function.
- `H`: hexagon form factor.
- `h(u,v)`: elementary scalar hexagon factor for two scalar magnons.
- `S_hex^scal`: scalar Watson factor obtained from `h(u,v)/h(v,u)`.
- `ell_ij`: bridge lengths between three single-trace operators.
- `p(bar alpha)`: total spin-chain momentum of a partition subset moved across
  a hexagon bridge.
- `A_i`: leading QSC asymptotic coefficients.
- `S`: Lorentz spin in the `SL(2)` QSC asymptotic conditions.
- `epsilon`: small-spin QSC amplitude with `epsilon^2=O(S)`.
- `I_J`: modified Bessel function entering the small-spin QSC slope.
- `W_MW(C,theta)`: Maldacena-Wilson line.
- `B(lambda)`: planar Bremsstrahlung function.
- `D(t)`: displacement operator on the line defect.

## Claim Ledger

- Defines the Pmu system, periodicity, cuts, and charge-carrying asymptotics.
- Adds the analytic one-row T-gauge before the `Pmu` system: strip
  analyticity, `T_{0,m}=1`, large-`u` normalization `T_{1,m}->m`, Cauchy
  transforms `G,bar G`, and the one-row ansatz
  `T_{1,m}=m+G^[m]+bar G^[-m]`.
- Proves the Hirota factorization
  `T_{2,m}=(1+G^[m+1]-G^[m-1])(1+bar G^[-m-1]-bar G^[-m+1])`
  and proves the magic-sheet continuation from the Cauchy-transform boundary
  relation `G_+=-bar G_-`:
  `hat T_{1,m}=m+hat G^[m]-hat G^[-m]`,
  `hat T_{2,m}=hat T_{1,1}^[m] hat T_{1,1}^[-m]`.
- Adds a QSC Riemann-Hilbert datum definition: spectral plane, single-cut
  `P_a`, antisymmetric `mu_ab`, fixed `chi`, tilde continuation, regularity,
  large-`u` charge asymptotics, gluing data, and cyclic single-trace
  constraints.
- Adds a two-row T-hook reconstruction datum in the physical/magic gauge:
  shifted Wronskians for `T_{1,m}`, `T_{0,1}=mu_12^2`,
  `T_{3,2}=T_{2,3} mu_12`, central-node regularity, and the nondegenerate
  Wronskian condition.
- Proves the local T-hook algebra behind the `Pmu` bridge: central-cut
  regularity of `T_{2,1}` gives
  `tilde mu_12-mu_12=P_1 tilde P_2-P_2 tilde P_1`, the central Hirota square
  gives `T_{1,0}=mu_12 tilde mu_12`, and hence
  `Y_{1,1}Y_{2,2}=tilde mu_12/mu_12`.
- Adds a T-hook-to-`Pmu` charge-bridge assumption for the fermionic nodes
  `Y_{1,1} Y_{2,2}`, now narrowed to the mirror-TBA large-`u` energy
  normalization after the local bridge algebra has been proved.
- Adds and proves the local large-`u` expansion of the fermionic-node
  scattering ratio
  `R_Q=((x_f-a)/(x_f-b))*((x_f^-1-b)/(x_f^-1-a))` on the small-`x`
  sheet: its constant term is `-tilde E_Q`, its `u^-1` coefficient is
  `-tilde p_Q`, and inverse mirror continuation gives
  `i p + i E/u` for a physical root.  This pins the sign in the
  `Y_{1,1}Y_{2,2}` energy normalization to the stringbook mirror convention.
- Proves from the `Pmu` discontinuity and pseudo-periodicity that
  `Y_{1,1}Y_{2,2}=mu_12(u+i)/mu_12(u)`, and derives
  `mu_12(u) ~ u^(Delta-J)` when the large-`u` behavior is power-like.
- Proves the remaining `mu_ab` large-`u` powers from the `Pmu` sheet
  equation and the `SL(2)` `P_a` powers, under an explicit common sheet
  exponent and no-accidental-cancellation assumption.  The proof also checks
  that the powers are homogeneous in the leading monodromy-recursion system
  used for the characteristic determinant.
- Derives the large-`u` QSC characteristic determinant from the six leading
  `mu_ab` monodromy-recursion equations, including the `mu_23` exponent and
  the determinant factorization `det M_alpha = alpha^2 Phi(alpha)`.  The
  physical assignment of the nonzero roots `alpha=Delta` and `alpha=S-1`
  remains an explicit QSC gluing/representation-theory input.
- Proves the displayed coefficient products `A_1A_4` and `A_2A_3` by solving
  the two root equations `Phi(Delta)=Phi(S-1)=0`.  This records the
  representation-theory status of the spin-shadow root instead of hiding it
  in the formula.
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
- Adds the dual `Qomega` system, defines the `eta^{ij}` raising tensor and
  dual Pfaffian normalization, and explains the analytic-gauge status of
  short and long cuts.
- Proves the local dual `Qomega` transport rule: the rank-two update
  `omega -> omega + Q wedge tilde Q` preserves `Pf omega` when
  `Q_i Q^i=0`, and pseudo-periodicity gives
  `omega_ij(u+i)=omega_ij+Q_i omega_jk Q^k-Q_j omega_ik Q^k`.  The text
  marks this as local cut-gauge algebra, not as a proof of the global
  `Qomega` Riemann-Hilbert problem.
- Adds the local `P-Q` bridge before the weak-coupling limit: the rank-one
  finite-difference relation `Q_{a|i}^+-Q_{a|i}^-=P_a Q_i`, the contraction
  formulae `Q_i=-P^a Q_{a|i}^-`, `P_a=-Q^i Q_{a|i}^-`, and the null
  contractions `P_a P^a=Q_i Q^i=0`.
- Proves that the `P-Q` contraction formulae are shift-independent and that
  the rank-one update preserves `det Q_{a|i}`.  This records the local
  algebraic reason for the unimodular `Q_{a|i}` gauge while keeping global
  cut/gluing existence as a QSC framework input.
- Derives the weak-QSC `mu_12` pre-Baxter finite-difference equation by
  eliminating `mu_24` from the leading `(1,2)` and `(2,4)` components of the
  Pmu monodromy recursion, explicitly using `P^1=-P_4`, `P^4=P_1`, and the
  suppression of `P_2 P_3` terms.
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
- Adds a collapsed-cut digamma-package lemma proving the pole locations,
  residues at `u=+-i(n+1/2)`, endpoint residue signs at `+-i/2`, and the
  `2 i r_0 log(u)/Q(i/2)` large-`u` coefficient used in the weak-QSC
  one-loop dimension extraction.
- Adds a half-integer digamma-primitive lemma proving the one-step shift
  defects of
  `psi(1/2-iu)+psi(1/2+iu)`, the resulting central second-difference
  identity, and the precise `i`-periodic ambiguity statement used to replace
  the earlier compressed "Baxter equation up to regular terms" step.
- Adds the twist-two spin-two Konishi Baxter polynomial example.
- Proves the full twist-two Baxter-polynomial family
  `Q_S(u) = 3F2(-S,S+1,1/2-iu;1,1;1)`, its finite-difference equation,
  endpoint/cyclicity values, harmonic-number logarithmic derivative, and the
  one-loop dimension `Delta_{J=2,S}=2+S+8g^2 H_S+O(g^4)` for physical even
  spin.  The proof uses a finite summand-level telescoping certificate and
  finite Chu--Vandermonde/Christoffel--Darboux identities.
- Records the cusp anomalous dimension and Konishi as benchmark outputs.
- Expands the small-spin QSC block into a proved slope proposition: derives
  the Laurent identity
  `sinh(2 pi u)=sum_n I_{2n+1}(4 pi g) x^{2n+1}`, extracts the leading
  `A_1,...,A_4` coefficients from the regularity split, uses the linearized
  QSC charge equations, and applies the Bessel recurrence to obtain
  `(Delta-J-S)/S = 4 pi g I_{J+1}(4 pi g)/(J I_J(4 pi g))+O(S)`.
  The analytic continuation from small spin to integer-spin Konishi remains
  explicitly marked as a QSC input.
- Defines the hexagon partition of planar three-point functions and states the
  proof boundary for deriving it from the gauge-theory path integral.
- Proves the planar pair-of-pants bridge-length formula
  `ell_12=(L_1+L_2-L_3)/2`, etc., from the three length-balance equations, and
  records the parity/triangle-inequality criterion for a nonnegative integer
  planar skeleton.
- Derives the bridge translation phase
  `prod_{u_j in bar alpha} exp(i p_j ell)=exp(i p(bar alpha) ell)` used in
  the schematic asymptotic hexagon partition sum.
- Adds the elementary scalar hexagon factor `h(u,v)` and its crossing-path
  caveat.
- Proves the local scalar Watson identity
  `h(u_1,u_2)/h(u_2,u_1)=S_hex^scal(1,2)`, including the
  `1/sigma_12^2` dressing orientation and the weak compact one-loop limit
  `(u_1-u_2+i)/(u_1-u_2-i)`.  The text warns that this should not be
  identified with the rank-one `SL(2)` ABA phase without transporting the
  vacuum, edge-crossing path, and scalar-factor split.
- Adds Maldacena-Wilson line, cusp, displacement-operator, radiated-power, and
  planar Bremsstrahlung function material with localization/QSC status labels.
- Derives the coefficient relation `C_D=12 B(lambda)` from the stated
  straight-line defect shape-variation Ward identity: the finite part
  transform of the displacement two-point kernel gives
  `pi C_D |omega|^3/6`, and the small-cusp profile
  `X(t)=varphi t Theta(t)` produces the logarithmic coefficient
  `C_D varphi^2/12`.

## Figure Ledger

No figure is included in this pass.  Future figures should show the QSC cut
structure and the pair-of-pants-to-hexagons cut.

## Calculation Checks

- The Baxter-limit algebra is paired with the finite Bethe-root checks in
  `calculation-checks/planar_n4_integrability_checks.py`, including the
  Konishi Baxter-polynomial orientation that gives the one-loop `SL(2)`
  Bethe phase `(u_j-u_k-i)/(u_j-u_k+i)`.
- The same script now checks the explicit Konishi Baxter polynomial and the
  Pmu Pfaffian rank-two update.
- The same script checks the algebraic `Y_{1,1}Y_{2,2}` bridge ratio and the
  large-`u` exponent extraction for `mu_12(u+i)/mu_12(u)`.
- The same script checks the one-row T-gauge Hirota factorization and the
  magic-sheet Cauchy-continuation sign behind the two-row Wronskian gauge,
  including a finite Cauchy-transform model that detects the wrong lower-sheet
  sign and verifies the `hat T_{2,m}=hat T_{1,1}^[m]hat T_{1,1}^[-m]`
  product.
- The same script checks the two-row T-hook Wronskian Pluecker identity,
  central-cut regularity of `T_{2,1}`, the `mu_12` discontinuity sign, and
  `T_{1,0}=mu_12 tilde mu_12`.
- The same script checks the fermionic-node ratio expansion: mirror sheet
  placement, mirror energy logarithm, mirror momentum convention, shortening,
  constant term `exp(-tilde E_Q)`, `u^-1` coefficient `-tilde p_Q`, and the
  inverse mirror continuation to `i p+i E/u`.
- The same script checks the QSC large-`u` characteristic determinant
  `det M_alpha = alpha^2 Phi(alpha)` for the six leading `mu_ab` equations,
  then checks the displayed `A_1A_4` and `A_2A_3` products, including the
  dimension root, the spin-shadow root `S-1`, the intermediate linear
  relation, and sensitivity to an overall sign flip.
- The same script checks the QSC large-`u` `mu_ab` power balance exactly:
  row homogeneity in `tilde P_a=mu_ab P^b`, the universal monodromy exponent
  `p_a+p_b+alpha=e_ab-1`, and term-by-term homogeneity of the retained
  monodromy-recursion terms.
- The same script checks the collapsed-cut digamma package for twist-two
  spins `S=2,4,6`: residues at `u=+-i/2` and the large-`u` logarithmic
  coefficient, using a local recurrence/Stirling implementation of
  `psi=Gamma'/Gamma`.
- The same script checks the half-integer digamma primitive shift defects,
  the central second-difference identity, and the induced shift defects for
  the QSC singular quotient `R_sing/Q` for twist-two spins `S=2,4,6`.
- The same script checks the sign convention in the `mu(u+i)` monodromy
  recursion against the rank-two discontinuity update and verifies
  antisymmetry of the shifted matrix.
- The same script checks the local `P-Q` bridge exactly over rational samples:
  plus/minus shift independence of the `P` and `Q` contractions, null
  contractions from antisymmetric raising, and determinant preservation under
  the rank-one update.
- The same script checks the dual `Qomega` transport algebra on exact and
  complex antisymmetric samples: `Q_i Q^i=0`, Pfaffian preservation,
  equality of the one-step monodromy recursion with the rank-two
  discontinuity update, antisymmetry of the shifted matrix, and sensitivity
  to the overall transport sign.
- The same script checks the weak-QSC `mu_12`/`mu_24` elimination algebra:
  the reconstructed `mu_24` recursion, the pre-Baxter difference equation,
  and finiteness of the weak transfer coefficient in sample twists.
- The same script checks the twist-two QSC Baxter-polynomial family for
  spins `S=1,...,8`: finite-difference equation, endpoint sign/cyclicity
  pattern, and the logarithmic-derivative energy identity `4 H_S`.
- The same script now also checks the twist-two finite-sum derivation
  exactly: endpoint values, endpoint derivatives, and the telescoping
  certificate for the Baxter equation over rational `z` test points.
- The same script checks the small-spin QSC Bessel slope by exact rational
  series: the recurrence `I_{J-1}-I_{J+1}=2J I_J/z` and the first two
  coefficients of `z I_{J+1}(z)/(J I_J(z))` for twists `J=1,...,6`.
- The same script checks the hexagon bridge-length bookkeeping: length-balance
  equations, parity/triangle existence criterion, bridge partition phase, and
  full-state cyclic translation phase.
- The same script checks the hexagon scalar Watson factor exactly on rational
  samples and verifies its weak compact one-loop orientation against the
  reciprocal `SL(2)` phase.
- The same script checks the displacement-kernel coefficient behind
  `C_D=12 B`: Taylor factor, finite-part Fourier coefficient, Fourier
  measure, and the two frequency half-lines give the exact logarithmic
  coefficient `1/12`.
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
