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
  Chern--Simons variation, the general hydrostatic Chern--Simons
  source-variation algebra, the \(e^2q^2\) electromagnetic charge factor,
  the cancellation of the Dirac vector-current \(T^2\) vortical term, and
  the sign algebra plus ideal-fluid cancellation in the canonical entropy
  divergence with an anomalous Ward identity.
- `anomaly_matching_wzw_checks.py`: exact rational checks for the anomaly
  matching and Wess--Zumino--Witten coefficient section, including
  \(n=N_c\) from matching the left-flavor anomaly, invariance of the
  completely symmetric descent coefficient under Abelianized Bardeen
  counterterm shifts, recovery of the symmetric cubic anomaly coordinate from
  the Abelianized descent polynomial by polarization, vector-flavor anomaly
  cancellation between the two chiral components of a Dirac quark, and
  \(\operatorname{Tr}(T^3\{q,q\})=1/3\) for the
  \(\pi^0\gamma\gamma\) normalization.
- `anomaly_polynomial_descent_checks.py`: exact rational checks for the
  index-normalized anomaly-polynomial and inflow sections, including the
  closed four-dimensional index coefficient, the local Clifford heat-kernel
  coefficient, six-form \(\widehat A\,\operatorname{ch}\) coefficients, the
  \(2\pi\ii\) conversion to effective-action inflow, universal
  Chern--Weil transgression coefficients through the five-form case,
  the \(n=2\) consistent-descent homotopy coefficients \(1\) and
  \(1/2\), the Abelian descent coefficient, invariance of the fully
  symmetric Cartan cubic anomaly coefficient under Abelianized cubic
  counterterm shifts, the Abelianized Bardeen--Zumino factor turning the
  consistent coefficient \(C\) into the covariant coefficient \(3C\),
  one-generation Standard Model hypercharge sums, and
  \(SU(N)\) fundamental/antifundamental/adjoint cubic-anomaly bookkeeping.
- `standard_model_anomaly_checks.py`: exact rational checks for the
  Standard Model hybrid-definition chapter, including one-generation
  hypercharge anomaly sums, electric charges from \(Q=T^3+Y\), the
  \(\mathbb Z_6\) global-form kernel generator, CKM parameter counting,
  Jarlskog rephasing cancellation, the tree-level \(\rho\)-identity,
  the Higgs mass coefficient, \(B-L\) anomaly bookkeeping with and
  without a singlet \(\nu^c\), Weinberg-operator mass normalization,
  tree-level singlet-neutrino matching, the dimension-six Warsaw-type
  one-generation class counts and field-content dimensions, the local and
  finite determinant-line obstruction checks used in the chiral-lattice
  regulator discussion, including small-cell local holonomy exponents and
  the weak-\(SU(2)\) Pfaffian parity sign,
  strong-CP phase invariance, one-loop gauge beta-function coefficients, GUT
  hypercharge-rescaling conversion, the top-Higgs one-loop subsystem
  coefficients and rank-one matrix-beta specialization, the Higgs
  large-field coupling-chart radial-potential,
  higher-operator ratio, and \(\beta_\lambda|_{\lambda=0}\) identities, and
  basic oblique-parameter identities for the \(S,T,U\) two-point
  coordinates.  It also checks the
  muon \(g-2\) Schwinger
  coefficient, the leading electroweak coefficient normalization, and the HVP
  Feynman-parameter kernel identity used in the hybrid-observable section.
- `background_index_theory_checks.py`: exact rational checks for the
  Volume XII background-index-theory chapter, including the
  \(\widehat A\)-genus expansion through degree eight, the four-dimensional
  \(\widehat A\,\operatorname{ch}\) index formula, trace-delta \(SU(N)\)
  instanton indices, the Abelian \(T^4\) flux index, the six-form
  anomaly-polynomial coefficients, and the Dirac zero-mode selection-rule
  count.
- `dhr_dr_reconstruction_checks.py`: finite algebra checks for the Volume IV
  Doplicher--Roberts reconstruction discussion, including pointed
  \(\mathbb Z/N\mathbb Z\) tensor automorphisms, root-of-unity fixed-degree
  projection, crossed-product associativity and involution, the local
  charged-field-core convention
  \(\rho^q(A)u^q=u^qA\) and recovery of \(\rho^q\) by conjugation, the
  compact \(U(1)\) Laurent-polynomial charge-lattice diagnostic, and the
  nonabelian \(S_3\) diagnostic for faithful standard representation,
  character-ring tensor products, and Haar projection onto the trivial
  isotypic part.  It also checks the neutral-channel projection in
  \(V\otimes V^*\): the identity tensor is fixed, traceless endomorphisms
  are killed, and an arbitrary endomorphism averages to its scalar trace
  component.  It also checks the finite \(S_3\) regular
  charged-coordinate core: right translation rotates matrix-coefficient
  columns, Haar expectation kills the standard and sign multiplets while
  preserving constants, and the same Haar expectation is idempotent,
  invariant under right translation, and a bimodule map over the fixed
  constant algebra.  It checks that \(\wedge^2 V\) gives the sign
  representation, and every left-equivariant automorphism of
  \(\operatorname{Fun}(S_3)\) is a
  right translation, giving the finite Tannakian converse.  The same \(S_3\)
  coefficient functions also check the finite Peter--Weyl Hopf coordinate
  algebra: coefficient functions span all functions on the group, the
  coproduct/counit/antipode identities hold pointwise, Haar is bi-invariant,
  and pointwise multiplication is compatible with the group-law coproduct.
- `free_weyl_net_checks.py`: exact rational checks for the Volume IV massive
  scalar Weyl-net benchmark, including associativity of the finite Weyl
  cocycle, the sign in \(W(u)W(v)=\exp[-i\sigma(u,v)]W(v)W(u)\), the Weyl
  group-commutator phase, symplectic-orthogonality locality, and the finite
  partition phase that turns \(u=\sum_j u_j\) into a product of local Weyl
  generators.
- `wightman_cluster_spectral_checks.py`: exact finite Hilbert-space checks
  for the Volume IV Wightman cluster/vacuum-uniqueness theorem, covering the
  zero-momentum projection algebra, the equivalence between the cluster
  bilinear identity on a dense polynomial orbit and
  \(P_0=|\Omega\rangle\langle\Omega|\), the product contribution of the vacuum
  atom, and removal of the zero atom by \((1-P_0)\).  The analytic
  Jost/Rajchman decay step remains the theorem content in the chapter.
- `wightman_net_bridge_checks.py`: exact rational finite-matrix checks for
  the Volume IV Wightman-to-local-net comparison datum, including parity
  exchange of odd-field spectral projections, the fixed-point observable
  subalgebra, conditional expectation onto observables, recovery of the full
  finite field algebra after adjoining odd spectral projections, a diagonal
  two-region fixed-point diagnostic where a neutral bilocal composite lies in
  the global fixed algebra but not in the algebra generated by separate local
  fixed points, the finite Haag-duality diagnostic separating exterior
  commutation from membership in the assigned local algebra, and the
  distinction between domain-level commutation and strong spectral-projection
  commutation in the bounded algebra model.  It also checks the finite
  spectral-projection algebra fact used in the Schwinger-model AQFT
  checkpoint: shifting a self-adjoint generator by a scalar relabels its
  spectral projections without changing the generated local von Neumann
  algebra.  The Schwinger finite model also checks that affine electric-field
  coordinates generate the same scalar spectral algebra, that current
  coordinates are derivative pullbacks lying inside that algebra, that a
  finite Gauss-law relation is a relation among those coordinates, that a
  line-dressed sector-changing operator is off diagonal rather than a local
  electric/current observable, and that a global flux-sector projection can
  commute with local electric coordinates while remaining outside the bounded
  local electric-coordinate algebra.  It also includes a finite analytic-vector
  strong-locality shadow:
  commuting finite self-adjoint generators have commuting spectral
  projections, and a finite core-like diagnostic in which a commutator
  vanishes on a stable test sector while spectral projections on the full
  space fail to commute.  It also includes a finite affiliation diagnostic:
  spectral projections of a diagonal self-adjoint generator commute with the
  commutant of the diagonal algebra, while odd-field spectral projections fail
  this commutant criterion.
  It also checks that affiliation is weaker than generation: a degenerate
  diagonal affiliated coordinate generates only a proper spectral subalgebra,
  while a second coordinate refines the partition to the full diagonal
  algebra.  Finally, it checks the finite additivity/covariance shadow used
  in the Wightman-to-net bridge: the spectral projections of a noncommuting sum
  \(3Z+4X\) are exact bounded functions of the summed generator inside the
  algebra generated by \(Z\) and \(X\), and conjugation by the finite symmetry
  transports those projections to the transformed summed generator.  It also
  checks the finite orbit-equality diagnostic: a separating vector for the
  generated diagonal algebra detects operator equality from orbit equality,
  while a nonseparating vector lets a proper diagonal algebra have the same
  orbit vector as the scalar subalgebra for selected operators.
- `os_tube_sign_checks.py`: finite checks for the Volume IV
  Osterwalder--Schrader reconstruction chapter, including the mostly-plus
  damping inequality \(p\cdot\eta<0\) for future \(p,\eta\), the ordered
  Euclidean-time map \(z^0=-i\tau=t-i\epsilon\), and the conversion between
  the abstract Fourier--Laplace variable \(x+i y\) and the physical
  Wightman tube depth \(z=\xi-i\eta\).  It also checks the finite insertion
  schedule used in the OS-II argument-domain exhaustion: the \(k\)-gap strict
  argument box is obtained from the one-gap interval by adding one bridge
  coordinate at each step, and checks the insertion-count arithmetic by which
  OS-II linear seminorm growth remains an affine polynomial-bound exponent for
  the regularized quadratic forms.
- `eta_global_anomaly_checks.py`: exact arithmetic checks for the
  Volume XII eta-invariant and global-anomaly chapter, including APS
  orientation bookkeeping, exact APS cylinder endpoint-kernel arithmetic,
  the inward half-cylinder mode-selection sign behind the APS boundary
  condition, the APS sign relating simple-crossing spectral flow to the cylinder index,
  the trace-delta \(SU(2)\) index table,
  Witten's parity criterion \(2j\equiv1\pmod4\), Pfaffian-sign
  multiplicativity, the \(\mathbb Z_2\) mapping-torus character bookkeeping
  behind the clutching construction, the reduced-eta integer jump at a single
  eigenvalue crossing, the finite skew-block Pfaffian orientation model,
  vanishing of the ordinary \(SU(2)\) cubic weight sum, the Quillen spectral-cut transition
  cocycle for determinant-line charts, the Cech-de Rham local
  connection/transition bookkeeping behind determinant-line holonomy, dual
  anomaly-line cancellation,
  nontrivial flat stabilizer holonomy before cancellation, stabilizer-character
  invariance under local frame changes, the single-orbit descent obstruction
  from nontrivial stabilizer character, and the finite
  \(U(1)\)-phase algebra of Dai--Freed gluing, together with a finite cochain
  Stokes model for the contractible-loop step from Bismut--Freed curvature to
  local descent.
- `free_fock_nuclearity_checks.py`: finite checks for the Volume IV
  nuclearity phase-space benchmark, including the bosonic finite-mode product
  formula, the sup-norm lattice shell count and derivative bound, and
  finite-cutoff samples of the \(\beta^{D-1}\log Z_B\) scaling behavior.
- `split_nuclearity_normality_checks.py`: finite matrix-algebra checks for the
  Volume IV nuclearity-to-split mechanism, including normal product-state
  extension through a tensor density matrix, positivity on \(C^*C\),
  independence of split product states from the chosen normal extensions off
  the stated local subalgebras, the separated bilinear expansion produced by a
  finite-rank nuclear map, and the finite type-I shadow with minimal
  projections and a normal trace used to keep positive-collar split data
  separate from sharp type-III local-algebra classification.
- `inflow_anomaly_line_checks.py`: exact finite checks for the anomaly-inflow
  chapter, including the finite Chevalley--Eilenberg sign identity underlying
  Wess--Zumino descent consistency, functorial composition of anomaly-line
  cocycles, local counterterm/frame changes of cocycle representatives, the
  finite-regulator scheme-change coboundary identifying cohomologous anomaly
  representatives, and the finite cochain Stokes identity behind the
  five-dimensional one-form \(BF\) inflow variation.
- `kms_foundation_checks.py`: finite checks for the Volume X KMS-foundations
  chapter, including the finite Gibbs-trace KMS strip boundary condition,
  detailed balance, spectral reconstruction from \(\rho=G^>-G^<\), the
  bosonic fluctuation--dissipation identity, and the
  \(\rho=-2\operatorname{Im}G^R\) retarded-sign convention entering the shear
  Kubo formula, together with the shear, charge-diffusion, and sound pole
  locations used in the hydrodynamic-pole figure.
- `unruh_boost_geometry_checks.py`: finite checks for the wedge modular-flow
  geometry used in Volume IV and Volume XII, including the complex boost
  imaginary part, the \(i\pi\) right-to-left wedge map, right/left wedge
  spacelike separation, detector detailed-balance sign, and the right-wedge
  lightlike half-sided-inclusion sign in the convention
  \(\Delta^{it}=U(\Lambda_R(-2\pi t))\), together with the mostly-plus
  physical light-ray translation sign
  \(U(ae_+)=\exp[-ia(P^0-P^1)]\).
- `qcd_phase_checks.py`: finite arithmetic checks for the Volume X QCD
  phase-structure chapter, including the free QCD Stefan--Boltzmann pressure,
  baryon-chemical-potential coefficients, Banks--Casher kernel normalization,
  fugacity Laurent-polynomial shift, source-curvature susceptibility identity,
  one-loop Polyakov-holonomy potential coefficients, chiral Ward-identity and
  GMOR normalization factors, low-temperature chiral effective theory
  coefficients, static HTL Debye-mass normalization, the Linde magnetic-scale
  power count, thermodynamic derivative identities for QGP observables,
  retarded HTL angular-kernel transversality bookkeeping, Roberge--Weiss
  angle-periodicity bookkeeping, Polyakov-loop effective-measure center-charge
  bookkeeping, high-density Fermi-surface density, dense HDL Debye-mass, and
  patch-curvature coefficients, dense non-Fermi-liquid self-energy
  coefficients, one-gluon exchange color factors in dense pairing channels,
  leading-log magnetic gap coefficient and exponent conversion,
  baryon-number cumulants and radius estimators, CFL gauge-invariant
  composite charges, dense neutrality bookkeeping, CFL screening-sector and
  collective-mode counts, dense Fermi-surface stress scales, CFL
  anomaly-matching coefficients, and the CFL Goldstone count.
