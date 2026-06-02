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
- `W_N^{(n)}`: cutoff Wick powers \(:X_N^n:\) as stochastic processes in
  \(C([0,T];H^{-s})\).
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
- `X_{i,n}`, `Y_n`, `Y`: smooth enhanced-noise approximants, smooth DPD
  remainders, and weak energy limit in the closedness theorem for the DPD
  energy inequality.
- `mathfrak D_T`, `K`, `B_{K,T}`, `tau(D)`: DPD enhanced-noise/initial-data
  space, compact data set, uniform rough energy-to-Besov bound, and maximal
  local existence time in the global compact-continuity criterion.
- `M_T`, `Q_T`: uniform smooth DPD energy-input bound and the stochastic
  time-space slab \([0,T]\times\mathbb T^2\) in the DPD energy-compactness
  theorem.
- `E_M`: finite-dimensional Fourier subspace used in the self-contained
  torus Aubin-Lions compactness lemma for DPD remainders.
- `mathcal C^gamma`, `Delta_j`, `S_j`, `prec`, `circ`, `succ`: Besov-Holder
  space \(B^\gamma_{\infty,\infty}\), dyadic Littlewood-Paley blocks,
  low-frequency cutoff, and Bony paraproduct/resonant operations in the DPD
  rough-product theorem.
- `theta=(alpha+kappa)/2`: Duhamel heat-smoothing exponent in the Besov DPD
  fixed-point theorem; the condition \(\alpha<2-\kappa\) is exactly
  \(\theta<1\).
- `P_t^(n), P_t`: cutoff and limiting Markov semigroups in the invariant-law
  passage lemma.
- `U_n(0), U_n(t), U_*(0), U_*(t)`: coupled cutoff and limiting Markov fields
  used to compare stationary laws after SPDE solution convergence.
- `delta_n`, `epsilon_{n,t}`, `a_t`: time-zero coupling defect, time-\(t\)
  residual convergence defect, and finite-time Lipschitz amplification
  constant in the stationary-law comparison.
- `eta`, `kappa`, `p`, `K_R`: Hilbert-scale tightness parameters in the
  cutoff-field compactness criterion; \(0<\eta<\kappa\), the moment order is
  \(p\), and \(K_R\) is the \(H^{-\eta}\)-ball viewed inside
  \(H^{-\kappa}\).
- `P_M`: Fourier projection to modes \(|k|\le M\) used locally in the
  compactness proof for \(K_R\).  This is distinct from the ultraviolet
  regulator \(P_N\) used in the stochastic cutoff family.
- `A`, `e_alpha`, `lambda_alpha`, `I_N`, `gamma_N`: Laplacian, real
  orthonormal eigenbasis, eigenvalues, spectral cutoff index set, and
  massive free Gaussian cutoff law in the reference negative-Sobolev
  tightness estimate.
- `rho_N`, `A_q`, `a=q/(q-1)`: normalized interacting density with respect
  to a Gaussian cutoff law, its uniform \(L^q\) bound, and the conjugate
  Holder exponent in the density criterion for interacting
  negative-Sobolev moments.
- `V_N`, `Z_N`: cutoff Wick quartic interaction and its finite-dimensional
  partition function in the Nelson-stability-to-density proposition.
- `C_N^{sigma sigma}`, `C_N^{sigma infinity}`: cutoff covariance and
  cutoff-limit mixed covariance in the mixed-covariance criterion for common
  Wick limits.
- `mu^sigma`, `K_{j,N}^nu`, `q_{j,N}^nu`: smooth Fourier multiplier,
  dyadic covariance block, and Euclidean symbol used in the smooth
  multiplier covariance-convergence theorem.
- `mathcal X_N`, `mathcal X_N^A`, `mathcal X_N^B`: finite vectors of
  smeared Wick coordinates used in the common-coordinate convergence
  corollary.
- `X_N^A`, `X_N^B`, `W_N^A`, `W_N^B`: regulator-dependent finite lists of
  cylinder coordinates and interaction densities in the bounded-cylinder
  common-density comparison theorem.
- `V_N^A`, `V_N^B`, `V`: regulator-dependent renormalized interaction
  potentials and their common limiting potential in the common-potential
  comparison corollary.
- `V_N=(\lambda/4):X_N^4:(1)`: cutoff Wick quartic potential in the
  potential-convergence corollary.
- `H_N`, `A_N`, `L_N`, `e_{N,alpha}`, `lambda_{N,alpha}`, `nu_N`:
  finite-dimensional Hilbert space, Hessian lower-bound operator, reference
  nonnegative operator, spectral basis, eigenvalues, and convex cutoff
  measure in the Brascamp-Lieb negative-Sobolev moment criterion.
- `mathcal L`, `u_epsilon`: finite-dimensional diffusion generator and
  resolvent solution used in the Brascamp-Lieb proof.
- `Lambda_{a,L}`, `vartheta`, `mu_{a,L}`, `S_{a,L}`, `V_x`: finite lattice,
  time reflection, lattice Euclidean measure, lattice scalar action, and
  reflection-invariant on-site potential used in the OS-positive lattice
  regulator proposition.
- `mu_N^F`, `mu_N^L`: Fourier-Galerkin stochastic cutoff family and
  lattice cutoff family in the regulator-comparison criterion for
  transferring OS positivity.
- `ell_j`, `V(phi)`: finite list of cylinder coordinates and exponential
  moment weight used to turn exponential tails into uniform integrability of
  polynomial OS observables.
- `a_x`, `b_x`, `d_x`: finite-lattice quartic coercivity constants in the
  cutoff tail estimate.
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
- `m`, `D`, `sigma`, `rho_*`: physical testing-scale index,
  scale-entropy exponent, regularity slack, and the strict cutoff-Cauchy rate
  retained after summing a shell-separated factor \(2^{-\rho(n-m)_+}\).
- `H_{rho_*,rho,a}`: deterministic summation constant in the
  shell-separated cutoff bridge, with \(a=\sigma-D/p\).
