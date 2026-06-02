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
- `S_{a_1...a_n}`, `E`, `G_OS`: Schwinger distribution windows, finite
  test-function subspaces, and finite reflection-positivity Gram windows in
  a local-QFT-strength observable germ.
- `G`: normalization group acting continuously on observable data.
- `a_k`, `q`, `B_k`, `Delta_phi`: ordinary short-range scalar lattice spacing,
  block kernel, block-spin map, and field scaling exponent.
- `g_k`, `K_k`: local coordinates and polymer activity in the ordinary
  short-range scalar block-spin RG chart.
- `mathbb B_k`, `mathcal P_k`: scale-\(k\) block set and connected polymer
  family used in the constructive polymer RG chart.
- `Gamma_k`, `R_k`: finite-range fluctuation covariance and its range in the
  scale-\(k\) graph distance.
- `E`, `F`, `mathcal L_{\le p}`, `M_{p+1}(r)`: finite-dimensional field
  space, local polymer functional, Taylor-localization map, and derivative
  bound in the finite localization estimate.
- `nu`, `m`, `Delta_phi`, `y_{nu,m}`: number of fields, number of lattice
  differences, field scaling dimension, and canonical local-monomial
  exponent \(D-\nu\Delta_\phi-m\).
- `Gamma`, `kappa`, `C_Gamma(kappa)`: finite Gaussian fluctuation
  covariance, quadratic large-field regulator coefficient, and determinant
  prefactor controlling regulator stability under fluctuation integration.
- `G_k(X,phi)`, `||K_k||_{k,a,h}`: large-field regulator and weighted
  polymer norm for scale-\(k\) activities.
- `mathcal L_k`, `mathcal A_k`: localization map extracting local
  coordinates and fluctuation-integration/rescaling map before reblocking.
- `A_irr`, `alpha`, `B_pol`, `epsilon_k`: linear irrelevant constant,
  scaling-gain exponent, quadratic circle-product constant, and
  local-coordinate extraction defect in the one-step polymer recursion.
- `x_k`, `q`, `r`, `theta`: polymer norm, linear contraction factor
  `A_irr L^{-alpha}`, invariant radius, and contraction margin in the
  finite smallness budget.
- `epsilon_j`, `E`, `sigma`: scale-dependent local-coordinate extraction
  defects and their geometric envelope in the multiscale polymer forcing
  estimate.
- `S_{n,k}`: connected cumulant distribution reconstructed from normalized
  block-spin fields.
- `Phi`, `Psi`: auxiliary-to-short-range RG transfer maps on Banach charts
  and observable-data spaces.
- `d_j`, `delta_j`, `M_j`, `z_j`: one-step transfer defect, its norm bound,
  target RG Lipschitz constant on the comparison tube, and accumulated
  short-range orbit error.
- `tau_aux`, `tau_sr`, `A`, `r`: auxiliary and target unstable tuning maps,
  their linear comparison, and the target tuning remainder.
- `Gamma_f`, `Gamma_c`, `P_e`, `B(A)_e`: finite fine/coarse gauge graphs,
  the chosen fine path assigned to a coarse edge, and the blocked coarse link
  defined by path product of fine links.
- `K_{k,X}`, `||K_k||_zeta`, `rho_k(F,c)`: gauge-blocked polymer activity,
  exponential locality norm, and reflection-positivity defect in the
  gauge-blocking continuum-control datum.
- `Rec_{O,k}`, `Rec_{O,*}`: finite-scale and limiting reconstruction data
  for gauge-invariant Wilson-loop, small-loop, or Wilson-line-connected
  observables.
- RG object / map theorem / source and observable theorem / target
  identification: the four-layer status ledger used to classify
  nonperturbative fixed-point claims without transferring theorem status
  between inequivalent RG systems.

## Claim Ledger

- Defines Gaussian block integration as an exact finite-regulator identity.
- Defines controlled RG maps on Banach spaces and scaling coordinates through
  linearization.
- Proves a local stable-graph theorem for a hyperbolic RG fixed point using
  an explicit Lyapunov-Perron contraction on a complete weighted sequence
  space, with the contraction constant displayed.
- Defines polymer activities, the weighted large-field polymer norm, the
  localization remainder, the quadratic circle-product estimate, and the
  finite one-step contraction budget
  \(x_{k+1}\le qx_k+B_{\rm pol}x_k^2+\epsilon_k\), including the explicit
  radius condition \(q+B_{\rm pol}r+\epsilon_k/r<1\).  The circle-product
  estimate is now derived from a submultiplicative large-field regulator
  bound and a finite pair-overlap majorant
  \(\mathfrak C_a^\circ\), making visible which geometric counting estimate
  a model-specific proof must supply.