- `qcd_dglap_checks.py`: exact rational checks for the Volume II DIS/DGLAP
  conventions, including the \(D_0=(1-x)^{-1}_+\) monomial moments, quark
  number conservation, quark/gluon momentum-column sum rules, the exact
  nonsinglet Mellin moment formula, and the trace-delta versus half-trace cusp
  coefficient conversion, plus the left-endpoint light-ray moment sign
  convention for quark and gluon PDF moment towers and the finite-channel
  RG cancellation \(df=P f\), \(dC=-CP\) in a factorized DIS convolution.
- `qcd_cusp_large_spin_checks.py`: finite checks for the Volume II cusped
  Wilson-line/large-spin section, including the Euclidean cusp angular
  integral \(J(\phi)=\phi\cot\phi\), smooth-line subtraction, the Lorentzian
  lightlike limit, \(D_0\) Mellin moments, the sign of the large-spin
  nonsinglet kernel, and trace-normalization invariance of \(g^2C_R\).
- `qcd_drell_yan_glauber_checks.py`: finite checks for the Volume II
  Drell--Yan/Glauber-status block, including leading-power rapidity
  kinematics, rapidity-scale product bookkeeping, time-reversal-odd staple
  orientation signs, and the finite tensor-product unitarity identity used as
  the algebraic model for Glauber cancellation.
- `qcd_non_global_log_checks.py`: exact rational checks for the finite
  non-global soft-dipole datum in the jets chapter, including real--virtual
  cancellation for unmeasured angular cells, the second-order expansion
  coefficient \(A_{ij}^2-\mathcal N_{ij}\), and the additive-measurement
  boundary where the non-global coefficient vanishes.
- `qcd_bfkl_small_x_checks.py`: finite checks for the Volume II small-\(x\)
  QCD block, including trace-delta versus half-trace invariance of the BFKL
  kernel coefficient, transverse inversion covariance of the dipole kernel
  measure, and the saddle value, first derivative, second derivative, and
  diffusion expansion of the leading BFKL characteristic function.  It also
  checks the finite compact Wilson-line diffusion algebra used as the
  JIMWLK theorem boundary: constant preservation, zero integral of the
  divergence-form generator, dissipative Fourier spectrum, and weak/strong
  duality in a finite torus model.  The same script now checks the finite
  BK-closure ledger: exact \(S\)-to-\(N\) conversion, inward pointing of the
  closed unit-cube vector field, transparent and black-disk fixed points, and
  the \(3L\) finite Gronwall coefficient controlling the connected
  double-dipole closure error.
- `qcd_tmd_gpd_checks.py`: symbolic checks for the Volume II QCD TMD/GPD
  convention block, including Collins--Soper/UV integrability, finite TMD
  scheme-change covariance, fixed-product rapidity-scale cancellation in
  two-hadron factorization, and GPD polynomiality from local twist-two
  contractions.
- `qcd_quasi_pdf_matching_checks.py`: exact finite checks for the Volume II
  quasi-/pseudo-PDF block, including the large-momentum Fourier prefactor
  convention, cancellation of a multiplicative spatial-Wilson-line factor in a
  reduced Ioffe-time ratio, finite matching-kernel scheme covariance, and
  charge preservation from matching-kernel column sums.
- `qcd_sum_rule_checks.py`: symbolic checks for the Volume II current
  sum-rule block, including the Borel transform of the dispersion kernel,
  annihilation of subtraction polynomials, inverse-power OPE terms, and the
  logarithmic Borel mass estimator as a spectral weighted average.
- `qcd_exclusive_pion_checks.py`: exact rational checks for the Volume II
  exclusive-pion asymptotic-freedom section, including the asymptotic LCDA
  normalization, Gegenbauer normalization moments, the plus-prescribed
  leading ERBL kernel eigenvalue normalization, leading ERBL anomalous
  dimensions, and trace-delta versus half-trace conversion for the charged
  pion form-factor coefficient.
- `thooft_model_checks.py`: exact rational checks for the Volume II
  large-\(N\) two-dimensional QCD chapter, including trace-delta color
  normalization, the finite DLCQ quadratic-form identity for the subtracted
  't Hooft kernel, positivity with positive endpoint masses, the massless
  constant zero mode, the endpoint-exponent small-mass expansion in the
  subtracted finite-part convention, and the finite-form monotonicity shadow
  of the closed continuum quadratic-form construction.
- `qcd_theta_witten_veneziano_checks.py`: exact checks for the Volume II theta
  and singlet-axial discussion, including the finite-volume topological
  susceptibility cumulant identity, CP-symmetric first moment, theta
  periodicity by branch relabeling, branch-mixture cluster covariance,
  thermodynamic branch selection, massless-quark theta screening, and the
  Witten--Veneziano mass coefficient.
- `qcd_hqet_checks.py`: finite algebra checks for the Volume II HQET
  Wilson-line section, including the mostly-plus heavy-velocity spin
  projectors, the transverse covariant-derivative projector, residual-momentum
  reparametrization, the free residual-dispersion expansion, and the
  first-order Wilson-line differential equation.
- `qcd_hqet_current_checks.py`: finite checks for the Volume II HQET
  heavy-light-current section, including QCD/HQET state normalization,
  \(f_H\sqrt M\) decay-constant scaling, the mostly-plus recoil variable,
  zero-recoil Isgur-Wise normalization, and finite current-scheme covariance.
- `qcd_nrqcd_checks.py`: finite checks for the Volume II NRQCD/pNRQCD
  convention block, including endpoint cancellation in gauge-invariant
  quarkonium bilocals, the Schrödinger kinetic-sign convention, the singlet
  color factor, the trace-delta to half-trace Coulomb-product conversion, and
  the hard/soft/ultrasoft scale hierarchy.
- `qcd_heavy_mass_static_energy_checks.py`: finite checks for the Volume II
  heavy-mass/static-energy section, including invariance under constant
  mass/potential scheme shifts, quarkonium eigenvalue shifts, the leading
  potential-subtracted mass coefficient, trace-convention invariance of
  \(g^2C_F\), and the attractive sign of the singlet Coulomb coefficient.
- `banks_zaks_two_loop_checks.py`: exact rational checks for the Banks-Zaks
  two-loop beta-function conventions in the monograph's
  \(\operatorname{tr}_{\square}(t^a t^b)=\delta^{ab}\) normalization,
  including the conformal-window edge and leading \(\epsilon_{\rm BZ}\)
  fixed-point formulas, and the sign convention for the IR-attractive
  linearized exponent.
- `bf_theory_checks.py`: exact finite cochain checks for the Volume VIII BF
  theory chapter, including finite Fourier projection onto flat cochains,
  the groupoid-cardinality partition function, cellular Wilson gauge
  invariance, and the Wilson/surface linking phase sign.
- `chern_simons_su2_modular_checks.py`: finite checks for the Volume VIII
  Chern--Simons chapter, including the finite-gauge-transgression winding
  coefficient, the Wess--Zumino extension-ambiguity coefficient in the same
  integral-level normalization, the Abelian limit fixing the total-derivative
  sign, holomorphic-polarization boundary-variation coefficients,
  Polyakov--Wiegmann cross-term bookkeeping, and the \(SU(2)_k\)
  modular-data orthogonality, quantum dimensions, Hopf links, Verlinde
  coefficients, and genus-zero/one state-space dimensions.
- `finite_gauge_state_sum_checks.py`: exact finite checks for the Volume VIII
  finite-gauge state-sum chapter, including action-groupoid cardinality,
  connected-manifold homomorphism counts, closed-surface character formulas
  for cyclic groups and \(S_3\), class-function convolution on the circle,
  the standard \(\mathbb Z_n\) Dijkgraaf--Witten \(3\)-cocycle condition, and
  spanning-tree gauge-fixing counts.
- `finite_gauge_boundary_checks.py`: exact finite checks for the Volume VIII
  Abelian finite-gauge boundary section, including electric/magnetic
  bosonic Lagrangian subgroups, rejection of non-bosonic diagonal subgroups,
  endpoint absorption, and the cylinder-sector count
  \(|\mathcal C/(L_0+L_1)|=|L_0\cap L_1|\).
- `finite_gauge_subgroup_boundary_checks.py`: exact finite checks for the
  Volume VIII subgroup-boundary section, including \(H_0\backslash G/H_1\)
  double-coset sectors, stabilizer/groupoid-cardinality weights,
  \(|H_1|^{-1}\)-normalized boundary-junction convolution with associativity
  and unit sectors, the \(S_3\) two-sector example
  \(X^2=2\mathbf 1+X\), and the relative Dijkgraaf--Witten cochain
  cancellation \(\delta\beta=i^*\omega\), including the opposite-orientation
  cancellation of boundary \(\beta\)-trivializations under relative gluing.
- `bpst_instanton_normalization_checks.py`: finite algebra and radial-integral
  checks for the BPST instanton section, including self-duality of the
  't Hooft symbols, the quadratic \(\eta\)-symbol identity used in the
  curvature calculation, \(\int F^a_{\mu\nu}F^a_{\mu\nu}=32\pi^2\), \(Q=1\),
  the cumulative radial profile drawn in the BPST figure, and the conversion
  between the common half-trace action
  \(8\pi^2/g_{\rm ht}^2\) and the monograph trace-delta coupling
  \(4\pi^2/g_{\rm YM}^2\), plus the one-instanton density checks for the
  scale-invariant \(\dd^4a\,\dd\rho/\rho^5\) factor, zero-mode \(g\)-power,
  one-loop \((\mu\rho)^{b_0}\) RG exponent, the small-instanton
  boundary-exponent threshold \(b_0+\beta_{\mathcal X}>4\), the general
  charge-\(k\) framed ADHM quotient dimension \(4kN_c\), the
  coarea/orbit-volume scaling of the ADHM quotient density, the
  finite-regulator nonzero-mode determinant bookkeeping, and the \(k=1\)
  ADHM orientation dimension and cone-volume power.
- `soliton_collective_coordinate_checks.py`: symbolic finite checks for the
  gauge-Higgs soliton and collective-coordinate section, including the
  Bogomolny and vortex square completions, the Prasad-Sommerfield profile
  equations, the monopole phase-coordinate Legendre transform and
  theta-angle charge-lattice relabelling, the framed monopole moduli
  dimension bookkeeping and horizontal-slice sign, the coordinate
  transformation of \(\sqrt{\det G_{ab}}\,d^mz\), and the \(4N_c\) local
  dimension count of the embedded one-instanton moduli.
- `borel_laplace_checks.py`: exact checks for the Borel--Laplace and
  zero-dimensional quartic large-order section, including Gaussian moments,
  perturbative coefficients, the ratio
  \(a_{n+1}/((n+1)a_n)\to-2/3\), and the corresponding Borel-radius
  normalization, together with the hypergeometric Borel-transform
  coefficient identity, the conformal-Borel map for a single negative cut,
  Borel--Leroy coefficient recovery, the factorial moment/Borel-pole algebra
  in the running-coupling renormalon model, and the algebraic cancellation of
  a two-term OPE renormalon ambiguity.  It also checks the positive-ray
  Euler-integrand bound used in the stable quartic Borel-control proposition
  and the integer-charge/conjugate-pair arithmetic of the instanton-sector
  transseries ledger, the BPST trace-delta instanton action conversion, and
  the finite algebra behind the statement that a Gevrey-one coefficient bound
  gives only local Borel convergence.
- `bphz_forest_formula_checks.py`: finite combinatorial checks for the
  Volume II BPHZ chapter, verifying that the Bogoliubov preparation recursion
  equals Zimmermann's forest formula for nested, disjoint, and overlapping
  subdivergence posets, and that a counterterm appends the subgraph as the
  largest Taylor operation in a nested forest.
- `bound_state_pole_checks.py`: finite algebra checks for the Volume II
  bound-state-pole chapter, including finite-rank spectral-residue
  factorization, mostly-plus denominator conversion \(P^2+M^2=M^2-s\),
  Legendre orthogonality, partial-wave selection of a spin-\(J\) pole, and
  the scalar-QED \(P_1(\cos\theta)\) numerator check.
- `cft_fixed_point_checks.py`: exact finite checks for the opening CFT
  fixed-point chapter, including the \(-(D-1)\partial^2L\) trace of the
  scalar stress-tensor improvement, the special conformal Killing equation in
  mostly-plus signature, the fact that conformal-current divergence depends
  only on the trace, and \(y=D-\Delta\) for linearized RG eigen-directions.
- `bv_localization_checks.py`: exact finite checks for the Volume VIII BV
  integration and localization chapter, including the one-pair BV Laplacian
  product identity, BV Stokes endpoint term, the BV-pushforward boundary
  obstruction identity, normal Gaussian Pfaffian/determinant factor,
  rank-one Mathai--Quillen normalization, and the \(S^2\) Atiyah--Bott
  fixed-point coefficient identity.
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
- `hamiltonian_truncation_dlcq_checks.py`: finite checks for the
  Hamiltonian-truncation and DLCQ benchmark chapter, including the Ising
  energy-deformation Bogoliubov spectrum, the finite sine-Gordon zero-mode
  vertex selection rule and second-order perturbative shift, the compact-boson
  sine-Gordon oscillator vertex assembly and spin-projection rule, the normal-ordered
  \(1+1\)-dimensional scalar \(\phi^4\) truncation basis and zero-mode matrix
  element, the scalar \(\phi^4\) DLCQ harmonic-resolution basis and
  convention-sensitive quartic matrix elements, the large-\(N\)
  two-dimensional QCD DLCQ quadratic-form identity, connected Ising TFFSA
  spin-block normalization, the \(E_8\) magnetic-Ising target-ratio
  Perron--Frobenius check, light-front metric and mass-shell bookkeeping,
  the one-particle measure Jacobian, residual-to-spectrum bound,
  spectral-projector leakage control, the finite Feshbach determinant
  identity behind truncation counterterms, and Krylov/Lanczos Ritz-residual
  plus finite spectral-moment identities.  It also verifies finite variational ansatz
  identities: energy variance as residual norm, spectral and ground-projector
  bounds, tangent-gradient formula, and local-energy mean/variance
  identities used by sampled neural-state calculations, the score-covariance
  force identity used in finite neural/VMC optimization, the finite
  transfer-operator spectral expansion and effective-mass diagnostic for
  matrix-product-state correlators, and the finite cross-method compatibility
  bound for comparing lattice, Hamiltonian
  truncation, and DLCQ coordinates after the target observable and
  normalization maps have been declared.  The same check imports the
  reader-facing `qft_scripts/benchmark_manifest_consistency.py` smoke
  manifest and verifies both a passing finite pairwise check and a
  deliberately failing manifest outside the declared envelopes.
