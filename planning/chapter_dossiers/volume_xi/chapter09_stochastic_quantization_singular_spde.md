# Chapter 09: Stochastic Quantization And Singular SPDE

## Source Position

Volume XI now adds stochastic quantization and singular SPDE constructions as
a route between Euclidean constructive fields, renormalized dynamics, and OS
data.

## Notation Inventory

- `S`, `L`: finite-dimensional action and Langevin generator.
- `C_Lambda`, `xi_Lambda`: ultraviolet covariance cutoff and regularized
  white noise.
- `phi_Lambda`, `lambda_Lambda`, `c_Lambda`: regularized field and local
  coordinates of the scalar theory.
- `rho_epsilon`, `phi_epsilon`: mollifier and mollified field.
- `C_epsilon`: Gaussian contraction in Wick powers.
- `X`, `Y`: Ornstein-Uhlenbeck stochastic convolution and
  Da Prato--Debussche remainder.
- `X_k`, `e_k`: Fourier modes of the stationary stochastic convolution on
  \(\mathbb T^2\).
- `P_N`, `C_N`: Fourier cutoff and cutoff covariance for Wick powers.
- `(A,T,G)`, `Pi_z`, `Gamma_zz'`: regularity structure, model maps, and
  reexpansion maps.
- `C_{1,epsilon}`, `C_{2,epsilon}`: one-loop and two-loop local SPDE
  counterterm constants in the displayed BPHZ convention.
- `Xi`, `X`, `mathcal I`: noise symbol, stochastic convolution symbol, and
  heat-integration map in the dynamic \(\Phi^4_3\) homogeneity ledger.
- `Y`: first nonlinear response \(\mathcal I(X^3)\) in the drift-level
  negative homogeneity ledger for dynamic \(\Phi^4_3\).
- `e_n`, `M`, `C_1(M)`, `S_r`: Fourier mode, sharp spatial cutoff, one-loop
  local coordinate, and \(\ell^\infty\)-shell used in the explicit
  one-loop growth calculation.
- `K_M`, `G_M`, `C_2(M)`, `B_l`, `P_l`: sharp Fourier-cutoff heat kernel,
  covariance, two-loop local coordinate, dyadic annuli, and lower-bound
  boxes used in the logarithmic two-loop growth estimate.
- `D_N`, `M_N`, `C_m^{shell}`: two-loop cutoff domains, dyadic momentum
  cutoffs, and uniform shell-increment constant in the \(C_2\) dyadic shell
  estimate.
- `K_epsilon`, `G_epsilon`: cutoff retarded heat kernel and covariance used
  in the finite-cutoff local counterterm calculation.
- `mathcal L`: projection to the local linear part of a finite-cutoff Wick
  contraction after removing nested one-loop subdivergences.
- `E_T`, `F_T`: Banach spaces of modelled distributions and forcing terms
  on a parabolic time slab in the abstract fixed-point theorem.
- `mathcal K_T`, `Psi_T`: zero-initial-time abstract heat integration
  operator and the associated nonlinear fixed-point map.
- `c_fin`: finite mass coordinate in the renormalized dynamic
  \(\Phi^4_3\) equation.
- `mu`: invariant Euclidean measure of the Markov process.
- `X_mathbb`: enhanced Da Prato--Debussche noise
  \((X,:X^2:,:X^3:)\).
- `kappa`, `beta`: Sobolev exponents in the self-contained DPD proof, with
  \(0<\kappa<1/4\) and \(\beta=1+2\kappa\).
- `mathcal N(Y,X_mathbb)`: DPD renormalized cubic nonlinearity
  \(Y^3+3Y^2X+3YX^{(2)}+X^{(3)}\).
- `Psi`: mild fixed-point map for the DPD remainder equation.
- `X_1,X_2,X_3`: smooth enhanced-noise placeholders in the DPD energy
  estimate.
- `P_t^(n), P_t`: cutoff and limiting Markov semigroups in the invariant-law
  passage lemma.
- `R F`: reconstruction of a modelled distribution.
- `N_n`, `D_n`, `d_{K;gamma}`: random model seminorm, dyadic increment, and
  model distance used in the random-model Cauchy criterion.
- `Z_n`, `Z_infty`: cutoff random models and their limiting model on a finite
  regularity sector.
- `H`, `xi`, `I_q(f)`: Hilbert space, isonormal Gaussian process, and
  \(q\)-fold Wick multiple integral in the finite Wiener-chaos estimate.
