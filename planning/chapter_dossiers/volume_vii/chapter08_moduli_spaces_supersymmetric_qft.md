# Chapter 08: Moduli Spaces In Supersymmetric Quantum Field Theory

## Source Position

Volume VII now separates supersymmetric vacuum spaces from the earlier exact
Wilsonian dynamics.  The chapter supplies moduli-space definitions before the
later lower-dimensional examples, protected sectors, and localization.

## Notation Inventory

- `Phi^i`, `W`, `F_i`, `mu`: chiral fields, superpotential, F-term equations,
  and moment map.
- `V`, `G_C`, `Z_F`, `I_F`: scalar representation, complexified reductive
  gauge group, F-flat locus, and F-term ideal.
- `M_cl`: classical Kahler or holomorphic quotient vacuum space.
- `M_ch,cl`, `M_mu,cl`: affine chiral quotient and symplectic vacuum
  quotient.
- `M`, `H_p`, `A_p`, `G_p`: quantum moduli space, Hilbert space, local
  operator algebra, and background response in vacuum `p`.
- `mathfrak M`: full quantum supersymmetric moduli-space datum, consisting of
  the stratified reduced vacuum space, holomorphic branch-coordinate sheaf,
  Hilbert spaces, low-energy operator algebras, branch EFT data, and
  background-response data.
- `O_M^hol`: holomorphic coordinate sheaf of a branch, generated where valid
  by protected chiral expectation values.
- `E_p`: effective branch data in vacuum sector `p`, including massless
  fields, metric, Wess-Zumino terms, superselection sectors, and domain of
  validity.
- `R_ch`, `ev_p`: chiral ring and evaluation homomorphism at a vacuum.
- `F`, `T`, `Lambda_QFT`, `W_F`: compact internal global symmetry, selected
  torus, allowed charge lattice after global-form/anomaly data, and Weyl
  group quotient used to label nonabelian fixed-charge sectors.
- `j_A^mu`, `Q_A`, `q_A`, `Hilb_q`: conserved currents, torus charge
  operators, fixed charge vector, and the corresponding joint charge sector.
- `mu^A`, `H_mu`: chemical potentials and the Hamiltonian variational
  operator \(H-\mu^AQ_A\).
- `K_A`, `M_gap(p)`, `L_br`, `E_EFT(q,R)`: branch isometry vector fields,
  transverse mass scale of the branch EFT, branch Lagrangian evaluated on a
  homogeneous charge orbit, and fixed-charge energy computed by the
  constrained Routhian/Legendre transform.
- `X`, `Y`, `lambda`, `n`, `rho`, `omega`: supersymmetric chiral-branch model
  used for the fixed-charge example, with \(W=(\lambda/2)XY^2\), branch
  coordinate \(X\), transverse field \(Y\), charge unit, branch radius, and
  physical phase frequency.
- `Wightman-type data`: local operator-valued distributions, Hilbert spaces,
  vacuum sectors, correlation distributions, spectrum, locality, and
  covariance.
- `Kontsevich-Segal-type data`: geometric amplitudes, boundary state spaces,
  sewing maps, reflection pairings, and background-field dependence.
- `Q^a_i`, `tilde Q_a^i`, `M^i_j`: SQCD quarks, antiquarks, and mesons.
- `P_a^I`, `V^{IJ}`: \(SU(2)\), \(N_f=2\) doublet fields and antisymmetric
  meson/baryon Plucker coordinates.
- `Pf(V)`: Pfaffian
  \(V^{12}V^{34}-V^{13}V^{24}+V^{14}V^{23}\) for the \(SU(2)\),
  \(N_f=2\) quotient.
- `eq:su2-nf2-classical-plucker-hypersurface`: classical \(SU(2)\),
  \(N_f=2\) SQCD quotient as the Pfaffian/Plucker hypersurface.
- `eq:su2-nf2-quantum-deformed-pfaffian`: Wilsonian quantum-deformation
  input for the \(SU(2)\), \(N_f=2\) branch; the subsequent algebraic
  consequences are written in prose rather than as a theorem-family claim.
- `eq:su2-nf2-massive-vacua`: two isolated vacua after a nondegenerate
  antisymmetric mass deformation of the \(SU(2)\), \(N_f=2\) branch.