- `charged_flux_dressing_checks.py`: finite checks for the charged-sector
  Haag--Ruelle/LSZ discussion, including the boosted Coulomb flux integral,
  extraction of the charged velocity from flux extrema, the half-line Fourier
  transform of an asymptotic worldline current, and the equality between the
  worldline-current denominator and the momentum-space eikonal denominator.
  It also checks the Coulomb-tail logarithmic Dollard phase coefficient,
  the oriented pairwise many-body Dollard logarithm with creator/adjoint
  signs, decay of the log-subtracted pair remainder on large dyadic time
  intervals, the discrete Cook-tail distinction between an unsubtracted
  \(1/t\) derivative and an \(L^1\) residual, and the same-flux truncation
  schedule arithmetic needed for a noncompact Wilson-line tail to define a
  uniform large-time asymptotic coordinate.  It checks the pair-coefficient
  residual budget: the correct logarithmic Dollard coefficient leaves an
  \(L^1\) residual, a wrong coefficient leaves a nonintegrable dyadic
  \(1/t\) tail, compact same-flux deformations alter only finite phases, and
  equal velocities lie outside the separated-pair estimate.  It also checks
  the finite
  spectral-measure arithmetic behind the nonconfining charged-sector
  boundary: common finite-energy windows, Markov's sufficient first-moment
  estimate, and linear string-energy escape beyond every fixed cutoff.
  It also checks soft coherent
  velocity-separation positivity, finite-cutoff Weyl characteristic
  functionals, coherent-overlap decay, and finite Hilbert soft-coordinate
  transformations.  The same script checks the finite
  left-inverse algebra of dressed LSZ residues: the pole residue is a Gram
  matrix of charged one-particle overlaps, and finite dressing-coordinate
  changes leave the extracted amplitude invariant.  It also verifies the
  finite boundary-charge Ward bookkeeping for dressed correlators: abelian
  signed charges must sum to zero in vacuum matrix elements, and elementary
  \(SU(2)\) endpoint representations contribute only through singlet channels.
  It further checks that boundary-charge neutrality is only the zero-mode
  condition on the angular flux profile: opposite charges with the same
  velocity cancel pointwise, while opposite charges with different velocities
  have zero total charge but a nonzero angle-dependent flux profile.
  It also checks the compact abelian Wilson-line path-deformation algebra:
  the change of a line integral is an exact curvature surface flux and hence
  changes only a neutral surface factor, not the endpoint charge.
- `cs_matter_lightfront_checks.py`: exact coefficient checks for the
  three-dimensional Chern--Simons--matter light-cone-gauge section, including
  the factor of two in the quadratic light-cone Chern--Simons action, the
  first-order Gaussian source sign, the trace-delta large-\(N\) color
  contraction, and the rational part of the planar exchange coefficient
  \(N(2/k_{\rm eff})=2\lambda\), together with the bilocal saddle scaling
  \(N^2(2/k_{\rm eff})=2N\lambda\) versus the \(O(1)\) trace subtraction,
  the exact rank/level and complementary-coupling algebra behind the planar
  Chern--Simons vector-model bosonization datum, the finite-matrix derivative
  giving the planar bilocal self-energy, and the index convention in
  \(G(Q+\Sigma)=1\).  It also verifies the bilocal Hessian/Bethe--Salpeter
  source-response convention for planar singlet two-point functions.
- `chpt_nlo_checks.py`: finite arithmetic checks for the NLO chiral
  perturbation theory section, including the ten \(L_1,\ldots,L_{10}\)
  Gasser--Leutwyler labels, selected \(\Gamma_i\) entries, and the
  cancellation of the \(\mu\)-dependence in the two-flavor
  \(M_\pi^2\) chiral logarithm by the running of \(l_3^r(\mu)\).
- `qed_form_factor_checks.py`: exact rational checks for the Volume I QED
  renormalization and form-factor chapter, including the photon
  vacuum-polarization pole coefficient, Ward organization \(Z_1=Z_\psi\),
  Dirac--Pauli conversion \(F_1=F+G\), \(F_2=-G\), the zero-transfer
  vertex-parameter integral, and Schwinger's
  \(g_{\mathrm{mag}}-2=\alpha/\pi\) normalization.
- `qed_external_state_checks.py`: finite sign checks for the Volume I QED
  external-state chapter, including local charge neutrality, Abelian
  Wilson-line endpoint cancellation, field independence of the Abelian
  Faddeev--Popov determinant, tree Compton longitudinal Ward-cancellation
  signs, and the fixed-incoming-label cross-section sum.
- `conformal_collider_checks.py`: exact rational checks for the ANEC and
  conformal-collider section, including the \(S^2\) angular averages in the
  four-dimensional stress-tensor flux form, the helicity \(2,1,0\) reductions
  to the Hofman--Maldacena inequalities, the full helicity-projector spectral
  decomposition of the stress-tensor detector quadratic form, the vanishing
  of the integrated \(t_2,t_4\) deformations, and the embedding-space
  light-transform homogeneity map \((\Delta,J)\mapsto(1-J,1-\Delta)\), plus
  the null-cut modular-variation sign bookkeeping and entropy-squeeze
  inequality behind the modular ANEC route, and the transverse homogeneity
  ledger for coefficient distributions in the light-ray OPE.
- `conformal_light_transform_algebra_checks.py`: exact polynomial checks for
  the conformal-algebra convention behind the light transform, including the
  Euclidean conformal Killing vector bracket table, the charge sign conversion
  from \(U(s)=\exp(i sQ)\), the radial real-form conversion used in descendant
  Gram matrices, and the light-transform weight map
  \((\Delta,J)\mapsto(1-J,1-\Delta)\).
- `cft_energy_detector_contact_checks.py`: exact finite positive-measure
  checks for the CFT light-ray/energy-correlator chapter, including the
  statewise detector Riesz bound, finite-bin Cauchy--Schwarz positivity,
  finite-resolution Lipschitz partition estimates for one-detector and
  detector-product measures,
  compact moment-matrix positivity, finite-grid moment reconstruction,
  truncated-moment ambiguity,
  off-diagonal plus diagonal split of two detector products, the vanishing of
  diagonal terms for disjoint detector supports, the total-energy Ward
  identity \(\mathcal G_2(1,1)=\langle(P^0)^2\rangle\), the
  partition-of-diagonals decomposition for three detector insertions, and the
  finite CFT light-ray OPE chart bound obtained from retained coefficient-map
  norms, light-ray form bounds, and the declared remainder, with a separate
  check that separated-angle data alone do not determine the diagonal contact
  coordinate.  It also checks retained-basis covariance of the finite
  light-ray chart and the compensating contact-coordinate shift required when
  diagonal distributions are reshuffled between retained coefficient maps and
  explicit contact terms.  It also checks the small-angle EEC pushforward
  exponent: the actual \(\delta(\cos\chi-\cos\theta)\) kernel contributes one
  inverse shell power relative to a \(\delta(\chi-\theta)\) convention, and
  changing to \(z=(1-\cos\chi)/2\) halves the leading power.
- `cosmological_particle_creation_checks.py`: exact convention checks for the
  Volume XII cosmological-particle-creation chapter, including the
  conformal-coupling cancellation in arbitrary dimension, de Sitter
  \(\nu\)-parameter arithmetic, sudden-quench Bogoliubov normalization, the
  Riccati equation for a power-law adiabatic frequency, and finite positive
  type of detector-response Gram forms.
- `energy_correlator_sum_rule_checks.py`: exact finite-event checks for the
  energy-energy-correlator zeroth and first moment sum rules and the
  coincident-detector contact weight in the QCD detector-observable chapter;
  it also checks the finite-event multiplication-operator algebra for smeared
  detector products, diagonal contact contributions, ensemble-connected
  cumulants versus detector-contact strata, and the endpoint delta-coordinate
  ledger that glues an open-interval EEC distribution to the two exact
  detector moment constraints.
- `energy_correlator_collinear_checks.py`: exact rational checks for the
  tree-level small-angle EEC coefficient, including local detector-weight
  conservation, cancellation of real splitting-kernel endpoint poles by the
  ordered EEC weight \(2x(1-x)\), and the resolved real-kernel integrals
  \(\frac32 C_F\), \(\frac{14}{5}C_A\), and \(\frac15T_F\).
- `energy_correlator_light_ray_ope_checks.py`: finite algebraic checks for
  the renormalized small-angle EEC light-ray OPE bookkeeping, including the
  plus distribution on \(0<\rho<\rho_0\), cancellation of the endpoint cutoff
  logarithm against the contact subtraction, the finite \(\delta(\rho)\)
  moment, the finite-resolution identity that moves an endpoint annulus into
  the compensating contact coordinate, the row/column anomalous-dimension
  sign convention, finite \(Z^{-1}dZ\) operator mixing, finite scheme-change
  covariance, paired coefficient/operator invariance, finite path-ordered
  light-ray transport, derivative-term signs in the two-scale flatness
  equation, the cusp-log rapidity chart and its wrong-sign curvature
  obstruction, flatness versus curvature obstruction, and the energy-sum
  left-null-vector condition.
- `energy_correlator_track_checks.py`: exact rational checks for the
  selected calorimetric measure and track-energy-correlator bookkeeping,
  including the selected EEC zeroth and first moment identities, selected
  contact weight, the binomial collinear track-function moment ledger, and
  the reduction of the separated track-EEC weight to \(2z(1-z)\) for the
  full calorimeter.
- `energy_correlator_sudakov_checks.py`: exact rational checks for the
  back-to-back EEC leading Sudakov factor, including
  \(\int_0^{L_b}u\,du=L_b^2/2\), the fixed-coupling differential equation for
  \(\exp[-\Gamma_{\rm cusp}^qL_b^2/2]\), and trace-delta versus half-trace
  invariance of the one-loop cusp coefficient \(g^2C_F/(4\pi^2)\).
- `constructive_scalar_spde_checks.py`: finite checks for the constructive
  scalar and singular-SPDE chapters, including Hermite/Wick coefficients for
  \(:\phi^2:\), \(:\phi^3:\), \(:\phi^4:\), finite Wiener-chaos isometry and
  moment constants, the exact two-mode finite-Langevin reversibility and
  Dirichlet-form identity fixing the \(\sqrt2\) noise normalization, the
  sharp-cutoff tadpole coefficients in two and three Euclidean dimensions,
  the displayed
  \(\phi^4_d\) superficial-degree formula, and the two-loop
  \(\Phi^4_3\) sunset combinatorics giving the logarithmic mass-coordinate
  coefficient in the chapter's \(\lambda\phi^4+\alpha\phi^2\)
  normalization, the finite-cutoff local stability lower bound, the
  multiscale phase-cell geometric tail estimate and its source-decorated
  Schwinger-seminorm variant, plus the
  stochastic-quantization OU variance, two negative-Sobolev threshold checks,
  heat-kernel smoothing optimization, the path-space
  \(\Phi^4_2\) enhanced-noise increment and Kolmogorov threshold arithmetic,
  and the Sobolev exponent inequalities used in the Da Prato--Debussche
  local fixed-point proof, together with the
  three-dimensional Sobolev obstruction to applying the same DPD closure to
  \(\Phi^4_3\), the Young-exponent arithmetic in the smooth DPD energy
  estimate, a finite Markov-chain invariant-measure identity, and the
  bounded-Lipschitz defect arithmetic for the coupled stationary-law
  comparison, plus the coarse/fine dyadic
  exponent arithmetic in the compact reconstruction proof and the
  homogeneity/sign/combinatorial checks for the dynamic \(\Phi^4_3\) BPHZ
  local counterterm calculation, together with exact arithmetic for the
  abstract modelled-distribution fixed-point ball, contraction, and Picard
  tail estimates, the fixed-point-sector perturbation budget that transfers
  model-map convergence to solution convergence, plus the dyadic geometric-tail arithmetic in the random
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
	  coordinate supremum arithmetic, the shell-separated cutoff summation that
	  converts \(2^{-\rho(n-m)_+}\) into a scale-summed \(2^{-\rho_*n}\) rate
	  when slack beats entropy, the projective shell-separated coordinate
	  arithmetic that sums finite-chaos constants before the dyadic-net and
	  shell-summation steps, the specialized nonlinear \(\Pi\)-coordinate
	  shell-cutoff arithmetic for \(XY\) with physical-scale entropy \(5\),
	  edge entropy \(6\), and retained rate
	  \(\rho_*<\min\{\rho,\sigma-5/p\}\), and the seven-coordinate constants in the
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
  formulas, together with the marginal \(XY\) graph power-counting and the
  conversion of its logarithmic scalar tested-coordinate loss and same-scale
  parameter-edge loss into \(4\kappa-\zeta_{XY}\) normalized slack, plus the
  cutoff-shell arithmetic converting the minimum proper-subgraph deficit
  into the scalar scale-separated gain \(2^{-\rho(n-m)_+}\), the
  physical-scale arithmetic for the logarithmic first-chaos \(X^2Y\) bound,
  the first-chaos cutoff-shell and parameter-edge arithmetic, and the dyadic covariance
  double-increment scale gains entering that bound, the OS-II reconstruction-growth
  bookkeeping that keeps reflected positive-time cylinder tests at linear
  seminorm order, the finite SPDE/constructive hierarchy-transfer check for
  matching OS Gram forms and growth envelopes, a finite hard-core polymer
  source-cumulant check showing factorization without an incompatibility bridge
  and a nonzero connected
  cumulant with such a bridge, exact set-partition enumeration for the
  connected-to-full Schwinger hierarchy growth loss, and the
  interval-recursion arithmetic in the rough-forcing energy-to-Besov
  bootstrap.