- Derives the scale-summed polymer forcing estimate
  \(x_n\le\theta^n x_0+\sum_{j<n}\theta^{n-1-j}\epsilon_j\), including the
  closed geometric envelope for \(\epsilon_j\le E\sigma^j\) and the uniform
  forcing invariant-ball condition \(x_0+E/(1-\theta)\le r\).  The dossier
  records this as deterministic proof infrastructure: a model-specific
  constructive theorem must still prove the input constants from covariance,
  localization, and large-field estimates.
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
- Defines finite-range fluctuation covariance data and proves the exact
  finite-dimensional Gaussian factorization that makes fluctuation
  integration over separated polymer regions independent.  This identifies
  covariance locality or a replacement cluster-decay estimate as a
  load-bearing input to the one-step polymer contraction datum.
- Proves a finite Taylor-localization remainder estimate and derives the
  canonical scaling exponent \(y_{\nu,m}=D-\nu\Delta_\phi-m\) for scalar
  local density monomials.  The chapter now records explicitly that an
  omitted local coordinate enters the irrelevant activity only after the
  first omitted exponent has a positive gap; in canonical \(D=3\) scalar
  bookkeeping \(\phi^6\) is marginal, so it cannot be discarded on
  engineering scaling alone.
- Proves finite Gaussian stability of a quadratic large-field regulator:
  after fluctuation integration the exact determinant prefactor is
  \(C_\Gamma(\kappa)=\det(1-2\kappa\Gamma)^{-1/2}\), and the regulator
  exponent is enlarged by the spectral factor
  \((1-2\kappa\|\Gamma\|_{\rm op})^{-1}\).  The spectral bound, determinant
  constant, and next-scale regulator strengthening are therefore explicit
  proof data for any polymer RG theorem using this norm.
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
- Adds a fixed-point status ledger separating theorem status for
  hierarchical scalar systems, long-range fermionic systems, tensor RG maps,
  ordinary short-range scalar targets, and gauge targets.  The ledger records
  which layers have actually been constructed: RG object, map theorem, source
  and observable theorem, and target identification.
- Adds a finite gauge-compatible blocking construction: coarse links are path
  products of fine links, internal gauge factors cancel, the blocked links
  transform by endpoint conjugation, a fine gauge-invariant measure pushes
  forward to a coarse gauge-invariant measure, and coarse Wilson loops are
  fine Wilson loops along concatenated paths.  The construction is explicitly
  finite-regulator; locality of the blocked action and continuum
  reconstruction remain separate polymer/positivity/reconstruction estimates.
- Defines the gauge-blocking continuum-control datum needed after exact
  finite path blocking: a gauge-invariant polymer representation of the
  blocked measure, an exponential locality norm with a cluster-tail estimate,
  reflection-positivity defect control on the positive-time gauge-invariant
  observable algebra, and reconstruction estimates for gauge-invariant local
  and extended observables.
- Explains the consequences of those estimates without promoting them to a
  theorem-family claim: gauge invariance, quasi-locality, and reflection
  positivity pass to limiting reconstructed observables only after the
  stated estimates have been supplied.
- Gives a precise monograph definition of universality class as an RG
  attraction statement plus reconstruction data.
- Defines a Wilsonian universality datum with microscopic regulators, tuned
  initial points, a Banach RG chart, reconstruction maps, observable topology,
  and normalization group.
- Refines the phrase "universality class" to an equivalence class of
  normalized observable germs in a projective topology of finite observation
  windows, and separates finite-window certificates from theorem-level
  convergence in the full directed family.
- Defines a local-QFT-strength observable germ: the directed observable
  family must include full tempered distribution windows, OS or Wightman
  positivity windows, covariance/locality identities, source contact-term
  data, and reconstruction growth hypotheses before a universality statement
  can be read as equality of reconstructed local QFTs.
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
  observable-germ finite-window certificate.  The same script now checks a
  finite OS-positivity Gram-window failure that is invisible in a declared
  one-coordinate observable window, and it checks the exact finite arithmetic
  behind the polymer contraction budget and the quadratic circle-product
  bound, including a finite interval enumeration of the pair-overlap
  majorant entering \(B_{\rm pol}\).  It also checks the finite-range
  Gaussian factorization, Taylor-localization scaling ledger, and the
  quadratic large-field regulator determinant/exponent bookkeeping.
