# Chapter 08: Witten-Donaldson Theory And The Seiberg-Witten Comparison

## Source Position

Volume VIII applies twisting to the central four-dimensional cohomological
gauge-theory example.  This chapter now separates finite-dimensional
Donaldson and monopole geometry from the cohomological field-theory Ward
identities and from the four-dimensional RG comparison.  It supplies the
index derivations and normalization checks needed before later chapters use
Donaldson-Witten theory as a serious example of TQFT arising from a physical
gauge theory.

## Notation Inventory

- `X`, `g`, `b_2^+`, `chi`, `sigma`: four-manifold, metric, positive
  intersection rank, Euler characteristic, and signature.
- `P`, `A`, `F_A^\pm`, `G_P`: principal `SU(2)` bundle, connection,
  self-dual/anti-self-dual curvature, and gauge group.
- `k(P)`: instanton number in the trace-delta convention.
- `H_A^i`, `D_A`: ASD deformation cohomology and gauge-fixed elliptic
  operator.
- `O^(j)`, `I(gamma_j)`, `mu(gamma_j)`: descent operators, integrated
  observables, and Donaldson `mu`-classes.
- `D_X^w`, `mathbb D_X^w`, `x`, `h`, `K`, `a_K^w`: Donaldson generating
  function, reduced simple-type series, point/surface variables, basic
  classes, and simple-type coefficients.
- `M_k^sm`, `overline M_k^U`, `B_S`: smooth ASD stratum, Uhlenbeck
  compactification, and BV boundary functional for compactification strata.
- `u`, `a_D`, `a`, `tau(u)`: Seiberg-Witten Coulomb-branch data.
- `s`, `S^pm_s`, `L_s`, `B`, `q`, `sigma(q)`: Spin^c structure, spinor
  bundles, determinant line, Abelian connection, monopole spinor, and
  quadratic self-dual two-form.
- `SW_X(s)`, `B_SW(X)`, `BF_X(s)`: Seiberg-Witten invariant,
  Seiberg-Witten basic classes, and Bauer-Furuta stable cohomotopy class.
- `omega_g`, `lambda`, `L_lambda`, `WC_lambda^X`: period ray, reducible wall
  class, reducible link, and Kotschick-Morgan wall-crossing functional.
- `T(u)`, `Z_D(p,S)`: Abelian contact term and Donaldson generating
  function.

## Claim Ledger

- Fixes the trace-delta Yang-Mills action normalization and derives the ASD
  topological bound with coefficient `4 pi^2 k/g_YM^2`.
- Defines the Donaldson-Witten fields, off-shell `Q`-rules, auxiliary field,
  and localization onto `F_A^+=0`.
- Constructs the ASD deformation complex, determinant line, orientations, and
  Uhlenbeck compactification; proves the virtual dimension formula from
  Atiyah-Singer.
- Defines Donaldson simple type, the reduced Donaldson series, Donaldson
  basic classes, and the exponential simple-type structure theorem with
  status separated from QFT construction.
- Recasts Uhlenbeck small-instanton, reducible, and obstructed strata as BV
  boundary functionals using the finite BV pushforward obstruction theorem.
- Defines the Donaldson descent observables, their degrees, and the
  differential-geometric `mu`-map via the universal bundle.
- Proves the Spin^c characteristic-lift torsor statement, including the
  two-torsion caveat for the first Chern class.
- Defines Spin^c data, the monopole equations, gauge action, deformation
  operator, and proves the expected dimension formula from Dirac and Abelian
  gauge indices.
- Uses the Weitzenbock identity to explain the compactness mechanism for
  monopole moduli spaces.
- Defines Seiberg-Witten basic classes and simple type, adds K3, `E(n)`, and
  blow-up arithmetic examples, and records the Bauer-Furuta refinement and
  Furuta \(10/8+2\) inequality.
- States the Coulomb-branch RG comparison datum, including the `u`-plane,
  singular fibers, observable map, contact term `T(u)`, chamber dependence,
  and determinant-line phases.
- Defines \(b_2^+=1\) chambers, reducible wall classes, the wall equation,
  the link form of Kotschick-Morgan wall crossing, and the BV boundary
  interpretation of chamber jumps.  The 2026-05-29 continuing anti-wrapper
  audit demoted the chamber-jump BV-boundary statement from proposition form
  to conditional explanatory prose, since the mathematical work is carried by
  the compactified parameterized moduli problem and Stokes theorem.
- States the Witten simple-type comparison datum and separates the
  Donaldson structure theorem from the SW-identification/QFT RG problem.
- Gives the normalization-sensitive \(u\)-plane integral data with
  \(A(u)^\chi B(u)^\sigma\), theta kernel, contact term, and a conditional
  boundary derivation of wall crossing.
- Preserves the open problem of deriving the Donaldson-Seiberg-Witten
  comparison as a theorem-level statement inside constructed four-dimensional
  QFT.

## Calculation Checks

- `calculation-checks/donaldson_sw_comparison_checks.py` verifies the ASD
  index formula, the Seiberg-Witten expected dimension formula, the
  `2 chi + 3 sigma` identity, Donaldson descent degrees, Spin^c
  characteristic-lift parity, K3 and elliptic-surface simple-type arithmetic,
  blow-up square shifts, elliptic-surface binomial coefficients, Furuta
  examples, and the trace-delta instanton action coefficient.

## Figure Ledger

No figure is included in this pass.  Future figures should show the ASD
deformation complex, the monopole deformation complex, the `u`-plane with
singular fibers, and the RG comparison from the twisted non-Abelian theory to
the Abelian monopole theory.
