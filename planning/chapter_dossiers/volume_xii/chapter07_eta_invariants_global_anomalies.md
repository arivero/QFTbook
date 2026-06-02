# Chapter 07: Eta Invariants and Global Anomalies

## Source Position

Volume XII has introduced background gauge fields, index theory, anomaly
polynomials, and determinant lines.  This chapter now develops the holonomy
side of the same structure: eta invariants, APS boundary terms, determinant
and Pfaffian-line transport, Dai--Freed inflow, and the Witten \(SU(2)\)
global anomaly as an explicit mod-two-index example.

## Notation Inventory

- `Y`: closed odd-dimensional spin manifold; `X`: compact even-dimensional
  spin manifold with boundary.
- `B_Y`: self-adjoint odd-dimensional Dirac operator.
- `eta_B(s)`, `h(B)`, `xi(B)`: eta function, kernel dimension, and reduced
  eta invariant.
- `D_X^{+,APS}`: chiral Dirac operator with APS spectral boundary condition.
- `P_{\geq0}`: APS projection onto nonnegative boundary spectrum.
- `Det D`, `Pf D`: determinant and Pfaffian lines over background-field space.
- `gamma`, `Y_gamma`: closed loop of backgrounds and its mapping torus.
- `Ind_2(B_Y)`: mod-two index of the real/pseudoreal Dirac operator.
- `R_j`, `n=2j`, `T_Delta(R_j)`: \(SU(2)\) isospin representation, doubled
  isospin, and trace-delta Dynkin index.

## Claim Ledger

- Defines the eta function and reduced eta invariant for self-adjoint
  Dirac-type operators, including the integer jump at zero crossings.
- States the APS formula as an external global-analysis theorem with explicit
  product-collar and boundary-projection conventions, and now explains the
  Fredholm boundary-condition mechanism, the heat-kernel/local-density input,
  and the eta boundary term used by the QFT anomaly argument.
- Adds the inward half-cylinder mode calculation for the APS spectral
  projection: with \(u\in(-\infty,0]\),
  \(f_\lambda(u)=e^{-\lambda u}f_\lambda(0)\) is square-integrable exactly for
  \(\lambda<0\), zero modes are excluded, and opposite boundary orientation
  replaces \(B\) by \(-B\).
- Proves the cylinder variation formula for \(\xi\) modulo integers from the
  APS theorem, including the orientation-reversal bookkeeping
  \(\xi(-B)=-\xi(B)+h(B)\).
- Records the exact APS cylinder identity
  \(\operatorname{Ind}=I_X-\xi(B_1)+\xi(B_0)-h(B_0)\), so the endpoint-kernel
  convention and the sign relating simple-crossing spectral flow to the
  cylinder index are explicit before the phase is reduced modulo
  \(\mathbb Z\).
- Defines determinant-line fibers and states the Bismut--Freed holonomy
  theorem for mapping tori, with an expanded mechanism explaining local
  zeta-determinant charts, the Bismut--Freed connection, curvature as the
  family index density, and holonomy as the adiabatic eta invariant.
- Adds the elementary Cech-de Rham line-bundle bookkeeping behind
  Bismut--Freed holonomy: local frames \(e_i\), normalized connection forms
  \(a_i\), transition functions \(f_{ij}\), the overlap law
  \(a_j=a_i-df_{ij}\), the arc-plus-vertex expression for loop holonomy, and
  the telescoping invariance under local frame changes.
- Makes the Quillen determinant-line spectral-cut chart construction explicit:
  the low-mode line \(L_a(b)\), the finite window
  \(E_{[a,c)}^\pm(b)\), the determinant transition element
  \(\det D^+_{[a,c)}\), and its cocycle identity under a refinement of cuts.
- Connects reduced-eta integer jumps at eigenvalue crossings to the
  determinant-line spectral-cut transition rule, explaining that local
  curvature, spectral-flow jumps, and mapping-torus eta phases are curvature,
  transition, and holonomy data of the same anomaly line.
- Explains finite gauge-transformation phases as determinant-line holonomies,
  as a direct application of the quoted Bismut--Freed holonomy theorem to the
  mapping torus of the gauge transformation.
- Makes the descent criterion over the quotient background groupoid explicit:
  determinant-line transport is a groupoid `1`-cocycle, changes of local
  trivialization shift it by a coboundary, based-loop holonomies are
  invariant, and a quotient-valued partition function exists only after an
  equivariant trivialization of the anomaly line.
- Adds the dual-line cancellation criterion: the dual anomaly line has the
  inverse groupoid cocycle, `L \otimes L^\vee` is trivialized by evaluation,
  and local curvature cancellation is weaker than global cancellation because
  a flat anomaly line can still have nontrivial based-loop holonomy.
- Defines the Pfaffian mod-two index and proves its deformation invariance in
  the real skew setting.
