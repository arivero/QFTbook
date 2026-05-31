# Statmech Project Crosswalk For QFT Development

Date: 2026-05-31.

Local source inspected: `/Users/xiyin/statmech/`.  The relevant source files
are principally:

- `/Users/xiyin/statmech/README.md`;
- `/Users/xiyin/statmech/planning/06_table_of_contents.md`;
- `/Users/xiyin/statmech/codex_review.md`;
- `/Users/xiyin/statmech/tex/volume_ii/chapters/ch15_lattice_models.tex`;
- `/Users/xiyin/statmech/tex/volume_ii/chapters/ch16_liquids_solids_defects_elasticity.tex`;
- `/Users/xiyin/statmech/tex/volume_ii/chapters/ch17_topological_phases.tex`;
- `/Users/xiyin/statmech/tex/volume_ii/chapters/ch19_scaling_universality_finite_size.tex`;
- `/Users/xiyin/statmech/tex/volume_ii/chapters/ch20_wilsonian_renormalization_group.tex`;
- `/Users/xiyin/statmech/tex/volume_ii/chapters/ch21_nonperturbative_statistical_field_theory.tex`;
- `/Users/xiyin/statmech/tex/volume_ii/chapters/ch22_quantum_phase_transitions_low_dimensional.tex`;
- `/Users/xiyin/statmech/tex/volume_iii/chapters/ch27_transfer_matrices_exact_diagonalization.tex`;
- `/Users/xiyin/statmech/tex/volume_iii/chapters/ch28_monte_carlo_markov_rare_events.tex`;
- `/Users/xiyin/statmech/tex/volume_iii/chapters/ch30_tensor_networks_variational_many_body.tex`;
- `/Users/xiyin/statmech/tex/volume_iii/chapters/ch31_neural_variational_estimators.tex`;
- `/Users/xiyin/statmech/tex/volume_iv/chapters/ch32_linear_response_transport_hydrodynamics.tex`;
- `/Users/xiyin/statmech/tex/volume_iv/chapters/ch33_fluctuation_theorems_stochastic_thermo.tex`;
- `/Users/xiyin/statmech/tex/volume_iv/chapters/ch34_open_quantum_systems_thermalization.tex`;
- `/Users/xiyin/statmech/tex/volume_iv/chapters/ch35_statistical_turbulence_cascades.tex`;
- `/Users/xiyin/statmech/tex/volume_iv/chapters/ch36_turbulence_closure_computation.tex`;
- `/Users/xiyin/statmech/tex/volume_iv/chapters/ch37_frontiers_limitations_open_problems.tex`.

The statmech text should be used as an adjacent internal project, not as an
authority.  Any QFT-side absorption must rederive the statement in QFT notation,
declare regulators and limits, and avoid importing statistical-mechanics
language whose hypotheses do not apply to relativistic QFT.

## High-Value Absorption Tracks

### Exact RG, Projected RG, And Universality

Statmech source: Volume II Chapters 19 and 20.

QFT target:

- Volume II Chapter 16, Wilsonian effective field theory;
- Volume II Chapters 14 and 15, Wilson--Fisher and Ising universality;
- Volume XI Chapter 7, rigorous renormalization group.

Useful content:

- the distinction between exact pushforward RG, projected finite-coordinate
  RG, perturbative beta functions, rigorous hierarchical RG, and physical
  universality interpretations;
- fixed points and stable manifolds as claims about a specified RG map in a
  specified topology;
- finite-size scaling and data-collapse criteria as evidence statements with
  corrections and critical-point uncertainty, rather than definitions of a
  universality class;
- dangerous irrelevance, marginal variables, logarithmic corrections, and
  boundary/shape dependence as concrete ways in which naive scaling collapses
  can mislead.

QFT action: use this taxonomy as an audit standard for every RG statement.  It
fits the existing QFT standard that a beta function is a coordinate
description, not the definition of RG.  The actual QFT development must be
rewritten in terms of regulated path integrals, local operators, BV/lattice
compatibility for gauge theories, and continuum-limit observables.

### Constructive And Nonperturbative Statistical Field Theory

