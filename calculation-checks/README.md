# Calculation Checks

This directory contains public-facing scripts that verify convention-sensitive
algebra used in the monograph.  They are not substitutes for the derivations
in the text; they are reproducible checks of signs, trace normalizations, and
finite algebraic reductions.

Plain text formats are preferred over notebook-only formats.  Mathematica
checks should be committed as Wolfram Language `.wl` files, with optional
notebooks generated from them when useful.  Computationally heavy checks
should be written in Python rather than Mathematica; Wolfram Language files in
this directory should stay lightweight and reader-readable.

Current checks:

- `anomalous_transport_checks.py`: finite arithmetic checks for the chiral
  magnetic and chiral vortical coefficients, including the equilibrium
  Chern--Simons variation, the \(e^2q^2\) electromagnetic charge factor, and
  the cancellation of the Dirac vector-current \(T^2\) vortical term.
- `anomaly_matching_wzw_checks.py`: exact rational checks for the anomaly
  matching and Wess--Zumino--Witten coefficient section, including
  \(n=N_c\) from matching the left-flavor anomaly, vector-flavor anomaly
  cancellation between the two chiral components of a Dirac quark, and
  \(\operatorname{Tr}(T^3\{q,q\})=1/3\) for the
  \(\pi^0\gamma\gamma\) normalization.
- `anomaly_polynomial_descent_checks.py`: exact rational checks for the
  index-normalized anomaly-polynomial and inflow sections, including the
  six-form \(\widehat A\,\operatorname{ch}\) coefficients, the
  \(2\pi\ii\) conversion to effective-action inflow, one-generation Standard
  Model hypercharge sums, and \(SU(N)\) fundamental/antifundamental/adjoint
  cubic-anomaly bookkeeping.
- `background_index_theory_checks.py`: exact rational checks for the
  Volume XII background-index-theory chapter, including the
  four-dimensional \(\widehat A\,\operatorname{ch}\) index formula,
  trace-delta \(SU(N)\) instanton indices, the Abelian \(T^4\) flux index,
  the six-form anomaly-polynomial coefficients, and the Dirac zero-mode
  selection-rule count.
- `eta_global_anomaly_checks.py`: exact arithmetic checks for the
  Volume XII eta-invariant and global-anomaly chapter, including APS
  orientation bookkeeping, the trace-delta \(SU(2)\) index table,
  Witten's parity criterion \(2j\equiv1\pmod4\), Pfaffian-sign
  multiplicativity, and vanishing of the ordinary \(SU(2)\) cubic weight sum.
- `inflow_anomaly_line_checks.py`: exact finite checks for the anomaly-inflow
  chapter, including functorial composition of anomaly-line cocycles, local
  counterterm/frame changes of cocycle representatives, and the finite
  cochain Stokes identity behind the five-dimensional one-form \(BF\) inflow
  variation.
- `kms_foundation_checks.py`: finite checks for the Volume X KMS-foundations
  chapter, including the finite Gibbs-trace KMS strip boundary condition,
  detailed balance, spectral reconstruction from \(\rho=G^>-G^<\), the
  bosonic fluctuation--dissipation identity, and the
  \(\rho=-2\operatorname{Im}G^R\) retarded-sign convention entering the shear
  Kubo formula.
- `banks_zaks_two_loop_checks.py`: exact rational checks for the Banks-Zaks
  two-loop beta-function conventions in the monograph's
  \(\operatorname{tr}_{\square}(t^a t^b)=\delta^{ab}\) normalization,
  including the conformal-window edge and leading \(\epsilon_{\rm BZ}\)
  fixed-point formulas.
- `bf_theory_checks.py`: exact finite cochain checks for the Volume VIII BF
  theory chapter, including finite Fourier projection onto flat cochains,
  the groupoid-cardinality partition function, cellular Wilson gauge
  invariance, and the Wilson/surface linking phase sign.
- `finite_gauge_state_sum_checks.py`: exact finite checks for the Volume VIII
  finite-gauge state-sum chapter, including action-groupoid cardinality,
  connected-manifold homomorphism counts, closed-surface character formulas
  for cyclic groups and \(S_3\), class-function convolution on the circle,
  the standard \(\mathbb Z_n\) Dijkgraaf--Witten \(3\)-cocycle condition, and
  spanning-tree gauge-fixing counts.
- `bpst_instanton_normalization_checks.py`: finite algebra and radial-integral
  checks for the BPST instanton section, including self-duality of the
  't Hooft symbols, the quadratic \(\eta\)-symbol identity used in the
  curvature calculation, \(\int F^a_{\mu\nu}F^a_{\mu\nu}=32\pi^2\), \(Q=1\),
  and the conversion between the common half-trace action
  \(8\pi^2/g_{\rm ht}^2\) and the monograph trace-delta coupling
  \(4\pi^2/g_{\rm YM}^2\).
- `borel_laplace_checks.py`: exact checks for the Borel--Laplace and
  zero-dimensional quartic large-order section, including Gaussian moments,
  perturbative coefficients, the ratio
  \(a_{n+1}/((n+1)a_n)\to-2/3\), and the corresponding Borel-radius
  normalization, together with the hypergeometric Borel-transform
  coefficient identity, the conformal-Borel map for a single negative cut,
  Borel--Leroy coefficient recovery, the factorial moment/Borel-pole algebra
  in the running-coupling renormalon model, and the algebraic cancellation of
  a two-term OPE renormalon ambiguity.
- `bv_localization_checks.py`: exact finite checks for the Volume VIII BV
  integration and localization chapter, including the one-pair BV Laplacian
  product identity, BV Stokes endpoint term, normal Gaussian
  Pfaffian/determinant factor, rank-one Mathai--Quillen normalization, and
  the \(S^2\) Atiyah--Bott fixed-point coefficient identity.
- `bv_master_algebra_checks.py`: finite sign and grading checks for the BV
  master-formalism chapter, including antibracket ghost-number bookkeeping,
  Yang--Mills ghost nilpotency in an \(\mathfrak{su}(2)\) test algebra, and
  the BRST-doublet contracting homotopy.
- `center_polyakov_checks.py`: finite center-phase checks for the thermal
  center-symmetry and Polyakov-loop section, including temporal-plaquette
  phase cancellation, Polyakov-loop \(N\)-ality, neutral pair correlators,
  center averaging of charged loops, and the static-source free-energy
  relation.
- `finite_temperature_path_integral_checks.py`: finite convention checks for
  the thermal path-integral chapter, including bosonic and fermionic
  Matsubara boundary phases, the one-mode fermionic coherent-state trace
  identity with the chapter's Berezin sign convention, the finite-volume
  spectral representation of Euclidean correlators, the separate
  zero-frequency degenerate term, the Matsubara Cauchy transform, and
  chemical-potential twist and imaginary-holonomy periodicity.
