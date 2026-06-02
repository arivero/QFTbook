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
- `mathcal X_k`, `T_{k,k-1}`, `Loc_k`: finite-regulator object, exact
  Wilsonian step, and localization map in the Wilsonian RG reconstruction
  problem.
- `Z_{k,E}`, `W_{k,E}`, `E`: finite source-window functional, connected
  source functional, and finite test window in the source-extended part of
  the reconstruction problem.
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
- `alpha=(n,m,ell,p)`, `H_alpha`, `D_sc(alpha)`: fermionic
  source-extended kernel label, corresponding pinned \(L^1\) kernel, and
  kernel scaling exponent in the long-range fermionic benchmark.
- `g`, `K`, `A_loc`, `A_irr`, `B_loc`, `B_irr`: trimmed local coordinates,
  irrelevant kernel tail, and local/irrelevant blocks of the fermionic RG map.
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
- `mathcal E`, `E_infty`, `S_E`, `q_r`: directed finite test-function
  windows, their dense union, compatible window functionals, and the
  Schwartz seminorm used in the projective distribution-window extension
  lemma.
- `N_k`, `S_{k,N}`, `eta_{N,k}`, `k_j`: number of controlled finite windows
  at regulator scale \(k\), regulated window functionals, fixed-window
  Cauchy modulus, and diagonal cofinal scale subsequence in the
  finite-window assembly criterion.
- `G`: normalization group acting continuously on observable data.
- `a_k`, `q`, `B_k`, `B_k^\dagger`, `Delta_phi`: ordinary short-range scalar
  lattice spacing, block kernel, block-spin map, adjoint source-blocking map,
  and field scaling exponent.
- `g_k`, `K_k`: local coordinates and polymer activity in the ordinary
  short-range scalar block-spin RG chart.
- `mathbb B_k`, `mathcal P_k`: scale-\(k\) block set and connected polymer
  family used in the constructive polymer RG chart.
- `Gamma_k`, `R_k`: finite-range fluctuation covariance and its range in the
  scale-\(k\) graph distance.
- `D_vol`, `C_sh`, `A_Gamma`, `s`, `R`: shell-count dimension, shell-count
  constant, covariance-tail amplitude, decay exponent, and polymer-set
  separation in the summable covariance-tail bridge estimate.
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
- `J`, `rho_j`, `s_j`, `R_j(J)`, `eta_j`, `U_{j->N,beta}`: source
  variables, source polydisc radii, retained source degree, source-tail
  functional, source-tail norm, and propagated source-window map in the
  source-extended polymer RG estimate.
- `W_{k,Omega,E}`, `K_{E,k}`, `R_Omega`, `Xi(R)`: finite-volume connected
  source functional, lattice source support, distance from the source window
  to the finite-volume boundary, and boundary-tail function in the
  thermodynamic source-window estimate.
- `S_{n,k}`: connected cumulant distribution reconstructed from normalized
  block-spin fields.
- `Phi`, `Psi`: auxiliary-to-short-range RG transfer maps on Banach charts
  and observable-data spaces.
- `d_j`, `delta_j`, `M_j`, `z_j`: one-step transfer defect, its norm bound,
  target RG Lipschitz constant on the comparison tube, and accumulated
  short-range orbit error.
- `tau_aux`, `tau_sr`, `A`, `r`: auxiliary and target unstable tuning maps,
  their linear comparison, and the target tuning remainder.
- `a_{alpha,k}`, `epsilon_{alpha,k}`, `L_{alpha,k}`, `n_{alpha,k}`:
  auxiliary-window convergence error, auxiliary-to-target observable-window
  defect, short-range reconstruction Lipschitz constant, and normalization
  mismatch in the projective-window transfer estimate.
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
- Defines the Wilsonian RG reconstruction problem as a package of
  finite-regulator objects, exact finite maps, localization into a declared
  normed chart, finite source windows, reconstruction maps, and estimates
  strong enough to control domain stability, irrelevant tails, tuning,
  positivity, distributional growth, and common directed scale schedules.
- Defines controlled RG maps on Banach spaces and scaling coordinates through
  linearization.
- Proves a local stable-graph theorem for a hyperbolic RG fixed point using
  an explicit Lyapunov-Perron contraction on a complete weighted sequence
  space, with the contraction constant displayed.
- Proves a \(C^1\) stable-graph criterion by differentiating the
  Lyapunov--Perron fixed-point equation in the weighted sequence space.  The
  proof identifies the derivative sequence, its contraction bound, and the
  tangency \(Dh(0)=0\); model-specific RG work must still prove the required
  uniform derivative bounds in its chosen norm.
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
- Proves a finite source-window extraction estimate for source-extended
  polymer RG charts: source derivatives retained by the Taylor source-coordinate system
  have zero tail, omitted derivatives obey a Banach-valued Cauchy-radius
  bound, and reconstructed source-window errors are bounded by the
  propagated scale sum
  \(\sum_{j<N}P_{j,N,\beta}\beta!\eta_j/\rho_j^\beta\) over scales whose
  retained source degree is below \(|\beta|\).  This records the condition
  needed to turn a scalar fixed-point trajectory into controlled connected
  correlator windows.
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
- Adds the finite-window observable approximation layer: a projected fixed
  point controls reconstructed observables only after the lift radius,
  reconstruction Lipschitz constants, and projected observable chart errors
  are bounded in the seminorms of the declared observable topology.
