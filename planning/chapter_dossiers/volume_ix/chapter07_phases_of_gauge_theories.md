# Chapter 07: Phases Of Gauge Theories
Source-File: monograph/tex/volumes/volume_ix/chapter07_phases_of_gauge_theories.tex

## Source Position

Volume IX has developed global forms, higher-form symmetries, line and
surface operators, confinement, screening, discrete theta terms, and anomaly
inflow.  This chapter synthesizes those structures into a precise
infinite-volume definition of gauge-theory phase data and explains how local
analyticity, static potentials, higher-form symmetry, screening, condensates,
and topological sectors fit together.

## Source And Reference Controls

- `SRC-EXTERNAL-LSMOH`: Lieb--Schultz--Mattis, Oshikawa, and Hastings are used
  for the theorem-boundary LSMOH obstruction.  The chapter derives the exact
  finite momentum-shift algebra locally and identifies the higher-dimensional
  thermodynamic/quasi-adiabatic step as imported theorem machinery.
- `SRC-EXTERNAL-LSM-ANOMALY`: Metlitski--Thorngren,
  Else--Thorngren, and Cheng--Seiberg are used for the anomaly interpretation
  of LSM-type constraints.  The chapter treats this as a reformulation and
  matching language, not as a substitute for the finite-regulator proof.
- `SRC-EXTERNAL-FRADKIN-SHENKER`: Osterwalder--Seiler and
  Fradkin--Shenker are used for the uniform thermodynamic analytic-corridor
  theorem in fixed-length gauge--Higgs models.  The chapter owns the concrete
  finite \(\mathbb Z_2\) model, gauge-invariant observable algebra, expansion
  variables, and diagnostic limitations; the constants, polymer convergence,
  and infinite-volume analyticity are marked as imported theorem input.
- `SRC-EXTERNAL-GAPPED-AUTOMORPHIC-EQUIVALENCE`:
  Bachmann--Michalakis--Nachtergaele--Sims are used for the theorem-boundary
  statement that uniformly gapped local Hamiltonian paths yield quasi-local
  spectral-flow automorphisms implementing equivalence of gapped ground-state
  phases.  The chapter derives only the finite locality/spectral-flow
  mechanism and treats thermodynamic convergence as imported theorem input.
- `SRC-EXTERNAL-GAUGE-HIGGS-DIAGNOSTICS`: Fredenhagen--Marcu and
  Caudy--Greensite are used for charged-state/remnant-symmetry diagnostic
  context around the local analytic theorem.

## Notation Inventory

- `A_Lambda`: finite-region gauge-invariant observable algebra.
- `A_obs`: declared quasi-local observable system.
- `omega`: thermodynamic-limit state on `A_obs`.
- `P`: parameter domain of couplings and topological terms.
- `alpha_{1<-0}`: quasi-local spectral-flow automorphism transporting the
  declared observable algebra and ground-state sector; it is the output of the
  imported automorphic-equivalence theorem, not a hypothesis in the gapped
  path definition.
- `O_L`, `X_L`: increasing extended-operator family and its growing support,
  used only after a carrier topology and uniform estimates are declared.
- `gamma`: volume-uniform positive gap lower bound in the gapped phase
  equivalence criterion.
- `Phi(Z)`, `I_Lambda`, `J_*`, `N_*`: finite interaction terms, nonzero
  interaction supports, interaction strength, and overlap degree in the
  finite-regulator locality section.
- `d_Phi(X,Y)`, `partial_Phi X`: interaction-overlap chain distance and
  interaction boundary of a finite region.
- `P_Lambda(s)`, `K_Lambda(s)`, `D_Lambda(s)`: isolated-band projection,
  finite projection-commutator generator, and quasi-adiabatic generator along
  a gapped local Hamiltonian path.
- `F_gamma`: real odd quasi-adiabatic filter with
  `hat F_gamma(omega)=i/omega` outside the spectral gap.
- `nu=p/q`: rational filling per microscopic unit cell in the LSMOH section.
- `G_1`: large gauge transformation returning a \(2\pi\) flux insertion to
  zero-flux gauge.
- `L_perp`: transverse volume entering the finite LSMOH momentum shift
  `Delta P_1=2*pi*nu*L_perp`.
- `phi=(phi_x,phi_y)`: dimensionless flux coordinates on the finite flux
  torus `T^2`.