- `continuum_scaling_window_checks.py`: finite checks for the Volume XI
  continuum-limit chapter, including the lattice momentum expansion, the
  tree-level Symanzik cutoff artifact and improved-kernel cancellation, the
  exact free-scalar pole mass and correlation length, the Gaussian
  mass-squared RG eigenvalue, the \(\nu=1/y_t\) scaling relation, the
  finite-size endpoint variable and irrelevant correction, the physical
  finite-volume scaling variable, and finite Wick-subtraction
  contact-coordinate shifts.
- `rg_projection_checks.py`: exact rational checks for the Volume XI
  rigorous-RG projection-truncation section, including a spurious projected
  zero with no full fixed point and the finite-dimensional
  complement-residual lift condition used in the Newton--Kantorovich
  argument, plus the finite irrelevant-tail graph equation illustrating why
  projected local coordinates alone do not define a Wilsonian fixed point.
  It also checks the residual-lift plus reconstruction-seminorm budget that
  turns a projected fixed point into a controlled finite-window observable
  approximation, and the finite-step residual amplification bound for a
  projected functional-RG flow.  It also checks the tensor-RG truncation
  residual recursion and its finite observable-window transport.
- `rg_fermionic_fixed_point_checks.py`: exact rational checks for the
  Volume XI long-range fermionic rigorous-RG benchmark, including the
  kernel scaling-dimension ledger
  \(D_{\rm sc}=d-n(d-\Delta_1)-m(d-\Delta_2)-\ell[\psi]-|p|_1\), the
  pinned \(L^1\) exponent relation, the trimmed local-coordinate list, and
  a finite irrelevant-tail fixed-point graph equation.
- `rg_hierarchical_scalar_checks.py`: exact rational checks for the Volume XI
  hierarchical-scalar RG benchmark, including the Gaussian
  Wick-coordinate eigenvalue
  \(D\mathcal R_0(:\Phi^n:)=b a^n:\Phi^n:\), the engineering exponents
  \(y_{2r}=D-r(D-2)\), and the relevance/marginality/irrelevance
  bookkeeping for the mass, quartic, sextic, and higher scalar coordinates.
- `rg_short_range_reconstruction_checks.py`: exact finite checks for the
  ordinary short-range scalar block-spin reconstruction datum, including
  block-kernel normalization, constant-field scaling, invariance of the
  block-constant distribution pairing, the adjoint source-blocking identity
  with its \(L^D\) pullback factor, the uniform-kernel smooth-test sampling
  error bound, independent-site covariance scaling, geometric
  reconstruction-bound arithmetic, and correction-to-scaling bookkeeping
  separating universal irrelevant exponents/correction
  distributions from regulator-dependent amplitudes.  The script also checks
  the auxiliary-to-short-range RG transfer telescope and the relevant-direction
  amplification formula, together with the quantitative microscopic tuning
  contraction constants used to separate stable comparison estimates from
  unstable tuning data.  It also checks the non-diagonal unstable-block
  amplification formula for a finite Jordan block, including the polynomial
  loss beyond the diagonal eigenvalue exponent and the corresponding
  propagation of one-step relevant-coordinate errors.  It also checks the
  auxiliary projective-window transfer estimate combining auxiliary-window convergence,
  auxiliary-to-target observable defects, short-range orbit-transfer
  defects, and normalization mismatch.  It also checks the differentiated
  Lyapunov--Perron equation for a finite one-dimensional nonlinear stable
  graph, verifying the \(C^1\) stable-graph derivative formula and tangency
  to the stable subspace.  It also checks the projective observable-germ finite-window
  estimate used to prevent finite observable agreement from being
  overstated as full universality.  It also checks the projective
  distribution-window extension check: compatible finite
  test-function windows plus a single seminorm bound define one bounded
  functional, while restriction defects and declared-bound failures are
  detected explicitly.  It also checks the cofinal finite-window assembly
  step: regulated compatible windows with a uniform seminorm bound must be
  cofinal and Cauchy on each already-controlled finite window before they
  determine a limiting tempered distribution.  It also checks the moving
  finite-window approximation step: scale-dependent finite approximants
  \(\Pi_{N_k}f\) converge to the value of the limiting distribution on the
  fixed test function only when the same seminorm controls the projection
  tails and the window schedule is cofinal.  It also checks the
  QFT-strength observable-germ
  warning that matching a visible finite correlator window can miss a hidden
  OS-positivity Gram-window failure.  It also checks the finite
  reflection-positive block-spin pullback mechanism: a coarse positive-time
  Gram matrix obtained from a reflection-compatible block field is the
  compression \(B^T G_{\rm fine}B\) of the fine positive-time Gram form.
  It also checks the
  finite OS-positivity bound: if a regulated Gram matrix has a lower
  spectral bound and the limiting window has a declared entrywise error, the
  limiting Gram matrix retains the quantified positive lower bound.  It also
  checks the complementary family-size obstruction by an all-ones perturbation,
  the safe \(m\)-dependent entrywise-error schedule for directed positive-time
  windows, and the approximate OS-positivity defect budget
  \(\delta_m+m\epsilon_m\) needed when regulator positivity is available only
  up to a defect.  It also checks the short-range RG-to-OS assembly budget combining
  source-window chart errors, thermodynamic tails, cofinal-window errors,
  Cauchy extraction, directed OS Gram lower-bound bookkeeping, and the common
  directed scale schedule needed to close source, Gram, time-continuity, and
  OS-II estimates on the same regulator tail.  It also checks the finite
  restriction/Cauchy arithmetic used in the directed OS-positive form assembly
  lemma.  A
  fixed entrywise tolerance loses positivity once the \(m\epsilon\) term
  overwhelms the regulated lower bound, while an operator-norm estimate has the
  dimension-independent lower bound stated in the chapter.  It also checks the
  positive-time translation-window estimate used for OS semigroup continuity,
  including the support margin, quadratic modulus, regulator-error limit,
  null-quotient stability condition, and dense-domain extension bound.  It also
  checks the
  stable-chart observable-window bound that decomposes a finite
  universality comparison into relevant mismatch, stable-coordinate
  contraction, accumulated one-step defects, and source-tail or
  normalization errors.  It also checks the
  one-step polymer
  contraction budget \(x_{k+1}\le qx_k+B_{\rm pol}x_k^2+\varepsilon_k\),
  including the finite radius smallness condition, the quadratic
  circle-product bound, the finite interval pair-overlap majorant
  underlying \(B_{\rm pol}\), and the scale-summed forcing estimates that
  turn extraction defects into a uniform multiscale smallness condition.  It
  also checks the finite-range Gaussian characteristic-function factorization
  behind independent fluctuation integration on separated polymers, together
  with the mixed term produced by a nonzero covariance tail.  It also checks
  the summable covariance-tail replacement for exact factorization: shell
  counting gives a Schur tail bound, and the resulting cross-covariance
  operator bound controls the connected bridge between separated polymer
  observables.  It also checks the finite Taylor-localization remainder bound
  and the canonical
  local-monomial scaling exponents, including the fact that a \(D=3\)
  canonical scalar \(\phi^6\) coordinate has no engineering irrelevant gain.
  It also checks the finite Gaussian stability identity for a quadratic
  large-field regulator, including the determinant prefactor, the exact
  exponent, and the spectral-bound exponent enlargement needed after
  fluctuation integration.  It also checks the source-window extraction rule
  for a source-extended polymer chart: retained Taylor-source derivatives
  vanish in the tail, omitted derivatives obey the Cauchy-radius bound, and
  propagated source-tail errors sum with the declared scale weights.  It also
  checks finite source-window-to-cumulant extraction: Cauchy control of
  derivatives from holomorphic window convergence, restriction compatibility
  for \(E\subset F\), and the separate uniform Schwartz-seminorm bound needed
  to extend compatible finite windows to a distribution.  It also checks the
  OS-II source-majorant bridge: a uniform holomorphic moment-source bound on
  insertion-dependent polydiscs gives the Cauchy moment estimate, the
  projective tensor seminorm estimate, and the \(B_{\rm OS}=C_\pi B/\rho\)
  growth constant, while a shrinking source radius is detected as a failure
  mode for corrected OS reconstruction.  It also checks the connected
  cumulant-to-moment partition bridge: exact set-partition enumeration
  verifies the Schwinger moment bound obtained from connected-cumulant bounds
  and the unavoidable factorial-exponent loss from the Bell/partition
  overcount, while hidden cluster-count growth is detected as a failure mode.
  It also checks the polymer source-derivative norm feeding this bridge:
  an exponentially weighted derivative-cluster norm controls both the
  unweighted connected cumulant and the separated-support decay bound, while
  hidden source-window growth is detected as a failure mode.  It also checks the
  source-chart-to-holomorphic-window estimate: convergence of the local
  normalizing coordinate, retained local coordinates, source-decorated
  polymer tail, and finite-step remainder gives a uniform source-window
  bound on a fixed polydisc before Cauchy extraction is invoked.  It also
  checks the source-stable trajectory estimate combining stable contraction,
  unstable source-local amplification, polymer-tail control, and
  normalizing/remainder defects before a source window can be used.  It also
  checks the
  finite-volume source-window cluster-tail estimate: a connected-polymer
  bridge majorant with exponentially weighted shell sums gives the
  boundary-tail bound on holomorphic source functionals; that bound gives the
  corresponding cumulant-derivative Cauchy estimate, controls comparison of
  cofinal exhaustions, and combines with an RG-chart error in the joint
  scale/volume schedule.
- `lattice_gauge_blocking_checks.py`: exact finite \(S_3\) checks for the
  Volume XI gauge-compatible RG construction, including endpoint covariance
  of path-blocked coarse links, equality of the blocked Wilson loop with the
  concatenated fine plaquette, invariance of the Wilson-loop character under
  coarse gauge transformations, gauge invariance of a fine plaquette
  class-function weight, and invariance of the blocked pushforward weights
  under the coarse gauge group.  It also checks that closed-loop source
  coordinates and their rational source polynomial descend to coarse gauge
  orbits, while an open-link source fails the invariance test, matching the
  gauge-invariant source-window construction in Volume XI.  It also checks
  the finite arithmetic behind the weighted polymer-tail bound used in the
  gauge-blocking locality datum and the compression of a reflection-positive
  finite Gram matrix by a blocking map.  It also detects a nondecaying
  polymer-tail failure mode and checks the finite reconstruction error budget
  \(C\varepsilon+\eta\), including that the residual reconstruction term is
  load-bearing.
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
- `conformal_manifold_checks.py`: exact finite checks for the conformal
  manifold and exact-marginality source-coordinate section, including
  Klebanov--Witten, \(\mathcal N=4\), and standard ABJM local dimension
  counts, the rank-count quotient by beta constraints and redundancies, the
  tensorial coordinate transformation law for the Zamolodchikov metric, and
  the null-direction quotient for redundant marginal coordinates.
- `cft_voa_modular_checks.py`: exact \(\mathbb Q(\sqrt2)\) checks for the
  Ising VOA/modular-data example, including \(S^2=1\), Verlinde fusion
  coefficients, quantum dimensions, shifted character exponents, the
  \(T\)-phase spin-selection rule, uniqueness of the diagonal genus-one
  Ising modular invariant with one vacuum, the Cardy Tauberian saddle
  coefficient, the finite multi-edge sewing trace-norm bound and paired
  internal-edge relabelling invariance, Verlinde/topological-defect
  eigencharacters, exact temporal to spatial defect \(S\)-move
  multiplicities, the Ising spin-field
  one-point selection rule under the spin-flip defect, the rank-two
  logarithmic Jordan-cell Ward identities and trace invisibility of the
  nilpotent extension, the dual-number projective pseudo-trace detecting the
  nilpotent \(\tau\)-coefficient missed by the ordinary character, and the
  Zhu-algebra top-weight polynomial with its primitive idempotents.
- `cft_virasoro_minimal_checks.py`: exact checks for the unitary Virasoro
  minimal-model and Ising BPZ-block material, including Kac-table
  identifications, Ising and tricritical-Ising weights, the Rocha--Caridi
  theta-character Poisson transform producing the A-series minimal-model
  \(S\)-matrix, \(S^2\), Verlinde integrality, agreement with the exact
  \(SU(2)\)-quotient fusion rule, the Coulomb-gas background-charge
  convention, screening dimensions, Kac weights, charge reflection modulo the
  unitary null charge relation, the Euler beta integral used in the
  one-screening Dotsenko--Fateev block, the level-two Gram determinant and
  null vector, the level-two Kac determinant roots \(h_{1,2}\) and \(h_{2,1}\),
  the Ising spin-field BPZ differential equation, and the crossing matrix
  fixing \(C_{\sigma\sigma\varepsilon}=1/2\).
- `cft_higher_genus_sewing_checks.py`: exact finite checks for the
  higher-genus sewing section, including equality between one-channel basis
  sewing and the propagation inner product, torus one-point traces from
  self-sewing, the vacuum character trace, and the graph formula
  \(g(\Gamma)=\sum_v g_v+b_1(\Gamma)\).
- `nonrational_cft_direct_integral_checks.py`: exact finite checks for the
  direct-integral nonrational-CFT formalism, including unitarity of a rational
  fusing kernel, preservation of the Plancherel inner product under channel
  change, the finite direct-sum version of the spectral radial-product
  identity, the noncompact free-boson charge-convolution associativity, and
  the modular-weight cancellation in the noncompact partition density
  \(\tau_2^{-1/2}|\eta|^{-2}\).
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
  fusion associativity, fusion-ring characters, the normalized Cardy two-bulk
  classifying sewing identity, the matrix-unit Frobenius cutting move behind
  rational boundary sewing, the finite classifying-center model for
  non-diagonal rational boundary sewing, boundary entropy squares,
  Chan--Paton direct sums, the positive spectral weight in the
  boundary-entropy gradient metric, compact-boson T-duality zero modes,
  Ising boundary-changing fusing constants and OPE powers, the finite
  four-boundary Cardy--Lewellen sewing cell, and the Liouville FZZT/ZZ
  hyperbolic identities used in the nonrational boundary-state discussion.
