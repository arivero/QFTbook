# Volume VII, Chapter 4 Dossier: Supersymmetric Wilsonian Schemes
Source-File: monograph/tex/volumes/volume_vii/chapter04_supersymmetric_wilsonian_schemes.tex

## Logical Role

- Role in the monograph: state the finite-cutoff scheme data required before
  exact supersymmetric dynamics can be formulated.
- Immediate predecessor: supersymmetric gauge theory.
- Immediate successor: holomorphy, nonrenormalization, and four-dimensional
  \(\mathcal N=1\) dynamics.

## Definitions And Results

- Supersymmetric Wilsonian datum.
- Gauge-compatible Wilsonian data: BV finite-cutoff data or finite lattice
  gauge data with blocking maps.
- BV quantum master equation at finite cutoff.
- Admissible BV Wilsonian step: split odd symplectic spaces, Lagrangian
  integration cycle, convergence prescription, BV boundary condition, and
  supersymmetry compatibility; the chapter now emphasizes that this hypothesis
  is the load-bearing construction problem, while QME preservation is the BV
  Stokes consequence.
- Finite-cutoff Darboux-coordinate BV Stokes calculation for the integrated
  variables, kept as worked prose because the substantive datum is the
  boundaryless admissible cycle rather than the coordinate divergence
  identity.
- BV pushforward of half-densities and preservation of the quantum master
  equation by BV Stokes.
- Composable BV Wilsonian tower and semigroup property of BV pushforward.
- Finite circle-Darboux model verifying BV Stokes, QME preservation by
  pushforward, and product-cycle semigroup behavior in an explicit
  Fourier/odd-variable algebra.
- \(F\)-term and \(D\)-term local coordinates.
- Holomorphic Wilsonian scheme hypothesis.
- Selection rule for Wilsonian \(F\)-terms.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\mathcal E_\Lambda\) | regulated superfield variable space |
| \(S_\Lambda\) | Wilsonian action at cutoff \(\Lambda\) |
| \((\,\cdot\,,\,\cdot\,)_\Lambda\) | regulated BV bracket |
| \(\Delta_\Lambda\) | regulated BV Laplacian |
| \(\rho_\Lambda\) | BV half-density \(\exp(iS_\Lambda/\hbar)\mu_\Lambda^{1/2}\) |
| \(K_{\Lambda\Lambda'}\) | eliminated BV variables in a Wilsonian step |
| \(\mathcal L_{\Lambda\Lambda'}\) | Lagrangian integration cycle for eliminated variables |
| \(\mathcal R_{\Lambda\Lambda'}\) | Wilsonian coarse-graining map |
| \(\tau\) | holomorphic gauge coupling coordinate |
| \(P\) | finite model pushforward, normalized circle integral with \(\xi=0\) |

## Claim Ledger

1. Supersymmetric Wilsonian integration and supersymmetric regularization are
   distinct data.
2. BV pushforward is first a map of half-densities; the action is obtained
   only after choosing a reference half-density and logarithm coordinate.
3. BV pushforward preserves the quantum master equation when the split BV
   Laplacian, Lagrangian cycle, and BV boundary condition are part of the
   finite-cutoff data.
4. The Wilsonian semigroup law follows from a composable BV tower: compatible
   odd symplectic splittings, product Lagrangian cycle, product Berezinian
   convention, and a valid ordinary or oscillatory Fubini theorem.
5. The finite circle-Darboux model checks the algebraic content of the BV
   pushforward statement: \(P\Delta_K=0\), \(P\Delta=\Delta_BP\), and
   iterated product-cycle pushforwards commute.
6. Holomorphic exact-dynamics claims require a declared holomorphic Wilsonian
   scheme and anomaly ledger.
7. Gauge-theory Wilsonian schemes must be formulated through BV finite-cutoff
   data or finite lattice gauge data before holomorphic coordinates,
   moduli-space statements, or exact-dynamics arguments are used.
8. In a gauge-fixed supersymmetric Wilsonian path integral, gauge consistency
   is the quantum BV master equation before restriction to the gauge-fixing
   Lagrangian submanifold; the gauge-fixed Ward identities are obtained from
   this equation by BV Stokes.

## Calculation Checks

- `calculation-checks/susy_wilsonian_bv_checks.py` verifies the finite
  circle-Darboux model: fiber BV Stokes, the BV pushforward chain-map
  identity, preservation of a finite QME-closed half-density, and semigroup
  behavior for two product-cycle fiber integrations.

## Figures

- None in this chapter.

## Anti-Wrapper Audit

- 2026-05-29: demoted the semigroup property of a composable BV Wilsonian
  tower to a worked paragraph.  The content is the Fubini/product-cycle
  consequence of the composability definition; the genuinely nontrivial
  material is the construction and admissibility of that BV tower.
- 2026-05-29 seventh pass: demoted the finite-cutoff Darboux BV Stokes
  coordinate calculation from lemma form to worked prose, and expanded QME
  preservation to show the split Laplacian, commutation with the fiber
  integral, and vanishing boundary functional explicitly.
