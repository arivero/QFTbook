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
- `E`, `E**`, `Q`: local torsion-free sheaf, double dual, and punctual
  quotient used to compare Donaldson--Uhlenbeck and Gieseker policies.
- `u`, `a_D`, `a`, `tau(u)`: Seiberg-Witten Coulomb-branch data.
- `s`, `S^pm_s`, `L_s`, `B`, `q`, `sigma(q)`: Spin^c structure, spinor
  bundles, determinant line, Abelian connection, monopole spinor, and
  quadratic self-dual two-form.
- `SW_X(s)`, `B_SW(X)`, `BF_X(s)`: Seiberg-Witten invariant,
  Seiberg-Witten basic classes, and Bauer-Furuta stable cohomotopy class.
- `omega_g`, `lambda`, `L_lambda`, `WC_lambda^X`: period ray, reducible wall
  class, reducible link, and Kotschick-Morgan wall-crossing functional.
- `x_lambda(omega)`: wall-normal component `lambda` paired with the period
  ray.
- `E_t(x)`: completed sign/error-function normal factor in the local
  Siegel-Narain wall-crossing model.
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
  status separated from QFT construction; the theorem boundary now separates
  the finite-dimensional Donaldson input from the algebraic consequence that
  the Gaussian-reduced series is a finite exponential sum obeying
  constant-coefficient ODEs along every surface direction.
- Recasts Uhlenbeck small-instanton, reducible, and obstructed strata as BV
  boundary functionals using the finite BV pushforward obstruction theorem.
- Adds a Donaldson--Uhlenbeck versus Gieseker comparison policy: the same
  lost second Chern class is kept as an Uhlenbeck support cycle for
  Donaldson invariants, but as punctual quotient data and equivariant Euler
  classes in the Nekrasov/Gieseker resolution.
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
  Furuta \(10/8+2\) inequality with the monopole-map Fredholm-plus-compact
  construction and the spin \(\operatorname{Pin}(2)\)-equivariant obstruction
  mechanism exposed at the point of use.
- States the Coulomb-branch RG comparison datum, including the `u`-plane,
  singular fibers, observable map, contact term `T(u)`, chamber dependence,
  and determinant-line phases.
- Defines \(b_2^+=1\) chambers, reducible wall classes, the wall equation,
  the link form of Kotschick-Morgan wall crossing, and the BV boundary
  interpretation of chamber jumps.  The theorem-boundary mechanism now spells
  out the parameterized moduli space, the truncated boundary
  \(\mathcal M_+\sqcup(-\mathcal M_-)\sqcup\mathbb L_\lambda\), Stokes'
  theorem for the extended \(\mu\)-class, and the reducible normal-complex
  reason for the Kotschick-Morgan universal polynomial.  The 2026-05-29
  continuing anti-wrapper audit demoted the chamber-jump BV-boundary statement
  from proposition form to conditional explanatory prose, since the
  mathematical work is carried by the compactified parameterized moduli problem
  and Stokes theorem.
- States the Witten simple-type comparison datum and separates the
  Donaldson structure theorem from the SW-identification/QFT RG problem; the
  chapter now decomposes that RG problem into proof obligations involving
  nonperturbative twisted-theory construction, \(Q\)-compatible Wilsonian flow,
  \(u\)-plane boundary control, singular-fiber monopole replacement, and
  determinant/contact normalization.
- Adds an explicit comparison-architecture guide: the Donaldson
  moduli-space layer, cohomological localization layer, Coulomb-branch layer,
  and final Wilsonian gluing claim are now separated as a dependency ladder.
  The simple-type formula also has a factor-origin ledger distinguishing the
  finite Donaldson exponential shape, SW labels/counts, contact Gaussian,
  determinant-line phase, universal constant, and chamber/\(u\)-plane
  boundary contribution.
- Gives the normalization-sensitive \(u\)-plane integral data with
  \(A(u)^\chi B(u)^\sigma\), theta kernel, contact term, and a conditional
  boundary derivation of wall crossing; the wall-normal theta-kernel factor
  is now isolated as an error-function completion whose derivative is a
  delta sequence of mass \(2\), explaining the local analytic source of the
  reducible-flux jump.