- Adds the functional-RG projected-flow residual estimate: a finite ansatz for
  the Wetterich flow controls the exact regulated effective action only when
  the omitted vector-field component \(Q_N\mathcal F_t(\gamma_N(t))\) is
  integrated with the RG amplification factor and then transported through
  observable seminorms.
- Adds the tensor-RG truncation-window estimate: exact and algorithmic tensor
  orbits are compared by a one-step residual
  \(\|\mathcal T_j(\widehat T_j)-\widehat{\mathcal T}_j(\widehat T_j)\|\),
  amplified by the exact tensor-map Lipschitz constants and then transported
  through normalized finite observable windows.
- Adds a model-by-model status synthesis for rigorous Wilsonian RG: massive
  constructive scalar models, auxiliary hierarchical scalar systems,
  long-range fermionic fixed points, tensor RG, functional RG truncations,
  ordinary short-range critical scalar targets, and gauge targets are compared
  by the actual theorem stage reached--map construction, fixed point,
  source-extension, reconstruction, and target identification--so theorem
  status is not transferred between inequivalent RG systems.
- Defines the output data of a constructive fermionic RG fixed point:
  fixed-cutoff Grassmann covariance, Banach kernel space, exact RG map, fixed
  interaction, source-field dimensions \(d-\Delta_i\), operator dimensions
  \(\Delta_i\), response functions, and remainders.
- States the long-range fermionic \(\psi^4_d\) fixed-point theorem as a
  quoted benchmark: a nontrivial fixed interaction, constructed response
  functions, naive field exponent, anomalous analytic density exponent, and
  stretched-exponential cutoff-controlled remainders.
- Expands the fermionic benchmark mechanism: the fixed point lives in a
  trimmed infinite sequence of nonlocal Grassmann kernels, the pinned
  \(L^1\)-scaling exponent is
  \(D_{\rm sc}=d-n(d-\Delta_1)-m(d-\Delta_2)-\ell[\psi]-|p|_1\), the
  mass/quartic/source exceptional local coordinates form the finite trimmed
  block, and the irrelevant tail is solved by a contraction equation rather
  than discarded.
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
- Proves the finite reflection-positive block-spin pullback mechanism:
  if the microscopic finite measure is reflection positive and the block
  kernel maps coarse positive-time fields to fine positive-time fields while
  commuting with reflection, then the blocked finite measure is reflection
  positive on the coarse positive-time polynomial algebra.  The proof is the
  compression of the fine OS Gram form by the block-spin pullback; the
  continuum OS burden remains the directed-family convergence and growth
  estimates.
- Defines the ordinary short-range scalar OS reconstruction requirements:
  infinite-volume prescription, distributional convergence with uniform
  temperedness, covariance/symmetry/Hermiticity, directed reflection-positive
  Gram-window convergence, positive-time semigroup regularity, corrected OS-II
  analytic growth, and the ordered-insertion adjoint identity.  The chapter now
  explicitly separates these estimates from the existence of a Wilsonian fixed
  point or stable trajectory.
- Proves the moving finite-window approximation step needed after cofinal
  assembly: if regulated RG estimates control only \(S_{k,N_k}\) on a
  scale-dependent finite test space, then \(S_{k,N_k}(\Pi_{N_k}f)\) converges
  to the limiting distribution value \(S(f)\) only after the projections
  \(\Pi_N f\) converge in the same seminorm that uniformly bounds the finite
  functionals and the window schedule is cofinal.
- Adds a concrete positive-time translation-window criterion for the OS
  semigroup regularity item: for every positive-time test vector \(F\) with
  time-support margin, the RG construction must bound the finite Gram-window
  norm of \(\tau_tF-F\) by a modulus \(\omega_F(t)\to0\) plus a regulator
  error.  The limiting OS norm and the dense-domain extension then follow
  from the same Gram-window estimates; finite reflection positivity alone
  does not supply this continuity.
- Adds Lemma `lem:rg-positive-time-quotient-semigroup-criterion`, proving the
  quotient step for OS time translations: a positive-time translation map
  descends through the OS null space only after a bound
  \(Q(\tau_tF,\tau_tF)\le C_tQ(F,F)\), and the Gram-continuity estimate then
  gives a strongly continuous semigroup on the Hilbert completion.
- Defines the short-range scalar RG-to-OS assembly package: a tuned polymer RG
  trajectory, fixed-radius source windows, the combined source budget
  \(\delta^C+L_E(\delta^g+\delta^K)+\delta^r+A_E\Xi(R)+\sigma\), uniform
  Schwartz-seminorm distribution bounds, cofinal finite-window compatibility,
  directed OS positivity, quotient-stable time translations, and corrected
  OS-II growth, all on a common directed scale schedule for each finite
  reconstruction demand.  The chapter states this as the theorem-facing
  estimate package needed before applying OS reconstruction, not as an
  already-proved theorem for the ordinary short-range critical scalar target.
