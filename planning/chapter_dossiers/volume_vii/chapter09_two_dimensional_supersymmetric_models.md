# Chapter 09: Two-Dimensional Supersymmetric Models
Source-File: monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex

## Source Position

Volume VII now leaves the four-dimensional gauge-dynamics core and begins the
lower-dimensional supersymmetric examples with `2D` `N=(2,2)` theories.
The LG/GLSM and mirror-duality material uses Xi's stringbook Appendix K as an
internal source lead and convention comparator.  It is rewritten here as an
intrinsic two-dimensional QFT development, with the charged-chiral
dualization, one-loop matching, vortex-term proof boundary, protected
projective-space residue test, and cigar/Liouville comparison made more
explicit than the stringbook appendix.
Hori--Vafa is treated as a protected-data benchmark and source lead rather
than as an authority to quote through; every imported formula must be
rechecked against the chapter's regulator, determinant, zero-mode, boundary,
and normalization conventions.
The full abelian GLSM/Hori--Vafa mirror claim and the cigar/Liouville claim
are now named as central QFT conjectures in the chapter, with protected
calculations recorded as evidence or conditional consequences rather than as
the full equivalences themselves.
Primary reference sidecars currently used for scrutiny, not authority, are
`references/susy_glsm_mirror/hori_vafa_mirror_symmetry_hep-th_0002222.txt`
and
`references/susy_glsm_mirror/hori_kapustin_cigar_liouville_hep-th_0104202.txt`.

## Notation Inventory

- `Q_pm`, `bar Q_pm`, `P_pm`: two-dimensional supersymmetry generators and
  light-cone momenta.
- `F_V`, `F_A`: vector and axial `R` charges.
- `s`, `s_A`, `s_B`: untwisted, A-twisted, and B-twisted Lorentz spins.
- `Q_A`, `Q_B`: scalar supercharges after the A and B twists.
- `Phi^i=(phi^i, psi^i_+, psi^i_-, F^i)`, `K`, `g_i bar j`, `W`:
  Landau-Ginzburg chiral multiplet variables, Kahler potential, metric, and
  superpotential.
- `q_i`: quasihomogeneous Landau-Ginzburg weights.
- `g_i`: background chiral Wilsonian couplings for Fermat
  Landau-Ginzburg monomials `g_i (Phi^i)^{d_i}`.
- `Jac(W)`: Landau-Ginzburg Jacobian ring.
- `chi_y`: finite protected Ramond charge polynomial coordinated with the
  Volume V elliptic-genus interface.
- `eta_i`: B-type odd local variables used in the cohomological derivation
  of the Jacobian quotient.
- `H_W`, `Res_W`: Landau-Ginzburg Hessian determinant and Morse residue
  functional.
- `X`, `g_i bar j`, `B`, `omega`, `chi^a`: sigma-model target, Kahler
  metric, `B`-field, Kahler form, and A-model odd zero modes.
- `vartheta`, `tilde vartheta`, `R`, `A`: compact scalar, dual compact
  scalar, radius, and first-order abelian duality one-form.
- `mathcal B`, `Y`, `u=Y+bar Y`, `K`, `tilde K`: local real superfield,
  twisted-chiral dual variable, real Legendre coordinate, original Kahler
  potential, and dual Kahler potential in abelian `N=(2,2)` duality.
- `G`, `V`, `r`, `Q_i`, `tau`, `T`, `q`, `sigma`: GLSM gauge group,
  matter representation, Fayet-Iliopoulos coordinate, charges, period-one
  FI-theta coordinate, logarithmic FI-theta coordinate
  `T=2 pi i tau`, exponentiated compact flux fugacity `q=exp(T)`, and
  vector-multiplet scalar.
- `Lambda_G`, `Lambda_G^vee`: cocharacter/flux lattice of an abelian quotient
  gauge group and its dual electric character lattice.  These control allowed
  matter charges, dual exponentials, FI-theta periods, and residual mirror
  orbifolds.
- `a`, `p_a`, `L`, `M_i(sigma)`, `Q_dyn`: spatial gauge holonomy, its
  quantized electric momentum, Hamiltonian circle length, charged-matter
  masses along the Coulomb direction, and the dynamical charge lattice that
  controls finite-mass electric screening.
- `Delta T^phys`: FI-character shift induced by changing branches of
  `log c_i`; it must lie in `2 pi i Lambda_G^vee` so that every compact flux
  in `Lambda_G` sees only an integral theta-period phase.
- `p_A`, `L_W`: chiral-superpotential monomial exponent vector and preserved
  phase-isometry lattice available to abelian dualization.
- `Sigma`, `tilde W_eff`, `mu`, `Q_tot`: twisted chiral field strength,
  abelian Coulomb-branch effective twisted superpotential, renormalization
  scale, and total positive charge in the one-loop Coulomb ledger.
- `Y_i`, `B_i`, `U_i`, `M_i(Sigma)`, `c_i`, `X_i`: charged-chiral dual
  twisted variables, first-order real superfields, real dual coordinates,
  charge-linear Coulomb masses, vortex-normalization constants, and
  exponential torus coordinates in the abelian mirror presentation.
- `conj:abelian-glsm-hori-vafa-mirror-qft`, `D_loc`, `D_pert`, `D_vort`,
  `D_obs`, `E_cont`, `E_op`, `E_top`, `E_bg`, `E_sing`: named full-QFT
  GLSM/Hori--Vafa mirror conjecture, its observable comparison layers, and the
  separate continuum/operator/topological/background/singular-locus proof
  debts.
- `constr:glsm-vortex-core-disorder-datum`, `mathfrak V_{pi,Lambda}`,
  `C_{pi,epsilon}`, `h_i(epsilon)`, `R^{core}_{pi,Lambda}`:
  gauge-covariant punctured-disk vortex-core disorder data, separating smooth
  extendable vortex cores from singular holonomy defects and from the later
  dual-frame source-row monomial `sum_i pi_i e^{-Y_i}`.
- `mathfrak M_Lambda`, `K_mir`, `D^mir_Lambda`, `C_ct`, `B_infty`,
  `G_glob`, `R_{Lambda->IR}`: full mirror-QFT datum separating the
  protected Hori--Vafa twisted-superpotential presentation from the mirror
  `D`-term/Kahler functional, functional measure, counterterms, noncompact
  boundary conditions, global/orbifold data, and Wilsonian map to the IR.
- `Z^mir_Lambda[J]`, `H_IR`, `mu_cont`, `R_lambda(p)`: admissible mirror
  cutoff functional integral, infrared Hilbert-space/spectral resolution,
  continuous spectral measure, and noncompact wall reflection datum.  These
  separate mirror-data existence, D-term universality, and the actual duality
  claim.
- `rem:glsm-mirror-dterm-rg-schur-obligation`, `H_eff^M(E)`, `o_eff^M(E)`,
  `Gamma_{AB}^M(E,Omega)`, `B_RG(E)`: finite Wilsonian Schur-complement test
  for mirror `D`-term universality, including high-mode elimination,
  counterterm transport, source renormalization, source-resolvent bounds, and
  source-metric residual bounds.
- `rem:glsm-mirror-operator-source-data`: finite-volume operator/source
  warning that equal spectra and protected multiplication data do not
  determine local-source matrix elements or source-normalized correlators.
- `rem:glsm-mirror-background-response-obligation`,
  `G^{bg}_{AI,Lambda}`, `C^{bg}_{AI,Lambda}`,
  `B^{bg}_{AI,Lambda}`: finite-regulator background-source response gate for
  the stress-tensor multiplet, vector/axial current multiplets, gravitational
  and `R`-current contact terms, and dilaton/background-charge couplings.
- `rem:glsm-mirror-boundary-defect-obligation`, `Z^cl_{\alpha\beta,Lambda}`,
  `Z^op_{\alpha\beta,Lambda}`, `D_{r,Lambda}`, `Z_{r,Lambda}`:
  finite-regulator boundary-state and defect comparison data, including
  closed/open cylinder amplitudes, Cardy residuals, defect fusion, and
  defect-twined traces.
- `rem:cigar-liouville-pathwise-fake-fixed-point-obligation`,
  `S_{\Lambda,L}(kappa)`, `theta(s)`, `P_n`: finite-regulator
  cigar/Liouville pathwise transport package for energies, spectral
  projectors, reflection phases, pole residues, boundary annuli, source rows,
  and noncompact wall domains; this separates local deformation rigidity from
  global fake-fixed-point exclusion.
- `constr:cigar-liouville-source-spectral-resolution`,
  `d\mu^{cont}_{O,\alpha}`, `G_{O,\alpha}^{I}(\beta)`: positive source
  noncompact spectral-resolution coordinate for the cigar/Liouville comparison,
  separating signed reflection phase/counting density from the finite-box
  normalized Plancherel/source Gram measure, normalizable bound states,
  resonance continuation, and contact terms in a Euclidean two-point observable.
- `constr:cigar-liouville-matrix-spectral-measure`,
  `d\mu^{cont}_{IJ,\alpha}`, `G^{f,\mathcal I}_{IJ,\alpha}`: positive
  matrix-valued continuous spectral measure for a family of local sources,
  including Plancherel weights, source rows, normalizable bound-state norming
  constants, resonance continuation, positivity, and contact scheme data.
- `constr:cigar-liouville-asymptotic-deformation-filter`, `ell`, `g_a`,
  `b_alpha`, `delta S`: asymptotic Liouville deformation classifier separating
  the integer periodic protected `F`-term inventory from real `D`-term,
  boundary-domain, and source/contact deformations that can move reflection
  density, residues, annuli, or source rows.
- `hat X_i`, `q_phys`, `R_{P^{N-1}}`, `H`: vortex-normalized mirror-torus
  coordinate, physical exponentiated FI coordinate after finite determinant
  normalization, normalized projective-space mirror residue trace, and
  hyperplane/Coulomb class in the `P^{N-1}` protected ring test.
- `Q_Sigma`, `C_Q^br`, `Lambda_Q`: rank-one GLSM charge sum, branch-fixed
  Coulomb charge constant, and RG-invariant vortex/Coulomb transmutation
  scale after the vortex coefficients and FI coordinate have been combined.
- `A^A_{Lambda,k}`, `S_k(q_Lambda)`, `R_coeff`, `R_det`, `R_zm`,
  `R_cpt`, `R_gl`, `R_op`, `R_cont`: finite-regulator A-twisted observable,
  mirror-residue prediction, and stage residuals in the vortex-to-observable
  comparison ledger.