- `eq:su2-nf2-massive-superpotential-values`: corresponding superpotential
  values after solving the constrained \(F\)-term equations.
- The quantum-deformation calculation uses
  \(\operatorname{Pf}(V)=\Lambda_h^4\), including smoothness and the
  diagonal-mass two-vacuum check.
- `m_1`, `m_2`, `X`: diagonal mass-source parameters and the Lagrange
  multiplier used to impose the quantum-deformed Pfaffian constraint.
- `Lambda_0`: pure \(SU(2)\) holomorphic scale after the nondegenerate
  antisymmetric mass deformation, with
  \(\Lambda_0^6=m_1m_2\Lambda_h^4\).
- `M_H`, `mu_R`, `mu_C`: hyperkahler quotient and real/complex moment maps.
- `g_{i bar j}`: branch metric in the low-energy effective action.
- `q_i`, `tilde q_i`: rank-one \(U(1)\) hypermultiplet coordinates with
  charges \(+1\) and \(-1\).
- `z_i^(a)`, `p_i^(a)`: local base and cotangent coordinates on the
  \(q_a\neq0\) patch of the rank-one hyperkahler quotient.
- `zeta`: positive real FI parameter in the rank-one hypermultiplet model.
- `Theta`: holomorphic cotangent one-form \(\sum_i\tilde q_i\,dq_i\).
- `prop:n2-rank-one-hyperkahler-quotient`: explicit construction of the
  rank-one \(U(1)\) hypermultiplet Higgs branch as
  \(T^\ast\mathbb P^{N-1}\), including dimension, local coordinates, moment
  map solving, and one-form descent.
- `hyp:smooth-higgs-branch-metric-protection`: theorem-boundary input for
  smooth-stratum metric protection in eight-supercharge Lagrangian theories.
- `Delta S_H^(2)`, `Delta g_mn(q)`: local two-derivative Higgs-branch metric
  counterterm test on a smooth fully Higgsed stratum.
- `eq:higgs-branch-protected-quotient-metric`: local quotient-metric equality,
  explicitly separated from global nonperturbative continuum assertions.
- `constr:higgs-branch-background-field-derivation-target`,
  `eq:higgs-branch-background-field-trace-log`: explicit rank-one
  background-field target for an actual Higgs-metric determinant calculation.
- `ex:higgs-branch-rxi-determinant-split`,
  `eq:higgs-branch-rxi-gauge-vector-split`,
  `eq:higgs-branch-rxi-xi-sector-cancellation`: constant-background
  \(R_\xi\) determinant split deriving the longitudinal-vector, Goldstone, and
  ghost gauge-parameter cancellation before the tangent-vertex calculation.
- `ex:higgs-branch-frame-connection-seagull`,
  `eq:higgs-branch-frame-connection-seagull-identity`: generated
  seagull/double-insertion cancellation for the pure moving-frame part of the
  heavy Higgs fluctuation determinant.
- `ex:higgs-branch-mass-curvature-ward-pair`,
  `eq:higgs-branch-mass-curvature-ward-pair`: determinant-level \(X,Y\) vertex
  pairing test for mass-curvature, Yukawa/connection, and auxiliary-contact
  contributions after the pure moving-frame part has been removed.
- `ex:higgs-branch-supercharge-factorization`,
  `eq:higgs-branch-supercharge-factorized-operators`,
  `eq:higgs-branch-supercharge-factorized-vertices`,
  `eq:higgs-branch-supercharge-factorized-supertrace`: off-shell heavy
  \(Q\)-complex mechanism generating the paired second-variation vertices and
  their determinant cancellation on the regulated nonzero spectrum.
- `ex:higgs-branch-off-shell-row-completion`,
  `eq:higgs-branch-row-completed-heavy-map`,
  `eq:higgs-branch-row-completed-bosonic-vertices`,
  `eq:higgs-branch-row-completed-fermionic-seagull`,
  `eq:higgs-branch-row-contact-residual`: row-resolved construction criterion
  for obtaining the Higgs heavy \(Q\)-complex from kinetic, gauge-fixing,
  moment-map auxiliary, and Yukawa pieces of the quadratic Lagrangian.