- Defines finite-range fluctuation covariance data and proves the exact
  finite-dimensional Gaussian factorization that makes fluctuation
  integration over separated polymer regions independent.  This identifies
  covariance locality or a replacement cluster-decay estimate as a
  load-bearing input to the one-step polymer contraction datum.
- Proves a summable covariance-tail bridge estimate replacing exact
  finite-range factorization when the fluctuation shell has only decay:
  pointwise covariance decay
  \(|\Gamma(x,y)|\le A_\Gamma(1+d(x,y))^{-s}\), \(s>D_{\rm vol}\), and the
  shell-count bound give a Schur operator estimate
  \(A_\Gamma C_{\rm sh}(1+(s-D_{\rm vol})^{-1})(1+R)^{D_{\rm vol}-s}\) for
  the cross covariance between separated polymer supports; Gaussian
  interpolation then bounds the connected bridge between \(C^1\) local
  polymer observables by this cross norm times their derivative seminorms.
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
- Derives the projective-window transfer estimate
  \(n_{\alpha,k}+a_{\alpha,k}+\epsilon_{\alpha,k}
  +L_{\alpha,k}\sum_j(\prod_{\ell>j}M_\ell)\delta_j\), separating auxiliary
  observable convergence, auxiliary-to-target observable comparison, target
  orbit-transfer defects, and normalization mismatch before an auxiliary RG
  theorem can be promoted to an ordinary short-range observable-germ claim.
- Tightens the anti-inflation boundary around auxiliary transfer and
  universality: the orbit telescope is a finite recurrence whose
  load-bearing inputs are the comparison map, tube constants, defects, and
  target reconstruction estimates; pairwise finite-window comparisons with
  unrelated normalizations are not a theorem-level universality relation
  without convergence to a common reconstructed observable germ.
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
  windows, and separates finite-window estimates from theorem-level
  convergence in the full directed family.
- Defines a local-QFT-strength observable germ: the directed observable
  family must include full tempered distribution windows, OS or Wightman
  positivity windows, covariance/locality identities, source contact-term
  data, and reconstruction growth hypotheses before a universality statement
  can be read as equality of reconstructed local QFTs.
- Proves the projective distribution-window extension lemma used by
  local-QFT-strength observable germs: compatible finite test-function
  windows with a single Schwartz-seminorm bound define a unique tempered
  distribution extending all windows.  This identifies the exact bridge from
  finite RG observation windows to a Schwinger distribution eligible for
  OS/Wightman reconstruction tests.
- Proves the cofinal finite-window assembly lemma for regulated RG output:
  compatible finite window functionals \(S_{k,N}\) with \(N_k\to\infty\), a
  uniform \(q_r\)-seminorm bound, and fixed-window Cauchy control define
  compatible limiting windows and hence a tempered distribution by the
  projective extension lemma.  The proof also constructs a diagonal scale
  subsequence \(k_j\) controlling the first \(j\) windows with \(2^{-j}\)
  error.  This is still a functional-analytic assembly step, not the
  model-specific polymer, cluster, or tensor estimate proving the hypotheses.
- Derives the finite OS-positivity Gram-window bound used by a
  reconstruction-strength observable germ: entrywise convergence of every
  finite positive-time test-family Gram matrix preserves positivity in the
  limit, and a regulated lower bound plus an entrywise error gives the
  explicit lower estimate
  \(c^*G_*c\ge(\ell-m\epsilon)\|c\|_2^2\).
- Adds a finite stable-chart observable-window bound: after the
  microscopic data have entered one RG chart, the finite observation-window
  difference is bounded by the relevant mismatch, stable-coordinate
  contraction, accumulated one-step comparison defects, and declared
  source-tail/normalization errors.  The chapter now states the
  projective-limit quantifier order explicitly: after the window-dependent
  constants are fixed, the relevant mismatch must vanish, the defect
  convolution must have a summable tail, the source/normalization error must
  go to zero, and a cofinal schedule of window depths and regulator tails
  must outpace any growth of the window constants.  Thus finite-window
  universality evidence becomes a checkable RG error budget, not a disguised
  theorem about the full observable germ.
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
- Derives the quantitative finite-dimensional tuning estimate used after a
  microscopic transverse chart is fixed: normalized residual
  \(\|A^{-1}e\|\), derivative-variation bound
  \(\sup\|A^{-1}(DF-A)\|\), and the contraction of the frozen-Newton map on a
  declared ball.  This is the finite-regulator step that solves the relevant
  coordinate equation once the stable graph and transversality estimates have
  already been supplied.

## Figure Ledger

No figure is included in this pass.  A later diagram should show covariance
decomposition, block integration, projection to local coordinates, and polymer
remainder contraction.

## Companion Scripts

- `calculation-checks/rg_projection_checks.py`: exact rational check for the
  finite-dimensional projected-zero counterexample and complement-residual
  lift calculation, the residual-lift plus finite-window observable-error
  budget, the finite-step projected functional-RG residual-amplification
  bound, the tensor-RG truncation-window recursion, and the finite
  irrelevant-tail graph equation.