- `C_{Lambda,1}`, `R_line`, `epsilon_{off,a}`: finite-regulator degree-one
  three-point coefficient for the `P^{N-1}` quantum product, the line-count
  compactification/orientation residual, and off-pairing bounds needed before
  the product relation is a controlled A-twisted observable.
- `Omega_{Lambda,1}`, `J_Lambda`, `r_i`: transported finite
  degree-one instanton-measure density, retained-chart Jacobian, and finite
  vortex-coefficient rescaling used to test scheme covariance of the
  `P^{N-1}` degree-one observable.
- `ex:cpn-degree-one-euler-determinant-line`,
  `eq:cpn-degree-one-euler-zero-mode-quotient`,
  `eq:cpn-degree-one-euler-determinant-line`: degree-one `P^{N-1}` Euler
  sequence quotient computing the `H^0(O(1)^N)/H^0(O)` tangent zero modes,
  determinant-line orientation, and paired nonzero-mode cancellation in the
  retained A-twisted window.
- `ex:cpn-degree-one-evaluation-berezin-jacobian`,
  `eq:cpn-degree-one-evaluation-berezin-jacobian`: evaluation-form Berezin
  Jacobian for the degree-one `P^{N-1}` three-point insertion, showing how two
  point insertions and one hyperplane insertion saturate the fermionic zero-mode
  measure with coefficient `+1`.
- `ex:cpn-degree-one-representative-independence-gate`,
  `eq:cpn-degree-one-primary-representative-independence`,
  `eq:cpn-degree-one-excess-invariance`,
  `eq:cpn-degree-one-boolean-boundary-negative-control`,
  `eq:cpn-degree-one-source-contact-observable`: representative-independence
  gate for the degree-one `P^{N-1}` primary A-model coefficient.  The current
  text treats non-transverse representatives by deformation or refined/excess
  intersection, rejects Boolean boundary-indicator arithmetic, and separates
  collision-sensitive source contacts from the primary invariant.
- `q_mir`, `I_{Lambda,1}`, `B_vort`, `B_I`, `B_q`, `B_off,a`:
  mirror-residue FI coordinate typed as the transported compact FI character,
  retained finite degree-one instanton-measure integral, and residual majorants
  in the Hori--Vafa residue/direct-instanton comparison map.
- `V_{1,Lambda}`, `U_Lambda`, `pi_i`, `tilde pi_i`, `Pi_O`,
  `B_span`: finite common-flux source space, original-to-dual operator
  transport map, primitive original and mirror source rows, tested observable
  row, and residual controlling whether primitive mirror rows span the
  observable being compared.
- `overline M_{0,3}(P^{N-1},d)`, `ev_j`, `I_d`: compactified genus-zero
  stable-map moduli space, evaluation maps, and A-model three-point invariant
  used in the direct `P^{N-1}` quantum-product computation.
- `U_{i,1,Lambda}`, `W_{i,1,Lambda}^{nz}`, `Z_{i,F,Lambda}^0`,
  `c_{i,Lambda}`: finite-regulator one-vortex chart, nonzero-mode
  determinant ratio, zero-mode Berezin coefficient for the twisted
  `F`-term measure, and regulated vortex coefficient.
- `lambda_pm`, `xi_pm`, `eta_alpha`, `P_Lambda`, `U_{pm,Lambda}`,
  `A^{(1)}_{i,Lambda}(O)`, `I^0_{O,Lambda}`, `R_src`, `R_prop`:
  one-vortex source-functional bookkeeping sources, universal and residual
  fermion zero-mode coordinates, finite source polynomial,
  source-to-zero-mode overlaps, source-differentiated component amplitude,
  retained zero-mode/source overlap, and the source/propagator residuals
  separating component amplitudes from the twisted `F`-term coefficient.
- `K_p`, `u_A`, `u_B`, `Delta_AB`, `C'_{AB}`, `R_{AB,Lambda}`:
  finite one-vortex component-amplitude cell weight, source-overlap vectors on
  the universal zero-mode line, their oriented Berezin minor, primed
  nonzero-mode contact term, and residual in the worked component cell.
- `U_R`, `C_R`, `M_R`, `kappa_R`, `T_R`, `epsilon_det`,
  `epsilon_zm`, `epsilon_cpt`, `epsilon_cont`: retained compact vortex
  window, its signed one-vortex coefficient, its absolute one-vortex mass,
  the noncancellation margin, and the tail/determinant/zero-mode,
  compactification-boundary, and continuum residual bounds used to control
  that the regulated single-vortex coefficient is genuinely nonzero.
- `D_{F,i,Lambda}`, `Pi_univ`, `K^{res}_{i,Lambda}`,
  `nu^{res}_{i,Lambda}`: vortex-sector fermion Hessian, universal
  two-dimensional zero-mode pair, residual fermion-zero-mode space, and its
  dimension after the universal `d^2 theta_tilde` pair is removed.
- `g_{Lambda,z}`, `B_{Lambda,z}`, `E_{Lambda,z}`, `G_z`, `L_z`,
  `M_z`, `H_{B,z}`: finite-regulator gauge-orbit space, bosonic fluctuation
  space, linearized vortex-equation space, gauge variation map, linearized
  vortex/gauge-slice map, Faddeev-Popov operator, and sliced bosonic Hessian
  in the local vortex fluctuation complex.
- `Y_P`, `rho`, `vartheta`, `u`, `chi`, `k`: logarithmic-chiral dual
  variable, polar coordinate for the charged chiral scalar, angular
  coordinate, real and periodic parts of `P`, and cigar level parameter.
- `conj:cigar-liouville-mirror-qft`, `C_cl`, `C_dual`, `C_vort`,
  `C_spec`, `C_bdry`, `R(j,m,bar m;k)`, `nu_raw(k)`,
  `nu_+(k;mu,varrho_ref)`: named full-QFT cigar/Liouville mirror conjecture,
  the protected-data/proof-debt lanes separating quotient/dualization/vortex
  checks from spectral-flow, continuous-spectrum, defect, and boundary data,
  and the exact reflection-amplitude datum that a full spectral comparison must
  reproduce with a declared positive normalization scale.
- `X_i`, `P`, `G_d`, `d`, `mu_d`: hypersurface GLSM fields, homogeneous
  polynomial, degree, and residual finite gauge group.
- `H`, `Y_G`, `C_branch`, `T`: hyperplane Chern class on projective space,
  smooth hypersurface target in the positive chamber, branch-dependent
  Coulomb constant for the anomaly-free hypersurface charge vector, and the
  shifted additive FI coordinate.

## Claim Ledger

- Defines the `N=(2,2)` supersymmetry algebra and BPS positivity input.
- Defines polynomial Landau-Ginzburg data as field-variable presentations,
  including component variables, Kahler metric, and superpotential.
- Derives the auxiliary-field potential and identifies classical vacua as the
  critical locus of `W`.
- Defines quasihomogeneous isolated Landau-Ginzburg data and the Jacobi
  algebra.
- Proves that the B-type local differential with
  `Q_B eta_i = partial_i W` gives degree-zero polynomial cohomology
  `Jac(W)`.
- Proves the quasihomogeneous charge ledger, Fermat Jacobi basis, Fermat
  Jacobi dimension, and protected central-charge test, while marking the
  infrared fixed-point existence claim as a separate construction problem.
- Adds the Fermat Wilsonian superpotential coordinate argument: under a
  declared chiral Wilsonian scheme, regularity at `g_i=0`, flavor spurion
  symmetries, and `R(W)=1`, the only regular holomorphic monomials in the
  superpotential are the original `g_i (Phi^i)^{d_i}` terms.  This is a
  coordinate-level nonrenormalization statement, not an infrared existence
  theorem.
- Adds the coordination bridge to Volume V: if the infrared SCFT exists and
  `Jac(W)` classes become NS chiral primaries, then spectral flow by
  `eta=-1/2` shifts a monomial charge to the left Ramond charge
  `Q_R-c_LG/6`, giving the finite `chi_y` protected polynomial required by
  the elliptic-genus interface.
- Defines sigma-model and GLSM data and separates protected coordinates from
  full infrared QFT equivalence.
- Records the Coleman low-dimensional continuous-symmetry caveat for
  \(1+1\)-dimensional flavor and \(R\)-symmetry language: protected chiral
  rings, indices, anomalies, twists, and topological sectors are not ordinary
  local continuous order parameters.
- Defines the A/B twist spin-shift convention and proves that
  `Q_A = bar Q_+ + Q_-` and `Q_B = bar Q_+ + bar Q_-` are scalar nilpotent
  supercharges in the central-charge-free local sector.
- States the anomaly requirements for the vector and axial `R` symmetries
  and identifies the axial GLSM obstruction as the charge sum.
- Proves that the Morse residue functional descends to `Jac(W)` and gives a
  nondegenerate pairing when the critical points of `W` are nondegenerate.
- Records the genus-`g` B-twisted LG zero-mode formula with its determinant
  and regulator status boundary.
- Proves that the constant-map A-model zero-mode algebra is the de Rham
  complex of the target.
- States the A-model holomorphic-map energy decomposition and names the
  compactification/orientation/contact-term inputs required for genuine
  correlation functions.
- Defines abelian duality as an intrinsic two-dimensional QFT operation,
  not a string-theoretic mirror-symmetry argument.
- States the compact scalar first-order duality hypotheses, including
  winding sectors, integral-period normalization, Gaussian contour, and
  determinant normalization.
- Proves the local compact-scalar radius inversion `R -> R^{-1}` from the
  first-order Gaussian path integral and records the momentum-winding
  spectrum test.
- Defines the local `N=(2,2)` chiral/twisted-chiral Legendre-transform
  duality datum and proves the Hessian inversion `tilde K'' = 1/K''`.
- Records the GLSM charged-chiral dualization ledger and marks
  nonperturbative exponential twisted-superpotential terms as requiring a
  separate vortex-instanton compactness/zero-mode/determinant proof.
- States the named abelian GLSM/Hori--Vafa mirror QFT conjecture with charge
  matrix, FI-theta coordinate, global gauge form, spin/background data,
  regulator, phase chamber, singular-locus exclusions, mirror `D`-term/Kahler
  data, functional measure, counterterms, global/orbifold data, noncompact
  boundary conditions, continuum Hilbert spaces/Hamiltonians, local OPEs, A/B
  sectors and pairings, defects, boundaries, topological sectors, contact
  terms, and RG endpoints.  The statement is now explicitly an equivalence of
  infrared endpoints of regulated theories, and the chapter separates this
  full-QFT statement from the protected evidence lanes `D_loc`, `D_pert`,
  `D_vort`, and `D_obs`, and from the proof-debt lanes `E_cont`, `E_op`,
  `E_top`, `E_bg`, and `E_sing`.
