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
- `banks_zaks_two_loop_checks.py`: exact rational checks for the Banks-Zaks
  two-loop beta-function conventions in the monograph's
  \(\operatorname{tr}_{\square}(t^a t^b)=\delta^{ab}\) normalization,
  including the conformal-window edge and leading \(\epsilon_{\rm BZ}\)
  fixed-point formulas.
- `bf_theory_checks.py`: exact finite cochain checks for the Volume VIII BF
  theory chapter, including finite Fourier projection onto flat cochains,
  the groupoid-cardinality partition function, cellular Wilson gauge
  invariance, and the Wilson/surface linking phase sign.
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
  coefficient identity.
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
  heat-kernel smoothing optimization, and the Sobolev exponent inequalities
  used in the Da Prato--Debussche local fixed-point proof, together with the
  Young-exponent arithmetic in the smooth DPD energy estimate and a finite
  Markov-chain invariant-measure identity, plus the coarse/fine dyadic
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
  entropy exponents after the test-function supremum has been dualized.
- `continuum_scaling_window_checks.py`: finite checks for the Volume XI
  continuum-limit chapter, including the lattice momentum expansion, the
  exact free-scalar pole mass and correlation length, the Gaussian
  mass-squared RG eigenvalue, the \(\nu=1/y_t\) scaling relation, and finite
  Wick-subtraction contact-coordinate shifts.
- `cft_anomaly_regression_checks.py`: finite arithmetic checks for the
  issue-#447 regression class: the \(\pi^0\to2\gamma\) anticommutator factor,
  the \(4/3\) identity-block cubic coefficient, the \(W=-\log Z\)
  stress-tensor source sign, and the Lorentzian-to-radial \([P,K]\) sign.
- `cft_voa_modular_checks.py`: exact \(\mathbb Q(\sqrt2)\) checks for the
  Ising VOA/modular-data example, including \(S^2=1\), Verlinde fusion
  coefficients, quantum dimensions, and shifted character exponents.
- `cohomological_metric_descent_checks.py`: exact polynomial differential-form
  checks for the Volume VIII metric-independence chapter, including
  \(Q^2=0\) in the de Rham model, the graded Leibniz sign, Stokes' boundary
  term on the unit square, and vanishing of a \(Q\)-exact deformation when the
  boundary contribution is zero.
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
- `gamma_trace_checks.py`: mostly-plus gamma-matrix conventions, \(\gamma_5\),
  the Weinberg/Wess-Bagger chiral phase comparison, the four-gamma trace, the
  two-dimensional chirality trace, and the anticommutator normalization used
  in the nonabelian anomaly coefficient.
- `gauge_convention_checks.py`: \(SU(N)\) Hermitian-generator normalization
  \(\operatorname{tr}(t^a t^b)=\delta^{ab}\), output-first structure
  constants, \(C_A=2N\), \(T_F=1\), \(C_F=(N^2-1)/N\), the coupling-coordinate
  conversion from the common half-trace convention, and the Wilson-plaquette
  factor giving \((4g_0^2)^{-1}\int\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\).
- `global_form_line_lattice_checks.py`: exact finite checks for the
  \(\mathfrak{su}(N)\) global-form and Wilson--'t Hooft line-lattice
  section, including the \(\mathbb Z_N^{\mathrm e}\oplus\mathbb Z_N^{\mathrm m}\)
  Dirac pairing, bilinearity and nondegeneracy, \(SU(N)/\mathbb Z_k\)
  Wilson-charge descent, magnetic cocharacter enlargement, and maximal
  isotropy of \(L_{N,k,p}=\langle(k,0),(p,N/k)\rangle\).
- `sw_su2_periods.py`: numerical and exact checks for the pure \(SU(2)\)
  Seiberg--Witten period section, including Picard--Lefschetz monodromy
  matrices, the Picard--Fuchs equation, the electric large-\(u\) asymptotic,
  logarithmic dual-period growth, and linear monopole-period vanishing at
  \(u=\Lambda^2\).