- `H_Lambda(phi)`, `I_a=partial_{phi_a}H_Lambda`: finite many-body flux
  Hamiltonian and flux-current operators.
- `P_Lambda(phi)`, `r_Lambda`, `F_xy,Lambda`, `C_Lambda`,
  `kappa_bar_xy,Lambda`:
  isolated flux-band projection, band rank, trace Berry curvature, finite
  many-body Chern number, and flux-averaged dimensionless Hall coefficient.
- `W_R(C)`, `C_{T,L}`, `V_R(L)`: Wilson loop, rectangular contour, and static
  potential.
- `rho_{R,L}`: spectral measure for a static-source transfer-matrix sector.
- `sigma_gamma`, `mu_gamma`, `kappa_R`: area-law string tension, perimeter
  coefficient, and Coulomb coefficient.
- `A`, `Ahat`: finite one-form symmetry and its Pontryagin dual.
- `C`: finite center-sensitive dyonic charge group.
- `B`: finite Dirac pairing on `C`.
- `S`, `S_perp`: subgroup screened by dynamical finite-energy excitations and
  its finite-braiding orthogonal complement.
- `C_ext`, `C_top`: external-probe quotient `C/S` and residual topological
  charge group `S_perp/S` when the screened subgroup is isotropic.
- `K`, `K_perp`: condensed isotropic charge subgroup and its orthogonal
  complement.
- `sigma_e`, `varphi_x`: \(\mathbb Z_2\) gauge--Higgs link and fixed-length
  site variables in the Fradkin--Shenker theorem-boundary model.
- `B_p`, `H_e`, `M_gamma`: plaquette term, Higgs hopping term, and
  Higgs-ended open Wilson line in the gauge--Higgs model.
- `u=tanh beta`, `v=tanh kappa`, `r=e^{-2 kappa}`: expansion variables for
  the strong, bridge, and Higgs polymer-domain discussion.
- `||zeta||_a`: Kotecky--Preiss style polymer norm used to state the imported
  corridor mechanism.
- `G_R(gamma_xy)`, `rho_R(gamma)`: open gauge-invariant transporter
  correlator and Fredenhagen--Marcu type ratio.
- `Phi_IR`: map from microscopic topological extended operators to the
  long-distance topological sector.
- `V,E,P`: vertices, edges, and plaquettes of the finite square-torus
  \(\mathbb Z_2\) gauge-code laboratory.
- `A_v`, `B_p`, `P_0`: star stabilizers, plaquette stabilizers, and the exact
  ground-space projector in that finite laboratory.
- `Z(c)`, `X(eta)`: chain and cochain Pauli line operators.
- `<eta,c>`: mod-two finite intersection pairing controlling the logical
  line commutator.

## Claim Ledger

- Defines a phase problem only after specifying regulator class, parameter
  domain, observable system, limit prescription, fixed symmetry/global-form/
  boundary conventions, and a stability criterion; comparison topology is
  auxiliary data for transported observables.
- Replaces continuity-only phase equivalence by a regulated gapped-path
  criterion: same phase requires a local Hamiltonian path with uniform locality
  bounds, sufficient \(s\)-regularity, fixed symmetry/global-form/boundary
  data, a volume-uniform positive gap above the declared ground-state band, and
  controlled thermodynamic/Cauchy hypotheses.  The quasi-local spectral-flow
  automorphism transporting the observable algebras and ground-state sectors is
  the output of the imported automorphic-equivalence theorem.
- Types extended phase diagnostics before transporting them: fixed finite
  loops are local-algebra elements; increasing loop/surface nets require a
  topology on renormalized asymptotics and uniform estimates; charged/disorder
  sectors need cone-localized, field-algebra, or boundary-category carriers;
  logical operators depend on finite-volume topology and growing supports; and
  boundary algebras or continuum-renormalized defects require separate limit
  maps.
- Separates phase boundaries and gapless universality: a boundary includes
  loss of the uniform gap, divergent correlation length, failed limit, changed
  declared data, or failed automorphism even when pointwise observables remain
  continuous; gapless regimes require separately declared stable IR data and no
  general automorphic equivalence theorem is assumed.
- Proves a finite path-count Lieb--Robinson bound from the commutator
  expansion, with explicit dependence on interaction strength, overlap degree,
  interaction-boundary size, and overlap-chain distance.
- Derives finite isolated-band spectral transport from the projection identity
  `P^2=P`, then identifies the missing locality estimate in the global
  projection generator.