- Adds the global-form flux lattice datum for abelian mirrors.  The compact
  gauge torus is specified by its cocharacter lattice `Lambda_G`, fluxes lie in
  `Lambda_G`, charged fields and allowed mirror exponentials lie in
  `Lambda_G^vee`, and logarithmic FI periods are characters of `Lambda_G`.
  The rank-one `U(1)/Z_n` example shows explicitly that cover-charge-one
  matter, ordinary `2 pi i` FI periods, and covering-torus product constraints
  cannot be reused without the quotient mirror orbifold.
- Adds the Hamiltonian electric-flux lift of the large-`sigma` region: on a
  spatial circle the compact holonomy `a` has momentum
  `p_a in Lambda_G^vee`, the Lorentzian zero-mode Lagrangian
  `dot a^2/(2 e^2 L)+(theta/2 pi) dot a` gives
  `E_n/L=(e^2/2)(n-theta/2 pi)^2`, and the physical minimum is taken over the
  declared electric character lattice.  The text separates this dynamical
  large-`sigma` energy from the protected Coulomb-coordinate singularity,
  records charged-pair screening by `Q_dyn` at finite matter mass, and
  distinguishes covering non-effective presentations from faithful
  `U(1)/Z_g` global form with `Lambda_G^vee=gZ` and theta period `2 pi g`.
- Defines the full mirror-QFT datum `mathfrak M_Lambda`, distinguishing the
  protected Hori--Vafa presentation `(Y_i,Sigma_a,W_tilde_dual)` from the
  mirror Kahler/D-term functional, induced measure, counterterms,
  noncompact-boundary functional, global data, and Wilsonian map.  The chapter
  now states that two mirror theories with the same twisted superpotential are
  physically interchangeable only after a universality/rigidity statement and
  boundary-term control.
- Adds the admissible-mirror datum and IR-equivalence ladder:
  `mathfrak M_Lambda` must be realized as a regulated path integral with a
  self-adjoint Hamiltonian domain, renormalized operator topology, noncompact
  spectral resolution, reflection relation, pole-residue normalization, and
  source contact terms.  The chapter now separates the existence of such a
  mirror datum, the universality/rigidity of choices of finite-field `K` and
  boundary data, and the final GLSM/mirror duality assertion.
- Adds `rem:glsm-mirror-operator-source-data`: a finite-volume source
  spectral formula showing that a Hamiltonian spectrum and protected
  chiral-ring multiplication do not determine the matrix elements entering
  source derivatives of the regulated generating functional.  The full mirror
  datum must include operator topology, source normalization, and an
  operator/state map.
- Adds `rem:glsm-mirror-background-response-obligation`: a finite
  background-source kernel showing that stress-tensor, vector/axial
  `R`-current, flavor-current, gravitational contact, and dilaton/background
  charge responses are full-QFT data.  A flat source metric or a single
  contact-patched background probe does not determine the generating
  functional coupled to background fields.
- Derives the first-order charged-chiral dualization with real superfield
  `B_i`, twisted-linear constraint, Legendre elimination, and the
  superspace integration-by-parts identity producing the linear
  `-Q_i^a Sigma_a Y_i` twisted `F`-term.
- Records the charged-chiral dual `D`-term
  `K_i^cl(U_i)=-1/2 U_i log(U_i/2)`, its `U_i=Y_i+bar Y_i>0` domain, the
  singular boundary at `U_i=0`, the weak-coupling cylindrical end, and the
  induced-measure/anomaly obligation.  This makes the local mirror coordinate
  a full-action datum rather than only a holomorphic variable.
- Defines the dual mass linear form `M_i(Sigma)=sum_a Q_i^a Sigma_a` and the
  protected dual twisted-superpotential datum with exponential
  `-mu c_i exp(-Y_i)`, while recording the vortex-term proof obligations
  left schematic in classic mirror-duality papers.
- Identifies the coefficient `c_i` as the continuum limit of the reduced
  determinant/operator normalization after the classical FI-theta sector
  weight has been divided out and the original-to-dual map has been fixed.  The
  original GLSM amplitude carries the numerical FI-theta sector weight
  separately, together with the nonzero-mode determinant ratio, the
  source-dependent interacting normal-mode expectation, two universal fermion
  zero modes forming the twisted `F`-term measure, possible extra zero-mode
  saturation, collective-coordinate integration, and the punctured-disk core
  boundary condition needed to define the original disorder insertion; the dual
  frame supplies the operator `exp(-Y_i)`.  This makes the Hori--Vafa
  exponential term a rechecked amplitude datum in the chapter's conventions
  rather than a scalar inserted into the original path integral.
- Adds a one-vortex source-functional extraction bridge: the same regulated
  sector is written with bookkeeping sources for the two universal fermion
  zero modes, residual zero-mode coordinates, and local component sources.
  The twisted `F`-term coefficient is the `xi_+ xi_- eta_top` coefficient of an
  effective insertion `<exp(-V_int) P_bare>'`, while source-differentiated
  component amplitudes additionally carry source-to-zero-mode overlaps, primed
  propagator contractions, source/operator normalization, source-dependent
  interacting normal-mode cumulants, and residual budgets.
  This separates the physical
  instanton amplitude from a moduli-space volume, Coulomb-logarithm match, or
  formal Hori--Vafa monomial.
- Adds a worked finite one-vortex component-amplitude cell: two component
  sources are projected to overlap vectors on the universal fermion zero-mode
  line, the Berezin integral extracts the oriented minor
  `u_{A,+}u_{B,-}-u_{A,-}u_{B,+}`, and a primed nonzero-mode contact term plus
  residual bound are kept outside the protected coefficient `c_i`.  Parallel
  source overlaps, source orientation changes, and omitted contact terms now
  have explicit physical consequences.
- Adds the single-vortex coefficient noncancellation bound: after choosing a
  retained compact vortex window, the reduced signed coefficient `C_R` must
  dominate the absolute one-vortex mass by a margin `kappa_R` and must exceed
  the tail, determinant, zero-mode/orientation, and compactification residual
  budget.  A dual-frame nonzero claim compares `Z_map C_R`, not `C_R`, and
  includes map and continuum residuals.  This separates the physical
  nonzero-amplitude claim from charge matching, holomorphy, and
  Coulomb-logarithm matching.
- Adds the vortex zero-mode filter for twisted `F`-terms: after the two
  universal fermion zero modes are identified with `d^2 theta_tilde`, the
  residual Berezin integral extracts the top residual Grassmann degree, so the
  uninserted vortex superpotential term vanishes unless no residual zero modes
  remain.  This isolates the physical amplitude question behind the compact mirror
  monomial.
- Adds the finite-regulator vortex fluctuation complex: the coefficient
  `c_i` is tied to a local gauge complex
  `g_Lambda -> B_Lambda -> E_Lambda`, a Faddeev-Popov determinant, the
  sliced bosonic Hessian, and the primed fermion Hessian after universal and
  residual zero modes have been separated.  This exposes the determinant
  calculation behind the Hori-Vafa coefficient without promoting it to a full
  continuum proof.
- Derives that a general connected holomorphic correction
  `h_i(X_i)`, `X_i=exp(-Y_i)`, is forced to be the primitive monomial
  `mu c_i X_i` if the eliminated branch is required to reproduce the
  Coulomb one-loop logarithm for all nonzero `M_i` in the local branch.
  This is a finite protected matching argument, not a construction of the
  vortex amplitude.
- Proves that eliminating `Y_i` reproduces the Coulomb one-loop
  superpotential and that the constants `c_i` shift the finite definition of
  the FI coordinate.
- Adds one-loop branch/monodromy bookkeeping before Hori--Vafa mirror
  constraints are used: the component determinant response selects the
  logarithm sign, logarithm-sheet shifts of the Coulomb determinant are
  transported into integral periods of the logarithmic FI coordinate `T`, the
  `Sigma=0` monodromy is identified with `sum_i Q_i`, and
  compact-periodicity-as-sign and absolute-value-only logarithm shortcuts are
  rejected.  This is an exact convention-control remark, not a controlled
  approximation.
- Adds the compact FI-theta normalization ledger: with
  `k=(2 pi)^{-1} int F`, `tau=theta/(2 pi)+i r`, and
  `T=2 pi i tau=-2 pi r+i theta`, a flux-`k` saddle carries
  `q^k=exp(T k)`, invariant under `theta -> theta+2 pi`.  The old
  `exp(tau)` fugacity is explicitly ruled out.
- Rebuilds the one-vortex notation around the common gauge-bundle flux:
  the flux-one sector is not attached to a flavor label.  The index `i` labels
  a dual disorder/source projection to `exp(-Y_i)`, while the original GLSM
  flux weight is the common `q_top`.  The source-projection interface now writes
  `hat c_i^orig=Pi_i(A_{1,Lambda})` for projections of one FI-stripped common
  sector and separates physical observable projections
  `C_O^{(1)}=Pi_O(A_{1,Lambda})` from mirror-coordinate products
  `prod_i c_i^{Q_i^a}`.  Such products are coordinate assemblies until a
  source-factorization or observable-comparison theorem supplies the assembly
  map and residual bounds.
- Adds `rem:glsm-common-flux-operator-map-diagnostic`: a finite-regulator
  diagnostic for turning common-flux primitive projections into a mirror
  operator map.  It requires an original-to-dual source transport map,
  row-wise matrix-element comparisons for the `exp(-Y_i)` representatives,
  flavor covariance, an observable assembly row, and a span residual.  The
  block exhibits the failure mode where two common-flux functionals have the
  same primitive projected `c_i` but differ on the tested observable.  The
  status is a residual diagnostic, not a controlled estimate until component
  bounds are supplied in one source topology.
- Extends the vortex-normalization/FI-coordinate comparison to all abelian
  ranks: normalized mirror-torus variables `hat X_i=c_i exp(-Y_i)` move the
  constants into `T_a^phys=T_a+sum_i Q_i^a log c_i`, and the same shift is
  checked against the Coulomb affine term, with logarithm-branch changes
  identified as integral `2 pi i` shifts of the logarithmic FI coordinate.
  The follow-on FI-character proposition checks the same branch shifts against
  the declared compact flux lattice, so the normalization constants are
  harmless scheme data only when the charge rows are characters of
  `Lambda_G`.
- Adds the rank-one vortex-fugacity transmutation check: the protected
  Coulomb roots depend on
  `mu^{sum_i Q_i} exp(T+sum_i Q_i log c_i)/prod_i Q_i^{Q_i}`, so `mu` is
  fake only after FI running and finite vortex determinant normalization are
  combined; in the anomaly-free case the `mu` power cancels instead.