- `calculation-checks/lattice_gauge_blocking_checks.py`: exact finite \(S_3\)
  checks for gauge-compatible path blocking, including endpoint covariance,
  equality of the blocked coarse Wilson loop with the concatenated fine
  plaquette, class-function gauge invariance, and invariance of the blocked
  pushforward weights under the coarse gauge group.  The script also checks
  the finite arithmetic behind weighted polymer-tail bounds and compression
  of a reflection-positive finite Gram matrix by a blocking map.

## Audit Notes

- 2026-06-01 polymer RG contraction-datum pass: replaced the schematic
  polymer estimate by a finite-regulator datum naming the polymer norm,
  large-field regulator, localization map, irrelevant gain, circle-product
  constant, extraction defect, and smallness budget.  The pass deliberately
  keeps the ordinary short-range critical scalar construction open: proving
  the constants uniformly along a tuned critical trajectory remains the
  model-specific theorem burden of issue #505.
- 2026-06-01 polymer RG multiscale-forcing pass: extended the one-step
  contraction budget to the deterministic sequence estimate
  \(x_n\le\theta^nx_0+\sum_{j<n}\theta^{n-1-j}\epsilon_j\), with geometric
  and uniform forcing envelopes.  This closes a bookkeeping gap between a
  one-step polymer estimate and a scale-uniform trajectory estimate, while
  preserving the open model-specific burden of constructing the constants
  and source extensions for ordinary short-range critical scalar theories.
- 2026-06-02 polymer pair-overlap pass: expanded the circle-product estimate
  in the one-step polymer RG datum into an explicit scalar-majorant
  derivation.  The chapter now defines the pair-overlap constant
  \(\mathfrak C_a^\circ\), displays the submultiplicative regulator input,
  and derives \(B_{\rm pol}=C_G\mathfrak C_a^\circ\).  The companion
  short-range RG check now enumerates connected intervals in a finite
  one-dimensional block line exactly, verifying the finite pair-overlap
  arithmetic that models the geometric counting step.
- 2026-06-02 finite-range covariance locality pass: inserted the missing
  finite-regulator mechanism before the polymer contraction datum.  The
  chapter now defines a finite-range fluctuation covariance datum and proves
  Gaussian factorization for separated field regions from the vanishing
  covariance cross-block.  The companion short-range RG check verifies the
  exact characteristic-exponent splitting and the mixed term produced when a
  covariance tail remains.  This is proof infrastructure for issue #505; it
  does not construct the model-specific finite-range decomposition or the
  uniform estimates for an ordinary short-range critical scalar fixed point.
- 2026-06-02 Taylor-localization scaling pass: added the finite
  Taylor-remainder estimate behind the localization map and the canonical
  local-monomial exponent ledger.  This pass makes the first omitted
  coordinate part of the proof data: the companion short-range RG check now
  verifies the finite Taylor bound and the \(D=4\) versus \(D=3\) scalar
  exponent comparison, including the \(D=3\) \(\phi^6\) marginal caveat.
- 2026-06-02 large-field Gaussian regulator pass: added the exact finite
  Gaussian estimate controlling quadratic large-field regulators under
  fluctuation integration.  The chapter now displays the determinant factor,
  the spectral condition \(2\kappa\|\Gamma\|_{\rm op}<1\), and the exponent
  enlargement that the next-scale regulator must absorb.  The companion
  short-range RG check verifies the same determinant and completing-square
  arithmetic by exact rational calculation.
- 2026-06-02 local-QFT-strength observable-germ pass: inserted the missing
  bridge from projective observable-window universality to equality of a
  reconstructed local QFT.  The new definition requires full distribution
  windows, OS or Wightman positivity windows, covariance/locality identities,
  contact-term data, and growth hypotheses before RG universality is allowed
  to invoke OS or Wightman reconstruction.  The companion short-range RG
  check now exhibits an exact finite hidden-window failure: a visible
  two-point coordinate can agree while an undeclared reflection-positivity
  Gram determinant is negative.
- 2026-06-01 gauge-compatible RG example pass: added the finite path-blocking
  construction as the minimal lattice half of a gauge-compatible Wilsonian RG
  datum and paired it with an exact \(S_3\) calculation check.  The pass
  deliberately does not claim locality of the blocked action or continuum
  reconstruction; those remain the model-specific estimates required by
  issue #505.
- 2026-06-01 gauge-blocking continuum-control pass: added the missing
  locality/positivity/reconstruction estimate layer after finite path
  blocking.  The text now states exactly what must be proved before a
  gauge-compatible blocking construction can be used as evidence for a
  continuum local QFT, and the proof-like closure statements were kept as
  prose consequences rather than inflated into weak propositions.