- `liouville_bpz_checks.py`: exact algebra checks for the Liouville chapter,
  including the probabilistic GMC threshold normalization
  \(Q_\gamma=2/\gamma+\gamma/2=b+b^{-1}\) and the distinction between the
  first-moment and Seiberg local-integrability bounds, the level-two BPZ null
  vector, its \(b\leftrightarrow b^{-1}\) dual, one-screening and dual
  one-screening coefficient rewrites, DOZZ \(b\)-shift powers,
  hypergeometric connection arguments, Virasoro block coefficients through
  level three with Gram determinant factorization and global-block limits,
  the FZZT \(b\)- and \(b^{-1}\)-shift ratios, the normalized FZZT boundary
  finite-difference identity together with the two exponential branches and
  reflection-even selection, and the elliptic \(q\)-coordinate conversion
  through \(q^2\).
- `superconformal_algebra_checks.py`: exact rational checks for the
  two-dimensional superconformal-algebra chapter, including the
  \(\mathcal N=1\) Ramond zero-mode shift, \(\mathcal N=2\) chiral-primary
  norm identities, spectral-flow automorphism, NS-to-R ground-state shift,
  extended \(\mathcal N=2\) spectral-flow operator weights, charges,
  Heisenberg OPE exponents, and descendant charges, protected
  Landau--Ginzburg central-charge arithmetic, elliptic-genus spectral-flow
  Jacobi multipliers, Fourier-coefficient orbit discriminants,
  Landau--Ginzburg \(\chi_y\) Ramond charge
  polynomials and Witten-index counts, and the
  supersymmetric \(SU(2)/U(1)\) and \(SL(2,\mathbb R)/U(1)\) rank-one
  coset central-charge, compact chiral-ring, chiral-primary,
  field-identification, and spectral-flow formulas.
- `cohomological_metric_descent_checks.py`: exact polynomial differential-form
  checks for the Volume VIII metric-independence chapter, including
  \(Q^2=0\) in the de Rham model, the graded Leibniz sign, Stokes' boundary
  term on the unit square, and vanishing of a \(Q\)-exact deformation when the
  boundary contribution is zero.
- `cohomological_field_theory_checks.py`: exact finite checks for the Volume
  VIII cohomological-field-theory chapter, including the Cartan identity
  \(d_C^2=-u\mathcal L_v\), equivariant closure of
  \(\omega+u\mu\) for the Hamiltonian rotation model, the
  Mathai--Quillen auxiliary Gaussian square-completion sign, rank-one
  zero-locus orientation, and the squared normal inverse-Euler factor
  \(\operatorname{Pf}(C)^2/\det(A)\) for a two-even/two-odd local model.
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
  \(\sum_\alpha\lambda_\alpha^{1-g}\), together with the semisimple
  separability idempotent, the splitting of \(A^e\to A\), and the
  \(HH_0(\Bbbk^r)=\Bbbk^r\) commutator check.
- `donaldson_sw_comparison_checks.py`: exact arithmetic checks for the
  Witten-Donaldson and Seiberg-Witten comparison chapter, including the
  anti-self-dual deformation-complex index, the monopole expected-dimension
  formula from Dirac plus Abelian gauge indices, the
  \(2\chi+3\sigma\) identity, Donaldson descent degrees,
  \(\operatorname{Spin}^c\) characteristic-lift bookkeeping, K3 and
  elliptic-surface simple-type arithmetic, blow-up square shifts, Furuta
  inequality examples, and the trace-delta instanton-action coefficient.
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
- `categorical_defect_structure_checks.py`: exact finite checks for the
  categorical-symmetry defect-fusion chapter, including defect fusion as
  composition of local-operator actions, noninvertible projection kernels,
  dagger reversal of junction composition, positivity of the finite
  reflection pairing, the BPZ weighted-adjoint identity for defect actions,
  and unitarity of isotopy changes of junction basis.
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
- `spinor_convention_checks.py`: exact finite checks for the local
  spinor-convention section, including the mostly-plus Clifford algebra,
  Dirac-adjoint identities, spin-generator commutators, \(\gamma_5\) trace
  normalization, two-component \(\rho\)-block signs, Majorana conjugation,
  Wess-Bagger phase translation, low-dimensional Lorentzian traces, and
  Euclidean Clifford recursion.  It also checks the two-dimensional
  chiral-component convention
  \((\widehat\Gamma^+)_{++}=(\widehat\Gamma^-)_{--}=2i\) and its basis
  change to the two-dimensional Dirac-anomaly convention.
- `gauge_convention_checks.py`: \(SU(N)\) Hermitian-generator normalization
  \(\operatorname{tr}(t^a t^b)=\delta^{ab}\), output-first structure
  constants, \(C_A=2N\), \(T_F=1\), \(C_F=(N^2-1)/N\), the coupling-coordinate
  conversion from the common half-trace convention, and the Wilson-plaquette
  factor giving \((4g_0^2)^{-1}\int\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\).
- `gribov_zwanziger_checks.py`: exact finite checks for the Volume II
  Gribov--Zwanziger horizon-functional subsection, including spectral
  growth near a soft Faddeev--Popov eigenmode, the imaginary-source sign in
  the local Gaussian representation, the tree-level transverse propagator as
  the inverse of the horizon-modified kernel, and the complex \(p^2\)-plane
  pole locations.
- `gauge_phase_diagnostics_checks.py`: finite checks for the gauge-theory
  phases chapter, including electric, magnetic, and dyonic condensate
  orthogonality in \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\), the finite
  Dirac-pairing confinement criterion, tropical spectral extraction of static
  potentials, and exponent bookkeeping for Fredenhagen--Marcu type ratios.
- `hall_flux_curvature_checks.py`: finite checks for the many-body
  flux-torus Hall-response section, including the equality between projector
  curvature and the finite Kubo resolvent formula, plus the Chern-number
  normalization of the two-band lattice benchmark.
- `lattice_locality_flow_checks.py`: finite-regulator locality checks for the
  gauge-theory phases chapter, including overlap-chain counting for the
  path-count Lieb--Robinson estimate, the factorial-to-exponential tail bound,
  two-level spectral-flow transport, and the time-window split behind
  quasi-local generator tails.
- `toric_code_logical_operator_checks.py`: finite Pauli and chain-complex
  checks for the gauge-theory phases chapter, including star/plaquette
  commutation, global stabilizer redundancies, the four-dimensional torus
  ground space, logical line anticommutation, contractible stabilizer loops,
  and the constant local energy barrier of a simple logical string.
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
- `walker_wang_boundary_checks.py`: exact finite checks for the Walker--Wang
  boundary mechanism, including the pointed toric-code radical computation, a
  symmetric nonmodular \(\mathbb Z_2\) counterexample whose radical is all of
  the line group, cyclic nondegenerate pointed examples, boundary fusion
  associativity, and the non-pointed Ising modular-category M\"uger-center
  row-factorization test.
- `finite_higher_gauging_checks.py`: exact finite checks for the
  higher-gauging condensation-defect normalization, including the equality
  between the cochain groupoid factor
  \(|C^0|\,|Z^2|/|C^1|\) and the cohomological topological expression
  \(|H^0|\,|H^2|/|H^1|\), the fusion coefficient algebra
  \(\mathfrak C^2=Z^{(2)}\mathfrak C\), explicit boundary flux-sector counts
  \(\dim\mathcal H^{(2)}_N(\Sigma)=|H^2(\Sigma,\mathbb Z_N)|\), and the
  cell-dependence of the incomplete \(|C^1|^{-1}\) normalization.
- `haag_ruelle_fock_inner_product_checks.py`: exact rational checks for the
  Haag--Ruelle Fock inner-product recursion, comparing the recursive
  contraction formula with the direct bosonic permanent and particle-number
  orthogonality.
- `haag_ruelle_velocity_checks.py`: finite checks for the Volume I
  Haag--Ruelle velocity-support chapter material, including positive-energy
  phase cancellation, massive group-velocity subluminality,
  velocity-tube separation, and the nonstationary phase-gradient lower bound.
- `global_form_line_lattice_checks.py`: exact finite checks for the
  \(\mathfrak{su}(N)\) global-form and Wilson--'t Hooft line-lattice
  section, including the \(\mathbb Z_N^{\mathrm e}\oplus\mathbb Z_N^{\mathrm m}\)
  Dirac pairing, bilinearity and nondegeneracy, \(SU(N)/\mathbb Z_k\)
  Wilson-charge descent, magnetic cocharacter enlargement, and maximal
  isotropy of \(L_{N,k,p}=\langle(k,0),(p,N/k)\rangle\).  It also checks the
  finite \(\mathbb Z_N\) higher-form linking phase: deformation away from the
  charged operator, single crossing, orientation reversal, defect fusion, and
  charge fusion.
- `sw_su2_periods.py`: numerical and exact checks for the pure \(SU(2)\)
  Seiberg--Witten period section, including Picard--Lefschetz monodromy
  matrices, central-charge action and symplecticity, the rigid
  special-K\"ahler metric identity \(g=(2\pi)^{-1}\operatorname{Im}\tau\),
  the one-instanton \(R\)-anomaly zero-mode count, the residual
  \(R\)-symmetry action \(u\mapsto -u\), the two-singularity scale ledger, the
  single-nodal-monodromy exclusion, the minimal-curve discriminant, the
  Picard--Fuchs equation, the electric large-\(u\) asymptotic, logarithmic
  dual-period growth, linear monopole-period vanishing at \(u=\Lambda^2\),
  and rank-one Argyres-Douglas cusp scaling dimensions, discriminant
  collision, and mutual-nonlocality obstruction.
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
  the classical FDT relation, the finite bond-current contraction behind the
  macroscopic current cost, the Gaussian time-domain tail, nonanalytic loop
  coefficients, the \(d=2\) cutoff logarithm coefficient, the \(d=3\)
  cutoff/nonanalytic split, and positivity of the stress-noise tensor.
- `ising_defect_fusion_checks.py`: exact \(\mathbb Q(\sqrt2)\) checks for
  the Ising/Kramers--Wannier noninvertible defect example, including fusion
  associativity, Frobenius--Perron dimensions, modular \(S\)-matrix
  orthogonality, the Verlinde formula, and the diagonal action of defects on
  local primary sectors, plus finite regular-algebra separability/Frobenius
  identities and self-dual gauging fusion-ring associativity for cyclic
  groups and \(S_3\).
- `ising_form_factor_checks.py`: finite checks for the Volume VI
  free-Majorana and Ising form-factor examples, including Watson exchange,
  cyclicity, the Cauchy-kernel orientation behind the kinematic-pole residue
  sign, the two-particle invariant-mass identity, the energy-density spectral
  threshold factor, the Euclidean Bessel-kernel prefactor, the even spin-field
  semi-local cyclicity phase, the crossed \(\coth\) matrix element, the mixed
  bra/ket product formula, the semi-local kinematic-pole residue, and the
  even/odd spectral-series majorants used in the separated Euclidean
  reconstruction estimate.
- `finite_volume_form_factor_checks.py`: finite checks for the Volume VI
  finite-volume form-factor chapter, including the two-particle Gaudin
  determinant, cancellation of the Gaudin density between matrix elements and
  state counting, connected diagonal subset combinatorics, and the
  free-Majorana two-particle Bessel-reduction prefactor.
- `ising_metropolis_finite_checks.py`: exact enumeration checks for the
  `qft_scripts/ising2d_metropolis.py` companion script, verifying the local
  energy difference and detailed balance on the \(2\times2\) periodic Ising
  chain.
- `phi4_lattice_metropolis_checks.py`: finite algebra checks for the scalar
  two-dimensional \(\phi^4\) Metropolis companion script.  It verifies the
  local action difference against the total action, the symmetric-proposal
  pairwise detailed-balance identity, and the pointwise quartic stability
  bound used to define the finite measure.
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
- `su3_lattice_update_checks.py`: exact checks for the Volume XI
  \(SU(3)\) subgroup-update section, including embedded \(SU(2)\)
  unitarity and determinant one, the \(\mathfrak{su}(3)\) span from the
  three color-pair subgroups, subgroup commutator normalizations, local
  staple-score gauge covariance, and Metropolis pairwise balance.
- `su3_hdf5_sampler_checks.py`: finite checks for
  `qft_scripts/su3_gauge_4d_metropolis_hdf5.py`, verifying embedded subgroup
  proposals, local score changes, gauge invariance, the \(1\times1\)
  Wilson-loop/plaquette identity, and HDF5 measurement/checkpoint output.
  If the default Python lacks `h5py`, the check uses `QFT_HDF5_PYTHON` or the
  bundled Codex runtime Python when available.
- `su3_wilson_flow_checks.py`: finite checks for
  `qft_scripts/su3_wilson_flow_hdf5.py`, verifying the explicit \(SU(3)\)
  Wilson-score gradient by directional derivatives, one-step gauge
  covariance, small-step monotonicity, group preservation, HDF5 trajectory
  layout, and flow from a sampler checkpoint.  If the default Python lacks
  `h5py`, the check uses `QFT_HDF5_PYTHON` or the bundled Codex runtime
  Python when available.
- `su3_ape_smearing_checks.py`: finite checks for
  `qft_scripts/su3_ape_smearing_hdf5.py`, verifying the cold fixed point,
  spatial-mode preservation of temporal links, gauge covariance of the APE
  map, and HDF5 sampler-to-smearing plus smearing-to-smearing checkpoint
  layout.
- `su3_topological_charge_diagnostics_checks.py`: finite checks for
  `qft_scripts/su3_topological_charge_diagnostics_hdf5.py`, verifying
  oriented plaquette conventions, clover-field anti-Hermiticity and
  antisymmetry, vanishing on the cold configuration, gauge invariance of
  \(Q_{\rm clover}\) and the clover action density, and the
  sampler-to-flow-to-topology HDF5 pipeline.  If the default Python lacks
  `h5py`, the check uses `QFT_HDF5_PYTHON` or the bundled Codex runtime
  Python when available.
- `lattice_gradient_flow_checks.py`: exact finite checks for the Volume XI
  Wilson-flow section, including negative-gradient monotonicity, adjoint
  norm invariance, linearized heat-kernel damping, the \(w_0\) scale
  derivative, and the factor two in the Chern--Weil variation of
  \(\operatorname{tr}(F\wedge F)\).
- `gauge_action_improvement_checks.py`: exact arithmetic checks for the
  Volume XI tree-level improved gauge-action section, including rectangle
  flux moments, the equations \(c_0+8c_1=1\) and \(c_0+20c_1=0\), and the
  plaquette-plus-rectangle normalization convention.
- `link_smearing_checks.py`: finite matrix-algebra checks for the Volume XI
  gauge-covariant link-smearing section, including polar-projection
  equivariance, the \(\mathfrak{su}(N)\) projection used in stout smearing,
  and endpoint-conjugation covariance of the stout algebra element.