- Derives the low-energy `Sigma_a` constraints
  `sum_i Q_i^a Y_i=-T_a`, producing the logarithmic-torus mirror
  Landau-Ginzburg presentation of protected twisted-chiral data.
- Works out the `P^{N-1}` mirror critical equations and matches their `N`
  simple critical points to the Coulomb vacuum count.
- Adds the `P^{N-1}` protected observable test after Hori--Vafa
  normalization: with `q_phys=exp(T+sum_i log c_i)`, the constrained mirror
  logarithmic Hessian is `N x^{N-1}` and the finite residue trace gives
  `R(H^k)=q_phys^d` for `k=N-1+dN` and zero off that selection rule.  This
  recovers the protected quantum-product relation `H^N=q_phys` only after the
  vortex coefficient, determinant-line orientation, stable-map
  representative/excess convention, and any declared source-contact data are
  fixed.
- Adds the vortex-to-observable residual comparison: the regulated
  `P^{N-1}` A-twisted correlator is compared to the mirror residue through
  separate coefficient, determinant, zero-mode, representative/excess,
  source-contact, gluing, operator-map, and continuum residuals.  The chapter
  now makes the nonzero vortex coefficient and the vanishing of those residuals
  the load-bearing physics inputs before the finite Hori--Vafa residue identity is
  promoted to the quantum-product statement.
- Adds the direct A-model stable-map computation for the `P^{N-1}` quantum product:
  the virtual dimension of `overline M_{0,3}(P^{N-1},d)` is `(N-1)+Nd`,
  the degree-one insertions `(H,H^{N-1},H^{N-1})` have the matching
  codimension `2N-1`, and the geometric line count is one.  This supplies the
  physical stable-map side of `H^N=q_phys` after the virtual class,
  determinant orientation, compactification, and operator map have been fixed.
- Replaces the degree-one vortex observable assembly claim with a retained
  finite zero-mode/intersection model plus a conditional proof-obligation template: the
  check computes the determinant-normalized fugacity, incidence orientation,
  Berezin saturation, compactification exclusion, and unit hyperplane
  normalization before comparing
  `eta_Lambda(H star_Lambda H^{N-1},H^{N-1})` with `q_Lambda` through
  coefficient, determinant, zero-mode, line-count, operator-map, off-pairing,
  and continuum residuals.  This prevents both mirror-residue-only and
  dimension-count-only arguments from being treated as the physical A-twisted
  correlator.
- Adds a degree-one A-model zero-mode measure bridge before the
  proof-obligation template: the retained path-integral coefficient is written as a
  vortex-normalized fugacity times a bosonic collective-coordinate density,
  nonzero-mode determinant-line element, and A-twisted Berezin zero-mode
  coefficient.  For convex `P^{N-1}` the obstruction space vanishes, so the
  insertions `(H,H^{N-1},H^{N-1})` saturate the top zero-mode degree
  `2N-1`; orientation reversal, extra zero modes, or omitted obstruction data
  change or kill the coefficient.
- Adds the explicit degree-one projective Euler-sequence determinant-line
  calculation: pulling back
  `0 -> O -> O(1)^N -> phi^* T P^{N-1} -> 0` computes the `2N-1`
  tangent/fermion zero-mode quotient, removes the common homogeneous
  rescaling, fixes the complex determinant-line orientation, and keeps the
  paired nonzero-mode determinant ratio distinct from the incidence count.
- Adds the degree-one evaluation-form Berezin-Jacobian calculation: in the same
  affine stable-map chart, the two point insertions and the hyperplane
  insertion are pulled back as zero-mode one-forms, and their top wedge has
  determinant `+1`.  Duplicated/contact forms, hyperplane rescalings, and
  orientation swaps change the A-twisted coefficient, so the line count is tied
  to the operator representative and fermion measure.
- Adds the finite measure-scheme covariance test for that same degree-one
  observable: rescaling the supplied vortex coefficients must be accompanied by
  the inverse FI-coordinate shift, and changing the zero-mode chart density
  must transport the inverse Jacobian through the nonzero-mode/Berezin density.
  The retained coefficient is invariant only for the full package
  `q_Lambda * int Omega_{Lambda,1}`; stale FI coordinates, missing Jacobians, or
  untransported orientation signs are treated as real coefficient changes.
- Adds the Hori--Vafa residue/direct-instanton comparison map for the
  degree-one `P^{N-1}` product: the mirror residue `S_1(q_mir)` is compared
  against the direct A-twisted coefficient only after `q_mir` and the
  transported vortex fugacity `q_Lambda` have been placed on the same compact
  FI-character line.  The comparison then uses the retained instanton-measure
  integral `I_{Lambda,1}`, FI-coordinate transport, operator/continuum
  residuals, and off-pairing bounds.  The direct side now also exposes the finite
  degree-one incidence determinant `+1`, insertion-degree gate, and
  compactification exclusion before the residual `I_{Lambda,1}-1` is
  budgeted.  This prevents the protected root sum, the stable-map line count,
  the Coulomb normalization check, or a separately chosen mirror fugacity from
  standing in for the regulated vortex measure and zero-mode calculation.
- Derives the classical cigar quotient metric by solving the auxiliary
  constraint, gauge fixing the logarithmic chiral scalar, and eliminating the
  gauge field.
- Develops the cigar/Liouville mirror chain as a QFT comparison problem:
  dual variables `Y,Y_P`, the single exponential from the ordinary charged
  chiral multiplet, the finite topological obstruction to a smooth
  finite-action logarithmic-chiral vortex exponential,
  the intermediate dual `D`-term action with
  `-1/2(Y+bar Y)log(Y+bar Y)-1/(2k)bar Y_P Y_P`, the `Y+Y_P=0` vector
  constraint, the resulting `N=2` Liouville superpotential, and the
  theorem-status boundary for full equality with the cigar coset QFT.
- States the named cigar/Liouville mirror QFT conjecture with level and
  background-charge conventions, spin structures, spectral-flow sectors,
  normalizable states, nonnormalizable sources, continuous-spectrum measure,
  local operator map, reflection amplitudes, Hilbert space, superconformal
  generators, finite-field `D`-term/Kahler control, allowed-deformation
  classification, defects, boundaries, and contact terms.  The quotient metric,
  asymptotic dualization, ordinary chiral exponential, and logarithmic-vortex
  obstruction are recorded as `C_cl`, `C_dual`, and `C_vort` evidence.
  The chapter now also records `C_spec` normalization targets: the
  metric/dilaton as a large-level representative rather than exact finite-level
  QFT data, central charge `c=3+6/k`, noncompact effective central charge,
  continuous/discrete `(j,m,bar m)` sectors, the bosonic
  `SL(2,R)_{k+2}` convention, spectral-flow momentum/winding lattice,
  noncompact field identification, spin-structure pairing boundary, reflection
  amplitude `R(j,m,bar m;k)` as an imported normalization target together with
  its signed continuous phase-density and sample simple-residue consequences,
  the positive matrix-valued source spectral measure needed to compare
  Plancherel weights, finite-box normalization, normalizable-state norming
  constants, and resonance continuation across a family of local sources, the
  ordinary-chiral endpoint Liouville action with background-charge coupling,
  the Liouville exponential marginality check, and an asymptotic deformation
  filter showing that the primitive integer exponential is the only marginal
  protected `F`-term while wall-domain and `D`-term/source deformations still
  need spectral-response control.  Full derivation of the Liouville
  normalization, complete spectral measure, all pole-residue normalization,
  operator completeness, finite-field rigidity, and defect/boundary matching
  remain obligations.  The boundary/defect obligation makes that last obligation
  concrete through closed/open cylinder amplitudes, Cardy residuals,
  defect-twined traces, and defect fusion data.  The pathwise fake-fixed-point
  obligation makes the Hori--Kapustin continuity obligation concrete through
  finite-regulator spectral/source/boundary transport, rather than local
  rigidity at a single endpoint.
- Defines abelian GLSM data with fields, integer charges, invariant
  superpotential, complexified FI-theta coordinate, gauge coupling, and
  regulator.
- States the axial anomaly charge sum as a finite ledger and a necessary
  condition, not a conformality proof.
- States the abelian GLSM Coulomb-branch one-loop determinant hypotheses,
  including logarithm branches, regulator scheme, and exclusion of
  boundary/vortex/singular-locus contributions from the local determinant,
  and then derives the perturbative local determinant contribution from the
  complete charged-chiral quadratic action, the Hermitian corrected Dirac
  square `D_F^dagger D_F=-nabla^2+|M|^2+Q gamma_* F_12+...`, the local
  determinant density `Q/(4 pi) log(|M|^2/mu^2)`, and the `1/(2 pi)`
  twisted-`F` component bridge that converts this density to the real part of
  `Q log(M/mu)`.  The Fujikawa phase is tied to the same heat-kernel
  convention: `Tr_reg gamma_*=-Q k`, with the finite companion now computing
  the same sign from a warning-clean flux-carrying magnetic-torus
  Wilson-overlap kernel rather than an assigned chiral dimension mismatch;
  the mass-rotation generator `-gamma_*/2` gives the theta shift
  `theta -> theta+Q alpha`.
- Derives the effective twisted-superpotential critical equation
  `prod_i (Q_i sigma/mu)^{Q_i}=exp(T)` and proves that all-positive charges
  give `sum_i Q_i` simple local Coulomb vacua.
- Works out the `P^{N-1}` charge-one vacuum count and records the
  hypersurface charge-vector signal: the Coulomb `sigma` exponent is
  `N-d`, equal to the axial anomaly coefficient, so the anomaly-free case
  gives a FI-theta singular-locus condition rather than isolated Coulomb
  roots.
- Derives the classical chamber analysis for the hypersurface GLSM with
  charges `(1,...,1,-d)`, including the `r>0` hypersurface quotient, the
  `r<0` Landau-Ginzburg finite-quotient chamber, and the singular status of
  `r=0`.
- Derives the hypersurface adjunction formula
  `c1(TY_G)=(N-d)H|_{Y_G}` and `K_{Y_G}=O(d-N)|_{Y_G}`, making the
  `d=N` Calabi-Yau condition a finite geometric consequence rather than a
  slogan.
- Compares the large-volume sigma-model central-charge target
  `3(N-2)` with the Fermat Landau-Ginzburg protected central charge
  `3N(1-2/d)`, proving equality precisely for `d=N`.
- Makes the residual finite gauge theory explicit in the `r<0` chamber:
  after fixing nonzero `P`, the unbroken group is `mu_d`, it acts by
  `X_i -> zeta X_i`, the degree-`d` superpotential descends, and the
  untwisted Jacobi-basis invariant condition is
  `sum_i a_i = 0 mod d`.
