# Chapter 09: Categorical Symmetry And Defect Fusion

## Source Position

Volume IX now extends ordinary and higher-form symmetry to the categorical
symmetry language of topological defects, junctions, fusion, condensation, and
anomaly obstruction.

## Notation Inventory

- `D_Q`: defect category of a local QFT.
- `D`, `D_a`: codimension-one topological defects and simple defect labels.
- `rho_D`: action of a defect on the local-operator space.
- `N_ab^c`: defect fusion coefficients.
- `Hom(D_a tensor D_b, D_c)`: junction spaces.
- `A`, `m`, `eta`: algebra object and its multiplication/unit maps for
  condensation.
- `A_H`, `Delta`: regular algebra of a finite symmetry and its normalized
  comultiplication in the untwisted pointed defect subcategory.
- `N_H`: self-dual finite-gauging defect satisfying
  \(N_H^2=\oplus_{h\in H}D_h\) after a self-adjoint duality choice.
- `eta`, `N`: in the Ising example, the invertible spin-flip defect and the
  Kramers--Wannier noninvertible defect; the TeX uses `\eta` and
  `\mathcal N`.
- `S_Ising`: the \(3\times3\) Ising modular matrix in the
  \((1,\varepsilon,\sigma)\) basis; the \(\varepsilon\) row is the spin-flip
  line `eta`, and the \(\sigma\) row is the Kramers--Wannier line `N`.
- `lambda_a(i)`: eigenvalue of the topological defect \(D_a\) acting on the
  primary sector \(i\), \(S_{ai}/S_{1i}\).

## Claim Ledger

- Defines categorical symmetry from topological defects and fusion.
- Defines the action of a codimension-one defect on local operators by
  surrounding insertions.
- Relates associativity of defect fusion to junction spaces and pentagon
  identities.
- Formulates gauging as condensation of an algebra object.
- Develops the finite regular algebra \(A_H=\oplus_h D_h\) as an explicit
  separable Frobenius algebra object in the untwisted pointed defect
  subcategory, including the normalized comultiplication.
- Proves the object-level self-dual finite-gauging fusion ring
  \(D_gD_h=D_{gh}\), \(D_hN_H=N_HD_h=N_H\),
  \(N_H^2=\oplus_hD_h\), its associativity, and
  \(d(N_H)=\sqrt{|H|}\).
- Develops the Ising/Kramers--Wannier example as a concrete noninvertible
  categorical symmetry: \(N^2=1+\eta\), \(d_N=\sqrt2\), and the defect action
  on the three primary sectors is diagonalized by the Ising modular matrix.
- Proves directly that the defect eigenvalues furnish a representation of
  the fusion algebra, so the vanishing action of \(N\) on the spin sector is
  a consequence of the fusion rules and not a slogan about duality.
- Explains the rational-example SymTFT comparison map
  `bulk topological lines -> boundary topological defects -> End(V_loc)`
  without claiming that arbitrary continuum QFTs have already been built
  from such a fully extended bulk-boundary construction.
- Identifies anomaly as obstruction to choice-independent defect-network
  evaluation.
- Hands off explicitly to Chapter 10 for the finite normal-subgroup gauging
  and electric-magnetic line-lattice examples, while keeping the unresolved
  interacting-continuum construction as the open problem.
- Hands off explicitly to Chapter 11 for the finite `Z_N` one-form SymTFT and
  higher-gauging condensation-defect cochain construction, so the categorical
  framework is connected to the modern four-dimensional condensation mechanism
  without treating the continuum surface-operator construction as already
  solved.

## Calculation Checks

- `calculation-checks/ising_defect_fusion_checks.py` verifies, in exact
  \(\mathbb Q(\sqrt2)\) arithmetic, the Ising defect fusion associativity,
  Frobenius--Perron dimension homomorphism, modular \(S\)-matrix
  orthogonality, Verlinde formula, and line-eigenvalue representation of the
  fusion algebra.  It also verifies finite regular-algebra separability and
  Frobenius identities plus self-dual gauging fusion-ring associativity for
  cyclic examples and \(S_3\).

## Figure Ledger

No figure is included in this pass.  Future figures should include defect
spheres acting on local operators, junction bases, pentagon moves, and
condensation networks.

## Anti-Wrapper Audit

- 2026-05-29: strengthened the reflection-positivity-to-dagger-category proof
  by spelling out half-ball states, order reversal under radial reflection,
  null-junction quotienting, and unitarity of isotopy maps in orthonormal
  junction bases.
- 2026-05-30 proof-substance pass: retained `Reflection adjoint of a
  topological-defect action` as proposition-level material, but expanded the
  proof so it is an actual Hilbert-space/domain argument.  The proof now
  introduces finite-radius defect actions, takes the shrinking-limit inside
  the BPZ pairing on the dense local domain, reflects the finite-radius ball
  correlator to the \(D^\dagger\) insertion, uses topological isotopy before
  passing to the limit, and only then extends by boundedness to
  \(\mathcal H_{\rm loc}\).  The text also separates reflection
  self-adjointness from invertible-defect unitarity.