- `ex:higgs-branch-dimensional-reduction-row-audit`,
  `eq:higgs-branch-reduced-scalar-row-contact`,
  `eq:higgs-branch-reduced-scalar-contact-residual`,
  `eq:higgs-branch-d-dimensional-balance-diagnostic`: dimensional-reduction
  audit separating \(d\)-dimensional connection modes from reduced
  vector-multiplet scalar rows and their contact residuals.
- `eq:higgs-branch-heavy-multiplet-balance-heuristic`: signed
  four-dimensional long-multiplet balance, retained only as a diagnostic for
  missing sectors after the Ward identity or trace-log calculation has supplied
  the real pairing.
- `K`, `W`, `Q_1`, `Q_5`: vector spaces and ranks in the two-dimensional
  \(\mathcal N=(4,4)\) ADHM/D1--D5 gauge-theory example.
- `B_1`, `B_2`, `I`, `J`: adjoint and fundamental hypermultiplet scalars in
  the ADHM/D1--D5 example.
- `eq:d1-d5-adhm-complex-moment`,
  `eq:d1-d5-adhm-real-moment`, and
  `eq:d1-d5-adhm-higgs-quotient`: complex moment map, real moment map, and
  Higgs-branch quotient for the \(\mathcal N=(4,4)\) ADHM gauge theory.
- `rem:d1-d5-coulomb-throat-higgs-bridge`: intrinsic QFT bridge datum between
  the D1--D5 gauge theory and the symmetric-product CFT tangent, separating
  protected Higgs metric data from the quantum-corrected Coulomb throat,
  torsion flux, positive-FI lifting, operator-map, and global CFT
  identification obligations.
- `eq:d1-d5-coulomb-throat-metric-flux`: rank-one Coulomb branch metric and
  torsion package \(h(r)=h_\infty+Q_5/(2r^2)\), \(H=-\ast_4dh\).
- `eq:d1-d5-coulomb-hflux-quantization`: harmonicity away from the origin and
  normalized \(S^3\) flux \(Q_5\).
- `eq:d1-d5-positive-fi-coulomb-lift-bound`: trace lower bound showing that a
  positive FI parameter lifts the empty-framing Coulomb vacuum.

## Claim Ledger

- Defines classical supersymmetric vacuum equations and quotient data.
- States the precise affine chiral quotient and symplectic quotient data and
  proves their coordinate-ring comparison under explicit Kempf-Ness
  hypotheses.
- Works out the rank-one abelian quotient
  `C[x,y]^{C^*}=C[xy]` and its moment-map quotient, fixing the quotient
  convention used later in rank-one gauge-theory examples.
- Defines the quantum supersymmetric moduli-space datum as a stratified
  family of supersymmetric vacuum sectors with holomorphic coordinate sheaf,
  Hilbert spaces, low-energy operator algebras, branch EFT data, and
  background-response/anomaly data.
- Relates chiral rings to holomorphic functions under explicit separation and
  reducedness hypotheses.
- Adds the fixed-charge/large-charge probe of a branch: defines charge
  sectors by a selected torus, global-form/anomaly-restricted charge lattice,
  and Weyl orbit; fixes chemical-potential conventions, homogeneous charged
  saddles on the cylinder, the Noether map, and the constrained
  Routhian/Legendre transform from branch EFT data to fixed-charge energy.
- States the stability and control hypotheses for branch fixed-charge EFT:
  susceptibility positivity, transverse fluctuation positivity, gauge/Gauss
  constraints, zero-mode quantization, multiple-saddle comparison, and a
  demonstrated scale hierarchy.  Separates the generic non-BPS large-\(\mu\)
  window \(R^{-1}\ll|\mu|\ll M_{\rm gap}\) from protected supersymmetric
  branch examples where \(\mu R=O(1)\) but \(M_{\rm gap}R\to\infty\).
- Works a supersymmetric chiral-branch example with
  \(W=(\lambda/2)XY^2\), charge lattice \(q=nJ\), cylinder saddle
  \(X=\rho e^{i\omega t}\), Noether map \(q=2n\omega V_R\rho^2\),
  fixed-charge energy \(E=q/(nR)\), transverse multiplet gap
  \(M_Y=|\lambda|\rho\), fluctuation spectrum, and explicit branch window.