- Derives the hypersurface Coulomb-coordinate signal
  `(sigma/mu)^{N-d}(-d)^{-d}_{branch}=exp(T)` and the anomaly-free
  branch condition `exp(T)=C_branch`, or `T_sing=0` after an additive FI-coordinate
  shift.
- Inserts the separate Hamiltonian explanation of the hypersurface
  large-`sigma` lift: in the ordinary `U(1)` hypersurface GLSM the charge gcd
  is one, finite-mass matter can screen adjacent electric sectors, but in the
  `L |sigma| -> infinity` retained zero-mode limit a nonintegral
  branch-shifted theta class has positive minimized electric-flux energy.  The
  text now explicitly distinguishes the D-term chambers, protected one-loop
  Coulomb coordinate, dynamical electric-flux energy, and conjectural
  nonsingular IR equivalence.
- Presents the quintic GLSM solely as intrinsic two-dimensional QFT data, not
  as a string compactification.
- Records the construction problem for GLSM flows to Landau-Ginzburg and
  hypersurface sigma-model fixed points as intrinsic two-dimensional QFTs.

## Calculation Checks

- `calculation-checks/susy_2d_lg_glsm_checks.py` verifies:
  - `A_k` quasihomogeneous superpotential and derivative charges;
  - `A_k` Jacobi dimensions and central charges;
  - Fermat tensor-product monomial charges and Jacobi dimensions;
  - Fermat Wilsonian superpotential spurion selection, showing that
    regular holomorphic monomials obeying the declared flavor and `R` charges
    are exactly the original superpotential monomials;
  - quintic Landau-Ginzburg central charge `c=9` and Jacobi dimension `4^5`;
  - hypersurface GLSM gauge-invariance, axial-anomaly sum, positive-chamber
    dimension, and negative-chamber residual finite group order;
  - A/B twist spin shifts and scalar-supercharge nilpotence ledger;
  - abelian circle-duality momentum-winding spectrum invariance and
    chiral/twisted-chiral Legendre-Hessian inversion;
  - abelian GLSM Coulomb one-loop charge-exponent, positive-charge
    vacuum-count, hypersurface exponent/anomaly, quintic exponent-zero
    arithmetic, and the primitive of the Coulomb logarithmic derivative with
    its finite FI-coordinate shift under determinant normalization changes,
    plus the Coulomb determinant/Fujikawa response cell checking the corrected
    Hermitian Dirac square, signed-log coefficient extraction across charge
    and mass-order reversals, paired nonzero fermion spin traces, a
    warning-clean flux-carrying magnetic-torus Wilson-overlap index,
    heat-kernel chiral trace, and theta-shift Jacobian;
  - compact FI-theta/common-flux checks: `T=2 pi i tau=-2 pi r+i theta`
    gives the theta-periodic flux weight `q=exp(T)` while the nonperiodic
    `exp(tau)` shortcut fails; equal-charge flavor rotations preserve the
    common gauge flux but not flavor-labelled topological sectors; finite
    source-projection functionals compute projected coefficients and a direct
    common observable amplitude by separate routes, so arbitrary projected data
    or a bare projected product fail without an assembly map;
  - the vortex-core disorder-insertion gate: the covariant boundary period
    `h_i=(2 pi)^{-1} int(d theta_i+Q_i A)` is invariant under large gauge
    transformations, smooth core extension requires regular holonomy and an
    integral divisor zero, singular holonomy cancellation is a separate defect
    domain, the first-order boundary term on the excised disk gives the
    primitive `exp(-Y_i)` orientation, flavor rotations act on source rows
    rather than flux sectors, and the core-domain residual is a required
    operator-map budget term;
  - quotient global-form flux/character lattice checks: for `U(1)/Z_n` the
    flux lattice contains `1/n`, the electric character lattice is `nZ`, the
    logarithmic FI period is `2 pi i n` in covering coordinates, cover-charge
    one is not allowed matter, and the residual mirror orbifold order cannot be
    dropped;
  - theta-shifted compact electric-flux Hamiltonian checks: the finite
    holonomy Legendre transform gives
    `E_n/L=(e^2/2)(n-theta/2 pi)^2`, noncompact holonomy falsely removes the
    theta gap, quotient global form changes the electric lattice and theta
    period, and finite-mass charged screening collapses sectors by the
    dynamical charge gcd before the large-`sigma` unscreened limit is taken;
  - chiral-superpotential phase-isometry checks: a gauge-neutral monomial
    `P X_1 X_2` with charges `(1,1,-2)` preserves only the kernel
    `v_1+v_2+v_P=0`, so charge neutrality alone cannot justify dualizing all
    individual phases or using the bare Hori--Vafa variables without extra
    spurion/mirror-interaction data;
  - charged-chiral mirror-variable elimination matching the Coulomb one-loop
    superpotential and the finite FI-coordinate shift induced by vortex
    coefficient normalizations;
  - primitive mirror monomial selection from exact Coulomb matching, showing
    that higher connected harmonics spoil the branch identity
    `X_i(M_i)=M_i/(mu c_i)`;
  - vortex zero-mode filter: residual Berezin saturation, vanishing of the
    uninserted twisted `F`-term when extra residual zero modes remain, and
    removal of the two universal modes into the superspace measure;
  - single-vortex amplitude assembly: zero-mode removal before determinant
    formation, determinant-power bookkeeping, survival of the saturated
    twisted `F`-term zero-mode coefficient, vanishing with extra unsaturated
    zero modes, and the finite FI shift induced by the vortex coefficient;
  - one-vortex source-functional extraction: the zero-source component
    vanishes before the two universal Grassmann zero modes are projected into
    the twisted `F`-term measure; normalized source differentiation recovers
    the coefficient, nontrivial source overlaps change component amplitudes,
    and negative controls reject moduli-only, ghost-omitted, mirror-only,
    vacuum-scalar-only, determinant-only, and unsaturated residual-zero-mode
    shortcuts;
  - the finite one-vortex component-amplitude cell: exact retained-cell
    assembly with the oriented universal-zero-mode source minor, a
    primed-propagator contact term, a residual telescope, and negative controls
    rejecting norm-product pairing, orientation flips, contact omission,
    parallel-source saturation, mirror-coefficient bypass, and underbudgeted
    propagator residuals;
  - the single-vortex coefficient noncancellation bound: exact
    retained-window signed value, retained absolute mass, residual telescope,
    signed-window domination over determinant/zero-mode/boundary errors, a
    separate dual-frame `Z_map` residual budget, relative-error budget, and
    negative controls rejecting both
    omitted determinant residuals and symmetry-only nonzero claims under
    coherent signed cancellation;
  - the `P^{N-1}` mirror critical-point simplicity ledger and FI-transport
    check: the first CP root equation and degree-one residue trace use the
    transported `q_phys=exp(T) prod_i c_i`, while a stale bare `exp(T)` fails
    after vortex-determinant/operator coefficient rescaling;
  - the `P^{N-1}` mirror residue/quantum-product test: exact Hessian
    determinant, root-of-unity selection rule, `R(H^{N-1+dN})=q_phys^d`,
    off-selection vanishing, and the trace recurrence equivalent to
    `H^N=q_phys`;
  - the vortex-to-protected-observable proof-obligation map: exact residual
    telescope, underbudget negative control, rejection of bare-FI shortcuts
    that ignore finite vortex coefficients, and vanishing when the zero-mode
    gate is unsaturated;
  - the vortex-fugacity transmutation ledger: RG-invariant Coulomb scale,
    rejection of bare-FI and uncompensated-regulator-scale shortcuts, and the
    anomaly-free zero `mu`-power check;
  - the direct `P^{N-1}` degree-one stable-map quantum-product gate:
    virtual-dimension/codimension matching for
    `I_1(H,H^{N-1},H^{N-1})`, wrong-degree and lower-insertion negative
    controls, the unique-line/hyperplane-intersection count, and the finite
    quantum-product pairing check for `H * H^{N-1}=q`;
  - the degree-one vortex zero-mode/intersection model and proof-obligation template:
    exact determinant-line fugacity from finite spectra, incidence-orientation
    determinant, Berezin saturation, compactification-boundary exclusion,
    unit-hyperplane normalization, independently signed conditional residual
    propagation, off-pairing vanishing by zero-mode degree, and negative controls
    rejecting mirror-only, dimension-only, determinant-orientation,
    zero-mode-multiplicity, compactification, and hyperplane-normalization
    shortcuts;
  - the degree-`d` projective instanton iteration test: exact mirror residue
    and quantum-product traces for `R(H^{N-1+dN})=q_phys^d`, followed by a
    signed residual telescope for gluing, off-pairing, determinant, zero-mode,
    compactification, operator-map, and continuum errors; negative controls
    reject bare-FI powers, iterated line-count-only arguments, omitted gluing
    residuals, off-pairing leakage, and unsaturated zero-mode gates;
  - the degree-one A-model zero-mode measure bridge: the line count for
    `I_1(H,H^{N-1},H^{N-1})` is connected back to the finite-regulator
    A-twisted path integral through the vortex-normalized fugacity, the
    nonzero-mode determinant-line element, the Berezin top-degree filter, the
    vanishing obstruction space for convex `P^{N-1}`, and the orientation
    comparison.  This makes clear that the stable-map incidence count and the
    Hori--Vafa residue are protected evidence only after the same regulator
    supplies the instanton measure and fermion-zero-mode saturation.
  - the degree-one `P^{N-1}` Euler-sequence determinant-line check: computes
    the tangent zero modes from `H^0(O(1)^N)/H^0(O)`, verifies the Berezin
    selection degree, fixes the retained complex orientation, checks paired
    nonzero-mode determinant cancellation, and rejects forgetting the common
    rescaling, flipping the determinant orientation, or omitting an obstruction
    Euler factor;
  - the degree-one evaluation-form Berezin-Jacobian check: pulls the two point
    insertions and one hyperplane insertion back to the Euler-oriented zero-mode
    chart, computes the top wedge coefficient `+1`, and rejects duplicated
    evaluation forms, hyperplane normalization changes, orientation swaps, and
    missing forms;
  - the degree-one finite measure-scheme covariance test: exact transport of
    finite vortex-coefficient rescalings into the FI coordinate, retained-chart
    Jacobian cancellation between the collective-coordinate measure and the
    determinant/Berezin density, and negative controls for stale FI coordinates,
    missing inverse Jacobians, and untransported orientation signs.
  - the Hori--Vafa residue/direct-instanton comparison map: exact telescope
    comparing the mirror degree-one residue with the direct A-model/vortex
    coefficient, including transported FI coordinate, retained measure
    integral, vortex, operator, continuum, and off-pairing residuals; negative
    controls reject mirror-only zero-mode bypass, line-count-only fugacity,
    stale FI transport, and hidden determinant-orientation flips.
  - the cigar quotient metric coefficients after algebraic elimination of the
    gauge field.
  - the logarithmic-chiral vortex obstruction: a unit-norm charged section
    can exist smoothly only in zero flux, whereas an ordinary charged scalar
    can absorb flux through zeros.
  - the mirror-conjecture observable-boundary check: the named GLSM/Hori--Vafa and
    cigar/Liouville full-QFT conjectures list continuum, operator, spectral,
    defect, boundary, global, and contact-term data, while local dualization,
    Coulomb logarithms, vortex coefficients, mirror residues, stable-map
    incidence, quotient metrics, asymptotic dual variables, and vortex
    obstructions remain proper protected-evidence subsets.
  - the full-action/IR mirror data boundary: a superpotential-only package is
    checked to omit the mirror Kahler/D-term functional, measure, counterterms,
    global/orbifold data, noncompact boundary conditions, RG map,
    operator/state map, and spectral measure; a finite Legendre-domain cell
    checks the `Y+bar Y>0` singular boundary, a noncompact `D`-term
    boundary contribution, and a half-line Robin reflection phase showing that
    boundary data can change the continuous density while leaving the
    asymptotic `F`-term package intact; the same Robin datum is checked in a
    finite radial box where it shifts the Hamiltonian eigenmomenta and
    energies; a finite Schur-complement RG cell shows that high-mode
    Kahler/measure couplings shift both the retained Hamiltonian and source
    row, so Hamiltonian counterterms without source renormalization do not
    match low source-resolvent observables, and a two-source extension shows
    that matching one source normalization still leaves the mixed source
    metric wrong unless the full source-renormalization matrix is supplied; a
    finite background-response cell shows that matching the flat source metric
    and patching one probe with a local contact term still leaves a wrong
    stress-tensor/current row visible in a second mixed background-source
    kernel; a
    fake-Liouville shortcut with
    only the same F-term,
    asymptotics, and central charge is rejected without finite-field Kahler
    control, spectral measure, reflection amplitude, boundary conditions, and
    deformation classification.
  - the full-mirror operator/source obstruction: equal finite spectra and
    protected multiplication data are tested against different source-vector
    matrix elements, showing that source-normalized Euclidean two-point
    coefficients require operator topology and an operator/state map.
  - the cigar/Liouville spectral-data cell: exact arithmetic for
    `c=3+6/k`, noncompact `c_eff=3`, Liouville exponential marginality,
    asymptotic Liouville deformation filtering of integer periodic `F`-terms
    versus wall-domain spectral response, spectral-flow momentum/winding
    integrality, the noncompact field identification, rejection of
    metric-as-exact-QFT and rescaling-as-chiral-map shortcuts, the
    Hori--Kapustin local/global rigidity boundary, the
    pathwise fake-Liouville exclusion obligation comparing reflection phases, pole
    residues, boundary annuli, and source rows along a finite-regulator
    `kappa` path, and direct Gamma-function evaluation of the imported
    reflection target: continuous unitarity, `R(j)R(1-j)=1`, the positive
    `nu_+(k)` contribution to phase density, the `nu_raw(k)` sign ledger on
    intervals `(1/(n+1),1/n)`, sampled raw `k=1/n` normalization failures, and
    a sample simple-pole residue.  The source spectral-resolution bridge checks
    that the phase-density derivative is only a signed counting diagnostic and
    that finite-box normalization, positive Plancherel/source weights,
    normalizable bound-state masses, resonance continuation, and contact data
    enter Euclidean two-point observables.  The matrix spectral-measure
    completeness check uses a two-source Gram kernel where one source and one
    contact-patched heat-kernel probe agree while a second Euclidean test still
    detects the wrong positive Plancherel/source measure.
  - hypersurface adjunction signs, LG/sigma-model central-charge matching,
    residual finite-gauge invariant Jacobi monomial counting, and the
    Coulomb-coordinate singular-signal ledger.