- `calculation-checks/rg_fermionic_fixed_point_checks.py`: exact rational
  checks for the fermionic benchmark kernel scaling ledger, pinned \(L^1\)
  exponent relation, trimmed local-coordinate list, and finite irrelevant-tail
  graph equation.
- `calculation-checks/rg_hierarchical_scalar_checks.py`: exact rational
  checks for the hierarchical scalar Gaussian Wick-coordinate eigenvalue,
  engineering exponents, and relevance bookkeeping.
- `calculation-checks/rg_short_range_reconstruction_checks.py`: exact rational
  checks for ordinary short-range scalar block-spin normalization, pairing,
  covariance scaling, reconstruction-bound arithmetic, and
  correction-to-scaling bookkeeping, plus the auxiliary-transfer telescoping
  estimate, relevant-direction amplification formula, non-diagonal unstable
  Jordan-block finite-depth tuning loss, differentiated Lyapunov--Perron
  \(C^1\) stable-graph formula, and projective
  observable-germ finite-window estimate.  The same script now checks the
  projective distribution-window extension lemma: restriction
  compatibility, induced finite functional value, a single seminorm bound,
  and the exact defects produced by incompatible windows or a failed declared
  bound.  It also checks the cofinal finite-window assembly step by verifying
  finite-scale restriction compatibility, a uniform \(l^1\)-seminorm dual
  bound, the \(k_j=2^j\) diagonal error estimate, the limiting functional
  value, and the failure of a noncofinal window schedule.  It also checks a
  finite OS-positivity Gram-window failure that is
  invisible in a declared one-coordinate observable window, and now checks
  the reflection-positive block-spin pullback compression \(B^TG_{\rm fine}B\)
  and the finite OS-positivity bound with an explicit regulated lower bound
  and entrywise limiting error, together with the all-ones family-size
  obstruction showing why fixed entrywise error cannot prove directed
  reflection positivity.  It also checks the combined RG-to-OS assembly
  budget that feeds source-window convergence and directed OS positivity into
  reconstruction.  It also checks the positive-time translation-window
  arithmetic behind OS semigroup continuity: support margin, quadratic
  modulus, regulator-error limit, null-quotient stability condition, and
  dense-domain extension.  It also checks
  the exact finite arithmetic behind the polymer
  contraction budget and the quadratic circle-product bound, including a
  finite interval enumeration of the pair-overlap majorant entering
  \(B_{\rm pol}\).  It also checks the finite-range
  Gaussian factorization, the summable covariance-tail bridge estimate,
  Taylor-localization scaling ledger, and the quadratic large-field regulator
  determinant/exponent bookkeeping.  It also checks source-window extraction
  for a source-extended polymer chart,
  including retained-derivative vanishing, omitted third-derivative Cauchy
  bounds, and propagated scale-summed source-tail errors.  It also checks
  the stable-chart finite-window bound, decomposing the observable
  error into relevant, stable, defect, and source-tail pieces.
- `calculation-checks/lattice_gauge_blocking_checks.py`: exact finite \(S_3\)
  checks for gauge-compatible path blocking, including endpoint covariance,
  equality of the blocked coarse Wilson loop with the concatenated fine
  plaquette, class-function gauge invariance, and invariance of the blocked
  pushforward weights under the coarse gauge group.  The script also checks
  closed-loop source-window descent to coarse gauge orbits, the failure of an
  open-link source to define an invariant window, the finite arithmetic
  behind weighted polymer-tail bounds, a nondecaying tail failure mode,
  compression of a reflection-positive finite Gram matrix by a blocking map,
  and the finite reconstruction error budget \(C\varepsilon+\eta\).

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
- 2026-06-02 covariance-tail bridge pass: added the quantitative replacement
  for exact finite-range factorization when a fluctuation covariance has only
  summable decay.  The chapter now derives the Schur operator bound from a
  shell-count estimate and pointwise covariance decay, then uses Gaussian
  interpolation to control the connected bridge between separated polymer
  observables.  The companion short-range RG check verifies the shell-tail,
  Schur, and connected-bound arithmetic exactly.  This narrows the analytic
  input for smooth momentum-shell or exponentially decaying covariance
  decompositions, while leaving the model-specific construction of uniform
  covariance and polymer estimates open.
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
- 2026-06-02 short-range RG-to-OS assembly pass: added
  Definition~\(\ref{def:short-range-rg-to-os-assembly-datum}\), which gathers
  the source-window, thermodynamic, cofinal-window, distributional bound,
  directed OS positivity, quotient semigroup, and OS-II requirements into the
  precise estimate package needed before a model-specific short-range scalar
  RG proof can invoke OS reconstruction.  The companion check verifies the
  combined source-budget-to-cumulant arithmetic and the finite directed OS
  lower-bound schedule.  The pass does not claim that the ordinary
  three-dimensional critical scalar target has been constructed; it makes the
  remaining model-specific proof obligations explicit.