- `charged_flux_dressing_checks.py`: finite checks for the charged-sector
  Haag--Ruelle/LSZ discussion, including the boosted Coulomb flux integral,
  extraction of the charged velocity from flux extrema, the half-line Fourier
  transform of an asymptotic worldline current, and the equality between the
  worldline-current denominator and the momentum-space eikonal denominator.
- `chpt_nlo_checks.py`: finite arithmetic checks for the NLO chiral
  perturbation theory section, including the ten \(L_1,\ldots,L_{10}\)
  Gasser--Leutwyler labels, selected \(\Gamma_i\) entries, and the
  cancellation of the \(\mu\)-dependence in the two-flavor
  \(M_\pi^2\) chiral logarithm by the running of \(l_3^r(\mu)\).
- `conformal_collider_checks.py`: exact rational checks for the ANEC and
  conformal-collider section, including the \(S^2\) angular averages in the
  four-dimensional stress-tensor flux form, the helicity \(2,1,0\) reductions
  to the Hofman--Maldacena inequalities, and the vanishing of the integrated
  \(t_2,t_4\) deformations.
- `cosmological_particle_creation_checks.py`: exact convention checks for the
  Volume XII cosmological-particle-creation chapter, including the
  conformal-coupling cancellation in arbitrary dimension, de Sitter
  \(\nu\)-parameter arithmetic, sudden-quench Bogoliubov normalization, the
  Riccati equation for a power-law adiabatic frequency, and finite positive
  type of detector-response Gram forms.
- `energy_correlator_sum_rule_checks.py`: exact finite-event checks for the
  energy-energy-correlator zeroth and first moment sum rules and the
  coincident-detector contact weight in the QCD detector-observable chapter.
- `constructive_scalar_spde_checks.py`: finite checks for the constructive
  scalar and singular-SPDE chapters, including Hermite/Wick coefficients for
  \(:\phi^2:\), \(:\phi^3:\), \(:\phi^4:\), finite Wiener-chaos isometry and
  moment constants, the sharp-cutoff tadpole coefficients in two and three
  Euclidean dimensions, the displayed
  \(\phi^4_d\) superficial-degree formula, and the two-loop
  \(\Phi^4_3\) sunset combinatorics giving the logarithmic mass-coordinate
  coefficient in the chapter's \(\lambda\phi^4+\alpha\phi^2\)
  normalization, the finite-cutoff local stability lower bound, the
  multiscale phase-cell geometric tail estimate, plus the
  stochastic-quantization OU variance, two negative-Sobolev threshold checks,
  heat-kernel smoothing optimization, the path-space
  \(\Phi^4_2\) enhanced-noise increment and Kolmogorov threshold arithmetic,
  and the Sobolev exponent inequalities used in the Da Prato--Debussche
  local fixed-point proof, together with the
  three-dimensional Sobolev obstruction to applying the same DPD closure to
  \(\Phi^4_3\), the Young-exponent arithmetic in the smooth DPD energy
  estimate and a finite Markov-chain invariant-measure identity, plus the
  coarse/fine dyadic
  exponent arithmetic in the compact reconstruction proof and the
  homogeneity/sign/combinatorial checks for the dynamic \(\Phi^4_3\) BPHZ
  local counterterm calculation, together with exact arithmetic for the
  abstract modelled-distribution fixed-point ball, contraction, and Picard
  tail estimates, plus the dyadic geometric-tail arithmetic in the random
  model convergence criterion and the exponent/geometric-factor arithmetic in
  the dyadic parabolic convolution bound, and the exponent arithmetic in the
  parabolic Taylor-subtraction gain, together with the finite-net entropy
  cancellation and geometric-series arithmetic in the dyadic-net supremum
  upgrade from pointwise coordinate moments to compact model-seminorm bounds,
  plus the finite-coordinate arithmetic that converts those compact
  suprema into the random-model Cauchy constants, and the multiscale-sector
  geometric factors used to pass from positive gap exponents to uniform and
  cutoff-increment kernel bounds, together with the one-loop relative-scale
  gap arithmetic for the local and off-diagonal sectors of the dynamic
  \(\Phi^4_3\) prototype, the negative cubic drift ledger, and the sharp
  Fourier-cutoff shell counts for the one-loop coordinate \(C_1\), plus the
  dyadic block arithmetic proving logarithmic growth of the two-loop
  coordinate \(C_2\), the bounded dyadic shell increment for \(C_2\), and
  the two-loop sunset sector gaps plus nested forest cancellation and the
  finite negative-sector coordinate chart, including the scale-summed
  coordinate supremum arithmetic and the seven-coordinate constants in the
  negative-sector model convergence criterion, plus the physical-parameter
  entropy exponents after the test-function supremum has been dualized, and
  the projective-tensor arithmetic in the dual-norm finite-chaos estimate and
  the kernel-to-projective-norm criterion, plus the Gaussian-coordinate scale
  slack for \(\Xi,X,X^2,X^3\) and the wavelet \(H^{-s}\)-summability
  arithmetic used in the dual-norm Gaussian-coordinate upgrade, together
  with the heat-integration reexpansion arithmetic that transfers the
  \(X^3\) slack to the \(c_n\) coordinate, and the finite-cutoff Wick
  contraction arithmetic for the nonlinear negative coordinates \(XY\) and
  \(X^2Y\), including the tested finite-chaos arities \(4,2\) and \(5,3,1\)
  and the symmetrized kernel-norm weights used in the covariance-integral
  formulas, together with the physical-scale arithmetic for the logarithmic
  first-chaos \(X^2Y\) bound and the dyadic covariance double-increment
  scale gains entering that bound, the OS-II reconstruction-growth
  bookkeeping that keeps reflected positive-time cylinder tests at linear
  seminorm order, and the interval-recursion arithmetic in the
  rough-forcing energy-to-Besov bootstrap.
- `continuum_scaling_window_checks.py`: finite checks for the Volume XI
  continuum-limit chapter, including the lattice momentum expansion, the
  exact free-scalar pole mass and correlation length, the Gaussian
  mass-squared RG eigenvalue, the \(\nu=1/y_t\) scaling relation, and finite
  Wick-subtraction contact-coordinate shifts.
- `trace_anomaly_checks.py`: exact finite checks for the Volume XII curved
  trace-anomaly chapter, including the conformal-scalar heat-kernel
  curvature combination, the \(R^2\) Weyl-variation shift of the
  \(\nabla^2R\) coefficient, free-field \(a,c\) entries, the
  \(\mathcal N=4\) Yang--Mills \(a=c\) sum, constant-curvature
  \(E_4,W^2\) identities, and the two-dimensional Wess--Zumino action
  variation.
- `cft_anomaly_regression_checks.py`: finite arithmetic checks for the
  issue-#447 regression class: the \(\pi^0\to2\gamma\) anticommutator factor,
  the \(4/3\) identity-block cubic coefficient, the \(W=-\log Z\)
  stress-tensor source sign, and the Lorentzian-to-radial \([P,K]\) sign.