## Figure Ledger

No figure is included in this pass.  Future figures should include GLSM
chambers, LG critical loci, and quotient diagrams for simple toric examples.

## Issue Links

- Advances #603 by expanding Landau-Ginzburg and GLSM content as intrinsic
  two-dimensional `N=(2,2)` QFT and by excluding string-theory mirror or
  compactification interpretations from the proof content.
- The 2026-05-31 GLSM/mirror pass advances the same issue by incorporating
  and deepening the stringbook Appendix K charged-chiral mirror and
  cigar/Liouville material, while recording the regulator-level vortex and
  full-QFT equivalence proof obligations explicitly.
- The 2026-05-31 hypersurface phase pass further deepens Appendix K's
  Calabi-Yau/Landau-Ginzburg chamber discussion with adjunction, central
  charge, finite-gauge, and Coulomb-coordinate derivations.
- The 2026-05-31 Fermat Wilsonian pass imports and sharpens Appendix K's
  nonrenormalization footnote into an explicit two-dimensional
  holomorphic-coordinate selection argument with calculation-check coverage.
- The 2026-06-03 Hori--Vafa scrutiny pass adds the finite-regulator
  one-vortex amplitude formula for the exponential term and records the
  recheck protocol for every Hori--Vafa-derived formula: vortex-number coupling,
  determinant ratio, universal and extra fermion zero modes, boundary
  behavior, and FI-coordinate normalization.  The follow-on all-rank
  normalization pass makes the shifted FI-theta coordinate explicit in both
  the mirror-torus constraints and the Coulomb-eliminated affine term, and
  checks the associated logarithm-branch theta periodicity.
- The 2026-06-07 Hori--Vafa one-loop branch pass strengthens the remaining
  sign/normalization chain by adding
  `rem:glsm-coulomb-one-loop-branch-monodromy` before the Coulomb critical
  equation.  The pass makes the determinant branch sheet, axial monodromy,
  compact `T` period, and physical fugacity `exp(T)` part of the local
  Coulomb calculation itself, before any historical Hori--Vafa formula is
  compared.
- The 2026-06-07 issue #847 determinant-sign re-audit corrects that branch
  pass: compact `T` periodicity tests integrality and `2 pi` normalization,
  but it cannot choose the determinant-log sign because both signs are
  integral-period transports.  The follow-up determinant/Fujikawa re-audit
  replaces the previous assignment-style companion with a convention-closed
  gamma-matrix, Hermitian Dirac-square, determinant-density, paired-fermion,
  finite-flux Wilson-overlap kernel, and heat-kernel model: the real
  sign comes from the complex-scalar determinant density after division by the
  signed analytic logarithm, while the theta partner comes from
  `Tr_reg gamma_*=-Q k` together with the mass-rotation generator
  `-gamma_*/2`.
- The 2026-06-07 issue #848 full-action/IR-universality pass reformulates the
  GLSM/Hori--Vafa and cigar/Liouville statements as IR equivalences of
  regulated QFTs, not equivalences defined by a twisted superpotential alone.
  It imports and rechecks the stringbook floor in the chapter's conventions:
  charged-chiral dual domains and induced-measure obligations, the
  quantum-corrected mirror `D`-term/Kahler boundary, the intermediate
  cigar-dual `D`-term action, cigar metric/dilaton representative versus exact
  coset data, spectral labels, reflection-amplitude normalization, and
  normalized Liouville action.  It remains a partial #848 repair: full
  finite-field Kahler control, exact spectral-measure/pole-residue matching,
  deformation rigidity, and boundary state/defect matching remain open.
- The 2026-06-03 projective-space residue pass extends that scrutiny from
  mirror critical points to a protected observable: it computes the finite
  Hessian/residue trace behind the `P^{N-1}` A-model selection rule and records
  the remaining physics inputs needed before using Hori--Vafa as a full QFT
  equivalence theorem.
- The 2026-06-03 vortex zero-mode filter pass advances the same physics-first
  instanton standard by separating the universal `d^2 theta_tilde` pair from
  residual fermion zero modes and proving the Berezin saturation criterion
  that decides whether the regulated vortex sector can generate a twisted
  superpotential term at all.
- The 2026-06-04 vortex-to-observable pass strengthens the architecture
  rather than adding another local identity: it connects the regulated
  vortex coefficient to the protected `P^{N-1}` A-model observable through an
  explicit residual telescope, registers the GLSM companion in the
  evidence-contract manifest, and adds adversarial checks for missing vortex
  coefficients, unsaturated zero modes, and underbudgeted comparison errors.
- The 2026-06-04 stable-map quantum-product pass adds the direct A-model side
  of the same comparison: the degree-one stable-map dimension and line-count
  calculation for `I_1(H,H^{N-1},H^{N-1})=1`, the resulting `H^N=q_phys`
  product computation, and finite checks rejecting mirror-only or dimension-mismatched
  shortcuts.
- The 2026-06-04 degree-one vortex observable repair pass replaces the circular
  assembly check with a finite zero-mode/intersection calculation: it derives
  the determinant-normalized fugacity, incidence orientation, Berezin
  saturation, compactification exclusion, and hyperplane normalization before
  leaving the full continuum comparison in a conditional proof-obligation map with
  adversarial controls.
- The 2026-06-04 vortex-fugacity pass scrutinizes the Hori--Vafa scale
  statement itself: the chapter now derives the RG-invariant rank-one
  combination of `mu`, the FI coordinate, and finite vortex determinant
  constants, and the companion rejects both bare-FI and uncompensated-`mu`
  shortcuts before a Coulomb root or mirror coordinate is treated as physical.
- The 2026-06-04 single-vortex noncancellation pass answers the instanton
  depth concern directly inside the two-dimensional GLSM lane: it upgrades
  the coefficient integral into a retained-window amplitude bound,
  requiring determinant-line orientation, zero-mode saturation, boundary
  control, and continuum comparison errors to be smaller than the signed
  one-vortex coefficient before the Hori--Vafa primitive term is used as a
  nonzero physical input.
- The 2026-06-04 comparison-map pass is an issue #755/#626 coherence repair:
  before the detailed Hori--Vafa formulas, the chapter now separates local
  dualization, Coulomb matching, vortex-amplitude construction, and protected
  observable comparison.  This keeps the reader-facing argument architecture
  ahead of the many finite checks and makes the physics-first instanton
  standard explicit without putting process directives in the TeX.