- 2026-06-02 source-window extraction pass: added the finite source-extension
  estimate needed for RG reconstruction of connected correlator windows.  The
  chapter now states that retaining source degree \(s\) controls source
  derivatives only through degree \(s\), and that omitted source derivatives
  require a Cauchy-radius bound plus a propagated scale sum.  The companion
  short-range RG check verifies the retained-tail vanishing, omitted
  derivative, Cauchy majorant, and propagated bound by exact rational
  arithmetic.
- 2026-06-02 local-QFT-strength observable-germ pass: inserted the missing
  bridge from projective observable-window universality to equality of a
  reconstructed local QFT.  The new definition requires full distribution
  windows, OS or Wightman positivity windows, covariance/locality identities,
  contact-term data, and growth hypotheses before RG universality is allowed
  to invoke OS or Wightman reconstruction.  The companion short-range RG
  check now exhibits an exact finite hidden-window failure: a visible
  two-point coordinate can agree while an undeclared reflection-positivity
  Gram determinant is negative.
- 2026-06-02 finite OS-positivity Gram-bound pass: added the concrete
  finite Gram-window mechanism that a reconstruction-strength observable
  germ must control.  The chapter now derives passage of OS positivity to the
  limiting Gram matrix and gives the quantitative
  \((\ell-m\epsilon)\)-lower bound.  The anti-inflation audit now stresses
  the real directed-family burden: for an expanding family of \(m\) test
  vectors, an entrywise estimate must scale like \(O(1/m)\), or be replaced by
  an operator-norm estimate, before it can support OS reconstruction.  The
  companion short-range RG check verifies the same rational arithmetic on an
  explicit finite window.
- 2026-06-02 positive-time translation-window pass: added the concrete
  Gram-window equicontinuity estimate needed for item 5 of the short-range
  scalar OS reconstruction requirements.  The chapter now derives strong
  continuity of the OS time-translation semigroup from a bound on
  \(S_k(\Theta(\tau_tF-F)(\tau_tF-F))\) with a vanishing modulus and regulator
  error, and records the dense-domain extension burden.  The companion
  short-range RG check verifies the support-margin, quadratic-modulus,
  limiting-window, and dense-domain extension arithmetic.  This is still
  proof infrastructure for #505; it does not construct the model-specific
  short-range critical scalar RG estimates.
- 2026-06-02 OS quotient-semigroup pass: inserted the quotient-stability
  criterion needed before translated positive-time tests define operators on
  the OS Hilbert quotient.  The new lemma proves that
  \(Q(\tau_tF,\tau_tF)\le C_tQ(F,F)\) sends null vectors to null vectors,
  gives a bounded quotient operator, and combines with the Gram-continuity
  estimate to yield a strongly continuous semigroup.  The companion
  short-range RG check verifies the finite null-space obstruction and a
  quotient-stable map.
- 2026-06-02 stable-chart finite-window bound pass: added the
  RG-coordinate error budget behind finite universality evidence.  The
  chapter now bounds a finite reconstructed window by a tuned relevant
  mismatch, a stable contraction term, accumulated one-step defects, and
  source-tail/normalization errors.  The companion short-range RG check
  verifies the same recurrence and observable-bound arithmetic exactly.
- 2026-06-02 directed-window quantifier pass: sharpened the finite
  stable-chart bound into its theorem-facing quantifier order.  For every
  observation window and tolerance, the constants are fixed first and then a
  depth/regulator tail must make the relevant mismatch, stable contraction,
  defect convolution, and source-tail terms small.  For cofinal windows the
  schedule must be compatible with the projective system and with any growth
  of window constants.  This addresses issue #505's anti-inflation concern
  by making clear that a finite window estimate is not a full Wilsonian
  universality theorem.
- 2026-06-02 \(C^1\) stable graph pass: upgraded the critical-surface
  analytic infrastructure by proving a self-contained differentiability
  criterion for the Lyapunov--Perron stable graph.  The companion short-range
  RG check verifies the differentiated stable-graph formula in an exact
  one-dimensional nonlinear model.
- 2026-06-02 projective distribution-window extension pass: added the
  missing functional-analytic bridge from compatible finite Schwinger
  distribution windows to an actual tempered distribution.  The proof now
  separates the algebraic compatibility step from the uniform
  Schwartz-seminorm continuity estimate, and the companion short-range RG
  check verifies the same finite restriction and boundedness arithmetic.
- 2026-06-02 auxiliary projective-window transfer pass: added the
  finite-window estimate needed before an auxiliary fixed-point theorem
  can be read as a statement about the ordinary short-range observable germ.
  The bound now separates auxiliary-window convergence, auxiliary-to-target
  observable comparison, target orbit-transfer defects, and normalization
  mismatch.  The companion short-range RG check verifies the exact rational
  telescope and shows explicitly that nondecaying transfer defects leave a
  positive error floor.
- 2026-06-02 auxiliary-transfer anti-inflation pass: tightened the prose
  around the same recurrence so the finite iteration is not presented as the
  substantive theorem.  The manuscript now identifies the model-specific
  burden as construction of the comparison map, common target tube, constants
  \(M_j\), defects \(\delta_j\), and target reconstruction estimates, and
  explains that pairwise universality comparisons with incompatible
  normalizations do not replace convergence to a common observable germ.