- `conformal_perturbation_rg_checks.py`: exact rational checks for the
  two-dimensional conformal-perturbation section, including the cutoff-power
  cancellation in the annular OPE integral, the second-order \(\pi\) factor,
  the length-scale versus energy-scale beta-function sign, and the quadratic
  contact-term scheme-shift law.
- `cft_voa_modular_checks.py`: exact \(\mathbb Q(\sqrt2)\) checks for the
  Ising VOA/modular-data example, including \(S^2=1\), Verlinde fusion
  coefficients, quantum dimensions, shifted character exponents, the
  \(T\)-phase spin-selection rule, uniqueness of the diagonal genus-one
  Ising modular invariant with one vacuum, the Cardy Tauberian saddle
  coefficient, the rank-two logarithmic Jordan-cell Ward identities and trace
  invisibility of the nilpotent extension, and the Zhu-algebra top-weight
  polynomial with its primitive idempotents.
- `conformal_block_companion.py`: reusable numerical companion routines for
  OPE-normalized global scalar conformal blocks in the chapter conventions,
  using the Dolan--Osborn hypergeometric closed forms in \(D=2\) and \(D=4\),
  the Dolan--Osborn/Hogervorst--Rychkov Casimir \(z\)-series recursion for
  \(D=3\) and other \(D>2\) checks, the universal leading radial
  Gegenbauer/harmonic term, and the mixed-correlator \(F_\pm\) crossing kernel
  normalization.  Two-dimensional Virasoro blocks require a separate
  Zamolodchikov-recursion companion rather than this global-block evaluator.
- `bcft_cardy_checks.py`: exact checks for the two-dimensional BCFT chapter,
  including the Ising modular \(S\)-matrix arithmetic, Cardy annulus spectra,
  fusion associativity and fusion-ring characters, boundary entropy squares,
  Chan--Paton direct sums, compact-boson T-duality zero modes, Ising
  boundary-changing fusing constants and OPE powers, and the Liouville
  FZZT/ZZ hyperbolic identities used in the nonrational boundary-state
  discussion.
- `liouville_bpz_checks.py`: exact algebra checks for the Liouville chapter,
  including the level-two BPZ null vector, its \(b\leftrightarrow b^{-1}\)
  dual, one-screening and dual one-screening coefficient
  rewrites, DOZZ \(b\)-shift powers, hypergeometric connection arguments,
  level-two Virasoro block coefficients, and the elliptic \(q\)-coordinate
  conversion through \(q^2\).
- `superconformal_algebra_checks.py`: exact rational checks for the
  two-dimensional superconformal-algebra chapter, including the
  \(\mathcal N=1\) Ramond zero-mode shift, \(\mathcal N=2\) chiral-primary
  norm identities, spectral-flow automorphism, NS-to-R ground-state shift,
  extended \(\mathcal N=2\) spectral-flow operator weights, charges,
  Heisenberg OPE exponents, and descendant charges, protected
  Landau--Ginzburg central-charge arithmetic, and the
  supersymmetric \(SU(2)/U(1)\) and \(SL(2,\mathbb R)/U(1)\) rank-one
  coset central-charge, chiral-primary, field-identification, and
  spectral-flow formulas.
- `cohomological_metric_descent_checks.py`: exact polynomial differential-form
  checks for the Volume VIII metric-independence chapter, including
  \(Q^2=0\) in the de Rham model, the graded Leibniz sign, Stokes' boundary
  term on the unit square, and vanishing of a \(Q\)-exact deformation when the
  boundary contribution is zero.
- `cohomological_field_theory_checks.py`: exact finite checks for the Volume
  VIII cohomological-field-theory chapter, including the Cartan identity
  \(d_C^2=-u\mathcal L_v\), equivariant closure of
  \(\omega+u\mu\) for the Hamiltonian rotation model, the
  Mathai--Quillen auxiliary Gaussian square-completion sign, and rank-one
  zero-locus orientation.
- `topological_sigma_model_checks.py`: exact finite checks for the Volume
  VIII topological sigma-model chapter, including the A-model pointwise
  energy identity, \(QH^\bullet(\mathbb P^m)\) with \(H^{m+1}=Q\),
  associativity and degree selection in projective-space quantum cohomology,
  the stable-map virtual-dimension formula, and the B-model top-form degree
  condition.
- `twisting_representation_checks.py`: exact finite checks for the Volume
  VIII supersymmetric-twists chapter, including the \(SU(2)\) tensor-product
  decomposition of the Donaldson twist, the dimensions of the twisted
  gaugino form fields, the two-dimensional A/B twist scalar-supercharge
  charge bookkeeping, and the Donaldson-Witten \(Q^2=\delta_{-\phi}\)
  closure ledger.
- `tqft_frobenius_gluing_checks.py`: exact rational checks for the Volume VIII
  bordism-functoriality chapter, including the inverse-pairing cylinder
  identity, Frobenius neck-exchange relation, pair-of-pants associativity, and
  the semisimple genus-\(g\) partition function
  \(\sum_\alpha\lambda_\alpha^{1-g}\).
- `donaldson_sw_comparison_checks.py`: exact arithmetic checks for the
  Witten-Donaldson and Seiberg-Witten comparison chapter, including the
  anti-self-dual deformation-complex index, the monopole expected-dimension
  formula from Dirac plus Abelian gauge indices, the
  \(2\chi+3\sigma\) identity, Donaldson descent degrees, and the
  trace-delta instanton-action coefficient.
- `discrete_theta_terms_checks.py`: finite arithmetic checks for the discrete
  theta terms chapter, including the Pontryagin-square quadratic-refinement
  identity, oriented classification periodicity of the counterterm group,
  \(p\sim p+k\) for \(SU(N)/\mathbb Z_k\) line lattices, mutual locality of
  \(L_{N,k,p}\), the \(SU(2)\), \(SO(3)_+\), and \(SO(3)_-\) cases, and the
  electric tilt under a \(2\pi\) theta shift, together with tensor-line
  invariance of the projective second Chern coordinate and the fractional
  \(PSU(N)\) instanton-number sign convention.
- `extended_defect_ward_checks.py`: finite arithmetic checks for the extended
  operators and topological defects chapter, including group-like
  \(\mathbb Z_N\) fusion, higher-form Ward phase multiplicativity, orientation
  and charge reversal, linking/intersection dimension bookkeeping, and
  junction charge conservation.
- `free_cylinder_partition_checks.py`: finite character checks for the
  radial-cylinder free-field section, including the four-dimensional scalar
  reduction \(q(1-q^2)/(1-q)^4=q(1+q)/(1-q)^3\), Weyl/Dirac fermion
  degeneracies, and the Maxwell identity
  \(q^2(6-8q+2q^2)/(1-q)^4=(6q^2-2q^3)/(1-q)^3\).