- Derives the finite quasi-adiabatic off-diagonal transport equation and the
  locality mechanism: the spectral gap fixes the filter, the filter tail
  controls long times, and the Lieb--Robinson estimate controls spatial
  leakage of evolved local terms.
- Adds the LSMOH constraint layer: derives the exact finite large-gauge and
  translation commutator, obtains the flux-insertion momentum shift, states the
  thermodynamic theorem boundary with uniform locality/gap/quasi-adiabatic
  hypotheses, and separates the three infrared exits: symmetry breaking,
  gaplessness, or intrinsic topological order.
- Works the spin-\(1/2\) chain as half filling and a fractional
  \(U(1)\)-filling lattice example, while distinguishing the anomaly
  interpretation from the microscopic proof and from continuum-QFT existence.
- Defines the finite many-body flux-torus Hall datum and proves that the
  flux-averaged curvature is `C_Lambda/(2*pi*r_Lambda)` with integer
  `C_Lambda`.
- Derives the finite Kubo resolvent formula for the trace Berry curvature
  when the isolated band is an exact finite degenerate eigenvalue, while
  separating this exact finite statement from thermodynamic Hall-conductance
  hypotheses.
- Derives finite-volume gauge averaging: gauge-variant local fields have zero
  expectation with gauge-invariant finite-volume boundary conditions.
- Defines static potentials from renormalized rectangular Wilson loops.
- Derives large-time extraction of the bottom static-source spectral energy
  from a positive transfer-matrix spectral measure.
- Defines area, perimeter, and Coulomb responses as asymptotic laws of
  renormalized line operators.
- States the one-form symmetry action on charged lines by linking with
  topological symmetry surfaces.
- Distinguishes external-probe screening quotient from the residual
  finite-braiding topological charge group on which the pairing descends.
- Defines isotropic condensate subgroup and orthogonal complement of
  unconfined finite charges.
- Proves the finite condensate confinement criterion under its stated
  long-distance condensate hypothesis.
- Formulates electric, magnetic, and oblique confinement as applications of
  the finite Dirac pairing.
- Replaces the conditional gauge-Higgs corridor paragraph with a concrete
  fixed-length \(\mathbb Z_2\) gauge--Higgs model, a quoted
  Fradkin--Shenker/Osterwalder--Seiler theorem-boundary statement, the
  strong/bridge/Higgs polymer-domain anatomy, and the observable limitations:
  local gauge-invariant correlators are analytically connected in the theorem
  corridor, while extended probes, boundary sectors, Fredenhagen--Marcu ratios,
  exact center one-form diagnostics, and continuum limits remain separately
  declared data.
- Defines Fredenhagen--Marcu type ratios and proves their leading exponential
  scaling under assumed open-line and closed-loop asymptotics.
- Defines topological order/deconfined gauge theory data as an IR TQFT plus
  the map from microscopic extended operators.
- Builds a finite \(\mathbb Z_2\) gauge-code laboratory on the square torus:
  star and plaquette stabilizers, stabilizer relations, four-dimensional
  ground space, chain/cochain logical line algebra, and the mod-two
  intersection pairing.
- Derives local indistinguishability in contractible regions by Pauli-basis
  expansion: non-closed monomials have a stabilizer syndrome and closed local
  monomials reduce to products of stabilizers.
- Derives the constant \(4J\) local energy barrier for simple two-dimensional
  logical strings and separates this finite statement from any
  positive-temperature memory theorem.

## Calculation Checks

- `calculation-checks/gauge_phase_diagnostics_checks.py` verifies finite
  condensate orthogonality, electric/magnetic/dyonic confinement by the
  \(\mathbb Z_N\) Dirac pairing, tropical static-energy extraction, and
  Fredenhagen--Marcu exponent bookkeeping.
- `calculation-checks/gauge_higgs_fradkin_shenker_checks.py` verifies finite
  gauge invariance, high-temperature parity selection, charge-one screening,
  center-neutral negative controls, and the connected-domain bookkeeping behind
  the Fradkin--Shenker/Osterwalder--Seiler theorem-boundary discussion.
- `calculation-checks/hall_flux_curvature_checks.py` verifies the finite
  flux-torus Hall conventions: projector curvature equals the Kubo resolvent
  formula for a two-level isolated band, and the standard two-band lattice
  benchmark has Chern numbers \(0,+1,-1,0\) in the four mass chambers.