- `thooft_line_local_model_checks.py`: finite checks for the Volume IX
  't Hooft-line local model, including the northern/southern Dirac-monopole
  patch difference, flux normalization, integer Dirac phase, finite linking
  pairing bilinearity, theta-angle Witten-effect automorphism, and Cartan
  surface-operator cocharacter shifts.
- `hawking_bogoliubov_checks.py`: finite numerical checks for the Hawking
  mode-tracing calculation, including the imaginary-axis Gamma-function norm,
  the \(|\alpha|^2/|\beta|^2=e^{2\pi\omega/\kappa}\) ratio, the displayed
  Planck factor in \(|\beta_{\omega\omega'}|^2\), the continuum
  normalization-density identity, and the exponential precursor blueshift.
- `hydrodynamic_modes_checks.py`: finite algebra checks for the Volume X
  hydrodynamic Ward-identity chapter, including shear diffusion, sound
  attenuation, entropy-production positivity for sample transport matrices,
  and the diffusion Einstein relation plus retarded density pole.
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
- `ising_metropolis_finite_checks.py`: exact enumeration checks for the
  `qft_scripts/ising2d_metropolis.py` companion script, verifying the local
  energy difference and detailed balance on the \(2\times2\) periodic Ising
  chain.
- `kinetic_theory_checks.py`: finite algebra checks for the Volume X kinetic
  theory chapter, including Bose/Fermi detailed balance, the H-theorem
  integrand, linearized collision-operator positivity and null vectors, and
  the relaxation-time shear-viscosity integral.
- `large_n_topology_checks.py`: finite checks for the 't Hooft
  large-\(N\) section, including the \(SU(N)\) completeness relation in the
  monograph trace normalization, the planar-versus-one-handle theta-graph
  \(N^{-2}\) suppression, normalized single-trace scaling, and fixed-\(N_f\)
  versus Veneziano quark-boundary counting, plus the displayed baryon Hartree
  pair-counting and fixed-spin rotor \(1/N_c\) scaling.
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
- `nonequilibrium_open_system_checks.py`: finite checks for the Volume X
  nonequilibrium steady-state and open-system chapter, including reservoir
  entropy production, GKSL trace preservation, KMS detailed balance for a
  two-level system, Ornstein-Uhlenbeck noise normalization, and positivity of
  a quadratic noise kernel.
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
  \(c_0=6\) length-two value \(h=3/8\), and the real
  \(\mathbb Z_2\) reflection twist value \(h=1/16\).
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
- `sk_diffusion_action_checks.py`: finite algebra checks for the Volume X
  Schwinger--Keldysh hydrodynamic diffusion action, including the sourced
  density saddle, diffusive response kernel, transverse Ohm response, KMS
  noise coefficient, and Hubbard--Stratonovich noise normalization.
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
- `susy_localization_matrix_checks.py`: finite checks for the compact-space
  supersymmetric localization chapter, including the trace-delta \(S^4\)
  Gaussian coefficient, the \(U(1)\) \(S^4\) Gaussian matrix integral, the
  \(U(1)_k\) \(S^3\) Chern--Simons Fresnel completion of the square, and the
  round-\(S^3\) conjugate-chiral-pair integral
  \(\int d\sigma/(2\cosh\pi\sigma)=1/2\).
- `susy_qm_index_checks.py`: exact rational checks for the Volume I
  SUSY-QM and worldline index-density section, including the oscillator
  supertrace identity, zero-mode index count, two-variable Berezin Pfaffian
  extraction, and the \(\widehat A\)-series coefficients through degree six.
- `symmetric_product_orbifold_checks.py`: exact finite group-theory and
  rational-weight checks for the Volume V symmetric-product orbifold section,
  including \(S_N\) centralizer orders, conjugacy-class counting, central
  charge additivity, cycle-type twist weights, join/split weight shifts, and
  the two-cycle normalization count.
- `thermal_kubo_checks.py`: finite checks for the Volume X Kubo and
  spectral-function conventions, including detailed balance and
  fluctuation--dissipation in a two-level system, the sign
  \(\rho=-2\operatorname{Im}G^R\), the shear-viscosity spectral slope, and
  the vector-potential response sign, plus the fact that real local contact
  terms do not change dissipative spectral slopes.
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
  identity, and the Ising/tricritical-Ising coset values.
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