- `free_scalar_four_point_checks.py`: finite checks for the generalized-free
  scalar OPE/crossing example, including the monomial form of
  \(v^{\Delta_\phi}\mathcal G(u,v)=
  u^{\Delta_\phi}\mathcal G(v,u)\), Wick-pairing counts, the normalized
  \(:\phi^2:/\sqrt2\) OPE coefficient \(a_{0,0}=2\), and the even-spin
  bilinear dimensions.
- `ising_mixed_bootstrap_checks.py`: exact rational checks for the
  higher-dimensional mixed-correlator Ising bootstrap conventions, including
  scalar four-point prefactor crossing ratios, the \(F_\pm\) symmetry signs,
  the spin-\(\ell\) exchange sign, even-sector OPE positive-semidefinite
  matrices, and the five-vector packing of the \(\sigma,\varepsilon\)
  crossing equations.
- `gamma_trace_checks.py`: mostly-plus gamma-matrix conventions, \(\gamma_5\),
  the Weinberg/Wess-Bagger chiral phase comparison, the four-gamma trace, the
  two-dimensional chirality trace, and the anticommutator normalization used
  in the nonabelian anomaly coefficient.
- `gauge_convention_checks.py`: \(SU(N)\) Hermitian-generator normalization
  \(\operatorname{tr}(t^a t^b)=\delta^{ab}\), output-first structure
  constants, \(C_A=2N\), \(T_F=1\), \(C_F=(N^2-1)/N\), the coupling-coordinate
  conversion from the common half-trace convention, and the Wilson-plaquette
  factor giving \((4g_0^2)^{-1}\int\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\).
- `gauge_phase_diagnostics_checks.py`: finite checks for the gauge-theory
  phases chapter, including electric, magnetic, and dyonic condensate
  orthogonality in \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\), the finite
  Dirac-pairing confinement criterion, tropical spectral extraction of static
  potentials, and exponent bookkeeping for Fredenhagen--Marcu type ratios.
- `oblique_confinement_checks.py`: exact finite checks for the confinement
  chapter, including screened-pairing descent to \(S^\perp/S\), maximal
  isotropy of dyonic condensates \(\langle(p,1)\rangle\), the oblique
  unconfined condition \(e\equiv pm\pmod N\), and confinement of nonzero
  electric \(N\)-ality under magnetic condensation.
- `duality_defect_gauging_checks.py`: exact finite checks for the finite
  gauging and duality-defect chapter, including the regular algebra identity
  \(A_H\otimes A_H=|H|A_H\), normality of \(A_3\triangleleft S_3\), the
  \(S_3/A_3\simeq\mathbb Z_2\) quotient multiplication, orbifold
  pair-of-pants monodromy, centralizer sizes, and preservation of the
  electric-magnetic Dirac pairing by \(S\), \(T\), and \(T^p\).
- `haag_ruelle_fock_inner_product_checks.py`: exact rational checks for the
  Haag--Ruelle Fock inner-product recursion, comparing the recursive
  contraction formula with the direct bosonic permanent and particle-number
  orthogonality.
- `global_form_line_lattice_checks.py`: exact finite checks for the
  \(\mathfrak{su}(N)\) global-form and Wilson--'t Hooft line-lattice
  section, including the \(\mathbb Z_N^{\mathrm e}\oplus\mathbb Z_N^{\mathrm m}\)
  Dirac pairing, bilinearity and nondegeneracy, \(SU(N)/\mathbb Z_k\)
  Wilson-charge descent, magnetic cocharacter enlargement, and maximal
  isotropy of \(L_{N,k,p}=\langle(k,0),(p,N/k)\rangle\).
- `sw_su2_periods.py`: numerical and exact checks for the pure \(SU(2)\)
  Seiberg--Witten period section, including Picard--Lefschetz monodromy
  matrices, central-charge action and symplecticity, the minimal-curve
  discriminant, the Picard--Fuchs equation, the electric large-\(u\)
  asymptotic, logarithmic dual-period growth, linear monopole-period
  vanishing at \(u=\Lambda^2\), and rank-one Argyres-Douglas cusp scaling
  dimensions.
- `thooft_line_local_model_checks.py`: finite checks for the Volume IX
  't Hooft-line local model, including the northern/southern Dirac-monopole
  patch difference, flux normalization, integer Dirac phase, finite linking
  pairing bilinearity, theta-angle Witten-effect automorphism, and Cartan
  surface-operator cocharacter shifts.
