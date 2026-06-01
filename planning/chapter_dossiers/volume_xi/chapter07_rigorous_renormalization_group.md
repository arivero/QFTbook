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
- `P_N`, `Q_N`, `B_N`: finite-dimensional projection, complementary
  projection, and projected RG subspace.
- `epsilon_N(V_N;A)`: complement residual after solving the projected RG
  fixed-point equation.
- `B_ker`: Banach space of kernels in a constructive fermionic fixed-point
  output datum.
- `C_Lambda`, `V_*`: fixed-cutoff covariance and fixed interaction in the
  long-range fermionic benchmark.
- `[psi]`, `[J]`: field and density source scaling dimensions in the
  fermionic fixed-point output theorem.
- `L`, `D`, `b=L^D`: hierarchical scale factor, dimension parameter, and
  block volume in the scalar hierarchical RG datum.
- `Delta`, `a=L^{-Delta}`, `gamma`: field scaling dimension, rescaling
  factor, and hierarchical Gaussian fluctuation variance.
- `B_hier`: Banach space of even analytic scalar hierarchical interactions,
  modulo additive constants.
- `R_hier`: hierarchical nonlinear RG map defined by one-dimensional Gaussian
  convolution and block power.
- `c_*`, `:Phi^n:_{c_*}`: fixed Gaussian variance and Wick coordinates used
  to diagonalize the Gaussian hierarchical linearization.
- `y_{2r}=D-r(D-2)`: engineering exponent of the even scalar local
  coordinate `:Phi^{2r}:`.
- `I`: index set of microscopic regulators in a Wilsonian universality datum.
- `Rec_{i,n}`: \(n\)-step reconstruction map from a tuned microscopic
  regulator to normalized long-distance observable data.
- `O`, `O_*`: observable-data topological vector space and common
  reconstructed limit.
- `A_frak`, `O_alpha`, `pi_alpha_beta`, `O_germ`: directed family of finite
  observation windows, Banach observable windows, projection maps, and the
  projective-limit observable germ used to define universality classes.
- `G`: normalization group acting continuously on observable data.
- `a_k`, `q`, `B_k`, `Delta_phi`: ordinary short-range scalar lattice spacing,
  block kernel, block-spin map, and field scaling exponent.
- `g_k`, `K_k`: local coordinates and polymer activity in the ordinary
  short-range scalar block-spin RG chart.
- `S_{n,k}`: connected cumulant distribution reconstructed from normalized
  block-spin fields.
- `Phi`, `Psi`: auxiliary-to-short-range RG transfer maps on Banach charts
  and observable-data spaces.
- `d_j`, `delta_j`, `M_j`, `z_j`: one-step transfer defect, its norm bound,
  target RG Lipschitz constant on the comparison tube, and accumulated
  short-range orbit error.
- `tau_aux`, `tau_sr`, `A`, `r`: auxiliary and target unstable tuning maps,
  their linear comparison, and the target tuning remainder.

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
- Defines finite-dimensional projection truncations of an RG equation and the
  complement residual.
- Proves that projected RG zeros can be spurious, even in finite dimension.
- Proves the corollary that a projected RG zero lifts to a true fixed point
  only when the complement residual and Newton--Kantorovich constants satisfy
  the full Banach-space contraction inequalities.
- Defines the output data of a constructive fermionic RG fixed point:
  fixed-cutoff Grassmann covariance, Banach kernel space, exact RG map, fixed
  interaction, source dimensions, response functions, and remainders.
- States the long-range fermionic \(\psi^4_d\) fixed-point theorem as a
  quoted benchmark: a nontrivial fixed interaction, constructed response
  functions, naive field exponent, anomalous analytic density exponent, and
  stretched-exponential cutoff-controlled remainders.
- Proves that irrelevant-kernel tails are part of the fixed-point theorem:
  solving only the projected local-coordinate equation leaves an uncontrolled
  \(Q(\mathcal R(V)-V)\) residual unless a graph or contraction solves the
  full irrelevant equation.
