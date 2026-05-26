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
- `Y_n(a)`, `sigma(a)`: model-coordinate random variable and deterministic
  scale weight in the kernel-to-coordinate moment corollary.

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