- `hawking_bogoliubov_checks.py`: finite numerical checks for the Hawking
  mode-tracing calculation, including the imaginary-axis Gamma-function norm,
  the \(|\alpha|^2/|\beta|^2=e^{2\pi\omega/\kappa}\) ratio, the displayed
  Planck factor in \(|\beta_{\omega\omega'}|^2\), the continuum
  normalization-density identity, the wave-packet Planck-bin average, the
  exponential precursor blueshift, the exponential-map Schwarzian flux, and
  the Schwarzschild \(T_H=1/(8\pi M)\) convention.
- `hydrodynamic_modes_checks.py`: finite algebra checks for the Volume X
  hydrodynamic Ward-identity chapter, including shear diffusion, sound
  attenuation, entropy-production positivity for sample transport matrices,
  the sourceful ideal-Euler reduction of acceleration to thermodynamic force
  variables, the diffusion Einstein relation, the multi-charge susceptibility
  geometry, and the static limit of the density source-response pole.
- `hydrodynamic_long_time_tail_checks.py`: finite checks for the Volume X
  hydrodynamic fluctuation chapter, including diffusive static covariance,
  the classical FDT relation, the Gaussian time-domain tail, nonanalytic
  loop coefficients, the \(d=3\) cutoff/nonanalytic split, and positivity of
  the stress-noise tensor.
- `ising_defect_fusion_checks.py`: exact \(\mathbb Q(\sqrt2)\) checks for
  the Ising/Kramers--Wannier noninvertible defect example, including fusion
  associativity, Frobenius--Perron dimensions, modular \(S\)-matrix
  orthogonality, the Verlinde formula, and the diagonal action of defects on
  local primary sectors.
- `ising_form_factor_checks.py`: finite checks for the Volume VI
  free-Majorana and Ising form-factor examples, including Watson exchange,
  cyclicity, the kinematic-pole residue sign, the two-particle invariant-mass
  identity, the energy-density spectral threshold factor, the Euclidean
  Bessel-kernel prefactor, the even spin-field semi-local cyclicity phase,
  the crossed \(\coth\) matrix element, the mixed bra/ket product formula,
  and the semi-local kinematic-pole residue.
- `finite_volume_form_factor_checks.py`: finite checks for the Volume VI
  finite-volume form-factor chapter, including the two-particle Gaudin
  determinant, cancellation of the Gaudin density between matrix elements and
  state counting, connected diagonal subset combinatorics, and the
  free-Majorana two-particle Bessel-reduction prefactor.
- `ising_metropolis_finite_checks.py`: exact enumeration checks for the
  `qft_scripts/ising2d_metropolis.py` companion script, verifying the local
  energy difference and detailed balance on the \(2\times2\) periodic Ising
  chain.
- `z2_gauge_metropolis_checks.py`: exact finite checks for the
  `qft_scripts/z2_gauge_3d_metropolis.py` companion script, verifying the
  local link-flip plaquette-score change, pairwise detailed balance, gauge
  invariance of the action and Wilson loops, and the identity between the
  \(1\times1\) Wilson-loop average and the plaquette average.
- `su2_gauge_metropolis_checks.py`: finite checks for the
  `qft_scripts/su2_gauge_4d_metropolis.py` companion script, verifying
  quaternion \(SU(2)\) group operations, the local compact-link plaquette
  score change, pairwise detailed balance, gauge invariance of the action and
  Wilson loops, and the \(1\times1\) Wilson-loop/plaquette identity.
- `z2_strong_coupling_surface_checks.py`: exact enumeration of small
  cubical plaquette chain complexes over \(\mathbb F_2\), verifying the
  one-cube Wilson-loop polynomial \((t+t^5)/(1+t^6)\), the first
  \(2\times1\) rectangular surface counts, and the finite entropy-bound
  arithmetic used in the strong-coupling area estimate.
- `kinetic_theory_checks.py`: finite algebra checks for the Volume X kinetic
  theory chapter, including Bose/Fermi detailed balance, the H-theorem
  integrand, linearized collision-operator positivity and null vectors, and
  the relaxation-time shear-viscosity integral.
- `monte_carlo_sign_problem_checks.py`: exact finite checks for the Volume XI
  Monte Carlo and sign-problem chapter, including the finite-\(N\)
  autocorrelation variance identity, the reweighting identity, the
  average-phase relative-variance bound, and the distinction between
  \(\gamma_5\)-Hermiticity, determinant reality, and determinant positivity
  after flavor pairing.
- `large_n_topology_checks.py`: finite checks for the 't Hooft
  large-\(N\) section, including the \(SU(N)\) completeness relation in the
  monograph trace normalization, the planar-versus-one-handle theta-graph
  \(N^{-2}\) suppression, normalized single-trace scaling, and fixed-\(N_f\)
  versus Veneziano quark-boundary counting, plus the displayed baryon Hartree
  pair-counting and fixed-spin rotor \(1/N_c\) scaling.
- `lattice_continuum_bridge_checks.py`: exact finite checks for the
  Volume XI lattice-to-continuum local-QFT chapter, including cell-average
  test-function arithmetic, the finite-graph random-walk resolvent,
  closedness of reflection-positive Gram matrices, and tensor-product
  locality for spin algebras.
- `lattice_fermion_chiral_checks.py`: exact finite checks for the
  Volume XI lattice-fermion chapter, including naive-doubler chirality
  cancellation, Wilson corner-mass degeneracies, the Ginsparg-Wilson and
  overlap-index algebra, Berezinian index normalization, reflection-positive
  crossing-factor coefficients, Wilson reflection projectors, and staggered
  phase signs.
- `nested_bethe_ansatz_checks.py`: finite algebra checks for the Volume VI
  algebraic and nested Bethe-ansatz chapters, including the rational
  Yang--Baxter equation, transfer-matrix commutativity, one-magnon spectra at
  \(L=4,6,8\), an \(SU(3)\) nested-root solution, and Baxter \(TQ\)
  pole-cancellation.
- `planar_n4_integrability_checks.py`: finite checks for the Volume VII
  planar \(\mathcal N=4\) SYM integrability chapters, including cyclic
  one-loop Konishi Bethe roots, one-magnon XXX spectra, central-extension
  magnon dispersion, its weak-coupling expansion, and a local
  Hirota-to-Y-system algebra identity.
- `susy_n4_scft_checks.py`: exact arithmetic checks for the Volume VII
  \(\mathcal N=4\) SYM SCFT foundation material, including one-loop and
  holomorphic beta-function cancellation, the one-complex-dimensional
  exact-marginal coupling chart, theta-periodicity and \(SL(2,\mathbb Z)\)
  generator arithmetic, \(a=c=\dim\mathfrak g/4\), the \(SO(6)\)
  symmetric-traceless projector, stress-tensor-multiplet two-point
  normalization, and planar half-BPS chiral OPE coefficients.
- `lattice_reflection_positivity_checks.py`: finite character-expansion
  checks for the Osterwalder-Seiler lattice reflection-positivity proof,
  including \(U(1)\) Bessel/Fourier positivity, the \(SU(2)\) Wilson
  plaquette coefficient formula
  \(a_\ell=I_\ell-I_{\ell+2}=2(\ell+1)I_{\ell+1}/\beta\), and finite
  \(SU(2)\) tensor-product character multiplicities.
- `locally_covariant_kg_checks.py`: exact finite linear-algebra checks for
  the Volume XII locally covariant Klein--Gordon construction, including
  descent of the causal-propagator pairing to the equation-of-motion
  quotient, vanishing of equation generators in the CCR commutator,
  symplectic preservation under embeddings, and the quotient-level
  distinction between Cauchy and non-Cauchy morphisms.
- `qcd_string_luscher_checks.py`: exact rational checks for the QCD-string
  effective-string section, including the open and closed transverse-scalar
  Casimir coefficients \(-1/24\) and \(-1/6\), the displayed
  Nambu--Goto reference expansion coefficients at orders \(1/L\) and
  \(1/L^3\), the first \(D=4\) open-oscillator degeneracies, and the
  excited-level expansion coefficients with closed-string level matching, and
  the displayed baryonic \(Y\)-string Steiner lengths in the equilateral and
  \(120^\circ\)-threshold cases.
- `lee_yang_tba_checks.py`: finite checks for the Volume VI scaling
  Lee--Yang thermodynamic Bethe ansatz example, including scalar-amplitude
  unitarity and crossing, the sign and total integral of the TBA kernel, the
  golden-ratio plateau equation, and the Rogers-dilogarithm value
  \(L(\phi^{-2})=\pi^2/15\) giving \(c_{\rm eff}=2/5\).
- `mellin_four_point_checks.py`: finite algebra checks for the CFT
  four-point Mellin-representation section, including the constrained
  \(\delta_{ij}\) equations, compatibility with the chapter's scalar
  four-point prefactor, the \(\dd\delta_{12}\dd\delta_{14}
  =\dd\mathfrak s\,\dd\mathfrak t/4\) Jacobian, the
  \(\mathfrak s=\tau+2m\) pole-to-\(u^{\tau/2+m}\) exponent map, and the
  identical-scalar \(2\leftrightarrow4\) channel permutation.
- `narain_lattice_cocycle_checks.py`: finite integer checks for the
  two-dimensional toroidal CFT section, including the explicit lattice
  cocycle associativity and exchange laws, even-unimodular sample Gram
  matrices, cancellation of the antisymmetric \(B\)-field from the Narain
  integral pairing, and the distinction between even-unimodular existence
  and scalar modular-invariance in the presence of chiral gravitational
  anomaly.
- `nlsm_background_field_checks.py`: exact rational checks for the NLSM
  background-field source convention, including the mean-zero condition
  \(J=L\), the Gaussian square-completion sign used in the one-loop
  effective-action determinant, and the pure-metric second-variation
  normalization, curvature-vertex sign, heat-kernel pole normalization, and
  Ricci-counterterm sign.
- `nlsm_buscher_checks.py`: exact rational checks for the two-dimensional
  NLSM Buscher and pure-metric beta-function sections, including Buscher
  \(E\)-matrix involutivity, the component \(G,B\) rules, the dilaton-shift
  involution, the cell-regulated Euler-characteristic ledger for the
  Buscher determinant, the constant-curvature two-loop
  \(R_{ik\ell m}R_j{}^{k\ell m}\) coefficient, and the
  spherical/hyperbolic radius-flow beta functions.
- `nlsm_scheme_redefinition_checks.py`: finite polynomial checks for the
  NLSM finite-scheme-redefinition law
  \(\beta'=\beta+[\beta,F]+O(F^2)\), including the sign of the beta-vector
  Lie bracket in a two-coupling model.
- `nlsm_weyl_anomaly_checks.py`: exact rational checks for one-loop NLSM
  Weyl-anomaly bookkeeping, including the \(H^2\) metric and \(B\)-field
  variation coefficients, the local worldsheet tadpole and bubble origins of
  the \(H\)-dependent counterterms, the full string-frame metric trace split and
  scalar dilaton variation, linear-dilaton central-charge condition,
  heterotic Green--Schwarz coefficient, heterotic gauge/dilaton redundant
  direction, torsionful Ricci package, and local \(\dd^2=0\) preservation of
  the \(H\)-beta Bianchi identity.
- `nonequilibrium_open_system_checks.py`: finite checks for the Volume X
  nonequilibrium steady-state and open-system chapter, including reservoir
  entropy production, GKSL trace preservation, KMS detailed balance for a
  two-level system, Ornstein-Uhlenbeck noise normalization, and positivity of
  a quadratic noise kernel.
- `microlocal_spectrum_checks.py`: finite convention checks for the
  microlocal spectrum chapter, including the mostly-plus future-covector
  convention, the Klein-Gordon Hamilton-flow sign, the two-point graph
  covector pattern \((p,-p)\), and the opposite-cone product obstruction.
- `wilson_fisher_epsilon_checks.py`: exact rational arithmetic turning the
  two-loop \(N=1\) Wilson-Fisher pole coefficients into
  \(x_*\), \(\eta\), \(\gamma_{2*}\), \(y_t\), \(\nu\), and \(\omega\).
- `on_wilson_fisher_epsilon_checks.py`: exact rational arithmetic for the
  singlet \(O(N)\) Wilson-Fisher family, including the \(N=1\) reduction and
  the leading large-\(N\) scaling of \(u=Nx\).
- `on_sigma_gn_checks.py`: numerical finite checks for the Volume VI
  \(O(N)\) sigma-model and Gross-Neveu chapter, including the exact
  gamma-function S-matrix scalar identity, channel unitarity, crossing,
  finite-dimensional Yang-Baxter component identity, and large-\(N\) cutoff
  gap and beta-function algebra.
- `orbifold_twist_weight_checks.py`: finite rational checks for the
  two-dimensional orbifold chapter, including the cyclic permutation twist
  weight \(h=c_0(K-K^{-1})/24\), its Schwarzian-cover derivation, the
  \(c_0=6\) length-two value \(h=3/8\), the Hurwitz-zeta oscillator derivation
  of the complex rotation twist weight, and the real \(\mathbb Z_2\)
  reflection twist value \(h=1/16\).
- `paqft_algebra_checks.py`: finite polynomial checks for the curved pAQFT
  chapter, including Hadamard star-product associativity, the smooth
  Hadamard-change intertwiner, and scaling-degree ambiguity combinatorics.
- `point_splitting_stress_checks.py`: finite checks for the point-split
  stress-tensor examples, including the Bose integral
  \(\int_0^\infty x^3(e^x-1)^{-1}dx=\pi^4/15\), the flat thermal scalar
  energy density and traceless equation of state, the massless plane-wave
  eigenvalues of the displayed bidifferential operators, and the de Sitter
  constant-curvature anomaly specialization for a conformal real scalar.
- `schwinger_model_checks.py`: finite sign and normalization checks for the
  Schwinger-model chapter, including the two-dimensional current-duality
  convention, the algebraic elimination of the electric field, the
  anomaly-induced mass \(m_{\rm Sch}^2=e^2/\pi\), the screened static
  potential, and the periodicity of the massive-model string tension for
  integer probe charge.
- `semiclassical_backreaction_checks.py`: finite checks for the semiclassical
  backreaction chapter, including four-dimensional traces of the
  curvature-squared Euler tensors, the KMS fluctuation-dissipation factor,
  positivity of a finite noise covariance, and the low-energy root selected
  by reduction of order in a toy higher-derivative equation.
- `schwinger_keldysh_operator_checks.py`: finite two-level-system checks for
  the real-time Schwinger--Keldysh operator chapter, including diagonal
  unitarity, branch-exchange reality, the \(|Z|\le1\) positivity bound,
  the \(H-J^\alpha O_\alpha\) source-response sign from an impulsive physical
  source, the \(G^{aa}=0\) two-point cancellation and retarded support in the
  contour-to-\(r/a\) algebra, and KMS detailed balance.
- `sk_diffusion_action_checks.py`: finite algebra checks for the Volume X
  Schwinger--Keldysh hydrodynamic diffusion action, including the sourced
  density saddle, one-charge and noncommuting two-charge diffusive response
  kernels, transverse Ohm response, scalar and matrix KMS noise coefficients,
  and Hubbard--Stratonovich noise normalization.
- `sine_gordon_smatrix_checks.py`: numerical finite checks for the Volume VI
  sine-Gordon exact scattering datum, including soliton-matrix unitarity and
  Yang-Baxter, the free-fermion point, breather pole locations, breather mass
  kinematics, soliton-breather unitarity/crossing/pole kinematics, and
  lightest-breather unitarity and crossing.
- `sg_thirring_bosonization_checks.py`: exact rational checks for the
  sine-Gordon/massive-Thirring bosonization section, including the distinction
  between vertex-OPE exponent and scaling dimension, Coleman's coupling map,
  the current-dictionary coefficient, the Mandelstam exchange phase, the
  free-fermion point, and the sine-Gordon relevance threshold.
- `ks_allowability_checks.py`: finite complex-linear-algebra checks for the
  Kontsevich--Segal allowability chapter, including the angle criterion,
  Euclidean and Lorentzian boundary examples, two-time exclusion, and
  positivity of all diagonal \(q\)-form coefficients.
- `susy_abjm_6d_checks.py`: exact finite checks for the ABJM and
  six-dimensional supersymmetric field-theory chapters, including the ABJM
  superpotential \(R\)-charge, opposite-level parity bookkeeping, abelian
  BF normalization, standard ABJM conformal-locus tangent count,
  \(\mathbb Z_k\) orbifold order, \(S^3\) matrix-model denominator powers,
  six-dimensional Yang-Mills coupling dimension, \(A_{N-1}\) \((2,0)\)
  anomaly/tensor-branch arithmetic, and the trace-delta
  \(g_5^2=4\pi^2R\) compactification normalization.
- `susy_gauge_foundation_checks.py`: exact finite checks for the Volume VII
  supersymmetric gauge-theory foundation chapter, including the auxiliary
  \(D\)-field square completion and potential sign, the absence of
  Fayet--Iliopoulos parameters for an `su(2)` semisimple factor, vectorlike
  \(U(1)\) anomaly cancellation, and the conjugate-representation anomaly
  sign.
- `susy_moduli_space_checks.py`: finite algebra checks for the Volume VII
  supersymmetric moduli-space quotient conventions, including the
  rank-one \(U(1)\) invariant ring
  \(\mathbb C[x,y]^{\mathbb C^\ast}=\mathbb C[xy]\), the matching
  real/complex quotient dimension count, and the equivariance of an
  invariant superpotential's \(F\)-term ideal.
- `susy_2d_lg_glsm_checks.py`: exact finite checks for the
  two-dimensional \(\mathcal N=(2,2)\) Landau--Ginzburg and GLSM chapter,
  including \(A\)-series quasihomogeneous charges and central charges,
  Fermat Jacobi-basis dimensions, quintic Landau--Ginzburg central charge,
  hypersurface GLSM gauge-invariance arithmetic, axial-anomaly charge sums,
  positive-chamber hypersurface dimensions, and negative-chamber residual
  finite-gauge-group orders, together with the A/B twist spin-shift ledger
  that identifies the scalar supercharges and the abelian circle-duality
  momentum-winding/Legendre-Hessian inversion checks, plus the abelian GLSM
  Coulomb one-loop charge-exponent/vacuum-count ledger.
- `susy_holomorphy_nsvz_checks.py`: exact rational checks for Volume VII
  holomorphy and NSVZ coordinate algebra, including quadratic chiral
  tree-level elimination, the eliminated derivative identity, Konishi and
  vector-multiplet coordinate shifts, and the differentiated
  holomorphic-canonical relation leading to the NSVZ beta function.
- `susy_n1_conifold_checks.py`: exact rational checks for the
  four-dimensional \(\mathcal N=1\) conifold SCFT and cascade section,
  including the KW \(R\)-anomaly, \(\gamma=2\mathcal C\) NSVZ convention,
  KW beta-function rank count for the two gauge numerators and quartic
  marginality defect, the KW two-dimensional local conformal-locus count,
  \(a\)-maximization quadratic term, central charges, rank-one conifold
  relation, KS beta-function numerator signs, unequal-rank \(R\)-anomaly
  coefficients, Seiberg-dual magnetic rank, magnetic meson quadratic-form
  integration, Euclidean cascade step count, and
  \(\mathbb Z_{2M}\to\mathbb Z_2\) vacuum count.
- `susy_n1_pure_sym_checks.py`: exact finite checks for pure
  four-dimensional \(\mathcal N=1\) supersymmetric Yang--Mills, including
  the adjoint-fermion discrete chiral anomaly, the
  \(\mathbb Z_{2N_c}\to\mathbb Z_2\) condensate orbit, VY glueball
  dimension/source/\(F\)-term arithmetic, condensate branch monodromy under a
  theta-angle loop, pure-SYM one-instanton zero-mode saturation for
  \(S^{N_c}\) rather than a one-point condensate, instanton-number
  selection for separated \(S\)-correlators, the saturated Berezin
  coefficient and its factorial/sign conventions, finite-volume
  symmetry-basis versus cluster-branch linear algebra, the affine-Toda
  product constraint, constrained Hessian nondegeneracy, local holomorphic
  chiral oscillator index convention, local critical-point index
  contribution, and the affine-Toda/Witten-index vacuum count match.
- `susy_n1_sqcd_duality_checks.py`: exact rational checks for the
  four-dimensional \(\mathcal N=1\) SQCD duality and phase-ledger section,
  including Seiberg-dual rank involution, baryon-charge matching, SQCD
  holomorphic-canonical NSVZ coordinate-relation algebra, electric and
  magnetic NSVZ numerator cancellation in the monograph \(\gamma\)
  convention, magnetic gauge-\(R\) anomaly cancellation, magnetic
  superpotential dimension and \(R\)-charge, SQCD conformal-window
  central-charge and free-field \(a_{\mathrm{UV}}-a_{\mathrm{IR}}\)
  comparison factorization,
  full electric-magnetic
  't Hooft anomaly matching, mass and Higgs deformation rank/dimension/
  \(R\)-charge tests, \(N_f=N_c+1\) confining-superpotential
  dimension/\(R\)-charge checks, mass decoupling to the \(N_f=N_c\)
  quantum-modified constraint, massive-SQCD elimination to pure-SYM branch
  superpotentials, source identity, and mass-source/Konishi ledger, and the
  conformal-window/free-phase inequalities.
- `susy_instanton_nekr_checks.py`: exact rational checks for the
  supersymmetric instanton expansion, including the ADHM dimension count,
  the trace-delta to half-trace instanton-action conversion, ADS dimension
  and \(R\)-charge arithmetic, the \(N_f=N_c-1\) one-instanton zero-mode
  and Higgs-patch collective-coordinate ledger, the radial Higgs-cutoff
  integral scaling, the Yukawa-lifting Berezin determinant saturation and
  coefficient-factorization ledger, the maximal-rank meson
  determinant-invariant uniqueness step, holomorphic decoupling exponent
  shift, ADS decoupling-recursion coefficient and one-variable \(F\)-term
  algebra, the pure \(SU(2)\)
  one-instanton Nekrasov fixed-point sum, and the first Nekrasov
  prepotential coefficient \(q/(2a^2)\).
- `susy_localization_matrix_checks.py`: finite checks for the compact-space
  supersymmetric localization chapter, including the trace-delta \(S^4\)
  Gaussian coefficient, the finite normal Gaussian Pfaffian/determinant
  convention, the \(S^4\) \(H\)-function finite-product logarithmic
  derivative, the \(U(1)\) \(S^4\) Gaussian matrix integral, finite
  double-sine reflection and pole-convention checks, the \(U(1)_k\)
  \(S^3\) Chern--Simons Fresnel completion of the square, and the
  round-\(S^3\) conjugate-chiral-pair integral
  \(\int d\sigma/(2\cosh\pi\sigma)=1/2\).
- `soft_drop_irc_checks.py`: exact rational checks for the soft-drop
  IRC-classification section, including the \(\beta_{\rm SD}=0\) collinear
  counterexample for the groomed four-vector and the \(\beta_{\rm SD}>0\)
  threshold behavior.
- `track_function_moment_checks.py`: exact rational checks for the finite-kernel
  track-function RG identities, verifying preservation of normalization and
  the first-moment evolution formula for discrete track measures.
- `susy_qm_index_checks.py`: exact rational checks for the Volume I
  SUSY-QM and worldline index-density section, including the oscillator
  supertrace identity, zero-mode index count, two-variable Berezin Pfaffian
  extraction, and the \(\widehat A\)-series coefficients through degree six.
- `susy_representation_checks.py`: exact finite checks for the Volume VII
  supersymmetry representation chapter, including massive \(\mathcal N=1\)
  Fock-space dimensions, boson/fermion balance, the Clebsch--Gordan
  dimension identity for the one-oscillator spin sector, the rank-one massless
  supercharge norm matrix, and BPS-bound block eigenvalues
  \(2(m\pm z)\).
- `susy_superspace_component_checks.py`: finite Grassmann-algebra checks for
  the Volume VII superspace/local-actions conventions, including
  \(\theta^2=2\theta^1\theta^2\), the left-derivative rule for \(\theta^2\),
  the \((\theta\psi)(\theta\chi)\) identity, the
  \(-\frac12 W_{ij}\psi^i\psi^j\) chiral \(F\)-term coefficient, and
  auxiliary \(F\)-field elimination.
- `susy_wilsonian_bv_checks.py`: finite Fourier/odd-variable checks for the
  Volume VII supersymmetric Wilsonian-schemes chapter, including BV Stokes
  for a fiber Darboux pair, the pushforward chain-map identity, QME
  preservation in the finite model, and semigroup behavior for product
  cycles.
- `symmetric_product_orbifold_checks.py`: exact finite group-theory and
  rational-weight checks for the Volume V symmetric-product orbifold section,
  including \(S_N\) centralizer orders, conjugacy-class counting, central
  charge additivity, cycle-type twist weights, join/split weight shifts, the
  two-cycle normalization count, connected torus-cover Hecke weights, and the
  constant-seed partition-number test, plus Riemann--Hurwitz genus tests for
  twist-field two-point and primitive joining covers and beta-normalized
  primitive joining-cover local-coordinate coefficients, Schwarzian
  double-pole weights, primitive-joining OPE powers, and class-normalized
  primitive joining and transposition join/split group factors.
- `thermal_kubo_checks.py`: finite checks for the Volume X Kubo and
  spectral-function conventions, including detailed balance and
  fluctuation--dissipation in a two-level system, the sign
  \(\rho=-2\operatorname{Im}G^R\), the shear-viscosity spectral slope, and
  the vector-potential response sign, plus the fact that real local contact
  terms do not change dissipative spectral slopes, and the finite Mazur
  projection/Drude-weight relation for a current with conserved overlap.
- `trace_anomaly_classification_checks.py`: finite checks for the
  type-A/type-B trace-anomaly classification, including the parity-even bulk
  cohomology counts in \(D=2,4,6\), the engineering weights of the listed
  type-B densities, and the \(-12\) coefficient showing that the four-dimensional
  \(\nabla^2R\) term is shifted by an \(R^2\) counterterm.
- `virasoro_mode_checks.py`: finite residue checks for the two-dimensional
  stress-tensor OPE derivation of the Virasoro algebra, including the
  \((n-m)L_{n+m}\) coefficient, the \(c(n^3-n)/12\) central term, and the
  \(+c/24\) plane-cylinder stress-tensor shift for \(z=\exp(-iw)\).
- `wzw_sugawara_coset_checks.py`: exact arithmetic checks for the WZW and
  coset section, including Sugawara central charges at selected level-one
  simple groups, \(SU(2)_k\) affine-primary weights, the diagonal
  \(SU(2)_k\times SU(2)_1/SU(2)_{k+1}\) minimal-model central-charge
  identity, \(SU(2)_k/U(1)\) parafermion selection and field-identification
  weights, compact parafermion orbit counts, fusion rules, modular
  \(S\)-matrix unitarity, and Verlinde recovery of fusion,
  \(SL(2,\mathbb R)_k/U(1)\) cigar central charges, reflection weight
  invariance, momentum/winding spin checks, bell/cigar one-loop geometry
  residuals and leading-versus-exact central-charge shifts, and the
  Ising/tricritical-Ising coset values.
- `zeta_determinant_checks.py`: numerical and exact checks for the spectral
  zeta-determinant section, including the periodic resolvent identity for
  \(-\dd_\tau^2+\omega^2\), the derivative of
  \(\log\det_\zeta A_\omega\), equality with the canonical oscillator
  partition function, the circle Casimir coefficient
  \(\zeta_{\rm R}(-1)=-1/12\), and the sign of the determinant's scale
  dependence.
- `gamma_trace_checks.wl`: a Wolfram Language version of the same finite
  algebraic checks, adapted from the stringbook spinor appendix and
  `gamma matrices.nb` conventions without relying on `.nb` structure.

Run all available checks from the repository root with:

```bash
tools/run_calculation_checks.sh
```

For Wolfram Language checks, the runner requires a working batch backend when
any `.wl` files are present.  On the author's macOS installation the preferred
entrypoint is

```bash
/Applications/Wolfram.app/Contents/MacOS/WolframKernel -script calculation-checks/<file>.wl
```

The harness probes the selected backend before running checks, rejects `.wl`
files with arithmetic continuations that begin a line with `+`, `-`, `*`, or
`/`, and requires every Wolfram script to print a line of the form
`All Wolfram Language ... passed.`.  Set `QFT_SKIP_WOLFRAM=1` only for an
explicitly Python-only pass.  Set
`WOLFRAMKERNEL=/absolute/path/to/WolframKernel` or
`WOLFRAMSCRIPT=/absolute/path/to/wolframscript` to override executable paths.

Planned checks:

- dimensional-reduction triangle numerator reductions for the axial anomaly;
- background-field one-loop Yang--Mills heat-kernel coefficient bookkeeping;
- conformal-block normalization and Casimir-equation checks;
- superfield, supersymmetry-transformation, and spinor-index convention
  checks for later supersymmetric field-theory volumes;
- simple Feynman-parameter integrals appearing in one-loop examples.
