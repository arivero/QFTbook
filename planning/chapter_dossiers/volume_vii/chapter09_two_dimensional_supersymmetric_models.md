# Chapter 09: Two-Dimensional Supersymmetric Models

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
- `q_mir`, `I_{Lambda,1}`, `B_vort`, `B_I`, `B_q`, `B_off,a`:
  mirror-residue FI coordinate, retained finite degree-one instanton-measure
  integral, and residual majorants in the Hori--Vafa residue/direct-instanton
  comparison map.
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
  `C_spec`, `C_bdry`: named full-QFT cigar/Liouville mirror conjecture and
  the protected-data/proof-debt lanes separating quotient/dualization/vortex
  checks from spectral-flow, continuous-spectrum, defect, and boundary data.
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
  regulator, phase chamber, singular-locus exclusions, continuum Hilbert
  spaces/Hamiltonians, local OPEs, A/B sectors and pairings, defects,
  boundaries, topological sectors, contact terms, and RG endpoints.  The
  chapter now separates this full-QFT statement from the protected evidence
  lanes `D_loc`, `D_pert`, `D_vort`, and `D_obs`, and from the proof-debt
  lanes `E_cont`, `E_op`, `E_top`, `E_bg`, and `E_sing`.
- Derives the first-order charged-chiral dualization with real superfield
  `B_i`, twisted-linear constraint, Legendre elimination, and the
  superspace integration-by-parts identity producing the linear
  `-Q_i^a Sigma_a Y_i` twisted `F`-term.
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
  saturation, and collective-coordinate integration; the dual frame supplies
  the operator `exp(-Y_i)`.  This makes the Hori--Vafa exponential term a
  rechecked amplitude datum in the chapter's conventions rather than a scalar
  inserted into the original path integral.
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
- Adds the compact FI-theta normalization ledger: with
  `k=(2 pi)^{-1} int F`, `tau=theta/(2 pi)+i r`, and
  `T=2 pi i tau=-2 pi r+i theta`, a flux-`k` saddle carries
  `q^k=exp(T k)`, invariant under `theta -> theta+2 pi`.  The old
  `exp(tau)` fugacity is explicitly ruled out.
- Rebuilds the one-vortex notation around the common gauge-bundle flux:
  the flux-one sector is not attached to a flavor label.  The index `i` labels
  a dual disorder/source projection to `exp(-Y_i)`, while the original GLSM
  flux weight is the common `q_top`.
- Extends the vortex-normalization/FI-coordinate comparison to all abelian
  ranks: normalized mirror-torus variables `hat X_i=c_i exp(-Y_i)` move the
  constants into `T_a^phys=T_a+sum_i Q_i^a log c_i`, and the same shift is
  checked against the Coulomb affine term, with logarithm-branch changes
  identified as integral `2 pi i` shifts of the logarithmic FI coordinate.
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
  vortex coefficient, determinant-line orientation, and A-twisted
  compactification/contact data are fixed.
- Adds the vortex-to-observable residual comparison: the regulated
  `P^{N-1}` A-twisted correlator is compared to the mirror residue through
  separate coefficient, determinant, zero-mode, compactification/contact,
  gluing, operator-map, and continuum residuals.  The chapter now makes the
  nonzero vortex coefficient and the vanishing of those residuals the
  load-bearing physics inputs before the finite Hori--Vafa residue identity is
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
- Adds the finite measure-scheme covariance test for that same degree-one
  observable: rescaling the supplied vortex coefficients must be accompanied by
  the inverse FI-coordinate shift, and changing the zero-mode chart density
  must transport the inverse Jacobian through the nonzero-mode/Berezin density.
  The retained coefficient is invariant only for the full package
  `q_Lambda * int Omega_{Lambda,1}`; stale FI coordinates, missing Jacobians, or
  untransported orientation signs are treated as real coefficient changes.
- Adds the Hori--Vafa residue/direct-instanton comparison map for the
  degree-one `P^{N-1}` product: the mirror residue `S_1(q_mir)` is compared
  against the direct A-twisted coefficient only through the transported vortex
  fugacity `q_Lambda`, the retained instanton-measure integral
  `I_{Lambda,1}`, FI-coordinate transport, operator/continuum residuals, and
  off-pairing bounds.  The direct side now also exposes the finite
  degree-one incidence determinant `+1`, insertion-degree gate, and
  compactification exclusion before the residual `I_{Lambda,1}-1` is
  budgeted.  This prevents the protected root sum, the stable-map line count,
  or the Coulomb normalization check from standing in for the regulated vortex
  measure and zero-mode calculation.
- Derives the classical cigar quotient metric by solving the auxiliary
  constraint, gauge fixing the logarithmic chiral scalar, and eliminating the
  gauge field.
- Develops the cigar/Liouville mirror chain as a QFT comparison problem:
  dual variables `Y,Y_P`, the single exponential from the ordinary charged
  chiral multiplet, the finite topological obstruction to a smooth
  finite-action logarithmic-chiral vortex exponential,
  the `Y+Y_P=0` vector constraint, the resulting `N=2` Liouville
  superpotential, and the theorem-status boundary for full equality with the
  cigar coset QFT.
- States the named cigar/Liouville mirror QFT conjecture with level and
  background-charge conventions, spin structures, spectral-flow sectors,
  normalizable states, nonnormalizable sources, continuous-spectrum measure,
  local operator map, reflection amplitudes, Hilbert space, superconformal
  generators, defects, boundaries, and contact terms.  The quotient metric,
  asymptotic dualization, ordinary chiral exponential, and logarithmic-vortex
  obstruction are recorded as `C_cl`, `C_dual`, and `C_vort` evidence, while
  spectral/completeness and defect/boundary matching remain `C_spec` and
  `C_bdry` obligations.
- Defines abelian GLSM data with fields, integer charges, invariant
  superpotential, complexified FI-theta coordinate, gauge coupling, and
  regulator.
- States the axial anomaly charge sum as a finite ledger and a necessary
  condition, not a conformality proof.
- States the abelian GLSM Coulomb-branch one-loop determinant hypotheses,
  including logarithm branches, regulator scheme, and exclusion of
  boundary/vortex/singular-locus contributions from the local determinant,
  and then derives the perturbative local determinant contribution from the
  proper-time subtracted massive propagator plus the axial-anomaly phase that
  completes the holomorphic logarithm.
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
    its finite FI-coordinate shift under determinant normalization changes.
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
  - the `P^{N-1}` mirror critical-point simplicity ledger;
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