- Defines a hierarchical scalar RG datum as an explicit nonlinear Gaussian
  convolution map on a Banach space of even analytic interactions, with the
  hierarchical covariance and normalization convention included in the data.
- Proves the Gaussian hierarchical linearization in Wick coordinates:
  \(D\mathcal R_{\rm hier}|_0(:\Phi^n:)=b a^n:\Phi^n:\), and derives the
  canonical scalar engineering exponent \(y_{2r}=D-r(D-2)\).
- Quotes the theorem-level hierarchical scalar non-Gaussian fixed-point
  benchmark, while explicitly separating it from an unproved construction of
  the ordinary short-range three-dimensional scalar Wilson-Fisher fixed
  point.
- Defines the ordinary short-range scalar block-spin reconstruction datum:
  finite-range lattice Gibbs measures, normalized block kernels, block-spin
  maps, local coordinates plus polymer activity, cumulant distributions from
  normalized lattice fields, and the exact reconstruction estimate required
  to turn a tuned block-spin RG trajectory into distributional Schwinger
  functions.
- Defines the auxiliary-to-short-range RG transfer datum needed to use
  hierarchical, long-range, fermionic, tensor, or functional-RG fixed-point
  results as statements about ordinary short-range scalar targets.
- Derives the finite orbit-comparison telescope
  \(\|z_n\|\le \sum_j(\prod_{\ell>j}M_\ell)\delta_j\), the stable geometric
  bound when \(M_j\le\theta<1\), and the separate relevant-coordinate
  amplification estimate requiring target tuning-map control.
- Records current rigorous benchmarks: constructive long-range fermionic
  \(\psi^4_d\) fixed points with irrelevant kernels included, hierarchical
  scalar fixed points with controlled unstable/stable directions, and
  infinite-dimensional tensor-RG fixed points with explicit contraction
  neighborhoods.
- Gives a precise monograph definition of universality class as an RG
  attraction statement plus reconstruction data.
- Defines a Wilsonian universality datum with microscopic regulators, tuned
  initial points, a Banach RG chart, reconstruction maps, observable topology,
  and normalization group.
- Refines the phrase "universality class" to an equivalence class of
  normalized observable germs in a projective topology of finite observation
  windows, and separates finite-window certificates from theorem-level
  convergence in the full directed family.
- Proves that universality is an equivalence relation once convergence to a
  common reconstructed observable datum is part of the theorem.
- Defines correction-to-scaling data as part of a sharpened Wilsonian
  universality theorem: stable irrelevant eigendirections, rates
  \(\omega_a\), microscopic amplitudes \(c_{i,a}\), reconstructed correction
  distributions \(\mathcal C_a\), and seminorm remainder estimates.
- Records the finite-codimension critical-surface statement in prose rather
  than as a theorem-family result: after a \(C^1\) stable graph and microscopic
  transversality have been proved, the codimension statement is the standard
  submersion/implicit-function consequence.  The differentiability of the
  stable graph is the analytic RG burden, not a consequence of naming the
  locus ``critical.''

## Figure Ledger

No figure is included in this pass.  A later diagram should show covariance
decomposition, block integration, projection to local coordinates, and polymer
remainder contraction.

## Companion Scripts

- `calculation-checks/rg_projection_checks.py`: exact rational check for the
  finite-dimensional projected-zero counterexample and complement-residual
  lift calculation, plus the finite irrelevant-tail graph equation.
- `calculation-checks/rg_hierarchical_scalar_checks.py`: exact rational
  checks for the hierarchical scalar Gaussian Wick-coordinate eigenvalue,
  engineering exponents, and relevance bookkeeping.
- `calculation-checks/rg_short_range_reconstruction_checks.py`: exact rational
  checks for ordinary short-range scalar block-spin normalization, pairing,
  covariance scaling, reconstruction-bound arithmetic, and
  correction-to-scaling bookkeeping, plus the auxiliary-transfer telescoping
  estimate, relevant-direction amplification formula, and projective
  observable-germ finite-window certificate.
