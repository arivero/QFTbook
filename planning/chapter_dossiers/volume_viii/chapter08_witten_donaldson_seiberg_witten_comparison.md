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
- `u`, `a_D`, `a`, `tau(u)`: Seiberg-Witten Coulomb-branch data.
- `s`, `S^pm_s`, `L_s`, `B`, `q`, `sigma(q)`: Spin^c structure, spinor
  bundles, determinant line, Abelian connection, monopole spinor, and
  quadratic self-dual two-form.
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
- Defines the Donaldson descent observables, their degrees, and the
  differential-geometric `mu`-map via the universal bundle.
- Defines Spin^c data, the monopole equations, gauge action, deformation
  operator, and proves the expected dimension formula from Dirac and Abelian
  gauge indices.
- Uses the Weitzenbock identity to explain the compactness mechanism for
  monopole moduli spaces.
- States the Coulomb-branch RG comparison datum, including the `u`-plane,
  singular fibers, observable map, contact term `T(u)`, chamber dependence,
  and determinant-line phases.
- Preserves the open problem of deriving the Donaldson-Seiberg-Witten
  comparison as a theorem-level statement inside constructed four-dimensional
  QFT.

## Calculation Checks

- `calculation-checks/donaldson_sw_comparison_checks.py` verifies the ASD
  index formula, the Seiberg-Witten expected dimension formula, the
  `2 chi + 3 sigma` identity, Donaldson descent degrees, and the trace-delta
  instanton action coefficient.

## Figure Ledger

No figure is included in this pass.  Future figures should show the ASD
deformation complex, the monopole deformation complex, the `u`-plane with
singular fibers, and the RG comparison from the twisted non-Abelian theory to
the Abelian monopole theory.