Statmech source: Volume II Chapter 21.

QFT target:

- Volume XI Chapters 1--4, constructive status, scalar OS data, reflection
  positivity, and continuum limits;
- Volume XI Chapter 7, rigorous RG;
- Volume II Chapters 14--16 where statistical-field examples are used as QFT
  laboratories.

Useful content:

- OS data as a construction target;
- the separation between regulated identities and nonperturbative continuum
  claims;
- fields as distributions, source functionals, Wick ordering, cutoff removal
  of smeared covariances, and local-product status;
- polymer gases, cluster expansions, Pirogov--Sinai phase construction, and
  first-order finite-volume phase-sum scaling.

QFT action: this is suitable for deeper constructive chapters, especially where
the QFT manuscript still carries quoted constructive theorems.  The cluster and
polymer material should be imported only after a QFT-side construction states
the Banach norms, large-field regulator, covariance decomposition, polymer
activities, convergence theorem, and OS output being proved.

Absorption status: Volume XI, Chapter 2 now contains the hard-core polymer
activity norm, Penrose tree-graph bound, Kotecky--Preiss/Brydges--Kennedy
rooted-tree convergence proof, and the source-derivative bridge from the
abstract polymer gas to connected Schwinger coefficients.  The latter writes
derivatives of \(\log Z_\Lambda(\lambda)\) as connected cluster sums with
source assignments, so finite-volume factorization and exponential clustering
are tied to incompatibility paths rather than stated as folklore.  The
remaining constructive-cluster work is model-specific: derive the actual
large-field/phase-cell polymer activities and their scale-decay bounds for
the constructive scalar models rather than treating the abstract convergence
criterion as the whole proof.

### Lattice Gauge Theory, Center Order, And Elitzur Discipline

Statmech source: Volume II Chapter 21, especially lattice gauge theory,
Polyakov loops, center symmetry, thermal gauge theory, Higgs/confinement, and
Elitzur-discipline sections.

QFT target:

- Volume II Chapter 17b, lattice Yang--Mills;
- Volume IX Chapters 1, 4, and 7, global forms, confinement/screening, and
  phases of gauge theories;
- Volume X Chapter 12, QCD phase structure.

Useful content:

- finite-regulator gauge-invariant observables before phase claims;
- Polyakov-loop and center-symmetry diagnostics with boundary-condition and
  source-selection limits stated explicitly;
- Elitzur's theorem as a constraint on interpreting gauge-variant order
  parameters;
- lattice gauge theory as an honest statistical system with a continuum-limit
  problem, rather than a mnemonic for continuum path integrals.

QFT action: the QFT monograph already has much of this substance, but the
statmech chapter suggests a useful audit: every confinement/deconfinement or
Higgs/confinement phase statement should name the finite-regulator observable,
the limit order, and whether it is a theorem, a lattice diagnostic, or a
physical hypothesis.

### Topological Phases As Finite Locality Laboratories

Statmech source: Volume II Chapter 17.

QFT target:

- Volume VIII, TQFT;
- Volume IX, generalized symmetry, line/surface operators, categorical
  symmetry, duality defects, and phases of gauge theories.

Useful content:

- local quantum lattice systems and gapped ground-state phase definitions;
- Lieb--Robinson bounds, quasi-adiabatic continuation, and bounded-depth
  circuits as finite-regulator locality tools;
- interacting Hall-conductance quantization, flux insertion, strip currents,
  and local adiabatic control;
- toric-code local indistinguishability, degeneracy, logical Wilson loops, and
  anyonic excitation algebra;
- the distinction between topological defects and topological order;
- higher-form, subsystem, and non-invertible symmetries as operator algebras,
  not group-action slogans.

QFT action: use these finite lattice models as proof laboratories for the
QFT volumes on global structure and TQFT.  The QFT monograph should not replace
continuum QFT definitions by lattice phase definitions, but it should use
finite local models to test claims about higher-form symmetry, categorical
symmetry, topological lines, and boundary/defect sectors.