- Inserts a finite skew-block model of the Pfaffian line:
  \(\operatorname{pf}(a\,e^1\wedge e^2)=a\), direct sums multiply
  Pfaffians, and a sign holonomy is the parity of block sign crossings.
  This makes the real-line orientation mechanism visible before the
  infinite-dimensional mod-two-index theorem is used.
- States the mod-two index theorem for the Witten \(SU(2)\) mapping torus and
  derives the trace-delta Dynkin index for spin-\(j\) representations from
  the \(J_3\)-weight sum, then derives the parity criterion
  \(2j\equiv1\pmod4\) using exact binomial parity, while explicitly separating
  the five-dimensional real-index theorem from the subsequent
  trace-convention arithmetic.
- Makes the Witten mapping-torus clutching datum explicit: the bundle
  \(P_g=([0,1]\times S^4\times SU(2))/((1,x,u)\sim(0,x,g(x)u))\), its
  associated representation bundle, homotopy invariance by a six-dimensional
  clutching bordism, and additivity under concatenation of mapping tori.
- Explains Dai--Freed inflow as a boundary-line trivialization and derives the
  descent limit for contractible loops by combining Bismut--Freed curvature,
  ordinary Stokes on a background-space disk, and Chern--Weil descent.
- Expands the Dai--Freed gluing mechanism: for a closed odd manifold that
  bounds, APS identifies the eta phase with the exponentiated local index
  integral modulo integers; for an odd manifold with boundary, the
  Dai--Freed object is a vector in the inverse boundary anomaly line, and
  pairing two such vectors gives the closed phase of the glued odd manifold.
- Adds an explicit theorem-boundary paragraph separating the pure
  global-analysis inputs (APS Fredholm/heat-kernel theorem,
  Bismut--Freed determinant-line holonomy, Dai--Freed boundary-line gluing,
  and the real mod-two index theorem) from the QFT-facing consequences
  derived in the chapter: cylinder bookkeeping, quotient-groupoid descent,
  local descent, inflow cancellation, trace-delta parity arithmetic, and
  anomaly-line tensor-product cancellation.
- Records the interacting-QFT anomaly-line construction as an open problem.

## Calculation Ledger

- `calculation-checks/eta_global_anomaly_checks.py` checks the APS
  orientation bookkeeping, the exact APS cylinder endpoint-kernel identity,
  the sign convention relating simple-crossing spectral flow to the APS
  cylinder index, the inward half-cylinder APS mode-selection sign, the first
  \(SU(2)\) trace-delta Dynkin indices, Witten
  parity criterion, Pfaffian-sign multiplicativity, mapping-torus
  \(\mathbb Z_2\)-character bookkeeping, cubic-weight-sum cancellation, the
  finite skew-block Pfaffian orientation model, cylinder congruence
  arithmetic, action-groupoid anomaly cocycle/coboundary
  identities, based-loop holonomy invariance, the stabilizer-character
  obstruction to descent, dual anomaly-line cancellation, nontrivial flat
  stabilizer holonomy before cancellation, and the Quillen spectral-cut
  transition cocycle for determinant-line charts, the reduced-eta integer
  jump at a one-mode crossing, the finite \(U(1)\)-phase algebra behind
  Dai--Freed gluing, and a finite cochain Stokes model for the
  contractible-loop curvature-to-descent step.
- The same script now checks the Cech-de Rham local connection/transition
  algebra for determinant-line holonomy: \(a_j=a_i-df_{ij}\) on overlaps and
  invariance of the closed-loop exponent under frame changes
  \(e_i\mapsto e^{2\pi i h_i}e_i\).
- Related scripts: `calculation-checks/background_index_theory_checks.py`,
  `calculation-checks/anomaly_polynomial_descent_checks.py`, and
  `calculation-checks/inflow_anomaly_line_checks.py`.

## Figure Ledger

- `fig:eta-cylinder-mapping-torus` shows the APS cylinder and the mapping
  torus used to pass from local eta variation to determinant-line holonomy.

## Residual Work

- The quoted APS, Bismut--Freed, and mod-two-index theorems are mathematical
  inputs.  A later appendix could develop their proofs in the level of
  global analysis and KO-theory needed by the monograph.
- A later interacting-anomaly chapter should replace the free-fermion
  determinant-line model by a general construction of anomaly lines for
  interacting QFTs.
- 2026-05-29 anti-wrapper pass: demoted the local-descent limit from
  proposition form to derivation prose.  The result is an APS-transgression
  consequence inside the Dai--Freed construction; theorem-family status
  remains with the quoted APS/Bismut--Freed/global-index inputs.
- 2026-05-29 anti-wrapper pass: demoted finite gauge transformation as
  determinant-line transport from proposition/proof form to application prose,
  because the theorem-level input is the quoted Bismut--Freed holonomy formula.
