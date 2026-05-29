# Volume XII Proof-Substance Audit

Date: 2026-05-28

Scope: read the theorem-like statements and the bodies of their proofs in
`monograph/tex/volumes/volume_xii`.  This was a proof-substance pass.  I kept
wrappers when the proof body actually performs a variational calculation,
microlocal estimate, heat-kernel construction, spectral-flow/index argument,
or pAQFT algebraic construction.  I demoted wrappers when the proof was only
definition unpacking, a scope warning, or a direct mode substitution whose
content is better carried as an explicit calculation in the prose.

## Demoted wrappers

- `chapter01_locally_covariant_qft_and_hadamard_states.tex`: demoted the
  kinematic-net construction and the state-independent singular-part statement
  to `Remark~\ref{rem:kinematic-net-from-lcqft}` and
  `Remark~\ref{rem:hadamard-state-independent-subtraction}`.  The first is
  functoriality plus Einstein causality; the second is the defining Hadamard
  decomposition in two states.
- `chapter02_point_splitting_stress_tensor.tex`: demoted state dependence and
  subtraction dependence of the Wick square to
  `Remark~\ref{rem:point-splitting-smooth-change}`.  The calculation remains,
  but it is direct subtraction of two smooth remainders or two smooth
  subtraction kernels.
- `chapter03_trace_anomalies.tex`: demoted Wess-Zumino consistency and the
  four-dimensional parity-even cohomology representatives to
  `Remark~\ref{rem:curved-trace-wz-consistency}` and
  `Remark~\ref{rem:curved-four-dimensional-weyl-classes}`.  The Wess-Zumino
  identity is an abelian-variation calculation once locality is assumed; the
  four-dimensional statement records the representative basis and counterterm
  shift rather than proving the full local cohomology theorem.
- `chapter05_hawking_effect.tex`: demoted the Euclidean-regularity scope
  statement to `Remark~\ref{rem:hawking-euclidean-regularity-scope}`.  The
  text still states exactly what smoothness of the Euclidean section proves
  and what it does not prove for collapse states.
- `chapter08_cosmological_spacetimes_particle_creation.tex`: demoted the
  Robertson-Walker mode equation, the adiabatic Riccati equation, and the
  Bunch-Davies Hankel-mode check to
  `Remark~\ref{rem:flrw-mode-equation}`,
  `Remark~\ref{rem:adiabatic-frequency-riccati}`, and
  `Remark~\ref{rem:bunch-davies-hankel-modes}`.  These are useful explicit
  calculations, not standalone propositions.
- `chapter09_microlocal_spectrum_condition.tex`: demoted the Hadamard
  smooth-remainder criterion to
  `Remark~\ref{rem:microlocal-hadamard-smooth-remainder}` because it is the
  local form of the Hadamard definition after the parametrix recursion has
  already been constructed.

## Statements kept after reading the proof bodies

- In the locally covariant free scalar chapter, I kept the causal-propagator
  kernel lemma, functoriality of the free scalar algebra, and the time-slice
  property.  Their proof bodies use support of advanced/retarded Green
  operators, compatibility of causal propagators under causally convex
  embeddings, and cutoff propagation between Cauchy surfaces.
- In point splitting, I kept the leading Hadamard transport equation, the
  first logarithmic coefficient, the full logarithmic recursion, finite local
  stress-tensor freedom, and curvature-squared Euler tensors.  The proofs
  compute singular coefficients, diagonal coincidences, transport recursions,
  local tensor classification under covariance and conservation, and metric
  variations of curvature-squared actions.
- In trace anomalies, I kept the Weyl variation of the \(R^2\) counterterm,
  the two-dimensional Wess-Zumino action, and the conformal-scalar heat-kernel
  coefficient.  These proof bodies contain explicit Weyl-variation and
  heat-kernel coefficient computations.
- In the Unruh and Hawking chapters, I kept the complex boost geometry, free
  scalar wedge KMS theorem, polynomial wedge algebra corollary, detailed
  balance identity, Rindler normal form, late-time ray tracing, and late-time
  packet occupation.  The proof bodies carry analytic continuation, Wick
  reduction, KMS contour shifts, horizon normal-form expansion, ray-tracing
  asymptotics, and the logarithmic-frequency delta distribution.
- In the index and eta-invariant chapters, I kept McKean-Singer,
  Lichnerowicz, Seeley-DeWitt, local index density, eta-cylinder variation,
  determinant-line transport, the \(SU(2)\) parity criterion, and local descent
  from inflow.  These proofs use spectral pairing, Clifford curvature algebra,
  heat-kernel recursion, Getzler scaling, APS orientation bookkeeping,
  Bismut-Freed holonomy, Lucas parity, and APS filling of contractible loops.
- In cosmological particle creation, I kept Bogoliubov normalization and
  particle number, and positivity of the switched detector response.  The
  proof bodies use Wronskian conservation, mode-operator comparison, CCR
  vacuum algebra, positive-type distributions, and tubular smearing of
  worldline test functions.
- In the microlocal and pAQFT chapters, I kept the product criterion for
  distributions, transport equation for \(U\), Hadamard coefficient recursion,
  pAQFT star-product associativity, change of Hadamard function, extension
  with fixed scaling degree, and causal support of Bogoliubov fields.  The
  proofs contain conic Fourier estimates, Van Vleck transport, recursive
  singular-coefficient cancellation, contraction-operator algebra,
  normal-ordering intertwiners, Epstein-Glaser extension by Taylor
  subtraction, and causal-factorization support arguments.
- In semiclassical backreaction, I kept the diffeomorphism Ward identity,
  curvature-squared Euler tensors, retarded stress-tensor linear response, and
  Einstein-Langevin pushforward covariance.  The proof bodies perform the
  variational Ward identity, curvature variations, retarded commutator
  derivation, and Gaussian characteristic-functional pushforward.

## Remaining standard

This pass removes theorem-like wrappers whose proof bodies were not
theorem-level.  It does not turn quoted global-analysis theorems such as APS,
Bismut-Freed, or Shale-Stinespring into self-contained proofs; those remain
explicitly quoted boundaries until a later appendix supplies the analytic
proofs needed by the monograph.
