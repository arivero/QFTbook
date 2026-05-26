# Agent Handoff: Supersymmetric Gauge Dynamics And Localization

## Primary Scope

Issues: #588, #603, #605, #590, #592 where overlapping.
Main files:

- `monograph/tex/volumes/volume_vii/chapter01_supersymmetry_algebras_and_representations.tex`
- `monograph/tex/volumes/volume_vii/chapter02_superspace_superfields_local_actions.tex`
- `monograph/tex/volumes/volume_vii/chapter03_supersymmetric_gauge_theory.tex`
- `monograph/tex/volumes/volume_vii/chapter04_supersymmetric_wilsonian_schemes.tex`
- `monograph/tex/volumes/volume_vii/chapter05_nonrenormalization_holomorphy.tex`
- `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`
- `monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`
- `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `monograph/tex/volumes/volume_vii/chapter10_three_dimensional_chern_simons_matter.tex`
- `monograph/tex/volumes/volume_vii/chapter11_six_dimensional_superconformal_theories.tex`
- `monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex`

## Objective

Develop the supersymmetry volume into a rigorous treatment of SUSY algebras,
off-shell superfield variables, Wilsonian schemes, holomorphy,
non-renormalization arguments, N=1 and N=2 dynamics, localization, 2D
LG/CY/mirror symmetry, 3D Chern-Simons matter/ABJM, and 6D SCFTs.  The
development must explicitly distinguish Hilbert-space particle
representations from off-shell field-variable supermultiplets.

## Conceptual Constraints

- Never conflate a supermultiplet of particles with a supermultiplet of
  off-shell fields.
- Supersymmetric Wilsonian effective actions for gauge theories must be
  formulated using BV, lattice, or another explicit consistency framework.
- Do not claim that dimensional reduction is a mathematically consistent
  all-order regularization scheme beyond its known perturbative domain.
- Treat non-renormalization "theorems" from the physics literature as
  arguments unless their hypotheses and proof are supplied.
- Localization formulas require a theorem-boundary section: compactness of
  integration cycle, one-loop determinant definition, zero modes, singular
  loci, contour prescriptions, and instanton moduli-space compactification.

## Required Development Targets

### Supersymmetric Wilsonian Schemes

1. Define supersymmetric local coordinates in field space and source space.
2. Explain the difference between preserving supersymmetry in an integrating
   out procedure and having a manifestly supersymmetric regulator.
3. Formulate the BV quantum master equation for gauge-fixed supersymmetric
   Wilsonian actions.
4. State what is known, formal, or open about heat-kernel/Pauli-Villars,
   higher-derivative, dimensional reduction, and lattice regulators.

### N=1 Dynamics

1. Define moduli spaces of vacua as solution spaces modulo gauge equivalence,
   with complex/algebraic and symplectic quotients distinguished.
2. Derive holomorphic constraints on the superpotential and gauge coupling
   with all assumptions stated.
3. Develop the NSVZ beta function with a rigorous accounting of Wilsonian
   versus 1PI coupling, scheme dependence, Konishi anomaly, and canonical
   normalization.
4. Develop the Witten index, including the delicate 4D N=1 SYM logic:
   compactification, boundary conditions, mass gap assumptions/status, and
   relation to gaugino condensation.
5. Work through Seiberg duality examples with anomaly matching and moduli
   matching, labeled by proof status.

### N=2 Seiberg-Witten

1. Expand the SU(2) pure case with the argument-type ledger preserved.
2. Add BPS central charge, charge lattice, monodromy, wall crossing, and
   singular fibers with precise hypotheses.
3. Integrate dyonic bound-state logic after the soliton/monopole lane has
   supplied the needed classical background.
4. Avoid presenting physical derivation steps as mathematical theorems unless
   the proof infrastructure is present.

### Localization

1. Prove the finite-dimensional localization identity and identify its
   infinite-dimensional assumptions.
2. For S^4 Pestun localization, define the supercharge, fixed locus,
   one-loop determinant, instanton sector, and integration contour.
3. Prove or quote with hypotheses the H-function/Barnes double-gamma
   equivalence; do not assert it.
4. For S^3 localization, define the double sine function, FI terms,
   Chern-Simons phases, and JK-like contour issues where relevant.
5. Discuss zero-size instantons as a mathematical compactification issue, not
   as an automatic physical object.

### Lower/Higher Dimensional Examples

1. Develop 2D N=(2,2) LG models, chiral rings, tt* status, LG/CY phases, and
   Hori-Vafa mirror symmetry.
2. Develop ABJM and 3D Chern-Simons matter at the level of gauge group,
   levels, matter representation, moduli space, localization, and SCFT data.
3. Develop 6D SCFTs with anomaly polynomial, tensor branch, BPS strings, and
   status of non-Lagrangian definitions.

## Calculation Checks

Add checks for:

- R-charge/anomaly matching in N=1 examples;
- NSVZ coefficient conversion between generator normalizations;
- Seiberg-Witten monodromy matrices and symplectic pairing;
- localization one-loop determinant finite product identities;
- ABJM level/rank/parity convention checks.

## Completion Standard

Issue #588 should remain open until the N=1/N=2/ABJM/6D/localization scope is
substantially developed.  Partial commits are valuable but must be reported
as partial.