- 2026-06-02 reflection-positive block-spin pass: added the finite
  positivity-preservation mechanism missing from the ordinary short-range
  scalar block-spin datum.  The chapter now proves that a
  reflection-compatible block kernel pulls coarse positive-time polynomials
  back into the fine positive-time algebra and therefore sends fine OS Gram
  positivity to coarse OS Gram positivity by compression.  The companion
  short-range RG check verifies the same finite matrix compression and
  determinant arithmetic.  This remains finite-regulator proof
  infrastructure; it does not replace the directed Gram-window convergence
  and OS-II growth estimates needed for continuum reconstruction.
- 2026-06-02 adjoint source-blocking pass: inserted the missing
  source-normalization derivation for the ordinary short-range scalar
  reconstruction datum.  The chapter now defines
  \((B_k^\dagger F)(y+a_kr)=L^Dq(r)F(y)\), derives the exact equality of
  coarse source pairing with fine pulled-back source pairing, and gives the
  uniform-kernel \(C^1\) smooth-test sampling estimate that separates exact
  RG source pullback from pointwise approximation of continuum tests.  The
  companion short-range RG script checks the nonuniform-kernel \(L^D\)
  factor and the uniform-kernel sampling constant by exact rational
  arithmetic.
- 2026-06-02 quantitative tuning pass: added the finite-dimensional
  contraction estimate needed to turn microscopic transversality into an
  actual solution of the relevant-coordinate tuning equation in a declared
  ball.  The text presents this as proof infrastructure, not as a new RG
  theorem: the stable graph, parameter chart, residual bound, and derivative
  variation estimate remain the model-specific burden.  The companion
  short-range RG script checks the normalized residual, contraction constant,
  ball-map bound, sample contraction inequality, and a residual failure mode
  by exact rational arithmetic.
- 2026-06-02 short-range scalar OS reconstruction-requirements pass: inserted the missing
  reconstruction-level dependency chain for the ordinary short-range scalar
  target.  The manuscript now states that a critical short-range scalar
  Wilsonian RG construction must supply an infinite-volume prescription,
  distributional Schwinger convergence with uniform temperedness, all
  Euclidean identities, directed OS Gram positivity, positive-time semigroup
  regularity, corrected OS-II analytic growth, and the ordered-insertion
  adjoint identity before Theorem~\ref{thm:os-reconstruction} may be invoked.
  This pass deliberately does not claim existence of the Wilson-Fisher fixed
  point; it sharpens issue #505 by identifying exactly what remains to be
  proved in a model-specific construction.
- 2026-06-02 anti-inflation follow-up: renamed the visible generic prose in the
  ordinary short-range scalar OS passage to reconstruction requirements.  The
  label is retained for cross-reference stability, but the reader-facing
  language now emphasizes the actual estimates and directed Gram-window/growth
  requirements rather than a generic package name.
- 2026-06-02 short-range scalar common-schedule pass: sharpened the
  model-by-model RG synthesis and the short-range RG-to-OS assembly datum by
  adding the common directed scale schedule.  Source-window convergence,
  directed OS Gram positivity, positive-time semigroup estimates, and OS-II
  growth must hold on the same cofinal regulator tail for each finite
  reconstruction demand before the OS theorem can be invoked.  The companion
  short-range RG check now verifies the finite max-threshold arithmetic and
  detects a premature scale choice that leaves Gram and OS-II inputs outside
  the proven tail.
- 2026-06-02 finite OS family-size obstruction pass: added the exact companion
  check for the load-bearing \(m\epsilon\) loss in entrywise Gram-window
  control.  The calculation uses \(G_k=\ell I_m\) and
  \(G_\ast=\ell I_m-\epsilon J_m\), so the all-ones vector gives
  \(m(\ell-m\epsilon)\).  It confirms that fixed entrywise tolerance cannot
  support directed OS positivity as \(m\) grows, while a genuine operator-norm
  estimate has the separate \(\ell-\epsilon_{\rm op}\) lower bound.
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
- 2026-06-02 fermionic benchmark mechanism pass: expanded the long-range
  fermionic quoted benchmark so the reader sees the invariant kernel-space
  mechanism rather than only a theorem citation.  The chapter now defines the
  source-extended kernel labels, records that \(\Delta_i\) are operator
  dimensions while the source fields scale with \(d-\Delta_i\), derives the
  pinned \(L^1\)-scaling exponent, names the trimmed local sector, and writes
  the local/irrelevant fixed-point equation whose contraction is the
  nonperturbative burden.  The companion fermionic RG check verifies the exact
  finite arithmetic behind this ledger.
- 2026-06-02 finite source-window cumulant pass: inserted the missing bridge
  from holomorphic finite source-window convergence to the cumulant
  distributions used in the ordinary short-range scalar OS reconstruction
  pipeline.  The manuscript now defines \(W_{k,E}(z)\), identifies
  \(\partial_z^\beta W_{k,E}(0)\) with the corresponding joint cumulant,
  derives the polydisc Cauchy bound
  \(\beta!\epsilon_{E,k}/\rho^\beta\), records restriction compatibility for
  \(E\subset F\), and states the separate uniform Schwartz-seminorm bound
  needed to invoke the projective distribution-window extension lemma.  The
  companion short-range RG check verifies this finite arithmetic and detects
  both restriction and declared-bound failures.