- Preserves the open problem of deriving the Donaldson-Seiberg-Witten
  comparison as a theorem-level statement inside constructed four-dimensional
  QFT.

## Calculation Checks

- `calculation-checks/donaldson_sw_comparison_checks.py` verifies the ASD
  index formula, the Seiberg-Witten expected dimension formula, the
  `2 chi + 3 sigma` identity, Donaldson descent degrees, Spin^c
  characteristic-lift parity, K3 and elliptic-surface simple-type arithmetic,
  blow-up square shifts, elliptic-surface binomial coefficients, Furuta
  examples, spin Dirac quaternionic-index arithmetic in the Furuta examples,
  Donaldson blow-up cosh/sinh parity coefficients after the contact Gaussian,
  Donaldson finite-exponential moment reconstruction, and the trace-delta
  instanton action coefficient, as well as the wall-normal sign jump and
  delta-sequence mass/concentration coefficients used in the \(u\)-plane
  wall-crossing explanation.

## Figure Ledger

No figure is included in this pass.  Future figures should show the ASD
deformation complex, the monopole deformation complex, the `u`-plane with
singular fibers, and the RG comparison from the twisted non-Abelian theory to
the Abelian monopole theory.

## Audit Notes

- 2026-05-30 Bauer-Furuta proof-boundary pass: expanded the stable
  cohomotopy theorem boundary by writing the Sobolev monopole map
  \(\mathcal F=L+C\), identifying \(L=d^*\oplus d^+\oplus\not D\) as Fredholm
  and \(C\) as compact on bounded sets, explaining finite-dimensional
  approximation by low spectral modes, and separating the pure
  \(\operatorname{Pin}(2)\)-equivariant stable-homotopy input behind Furuta's
  inequality from the QFT comparison problem.
- 2026-05-30 wall-crossing proof-boundary pass: expanded the link-form theorem
  boundary by displaying the parameterized ASD moduli space and its truncated
  boundary, deriving the chamber jump by Stokes' theorem, and identifying the
  reducible splitting/off-diagonal normal complex as the source of the link
  and the universal polynomial variables.
- 2026-05-30 Donaldson simple-type proof-boundary pass: expanded the structure
  theorem boundary by identifying the point-operator minimal-polynomial input,
  the geometric content of finite characteristic exponential weights after the
  Gaussian factor is removed, and the purely algebraic finite-exponential ODE
  and moment-reconstruction consequences.
- 2026-05-30 Donaldson-SW RG-obligation pass: expanded the Witten comparison
  hypothesis into concrete QFT proof obligations, so the final comparison
  formula no longer hides the construction of the twisted theory, the
  \(Q\)-compatible Wilsonian flow, the \(u\)-plane boundary analysis, the
  monopole singular-fiber replacement, or the determinant/contact normalizations.
- 2026-05-31 \(u\)-plane wall-normal pass: exposed the local
  Siegel-Narain wall-crossing mechanism by writing the error-function
  completed sign factor, deriving its Gaussian delta sequence of total
  jump \(2\), and adding exact coefficient checks for the sign jump and
  concentration scale.
- 2026-06-03 Donaldson blow-up coefficient pass: expanded the comparison
  example into an exceptional-insertion parity table for
  \(e^{-t^2/2}\cosh t\) and \(e^{-t^2/2}\sinh t\), separating the contact
  Gaussian from the two exceptional basic-class phases and adding exact
  rational checks for the even and adjacent lift coefficients.
- 2026-06-03 comparison-architecture pass: added a chapter-level dependency
  ladder and a factor-origin ledger for the Witten simple-type formula, so the
  Donaldson finite-geometry theorem, SW finite-dimensional counts, Abelian
  contact Gaussian, determinant-line phase, universal constant, and
  chamber/\(u\)-plane boundary analysis are no longer left for the reader to
  infer from adjacent local mechanisms.
- 2026-06-03 small-instanton compactification policy pass: linked the
  Donaldson--Uhlenbeck BV boundary functional to the local Gieseker
  double-dual charge ledger, separating Uhlenbeck \(\mu\)-class extension and
  wall-boundary cancellation from Nekrasov/Gieseker resolved fixed-point
  integration.