- `E`, `E'`, `H^{odot q} \widehat\otimes_\pi E'`: Banach test-function
  space, its dual, and the projective tensor space used to turn
  distribution-valued chaos kernels into dual-norm coordinate estimates.
- `S`, `f_x`, `ell_x`, `delta_u`: kernel parameter space, Hilbert-valued
  deterministic chaos kernel, dual test-function functional, and point
  evaluation functional in the projective kernel criterion.
- `Y_n(a)`, `sigma(a)`: model-coordinate random variable and deterministic
  scale weight in the kernel-to-coordinate moment corollary.
- `Q`, `K_i`, `L_i`, `M_k`: homogeneous dimension, dyadic input kernels, and
  output convolution scale in the parabolic convolution estimate.
- `a`, `b`: kernel orders in the dyadic parabolic convolution bound.
- `psi_x^varphi`, `theta`, `C(u,v)`: rescaled physical test kernel, Holder
  edge exponent, and stochastic-convolution covariance in the Gaussian
  negative-coordinate scale theorem.
- `e_lambda`, `Lambda_j`, `s`, `||.||_{-s,*}`: parabolic wavelets, their
  unit-domain scale sets, the auxiliary Sobolev exponent, and the weighted
  wavelet norm used to dominate the \(E_r'\) dual norm of Gaussian
  coordinates.
- `F`, `P`, `H`, `r`: local factor, subtracted polynomial, remainder
  coefficient, and parabolic remainder order in the Taylor-subtraction gain.
- `mathcal X_l`, `pi_l`, `mathcal E_l`: finite dyadic nets, projections to
  the nets, and edge sets used to pass from pointwise coordinate moments to a
  compact supremum.
- `C_0`, `C_1`, `d`, `epsilon`: base-net size, edge entropy constant,
  entropy exponent, and excess moment-decay exponent in the dyadic-net
  supremum theorem.
- `m`, `D`, `sigma`: physical testing-scale index, scale-entropy exponent,
  and regularity slack in the scale-summed coordinate supremum theorem.
- `I`, `U_{n,i}`, `V_{n,i}`, `A_ctrl`: finite coordinate index set,
  uniform coordinate fields, cutoff-increment coordinate fields, and the
  deterministic constant controlling model seminorms and distances by
  coordinate suprema.
- `S_i`, `tilde S_i`: explicit dyadic-net constants for uniform coordinate
  bounds and cutoff-increment coordinate bounds in the coordinate-to-model
  convergence theorem.
- `D_i`, `epsilon_i`: coordinate-wise entropy exponent and excess
  increment-decay exponent in the coordinate-to-model theorem.
- `R`, `eta_h`, `eta_*`, `G`, `tilde G`: number of sector-gap variables,
  positive scale deficits, minimal deficit, full geometric factor, and shell
  geometric factor in the multiscale sector summability theorem.
- `f_{r,a,q}`, `f_{n,a,q}`: sector kernel contribution and finite-cutoff
  kernel entering the chaos expansion of a model coordinate.
- `T_{i,j}^{loc}`, `T_{i,j}^{off}`: one-loop local-subtraction and
  off-diagonal scale-sector integrals used as the first concrete BPHZ
  relative-scale estimate.
- `a`, `b`, `theta`, `V_A`: kernel orders, Holder exponent, and parabolic
  ball-volume constant in the one-loop relative-scale proposition.
- `S_{i,j,l}`, `n_*`, `r_K,r_L,r_M`, `eta_K,eta_L,eta_M`: non-nested
  two-loop sunset scale block, maximal dyadic scale, relative scale gaps,
  and gap exponents in the two-loop sector proposition.
- `C_{1,l}`, `G_l(0)`: fixed-scale tadpole coordinate used to prove
  scale-wise cancellation of the nested two-loop local coefficient.
- `gamma_-`, `T_-`, `P_{n,tau}`, `G_n`, `c_n(z,z')`: strict negative-sector
  cutoff, finite dynamic \(\Phi^4_3\) model sector, normalized
  \(\Pi\)-coordinates, normalized \(\Gamma\)-coordinate, and the constant
  reexpansion coefficient of \(Y=\mathcal I(X^3)\).
- `mathfrak C`, `Q_{n,i}`, `Delta Q_{n,i}`, `S_i^{sc}`,
  `tilde S_i^{sc}`, `N_n^-`, `D_n^-`: the seven-coordinate strict
  negative-sector index set, uniform and cutoff-increment coordinate
  functions, scale-summed constants, negative-sector model seminorm, and
  negative-sector model-distance increment.
- `Q_{n,tau}^{#}`, `mathcal X_{Pi,m}`, `mathcal X_{Gamma,m}`, `d_Pi`,
  `d_Gamma`:
  test-function-dualized \(\Pi\)-coordinates, physical scale-ratio parameter
  spaces, normalized-separation parameter spaces, and their entropy exponents.

## Claim Ledger

- Proves the finite-dimensional invariant-measure identity for Langevin
  dynamics.
- Defines a regularized stochastic field equation as a gradient flow plus
  noise.
- Derives the Wick subtraction in the cubic drift from Gaussian contractions.
- Constructs the stationary two-dimensional stochastic convolution in
  Fourier modes with the noise normalization
  \(\mathbb E\xi\xi=2\delta\delta\), proves the invariant covariance
  \((-\Delta+m^2)^{-1}\), and derives the \(H^{-s}\), \(s>0\), regularity
  bound.
- Proves a Sobolev-level convergence theorem for smeared Wick powers of the
  two-dimensional stochastic convolution, including convergence in
  \(L^2(\Omega;H^{-s})\) for every \(s>0\), using a two-dimensional
  massive-propagator convolution bound.
- Proves the Fourier heat-kernel smoothing estimate used as the Sobolev
  model for the parabolic Schauder estimates in the DPD fixed point.
- Proves the Sobolev product estimates used in the elementary DPD fixed point:
  \(H^\beta H^\beta\subset H^\beta\) and
  \(H^\beta H^{-\kappa}\subset H^{-\kappa}\), using a dyadic
  Littlewood--Paley/Bony decomposition.
- Proves a deterministic local mild fixed-point theorem for the DPD
  remainder equation with enhanced noise in
  \(C([0,T];H^{-\kappa})^3\), including the heat-smoothing time gain
  \(T^{1-\theta}\), \(\theta=(1+3\kappa)/2<1\), and local Lipschitz
  dependence on initial data and enhanced noise.
- Proves a smooth enhanced-noise energy estimate for the DPD remainder
  equation.  The proof multiplies by \(Y\), integrates by parts, and uses
  Young inequalities to absorb \(Y^3X_1\), \(Y^2X_2\), and \(YX_3\) into the
  positive quartic drift plus enhanced-noise norms.
- Proves an invariant-measure passage lemma: weak convergence of invariant
  cutoff measures plus compact-uniform semigroup convergence on
  high-probability compact sets implies invariance of the limiting measure.
- Develops the Da Prato--Debussche decomposition for `Phi^4_2`, identifies
  the role of the enhanced noise, proves a Sobolev local fixed-point version,
  and marks the sharper global Besov/Holder solution mechanism as a
  `quotedtheorem` pending the full self-contained proof.
- Defines regularity structures, models, and the reconstruction theorem at the
  level needed for singular SPDE; the compact finite-sector reconstruction
  theorem is now proved from the model and modelled-distribution seminorms by
  a dyadic wavelet construction and separate coarse/fine scale estimates.
- Presents the renormalized `Phi^4_3` dynamic equation at cutoff with
  one-loop and two-loop local counterterm constants; the quoted theorem now
  separates local cutoff well-posedness, BPHZ-renormalized convergence,
  invariant-law construction, and identification with the constructive
  Euclidean \(\Phi^4_3\) measure after matching regulator and local
  coordinates.
- Proves the finite-cutoff algebraic local-counterterm calculation for
  dynamic \(\Phi^4_3\): the one-loop Wick contraction gives
  \(-3\lambda C_{1,\epsilon}X_\epsilon\), the non-nested two-loop local
  contraction gives \(+9\lambda^2C_{2,\epsilon}X_\epsilon\), and the drift
  counterterm has the opposite signs.  The proof also separates the nested
  one-loop subdivergence from the new two-loop local coordinate.
- Proves the drift-level negative homogeneity ledger for the first nonlinear
  dynamic \(\Phi^4_3\) expansion: for \(0<\kappa<1/14\), the negative cubic
  drift monomials are exactly \(X^3\) and \(X^2\mathcal I(X^3)\), while
  \(X\mathcal I(X^3)^2\) and \(\mathcal I(X^3)^3\) have positive
  homogeneity.
- Proves the sharp spatial Fourier-cutoff calculation for the one-loop
  coordinate \(C_1(M)\), including the stationary OU variance, the
  \(\ell^\infty\)-shell count \((2r+1)^3-(2r-1)^3=24r^2+2\), linear upper
  and lower growth, and dyadic shell increment bound.
- Proves the sharp spatial Fourier-cutoff calculation for the two-loop
  coordinate \(C_2(M)\): the retarded heat kernel and covariance give the
  double momentum sum with denominator
  \(a_pa_q(a_p+a_q+a_{p+q})\), dyadic annuli give the upper bound
  \(O(\log M)\), and positive boxes give a matching lower bound
  \(\Omega(\log M)\).
- Proves the dyadic shell bound for \(C_2\): for \(M_N=2^N\), the
  increment \(C_2(M_{N+1})-C_2(M_N)\) is non-negative and uniformly bounded
  in \(N\).  The proof uses the same \(2^{-|\ell-s|}\) block estimate and
  the observation that a shell pair must have at least one momentum in the
  top three dyadic annuli.
- Proves an abstract local fixed-point theorem for modelled distributions:
  given a small-time Schauder estimate, cubic product Lipschitz estimate,
  and linear forcing estimate, the dynamic \(\Phi^4_3\) fixed-point map sends
  a closed ball to itself, is a contraction there, and has a unique solution
  with Lipschitz dependence on the lifted initial data plus stochastic
  convolution.
- Proves a dyadic random-model convergence criterion: uniform \(L^p\) model
  bounds and exponentially decaying \(L^p\) increments imply existence of a
  limiting random model, \(L^p\) convergence with an explicit geometric tail,
  almost-sure convergence with every weaker dyadic exponent, passage of the
  model identities to the limit, and the limiting analytic bound by Fatou's
  lemma.
- Proves a finite Wiener-chaos moment lemma from Wick exponential generating
  functions and finite pairing combinatorics, including the \(q!\) chaos
  isometry and even-moment bounds.
- Proves a kernel-to-coordinate stochastic moment corollary: finite chaos
  expansions with deterministic kernel bounds give the pointwise stochastic
  moment and dyadic increment estimates that enter random-model convergence.
- Proves a dual-norm finite-chaos estimate: projective tensor bounds on
  \(E'\)-valued chaos kernels give \(L^{2m}\) bounds for the dual norm.
  Applying this with \(E=E_r\), the \(C^r\) test-function Banach space,
  identifies \(Q_{n,\tau}^{#}\) with the correct dual norm and avoids
  treating the infinite-dimensional test-function ball as a finite
  parameter space.
- Proves a projective kernel criterion: if an \(E'\)-valued chaos kernel is
  represented by an integral of Hilbert kernels tensored with dual
  test-function functionals, its projective tensor norm is bounded by the
  integral of the Hilbert norm times the dual norm.  The edge version splits
  increments into Hilbert-kernel variation and dual-functional variation.
  For \(E_r=C^r\) test functions, point evaluations have bounded dual norm
  and their differences carry the expected Holder power.
- Proves a dyadic parabolic convolution bound: support and pointwise scale
  estimates for order-\(a\) and order-\(b\) kernels imply order-\((a+b)\)
  output bounds, including \(L^\infty\) and \(L^1\) estimates with explicit
  geometric factors.
- Proves Gaussian scale estimates for the primitive strict negative-sector
  coordinates: white-noise scaling gives \(\sigma_\Xi=\kappa\), and a
  parabolic covariance singularity \(C(u,v)=O(\|u-v\|_{\mathfrak s}^{-1})\)
  gives \(\sigma_{X^k}=k\kappa\) for \(k=1,2,3\), with Holder edge control
  on same-scale parameter increments.
- Proves the corresponding \(E_r'\)-dual-norm estimates for the primitive
  Gaussian coordinates when \(0<\theta<r-Q/2\): a parabolic wavelet
  \(H^{-s}\) majorant controls the supremum over the \(C^r\) test-function
  ball, white-noise coefficients sum when \(s>Q/2\), and Wick-power
  coefficients sum using the variance exponent \(2^{(k-Q)j}\).
- Proves a parabolic Taylor-subtraction gain: if a local factor is replaced
  by a remainder bounded by \(H\|h\|_{\mathfrak s}^r\), then pairing with an
  order-\(a\) dyadic kernel gains \(r\) additional powers of the scale.
- Proves a dyadic-net supremum upgrade: finite-net pointwise moment bounds
  and edge increment bounds with decay \(2^{-(d+\epsilon)\ell}\) imply an
  \(L^p\) bound for the compact supremum with the explicit constant
  \(C_0^{1/p}B_0+C_1^{1/p}B/(1-2^{-\epsilon/p})\), and cutoff decay factors
  pass through unchanged.
- Proves a scale-summed coordinate supremum theorem: when the parameter
  entropy at physical scale \(m\) costs \(2^{Dm}\) and the stochastic
  coordinate has regularity slack \(2^{-\sigma m}\), the supremum over all
  scales is \(L^p\)-controlled if \(\sigma>D/p\).  The proof applies the
  dyadic-net theorem at each scale and sums the resulting geometric series.
- Proves a coordinate-to-model convergence criterion: if finitely many
  compact coordinate suprema dominate the finite-sector model seminorm and
  model distance, and if each coordinate satisfies the dyadic-net moment and
  increment estimates, then the random-model Cauchy hypotheses follow with
  explicit constants \(C_N\) and \(C_D\).
- Proves a multiscale sector summability criterion: positive sector-gap
  exponents \(\eta_h\) imply uniform kernel bounds with geometric factor
  \(G=\prod_h(1-2^{-\eta_h})^{-1}\) and cutoff-increment bounds with shell
  factor \(\tilde G\), hence the deterministic kernel hypotheses of the
  finite-chaos moment corollary.
- Proves a one-loop relative-scale gap estimate for local subtraction:
  after subtracting the local value in the \(j\leq i\) sector the scale gap
  is \(a+\theta\), while the off-diagonal \(j>i\) sector has gap \(b\).
  For the dynamic \(\Phi^4_3\) one-loop contraction this leaves the expected
  mass-coordinate divergence \(2^k\) and makes the relative scales summable.
- Proves the two-loop non-nested sunset sector bound: for three kernels with
  orders \(a,b,c\) satisfying \(a+b+c=2Q\), each block is controlled by the
  relative-gap factor
  \(2^{-(Q-a)r_K-(Q-b)r_L-(Q-c)r_M}\), and the dyadic shell increment is
  uniformly bounded.  In dynamic \(\Phi^4_3\), the heat/covariance/covariance
  orders \((2,4,4)\) give gap exponents \((3,1,1)\) and shell factor
  \(60/7\).
- Proves scale-wise cancellation of the nested two-loop tadpole coefficient:
  the \(+6C_{1,l}\int K_iG_j\) coefficient from
  \(X(z)^2K_iX(w)^3\) is canceled exactly by the
  \(-6C_{1,l}\int K_iG_j\) coefficient generated by the inner one-loop
  forest subtraction \(X(w)^3\mapsto X(w)^3-3C_{1,l}X(w)\).
- Proves the finite negative-sector coordinate chart for dynamic
  \(\Phi^4_3\): with \(\gamma_-=\frac12-7\kappa\), the strict sector
  \(T_{<\gamma_-}\) contains exactly
  \(\mathbf1,\Xi,X,X^2,X^3,XY,X^2Y\) among the listed symbols, while
  \(XY^2\) lies on the excluded boundary.  The only nontrivial strict lower
  stochastic \(\Gamma\)-coordinates are \(XY\to X\) and \(X^2Y\to X^2\),
  both controlled by the constant reexpansion coefficient of
  \(Y=\mathcal I(X^3)\).  The proposition then proves model-seminorm and
  model-distance domination by six \(\Pi\)-coordinates and one
  \(\Gamma\)-coordinate.
- Proves the strict negative-sector model convergence criterion for dynamic
  \(\Phi^4_3\): scale-summed moment and parameter-increment estimates for the
  six \(\Pi\)-coordinates and the single \(c_n\) reexpansion coordinate imply
  uniform \(L^p\) model seminorm bounds, dyadic Cauchy bounds for model
  distance, and convergence to a limiting random model on \(\mathcal T_-\) with
  an explicit geometric \(L^p\) tail.
- Proves the physical-parameter entropy for those seven coordinates after the
  test-function supremum has been dualized: \(\Pi\)-coordinates use
  \(K\times[1/2,1]\) with scale entropy \(D=5\) and edge entropy \(d=6\), while
  the \(c_n\) coordinate uses \(K\) times the parabolic annulus of normalized
  separations with scale entropy \(D=5\) and edge entropy \(d=10\).
- Separates regularity-structure, paracontrolled, and RG routes.
- Separates invariant-measure construction from the OS hypotheses needed for
  QFT reconstruction.
- Records a self-contained singular-SPDE proof stack as an open obligation:
  Wick powers, Schauder and multiplication estimates, energy estimates,
  invariant-law identification, BPHZ model convergence, fixed points in
  modelled distributions, and SPDE-to-OS passage.

## Figure Ledger

No figure is included in this pass.  Future figures should include Markov
flow to invariant measure, covariance-scale decompositions, and SPDE-to-OS
data maps.

## Audit Notes

- 2026-05-25 issue #575 pass: the Da Prato--Debussche solution mechanism,
  Hairer reconstruction theorem, and renormalized dynamic \(\Phi^4_3\) SPDE
  datum are no longer ordinary theorem blocks followed by proof sketches.
  They are marked as `quotedtheorem` blocks, their proof sketches are
  rewritten as role/status text, and Open Problem
  `op:self-contained-singular-spde-proof-stack` records the monograph's
  obligation to prove the quoted SPDE results internally rather than accept
  them on authority.
- 2026-05-25 issue #558 pass: the dynamic \(\Phi^4_3\) theorem boundary now
  states the four requested components explicitly: local cutoff
  well-posedness, renormalized convergence with \(C_{1,\epsilon}\) and
  \(C_{2,\epsilon}\), invariant measures of the limiting Markov process, and
  equality with the constructive Euclidean \(\Phi^4_3\) OS hierarchy only
  after the regulator chart and local coordinates are matched.
- 2026-05-25 issue #582 pass: the chapter now proves the first elementary
  part of the singular-SPDE proof stack internally: Fourier construction of
  the stationary stochastic convolution, normalization of the factor \(2\) in
  the white-noise covariance, negative-Sobolev regularity, smeared Wick-power
  convergence in two dimensions, and a Fourier heat-kernel smoothing
  estimate.  The calculation-check companion verifies the OU variance,
  Sobolev threshold arithmetic, and heat-kernel optimization.
- 2026-05-25 DPD fixed-point pass: the chapter now proves the deterministic
  Sobolev local fixed-point component of the DPD construction internally.
  The pass also sharpens the Wick-power Sobolev theorem from the earlier
  crude \(s>1\) estimate to every \(s>0\), closing the regularity input
  needed for the displayed Sobolev DPD theorem.  The proof displays the
  Littlewood--Paley product bounds, constructs the mild map, proves the
  contraction from the Duhamel time gain, and adds a calculation-check gate
  for the exponent inequalities.
- 2026-05-26 issue #582 continuation: the chapter now proves two additional
  components of the singular-SPDE proof stack internally: a smooth
  enhanced-noise energy estimate for the DPD global step and an abstract
  invariant-measure passage lemma for cutoff limits.  The calculation-check
  companion now verifies the Young-exponent arithmetic and a finite
  invariant-measure identity.
- 2026-05-26 issue #582 reconstruction continuation: the earlier
  reconstruction theorem boundary has been replaced by a compact
  finite-sector theorem.  The proof defines parabolic test-function scaling,
  model seminorms, and modelled-distribution norms; proves the germ coherence
  estimate; constructs the reconstructed distribution from dyadic wavelet
  coefficients; and derives the \(\delta^\gamma\) reconstruction bound by
  separate coarse-scale and fine-scale sums.  The calculation-check companion
  now verifies the exponent arithmetic in those two sums.
- 2026-05-26 issue #582 BPHZ local-coordinate continuation: the dynamic
  \(\Phi^4_3\) section now proves the finite-cutoff homogeneity ledger and
  the local Wick-contraction calculation that fixes the displayed
  \(3\lambda C_{1,\epsilon}-9\lambda^2C_{2,\epsilon}\) drift counterterm.
  The calculation-check companion verifies the homogeneity, sign, and
  combinatorial arithmetic.
- 2026-05-26 issue #582 fixed-point continuation: the chapter now proves the
  abstract modelled-distribution fixed-point step from explicit Banach-space
  hypotheses rather than quoting the contraction argument.  The
  calculation-check companion verifies the ball condition, contraction
  constant, and Picard tail arithmetic.
- 2026-05-26 issue #582 random-model convergence continuation: the chapter now
  proves an abstract dyadic Cauchy criterion for random models.  The theorem
  constructs the limiting model from the model-distance Cauchy property,
  passes algebraic identities and analytic bounds to the limit, proves
  \(L^p\) convergence with an explicit tail, and derives the almost-sure
  dyadic rate by Markov and Borel-Cantelli.  The calculation-check companion
  verifies the geometric-series arithmetic used in the tail bound.
- 2026-05-26 issue #582 Wiener-chaos continuation: the chapter now proves the
  stochastic moment estimate used underneath BPHZ model bounds.  The proof
  derives the chaos isometry from Wick exponential generating functions,
  bounds higher even moments by counting admissible Wick pairings, and applies
  the result to finite chaos model-coordinate kernels.  The calculation-check
  companion verifies the second/third chaos isometry, the fourth moment of
  \(H_2(G)\), and a sample coordinate-moment constant.
- 2026-05-26 issue #582 dyadic-kernel continuation: the chapter now proves the
  deterministic parabolic convolution estimate used before finite-chaos
  moments can be applied to BPHZ model coordinates.  The proof derives the
  support, \(L^\infty\), and \(L^1\) bounds by splitting the scale sum into
  the two branches \(\min(i,j)=k\).  The calculation-check companion verifies
  the output exponents and geometric factors for a sample \(Q=5\),
  \(a=2\), \(b=1\) convolution.
- 2026-05-26 issue #582 Taylor-gain continuation: the chapter now proves the
  scale gain produced by Taylor subtraction at a dyadic kernel scale.  The
  proof is the direct \(L^1\)-kernel estimate multiplied by the parabolic
  Taylor remainder bound.  The calculation-check companion verifies the
  exponent arithmetic for a sample \(a=2\), \(r=3\), \(i=4\) estimate.
- 2026-05-26 issue #582 dyadic-net continuation: the chapter now proves the
  finite-net upgrade needed to convert fixed-coordinate BPHZ moment and
  increment estimates into compact model-seminorm bounds.  The proof gives
  the telescoping net expansion, the base-net and edge-level \(L^p\)
  estimates, the metric-entropy cancellation, and the exact geometric-series
  constant.  The calculation-check companion verifies the entropy
  cancellation and cutoff-factor arithmetic.
- 2026-05-26 issue #582 coordinate-to-model continuation: the chapter now
  proves the finite-coordinate criterion that packages coordinate supremum
  bounds into the random-model Cauchy hypotheses.  The proof applies the
  dyadic-net theorem coordinate by coordinate and then uses the explicit
  domination of the model seminorm and model distance.  The calculation-check
  companion verifies the resulting \(C_N\), \(C_D\), and dyadic distance
  arithmetic in an exact finite sample.
- 2026-05-26 issue #582 multiscale-sector continuation: the chapter now
  proves the sector-gap summability step needed between tree-level BPHZ
  kernel estimates and the finite-chaos coordinate moment corollary.  The
  proof sums the full product of geometric scales for uniform bounds and
  bounds a cutoff shell by a union over the active maximal gap.  The
  calculation-check companion verifies \(G\), \(\tilde G\), the sharp and
  relaxed increment bounds, and the shell union bound in an exact sample.
- 2026-05-26 issue #582 one-loop sector continuation: the chapter now proves
  the first concrete relative-scale estimate used by the BPHZ tree analysis:
  the one-loop local subtraction gains a positive scale gap in the
  \(j\leq i\) sector and the \(j>i\) sector is summable by support-volume
  decay.  The calculation-check companion verifies the dynamic
  \(\Phi^4_3\) exponents \(Q=5\), \(a=b=2\), and a sample Holder exponent
  \(\theta=1\).
- 2026-05-26 issue #582 negative-ledger continuation: the BPHZ dynamic
  \(\Phi^4_3\) section now proves the finite drift-level negative
  homogeneity list and the explicit Fourier-cutoff growth of the one-loop
  local coordinate \(C_1\).  The calculation-check companion verifies the
  four cubic homogeneities, the \(\kappa<1/14\) positivity boundary, the
  \(\mathbb Z^3\) shell count, and a dyadic shell increment bound.
- 2026-05-26 issue #582 C2-growth continuation: the BPHZ dynamic
  \(\Phi^4_3\) section now derives the Fourier-cutoff double sum for the
  two-loop local coordinate \(C_2(M)\) and proves matching logarithmic upper
  and lower bounds.  The calculation-check companion verifies the dyadic
  \(2^{-|\ell-s|}\) summability arithmetic and the lower positive-box block
  factor.
- 2026-05-26 issue #582 C2-shell continuation: the BPHZ dynamic
  \(\Phi^4_3\) section now proves that the dyadic shell increment
  \(C_2(2^{N+1})-C_2(2^N)\) is uniformly bounded.  The calculation-check
  companion verifies the finite shell sum bounded by the constant \(9\).
- 2026-05-26 issue #582 two-loop-sector continuation: the chapter now
  proves the deterministic non-nested sunset sector bound and the scale-wise
  nested tadpole cancellation for the dynamic \(\Phi^4_3\) two-loop local
  tree.  The calculation-check companion verifies the logarithmic exponent
  balance \(2Q-(2+4+4)=0\), the gap exponents \((3,1,1)\), the shell factor
  \(60/7\), and the exact \(+6-6\) forest-cancellation arithmetic.
- 2026-05-26 issue #582 negative-coordinate continuation: the chapter now
  constructs the finite strict negative-sector coordinate chart for dynamic
  \(\Phi^4_3\) and proves domination of the \(\Pi/\Gamma\) seminorms by the
  explicit coordinate fields.  The calculation-check companion verifies the
  homogeneity cutoff, the excluded boundary monomial, the two nontrivial
  \(\Gamma\)-gap exponents, and the coordinate count.
- 2026-05-26 issue #582 scale-summed-coordinate continuation: the chapter
  now proves the theorem that turns fixed-scale dyadic-net coordinate
  estimates into all-scale coordinate suprema when the regularity slack beats
  scale entropy after taking \(L^p\).  The calculation-check companion
  verifies the entropy cancellation, the geometric scale sum, and cutoff
  factor propagation in an exact sample.
- 2026-05-26 issue #582 negative-sector model continuation: the chapter now
  composes the finite negative-sector coordinate chart with the scale-summed
  coordinate theorem and the random-model Cauchy theorem.  The resulting
  theorem states the seven coordinate functions, the entropy hypotheses, the
  scale-slack condition \(\sigma_i>D_i/p\), the constants \(S_i^{sc}\) and
  \(\tilde S_i^{sc}\), and the exact \(L^p\) bounds that produce a limiting
  random model on \(\mathcal T_-\).  The calculation-check companion verifies
  the seven-coordinate \(C_N\), \(C_D\), and tail arithmetic in an exact sample.
- 2026-05-26 issue #582 physical-parameter continuation: the chapter now
  proves the parameter-space entropy used by the strict negative-sector
  convergence criterion, without treating the \(C^r\) test-function unit ball as
  a finite-dimensional parameter.  The proof first replaces the test-function
  dependence by the dualized coordinate \(Q_{n,\tau}^{#}\), then covers
  \(K\times[1/2,1]\) and \(K\times A_{\mathfrak s}\) by parabolic grids.  The
  calculation-check companion verifies the exponents \(D=5\), \(d_\Pi=6\), and
  \(d_\Gamma=10\).
- 2026-05-26 issue #582 dual-norm continuation: the chapter now proves the
  Banach-dual finite-chaos estimate needed after the test-function supremum is
  dualized.  The proof defines the projective tensor norm, constructs
  \(E'\)-valued chaos integrals by completion, and derives the \(L^{2m}\)
  dual-norm bound from the scalar chaos moment estimate and Minkowski's
  inequality.  The calculation-check companion verifies the integer
  overestimate constants and the transfer from projective edge decay to the
  dyadic-net moment exponent.
- 2026-05-26 issue #582 projective-kernel continuation: the chapter now
  proves the deterministic bridge from concrete BPHZ kernels to the
  projective tensor hypotheses of the dual-norm chaos theorem.  The proof is
  a Bochner integral estimate in the projective tensor product, with an edge
  decomposition separating Hilbert-kernel increments from movement of the
  test-function evaluation functional.  The calculation-check companion
  verifies the discrete base and edge arithmetic.
- 2026-05-26 issue #582 Gaussian-coordinate continuation: the chapter now
  proves the scalar Gaussian scale estimates for \(\Xi,X,X^2,X^3\).  The
  proof derives the white-noise \(L^2\) scaling, the Wick covariance identity,
  local integrability of \(\|u-v\|_{\mathfrak s}^{-k}\) for \(k\leq3<5\), and
  Holder edge estimates for same-scale parameter increments.  The
  calculation-check companion verifies the resulting scale slack exponents.
- 2026-05-26 issue #582 Gaussian dual-norm continuation: the chapter now
  upgrades the primitive Gaussian coordinate estimates to \(E_r'\)-valued
  bounds.  The proof introduces a wavelet \(H^{-s}\) majorant for the dual
  \(C^r\)-test norm, proves the white-noise and Wick-power coefficient
  summability exponents, and proves same-scale dual-norm edge estimates under
  \(0<\theta<r-Q/2\).  The calculation-check companion verifies the
  wavelet-summability and edge-tail arithmetic.