- `lattice_perturbation_tadpole_checks.py`: exact finite checks for the
  Volume XI lattice perturbative-coordinate section, including inversion of
  the tree-level gauge-fixed lattice kernel, the \(\widehat p^2\) expansion
  coefficient \(-1/12\), and the plaquette tadpole/boosted-coupling
  bookkeeping.
- `autocorrelation_resampling_checks.py`: finite checks for
  `qft_scripts/autocorrelation_resampling.py`, verifying block means,
  blocked standard errors, delete-one-block jackknife errors, biased
  autocovariances, and the windowed integrated autocorrelation coordinate.
- `static_potential_analysis_checks.py`: finite checks for
  `qft_scripts/static_potential_from_wilson_loops.py`, verifying that
  synthetic area-plus-perimeter Wilson-loop data reproduce the expected
  transfer-matrix effective masses and Creutz ratios, including elementary
  ratio-error propagation and sample-level correlated delete-one jackknife
  errors for nonlinear Wilson-loop ratios.  The check also exercises the HDF5
  bridge from the sampler convention
  `measurements/wilson_loops[sample,R-1,T-1]` to the correlated
  static-potential analysis.
- `nonabelian_lattice_observable_checks.py`: finite convention checks for
  the Volume XI nonabelian lattice-observable section, including the
  \(SU(N)\) fundamental plaquette strong-coupling slope, the single-state
  transfer-matrix ratio for static-energy extraction, and Creutz-ratio
  cancellation of area-plus-perimeter terms.
- `heatbath_overrelaxation_checks.py`: exact finite algebra checks for the
  Volume XI heat-bath and overrelaxation section, verifying conditional
  heat-bath detailed balance, \(SU(2)\) staple reduction, overrelaxation
  involution, local score preservation, and orthogonality of the
  overrelaxation map on \(S^3\), plus the corresponding local-staple and
  unit-link identities in `qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py`.
- `hmc_pseudofermion_checks.py`: exact finite algebra checks for the Volume
  XI HMC and pseudofermion section, verifying leapfrog determinant one,
  leapfrog reversibility, pairwise Metropolis balance, the diagonalized
  pseudofermion determinant identity, the rational-action spectral error
  bound used in the RHMC discussion, linear-solver action/force residual
  bounds, the RHMC determinant reweighting log bound, and the finite
  HMC/RHMC smoke-module regression.
- `z2_strong_coupling_surface_checks.py`: exact enumeration of small
  cubical plaquette chain complexes over \(\mathbb F_2\), verifying the
  one-cube Wilson-loop polynomial \((t+t^5)/(1+t^6)\), the first
  \(2\times1\) rectangular surface counts, and the finite entropy-bound
  arithmetic used in the strong-coupling area estimate.
- `kinetic_theory_checks.py`: finite algebra checks for the Volume X kinetic
  theory chapter, including Bose/Fermi detailed balance, the H-theorem
  integrand, the force-free quasiparticle drift projection from the
  Wigner-space mass-shell bracket, exact finite reversible-collision
  detailed balance, exact linearized rate and collision-invariant algebra,
  linearized collision-operator positivity and null vectors, and the
  relaxation-time shear-viscosity integral.
- `monte_carlo_sign_problem_checks.py`: exact finite checks for the Volume XI
  Monte Carlo and sign-problem chapter, including the finite-\(N\)
  autocorrelation variance identity, the reweighting identity, the
  average-phase relative-variance bound, and the distinction between
  \(\gamma_5\)-Hermiticity, determinant reality, and determinant positivity
  after flavor pairing.
- `large_n_topology_checks.py`: finite checks for the 't Hooft
  large-\(N\) section, including the \(SU(N)\) completeness relation in the
  monograph trace normalization, the planar-versus-one-handle theta-graph
  \(N^{-2}\) suppression, the half-trace coupling conversion
  \(g_{\rm ht}^2=2g^2\), normalized single-trace scaling, and fixed-\(N_f\)
  versus Veneziano quark-boundary counting, Eguchi--Kawai reduced-word
  center-charge selection, plus the displayed baryon Hartree pair-counting
  and fixed-spin rotor \(1/N_c\) scaling.
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
- `nested_integrability_checks.py`: exact and finite checks for the Volume VI
  nested-integrability chapters, including the \(SU(3)\) worked nested-root
  solution, Cartan-matrix nested Bethe equations, dressed-vacuum pole
  factorization, determinant QQ and Bäcklund restricted-Q-system algebra,
  the SoV single-zero shift factors from the RTT \(AB/DB\) components,
  Hirota-to-Y algebra, exact T-gauge covariance/Y-invariance, rank-one
  Baxter Casoratian transport for two finite-difference solutions, and the
  trigonometric rank-one q-oscillator local RLL identity in the chapter's
  six-vertex normalization.
- `planar_n4_integrability_checks.py`: finite checks for the Volume VII
  planar \(\mathcal N=4\) SYM integrability chapters, including cyclic
  one-loop Konishi Bethe roots, one-magnon XXX spectra, exact two-magnon BMN
  finite-chain quantization, central-extension magnon dispersion, its
  weak-coupling expansion, pentagon-OPE spectral resolution bookkeeping, and
  a local Hirota-to-Y-system algebra identity.
- `planar_n4_reader_companion_checks.py`: compact reader-facing checks for
  the planar \(\mathcal N=4\) integrability spine: the length-four Konishi
  spin-chain eigenvector, one-loop Bethe-Yang equations, local Y-system source
  algebra, and finite-grid mirror-TBA pseudoenergy identities.
- `susy_n4_scft_checks.py`: exact arithmetic checks for the Volume VII
  \(\mathcal N=4\) SYM SCFT foundation material, including one-loop and
  holomorphic beta-function cancellation, the one-complex-dimensional
  exact-marginal coupling chart, theta-periodicity and \(SL(2,\mathbb Z)\)
  generator arithmetic, \(a=c=\dim\mathfrak g/4\), the \(SO(6)\)
  symmetric-traceless projector, stress-tensor-multiplet two-point
  normalization, planar half-BPS chiral OPE coefficients, the finite-\(N\)
  Laguerre-polynomial circular Wilson-loop formula, the semicircle moments
  behind the planar circular Wilson-loop Bessel function, and the
  derivative/Bessel-ratio algebra for the planar Bremsstrahlung function.
  The weak and strong Bremsstrahlung expansions used in the cusp chapter are
  checked in `planar_n4_integrability_checks.py`.
- `planar_n4_integrability_checks.py` also verifies the BES strong-coupling
  normalization conversion used in Volume VII, including the shifted variable
  \(g_{\rm s}=g-3\log(2)/(4\pi)\) and the Catalan, \(\zeta(3)\), and
  \(\beta_{\rm D}(4)\) coefficients displayed there.
- The same planar integrability check verifies the one-cut finite-density
  spectral-curve bookkeeping behind the large-spin cusp resolvent:
  \(y^2=4z^2-1\), sheet exchange, branch endpoints, and the normalized
  one-cut cusp density.
- `lattice_reflection_positivity_checks.py`: finite character-expansion
  checks for the Osterwalder-Seiler lattice reflection-positivity proof,
  including \(U(1)\) Bessel/Fourier positivity, the \(SU(2)\) Wilson
  plaquette coefficient formula
  \(a_\ell=I_\ell-I_{\ell+2}=2(\ell+1)I_{\ell+1}/\beta\), and finite
  \(SU(2)\) tensor-product character multiplicities.
- `local_field_covariance_checks.py`: exact rational checks for the
  Volume I local-field chapter, including mostly-plus Lorentz interval
  preservation, the pullback composition order
  \((f_g)_h=f_{hg}\), Koszul signs for adjacent spacelike exchange, and the
  tensor-product ordering of component covariance factors in Wightman
  distributions.
- `poincare_algebra_sign_checks.py`: exact symbolic checks for the Volume I
  Poincare-algebra convention, including all Jacobi identities for the
  \(P^\mu,J^{\mu\nu}\) basis, the rotation tests
  \([J^{12},P^1]=\ii P^2\), \([J^{12},P^2]=-\ii P^1\), the boost test
  \([P^0,J^{01}]=\ii P^1\), the vector-representation Lorentz algebra and
  massless little-group commutators used in the helicity chapter, and the
  regression check that the opposite \([P,J]\) sign fails the issue-\#708
  Jacobi triple.
- `conformal_algebra_sign_checks.py`: exact symbolic checks for the Volume III
  conformal-algebra conventions against their underlying conformal Killing
  vector fields.  It verifies the Euclidean charge algebra, the Lorentzian
  mostly-plus analogue whose Poincare subalgebra contains the corrected
  \([P,J]\) sign, sign-sensitive Jacobi families involving \(D,P,K,J\), the
  displayed \(SO(D+1,1)\) change of basis, and the radial real-form map giving
  \([\widehat K_\mu,\widehat P_\nu]
  =2\delta_{\mu\nu}\widehat D_{\rm rad}-2\widehat J_{\nu\mu}\).
- `cross_section_partial_wave_checks.py`: exact rational checks for the
  Volume I cross-section chapter, including the Kallen momentum formula,
  invariant flux, two-body phase-space coefficient, identical \(\phi^4\)
  tree cross-section coefficient, the ordered \(16\pi\) partial-wave
  normalization, and the elastic/inelastic partial-wave unitarity circle.
- `lsz_residue_checks.py`: finite checks for the Volume I LSZ chapter,
  including mostly-plus invariant-denominator factorization, partial-fraction
  signs, per-leg amputation normalization, all-incoming momentum bookkeeping,
  and Lorentzian source-derivative phase compensation.
- `resonance_second_sheet_checks.py`: finite checks for the Volume II
  resonance chapter, including the two-particle threshold interval,
  self-energy and inverse-denominator sign conventions, adjacent-sheet
  logarithmic continuation, Breit--Wigner elastic unitarity, complex-energy
  pole conversion, the narrow-pole Newton step, and the physical-axis
  partial-wave bound.
- `maxwell_gauge_checks.py`: exact checks for the Volume I Maxwell chapter,
  including axial-gauge and covariant-gauge quadratic inverses, the
  finite-dimensional Faddeev--Popov slice Jacobian, Gupta--Bleuler null
  vectors, helicity-completeness \(C_\mu\)-term cancellation, and the
  cancellation of longitudinal representative terms from field-strength
  correlators.
- `massless_helicity_checks.py`: exact symbolic checks for the Volume I
  massless-particle chapter, including null-translation Lorentz matrices,
  polarization shifts under the little-group translation subgroup,
  auxiliary-vector polarization-projector transversality, spinor-helicity
  determinant conventions, and BCFW on-shell momentum conservation.
- `massive_spin_checks.py`: exact symbolic checks for the Volume I
  massive-particle spin chapter, including the mass-shell boost Jacobian,
  Wigner cocycle, spin-frame conjugation and inner-product invariance,
  \(SU(2)\) central signs, and the mostly-plus Dirac projector and spin-sum
  formulas.
- `spinor_grassmann_checks.py`: finite exact checks for the Volume I
  spinor-field and Grassmann path-integral chapter, including the phase signs
  in the free Dirac equations, the charge ledger for \(b,d\) oscillators, the
  CAR locality sign, the odd Dirac bracket, the purely odd Berezinian
  determinant, one-pair Berezin Gaussian normalization, and coherent-state
  trace and supertrace endpoint signs.
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
  \(1/L^3\), the first \(D=4\) open-oscillator degeneracies, the associated
  \(D_{\infty h}\) channel decomposition through oscillator level \(4\)
  including the first \(\Sigma_g^-\) entry, the trace-delta
  antisymmetric-Casimir \(k\)-string ratio, the sine-law comparison algebra
  and displayed low-rank values, the excited-level expansion coefficients
  with closed-string level matching, and the displayed baryonic \(Y\)-string
  Steiner lengths in the equilateral and \(120^\circ\)-threshold cases,
  together with the open/closed equality of the worldsheet Hagedorn
  coefficient.
- `qcd_glueball_spectrum_checks.py`: exact finite checks for the pure
  Yang--Mills glueball-spectrum extraction section, including the exact
  generalized-eigenvalue problem in a finite two-state subspace, large-\(N\)
  glueball width power counting, and the cubic-group dimension split of a
  continuum \(J=2\) channel.
- `qcd_spectroscopy_regge_checks.py`: exact algebra checks for the QCD
  hadron-spectroscopy and Regge sections, including the octet
  Gell-Mann--Okubo relation, decuplet equal spacing, pseudoscalar-baryon
  partial-wave \(J^P\) assignments, Veneziano-residue polynomial degrees and
  coefficients, the rational coefficient in the classical open-flux-tube
  Regge slope, triple-Regge exponent bookkeeping, eikonal Poisson
  normalization, free-Reggeon trajectory signs, the eikonal AGK factorial
  moment cancellation, the two-Reggeon cut intercept/slope bookkeeping and
  \(n\)-Reggeon free-cut slope law, the \(S\)-wave Luescher zeta normalization,
  unequal-mass
  Roy--Steiner kinematics and partial-wave normalization, GEVP basis
  covariance for finite-volume spectral extraction, shallow-bound-state
  effective-range pole and residue algebra, the \(\pi\pi\)
  isospin-crossing matrices and Roy-subtraction polynomial slope ratios, and
  the one-channel Luescher/K-matrix sign
  convention that maps finite-volume energies to a second-sheet pole
  equation, together with the coupled-channel determinant reduction,
  sheet-sign bookkeeping, two-channel sheet/residue adjugate algebra,
  two-state glueball/hybrid avoided-crossing algebra, the quarkonium
  \(J^{PC}\) chart, and the quarkonium
  spin-centroid algebra for fine and hyperfine splittings, the Coulombic
  \(1S\) pNRQCD energy and
  wavefunction-at-origin normalization, the leading \(1S\) hyperfine contact
  splitting, and the linear elastic-pole
  mass-width coordinate, plus the nucleon Sachs Dirac--Pauli coordinate
  transform, the stable-current three-point extraction ratio with
  excited-state suppression factors, the forward Compton/Baldin dispersion
  prefactor, and the GDH and forward spin-polarizability prefactors in the
  \(\Delta\sigma=\sigma_{1/2}-\sigma_{3/2}\) convention, together with the
  heavy-baryon spin-average cancellation of the chromomagnetic coordinate and
  the exact two-flavor contracted-\(SU(4)\) spin-flavor commutator scaling.