- 2026-06-02 finite-volume source-window pass: added the thermodynamic
  source-window estimate at fixed lattice spacing.  The manuscript now states
  that finite-volume connected source functionals \(W_{k,\Omega,E}\) must be
  holomorphic on a common polydisc and satisfy a boundary cluster-tail bound
  \(A_E\Xi(R_\Omega)\); Cauchy's formula then gives the cumulant derivative
  bound \(\beta!A_E\Xi(R_\Omega)/\rho^\beta\), making finite-volume windows
  Cauchy as the boundary recedes from the source support.  The text also
  records cofinal-exhaustion independence through a common larger region and
  warns that numerical local stability without such a tail estimate is not a
  thermodynamic Schwinger-window construction.  The companion short-range RG
  check verifies the tail-to-derivative and cofinal-comparison arithmetic.
- 2026-06-02 finite-volume cofinal/joint-limit tightening: expanded the
  thermodynamic source-window paragraph to display the common-larger-region
  bound for two cofinal exhaustions and the joint RG-plus-boundary estimate
  \(\epsilon^{\rm RG}_{E,k}+A_E\Xi(R_{\Omega_k})\).  The companion
  short-range RG check now verifies the exact rational joint holomorphic and
  derivative bounds and detects a stagnant boundary-tail schedule.
- 2026-06-02 source-window polymer-bridge pass: inserted the missing
  criterion turning a connected source-cluster expansion into the
  thermodynamic boundary-tail bound.  The lemma assumes absolute convergence
  of connected clusters meeting the source support and a bridge majorant
  \(\sum_{\mathcal C\ni b}\sup |w_{\mathcal C}|\le
  B_E e^{-\zeta d(b,K)}\); summing over boundary blocks and source-centered
  shells gives \(A_E\Xi(R)=B_EC_E\sum_{n\ge R}
  (1+n)^{D_E-1}e^{-\zeta n}\).  The companion check verifies the shell-tail
  arithmetic, a controlled boundary-cluster sum, and a bad shell-growth
  failure mode.
- 2026-06-02 source-chart-to-window pass: inserted the missing Wilsonian
  source-extension bridge between convergence of RG coordinates and
  convergence of the actual holomorphic source functional.  The manuscript now
  decomposes \(W_{k,E}\) on a fixed polydisc into a local normalizing
  coordinate \(C_{k,E}\), retained local source coordinates \(g_{k,E}\), a
  source-decorated polymer tail \(K_{k,E}\), and a finite-step remainder
  \(r_{k,E}\), then records the Lipschitz estimate that yields the uniform
  source-window bound needed before Cauchy extraction.  The text also marks
  fixed source-radius control as load-bearing.  The companion short-range RG
  check verifies the resulting finite inequality and the shrinking-radius
  failure mode.
- 2026-06-02 source-stable trajectory pass: added the source-window analogue
  of stable-manifold tuning.  The manuscript now splits
  \(g_{k,E}-g_{\ast,E}\) into source-local unstable coordinates \(u_{k,E}\)
  and stable/irrelevant coordinates \(s_{k,E}\), records the stable
  telescoping bound and the unstable finite-depth amplification bound, and
  feeds both into the holomorphic source-window error
  \(\epsilon_{E,N}^{\rm src}\).  This makes source-local contact coordinates
  part of the theorem-facing RG chart rather than after-the-fact additions to
  correlators.  The companion short-range RG check verifies the exact finite
  arithmetic and detects the mistuned unstable-source-coordinate failure
  mode.
- 2026-06-02 gauge-invariant source-window pass: added the missing
  gauge-theory source layer to the gauge-compatible RG section.  The
  manuscript now defines finite gauge-invariant source windows for closed
  Wilson-loop and Wilson-line-contracted observables, states the BV version
  as a QME-compatible holomorphic source family with contact/source
  coordinates, and records the invariant source-chart bound needed before
  Cauchy extraction of gauge-observable cumulants.  The companion finite
  \(S_3\) gauge-blocking check verifies that closed-loop class-function
  sources descend to coarse gauge orbits and that an open-link source fails
  the same invariance test.
- 2026-06-02 gauge-blocking reconstruction-budget check pass: extended the
  finite \(S_3\) companion to cover all three interfaces of the
  gauge-blocking continuum-control datum.  Besides gauge covariance and
  source descent, it now detects a nondecaying polymer-tail failure mode,
  retains the reflection-positive Gram compression check, and verifies the
  reconstruction estimate \(p(\operatorname{Rec}_{O,k}-\operatorname{Rec}_{O,*})
  \le C_{O,p}\varepsilon_k+\eta_{O,p,k}\) with a finite example where the
  residual \(\eta\) is necessary.