- `calculation-checks/lsmoh_flux_anomaly_checks.py` verifies exact rational
  momentum-shift bookkeeping for LSMOH flux insertion, the spin-\(1/2\) chain
  as half filling, fractional-filling obstruction arithmetic, and negative
  controls for integer filling, enlarged cells, gapless exits, and
  topological-sector absorption.
- `calculation-checks/lattice_locality_flow_checks.py` verifies overlap-chain
  counting for the finite path-count Lieb--Robinson estimate, the
  factorial-to-exponential tail bound, two-level spectral-flow transport, and
  the time-window split behind quasi-local generator tails.  It also includes
  negative controls showing that fixed-distance correlators can remain
  continuous while a gap closes and that a value-only comparison topology can
  miss a divergent susceptibility, plus a growing-support negative control in
  which automorphisms converge on every fixed local algebra but fail to
  transport a boundary/logical observable sequence.
- `calculation-checks/toric_code_logical_operator_checks.py` verifies the
  finite one-form laboratory: star/plaquette commutation, stabilizer
  redundancies, ground-space dimension, logical line anticommutation,
  contractible loop reduction, and constant string barrier.

## Figure Ledger

No figure is included in this pass.  A later diagram may show the observable
dependency of phase diagnostics: local correlators, line asymptotics,
screening quotient, condensate subgroup, and topological sector.

## Audit Notes

- 2026-05-29 anti-wrapper pass: demoted finite-volume gauge averaging from
  proposition form to prose.  The calculation is the finite-regulator Haar
  projection; continuum phase claims remain tied to the phase datum and
  thermodynamic-limit hypotheses.
- 2026-05-29 seventh pass: demoted the large-time spectral extraction lemma
  to a worked Laplace-principle paragraph.  The real phase-diagnostic input is
  the reflection-positive static-source transfer-matrix sector and its
  renormalized Wilson-loop spectral measure.
- 2026-05-31 statmech crosswalk pass: added a finite \(\mathbb Z_2\)
  gauge-code laboratory as exact extended-operator algebra for one-form
  symmetry, local indistinguishability, and the constant logical-string
  barrier.  The text explicitly bounds the lesson: finite stabilizer algebra is
  a proof laboratory for QFT phase diagnostics, not a substitute for a
  continuum or infinite-volume phase theorem.
- 2026-05-31 locality-machinery pass: added the finite-regulator
  Lieb--Robinson/spectral-flow machinery needed to make gapped phase stability
  claims operational.  The section proves the finite path-count estimate and
  the finite spectral-flow equations directly, while making the uniform
  thermodynamic hypotheses for quasi-local automorphic transport explicit.
- 2026-05-31 finite-Hall pass: added finite flux-torus Hall response as an
  interacting many-body curvature datum.  The text proves the integer
  Chern-number formula and the exact finite Kubo-curvature identity, then
  states the extra locality/gap/thermodynamic hypotheses needed before the
  finite curvature average can be called a phase-stable Hall conductance.
- 2026-06-05 issue #777 LSMOH pass: added the finite flux-insertion
  momentum-shift derivation, theorem-boundary statement, spin-\(1/2\) and
  fractional-filling examples, anomaly interpretation boundary, cross-volume
  links, and `lsmoh_flux_anomaly_checks.py`.
- 2026-06-05 issue #776 Fradkin--Shenker pass: replaced the assumed common
  gauge--Higgs corridor with a concrete fixed-length \(\mathbb Z_2\) model,
  theorem-boundary quotation, polymer-domain mechanism map, representation and
  observable limitations, primary references, and
  `gauge_higgs_fradkin_shenker_checks.py`.
- 2026-06-08 issue #881 pass: replaced the opening continuity-only phase
  definition with a uniform gapped-path/quasi-local-automorphism criterion,
  separated phase boundaries from gapless universality, added the
  Bachmann--Michalakis--Nachtergaele--Sims theorem boundary, and added
  continuity-only negative controls to `lattice_locality_flow_checks.py`.
- 2026-06-08 issue #951 pass: separated the gapped-path hypotheses from the
  imported automorphic-equivalence theorem output, typed extended/topological
  diagnostics by carrier and topology, downgraded the finite locality section
  to mechanism support for the theorem boundary, and added a negative control
  showing fixed-local convergence does not transport growing-support extended
  data.