- The 2026-06-05 issue #806 conjecture-status pass names the abelian
  GLSM/Hori--Vafa mirror and cigar/Liouville mirror statements as central
  full-QFT conjectures.  It lists the global, spectral, operator, defect,
  boundary, continuum, background/contact-term, and singular-locus data those
  conjectures require, and recasts the existing local dualization, Coulomb,
  vortex, residue, stable-map, quotient-metric, and logarithmic-vortex
  calculations as protected evidence or conditional consequences.
- The 2026-06-05 vortex fluctuation-complex pass sharpens the physics-first
  instanton standard inside the Hori--Vafa lane: the chapter now displays the
  finite-regulator gauge/ghost/boson/fermion determinant complex behind
  `c_i`, and the companion script rejects raw zero-mode determinants, omitted
  ghost factors, and residual-zero-mode shortcuts before the primitive mirror
  monomial is treated as a protected amplitude input.
- The 2026-06-06 measure-scheme covariance pass re-audits the preceding
  projective-space observable bridge against finite normalization changes:
  the retained degree-one coefficient is invariant only when vortex
  coefficient rescalings, the FI coordinate, chart Jacobians,
  determinant/Berezin densities, and orientation/operator signs are transported
  as one package.  This keeps the Appendix K/Hori--Vafa formula from hiding a
  stale instanton-measure convention.
- The 2026-06-06 issue #597 Hori--Vafa cross-check pass adds a double-entry
  protected-observable comparison map: the projective-space mirror residue can be used
  only after it agrees, within explicit residual majorants, with the direct
  vortex/A-model coefficient in the same FI, determinant-line, zero-mode,
  operator, and off-pairing convention.  This is a physics-depth instanton
  pass: it checks the amplitude/observable assembly behind the Hori--Vafa
  formula rather than adding another moduli-space cell.
- The 2026-06-06 issue #597 one-vortex source-functional pass opens the local
  amplitude extraction behind the two-dimensional instanton coefficient:
  before the Hori--Vafa monomial is compared with observables, the chapter now
  distinguishes the twisted `F`-term projection, zero-source component
  vanishing, source-differentiated component amplitudes, source-to-zero-mode
  overlaps, primed propagator/determinant data, ghost density, and residual
  zero-mode gates.  This directly addresses the physics-depth concern that the
  instanton calculation is the fluctuation/source amplitude, not just the
  moduli chart.
- The 2026-06-06 issue #597 one-vortex component-amplitude pass turns the
  previous source-functional bridge into a finite worked component cell.  The
  chapter now displays the oriented zero-mode source minor, keeps the
  primed-propagator contact contribution separate from the protected vortex
  coefficient, and bounds the component residual.  The companion check rejects
  norm-product, orientation, contact-omission, parallel-source, mirror-only, and
  underbudgeted-propagator shortcuts.  This is amplitude/source physics, not a
  moduli-space or Hori--Vafa-authority pass.
- The 2026-06-06 issue #597/#725 source-frame calibration pass adds the next
  amplitude-facing guardrail in the same Hori--Vafa lane.  A reference
  one-vortex component amplitude now calibrates a target component only through
  the directly computed ratio of source-minor-plus-primed-contact integrals.
  The companion rejects mirror-fugacity-only calibration, zero-reference
  denominators, omitted contact terms, and parallel-source shortcuts, and the
  GLSM companion is promoted to an extended evidence contract with explicit
  convention tags.
- The 2026-06-06 issue #844 source-frame status re-audit demotes that
  calibration surface to `rem:glsm-one-vortex-source-frame-calibration-map`.
  The retained ratio is exact finite algebra; the physical amplitude estimate
  is conditional on separately supplied target, reference, and source-frame
  transport bounds in one regulator convention.
- The 2026-06-06 issue #844 GLSM/Hori--Vafa architecture pass rephrases the
  reader-facing entrance to the mirror comparison as an observable comparison
  map.  The chapter now states the physical question, the compared finite-data
  package, the direct vortex amplitude layer, the protected observable layer,
  and the remaining full-QFT proof debts before using a Hori--Vafa expression.
  The companion boundary check now rejects a mirror-residue-only comparison
  that bypasses the direct vortex data.
- The 2026-06-06 issue #626/#597 Hori--Vafa incidence re-audit strengthens
  the residue/direct-instanton comparison itself.  The companion no longer
  treats the retained direct measure integral as a chosen near-unit scalar:
  it computes the degree-one projective-space incidence orientation, selection
  degree, compactification gate, and operator normalization before adding the
  determinant-line/measure residual and comparing with the mirror residue.
  The TeX records the same direct determinant and gate data in the protected
  comparison block, while process notes remain in planning.
- The 2026-06-06 degree-`d` instanton iteration pass extends the projective
  observable bridge beyond the first instanton sector without replacing the
  direct A-model calculation by the Hori--Vafa root sum.  The chapter now
  states the degree-`d` residual telescope whose weighted terms include
  gluing, off-pairing, determinant-line, zero-mode, compactification,
  operator-map, and continuum comparisons, and the companion script checks
  that omitted gluing/off-pairing residuals, bare-FI powers, line-count-only
  products, and unsaturated zero-mode gates fail.
- The 2026-06-06 issue #597 Hori--Vafa frame/interaction repair splits the
  original GLSM vortex amplitude from its dual twisted-chiral image, and the
  2026-06-07 re-audit separates the FI-theta sector weight from the reduced
  coefficient `c_i`.  The original finite source functional carries the
  common numerical FI-theta vortex weight `q_top`, while `c_i` carries the reduced
  determinant/operator normalization used in `exp(T) prod_i c_i`.  The
  interaction layer is now the effective insertion `<exp(-V_int) P_bare>'`, so
  a source-independent vacuum factor is allowed only under an additional
  localization/factorization theorem.  The dual `exp(-Y_i)` appears only after
  the abelian dual operator map.  The companion adds exact negative controls
  for determinant-only coefficients, FI double counting, scalar-vacuum
  source-factorization shortcuts, and substituting the dual operator tag for a
  numerical original-theory amplitude.
- The 2026-06-07 issue #847 compact-flux convention pass rebuilds the
  Hori--Vafa lane around the monograph's own FI-theta normalization:
  `tau=theta/(2 pi)+i r` has period one, `T=2 pi i tau` has period
  `2 pi i`, and the physical fugacity is `q=exp(T)`.  The chapter now displays
  the component compact-flux convention, checks the flux-sector weight
  `exp((-2 pi r+i theta)k)`, restricts the mirror conjecture to dualizable
  phase-isometry data unless extra mirror input is supplied, records global
  gauge-form flux-lattice data, and replaces flavor-attached vortex sectors by
  a common gauge-flux sector with `i` only a disorder/source projection.  The
  companion rejects nonperiodic `exp(tau)` fugacities and flavor-labelled
  topological sectors under equal-charge flavor rotations.
- The 2026-06-07 issue #847 chiral-superpotential phase-isometry pass adds
  `constr:glsm-chiral-superpotential-phase-isometry-lattice` after the global-form
  lattice datum.  The pass shows that gauge invariance
  `sum_i p_Ai Q_i^a=0` does not imply preservation of the individual phase
  rotations used in abelian dualization.  The companion check uses the
  gauge-neutral monomial `P X_1 X_2` with charges `(1,1,-2)`, computes the
  preserved rank-two phase lattice, rejects full individual phase dualization,
  and requires explicit spurion or broken-isometry mirror data before the
  superpotential can be folded into a mirror presentation.
- The 2026-06-07 issue #847 twisted-`F` component bridge pass closes the
  remaining local-density normalization gap between the Coulomb determinant
  and the normalized twisted superpotential.  The chapter now records the
  `(2,2)` derivative algebra, ordered twisted Berezin measure, Wess--Zumino
  vector representative, `Sigma=bar D_+ D_- V` top component
  `D+iF_12`, component expansions of the FI and `-Q Sigma Y` terms, and the
  exact relation
  `(1/(2 pi)) Q log(|M|/mu) = (Q/(4 pi)) log(|M|^2/mu^2)`.  The companion
  rejects repeated `1/(4 pi)` density normalization, doubled-log
  holomorphic coefficients, and half-density `Sigma Y` compact-period
  shortcuts.
- The 2026-06-07 issue #847 common-flux source-projection pass tightens the
  physical operator-map boundary: the original rank-one flux event is one
  common gauge-bundle sector, while `i` labels a source/disorder projection.
  The chapter now distinguishes projected coefficients from a direct common
  observable amplitude, marks `exp(T) prod_i c_i^{Q_i}` as a mirror-coordinate
  assembly rather than a direct original-sector amplitude, and restricts the
  displayed product formulae to the ordinary `U(1)^s` flux lattice unless the
  `U(1)^s/Gamma` cocharacter, theta-character, dual-character, and residual
  mirror-orbifold data are propagated.  The companion adds finite negative
  controls for arbitrary projected coefficients and quotient-lattice shortcuts.
- The 2026-06-07 issue #847 common-flux operator-map diagnostic pass adds the
  missing finite comparison map after the source-projection paragraph.  It
  states that primitive mirror rows are not a continuum operator map unless an
  original-to-dual source transport, row-wise matrix-element comparison, flavor
  covariance, observable assembly row, and span residual are supplied.  The
  companion constructs two common source functionals with identical primitive
  projected coefficients and different observable amplitudes, rejecting the
  projected-product shortcut even when a one-point assembly fit exists.
- The 2026-06-07 issue #844/#847 operator-map status re-audit demotes
  `ca:glsm-common-flux-operator-map-diagnostic` to
  `rem:glsm-common-flux-operator-map-diagnostic`.  The text now says the
  residual inequality is a target estimate only after component bounds have
  been constructed in one source topology.  The companion adds a status guard
  rejecting promotion of residual slot names to a controlled estimate without
  those component bounds.
- The 2026-06-07 issue #844/#847 projective-instanton status re-audit demotes
  the degree-one A-model zero-mode bridge, finite measure-scheme covariance,
  Hori--Vafa residue/direct-instanton cross-check, and degree-`d` projective
  instanton iteration from `controlledapproximation` blocks to remarks.  Their
  residual telescopes and finite incidence/covariance checks remain, but they
  are explicitly comparison architecture until the determinant-line,
  zero-mode, compactification, operator-map, and continuum estimates are
  constructed in one regulator.  The theorem-form audit now rejects
  comparison/proof-obligation titles in the controlled-approximation
  environment.
- The 2026-06-07 issue #847 determinant-line follow-up adds the degree-one
  `P^{N-1}` Euler-sequence zero-mode quotient and companion finite check.  This
  is a genuine retained-window calculation of the direct A-model measure side,
  not a full continuum Hori--Vafa proof: it closes the common-rescaling,
  determinant-line-orientation, and paired-nonzero-mode cell while leaving the
  vortex-regulator limit and operator/source comparison as residual work.