- `B_pi`, `B_pi^{ed}`: finite-chaos weighted sums of projective kernel
  constants in the projective shell-separated coordinate criterion; these are
  the constants that enter the dyadic-net base and edge bounds after the
  \(E_r'\)-valued chaos kernels have been estimated in projective norm.
- `rho_tau`, `rho_tau^*`, `widehat A_{tau,i}`,
  `widehat S_tau^{sh}`: nonlinear \(\Pi\)-coordinate shell gain, retained
  scale-summed cutoff-Cauchy rate, finite-chaos weighted shell constants, and
  resulting scale-summed cutoff constant in the shell-separated nonlinear
  \(XY\)/\(X^2Y\) corollary.
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
- `alpha`, `beta`, `sigma`, `gamma`, `mathfrak c_T(a,b)`: assigned
  negative homogeneity, integrated homogeneity, regularity slack, true
  integrated Holder exponent, and heat-integration reexpansion coefficient in
  the deterministic \(c_n\)-transfer estimate.
- `C_{2,epsilon}(a)`, `G_epsilon(a,b)`, `K_epsilon(a,b)`: finite-cutoff
  covariance, retarded kernel, and local two-loop coordinate used in the
  Wick decompositions of the nonlinear negative symbols \(XY\) and \(X^2Y\).
- `p_epsilon(a)`, `F_{XY,q}^{chi}`, `F_{X^2Y,q}^{chi}`: cutoff
  noise-to-field Hilbert kernel and the tested finite-chaos kernels of the
  nonlinear negative coordinates.
- `G_{uv}`, `K_{ab}`: shorthand in the nonlinear kernel-norm proposition for
  \(G_\epsilon(u,v)\) and \(K_\epsilon(a,b)\).
- `Z_{\epsilon,\delta,z}^{XY}`, `\zeta_{XY}`: scalar tested \(XY\)
  coordinate at physical scale \(\delta\) and the logarithmic scale-loss
  parameter used to convert the marginal graph ledger into normalized
  coordinate slack \(4\kappa-\zeta_{XY}\).
- `Z_{\epsilon,m,u}^{XY}`, `d_{\Pi,m}`: same-scale scalar tested \(XY\)
  coordinate and physical parameter metric used for the \(XY\) edge estimate
  in base point and test scale.
- `Z_{n,m,u}^{XY}`: dyadic-cutoff scalar tested \(XY\) coordinate used to
  isolate the ultraviolet shell gain in the cutoff increment
  \(Z_{n+1,m,u}^{XY}-Z_{n,m,u}^{XY}\).
- `Z_{\epsilon,\delta,z}^{X^2Y,\ge 3}`: the fifth- plus third-chaos scalar
  tested part of the locally subtracted \(X^2Y\) coordinate, separated from
  the first-chaos covariance-increment sector.
- `Z_{\epsilon,m,u}^{X^2Y,\ge 3}`: same-scale scalar tested high-chaos
  \(X^2Y\) coordinate on \(K\times[1/2,1]\), used for parameter-edge
  estimates in base point and physical test scale.
- `Z_{n,m,u}^{X^2Y,\ge 3}`: dyadic-cutoff scalar tested high-chaos
  \(X^2Y\) coordinate used to isolate the ultraviolet shell gain in
  \(Z_{n+1,m,u}^{X^2Y,\ge3}-Z_{n,m,u}^{X^2Y,\ge3}\).
- `A_n(a,h)`, `C_s`, `V_{\delta,N}^{(1)}`: shell packets of the local
  two-loop factor \(KG^2\), dyadic order-four covariance blocks, and the
  scalar first-chaos sector sum used to bound the locally subtracted
  \(X^2Y\) first-chaos coordinate.
- `\Delta_N V_\delta^{(1)}`: cutoff-shell increment
  \(V_{\delta,N+1}^{(1)}-V_{\delta,N}^{(1)}\) for the locally subtracted
  \(X^2Y\) first-chaos scalar sector.
- `mu_spde`, `mu_cons`, `S_n^spde`, `S_n^cons`, `D`: stationary SPDE law,
  constructive Euclidean measure, their Schwinger hierarchies, and the dense
  test-function subspace used in the common-hierarchy comparison criterion.

## Claim Ledger

- Proves the finite-dimensional Langevin integration-by-parts identity and
  records the finite-cutoff semigroup theorem actually used by stochastic
  quantization: under essential self-adjointness of the gradient generator
  on \(C_c^\infty\) and conservativeness of its Markov semigroup, the cutoff
  semigroup is reversible and invariant with Dirichlet form
  \(\int\nabla f\cdot\nabla g\,d\pi\).  This separates the infinitesimal
  invariant-density calculation from genuine stationarity of the stochastic
  process.
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
- Proves a mixed-covariance criterion for common Wick limits.  If two cutoff
  Gaussian fields and their common limiting Gaussian field have cutoff
  covariances \(C_N^{\sigma\sigma}\) and mixed covariances
  \(C_N^{\sigma\infty}\) converging to the limiting covariance \(C\) in
  \(L^n(\mathbb T^2\times\mathbb T^2)\), then the smeared \(n\)-th Wick
  powers converge in \(L^2\) to the same limit.  The proof differentiates
  the two-variable Wick generating function and uses
  \(\|a^n-b^n\|_1\le n\|a-b\|_n(\|a\|_n^{n-1}+\|b\|_n^{n-1})\).
- Proves a smooth Fourier multiplier covariance-convergence theorem.  For
  cutoff fields \(X_N^\sigma=\mu^\sigma(D/N)X\) with
  \(\mu^\sigma\in C_c^\infty\), real, even, and \(\mu^\sigma(0)=1\), both
  the cutoff covariance and the cutoff-limit mixed covariance converge to
  the massive covariance in every finite \(L^p\).  The proof uses a dyadic
  partition, symbol derivative bounds, Poisson summation, a uniform
  logarithmic majorant, pointwise convergence away from the diagonal, and
  dominated convergence.  This supplies a concrete check of the
  mixed-covariance hypothesis for smooth Fourier regulators.
- Extracts the finite Wick-coordinate vector convergence needed by regulator
  comparison.  For any finite list of smearings and Wick orders, coordinate
  convergence in \(L^2\) implies convergence of the vector in
  \(L^2(\Omega;\mathbb R^r)\), hence in probability; for two cutoff schemes
  with common Wick-power limits, the same argument gives common coordinate
  vectors.  Bounded continuous functions of these vectors therefore converge
  in probability by the subsequence form of the continuous-mapping theorem.
- Proves path-space convergence of the two-dimensional enhanced noise
  \((X_N,:X_N^2:,:X_N^3:)\) in
  \(C([0,T];H^{-s})^3\) for every \(s>0\).  The proof uses the exact
  Ornstein--Uhlenbeck time cross-covariance, a weakened-propagator
  convolution estimate, finite-Wiener-chaos moment bounds, and a
  Kolmogorov/grid argument.
- Extracts the Wick quartic potential convergence needed by regulator
  comparison.  Since the smeared Wick-power theorem applies with \(n=4\)
  and \(f\equiv1\), the cutoff potentials
  \(V_N=(\lambda/4):X_N^4:(1)\) converge in \(L^2\), hence in probability,
  to the common limiting Wick quartic.  For two cutoff schemes with the same
  Wick-power limit, this supplies the potential-convergence hypothesis in
  the common-potential comparison corollary; the remaining constructive
  burden is the uniform \(L^p\) stability of the exponential weights.
- Records and derives the Fourier heat-kernel smoothing estimate used as the
  Sobolev model for the parabolic Schauder estimates in the DPD fixed point;
  the endpoint \(\theta<1\) is identified as the deterministic Duhamel
  singularity in the \(L^\infty_t\) estimate.
- Proves the Sobolev product estimates used in the elementary DPD fixed point:
  \(H^\beta H^\beta\subset H^\beta\) and
  \(H^\beta H^{-\kappa}\subset H^{-\kappa}\), using a dyadic
  Littlewood--Paley/Bony decomposition.
- Proves the Besov-Holder product-continuity theorem for the DPD
  nonlinearity.  With \(0<\kappa<\alpha\), Bony's formula defines canonical
  products
  \(\mathcal C^\alpha\mathcal C^{-\kappa}\to\mathcal C^{-\kappa}\) and
  \(\mathcal C^\alpha\mathcal C^\alpha\to\mathcal C^\alpha\).  The proof
  derives the left paraproduct, right paraproduct, and resonant bounds
  directly from dyadic support geometry and the condition
  \(\alpha-\kappa>0\), then obtains local Lipschitz continuity of
  \(Y^3+3Y^2X_1+3YX_2+X_3\) in \(C_T\mathcal C^{-\kappa}\).
- Proves the Besov-Holder deterministic DPD local fixed-point theorem.
  For \(0<\kappa<\alpha<2-\kappa\), enhanced noise in
  \(C_T\mathcal C^{-\kappa}\) and initial data in \(\mathcal C^\alpha\)
  produce a unique mild solution in \(C_T\mathcal C^\alpha\) on a time
  interval controlled by the data norm.  The proof first proves a dyadic
  heat-smoothing estimate
  \(\mathcal C^\rho\to\mathcal C^{\rho+2\theta}\), then combines it with the
  Besov product theorem and Banach contraction; local Lipschitz dependence on
  the enhanced noise is included.
- Proves a deterministic local mild fixed-point theorem for the DPD
  remainder equation with enhanced noise in
  \(C([0,T];H^{-\kappa})^3\), including the heat-smoothing time gain
  \(T^{1-\theta}\), \(\theta=(1+3\kappa)/2<1\), and local Lipschitz
  dependence on initial data and enhanced noise.
- Proves a smooth enhanced-noise energy estimate for the DPD remainder
  equation.  The proof multiplies by \(Y\), integrates by parts, and uses
  Young inequalities to absorb \(Y^3X_1\), \(Y^2X_2\), and \(YX_3\) into the
  positive quartic drift plus enhanced-noise norms.
- Proves closedness of the integrated DPD energy inequality under smooth
  enhanced-noise approximation.  If \(X_{1,n}\to X_1\) in \(L^4\),
  \(X_{2,n}\to X_2\) in \(L^2\), \(X_{3,n}\to X_3\) in \(L^{4/3}\), the
  initial data converge strongly in \(L^2\), and the remainders converge
  weakly in \(L^2_tH^1_x\), \(L^4_{t,x}\), and at the terminal time in
  \(L^2_x\), then the limiting remainder satisfies the integrated energy
  inequality.  The proof uses the \(L^p\)-continuity of power integrals and
  weak lower semicontinuity of the quadratic and quartic energy terms.
- Proves the compactness step that supplies those weak limits for smooth DPD
  remainders under a cutoff-uniform bound on the initial \(L^2\) norm and the
  three enhanced-noise norms.  The proof derives a uniform
  \(L^{4/3}_tH^{-1}_x\) bound on \(\partial_tY_n\) from the equation, using
  the exponent identities \(Y^3,Y^2X_1,YX_2,X_3\in L^{4/3}_{t,x}\), then
  applies Banach--Alaoglu and a scalar \(W^{1,4/3}\)-compactness argument to
  identify terminal weak \(L^2\) limits.
- Proves the self-contained torus Aubin-Lions compactness lemma needed to
  upgrade the DPD weak compactness to strong \(L^2_{t,x}\) convergence:
  finite Fourier modes are compact by Arzela-Ascoli and high Fourier modes
  are uniformly small by the \(L^2_tH^1_x\) bound.
- Proves identification of the DPD distributional limit when
  \(X_{1,n}\to X_1\) in \(L^4\), \(X_{2,n}\to X_2\) in \(L^2\), and
  \(X_{3,n}\to X_3\) in \(L^{4/3}\).  The proof obtains strong
  \(L^r_{t,x}\) convergence of \(Y_n\) for every \(r<4\), then passes
  \(Y_n^3\), \(Y_n^2X_{1,n}\), \(Y_nX_{2,n}\), and \(X_{3,n}\) to the limit
  in \(L^1\), yielding the weak distributional equation with endpoint terms.
- Proves compatibility of the Besov local solution map with the smooth
  energy-compactness approximation on their common domain of validity.
  Smooth approximants converging in \(C_T\mathcal C^{-\kappa}\) and
  \(Y_{0,n}\to Y_0\) in \(\mathcal C^\alpha\) converge to the canonical
  Besov fixed point in \(C_T\mathcal C^\alpha\).  If the same enhanced
  noises also converge in the Lebesgue spaces required by the elementary
  energy inequality, compactness identifies the energy limit with this
  Besov solution and passes the integrated energy inequality to every
  terminal time on the common local interval.
- Proves a global compact-continuity criterion for the DPD solution map.
  Given the local Besov fixed point, a blow-up alternative, and a uniform
  rough energy-to-Besov bound on a compact enhanced-noise/initial-data set,
  every maximal solution extends to the full time interval and the solution
  map is uniformly continuous on that compact set.  The proof iterates the
  local contraction estimate with a single time step controlled only by the
  compact noise bound and the uniform Besov bound.  This reduces the global
  cutoff-convergence input in the \(\Phi^4_2\) assembly theorem to a precise
  rough a priori estimate rather than treating global DPD convergence as a
  black box.
- Proves an invariant-measure passage lemma: weak convergence of invariant
  cutoff measures plus compact-uniform semigroup convergence on
  high-probability compact sets implies invariance of the limiting measure.
- Proves the Sobolev compactness criterion used to turn a cutoff-uniform
  \(H^{-\eta}\) moment, with \(0<\eta<\kappa\), into tightness of cutoff
  laws in \(H^{-\kappa}\).  The proof is explicit in Fourier modes: the
  \(H^{-\kappa}\) high-frequency tail of the \(H^{-\eta}\)-ball is bounded
  by \(\langle M\rangle^{-2(\kappa-\eta)}R^2\), finite-dimensional
  projections give total boundedness, Fatou gives closedness, and Markov's
  inequality gives the probability tail.
- Proves the massive free Gaussian reference estimate:
  \(\sup_N\mathbb E_{\gamma_N}\|\phi\|_{H^{-\eta}}^2<\infty\) on
  \(\mathbb T^2\) for every \(\eta>0\).  The derivation reduces the second
  moment to
  \(\sum_{k\in\mathbb Z^2}(1+|k|^2)^{-1-\eta}\) and proves convergence by
  dyadic annuli, thereby giving free cutoff tightness in \(H^{-\kappa}\)
  whenever \(0<\eta<\kappa\).
- Proves an \(L^q\)-density criterion for interacting negative-Sobolev
  moments.  If \(\mu_N=\rho_N\gamma_N\), the Gaussian cutoffs have a uniform
  \(H^{-\eta}\) second moment, and \(\rho_N\) is uniformly bounded in
  \(L^q(\gamma_N)\) for some \(q>1\), then \(\mu_N\) has uniform
  \(H^{-\eta}\) moments of all finite orders.  The proof is self-contained:
  Holder's inequality reduces the estimate to Gaussian moments, and the
  latter are bounded by diagonalizing the covariance in \(H^{-\eta}\) and
  using \(\mathbb E(\sum_i\lambda_i g_i^2)^m\le
  (2m-1)!!(\sum_i\lambda_i)^m\).  The chapter records the resulting
  density route to \(\Phi^4_2\) stationary-law tightness: a uniform
  Nelson-type \(L^q\) bound for the normalized Wick-ordered density implies
  tightness in \(H^{-\kappa}\).
- Proves that Nelson exponential stability of the cutoff Wick quartic
  implies the normalized \(L^q\) density bound with no hidden normalization
  loss.  The proof uses Wick centering to show
  \(\mathbb E_{\mu_{0,N}}V_N=0\), Jensen's inequality to obtain the uniform
  lower bound \(Z_N\ge1\), and then the Nelson exponential estimate at
  exponent \(q\) to bound
  \(\|\rho_N\|_{L^q(\mu_{0,N})}^q=Z_N^{-q}\mathbb E e^{-qV_N}\).  The text
  distinguishes smooth-regulator stability covered by the quoted
  \(P(\phi)_2\) theorem from the still regulator-specific task of proving or
  comparing the same stability for a sharp Fourier-Galerkin stochastic
  regulator.
- Proves a bounded-cylinder regulator-comparison theorem from a common
  density limit.  If two cutoff schemes have cylinder coordinate vectors
  converging in probability to the same limit, their nonnegative interaction
  densities converge in \(L^1\) to the same limiting density, and the
  densities are uniformly \(L^p\)-bounded for some \(p>1\), then all bounded
  continuous cylinder expectations have the same normalized continuum limit.
  The proof treats the normalization constants by \(L^1\)-convergence and
  controls the term
  \(\int(F(X_N)-F(X))W_N\,d\gamma\) by convergence in probability plus
  uniform integrability from Holder.  This supplies a precise sufficient
  condition for the bounded-observable comparison required before transferring
  finite-cutoff OS positivity between regulators.
- Proves the common-potential corollary underneath the density comparison.
  If the two renormalized interaction functionals converge in probability to
  the same limiting potential and the exponential weights are uniformly
  \(L^p\)-bounded for some \(p>1\), then the weights converge in \(L^1\).
  The proof spells out the Vitali step: subsequential Fatou gives the
  limiting weight in \(L^p\), Holder gives uniform integrability of the
  cutoff weights plus the limit weight, and convergence in probability
  upgrades to \(L^1\).  This moves regulator comparison from an
  assumed-density statement to the potential-level stability estimate that
  constructive cutoff arguments can actually target.
- Proves a bounded Wick-cylinder comparison criterion for stable quartic
  cutoffs.  Given two cutoff schemes with common finite Wick-coordinate
  \(L^2\) limits, common \(L^2\) convergence of the Wick quartic potentials,
  and a uniform \(L^p\) bound on \(e^{-V_N^\sigma}\), all bounded continuous
  functions of the Wick-coordinate vector have the same normalized continuum
  expectation.  The proof checks the hypotheses of the common-potential
  theorem and uses Fatou to verify that the limiting weight is finite and
  has positive partition function.
- Proves a smooth-regulator consequence theorem from Nelson stability.  For
  smooth Fourier multiplier cutoffs satisfying uniform
  \(\sup_N E e^{-pV_N}<\infty\) for every finite \(p\), Jensen's inequality
  gives \(Z_N\ge1\), hence normalized \(L^q\) density bounds.  Holder
  against the massive Gaussian \(H^{-\eta}\) moments gives interacting
  \(H^{-\eta}\) moment bounds and tightness in \(H^{-\kappa}\).  Smooth
  multiplier covariance convergence plus the mixed-covariance Wick theorem
  gives common Wick-coordinate and potential limits, so the stable
  Wick-cylinder comparison theorem applies.
- Proves a finite-dimensional Brascamp-Lieb covariance domination theorem
  for convex scalar cutoffs.  The proof uses the symmetric generator
  \(\mathcal L=\Delta-\nabla S\cdot\nabla\), its Friedrichs resolvent, and
  the finite-dimensional Bochner identity to derive
  \(\operatorname{Var}_{\nu_N}(\ell_v)\le (v,A_N^{-1}v)\).  Applied to the
  spectral coordinates of a cutoff operator \(L_N\), this gives the
  interacting negative-Sobolev bound
  \[
    \int\|\phi\|_{H_N^{-\eta}}^2d\nu_N
    \le
    \sum_\alpha(1+\lambda_{N,\alpha})^{-\eta}
      (\lambda_{N,\alpha}+m^2)^{-1}
  \]
  whenever \(\nabla^2S_N\ge L_N+m^2{\bf 1}\) and the cutoff law is even.
- Proves closedness of OS reflection positivity under weak convergence for
  bounded positive-time cylinder observables, and isolates the additional
  uniform-integrability hypothesis needed to pass unbounded polynomial
  cylinder observables by truncation.
- Adds an explicit regulator-separation remark: Fourier-Galerkin cutoffs are
  used for stochastic estimates, while OS reflection positivity is a separate
  property of the Euclidean regulator and must either be assumed for that
  regulator or obtained by a regulator-comparison theorem.
- Proves that nearest-neighbor finite lattice scalar cutoffs with positive
  kinetic coefficients and reflection-invariant real on-site potential are
  OS reflection positive.  The proof expands each cross-plane factor
  \(\exp(c\phi_x\phi_{\vartheta x})\) into a nonnegative power series and
  writes the reflection quadratic form as a sum of half-lattice absolute
  squares.  The chapter then states precisely that this settles finite-cutoff
  positivity for the lattice regulator but not the comparison between lattice
  Schwinger functions and the Fourier-Galerkin stochastic family.
- Proves an abstract regulator-comparison criterion for transferring
  finite-cutoff lattice OS positivity to a Fourier-Galerkin stochastic
  continuum limit.  If the Fourier family converges weakly, the lattice
  family is OS-positive at finite cutoff, and bounded cylinder observables
  have matching expectations between the two regulators, then the limiting
  Fourier measure is OS-positive.  The same proposition treats unbounded
  polynomial cylinder observables by bounded truncation and uniform
  integrability, isolating exactly which analytic comparison estimate remains
  to be proved in \(\Phi^4_2\).
- Proves a de la Vallee Poussin-type criterion: exponential moment bounds for
  a finite list of cylinder coordinates imply uniform integrability of every
  polynomial cylinder observable built from those coordinates.  This supplies
  the exact condition needed to pass unbounded OS polynomial quadratic forms
  through weak limits.
- Proves finite-cutoff quartic exponential tails for finite lattice scalar
  regulators whose local potentials satisfy a quartic coercivity lower bound,
  while explicitly separating this finite-cutoff integrability statement from
  the uniform continuum estimates still required for tightness and OS
  polynomial limits.
- Adds a \(\Phi^4_2\) stochastic-quantization assembly theorem on the torus.
  The theorem now proves the path-space enhanced-noise input and makes
  explicit the remaining analytic inputs needed to pass from finite-cutoff
  invariant Wick-ordered measures to a limiting invariant Markov law and
  OS-positive Euclidean measure: the rough energy-to-Besov estimate that
  yields global compact-continuity of the DPD solution map, tightness of
  stationary cutoff laws, uniform integrability of the polynomial
  Wick-observable limits, and finite-cutoff reflection positivity or a
  regulator-comparison theorem.
- Proves the Sobolev DPD obstruction in three dimensions: the minimal
  multiplier threshold \(\beta>1/2+\kappa\) for \(YX\), combined with
  forcing regularity \(:X^3:\in H^{-3/2-3\kappa-\varepsilon}\), forces a
  Duhamel smoothing exponent \(\theta>1+2\kappa\), contradicting the
  integrability requirement \(\theta<1\).
- Develops the Da Prato--Debussche decomposition for `Phi^4_2`, identifies
  the role of the enhanced noise, proves a Sobolev local fixed-point version,
  proves the Besov-Holder local fixed-point mechanism, and records the
  sharper global closure as a concrete estimate ledger: the local
  rough-forcing estimate, Nelson stability for the chosen Wick quartic cutoff
  family, regulator comparison, uniform integrability, and OS-II growth.
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
- Proves a heat-integration reexpansion estimate: if a negative distribution
  of assigned homogeneity \(\alpha\) has true regularity \(\alpha+\sigma\),
  then the constant coefficient in \(\mathcal I\tau\) has assigned
  homogeneity \(\beta=\alpha+2\) and normalized scale slack \(\sigma\).
  Applied to \(Y=\mathcal I(X^3)\), this transfers the \(X^3\) slack
  \(3\kappa\) to the \(c_n\)-coordinate.
- Proves the finite-cutoff Wick decomposition of the nonlinear negative
  coordinates \(XY\) and \(X^2Y\).  The \(XY\) coordinate splits into fourth-
  and second-chaos pieces with contraction coefficient \(3\).  The BPHZ
  \(X^2Y\) coordinate splits into fifth-, third-, and locally subtracted
  first-chaos pieces, with coefficients \(1,6,6\) and local subtraction
  \(3C_{2,\epsilon}X_\epsilon\).  This identifies the exact kernels whose
  analytic estimates must produce slacks \(4\kappa\) and \(5\kappa\).
- Proves the tested finite-chaos kernel formulas for the nonlinear negative
  coordinates: after pairing with a test density \(\chi\), \(XY\) is
  \(I_4(F_{XY,4}^{\chi})+I_2(F_{XY,2}^{\chi})\), while locally subtracted
  \(X^2Y\) is
  \(I_5(F_{X^2Y,5}^{\chi})+I_3(F_{X^2Y,3}^{\chi})+
  I_1(F_{X^2Y,1}^{\chi})\), with
  \(F_{X^2Y,1}^{\chi}\) containing the precise difference
  \(p_\epsilon(b)-p_\epsilon(a)\).
- Proves exact covariance-integral formulas for the Hilbert norms of the
  tested nonlinear kernels.  The symmetrization weights are
  \((1/4,3/4)\) for \(XY\)'s fourth chaos, \((1/10,3/5,3/10)\) for
  \(X^2Y\)'s fifth chaos, and \((1/3,2/3)\) for \(X^2Y\)'s third chaos.
  The first-chaos formula contains the increment covariance
  \(G_{bb'}-G_{ba'}-G_{ab'}+G_{aa'}\), making the Taylor-subtraction gain
  visible in scalar-kernel form.
- Proves the scalar tested \(XY\) coordinate estimate from the marginal
  four-vertex graph ledger.  The covariance-graph bound gives
  \(\mathbb E|Z_{\epsilon,\delta,z}^{XY}|^2=O_\eta(\delta^{-\eta})\);
  finite-chaos moment control then yields the normalized model-coordinate
  bound
  \(\|\delta^{4\kappa}Z_{\epsilon,\delta,z}^{XY}\|_{L^p}
  =O(\delta^{4\kappa-\zeta_{XY}})\) for every
  \(0<\zeta_{XY}<4\kappa\).  The same graph estimate, combined with the
  \(L^1\)-Lipschitz dependence of transported \(C^1\) tests on
  \(d_{\Pi,m}\), gives the same-scale parameter-edge bound
  \(O(2^{-(4\kappa-\zeta_{XY})m}d_{\Pi,m}(u,v)^\theta)\) after model
  normalization.  A cutoff-shell version shows that, when one heat or
  covariance edge is forced into the dyadic ultraviolet shell \(n\), the
  smallest proper-subgraph deficit gives the scalar Cauchy gain
  \(2^{-\rho(n-m)_+}\) for every \(0<\rho<1/2\).  The scale-summed
  shell-separated cutoff bridge then turns this scalar gain into
  \(2^{-\rho_*n}\) for every
  \(\rho_*<\min\{\rho,\sigma-D/p\}\), provided the physical-scale slack
  beats entropy.  The dossier records these as scalar tested base, edge,
  scale-separated shell-gain, and scale-summed shell-bridge estimates.  The
  abstract \(E_r'\)-projective shell bridge and its nonlinear
  \(\Pi\)-coordinate specialization are now supplied separately; the
  remaining obligation is the regulator-specific projective kernel estimate
  that promotes the scalar \(XY\) shell gain and the full \(X^2Y\) shell
  gain, including the first-chaos covariance-increment sector, to those
  abstract hypotheses.
- Proves the scalar tested high-chaos \(X^2Y\) estimate separately from the
  locally subtracted first-chaos sector.  The three fifth-chaos graphs and
  two third-chaos graphs have total singular degree
  \(Q(|V|-2)+1=11\); fifth-chaos proper subgraphs have minimum deficit \(2\),
  third-chaos proper subgraphs have minimum deficit \(1\), and all
  relative-scale sums are geometric.  The remaining overall-scale sum gives
  \(\mathbb E|Z_{\epsilon,\delta,z}^{X^2Y,\ge3}|^2=O(\delta^{-1})\), hence
  \(\|\delta^{1/2+5\kappa}Z_{\epsilon,\delta,z}^{X^2Y,\ge3}\|_{L^p}
  =O(\delta^{5\kappa})\).  The same homogeneous graph estimate gives the
  same-scale parameter-edge bound
  \[
    \mathbb E|Z_{\epsilon,m,v}^{X^2Y,\ge3}
      -Z_{\epsilon,m,u}^{X^2Y,\ge3}|^2
    \le C_\theta 2^m d_{\Pi,m}(u,v)^{2\theta},
  \]
  hence \(2^{-5\kappa m}d_{\Pi,m}(u,v)^\theta\) after model normalization.
  If one heat or covariance edge is forced into the ultraviolet cutoff shell,
  the minimum proper-subgraph deficit gives
  \(C_\rho2^m2^{-2\rho(n-m)_+}\) in variance and
  \(2^{-5\kappa m}2^{-\rho(n-m)_+}\) after normalization, for every
  \(0<\rho<1/2\).  The only logarithmic slack in scalar \(X^2Y\) control now
  comes from the first-chaos covariance-increment estimate.
- Proves a deterministic scale bound for the locally subtracted
  \(X^2Y\) first-chaos kernel: under shell \(L^1\) bounds for the local
  \(KG^2\) packets and dyadic double-increment bounds for the order-four
  covariance blocks, the first-chaos variance is
  \(O(\delta^{-1}(1+|\log\delta|)^2)\).  Consequently the normalized
  \(X^2Y\) first-chaos coordinate has every slack strictly below
  \(5\kappa\), with the logarithm explicitly accounted for rather than
  hidden.  The cutoff increment
  \(V_{\delta,N+1}^{(1)}-V_{\delta,N}^{(1)}\) is also bounded with
  scale-separated variance gain
  \[
    C_\rho\delta^{-1}(1+m_\delta)^2
    2^{-2\rho(N-m_\delta)_+},\qquad 0<\rho<\theta/2,
  \]
  and therefore the normalized \(L^2\) cutoff increment has gain
  \(2^{-\rho(N-m_\delta)_+}\) after the same logarithmic slack loss.  The
  signed-test version of the same argument proves same-scale and cutoff
  parameter-edge estimates: the transported-test difference satisfies both
  \(L^1\) and scale-normalized \(L^\infty\) bounds, so the first-chaos
  overlap estimate gains \(d_{\Pi,m}(u,v)^{2\vartheta}\).  After Gaussian
  \(L^p\) control and model normalization, the first-chaos edge bounds carry
  \(2^{-(5\kappa-\eta)m}d_{\Pi,m}(u,v)^\vartheta\), and the cutoff edge has
  the additional shell factor \(2^{-\rho(N-m)_+}\).
- Verifies the local \(KG^2\) shell \(L^1\) hypothesis used in that
  first-chaos bound for dynamic \(\Phi^4_3\): heat order \(2\) and
  covariance order \(4,4\) give relative gaps \(3,1,1\), and the shell
  \(\max(i,j,\ell)=n\) is uniformly summable.
- Verifies the covariance double-increment hypothesis used in the same
  first-chaos bound for compact dyadic order-four covariance blocks.  The
  proof rescales \(C_s(a,a')\) to \(2^s c_s(\mathsf D_{2^s}(a-a'))\), proves
  the mixed scale-one finite-difference estimate from uniform \(C^2\) control,
  and converts the local supports \(2^{-n}\), \(2^{-n'}\) into the factors
  \(2^{-\theta(n-s)_+}\), \(2^{-\theta(n'-s)_+}\).
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
- Proves a scale-summed shell-separated cutoff bridge: if the cutoff increment
  carries \(2^{-\rho(n-m)_+}\) rather than a uniform \(2^{-\rho n}\), then
  the scale supremum still has a dyadic cutoff-Cauchy rate
  \(2^{-\rho_*n}\) for every
  \(0<\rho_*<\min\{\rho,\sigma-D/p\}\).  The proof splits the physical-scale
  sum at \(m=n\) and bounds the lower-scale part by a convolution of two
  geometric sequences with exponents \(a-\rho_*\) and \(\rho-\rho_*\).
- Proves a projective shell-separated coordinate criterion: if the
  \(E'\)-valued finite-chaos kernels satisfy projective base and
  parameter-edge bounds with the shell factor \(2^{-\rho(n-m)_+}\), then the
  finite-chaos estimate, norm-Lipschitz inequality, dyadic-net theorem, and
  shell-summation bridge combine to give the scale-summed cutoff-Cauchy
  dual-norm estimate.  This closes the abstract route from projective
  \(E_r'\)-kernel estimates to model-coordinate Cauchy bounds; the
  regulator-specific proof still has to supply those projective estimates for
  \(XY\), \(X^2Y\), and the remaining negative-sector coordinates.
- Specializes the projective shell-separated coordinate criterion to the
  nonlinear \(\Pi\)-coordinates \(XY\) and \(X^2Y\): shell-separated
  projective cutoff-increment bounds with scale gain
  \(2^{-\rho_\tau(n-m)_+}\) imply the scale-summed \(E_r'\)-dual-norm
  cutoff-Cauchy estimate with retained rate
  \(2^{-\rho_\tau^*n}\) for every
  \(0<\rho_\tau^*<\min\{\rho_\tau,\sigma_\tau-5/p\}\).  The constants are
  displayed in terms of \(H_{\rho_\tau^*,\rho_\tau,\sigma_\tau-5/p}\), the
  \(\Pi\)-net entropy constants, and
  \(\widehat A_{\tau,i}=\sum_q C_{q,m_0}\widehat B_{\tau,q,i}\).
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
- Adds the common Schwinger-hierarchy comparison construction: if the SPDE
  stationary law and constructive Euclidean measure are placed in the same
  field/mass/counterterm chart, their moment functionals are continuous, and
  they agree on a dense test-function subspace, then the two tempered
  Schwinger hierarchies coincide.  OS positivity, covariance, corrected OS-II
  growth, clustering, and the reconstructed Wightman data transfer through
  this hierarchy equality.  The model-specific equality of those hierarchies
  remains an analytic proof obligation rather than a consequence of Markov
  stationarity alone.
- Records a self-contained singular-SPDE proof stack as an open obligation:
  Wick powers, Schauder and multiplication estimates, energy estimates,
  invariant-law identification, BPHZ model convergence, fixed points in
  modelled distributions, and SPDE-to-OS passage.
- Proves the fixed-point-sector comparison criterion: if the cutoff and
  limiting modelled-SPDE maps are contractions on a common ball and their
  sup-norm map error tends to zero, then their fixed points converge with
  error \(\epsilon_n/(1-q)\).  The chapter also decomposes the map error into
  stochastic-convolution, heat-integration, cubic-product, linear-term, and
  mass-coordinate comparison errors.
- Proves the coupled stationary-law comparison lemma: if stationary cutoff
  solutions and the limiting Markov solution are realized on a common
  probability space with time-zero defect \(\delta_n\) and finite-time defect
  \(a_t\delta_n+\epsilon_{n,t}\), then the limiting law is invariant for the
  limiting Markov semigroup on bounded Lipschitz test functions.  The dossier
  keeps this separate from the common Schwinger-hierarchy comparison, which is
  still the layer needed for polynomial moments, OS positivity, and Wightman
  reconstruction.

## Figure Ledger

No figure is included in this pass.  Future figures should include Markov
flow to invariant measure, covariance-scale decompositions, and SPDE-to-OS
data maps.

## Audit Notes

- 2026-05-25 issue #575 pass: the Da Prato--Debussche solution mechanism,
  Hairer reconstruction theorem, and renormalized dynamic \(\Phi^4_3\) SPDE
  datum were separated from ordinary theorem/proof presentation.  The
  remaining theorem-boundary text is written as role/status material, and
  Open Problem
  `op:self-contained-singular-spde-proof-stack` records the monograph's
  obligation to prove the quoted SPDE results internally rather than accept
  them on authority.
- 2026-06-02 finite-cutoff Langevin reversibility pass: upgraded the opening
  finite-dimensional Langevin identity from an infinitesimal
  integration-by-parts statement to a semigroup-level reversibility lemma
  under explicit essential self-adjointness and conservativeness hypotheses.
  The \(\Phi^4_2\) assembly proof now invokes this lemma when it uses
  finite-cutoff stationarity, and
  `calculation-checks/constructive_scalar_spde_checks.py` now includes an
  exact rational two-mode check of the Dirichlet identity, generator
  symmetry, and constant conservation with the \(\sqrt2\) noise
  normalization.
- 2026-06-02 SPDE/constructive hierarchy-comparison pass: added the explicit
  common-Schwinger-hierarchy construction between stationary SPDE laws and
  constructive Euclidean measures in a shared renormalization chart.  The pass
  makes clear that OS/Wightman data transfer through equality of tempered
  Schwinger distributions, with bounded-cylinder comparison upgraded to
  polynomial cylinders only through the uniform-integrability criteria proved
  earlier.  The companion finite check verifies matching OS Gram matrices,
  polynomial quadratic forms, and transferred growth envelopes from an
  identical moment vector.
- 2026-06-02 SPDE fixed-point-sector comparison pass: added the contraction
  stability criterion needed after random-model convergence.  The new
  proposition proves that a common-ball contraction error
  \(\epsilon_n=\sup_{\mathbb B_R}\|\Psi_n-\Psi_\infty\|\) gives solution
  convergence \(\|U_n-U_\infty\|\le\epsilon_n/(1-q)\), and decomposes
  \(\epsilon_n\) into the modelled-SPDE data errors
  \(\delta_Y,\delta_K,\delta_P,\delta_L,\delta_M\).  The companion check
  verifies both the sharp affine contraction bound and the finite arithmetic
  of the error budget.
- 2026-06-02 SPDE stationary-law coupling pass: added the bounded-Lipschitz
  invariant-law bridge after finite-time SPDE convergence.  The lemma compares
  a stationary cutoff pair \(U_n(0),U_n(t)\) with a limiting pair
  \(U_*(0),U_*(t)\), proving the explicit defect
  \(\operatorname{Lip}(f)((a_t+1)\delta_n+\epsilon_{n,t})\).  The companion
  check verifies the rational arithmetic of the zero-time and finite-time
  defects and records that a nonvanishing finite-time residual cannot imply
  invariance.
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
  estimate treated as deterministic estimate rather than theorem-family
  wrapper.  The calculation-check companion verifies the OU variance,
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
- 2026-05-26 issue #582 reexpansion continuation: the chapter now proves the
  deterministic heat-integration estimate that turns an \(X^3\)-type
  distribution with true regularity \(-3/2\) into the constant reexpansion
  coefficient of \(Y=\mathcal I(X^3)\), normalized by
  \(|Y|=1/2-3\kappa\), with slack \(3\kappa\).  The proof splits heat-kernel
  scales at the physical separation and proves both the fine-scale tail and
  the coarse translation-gain bound.  The calculation-check companion verifies
  the homogeneity and coarse/fine exponent arithmetic.
- 2026-05-26 issue #582 nonlinear-coordinate continuation: the chapter now
  identifies the finite-cutoff chaos decompositions for \(XY\) and the
  locally subtracted \(X^2Y\) coordinate.  The calculation-check companion
  verifies the Wick contraction coefficients, the \(3C_2\) local subtraction
  normalization, the resulting \(9C_2\) mass-coordinate coefficient before
  coupling signs, the tested finite-chaos arities, and the target scale
  slacks \(4\kappa\) and \(5\kappa\).
- 2026-05-26 issue #582 nonlinear-kernel continuation: the chapter now
  converts the finite-cutoff Wick identities into explicit Hilbert-space
  finite-chaos kernels for tested \(XY\) and \(X^2Y\) coordinates.  This
  pins the analytic target to projective/Hilbert kernel estimates for the
  displayed kernels rather than informal products of distributions.
- 2026-05-26 issue #582 covariance-integral continuation: the chapter now
  expands those Hilbert-kernel norms into scalar covariance integrals with
  exact symmetrization coefficients and the first-chaos increment covariance.
  The next analytic pass can estimate explicit scalar kernels rather than
  infer the cancellation from notation.
- 2026-05-26 issue #582 first-chaos analytic continuation: the chapter now
  proves the first deterministic parabolic-scale estimate for the locally
  subtracted \(X^2Y\) first-chaos kernel.  The proof keeps the two local
  logarithmic shell factors and absorbs them only as an arbitrarily small
  loss of the available \(5\kappa\) slack.
- 2026-05-26 issue #582 local-shell verification: added the corollary
  deriving the \(KG^2\) local shell \(L^1\) hypothesis from the already
  established heat/covariance/covariance order arithmetic \((2,4,4)\).
- 2026-05-26 issue #582 covariance-increment verification: added the
  corollary proving the order-four covariance block double-increment bound
  from compact rescaled \(C^2\) block control, discharging the second
  deterministic hypothesis in the locally subtracted first-chaos estimate.
- 2026-05-26 issue #608 first pass: added the \(\Phi^4_2\)
  stochastic-quantization assembly theorem and the explicit three-dimensional
  Sobolev DPD obstruction.  This addresses the review weakness that the
  two-dimensional DPD pieces were present but not assembled into a theorem,
  while keeping the still-required rough Besov/Holder estimates as visible
  hypotheses rather than hidden folklore.
- 2026-05-26 issue #608 integrability pass: added the exponential-moment
  criterion for uniform integrability of polynomial OS cylinder observables
  and the finite-lattice quartic-tail proposition.  The calculation-check
  companion now verifies the one-site quartic moment scaling, the coercivity
  Young inequality, and the polynomial-by-exponential tail domination used in
  the proof.  The pass deliberately does not claim continuum tightness or
  uniform moment bounds; those remain constructive estimates.
- 2026-05-26 issue #608 tightness pass: added the Sobolev compactness
  criterion proving that a cutoff-uniform \(H^{-\eta}\) moment with
  \(0<\eta<\kappa\) implies tightness in \(H^{-\kappa}\).  The proof spells
  out the compact embedding by Fourier projection and records the exact
  Markov-tail estimate; the calculation-check companion verifies the
  Hilbert-scale exponent and sample Markov arithmetic.
- 2026-05-26 issue #608 Gaussian reference pass: added the massive free
  Gaussian negative-Sobolev moment estimate on \(\mathbb T^2\), including
  the dyadic annulus summability proof for
  \(\sum_k\langle k\rangle^{-2-2\eta}\).  The calculation-check companion
  verifies the two-dimensional shell exponent and the sample dyadic
  geometric sum.
- 2026-05-26 issue #608 convex-interacting pass: added a self-contained
  Brascamp-Lieb/Bochner-resolvent covariance domination theorem for
  uniformly convex finite-dimensional scalar cutoffs and derived the
  corresponding interacting negative-Sobolev moment bound.  The
  calculation-check companion verifies the weighted spectral-trace arithmetic
  and the inverse-monotonicity sample used in the proof.
- 2026-05-26 rough-energy closedness pass: added a theorem passing the DPD
  integrated energy inequality from smooth enhanced-noise approximants to a
  weak energy limit.  The calculation-check companion verifies the Holder
  conjugacy arithmetic behind the \(L^p\)-power continuity step for the
  \(L^4\), \(L^2\), and \(L^{4/3}\) enhanced-noise norms.
- 2026-05-26 rough-energy compactness pass: added the theorem deriving
  weak compactness, a time-derivative bound, and terminal weak \(L^2\)
  convergence for smooth DPD remainders from the same energy inputs.  The
  calculation-check companion verifies the \(L^{4/3}\) drift exponents
  behind the \(\partial_tY_n\) estimate.
- 2026-05-26 DPD distributional-limit pass: added a Fourier proof of the
  torus Aubin-Lions compactness input and a proposition identifying the
  compactness limit as a distributional DPD solution under strong Lebesgue
  convergence of the enhanced-noise approximants.  The calculation-check
  companion verifies the interpolation and product exponents.
- 2026-05-26 DPD Besov-product pass: added the self-contained
  Besov-Holder product-continuity theorem for the rough DPD nonlinearity,
  replacing a named placeholder in the smooth-to-rough roadmap by an actual
  paraproduct proof.  The calculation-check companion verifies the sample
  resonance, embedding, and algebra exponents.
- 2026-05-26 DPD Besov fixed-point pass: added the heat-smoothing estimate
  in Besov-Holder spaces and the corresponding deterministic local mild
  fixed-point theorem for rough enhanced noise, including local Lipschitz
  dependence.  The calculation-check companion verifies the Duhamel
  exponent \(\theta=(\alpha+\kappa)/2<1\) and the target regularity
  arithmetic.
- 2026-05-26 DPD Besov-energy compatibility pass: added the theorem
  identifying the Besov local fixed point with smooth energy-compactness
  limits when both the Besov enhanced-noise convergence and the Lebesgue
  energy convergence hypotheses hold.  The pass also removed a duplicated
  sentence in the Fourier Aubin-Lions proof and added a calculation-check
  companion for the exponent arithmetic used in the compatibility argument.
- 2026-05-26 regulator-comparison criterion pass: added the theorem-level
  criterion that transfers OS positivity from an OS-positive lattice cutoff
  family to a Fourier-Galerkin stochastic limit once bounded-cylinder
  comparison and polynomial uniform integrability are proved.  The assembly
  theorem now points to this criterion rather than leaving regulator
  comparison as an unnamed gap.
- 2026-05-26 SPDE-to-OS reconstruction pass: added a theorem-level criterion
  for when an SPDE invariant law actually supplies OS reconstruction data.
  The proposition states the precise moment-continuity, Euclidean covariance,
  polynomial reflection positivity, positive-time semigroup, and corrected
  OS-II linear-growth inputs needed to apply the reconstruction theorem.  The
  \(\Phi^4_2\) assembly theorem now points to this criterion instead of
  saying only that "usual growth hypotheses" remain.  The calculation-check
  companion verifies the linear seminorm-order bookkeeping for reflected
  positive-time tests.
- 2026-05-26 rough-forcing bootstrap pass: added a deterministic proposition
  converting a localized rough forcing estimate into the global
  energy-to-Besov bound required by the compact-continuity criterion.  This
  no longer leaves the phrase "rough energy-to-Besov" as an undefined slogan:
  the remaining stochastic/coercive task is the concrete interval estimate
  with no unabsorbed positive power of the Besov continuation norm.  The
  calculation-check companion verifies the absorption and recursion
  arithmetic.
- 2026-05-26 singular-SPDE ledger pass: revised the monograph open-problem
  ledger so it no longer lists already-proved \(\Phi^4_2\) infrastructure as
  quoted theorem-boundary material.  The remaining two-dimensional tasks are
  now the rough-forcing estimate, regulator-specific Nelson stability, and
  OS-II reconstruction inputs; the remaining \(\Phi^4_3\) tasks are the
  concrete BPHZ coordinate moment/cutoff-Cauchy estimates, extension from the
  strict negative sector to the full fixed-point sector, counterterm
  identification, invariant-law comparison, and SPDE-to-OS passage.
- 2026-05-26 Gaussian negative-sector input pass: promoted the Gaussian
  \(\Xi,X,X^2,X^3\) \(\Pi\)-coordinate assembly from prose to a theorem-level
  proposition.  The new result constructs the scale-summed coordinate fields
  on \(K\times[1/2,1]\), proves the explicit base and edge moment bounds with
  \(\sigma_\Xi=\kappa\), \(\sigma_{X^k}=k\kappa\), and
  \(\varepsilon=p\theta-6\), and records the exact moment conditions
  \(p\kappa>5\), \(p\theta>6\) needed to feed the negative-sector model
  convergence theorem.  The calculation-check companion verifies this
  entropy/slack arithmetic.
- 2026-05-26 Gamma heat-coordinate input pass: promoted the \(c_n\)
  reexpansion coefficient from a deterministic Schauder observation to a
  theorem-level \(\Gamma\)-coordinate input.  The new proposition proves the
  base and edge moment estimates from the \(X^3\) distribution norm, records
  \(D_{\mathfrak g}=5\), \(d_{\mathfrak g}=10\),
  \(\sigma_{\mathfrak g}=3\kappa\), and
  \(\varepsilon_{\mathfrak g}=p\theta-10\), and states the cutoff-Cauchy
  transfer separately.  The calculation-check companion verifies the
  heat-coordinate entropy/slack arithmetic.
- 2026-05-26 nonlinear Pi-kernel input pass: added a theorem-level criterion
  converting projective \(E_r'\)-valued kernel bounds for \(XY\) and the
  locally subtracted \(X^2Y\) into the \(\Pi\)-coordinate hypotheses of the
  strict negative-sector model theorem.  The criterion records
  \(\sigma_{XY}=4\kappa-\zeta_{XY}\),
  \(\sigma_{X^2Y}=5\kappa-\zeta_{X^2Y}\), the entropy data \(D=5,d=6\),
  and the exact high-moment conditions \(p\sigma_\tau>5\), \(p\theta>6\).
  A companion \(XY\) graph proposition proves the logarithmic power-counting
  bound from the marginal total degree and positive proper-subgraph deficits
  of the fourth- and second-chaos covariance graphs; the calculation-check
  companion verifies both that graph arithmetic and the sample nonlinear
  entropy/slack arithmetic.
- 2026-06-01 issue #608/#582 scalar \(XY\) coordinate pass: added the
  proposition converting the marginal \(XY\) graph ledger into the scalar
  tested normalized bound
  \(\|\delta^{4\kappa}Z_{\epsilon,\delta,z}^{XY}\|_{L^p}
  \lesssim \delta^{4\kappa-\zeta_{XY}}\).  This closes the scalar base
  estimate beneath the nonlinear \(\Pi\)-coordinate criterion and leaves the
  full \(E_r'\)-dualized parameter-edge estimate as the next analytic layer.
- 2026-06-01 issue #608/#582 scalar \(XY\) edge pass: added the same-scale
  parameter-edge estimate for the tested \(XY\) coordinate.  The proof
  derives the \(L^1\)-variation of transported \(C^1\) tests under the
  physical metric \(d_{\Pi,m}\), applies the homogeneous covariance-graph
  estimate to the signed test difference, and obtains the normalized
  \(2^{-(4\kappa-\zeta_{XY})m}d_{\Pi,m}(u,v)^\theta\) bound.  This advances
  the nonlinear \(XY\) coordinate from scalar base control to scalar edge
  control; the remaining analytic layer is the full \(E_r'\)-projective
  model-seminorm estimate and cutoff-increment analogues.
- 2026-06-01 issue #608/#582 scalar \(XY\) cutoff-shell pass: added the
  scalar dyadic-cutoff shell-gain estimate for the tested \(XY\) coordinate.
  The proof expands the cutoff increment in the finite-chaos covariance
  graphs, uses the fact that one heat/covariance edge is constrained to the
  ultraviolet shell, and converts the minimum proper-subgraph deficit \(1\)
  into the normalized Cauchy factor
  \(2^{-(4\kappa-\zeta_{XY})m}2^{-\rho(n-m)_+}\) for every
	  \(0<\rho<1/2\).  The remark in the chapter explicitly prevents overclaim:
	  this is a scalar scale-separated Cauchy layer, not the full
	  \(E_r'\)-projective cutoff increment required by the model-convergence
	  theorem.
- 2026-06-01 issue #608/#582 shell-summation bridge pass: added the
  deterministic scale-summed shell-separated cutoff corollary.  It proves that
  scalar cutoff factors \(2^{-\rho(n-m)_+}\) produce an actual scale-summed
  cutoff-Cauchy rate \(2^{-\rho_*n}\) once
  \(0<\rho_*<\min\{\rho,\sigma-D/p\}\), with the constant
  \(H_{\rho_*,\rho,a}\) explicitly defined and bounded.  The calculation
  companion now checks the split \(m\le n\), the high-scale tail, and the
  exact dyadic sample \(S_5=221/98304\).
- 2026-06-01 issue #608/#582 projective shell bridge pass: added the
  projective shell-separated coordinate criterion.  The proof first sums
  projective kernel constants with the finite-chaos constants to form
  \(B_\pi\) and \(B_\pi^{ed}\), then applies the dyadic-net theorem to the
  scalar norm field \(\|Y_{n,m}(x)\|_{E'}\), and finally invokes the
  shell-summation bridge.  The calculation companion checks the finite-chaos
  aggregation, the edge exponent conversion from projective norm to
  \(p\)-th-moment entropy decay, and the final \(H_{\rho_*,\rho,a}\)-bound.
  This is an abstract bridge; concrete \(E_r'\)-projective cutoff-increment
  estimates for the nonlinear model kernels remain open.
- 2026-06-02 issue #608/#582 nonlinear projective-shell specialization pass:
  added the nonlinear \(\Pi\)-coordinate corollary that specializes the
  abstract projective shell bridge to \(XY\) and \(X^2Y\).  The statement
  replaces the earlier uniform \(2^{-\rho n}\) cutoff input by
  \(2^{-\rho_\tau(n-m)_+}\), keeps the finite-chaos constants visible through
  \(\widehat A_{\tau,i}\), and proves the retained scale-summed rate
  \(2^{-\rho_\tau^*n}\) under
  \(0<\rho_\tau^*<\min\{\rho_\tau,\sigma_\tau-5/p\}\).  The calculation
  companion verifies the sample \(XY\) entropy/slack arithmetic
  \(D=5,d=6,p=80,\sigma_{XY}=3/20\), the admissible retained rate
  \(\rho_*<7/80\), and the finite-chaos aggregation
  \(\widehat A_0=13,\widehat A_1=11\).  This pass closes the abstract
  nonlinear coordinate-to-shell bridge; it does not claim the
  regulator-specific \(E_r'\)-projective kernel estimates.
- 2026-06-02 issue #608/#582 \(X^2Y\) high-chaos scalar pass: added the
  finite graph-power-counting estimate for the fifth- and third-chaos pieces
  of the locally subtracted \(X^2Y\) coordinate.  The pass displays all five
  covariance multigraphs, proves total degree \(11=Q(|V|-2)+1\), checks the
  proper-subgraph deficits, and derives the sharp scalar variance
  \(O(\delta^{-1})\).  The calculation companion verifies the graph
  arithmetic and normalized \(5\kappa\) slack exactly.  This closes a scalar
  high-chaos input beneath the nonlinear \(\Pi\)-coordinate criterion; the
  full regulator-specific \(E_r'\)-projective kernel estimates and invariant
  law/OS assembly remain open.
- 2026-06-02 issue #608/#582 \(X^2Y\) high-chaos edge/shell pass: added the
  same-scale parameter-edge and dyadic cutoff-shell estimates for the
  fifth- and third-chaos \(X^2Y\) sector.  The edge proof uses the
  homogeneous external-test-density form of the graph estimate, not a new
  normalization convention.  The shell proof records the admissible
  shell-representation hypothesis and uses the minimum proper-subgraph
  deficit \(1\) to retain any \(0<\rho<1/2\) after passing to \(L^p\).  The
  companion calculation check verifies the variance exponent, normalized
  slack, Holder edge exponent, and shell-gain ceiling.  The first-chaos
  covariance-increment sector, \(E_r'\)-projective estimates, invariant-law
  comparison, and OS assembly remain open.
- 2026-06-02 issue #608/#582 \(X^2Y\) first-chaos cutoff-shell pass: added the
  scale-separated cutoff increment estimate for the locally subtracted
  first-chaos covariance-increment sector.  The proof decomposes the cutoff
  difference into the three true shell cases: covariance block at scale
  \(N+1\), first local \(KG^2\) packet at scale \(N+1\), or second local
  \(KG^2\) packet at scale \(N+1\).  The covariance-shell case gains
  \(Q-1=4\) powers past the physical testing scale; the local-shell cases
  gain \(\theta\) powers after summing the lower cross scales, so the
  retained variance rate is \(2^{-2\rho(N-m_\delta)_+}\) for
  \(0<\rho<\theta/2\).  The companion calculation check verifies these
  exponent comparisons.  This closes the scalar first-chaos cutoff layer;
  the \(E_r'\)-projective lift, invariant-law comparison, and OS assembly
  remain open.
- 2026-06-02 issue #608/#582 \(X^2Y\) first-chaos parameter-edge pass: added
  the signed-test version of the locally subtracted first-chaos estimate.
  The proof records both the \(L^1\) and \(L^\infty\) variation of transported
  physical tests, derives the signed overlap bound
  \(d_{\Pi,m}^{2\vartheta}\min\{1,2^{5m}2^{-5s}\}\), and propagates it through
  the base and cutoff-shell first-chaos sums.  The companion calculation check
  verifies the normalized \(5\kappa-\eta\) slack, the edge entropy inequality
  \(p\vartheta>6\), the physical-scale entropy inequality
  \(p(5\kappa-\eta)>5\), and the retained cutoff-edge gain
  \(\rho<\theta/2\).  This closes the scalar first-chaos same-scale and
  cutoff-edge layers; the full \(E_r'\)-projective uniformization,
  invariant-law comparison, and OS assembly remain open.
- 2026-05-29 seventh anti-wrapper pass: demoted the finite-dimensional
  Langevin invariant-density identity from proposition form to an integration
  by parts calculation, while strengthening the stationary Ornstein-Uhlenbeck
  covariance proof with the \(L^2\) construction, complex Fourier-mode
  covariance convention, finite-cutoff Parseval identity, and monotone
  convergence to the negative-Sobolev bound.
- 2026-05-29 eighth anti-wrapper pass: demoted the parabolic
  Taylor-subtraction \(L^1\) scale gain from lemma form to an explicit
  calculation around `eq:spde-taylor-subtraction-gain`, and rewired later
  references to the equation rather than to a theorem-family wrapper.
- 2026-05-31 issue #701 structural-navigation pass: split the two giant
  sections of the chapter into mathematically meaningful subsections without
  changing theorem content.  The DPD section is now navigable by local
  product/fixed-point estimates, energy compactness, invariant-law/tightness,
  regulator/OS assembly, and the three-dimensional obstruction.  The
  regularity-structure section is now navigable by model/reconstruction
  input, random-model/finite-chaos coordinates, multiscale local
  subtractions, finite-sector coordinate-to-model convergence, and nonlinear
  negative-coordinate shell bounds.
- 2026-06-02 issue #608/#582 quoted-boundary audit: demoted the residual
  Da Prato--Debussche quoted theorem block to a sharp-closure status
  paragraph.  The two-dimensional stochastic-quantization proof boundary now
  consists only of the named estimates listed in the assembly hypothesis and
  open problem, while the single remaining quoted theorem boundary in the
  chapter is the dynamic \(\Phi^4_3\) regularity-structures package.