- 2026-05-30 anomaly proof-boundary pass: expanded the APS,
  Bismut--Freed, Pfaffian-line, and Witten mapping-torus theorem boundaries.
  The chapter now states what analytic/topological machinery is imported and
  what QFT conclusions are derived from it.  The remaining debt is a possible
  later global-analysis appendix proving APS/Bismut--Freed/mod-two index
  infrastructure rather than a hidden QFT anomaly claim.
- 2026-05-30 SU(2) trace-delta arithmetic pass: expanded the Witten anomaly
  theorem boundary by deriving \(T_\Delta(R_j)\) from finite-dimensional
  \(SU(2)\) weights in the monograph's \(t_a=\sqrt2 J_a\) normalization and
  isolating the \(2j\equiv1\pmod4\) parity criterion from the quoted
  five-dimensional mod-two index input.
- 2026-05-30 anomaly-line groupoid pass: added the quotient-background
  groupoid descent criterion and exact finite checks for the cocycle,
  coboundary, based-loop holonomy, and tensor-product behavior of anomaly
  lines.
- 2026-05-31 Quillen spectral-cut pass: expanded the determinant-line
  construction with low-mode spectral-cut charts, finite transition
  determinants, and the determinant cocycle under refinement of cuts; extended
  the eta/global-anomaly calculation check accordingly.
- 2026-05-31 eta-jump/chart-compatibility pass: added the mechanism connecting
  reduced-eta integer jumps to the finite determinant-line chart transition,
  and added an exact single-mode calculation check for the convention.
- 2026-05-31 finite Pfaffian orientation pass: added a finite real skew-block
  model explaining Pfaffian sign holonomy as orientation parity and extended
  `eta_global_anomaly_checks.py` to verify Pfaffian-square,
  crossing-parity, and direct-sum multiplicativity identities.
- 2026-05-31 Dai--Freed gluing pass: expanded the closed bounding-manifold
  normalization and boundary-vector gluing law, and extended
  `eta_global_anomaly_checks.py` with finite phase checks for gluing
  associativity and APS integer ambiguity.
- 2026-06-01 APS cylinder spectral-flow pass: added the exact integer
  cylinder identity before reduction modulo \(\mathbb Z\), isolated the
  endpoint-kernel term from the incoming APS boundary component, and recorded
  the resulting sign between simple-crossing spectral flow and the chosen
  APS cylinder index representative.
- 2026-06-01 contractible-loop descent pass: expanded the local-descent limit
  of Dai--Freed inflow into a background-space Stokes/transgression argument
  and extended `eta_global_anomaly_checks.py` with a finite cochain model of
  the interior-cut cancellation plus APS integer ambiguity.
- 2026-06-01 Witten clutching pass: added the explicit mapping-torus bundle
  \(P_g\), explained homotopy invariance and concatenation additivity before
  the mod-two-index theorem is used, and extended
  `eta_global_anomaly_checks.py` with exact \(\mathbb Z_2\)-character
  bookkeeping for the Pfaffian sign.
- 2026-06-01 APS half-cylinder sign pass: inserted the collar-mode calculation
  fixing why \(P_{\ge0}\psi|_Y=0\) keeps the negative spectral subspace in the
  inward-coordinate convention, and extended `eta_global_anomaly_checks.py`
  with exact sign checks for the inward cylinder, zero-mode exclusion, and
  opposite boundary orientation.
- 2026-06-01 global-anomaly theorem-boundary ledger: added the chapter-level
  separation between imported pure global-analysis infrastructure and
  QFT-facing anomaly conclusions derived from those inputs, to keep #696's
  remaining proof debt honest rather than hidden in quoted theorem language.
- 2026-06-01 dual anomaly-line cancellation pass: added the dual-line
  cancellation criterion over the quotient background groupoid and exact
  finite checks for inverse cocycles, tensor trivialization, and flat
  stabilizer holonomy before cancellation.
- 2026-06-01 Cech-de Rham determinant-line pass: inserted the local
  connection/transition formulae and loop-holonomy coordinate expression
  immediately after the Bismut--Freed theorem, and extended
  `eta_global_anomaly_checks.py` to verify the finite line-bundle algebra.
- 2026-06-02 stabilizer-character anomaly-line pass: sharpened quotient
  groupoid descent at fixed backgrounds.  The chapter now restricts the
  anomaly cocycle to the stabilizer \(\mathcal G_A\), proves in prose that it
  is a character invariant under local frame changes, and explains why
  triviality of this character is the exact algebraic condition for a
  line-valued determinant or Pfaffian vector to descend on a single orbit
  when no further curvature obstruction is present.  The companion
  `eta_global_anomaly_checks.py` now verifies frame-change invariance of
  stabilizer characters and the single-orbit representative-independence
  obstruction with exact finite arithmetic.