Absorption status: the first finite laboratory has been installed in
Volume IX, Chapter 7 as the square-torus \(\mathbb Z_2\) gauge code.  It gives
exact star/plaquette stabilizers, logical line intersection algebra, local
indistinguishability in contractible regions, and the constant logical-string
barrier.  The same chapter now also contains the finite-regulator
Lieb--Robinson/path-count proof, finite isolated-band spectral flow, and the
quasi-adiabatic locality mechanism that turns a uniformly gapped local path
into quasi-local transport of phase data.  It now also contains the finite
many-body flux-torus Hall response datum: trace Berry curvature of an
isolated band, integer Chern number, exact finite Kubo-curvature identity for
an exactly degenerate band, and explicit locality/gap/thermodynamic
hypotheses needed before the finite curvature average becomes a Hall
conductance theorem.  Volume VIII, Chapter 11 now also contains an exact
finite Abelian boundary laboratory: line-label group \(A\oplus\widehat A\),
braiding, spin, bosonic Lagrangian subgroups, endpoint absorption, and the
cylinder-sector count
\(|\mathcal C_A/(L_0+L_1)|=|L_0\cap L_1|\).  A second finite boundary pass
now adds nonabelian subgroup boundaries: interval sectors
\(H_0\backslash G/H_1\), stabilizer weights, and relative
Dijkgraaf--Witten boundary cochains \(\delta\beta=i^*\omega\).  It also
derives the finite junction convolution
\(|H_1|^{-1}\sum_{xy=g}f(x)k(y)\) for composing subgroup-boundary intervals,
including associativity, unit sectors, and the \(S_3\) two-sector algebra.
The remaining finite-locality tasks are deeper thermodynamic Hall-response
stability estimates beyond the finite curvature theorem, more substantial
twisted/non-Abelian boundary examples with higher junctions, and stronger
TQFT-boundary comparisons.

### Dynamic Critical Phenomena And Stochastic Field Theories

Statmech source: Volume II Chapter 19 and Volume IV Chapter 33.

QFT target:

- Volume X, thermal and nonequilibrium QFT;
- Volume XI Chapter 9, stochastic quantization, with a clear boundary between
  Euclidean stochastic quantization and physical stochastic dynamics.

Useful content:

- Model A and Model B as regulated stochastic field theories with specified
  conserved or nonconserved variables;
- Hohenberg--Halperin dynamic classes as hypotheses about slow variables and
  noise, not theorem labels;
- MSRJD functionals derived from discrete Langevin path measures;
- Doi--Peliti functionals derived from birth--death master equations;
- continuum-limit and renormalization status for nonequilibrium field
  theories.

QFT action: Volume X should eventually contain a systematic chapter-level
development of stochastic/nonequilibrium field theory, including MSRJD and
Doi--Peliti, because these are genuine QFT-adjacent path-integral formalisms.
They must be introduced from finite path measures or finite Markov generators,
then scaled; no formal response-field path integral should appear as a
definition without its regulator.

Absorption status: Volume X, Chapter 10 now derives finite-step MSRJD
variables from Gaussian transition kernels, formulates finite Model A/B
mobility-gradient data with Gibbs invariant density and the graph-incidence
conservation mechanism for Model B, derives Doi--Peliti variables from finite
reaction-network generators, and adds the finite Schwinger--Keldysh/MSRJD
Gaussian bridge: the quadratic SK influence weight is rewritten by an explicit
Hubbard--Stratonovich characteristic-function identity, the response variable
imposes \(E(\phi_r)+\xi=0\), and a linear retarded equation gives covariance
\(K^{-1}NK^{-T}\).  Remaining work in this track is the continuum
renormalization of nonequilibrium stochastic field theories, dynamic critical
models with additional slow variables, and model-by-model RG analyses of
conserved and nonconserved stochastic field theories.

### Linear Response, Kubo, Mori--Zwanzig, Hydrodynamic Limits, And GHD

Statmech source: Volume IV Chapter 32.

QFT target:

- Volume X Chapters 1, 4, 5, 8, and 11;
- Volume VI where generalized hydrodynamics interfaces with integrability.

Useful content:

