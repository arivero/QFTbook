# Chapter 07: Rigorous Renormalization Group

## Source Position

Volume XI now moves from constructive examples, lattice positivity,
continuum limits, lattice gauge theory, and Monte Carlo methods to the
renormalization group as a controlled map on normed spaces.  This chapter is
the local proof infrastructure for future nonperturbative fixed-point and
constructive RG developments.

## Notation Inventory

- `C=C_<+Gamma`: covariance decomposition.
- `mu_C`, `mu_Gamma`: Gaussian measures.
- `V`, `V_<`, `R_L`: interaction, integrated interaction, and RG map.
- `B`, `U`: Banach space of interactions and RG domain.
- `V_*`, `D R|_{V_*}`: fixed point and linearized RG.
- `E_u`, `E_s`: unstable and stable subspaces.
- `A`, `B`: unstable and stable linear blocks of the RG linearization in a
  local product coordinate.
- `a`, `b`, `gamma`: contraction constants for \(A^{-1}\), \(B\), and the
  weighted sequence norm in the local stable-graph theorem.
- `kappa`, `q_u`, `q_s`, `q`: nonlinear Lipschitz and Lyapunov-Perron
  contraction constants in the stable-graph proof.
- `X_{gamma,rho}(s_0)`: complete weighted sequence space used to construct
  the stable graph.
- `K(X,phi)`: polymer activity.
- `F(V)=R(V)-V`: fixed-point residual.
- `A`: bounded injective approximate inverse used in Newton--Kantorovich
  validation.
- `eta`, `rho`, `L`: residual, linear inverse-error, and derivative-Lipschitz
  constants in the validated fixed-point theorem.
- `I`: index set of microscopic regulators in a Wilsonian universality datum.
- `Rec_{i,n}`: \(n\)-step reconstruction map from a tuned microscopic
  regulator to normalized long-distance observable data.
- `O`, `O_*`: observable-data topological vector space and common
  reconstructed limit.
- `G`: normalization group acting continuously on observable data.

## Claim Ledger

- Defines Gaussian block integration as an exact finite-regulator identity.
- Defines controlled RG maps on Banach spaces and scaling coordinates through
  linearization.
- Proves a local stable-graph theorem for a hyperbolic RG fixed point using
  an explicit Lyapunov-Perron contraction on a complete weighted sequence
  space, with the contraction constant displayed.
- Defines polymer activities and the estimate needed to control irrelevant
  remainders.
- Defines the full data of a theorem-level nonperturbative Wilsonian fixed
  point: regulator class, map/domain/norm, fixed point, linearized spectrum,
  and reconstruction estimates.
- Proves a Newton--Kantorovich validation theorem for an RG fixed point in a
  Banach space, isolating the final fixed-point step from the model-specific
  cluster/tree/tensor estimates.
- Records current rigorous benchmarks: constructive long-range fermionic
  \(\psi^4_d\) fixed points with irrelevant kernels included, and
  infinite-dimensional tensor-RG fixed points with explicit contraction
  neighborhoods.
- Gives a precise monograph definition of universality class as an RG
  attraction statement plus reconstruction data.
- Defines a Wilsonian universality datum with microscopic regulators, tuned
  initial points, a Banach RG chart, reconstruction maps, observable topology,
  and normalization group.
- Proves that universality is an equivalence relation once convergence to a
  common reconstructed observable datum is part of the theorem.

## Figure Ledger

No figure is included in this pass.  A later diagram should show covariance
decomposition, block integration, projection to local coordinates, and polymer
remainder contraction.
