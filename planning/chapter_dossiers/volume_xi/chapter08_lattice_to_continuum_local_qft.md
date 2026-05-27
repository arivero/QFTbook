# Chapter 08: Relation Between Lattice And Continuum Local QFT

## Source Position

Volume XI now connects finite-regulator lattice objects to continuum local
QFT objects.  The chapter follows reflection positivity, continuum limits,
lattice gauge theory, Monte Carlo, and rigorous RG with the reconstruction
and local-algebra comparison layer.

## Notation Inventory

- `a`, `Lambda_a`, `V`: lattice spacing, lattice, and finite region.
- `Phi_a(f)`, `Z_a`: scaled smeared lattice field and field normalization.
- `Q_a(x)`, `I_a f`, `f_a`: lattice cell, cell-average map, and
  piecewise-constant test-function approximation.
- `O_A,a^ren`, `Z_AB(a)`: renormalized composite operator and mixing matrix.
- `S_{n,a}`, `S_n`: lattice and continuum Schwinger distributions.
- `T_a`, `D_0`, `p`: regulated multilinear functionals, dense test set, and
  controlling seminorm in the distributional convergence criterion.
- `G=(V,E)`, `A`, `K_m`, `N_n(x,y)`: finite graph, adjacency matrix,
  massive lattice operator, and length-\(n\) path count in the random-walk
  representation.
- `S_a`, `A_+`, `Theta`: reflected-positive Schwinger functional,
  positive-time test algebra, and reflection.
- `A_a(O_a)`, `A(O)`: lattice and continuum local algebras.
- `P_a(x)`: plaquette representative of action-density-type operators.

## Claim Ledger

- Defines scaling maps from lattice fields to continuum distributions.
- Proves that cell averages approximate continuum test functions and thereby
  fix the normalization of lattice smearing maps.
- Defines the scaling-limit datum: regulator states, trajectory, test spaces,
  operator maps, normalizations, and convergence topology.
- Defines distributional convergence of Schwinger functions.
- Proves a dense-test convergence criterion under a uniform seminorm bound,
  making explicit which part is functional analysis and which part is the
  constructive estimate.
- Proves the finite-graph random-walk resolvent for the massive lattice
  covariance and relates it to path/polymer expansions.
- States the OS reconstruction bridge under reflection positivity and growth
  hypotheses.
- Proves closedness of reflection positivity under entrywise convergence of
  finite reflected Gram matrices.
- Describes local-algebra limits and the additional gauge-theory center and
  Gauss-law data.
- Proves that tensor-factor locality for spin lattice algebras passes to the
  limiting GNS dense domain under convergence of local correlation functions.
- Defines universality as equality of reconstructed local QFT data, not only
  equality of selected exponents.

## Figure Ledger

No figure is included in this pass.  Future figures should show lattice cells
approximating a continuum region, operator mixing into continuum fields, and
the OS reconstruction pipeline.

## Calculation Checks

- `calculation-checks/lattice_continuum_bridge_checks.py` verifies the
  cell-average product arithmetic, finite-graph random-walk resolvent,
  reflection-positive Gram-matrix limit, and tensor-product locality for
  disjoint spin factors.