- 2026-06-02 cofinal finite-window assembly pass: added the diagonal
  assembly lemma needed when RG estimates produce regulated finite-window
  functionals rather than limiting distribution windows directly.  The
  manuscript now requires \(N_k\to\infty\), finite-scale compatibility, a
  regulator-uniform \(q_r\)-seminorm bound, and fixed-window Cauchy control
  before invoking the projective distribution-window extension lemma.  The
  proof constructs the limiting compatible windows and a diagonal subsequence
  \(k_j\) controlling the first \(j\) windows.  The companion short-range RG
  check verifies the finite restriction, seminorm, diagonal-error, limiting
  functional, and noncofinal-schedule arithmetic exactly.
- 2026-06-02 moving finite-window approximation pass: added
  Lemma~\(\ref{lem:rg-moving-window-fixed-test-approximation}\), which closes
  the diagonal step from scale-dependent finite approximants
  \(S_{k,N_k}(\Pi_{N_k}f)\) to the limiting distribution value \(S(f)\).
  The proof separates fixed-window convergence, projection-tail control in
  the same seminorm, and cofinality of \(N_k\).  The companion short-range RG
  check verifies the finite rational error decomposition and detects the
  noncofinal missed-tail failure mode.
- 2026-06-02 directed OS-positive form assembly pass: strengthened the
  ordinary short-range scalar reconstruction pipeline after the finite
  Gram-matrix lower bound.  The manuscript now proves that compatible
  positive-time finite Gram forms \(Q_{k,N}\), cofinal in the directed
  positive-time test family and Cauchy on every fixed finite window, assemble
  into a unique positive algebraic OS form on the dense positive-time union.
  The text explicitly separates this algebraic positivity step from the
  further OS continuity, semigroup-regularity, and OS-II growth estimates.
  The companion short-range RG check now verifies both the bad fixed
  entrywise-error schedule and a safe \(m\)-dependent schedule, plus the
  finite restriction/Cauchy arithmetic behind the directed form assembly.
- 2026-06-02 OS-II source-majorant bridge pass: added the missing estimate
  layer between fixed source-window cumulant convergence and the corrected
  OS-II linear-growth hypothesis.  The manuscript now distinguishes the
  connected source functional \(W_{k,E}\) from the moment source functional
  \(Z_{k,E}\), states a uniform holomorphic majorant on
  insertion-dependent polydiscs, derives the Cauchy moment bound, and records
  the projective tensor seminorm comparison needed to obtain
  \(B_{\rm OS}=C_\pi B/\rho\) in the OS-II growth estimate.  The companion
  short-range RG check verifies the exact rational bookkeeping and detects
  shrinking source radius as a failure mode.
- 2026-06-02 connected-to-moment OS-II pass: inserted the missing
  moment--cumulant partition bridge after the source-majorant paragraph.  The
  chapter now proves that uniform connected-cumulant bounds
  \(A_{\rm c}C_{\rm c}^{|B|}(|B|!)^{\gamma_{\rm c}}\) imply Schwinger moment
  bounds with base \(2C_{\rm c}\max(1,A_{\rm c})\) and factorial exponent
  \(\gamma_{\rm c}+1\), provided the constants are uniform in the insertion
  number and in the declared OS-II seminorm order.  The pass makes explicit
  that connected source estimates alone do not feed OS reconstruction if the
  cluster-count constants or source radii grow with \(n\).  The companion
  short-range RG check enumerates set partitions exactly and detects hidden
  cluster-count growth as a failure mode.
- 2026-06-02 model-by-model rigorous-RG synthesis pass: added the status
  synthesis in the fixed-point claim-content section.  The text now separates
  theorem outputs for massive constructive scalar models, hierarchical and
  auxiliary scalar systems, long-range fermionic fixed points, tensor RG,
  functional RG truncations, ordinary short-range critical scalar targets, and
  gauge targets according to the stage actually proved: map theorem,
  fixed-point or trajectory theorem, source theorem, reconstruction theorem,
  and target-identification theorem.  This addresses the #505 model-synthesis
  gap without promoting benchmark systems to ordinary short-range or gauge
  QFT fixed-point theorems.
- 2026-06-02 Wilsonian reconstruction architecture pass: added
  Definition~\(\ref{def:wilsonian-rg-reconstruction-problem}\) at the chapter
  entrance.  The definition makes explicit that the monograph's rigorous
  Wilsonian RG program begins with exact finite-regulator maps and reaches QFT
  only after localization, source-window, positivity, distributional-growth,
  and reconstruction estimates are supplied.  It prevents beta functions,
  functional-RG truncations, and tensor numerics from being read as standalone
  continuum-QFT constructions.
- 2026-06-02 unstable-block finite-depth tuning pass: sharpened the
  relevant-coordinate tuning discussion beyond a diagonal unstable
  linearization.  The chapter now defines
  \(M_A(N)=\max_{0\le n\le N}\|A^n\|\), records the sufficient finite-depth
  tuning condition \(\|u_0\|\le \rho/M_A(N)\), displays the Jordan-block power
  formula with its polynomial \(N^{m-1}\) loss, and writes the exact
  variation-of-constants sum for one-step relevant-coordinate errors.  The
  companion short-range RG check verifies the \(2\times2\) Jordan-block
  arithmetic and detects the failure of a diagonal-only tuning estimate.