- `sigma_model_family_checks.py`: exact finite checks for the integrable
  sigma-model family chapter, including the \(\CP^{N-1}\) projector geometry
  and topological-charge normalization on the \(\CP^1\) chart, the
  \(\CP^1=O(3)\) Pauli-matrix kinetic and degree-normalization identities,
  the algebraic equivalence between the principal-chiral-model and
  symmetric-space Lax flatness polynomials and their
  equation-of-motion/Maurer--Cartan systems, the Polyakov--Wiegmann boundary
  coefficient in the chapter's WZ normalization, sample WZW central charges,
  endpoint primary-weight formulae, diagonal \(SU(2)\) coset central charges,
  nonabelian-bosonization central-charge bookkeeping, the projective-model
  crossing tensors and \(V\otimes V^\vee\) singlet/adjoint projectors, the
  large-\(N\) projective induced-gauge polarization moments, Maxwell
  coefficient, and linear-potential coefficient, the \(SU(N)\)
  sine-mass/fusion-angle and rational-matrix bootstrap identities,
  the \(A_{N-1}\) inverse-Cartan formula, nested root-count integrality, and
  left/right principal-chiral doubling ledgers, the elementary CDD-block
  identities, the \(SU(N)\) Gross--Neveu and principal-chiral gamma-function
  scalar unitarity identities, the supersphere, projective-supermodel, and
  orthosymplectic one-loop cancellations,
  the repulsive sausage charged scattering identities, the full triplet
  matrix unitarity and formal \(q,u,v\) Yang--Baxter component proof, the rational
  \(O(3)\) limit, and the sausage-metric scalar-curvature, Ricci-flow
  closure, integrated Ricci trajectories, and cylinder endpoint formulae.
- `susy_yang_mills_family_checks.py`: exact finite checks for the
  supersymmetric Yang--Mills family discussion, including the pure-SYM
  root-of-unity domain-wall sine formula, the one-coordinate chiral
  mass-normalization algebra, the local Seiberg--Witten monopole-condensate
  \(F\)-term equation, and the Abelian vortex square completion.
- `susy_yang_mills_deformation_ladder_checks.py`: exact finite checks for
  the supersymmetric Yang--Mills deformation-ladder chapter, including
  holomorphic scale-dimension matching, the \(\mathcal N=1^\ast\)
  fuzzy-sphere \(F\)-term ansatz, and the sine-law/Casimir \(k\)-string
  ledger identities, the local Seiberg--Witten vortex-profile flux and
  small-radius normalization, the Abelianized \(A_{N-1}\) sine-vector
  eigenvalue and subadditivity algebra, together with pure
  \(\mathcal N=1\) SYM channel-pole and supersymmetry-restoration diagnostic
  bookkeeping.
- `lee_yang_tba_checks.py`: finite checks for the Volume VI scaling
  Lee--Yang thermodynamic Bethe ansatz example, including scalar-amplitude
  unitarity and crossing, the sign and total integral of the TBA kernel, the
  golden-ratio plateau equation, and the Rogers-dilogarithm value
  \(L(\phi^{-2})=\pi^2/15\) giving \(c_{\rm eff}=2/5\).
- `generalized_hydrodynamics_checks.py`: finite algebra checks for the
  Volume VI generalized-hydrodynamics bridge, including the finite-grid
  dressing equation, the equality of \(\sum h\rho v^{\rm eff}\) with the
  dressed-energy current expression, and the exact hard-rod
  effective-velocity solution.
- `weak_breaking_collision_cell_checks.py`: finite collision-cell checks for
  the Volume VI weak-integrability-breaking kinetic layer, including
  detailed balance, exact conservation of projected energy, nonconservation
  of a higher Bethe-type charge under allowed transitions, and the
  symmetrized relative-entropy production identity.
- `factorized_scattering_algebra_checks.py`: exact checks for the Volume VI
  factorized-scattering opening chapter, including mostly-plus rapidity
  kinematics, Newton separation of rapidity multisets, chamber braid
  relations, the rational Yang--Baxter identity, scalar two-body unitarity,
  and Watson-exchange coefficient bookkeeping.
- `yang_baxter_internal_symmetry_checks.py`: exact checks for the Volume VI
  Yang--Baxter/internal-symmetry chapter, including the additive
  fixed-tensor-product rational Yang--Baxter identity, the spectral classical
  Yang--Baxter commutator identity for \(r(u)=P/u\), and the
  \(O(N)\) vector-channel projector algebra into singlet, antisymmetric, and
  traceless-symmetric components.
- `integrable_scattering_bootstrap_checks.py`: finite analytic checks for the
  Volume VI rapidity-plane bootstrap chapter, including the elementary scalar
  block unitarity identity, the crossing relation
  \([x]_{\ii\pi-\theta}=-[1-x]_\theta\), the crossing-symmetric CDD-pair
  unitarity/crossing identities, and the opposite signs of the two
  physical-strip residues in the CDD pair.  It also checks the complex
  fusing-angle momentum identity behind the bound-state mass relation.
- `integrable_rg_flow_checks.py`: exact arithmetic checks for the Volume VI
  perturbed-CFT and integrable-RG-flow chapter, including the
  \(\phi_{1,3}\) Kac weight, relevance exponent, unitary minimal-model
  central-charge drops, the polynomial scalar Landau--Ginzburg
  multicritical ledger \(K=2m-2\), equation-of-motion descendant power
  \(2m-3\), order-field quotient count \(2m-3\), even tuning-ratio count
  \(m-2\), Kac-table identification, source-scaling sign, and
  right/left massless dispersion identities, plus the
  Zamolodchikov trace-sum-rule coefficient \(9/E^4\) and the
  \(\phi_{1,3}\) minimal-flow central-charge targets.
- `mirror_tba_wrapping_checks.py`: exact algebra checks for the Volume VI
  mirror-channel finite-size chapter, including the two-winding TBA expansion
  of \(L_a=\log(1+e^{-\epsilon_a})\), the displayed vacuum-energy
  coefficients, the vacuum Luescher \(K_1\) normalization and exponential
  remainder threshold, the \(K_1\) large-\(r\) asymptotic coefficients,
  F-term product subtraction, and the orientation sign in the \(\mu\)-term
  residue ledger.
- `nonintegrable_bridge_checks.py`: exact arithmetic checks for the Volume VI
  bridge from integrable to nonintegrable two-dimensional QFT, including the
  broken-charge commutator ledger, first-order form-factor mass shift,
  semi-local kinematic residue, Ising false-vacuum string tension,
  two-body phase-space Jacobian for \(1+1\)-dimensional decay widths,
  TCSA coupling and counterterm powers, and the Airy scaling of confined
  kink--antikink bound states.
- `numerical_extrapolation_checks.py`: exact rational and finite-matrix
  checks for the Volume XI finite-regulator extrapolation section, including
  Lagrange interpolation nonuniqueness of finite cutoff data, two-cutoff
  Richardson cancellation, integer-power extrapolation weights with explicit
  remainder bounds, and correlated least-squares covariance/error
  propagation for windowed continuum diagnostics.  It also imports the
  reader-facing `qft_scripts/finite_regulator_extrapolation.py` smoke datum
  and verifies its public intercept, covariance, systematic-coordinate, and
  window bookkeeping against the displayed linear algebra.
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
  entropy production, finite local-detailed-balance entropy splitting,
  the finite jump path-measure Radon--Nikodym ratio, a driven two-state
  Jarzynski identity, finite-step MSRJD Gaussian/Fourier normalization,
  Langevin generator expansion, finite Model A/B mobility-gradient
  data including graph-incidence mobility, conserved total drift, no
  constant noise mode, and zero Gibbs current, finite coupled slow-variable
  data including antisymmetric reversible Gibbs-current preservation and a
  Model C-style conserved-density mobility block, finite Doi--Peliti generator matrix
  identities, the Doi--Peliti symbol and exponential-test large-deviation
  Hamiltonian, the finite Feynman--Kac tilted generator for jump additives,
  the stationary finite-ring Gallavotti--Cohen similarity identity, the
  empirical-flow level-\(2.5\) cost and two-state level-\(2\) contraction,
  GKSL trace preservation, KMS detailed balance for a two-level system,
  Ornstein-Uhlenbeck noise normalization, positivity of a quadratic noise
  kernel, and the finite Schwinger--Keldysh Gaussian noise bridge from the
  Hubbard--Stratonovich characteristic function to
  \(K^{-1}NK^{-T}\) response covariance.
- `microlocal_spectrum_checks.py`: finite convention checks for the
  microlocal spectrum chapter, including the mostly-plus future-covector
  convention, the Klein-Gordon Hamilton-flow sign, the two-point graph
  covector pattern \((p,-p)\), the opposite-cone product obstruction, and
  the diagonal coefficients in the four-dimensional Hadamard recursion.
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
  stress-tensor examples, including the flat Synge identities and leading
  Hadamard \(U\)-transport equation, the first logarithmic \(v_0\) transport
  equation and coincidence value, the flat massive logarithmic Hadamard
  recursion through \(v_3\), state-difference cancellation of the common
  Hadamard singularity, the sign of smooth and scale subtraction changes,
  Wald finite-freedom engineering dimensions, the \(R^2\) and
  \(R_{\mu\nu}R^{\mu\nu}\) Euler-tensor trace coefficients, the
  Bose integral \(\int_0^\infty x^3(e^x-1)^{-1}dx=\pi^4/15\), the flat
  thermal scalar energy density and traceless equation of state, the massless
  plane-wave eigenvalues of the displayed bidifferential operators, and the
  de Sitter constant-curvature anomaly specialization for a conformal real
  scalar.
- `schwinger_model_checks.py`: finite sign and normalization checks for the
  Schwinger-model chapter, including the two-dimensional current-duality
  convention, the algebraic elimination of the electric field, the
  anomaly-induced mass \(m_{\rm Sch}^2=e^2/\pi\), the screened static
  potential and its dimensionless figure curve, and the periodicity of the
  massive-model string tension for integer probe charge.
- `semiclassical_backreaction_checks.py`: finite checks for the semiclassical
  backreaction chapter, including four-dimensional traces of the
  curvature-squared Euler tensors, the KMS fluctuation-dissipation factor,
  positivity of a finite noise covariance, the Einstein--Langevin
  pushforward covariance identity \(GNG^T\), and the low-energy root
  selected by reduction of order in a toy higher-derivative equation.
- `schwinger_keldysh_operator_checks.py`: finite two-level-system checks for
  the real-time Schwinger--Keldysh operator chapter, including diagonal
  unitarity, branch-exchange reality, the \(|Z|\le1\) positivity bound,
  the \(H-J^\alpha O_\alpha\) source-response sign from an impulsive physical
  source, the \(G^{aa}=0\) two-point cancellation and retarded support in the
  contour-to-\(r/a\) algebra, and KMS detailed balance.
- `sk_diffusion_action_checks.py`: finite algebra checks for the Volume X
  Schwinger--Keldysh hydrodynamic diffusion action, including the sourced
  density saddle, one-charge and non-diagonal two-charge diffusive response
  kernels, positivity and \(\chi^{-1}\)-self-adjointness of the multi-charge
  diffusion endomorphism, transverse Ohm response, scalar and matrix KMS
  noise coefficients, Hubbard--Stratonovich noise normalization, and the
  full noncommuting matrix density fluctuation--dissipation identity.
- `sine_gordon_smatrix_checks.py`: numerical finite checks for the Volume VI
  sine-Gordon exact scattering datum, including soliton-matrix unitarity and
  Yang-Baxter, the free-fermion point, breather pole locations, breather mass
  kinematics, soliton-breather unitarity/crossing/pole kinematics, and
  lightest-breather unitarity and crossing.  It also checks the
  \(A_r^{(1)}\) affine Toda cycle-Laplacian eigenvalues and the finite
  \(A_r\) Perron--Frobenius sine-mass relation.
- `sg_thirring_bosonization_checks.py`: exact rational checks for the
  sine-Gordon/massive-Thirring bosonization section, including the distinction
  between vertex-OPE exponent and scaling dimension, Coleman's coupling map,
  the current-dictionary coefficient, the Mandelstam exchange phase, the
  free-fermion point, and the sine-Gordon relevance threshold.
- `ks_allowability_checks.py`: finite complex-linear-algebra checks for the
  Kontsevich--Segal allowability chapter, including the angle criterion,
  Euclidean and Lorentzian boundary examples, two-time exclusion, and
  positivity of all diagonal \(q\)-form coefficients.
- `ks_semigroup_checks.py`: finite checks for the K-S positive-energy
  mechanism, including Mehler-kernel composition for a harmonic oscillator
  mode and the contraction-to-unitary boundary-value behavior of
  \(e^{-zH}\) for a positive spectrum.
- `susy_abjm_6d_checks.py`: exact finite checks for the ABJM and
  six-dimensional supersymmetric field-theory chapters, including the ABJM
  superpotential \(R\)-charge, opposite-level parity bookkeeping, abelian
  BF normalization, standard ABJM conformal-locus tangent count,
  \(\mathbb Z_k\) orbifold order, \(S^3\) matrix-model denominator powers,
  free-chiral \(S^3\) determinant normalization, rank-one ABJM sphere-integral
  factors, ABJM Fermi-gas first trace, leading Weyl coefficient, and Airy
  inverse-Laplace rescaling,
  non-abelian `3D` \(\mathcal N=2\) Chern--Simons-matter auxiliary
  elimination coefficients, `3D` \(\mathcal N=3\) adjoint-chiral
  elimination coefficients,
  six-dimensional Yang-Mills coupling dimension, chiral two-form physical
  degree-of-freedom count, \(A_{N-1}\), \(D_N\), and exceptional \((2,0)\)
  anomaly/tensor-branch arithmetic, the quadratic Green--Schwarz descent
  factor, the trace-delta \(g_5^2=4\pi^2R\) compactification normalization,
  the wrapped-string/W-boson scalar normalization, ADE defect-group orders
  from Cartan determinants, cyclic finite-flux polarization checks, the
  \(S^1\times X_5\) finite-flux decomposition and electric/magnetic
  polarization signs, the finite commutant criterion for genuine versus
  relative defects in an absolute polarization, symplectic-graph interface
  relations, and ADE class-\(S\) Hitchin-base degree sums.
