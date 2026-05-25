# Volume II, Chapter 16 Dossier: Statistical Ising Model And Universality

## Source Position

- Primary local source: second-sequence handwritten material, pages 136--146.
- Immediate predecessor: Wilson-Fisher fixed point and the first scaling
  operators.
- Immediate successor in the source order: Wilsonian effective actions with a
  floating cutoff.
- Role in the monograph: connect the fixed-point and scaling-operator
  construction to statistical spin systems by defining the Ising ensemble,
  its scaling limit, and the RG meaning of universality.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 136--146;
  checked against rendered page images in
  `monograph/tex/build/source_visual_trace/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  corresponding Ising-universality section, used only as a comparison layer.
- `SRC-EXTERNAL`: Rosten's exact-RG review for Wilsonian terminology and
  Simmons-Duffin's bootstrap lectures for CFT scaling-operator language.
  External sources orient theorem boundaries; the chapter follows the local
  logical order.
- `SRC-EXTERNAL`: Smirnov and Chelkak--Hongler--Izyurov for rigorous
  two-dimensional planar Ising scaling limits; Nelson, Simon, and
  Glimm--Jaffe for \(P(\phi)_2\) and massive \(\phi^4_3\) constructive
  scalar field theories with OS-to-Wightman reconstruction;
  Aizenman--Duminil-Copin and its corrigendum, together with earlier
  Aizenman/Fr\"ohlich triviality results, for four-dimensional and
  above-four-dimensional Ising/\(\phi^4\) triviality status.

## Construction Task

The chapter must define and derive:

- the finite-volume statistical Ising ensemble on a \(D\)-dimensional lattice;
- its status as the finite-lattice row of
  `tab:regulator-integration-status-catalog`: an ordinary finite probability
  measure before thermodynamic or scaling limits;
- the role of boundary conventions in \(E(\Lambda)\) and thermodynamic
  limits;
- the ferromagnetic thermodynamic-limit theorem: FKG positive association,
  GKS monotonicity, GHS concavity, monotone plus/minus infinite-volume limits,
  one-sided \(h\downarrow0\) phase selection, and clustering as the condition
  that makes a limiting Gibbs state pure;
- the equivalent finite-dimensional diagonal-operator trace notation;
- the canonical Boltzmann distribution and its maximum-entropy role;
- thermal spin correlators and the distinction among ordered, disordered, and
  critical long-distance regimes;
- spontaneous magnetization as an infinite-volume pure-phase limit;
- the correlation length and its divergence near the critical temperature;
- the critical exponents \(\Delta_\sigma\) and \(\nu\), including the
  quoted \(D=2\) and \(D=3\) values from the local source;
- the scaling limit in which lattice spin correlators become correlators of a
  continuum Ising field theory;
- the separated spin scaling limit as an explicit hypothesis: renormalized
  lattice spin correlators are assumed to converge for pairwise distinct
  continuum insertion points along the chosen thermal scaling trajectory;
- the dimension-dependent theorem-status table separating proved \(D=2\)
  Ising scaling limits, constructive \(P(\phi)_2/\phi^4_3\) scalar results,
  conditional/unproved \(D=3\) Ising continuum-limit/CFT claims, and
  \(D\ge4\) scalar/Ising triviality theorems;
- the distinction, for \(D\ge4\), between Gaussian separated critical scaling
  limits and the dangerous irrelevance of the quartic coordinate in ordered
  thermodynamic observables, with a cross-reference to the chapter where the
  \(D>4\) equation-of-state and \(D=4\) leading-log derivations are given;
- the signed thermal scaling parameter \(\mathfrak m\), whose absolute value
  is the continuum inverse correlation length and whose sign records the
  high- or low-temperature side;
- the distinction between this inverse-correlation-length gap and a spectral
  pole mass, which additionally requires an isolated one-particle atom in the
  reconstructed spectral measure;
- the magnetic scaling coordinate and the restriction to zero magnetic
  deformation in the displayed scaling limit;
- the critical \(\mathfrak m=0\) Ising fixed point and the assumptions under
  which it is interpreted as the Ising CFT;
- finite-lattice reflection positivity with respect to a Euclidean time
  reflection, as a property of the regulated measure rather than a consequence
  of universality language;
- the sum-of-squares proof that ferromagnetic nearest-neighbor Ising models
  and nearest-neighbor scalar models with positive one-site measure preserve
  reflection positivity;
- the distinction between reflection-positive regulator families and
  arbitrary lattice representatives in the same formal RG chart, including the
  possible failure caused by negative cross-reflection couplings or
  non-positive higher-derivative kernels;
- preservation of reflection positivity under scaling limits as a separate
  closedness statement for reflected quadratic forms;
- the operator dictionary as a leading scaling-field expansion, with
  \(s_x\) having leading field \(\sigma\) and the subtracted lattice energy
  density having leading field \(\varepsilon\);
- the scalar-coordinate statement that \(\phi\) represents \(\sigma\) and the
  identity-subtracted mass operator \([\phi^2]\) represents \(\varepsilon\);
- observable scaling limits as source-dependent distributions, including
  smeared renormalized lattice spin and energy observables;
- the source-dependent generating-functional limit
  \(W_a[\mathcal Z_a(\eta)]-W_a[0]-P_a(\eta)\to W_\ast[\eta]\);
- the separation between universal separated-point kernels, linear
  source-normalization data, and model- or scheme-dependent contact-term
  extensions;
- the generalized Ising model with a single-site potential and continuous
  spin variable;
- the rewriting of the generalized Ising partition function as a lattice
  scalar path integral;
- the Brillouin-zone cutoff, the derivative expansion of the lattice kinetic
  term, and the lattice-anisotropic irrelevant corrections;
- universality classes as fixed-point basins after tuning relevant
  coordinates;
- the relation \(\nu=1/(D-\Delta_\varepsilon)\) from the energy deformation;
- the distinction between nonuniversal metric factors, such as the coefficient
  relating \(T-T_c\) to the thermal scaling coordinate, and universal
  exponents.
- finite-cutoff universality in a local RG chart: endpoint maps for relevant
  coordinates, a conditional proposition applying the Wilsonian
  cutoff-removal estimate, nonuniversal microscopic coordinate maps, and the
  separate scaling-limit hypotheses needed before lattice observables become
  continuum operators;
- a conditional lattice-to-continuum universality theorem whose hypotheses
  include finite-coordinate RG convergence, source-renormalized generating
  functional convergence, sequential continuity of the coordinate-to-source
  map at the continuum graph, common field normalization, and convergence of
  reflection-positive OS quadratic forms;
- an end-to-end conditional Ising universality theorem from thermodynamic
  lattice data through Wilsonian coordinate convergence and source-functional
  scaling limits to CFT data, stating precisely when normalized long-distance
  Ising scaling functions are determined by the Ising CFT/OPE data and its
  constructed relevant deformations;
- the correction-to-scaling structure obtained by differentiating the
  coordinate-to-correlator map in retained irrelevant coordinates.

## Claim Ledger

1. A finite Ising model is a classical probability measure on spin
   configurations; diagonal-operator notation is exact finite-dimensional
   bookkeeping.  Its use as a continuum-QFT regulator requires separate
   thermodynamic and scaling-limit hypotheses.
2. Canonical weights arise from maximizing entropy at fixed expected energy.
3. The low-temperature ordered phase is defined by plus/minus
   infinite-volume Gibbs limits or one-sided symmetry-breaking-field limits;
   these limits exist in the ferromagnetic setting by FKG/GKS monotonicity,
   and they are pure only when the corresponding limiting state is clustering.
4. Critical spin correlators define the spin scaling dimension
   \(\Delta_\sigma\).
5. The scaling limit of near-critical lattice correlators produces Euclidean
   correlators of a continuum Ising field theory only when the separated
   spin scaling-limit hypothesis, or a stronger source-dependent scaling
   limit, has been proved or imposed.
6. At criticality the inverse correlation length vanishes; with the usual
   rotation, scale, and stress-tensor assumptions the limiting fixed point is
   the Ising CFT.
7. The generalized Ising model can be written as a scalar lattice path
   integral with a finite UV cutoff and many local couplings.
8. Lattice anisotropy and higher-derivative terms are irrelevant at the Ising
   fixed point in \(D=2,3\).
9. The temperature perturbation couples to the energy operator, whose dimension
   determines the correlation-length exponent.
10. In the \(\mathbb Z_2\)-even slice, only the thermal relevant coordinate
    must be tuned; without the symmetry, the magnetic coordinate is also
    relevant.
11. Under stated local RG hypotheses, tuned microscopic realizations have the
    same limiting finite-coordinate graph.  This coordinate statement does not
    by itself prove existence of the continuum scaling limit.
12. A source-dependent scaling limit gives operator-valued distributions by
    differentiating the limiting source functional.  The linear source jet
    fixes separated-point observable normalizations, while higher local
    source jets and source-local vacuum terms determine contact-term
    extensions on collision diagonals.
13. Normalized continuum correlator universality follows only after adding
    scaling-limit existence, positivity, locality, regularity, and continuity
    hypotheses for the coordinate-to-correlator map.
13a. The conditional lattice-to-continuum universality theorem states that,
     under those hypotheses plus finite-coordinate RG convergence, all
     microscopic representatives have the same normalized separated-point
     Schwinger functions, while source-local polynomial differences change
     only contact terms.
13b. The end-to-end conditional Ising universality theorem additionally
     assumes the fixed point satisfies OS/radial reconstruction, the
     stress-tensor hypotheses for a CFT, and radial OPE convergence.  Under
     those hypotheses the critical separated scaling functions are determined
     by the fixed-point CFT data, while nonzero thermal or magnetic scaling
     functions require the constructed relevant deformation by
     \(\varepsilon\) or \(\sigma\).
14. Reflection positivity is automatic for the ferromagnetic nearest-neighbor
    Ising model, and for the nearest-neighbor scalar model with positive
    one-site measure and nonnegative cross-reflection coupling, by an explicit
    expansion of the crossing Boltzmann factor into nonnegative
    rank-one terms.  It is not automatic for arbitrary microscopic
    representatives of a proposed universality class.
15. A scaling limit preserves reflection positivity only when the
    Osterwalder--Schrader quadratic forms of the renormalized lattice
    observables converge; separated-point convergence or finite RG-coordinate
    convergence is insufficient.
16. The theorem status of Ising/\(\phi^4\) continuum limits is
    dimension-dependent: planar critical Ising has rigorous scaling-limit
    constructions; \(P(\phi)_2\) and massive \(\phi^4_3\) have constructive
    scalar QFT constructions with Wightman reconstruction; the
    three-dimensional Ising fixed point as a CFT remains conditional; and
    standard \(D\ge4\) critical Ising/\(\phi^4\) scaling limits in the known
    theorem classes are Gaussian.
16a. The Gaussian endpoint of the \(D\ge4\) critical separated-point scaling
     limit is compatible with singular dependence on the quartic coordinate in
     ordered thermodynamic observables.  Above four dimensions this is
     dangerous irrelevance of the quartic coordinate; at four dimensions it is
     marginal dangerous irrelevance producing leading logarithms.

## Figure Requirements

- Lattice-spin ensemble and finite-volume trace representation.
- Spin correlator regimes below, at, and above the critical temperature.
- Scaling-limit map from lattice spin insertions to continuum Ising-field
  correlators, with the signed thermal scaling parameter recorded.
- Generalized Ising model as a cutoff scalar path integral with Brillouin-zone
  support and a lattice derivative expansion.
- RG universality diagram showing Ising lattice actions and scalar
  \(\phi^4\)-type actions flowing to the same critical fixed point in the
  \(\mathbb Z_2\)-even slice after tuning the thermal relevant direction.

## Audit Notes

- 2026-05-22 source-certification pass: handwritten 253b pages 136--146 were
  checked against rendered source images and comparison transcriptions.  The
  manuscript includes the finite Ising ensemble and diagonal trace notation,
  the entropy/Boltzmann and finite-state \(H\)-theorem reminder, low- and
  high-temperature spin-correlator regimes, the critical-exponent table, the
  continuum scaling limit with signed thermal scale, the separation between
  Euclidean Schwinger functions and reconstructed Lorentzian Hilbert space,
  the leading scaling-field dictionary, the generalized Ising scalar path
  integral, the Brillouin-zone derivative expansion and cutoff, and the RG
  universality argument with relevant scalar coordinates and nonuniversal
  temperature metric factors.
- Do not state or imply that the statistical spin Hilbert space is the
  Lorentzian QFT Hilbert space.
- Do not present universality as microscopic equality.
- Do not identify a microscopic lattice observable literally with a continuum
  field; use the scaling-field expansion and state nonuniversal normalizations.
- Do not erase the sign of the thermal deformation in the massive scaling
  limit.
- Use Wilsonian cutoff-flow estimates only with their stated finite-chart
  hypotheses; do not promote them to an uncontrolled infinite-dimensional
  theorem.
- 2026-05-24 issue #339 pass: added
  `thm:conditional-ising-universality-lattice-to-cft-data`, chaining
  thermodynamic lattice limits, finite-coordinate Wilsonian convergence,
  source-functional scaling limits, OS/radial reconstruction, and CFT/OPE data
  into one conditional theorem for normalized separated Ising scaling
  functions.
- Do not present local RG coordinate convergence as a theorem proving
  existence of a continuum lattice scaling limit.
- Do not infer Osterwalder--Schrader positivity from membership in a proposed
  universality class.  State the reflection-positive regulator class or keep
  positivity as a separate scaling-limit hypothesis.
- No reader-facing source-page references or course-note references.
- 2026-05-22 finite-cutoff-universality pass: added a section defining
  \(z=(u,v)\) at a reference scale, the microscopic endpoint map
  \(E_X(\Lambda_0,p_X)\), a local universality proposition derived from the
  finite-coordinate cutoff-removal estimate, the linear tuning relation
  \(T-T_{c,X}\sim A_X^{-1}(\mu_R/\Lambda_0)^{y_t}\lambda_{t,R}\), and the
  normalized scaling-field limit for separated lattice correlators.  Added
  the finite-chart correction-to-scaling expansion
  \(G^X_a=G_{u_R}+O((\mu_R a)^\kappa)\), with leading exponent identified
  with the smallest irrelevant eigenvalue when the generated-integral
  remainder is faster.
- 2026-05-22 source-dependent-observable pass: added a distributional
  source-functional formulation of observable scaling limits.  The manuscript
  now defines smeared renormalized lattice spin and energy observables,
  states the source-dependent scaling limit with local source maps and
  source-local vacuum subtractions, and proves that separated universality is
  controlled by the linear source jet while contact conventions are supported
  on collision diagonals.
- 2026-05-24 issue #236 pass: promoted the scaling-limit caveat from a remark
  to a proposition separating finite-coordinate universality from existence of
  a continuum measure/source functional.  The manuscript now states that
  normalized correlator universality requires additional scaling-limit,
  positivity, locality, regularity, clustering, and continuity hypotheses.
- 2026-05-24 issue #237 pass: added a reflection-positivity section defining
  the finite-lattice OS quadratic form, proving reflection positivity for
  ferromagnetic nearest-neighbor Ising and scalar lattice measures by explicit
  sum-of-squares factorization, and stating preservation under scaling limits
  as a separate convergence theorem for reflected quadratic forms.  The
  generalized scalar model now records that positive nearest-neighbor
  cross-reflection coupling preserves reflection positivity, while negative
  next-nearest-neighbor or non-positive higher-derivative cross-plane kernels
  can fail.
- 2026-05-24 issue #317 pass: added a dimension-dependent status table for
  Ising and scalar \(\phi^4\) continuum limits.  The manuscript now names the
  theorem-level two-dimensional Ising and massive \(\phi^4_3\) Wightman
  constructive results, separates them from the still-conditional
  three-dimensional Ising fixed point as a CFT, and records the
  Aizenman--Duminil-Copin/four-dimensional triviality boundary.
- 2026-05-24 issue #326 pass: made the separated spin scaling limit an
  explicit hypothesis and added a conditional lattice-to-continuum
  universality theorem.  The theorem combines finite-coordinate RG
  convergence, source-renormalized generating-functional convergence,
  sequential continuity of the coordinate-to-source map, common field
  normalization, and convergence of reflection-positive OS quadratic forms to
  prove equality of normalized separated-point Schwinger functions.
- 2026-05-24 issue #327 pass: added the ferromagnetic thermodynamic-limit
  theorem before the phase discussion.  The theorem records the finite-volume
  FKG, GKS, and GHS inequalities, proves FKG from log-supermodularity,
  derives monotone plus/minus infinite-volume and one-sided field limits, and
  states clustering as the condition under which a boundary-selected Gibbs
  state is pure.
- 2026-05-25 issue #462 pass: inserted the \(D\ge4\) dangerous-irrelevance
  caveat after the continuum-status table, separating Gaussian critical
  separated-point scaling limits from the quartic-dependent ordered equation
  of state and pointing to the explicit \(D>4\) and \(D=4\) derivations in the
  Wilson-Fisher/scaling-coordinate chapter.