- States the conformal bridge precisely: via the state-operator theorem,
  large-charge local operators of definite scaling dimension encode
  fixed-charge energy eigenstates, so the Hellerman large-charge expansion
  supplies asymptotic charged-sector information about the branch EFT rather
  than a full construction of the quantum vacuum datum.
- Reframes Open Problem 93.3 as a special supersymmetric test case of the
  larger reconstruction problem from Wightman-type local QFT data to
  Kontsevich-Segal-type geometric amplitude and sewing data.
- Records `N=1` SQCD branch behavior and `N=2` Coulomb/Higgs/mixed branch
  structures, while explicitly marking the SQCD table as an orientation
  ledger rather than a proof.
- Derives the classical \(SU(2)\), \(N_f=2\) SQCD quotient
  \(\mathcal M_{\mathrm{ch},\mathrm{cl}}\simeq
  \{\operatorname{Pf}(V)=0\}\subset\bigwedge^2\mathbb C^4\), with explicit
  doublet coordinates, Pfaffian convention, converse reconstruction on a
  nonzero Plucker chart, and dimension check.
- Separates the Wilsonian quantum-deformation input
  \(\operatorname{Pf}(V)=\Lambda_h^4\) from its algebraic consequences, then
  derives smoothness for \(\Lambda_h\neq0\), reduces a nondegenerate
  antisymmetric mass matrix to Darboux form, solves the constrained
  \(F\)-term equations, and matches the two superpotential values to pure
  \(SU(2)\) by holomorphic threshold scale matching.
- Proves the rank-one \(\mathcal N=2\) hypermultiplet quotient
  \(\{\mu_C=0,\mu_R=\zeta\}/U(1)\simeq T^\ast\mathbb P^{N-1}\) for
  \(\zeta>0\), including the elementary real-moment representative,
  local cotangent coordinates, and preservation of the canonical holomorphic
  one-form on overlaps.
- Replaces the vague protected-Higgs-metric sentence by a scoped
  theorem-boundary input: local Wilsonian protection is tied to eight
  supercharges, a smooth completely-Higgsed stratum, a transverse mass gap, and
  absence of mixed/additional massless sectors.  The counterterm filter
  classifies coordinate changes, FI/mass transport, vector/coupling-spurion
  \(D\)-terms, torsion/WZ terms, and singular/mixed-locus operators.  The
  rank-one background-field construction specifies the trace-log coefficient,
  nonminimal gauge operator, Goldstone, ghost, seagull, fermion, auxiliary, and
  gauge-parameter data that an independent determinant proof would have to
  evaluate.  It further records the row-resolved off-shell assembly obligation
  for the heavy \(Q\)-complex, including the trace-log residual caused by
  dropping a gauge-fixing, auxiliary, or Yukawa square-completion contact.  The
  old massive-multiplet balance is retained only as a diagnostic consistency
  check.  Global nonperturbative equality is retained only as an additional
  continuum assertion after boundary and extra-light-sector exclusions.
- Adds the two-dimensional \(\mathcal N=(4,4)\) ADHM/D1--D5 gauge-theory
  example with adjoint and fundamental hypermultiplets, explicit complex and
  real moment maps, quotient, dimension count
  \(\dim_{\mathbb R}\mathcal M=4Q_1Q_5\), and the QFT interpretation of the
  protected two-derivative Higgs-branch sigma-model metric.
- Adds the D1--D5 QFT bridge beyond the ADHM endpoint: the rank-one Coulomb
  branch has a one-loop harmonic \(r^{-2}\) metric coefficient, quantized
  torsion flux, and an infinite logarithmic throat, while positive FI data
  lift the empty-framing Coulomb locus by a trace lower bound.  The bridge to
  the symmetric-product CFT is explicitly conditional on throat decoupling,
  torsion/\(B\)-field data, a normalizable operator map to the blow-up tangent,
  and global CFT identifications; dimension matching is kept as a necessary
  check rather than a proof.
- Records boundary cases: the \(\zeta=0\), \(I=J=0\), commuting-\(B\) locus
  meets small-instanton/Coulomb directions and invalidates the smooth-stratum
  sigma-model closure; Coulomb-branch vector-multiplet metrics can receive
  quantum corrections and are not determined by the Higgs quotient.