- `susy_gauge_foundation_checks.py`: exact finite checks for the Volume VII
  supersymmetric gauge-theory foundation chapter, including the auxiliary
  \(D\)-field square completion and potential sign, the absence of
  Fayet--Iliopoulos parameters for an `su(2)` semisimple factor, vectorlike
  \(U(1)\) anomaly cancellation, and the conjugate-representation anomaly
  sign, the Hermitian-sign identity converting Wess--Zumino-gauge closure
  between ordinary-translation and covariant-translation forms, and the
  \(\mathcal N=2\) QCD cubic gauge contraction together with its
  \(2g_{\rm YM}^2\) \(F\)-term coefficient.
- `susy_moduli_space_checks.py`: finite algebra checks for the Volume VII
  supersymmetric moduli-space quotient conventions, including the
  rank-one \(U(1)\) invariant ring
  \(\mathbb C[x,y]^{\mathbb C^\ast}=\mathbb C[xy]\), the matching
  real/complex quotient dimension count, the equivariance of an invariant
  superpotential's \(F\)-term ideal, and the rank-one hyperk\"ahler quotient
  dimension and cotangent-transition algebra for \(T^\ast\mathbb P^{N-1}\),
  plus the \(SU(2)\), \(N_f=2\) Plucker/Pfaffian quotient identity and
  dimension ledger, nonzero quantum-deformation smoothness test,
  diagonal-mass two-vacuum algebra, and holomorphic threshold scale matching.
- `susy_2d_lg_glsm_checks.py`: exact finite checks for the
  two-dimensional \(\mathcal N=(2,2)\) Landau--Ginzburg and GLSM chapter,
  including \(A\)-series quasihomogeneous charges and central charges,
  Fermat Jacobi-basis dimensions, quintic Landau--Ginzburg central charge,
  hypersurface GLSM gauge-invariance arithmetic, axial-anomaly charge sums,
  positive-chamber hypersurface dimensions, and negative-chamber residual
  finite-gauge-group orders, together with the A/B twist spin-shift ledger
  that identifies the scalar supercharges and the abelian circle-duality
  momentum-winding/Legendre-Hessian inversion checks, plus the abelian GLSM
  Coulomb one-loop charge-exponent/vacuum-count ledger, the primitive of the
  Coulomb logarithmic derivative and its finite FI-coordinate shift under
  determinant normalization changes, the charged-chiral mirror-variable
  elimination matching the Coulomb one-loop superpotential, the finite
  FI-coordinate shift induced by vortex coefficient normalizations, the
  primitive-monomial selection forced by exact Coulomb matching, the
  \(\mathbb P^{N-1}\) mirror critical-point simplicity ledger, and the
  classical cigar quotient metric obtained by eliminating the gauge field,
  the logarithmic-chiral vortex obstruction, plus the hypersurface GLSM
  adjunction sign,
  Landau--Ginzburg/sigma-model central-charge matching condition, residual
  finite-gauge invariant Jacobi monomial count, and Coulomb-coordinate
  singular-signal ledger.  It also checks the Fermat Wilsonian
  superpotential spurion-selection arithmetic: regular holomorphic monomials
  with the declared flavor and \(R\)-charges are exactly the original
  \(g_i(\Phi^i)^{d_i}\) terms.
- `susy_holomorphy_nsvz_checks.py`: exact rational checks for Volume VII
  holomorphy and NSVZ coordinate algebra, including quadratic chiral
  tree-level elimination, the eliminated derivative identity, the
  loop-supergraph Grassmann-measure ledger behind the Wilsonian
  superpotential argument, the holomorphic gauge-coupling \(q^0\)
  perturbative projection, the separate one-loop shell determinant
  coefficient \(3C_2(G)-\sum_iT(R_i)\), Konishi and vector-multiplet
  coordinate shifts, and the differentiated holomorphic-canonical relation
  leading to the NSVZ beta function.
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
  conformal-window/free-phase inequalities.  These finite checks verify the
  displayed algebraic consistency conditions; they do not constitute a proof of
  Seiberg duality or of the existence of the infrared fixed points.
- `susy_instanton_nekr_checks.py`: exact rational checks for the
  supersymmetric instanton expansion, including the ADHM dimension count,
  Uhlenbeck stratum codimension arithmetic, the positive-ADHM-moment-map
  trace obstruction to unstable small-instanton subspaces, the one-box
  Gieseker tangent Euler-class specialization, the charge-one
  Gieseker-to-Uhlenbeck minimal-nilpotent-cone resolution arithmetic,
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
  Gaussian coefficient, the \(S^4\) \(\mathcal N=4\) adjoint-hyper
  root-pair cancellation of \(H\)-factors, the finite normal Gaussian
  Pfaffian/determinant convention, the \(S^4\) \(H\)-function
  finite-product logarithmic derivative, the finite-part mode-determinant
  ledger behind the \(H\)-powers, the \(U(1)\) \(S^4\) Gaussian matrix
  integral, finite double-sine reflection and pole-convention checks, the
  \(U(1)_k\) \(S^3\) Chern--Simons Fresnel completion of the square, and the
  round-\(S^3\) conjugate-chiral-pair integral
  \(\int d\sigma/(2\cosh\pi\sigma)=1/2\).
- `soft_drop_irc_checks.py`: exact rational checks for the soft-drop
  IRC-classification section, including the \(\beta_{\rm SD}=0\) collinear
  counterexample for the groomed four-vector and the \(\beta_{\rm SD}>0\)
  threshold behavior, finite Cambridge--Aachen tree decision-margin
  bookkeeping for stability away from grooming-boundary hypersurfaces, and
  the measured-function distinction between positive-angular-power groomed
  shapes and the retained-energy fraction in the mMDT one-prong collinear
  limit; it also checks the fixed-coupling soft-drop groomed-mass radiator
  area, including the mMDT single-log limit and continuity at the grooming
  transition, and the stopping-time normalization for the leading mMDT
  \(z_g\) distribution together with the \(\beta_{\rm SD}>0\)
  angular-domain condition for values below \(z_{\rm cut}\).
- `shape_function_convolution_checks.py`: exact rational checks for the
  jet shape-function section, including finite spectral pairing of the soft
  measurement coordinate, normalization of the endpoint convolution, the
  first-moment shift by \(\Omega_1/Q\), and paired translation covariance
  under finite subtraction-scheme changes.
- `n_subjettiness_continuity_checks.py`: exact rational checks for the
  minimized-\(N\)-subjettiness continuity section, using the \(N=1\),
  \(\beta_\tau=2\) weighted-variance model to verify the soft-addition bound,
  the collinear recombination variance identity, and independence of the
  minimized value from a discrete axis-label choice.
- `scet_factorization_checks.py`: finite checks for the SCET factorization
  datum in the jets chapter, including exact endpoint-convolution
  normalization and first-moment identities, the total-variation bound for a
  finite distributional factorization remainder, finite zero-bin
  inclusion--exclusion and scheme-reshuffling identities, finite
  multiplicative hard/jet/soft scheme covariance and anomalous-dimension
  consistency, scalar renormalization-group transport independence under the
  hard/jet/soft anomalous-dimension consistency equation, exact soft-drop
  boundary scale identities and hard/global-soft/jet/collinear-soft RG
  consistency, a finite Wilson-line algebra check of leading soft
  covariant-derivative decoupling, a finite Glauber unitarity diagnostic
  separating inclusive cancellation from noncommuting measurement obstruction
  together with an exact finite remainder identity and Hilbert--Schmidt bound,
  and the triangular logarithmic phase-space area behind the massive-vector
  Sudakov chart.
- `track_function_moment_checks.py`: exact rational checks for the finite-kernel
  track-function RG identities, verifying preservation of normalization, the
  first-moment evolution formula, and the full finite moment-tower formula
  for discrete track measures.
- `track_observable_lift_checks.py`: exact rational checks for the finite
  track-observable lift, verifying diagonal two-point terms with second track
  moments, enumeration of the lifted two-particle energy polynomial, the
  general \(k\)-point lift through a nontrivial three-point kernel with third
  track moments, failure of naive first-moment replacement, and the first- and
  second-moment collinear composition identities.
- `susy_qm_index_checks.py`: exact rational checks for the Volume I
  SUSY-QM and worldline index-density section, including the oscillator
  supertrace identity, zero-mode index count, two-variable Berezin Pfaffian
  extraction, and the \(\widehat A\)-series coefficients through degree six.
- `susy_representation_checks.py`: exact finite checks for the Volume VII
  supersymmetry representation chapter, including massive \(\mathcal N=1\)
  Fock-space dimensions, boson/fermion balance, the Clebsch--Gordan
  dimension identity for the one-oscillator spin sector, the rank-one massless
  supercharge norm matrix, and BPS-bound block eigenvalues
  \(2(m\pm z)\).  The same check also covers the HLS central-charge
  combined-index symmetry, the \(T Z+Z T^T=0\) internal-invariance condition,
  and the Lorentz-representation dimension ledger used in the HLS normal
  form.
- `susy_superspace_component_checks.py`: finite Grassmann-algebra checks for
  the Volume VII superspace/local-actions conventions, including
  \(\theta^2=2\theta^1\theta^2\), the left-derivative rule for \(\theta^2\),
  the \((\theta\psi)(\theta\chi)\) identity, the
  \(-\frac12 W_{ij}\psi^i\psi^j\) chiral \(F\)-term coefficient, and
  auxiliary \(F\)-field elimination.
- `susy_superfield_operator_algebra_checks.py`: exact formal-superfield
  checks for the Volume VII superspace differential-operator conventions,
  including the Koszul sign in left odd differentiation, the chiral and
  antichiral coordinate identities \(\bar D_{\dot\alpha}y^\mu=0\) and
  \(D_\alpha\bar y^\mu=0\), the full \(Q,\bar Q,D,\bar D\) anticommutation
  algebra on a generic finite superfield, and the anticommutation of
  supercharges with covariant derivatives.
- `susy_vector_superfield_checks.py`: exact finite exterior-algebra and
  sigma-matrix checks for the Volume VII vector-superfield conventions,
  including inverse epsilon raising, the bosonic \(\theta^2\) coefficient of
  \(W^\alpha W_\alpha\), and recovery of
  \(-F_{\mu\nu}F^{\mu\nu}/(4g^2)+D^2/(2g^2)\) after adding the Hermitian
  conjugate.
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
- `n4_symmetric_product_marginal_checks.py`: exact rational checks for the
  \(\mathcal N=(4,4)\) symmetric-product two-cycle marginal-tangent
  construction, including the \(c=6\) length-two twist weight \(3/8\), the
  spin-field dressing to \(h=1/2\), the supercharge top-component weight
  \(h=1\), normalized transposition class sums, and the local dimension
  counts \(16+4=20\) and \(80+4=84\).
- `thermal_kubo_checks.py`: finite checks for the Volume X Kubo and
  spectral-function conventions, including detailed balance and
  fluctuation--dissipation in a two-level system, the sign
  \(\rho=-2\operatorname{Im}G^R\), the shear-viscosity spectral slope, and
  the vector-potential response sign, plus the fact that real local contact
  terms do not change dissipative spectral slopes, the finite Mazur
  projection/Drude-weight relation for a current with conserved overlap, and
  the regular-versus-Drude decomposition used in the Kubo figure, together
  with a finite-dimensional Mori--Zwanzig projection identity and its
  Laplace-space Schur-complement form.
- `thermal_screening_checks.py`: finite checks for the Volume X thermal
  gauge-screening chapter, including the \(d\)-dimensional Yukawa asymptotic
  power, the transverse-projected pole residue, and the conversion of the
  one-loop Debye coefficient between half-trace and trace-delta generator
  normalizations.
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
  identity, the \(SU(2)\) four-fundamental KZ invariant-tensor relation,
  \(\Omega_{12}\) and \(\Omega_{23}\) residue matrices, and
  singlet/triplet residue eigenvalues, \(SU(2)_k/U(1)\) parafermion
  selection and field-identification weights, compact parafermion orbit
  counts, fusion rules, modular
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
- `cft_correlator_kinematics_checks.py`: symbolic checks for CFT
  correlator kinematics, including scalar three-point weights, four-point
  prefactor inversion weights, the generic four-point conformal-frame
  quotient dimension, and the \(u=z\bar z\), \(v=(1-z)(1-\bar z)\)
  cross-ratio frame.
- `cluster_sweep_grid_checks.py`: independent checks for the cluster
  SU(3) sweep-grid resolver in `qft_scripts/cluster/`, including Cartesian
  task ordering, out-of-range rejection, and environment-variable CLI output
  for SLURM-style job arrays.
- `renormalizability_counterterm_checks.py`: finite checks for the
  renormalizability and counterterm discussion, including the one-loop
  \(\phi^3_6\) pole coefficients, the finite-list power-counting logic for
  interactions of dimension at most \(D\), proliferation from repeated
  irrelevant insertions, and scaling-degree ambiguity bounds for supported
  distributions.
- `tomita_standard_form_checks.py`: finite matrix checks for the
  Tomita--Takesaki and Connes-standard-form conventions, including the
  Tomita polar data on matrix units, commutant and modular-automorphism
  identities, Connes cocycle composition, and positive-cone diagnostics.
- `gamma_trace_checks.wl`: a Wolfram Language version of the same finite
  algebraic checks, adapted from the source spinor appendix and
  `gamma matrices.nb` conventions without relying on `.nb` structure.
- `planar_n4_reader_companion_checks.wl`: a plain Wolfram Language companion
  to `planar_n4_reader_companion_checks.py`, keeping the same spin-chain,
  Bethe-Yang, Y-system, and mirror-TBA checks close to Mathematica-style
  symbolic manipulation.

Run all available checks from the repository root with:

```bash
tools/run_calculation_checks.sh
```

List the exact active inventory without running it with:

```bash
tools/run_calculation_checks.sh --list
```

For ordinary editing passes, run the relevant checks by pattern rather than
the full suite, for example:

```bash
tools/run_calculation_checks.sh --only qcd_dglap --skip-wolfram
```

The full runner is an explicit batch tool.  It is intentionally not invoked by
`tools/build_monograph.sh`: the default build verifies manuscript structure
and TeX consistency, while calculation checks are rerun when the formulae,
normalizations, or conventions they verify have been touched.

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