- Duhamel derivation of mechanical linear response;
- Kubo and Green--Kubo formulae with order-of-limits discipline;
- Mori--Zwanzig projection and memory kernels;
- hydrodynamic limit theorem status, with finite continuity identities kept
  separate from macroscopic closure assumptions;
- generalized hydrodynamics for integrable systems, including hard-rod
  checks and integrability-breaking cautions;
- probe-to-observable reductions for structure factors, spectral functions,
  conductivities, susceptibilities, and calorimetry.

QFT action: Volume X has the right skeleton but is still much shorter than the
statmech treatment.  The QFT version should be expanded around stress-tensor
and conserved-current Wightman/KMS correlators, Schwinger--Keldysh sources, and
operator definitions of transport coefficients, while using the statmech
chapter's order-of-limits and memory-kernel discipline.

### Fluctuation Relations, Large Deviations, And Path Measures

Statmech source: Volume IV Chapter 33.

QFT target:

- Volume X Chapters 3, 6, and 10;
- possible later sections on nonequilibrium steady states and open quantum
  systems.

Useful content:

- finite-time path-measure identities before thermodynamic terminology;
- entropy production as a Radon--Nikodym path ratio;
- Jarzynski and Crooks relations with initial and reversed path measures;
- hidden entropy production under partial observation;
- thermodynamic uncertainty relations and speed-limit inequalities;
- dynamical large deviations and \(s\)-ensembles;
- quantum fluctuation relations.

QFT action: incorporate only where the QFT monograph can state the path space,
initial state, time reversal, absolute-continuity hypothesis, and operator or
measurement protocol.  These topics are valuable for Volume X, but they must
remain distinct from equilibrium KMS theory and from Schwinger--Keldysh
generating functionals unless a derivation connects them.

### Open Quantum Systems, Thermalization, ETH, And Quantum Chaos

Statmech source: Volume IV Chapter 34.

QFT target:

- Volume X Chapter 10, open systems and nonequilibrium steady states;
- Volume X Chapter 1, KMS states and thermalization boundaries;
- Volume XII where locally covariant QFT or AQFT can treat KMS states.

Useful content:

- completely positive maps, quantum Markov semigroups, Lindblad generators,
  and quantum detailed balance;
- Davies weak-coupling limits with microscopic hypotheses;
- influence functionals and memory kernels;
- thermal operations and noncommuting charges;
- ETH matrix-element diagnostics and quantum-chaos diagnostics as finite
  many-body evidence, not definitions of thermalization;
- weak ergodicity breaking, scars, fragmentation, and MBL as finite-system
  or scaling claims with failure modes.

QFT action: develop open QFT only after the system/environment split, reduced
algebra, scaling limit, and domain of the generator are specified.  ETH and
chaos diagnostics can enter QFT only as regulated many-body evidence or as
large-volume spectral hypotheses; they should not be used as foundational
definitions of thermalization.

### Numerical QFT Methods And Evidence Standards

Statmech source: Volume III Chapters 27--31.

QFT target:

- Volume XI Chapter 6, Monte Carlo and sign problems;
- Volume XI Chapter 10, Hamiltonian truncation, DLCQ, and benchmarks;
- GitHub issues #494 and #631.

Useful content:

- transfer matrices, exact diagonalization, symmetry sectors, sparse
  Hamiltonians, Lanczos/Krylov residuals, and size-sequence extrapolation;
- Markov kernels, detailed balance, mixing, autocorrelation, reweighting,
  rare-event bias, HMC, auxiliary-field QMC, and QMC representation
  benchmarks;
- MPS, DMRG, MERA, symmetry-adapted tensors, transfer operators, discarded
  weight, correlation-length scaling, and tensor-network evidence standards;
- neural quantum states, stochastic reconfiguration, calibration, optimizer
  bias, sampled estimator error, surrogate failure, and validation bounds.

QFT action: the QFT monograph should absorb the evidence standard more than
the statistical-mechanics examples.  Every numerical QFT claim should specify
the finite regulator, target observable, estimator, autocorrelation or
variational error, systematic extrapolation model, and continuum/volume limit.
Tensor networks and neural states deserve QFT-side treatment only when tied to
concrete regulated QFT targets such as TCSA/DLCQ, lattice gauge theory, tensor
renormalization, or finite-volume Hamiltonian spectra.