- Identifies singularities as loci where the low-energy theory changes and
  records the domain of validity of branch effective actions.

## Calculation Checks

- `calculation-checks/susy_moduli_space_checks.py` verifies the rank-one
  abelian invariant-ring calculation, the matching real/complex quotient
  dimension count, F-term ideal equivariance for an invariant
  superpotential, and the rank-one hyperkahler quotient dimension, one-form
  descent, and cotangent transition algebra for \(T^\ast\mathbb P^{N-1}\),
  the two-dimensional \(\mathcal N=(4,4)\) ADHM/D1--D5 dimension ledger and
  positive-FI exclusion of the \(I=J=0\) boundary,
  the rank-one D1--D5 Coulomb harmonic metric coefficient, normalized
  \(H\)-flux, logarithmic radial throat floor, positive-FI Coulomb-lift trace
  bound, and the negative control that equal Higgs-branch dimension does not
  fix Coulomb-throat flux,
  the Higgs-metric theorem-boundary/local/global/torsion status matrix, the
  two-derivative counterterm filter with vector-spurion negative control, and
  the background-field derivation check that rejects bare component
  multiplicities, requires model/gauge/regulator/operator slots, derives the
  \(R_\xi\) longitudinal/Goldstone/ghost cancellation from generated operators,
  verifies the frame-connection seagull identity from operator conjugation,
  checks Ward-paired mass-curvature vertices with a mismatched-vertex negative
  control, checks supercharge-factorized heavy-block pairing with a
  dropped-contact negative control, checks row-resolved off-shell heavy-complex
  assembly with a missing auxiliary/Yukawa contact negative control, and rejects
  use of the four-dimensional gauge-field entry in dimensionally reduced
  arguments by checking reduced vector-scalar row contacts and the separate
  two-dimensional antisymmetric \(B/WZ\) channel,
  fixed-charge branch-EFT checks for global-form/Weyl charge labels, the
  supersymmetric chiral-branch Noether map and Routhian energy, transverse
  gap hierarchy, and the abstract large-\(\mu\) simultaneous-window scaling
  condition,
  together with the \(SU(2)\), \(N_f=2\) Pfaffian/Plucker identity,
  converse reconstruction chart, quotient dimension ledger, nonzero
  quantum-deformation smoothness test, diagonal-mass two-vacuum algebra, and
  holomorphic threshold scale matching.

## Figure Ledger

No figure is included in this pass.  Later figures should show the quotient
construction, SQCD branch cases, and the `N=2` Coulomb branch with singular
local models.

## Audit Notes

- 2026-05-30 anti-wrapper pass: demoted the classical \(SU(2)\), \(N_f=2\)
  Pfaffian/Plucker quotient from proposition/proof form to derivation prose.
  The invariant-theory calculation, converse chart, quotient dimension count,
  and convention definitions are retained.
- 2026-05-30 follow-up anti-wrapper pass: demoted the quantum-deformation
  algebra block from lemma/proof form as well.  The nonperturbative content is
  the Wilsonian input \(\operatorname{Pf}(V)=\Lambda_h^4\); smoothness,
  Darboux reduction, the two-vacuum solution, and threshold matching are
  finite algebraic consequences and are now presented as such.
- 2026-05-30 moduli-construction clarification: expanded Open
  Problem~93.3 so it explicitly distinguishes chiral-ring reconstruction of
  reduced holomorphic coordinates from fixed-charge/large-charge
  reconstruction of asymptotic branch EFT data.
- 2026-05-30 Wightman-to-KS refinement: sharpened Open Problem~93.3 so the
  moduli-space datum is treated as an output of the structural passage from
  local Wightman data to KS-style boundary/sewing/amplitude data.
- 2026-06-04 Higgs-branch protection pass: separated intrinsic metric
  protection from coordinate representatives and from bare hyperkahler
  quotient geometry, added the smooth-stratum Wilsonian status ledger,
  developed the \(\mathcal N=(4,4)\) ADHM/D1--D5 QFT example, and added finite
  checks for the dimension/FI-boundary arithmetic.
