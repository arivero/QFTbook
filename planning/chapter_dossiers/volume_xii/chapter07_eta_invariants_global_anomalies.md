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
- Proves the cylinder variation formula for \(\xi\) modulo integers from the
  APS theorem, including the orientation-reversal bookkeeping
  \(\xi(-B)=-\xi(B)+h(B)\).
- Defines determinant-line fibers and states the Bismut--Freed holonomy
  theorem for mapping tori, with an expanded mechanism explaining local
  zeta-determinant charts, the Bismut--Freed connection, curvature as the
  family index density, and holonomy as the adiabatic eta invariant.
- Makes the Quillen determinant-line spectral-cut chart construction explicit:
  the low-mode line \(L_a(b)\), the finite window
  \(E_{[a,c)}^\pm(b)\), the determinant transition element
  \(\det D^+_{[a,c)}\), and its cocycle identity under a refinement of cuts.
- Explains finite gauge-transformation phases as determinant-line holonomies,
  as a direct application of the quoted Bismut--Freed holonomy theorem to the
  mapping torus of the gauge transformation.
- Makes the descent criterion over the quotient background groupoid explicit:
  determinant-line transport is a groupoid `1`-cocycle, changes of local
  trivialization shift it by a coboundary, based-loop holonomies are
  invariant, and a quotient-valued partition function exists only after an
  equivariant trivialization of the anomaly line.
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
- Explains Dai--Freed inflow as a boundary-line trivialization and derives the
  descent limit for contractible loops.
- Expands the Dai--Freed gluing mechanism: for a closed odd manifold that
  bounds, APS identifies the eta phase with the exponentiated local index
  integral modulo integers; for an odd manifold with boundary, the
  Dai--Freed object is a vector in the inverse boundary anomaly line, and
  pairing two such vectors gives the closed phase of the glued odd manifold.
- Records the interacting-QFT anomaly-line construction as an open problem.

## Calculation Ledger

- `calculation-checks/eta_global_anomaly_checks.py` checks the APS
  orientation bookkeeping, the first \(SU(2)\) trace-delta Dynkin indices,
  Witten parity criterion, Pfaffian-sign multiplicativity, cubic-weight-sum
  cancellation, the finite skew-block Pfaffian orientation model, cylinder
  congruence arithmetic, action-groupoid anomaly cocycle/coboundary
  identities, based-loop holonomy invariance, the stabilizer-character
  obstruction to descent, and the Quillen spectral-cut transition cocycle for
  determinant-line charts, and the finite \(U(1)\)-phase algebra behind
  Dai--Freed gluing.
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
- 2026-05-31 finite Pfaffian orientation pass: added a finite real skew-block
  model explaining Pfaffian sign holonomy as orientation parity and extended
  `eta_global_anomaly_checks.py` to verify Pfaffian-square,
  crossing-parity, and direct-sum multiplicativity identities.
- 2026-05-31 Dai--Freed gluing pass: expanded the closed bounding-manifold
  normalization and boundary-vector gluing law, and extended
  `eta_global_anomaly_checks.py` with finite phase checks for gluing
  associativity and APS integer ambiguity.