- The 2026-06-07 issue #847 evaluation-form follow-up adds the degree-one
  `P^{N-1}` evaluation-form Berezin Jacobian.  The operator insertions now act
  on the fermion zero modes explicitly: the two point constraints and one
  hyperplane constraint have top wedge coefficient `+1` in the retained chart,
  while duplicated forms, rescalings, and orientation swaps change or kill the
  coefficient.  This deepens the direct instanton measure side without claiming
  the continuum vortex-regulator theorem.
- The 2026-06-07 issue #847 quotient global-form lattice pass makes that last
  boundary constructive.  The chapter now displays the cocharacter flux
  lattice, dual character lattice, FI-theta period lattice, and rank-one
  `U(1)/Z_n` obstruction.  The companion checks fractional quotient fluxes,
  forbidden cover-charge-one matter, enlarged FI periods, quotient-compatible
  `Sigma Y` periods, and residual mirror-orbifold order.
- The 2026-06-07 issue #847 vortex-normalization FI-character pass adds
  `prop:glsm-vortex-normalization-fi-character`.  Branch choices in
  `log c_i` now change `T^phys` by an explicit character
  `2 pi i sum_i n_i Q_i`, and the companion rejects the shortcut of testing
  this only on the covering lattice instead of on the actual compact flux
  lattice.
- The 2026-06-07 issue #848 cigar/Liouville re-audit corrects the endpoint
  architecture after the external review: the GLSM dual variable is explicitly
  kept twisted chiral until a separate mirror/T-duality automorphism is
  supplied; the cigar metric/dilaton is downgraded to a scheme-dependent
  sigma-model representative; exact finite-level data are assigned to the
  supercoset spectrum, field identification, reflection, measure, and sewing
  package; the ordinary-chiral Liouville action now includes the
  background-charge curvature/source coupling; and the Hori--Kapustin
  `kappa`-path is stated as a physical-continuity argument requiring global
  hypotheses beyond local rigidity.  The companion checks the same boundaries
  with finite negative controls.
- The 2026-06-07 reflection/spectral follow-up replaces symbolic
  reflection-factor cancellation in the GLSM companion with direct evaluation
  of the imported cigar reflection amplitude.  It verifies continuous-series
  unitarity and involution, extracts the positive `nu_+(k)` contribution to
  phase density, rejects the principal branch of negative `nu_raw(k)` below
  `k=1`, samples the raw special-level normalization failures at `k=1/n`, and
  checks a simple gamma-pole residue against the analytic residue formula.
  This is now evidence for finite consequences of the displayed target, not a
  derivation of the Liouville path integral normalization or the full
  continuous measure.
- The 2026-06-07 issue #848 noncompact `D`-term boundary pass adds a concrete
  half-line radial scattering diagnostic: a Robin wall parameter changes the
  reflection phase and continuous density while preserving unitary reflection
  and the same asymptotic `F`-term/central-charge package.  The chapter uses
  this to explain why finite-field Kahler/measure and boundary data are part
  of the cigar/Liouville QFT datum; the companion checks the boundary
  condition and phase-density dependence directly.
- The 2026-06-07 issue #848 admissible mirror spectral-domain pass turns the
  full datum interface into a cutoff-QFT admissibility condition and separates
  existence, universality, and duality claims.  It adds finite-volume Robin
  quantization to show that omitted wall/self-adjoint-domain data change
  regulated Hamiltonian energy levels, not only continuum phase-density
  bookkeeping.
- The 2026-06-07 issue #848 D-term RG Schur-complement pass adds
  `rem:glsm-mirror-dterm-rg-schur-obligation`: a finite Wilsonian high-mode
  elimination test in which two protected-equivalent mirror presentations have
  different retained Hamiltonians and source rows until the counterterm and
  source renormalization are transported together.  The companion checks the
  resulting source-resolvent observable and rejects Hamiltonian-only matching.
- The 2026-06-07 issue #848 source-metric D-term pass extends
  `rem:glsm-mirror-dterm-rg-schur-obligation`: with two source columns, the scalar
  normalization that matches one operator leaves the mixed low-energy source
  metric different.  The companion checks the mixed entry and verifies that
  matching the full finite source-renormalization matrix, not only the
  Hamiltonian or one source, is required before D-term changes are harmless for
  source-normalized correlators.
- The 2026-06-07 issue #848 operator/source pass adds
  `rem:glsm-mirror-operator-source-data` and a companion finite spectral
  obstruction: same Hamiltonian spectrum plus same protected multiplication is
  not enough to identify source-normalized local correlators.  This targets
  operator/state completeness rather than another protected Hori--Vafa
  residue identity.
- The 2026-06-07 issue #848 background-response pass adds
  `rem:glsm-mirror-background-response-obligation` and a companion finite
  mixed-kernel obstruction: the same flat source resolvent and protected
  source projection can still carry a different stress-tensor/current row, and
  a single local contact patch fails at a second Euclidean probe.  This makes
  background geometry, `R`-symmetry sources, flavor sources, and
  dilaton/background-charge couplings part of the full mirror-QFT datum.
- The 2026-06-07 issue #848 boundary/defect probe pass adds
  `rem:glsm-mirror-boundary-defect-obligation`: a finite cylinder-regulator
  comparison using boundary-state vectors, open-channel traces, Cardy residuals,
  defect operators, fusion residuals, and defect-twined traces.  The companion
  constructs protected-equivalent boundary and defect data that differ on
  annulus or twined-trace observables, rejecting protected-charge or
  protected-subspace shortcuts to the full topological sector map.
- The 2026-06-07 issue #848 pathwise fake-fixed-point pass adds
  `rem:cigar-liouville-pathwise-fake-fixed-point-obligation`: a finite-regulator
  continuity criterion for the Hori--Kapustin `kappa` route.  The companion
  constructs two protected-equivalent, locally rigid endpoints with equal
  finite energies but different reflection phases, pole residues, boundary
  annuli, and source rows, and rejects a discontinuous path that carries only
  protected endpoint labels.
- The 2026-06-07 issue #848 source spectral-resolution pass added
  `constr:cigar-liouville-source-spectral-resolution` as a QFT-observable
  bridge, but it initially overidentified the signed reflection phase density
  with a positive source measure.
- The 2026-06-07 issue #848 matrix spectral-measure pass added
  `constr:cigar-liouville-matrix-spectral-measure`: the spectral comparison is
  upgraded from one source two-point function to a positive matrix-valued
  Plancherel/source measure for local source families.
- The 2026-06-07 issue #852 spectral-theorem repair corrects both constructions:
  finite-volume `partial_s arg R` is now a signed counting/spectral-shift
  diagnostic, while the positive source measure is the weak limit of normalized
  finite-box source overlaps, equivalently a Plancherel/source Gram measure.
  Normalizable discrete states are separate positive energy masses; resonance
  poles live in analytic continuations of resolvents/correlators, not as
  Hilbert-space delta masses.  The companion now treats the old additive
  phase-density formula as a positivity-failing negative control and keeps the
  finite matrix check as a positive Gram-measure completeness test.
- The 2026-06-07 issue #848 asymptotic deformation-filter pass adds
  `constr:cigar-liouville-asymptotic-deformation-filter`: the text classifies
  integer `Y`-periodic Liouville `F`-term modes, identifies the primitive wall
  as the unique marginal nonconstant protected exponential, rejects fractional
  relevant modes without changed global data, and explains why `D`-term,
  boundary-domain, and source/contact deformations still require spectral
  response control.  The companion checks the mode weights, the dual-circle
  contribution, and the nonzero Robin wall response in the continuous density.
- The 2026-06-07 issue #847 gauge-covariant vortex-core repair replaces the
  earlier core block by `constr:glsm-vortex-core-disorder-datum`: the text
  defines the original disorder insertion as a punctured-disk
  principal-bundle/connection/section datum modulo gauge, distinguishes smooth
  extendable cores from singular holonomy defects, derives the dual
  `exp(-Y_i)` orientation from the excised-disk first-order boundary term, and
  treats equal-charge labels as flavor/source rows rather than topological flux
  sectors.  The companion checks large-gauge invariance, finite core energy,
  singular-holonomy negative controls, projective flavor-row covariance, and
  the core-domain and boundary-term residual budgets.
- The 2026-06-07 issue #851 stable-map contact repair replaces the previous
  Boolean compactification/contact formula by
  `ex:cpn-degree-one-representative-independence-gate`.  The TeX now states
  the primary invariant as the evaluation-class pairing on
  `Mbar_{0,3}(P^{N-1},1)`, explains that coincident or non-transverse
  representatives require deformation or refined/excess intersection rather
  than an added indicator boundary term, and confines contact constants to
  separately declared collision-sensitive source observables.  The companion
  now treats the old indicator arithmetic as a failing negative control.
- The 2026-06-07 issue #847 CP critical-coordinate transport pass updates the
  first `P^{N-1}` Hori-Vafa critical-point example so the algebraic torus uses
  `hat X_i=c_i exp(-Y_i)` and `q_phys=exp(T) prod_i c_i` from the start.  This
  keeps the root equation, the degree-one residue trace, and the later
  quantum-product check in the same transported determinant/operator
  normalization.  The companion adds an exact negative control in which the
  formal root count remains unchanged but a stale bare `exp(T)` moves the root
  product and the protected degree-one trace.
- The 2026-06-08 issue #847 compact-fugacity residue pass tightens
  `rem:cpn-hv-residue-instanton-cross-check`: `q_mir` is now explicitly the
  mirror image of the same compact FI character as `q_Lambda`, with
  `delta T_q` measuring the transported same-line mismatch.  The companion
  rejects stale bare mirror fugacities, period-one `exp(tau)` drift under a
  theta period, and omitted `q`-transport residuals in the degree-one
  residue/direct-instanton comparison.
- The 2026-06-09 issue #965 electric-flux pass restores the Hamiltonian
  mechanism behind the theta lift of the asymptotic Coulomb region.  Re-audit
  note: the addition is intentionally placed after the hypersurface
  Coulomb-coordinate paragraph so the chapter reads as a sequence of distinct
  mechanisms--D-term chambers, protected one-loop coordinate, compact
  electric-flux energy, and only then IR-equivalence status--rather than as
  another local Hori--Vafa-derived identity.  The finite companion checks the
  shifted rotor Hamiltonian and the requested negative controls for
  noncompact holonomy, wrong quotient theta period/lattice, and omitted
  charged screening.