- 2026-06-05 issue #808 large-charge branch-EFT pass: replaced the formal
  commuting-charge setup by a torus/global-form/Weyl charge-sector ledger,
  derived the Noether/Routhian conventions with WZ/background/gauge
  caveats, stated the nonempty simultaneous-window hypothesis, and added a
  worked supersymmetric chiral-branch example showing the distinction
  between protected fixed-charge control and a generic non-BPS large-\(\mu\)
  expansion.
- 2026-06-07 issue #849 Higgs-metric nonrenormalization pass: converted the
  previous assertion into a local Ward/counterterm mechanism, separated
  \(4d\ \mathcal N=2\), \(3d\ \mathcal N=4\), and
  \(2d\ \mathcal N=(4,4)\) theorem boundaries, added a background-field
  massive-multiplet determinant cancellation, and preserved the boundary that
  quotient evidence is not a global continuum proof.
- 2026-06-07 issue #594 D1--D5 QFT bridge pass: added the rank-one Coulomb
  throat metric/torsion package, positive-FI Coulomb-lift bound, and explicit
  bridge obligations to the symmetric-product blow-up tangent.  The pass keeps
  ADHM dimension, protected Higgs metric, Coulomb continuum, torsion flux, and
  IR CFT operator-map data separate.
- 2026-06-07 issue #850 Higgs-metric background-field audit: demoted the
  \(4+2+4-2-8\) cell from determinant proof to long-multiplet balance
  diagnostic, introduced the smooth Higgs-branch protection hypothesis and the
  rank-one trace-log derivation target, and updated the companion so component
  multiplicities are rejected unless model, gauge, regulator, generated
  operators, vertices, seagulls, ghosts, Goldstones, gauge-parameter
  cancellation, and dimension-reduction slots are present.
- 2026-06-07 issue #850 \(R_\xi\) determinant split pass: added the
  constant-background vector projector factorization and derived the
  longitudinal-vector/Goldstone/ghost cancellation from the gauge-fixed
  operators.  The companion now generates the dimension-specific spectrum and
  determinant weights from field type and mode count instead of accepting a
  hand-entered cancellation ledger.
- 2026-06-07 issue #850 frame-connection seagull pass: added the pure
  moving-frame trace-log identity
  \({\rm STr}(O^{-1}\ddot O-O^{-1}\dot O O^{-1}\dot O)=0\) for
  \(O(s)=U(s)O_0U(s)^{-1}\), and updated the companion so omitting the seagull
  or adding genuine mass curvature is detected by finite matrix checks.
- 2026-06-07 issue #850 mass-curvature Ward-pair pass: added the determinant
  \(X,Y\) vertex-pairing formula after the pure frame connection has been
  removed.  The companion now checks that matched bosonic and squared-fermion
  mass-curvature cells cancel only after statistical Ward pairing, while an
  equal-count but mismatched vertex assignment leaves a nonzero residual.
- 2026-06-07 issue #850 supercharge-factorization pass: added the off-shell
  heavy \(Q\)-complex mechanism
  \(O_B=Q^\dagger Q\), \(O_F=QQ^\dagger\), including the generated
  \(X,Y\) vertices and square-completion contacts.  The companion now verifies
  that the bosonic and fermionic second trace-log variations pair spectrally
  even when their vertex matrices differ, and that dropping the contact term
  leaves a residual.
- 2026-06-07 issue #850 off-shell row-completion pass: added the row-resolved
  construction criterion for obtaining the Higgs heavy \(Q\)-complex from the
  kinetic, gauge-fixing/ghost, moment-map auxiliary, and Yukawa pieces of the
  quadratic Lagrangian.  The companion now checks that row-local contacts sum to
  the full \(2Q_1^\dagger Q_1\) seagull and that dropping an auxiliary/Yukawa row
  contact gives the predicted trace-log residual.
- 2026-06-07 issue #850 dimensional-reduction row audit: added the lower-dimensional
  split \(A_M=(A_\mu,\sigma_I)\), with \(4-d\) reduced vector-multiplet scalar
  rows and their contact \(C_{\rm red}^{(d)}\).  The companion now checks that
  omitting those rows in 3d/2d leaves a trace-log residual, while the symmetric
  2d metric channel is kept separate from an antisymmetric \(B/WZ\) channel.