Partial QFT absorption on 2026-05-31: Volume XI, Chapter 10 now includes
Krylov/Lanczos finite spectral certificates for Hamiltonian truncation and
DLCQ matrices, including exact Ritz residuals, seed spectral-measure moments,
and the sector/seed-overlap obligations needed before finite spectra are read
as QFT evidence.  This addresses the exact-diagonalization/Krylov portion of
the numerical-evidence lane; tensor networks, neural variational states, and
larger production workflows remain separate development tasks.

Second partial absorption on 2026-05-31: the same chapter now formulates
tensor-network, DMRG/MERA, and neural-state computations as finite
variational ansatz data.  The added material derives the energy-variance
residual certificate, finite spectral/projector leakage bounds, the
tangent-gradient stationarity condition, and the local-energy mean/variance
identities used in sampled neural-state calculations.  Remaining numerical
evidence work includes production tensor-network extrapolation standards,
neural optimizer/calibration diagnostics, and larger workflow integration.

Third partial absorption on 2026-05-31: Volume XI, Chapter 10 now adds the
correlated finite-window extrapolation layer needed by production numerical
QFT workflows.  Fit windows, covariance matrices, declared fit functions, and
remainder envelopes are treated as part of the finite datum; the chapter
derives the exact intercept error decomposition, covariance propagation,
systematic row-amplifier coordinate, and correlated residual diagnostic.
Remaining numerical evidence work is now concentrated on concrete
tensor-network continuum-control examples, neural optimizer/calibration
diagnostics beyond local-energy variance, HMC/RHMC production machinery, and
larger workflow integration.

Fourth partial absorption on 2026-05-31: Volume XI, Chapter 6 now adds the
first HMC/RHMC production-certificate layer.  The chapter records finite
integrator, reversibility, solver-residual, spectral-interval,
rational-approximation, and determinant-reweighting coordinates; derives the
pseudofermion action/force residual bounds and the RHMC log-reweighting
bound; and adds `qft_scripts/hmc_rhmc_finite_demo.py` as a public-facing
finite HMC/RHMC smoke module.  Remaining numerical evidence work is now
focused on full dynamical-gauge-fermion production workflows, concrete
tensor-network continuum-control examples, neural optimizer/calibration
diagnostics beyond local-energy variance, and larger workflow integration.

### Defects, Elasticity, And Goldstone Effective Theories

Statmech source: Volume II Chapter 16.

QFT target:

- Volume IX Chapters 2--4 for extended operators and defects;
- Volume X hydrodynamics and low-energy effective theory;
- possible future treatment of nonrelativistic QFT and crystalline phases.

Useful content:

- microscopic density, pair correlations, static structure factor, and
  diffraction diagnostics;
- elasticity as an effective theory, phonons, dislocations, KTHNY two-stage
  melting, and defect unbinding;
- the distinction between topological defects and topological order.

QFT action: use selectively.  The QFT monograph should not become a condensed
matter text, but elasticity and defect-unbinding examples are valuable for
clarifying Goldstone EFTs, topological defects, order-parameter spaces,
domain-wall/string/vortex sectors, and nonrelativistic effective field
theory.

### Turbulence And Closure

Statmech source: Volume IV Chapters 35 and 36.

QFT target:

- Volume X Chapters 5, 6, 8, and 11 if the monograph develops turbulent
  hydrodynamic EFTs or nonequilibrium cascades.

Useful content:

- Galerkin-regulated statistical formulation of Navier--Stokes;
- exact energy balances, spectra, structure functions, flux hypotheses, and
  the four-fifths law;
- passive scalar and Burgers turbulence as separate regimes;
- LES/RANS closure and closure validation identities.

QFT action: this is a lower-priority but genuine frontier interface.  It is
appropriate only if the QFT monograph develops hydrodynamic effective actions
beyond near-equilibrium linear response.  If included, it must be built from
regulated equations and exact balance identities before closure assumptions.

