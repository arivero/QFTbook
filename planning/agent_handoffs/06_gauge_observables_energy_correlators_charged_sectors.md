# Agent Handoff: Gauge Observables, Energy Correlators, Jets, And Charged Sectors

## Primary Scope

Issues: #519, #526, #527, #528.
Main files:

- `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `monograph/tex/volumes/volume_iii/chapter10_light_ray_operators_and_energy_correlators.tex`
- `monograph/tex/volumes/volume_i/chapter12_haag_ruelle_scattering_theory.tex`
- `monograph/tex/volumes/volume_i/chapter13_lsz_reduction_and_the_s_matrix.tex`
- `monograph/tex/volumes/volume_i/chapter19_quantum_electrodynamics_and_external_states.tex`
- `monograph/tex/volumes/volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex`

## Objective

Develop detector observables and charged-sector scattering carefully enough
to avoid the usual particle-physics sloppiness around jets and charged
particles.  Energy correlators are nonperturbatively defined, infrared-safe
observables and should become the conceptual anchor.  Charged particles in
gauge theories require Wilson-line dressed operators and a generalized LSZ
logic, separate from infraparticle/IR divergence issues.

## Conceptual Constraints

- Do not define jets as final-state partons.
- Do not treat hadronization as a perturbative theorem.
- Do not apply ordinary Haag-Ruelle to charged sectors created only by
  gauge-invariant nonlocal dressings.
- Do not conflate Wilson-line dressing with a mere gauge-fixing artifact.
- S-matrix perturbation theory must remain downstream of nonperturbative
  scattering definitions and LSZ.
- Energy correlators should be defined as observables, not as event-shape
  folklore.

## Required Development Targets

### Energy Correlators And Light-Ray Operators

1. Define the energy-flow operator from the stress tensor, with smearing and
   limiting procedure stated.
2. Define \(n\)-point energy correlators and their domain as detector
   observables.
3. Prove positivity and basic covariance properties under stated
   assumptions.
4. Derive the conformal-collider one-point and two-point constraints where
   feasible, with all angular integrals shown.
5. Develop the light-ray OPE status: what is proven in CFT, what is expected
   in QCD-like theories, and what is perturbative.
6. Connect energy correlators to factorization and anomalous dimensions only
   after the observable is nonperturbatively defined.

### Jets And Hadronization

1. Define infrared and collinear safety as a property of observables.
2. Define jet algorithms at the level of final-state momenta/energy flow,
   not partons.
3. Treat soft drop, N-subjettiness, and track functions only if precise
   definitions and factorization status can be stated.
4. Discuss hadronization as a nonperturbative transition from QCD dynamics to
   detector observables, not as a model-independent theorem.

### Charged-Sector Haag-Ruelle/LSZ

1. State why compactly localized gauge-invariant operators cannot create
   charged states in the usual way.
2. Define Wilson-line dressed charged operators and their dependence on
   asymptotic direction/framing.
3. Formulate a charged-sector scattering problem with flux sectors or
   asymptotic electromagnetic fields.
4. Develop a generalized LSZ proposal for correlators with Wilson-line
   insertions.  Label as a program/open problem where the proof is not
   complete.
5. Separate this structural obstruction from the infraparticle issue in QED.

## Calculation Checks

Add checks for:

- angular integrals in conformal-collider constraints;
- energy-correlator normalization in free scalar/fermion/vector examples;
- Wilson-line eikonal denominator signs and Fourier transforms;
- IR-safe observable limits in finite toy examples.

## Completion Standard

Do not close #527/#528 unless the Wilson-line dressed scattering framework is
substantially developed and its open problems are honestly stated.  Do not
close #519 unless the energy-correlator chapter contains definitions,
derivations, and at least one substantial example.