### Disorder, Replicas, And Glassy Limits

Statmech source: Volume II Chapter 15 and Volume IV Chapter 37.

QFT target:

- possible future treatment of disordered QFTs, random fixed points, replica
  limits, and supersymmetric disorder formalisms;
- Volume II Wilson--Fisher/Ising material where random-field or random-bond
  perturbations are discussed;
- Volume X if aging and glassy nonequilibrium limits are developed.

Useful content:

- fixed-sample Gibbs measures;
- replica identity and analytic-continuation obstruction;
- Parisi theory, TAP equations, cavity fields, metastates, and short-range
  spin-glass domain-wall scaling;
- glassy aging, kinetically constrained models, dynamical large deviations,
  RFOT status, point-to-set lengths, jamming, and yielding.

QFT action: treat as a possible future QFT volume or chapter cluster rather
than a near-term insertion.  The key methodological lesson is that replica
continuation must be framed as an assumption or controlled limiting theorem,
not as algebraic magic.

## Topics To Exclude Or Keep Peripheral

The following statmech topics should not be imported into the core QFT
monograph except as brief analogies or as part of a deliberately separate
nonrelativistic/statistical-physics volume:

- density functional theory and real-material hydrogen phase prediction;
- molecular dynamics workflow details, Ewald methods, and interatomic
  potentials;
- machine-learned interatomic potentials and materials active learning;
- biological/living matter;
- active matter, unless a future nonequilibrium QFT treatment is explicitly
  launched with field equations, symmetries, response coefficients, and
  stability/entropy-production analysis;
- turbulence production workflows unless the QFT volume commits to
  hydrodynamic turbulence as a technical case study.

## Suggested Missing QFT Development Backlog

1. **Volume X nonequilibrium field theory expansion.**  The finite
   path-measure layer now covers MSRJD, Doi--Peliti, fluctuation relations,
   entropy production, empirical-flow large deviations, and the finite
   Schwinger--Keldysh Gaussian noise bridge.  Remaining work is the
   continuum renormalization and dynamic-critical-model layer, including
   conserved versus nonconserved slow variables and theorem-status limits.
2. **Volume X hydrodynamic theorem-status expansion.**  Add Mori--Zwanzig,
   Green--Kubo order of limits, hydrodynamic-limit status, kinetic closure
   boundaries, and generalized hydrodynamics as a bridge to the integrability
   volume.
3. **Volume XI numerical QFT evidence expansion.**  Use statmech's numerical
   evidence discipline to strengthen lattice Monte Carlo, HMC/RHMC,
   autocorrelation/error analysis, Hamiltonian truncation, transfer-matrix/ED,
   tensor-network, and neural-variational QFT sections.
4. **Volume IX finite-locality proof laboratories.**  Use toric code,
   interacting Hall conductance, Lieb--Robinson/quasi-adiabatic continuation,
   and finite gauge theories as laboratories for generalized symmetry,
   topological defects, and TQFT boundary claims.
5. **Volume XI constructive cluster-expansion machinery.**  Develop polymer
   gases, Pirogov--Sinai, phase-sum scaling, and cluster expansion estimates
   as proof machinery rather than quoted background.
6. **Future disordered-QFT cluster.**  Consider a later chapter or volume on
   random systems, replicas, random fixed points, spin glasses, and glassy
   nonequilibrium QFT.  This should be postponed until the core Wilsonian,
   constructive, and nonequilibrium frameworks are stronger.

## Immediate Conclusion

The statmech monograph is most valuable to the QFT project in three ways:

1. It supplies a disciplined language for RG, scaling, phase claims, numerical
   evidence, and theorem-status boundaries.
2. It contains adjacent technical developments that should be reworked into
   QFT notation: stochastic field theories, fluctuation relations, hydrodynamic
   limits, open-system limits, finite topological lattice models, and numerical
   methods.
3. It marks several missing QFT-frontier areas, especially nonequilibrium
   field theory and numerical evidence standards, where the present QFT
   volumes have a skeleton but not yet the same depth.
