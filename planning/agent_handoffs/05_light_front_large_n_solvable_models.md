# Agent Handoff: Light-Front Quantization, The 't Hooft Model, And Large-N Solvable Models

## Primary Scope

Issue: #596.
Likely files:

- new Volume II or Volume XI chapter on light-front quantization;
- new or expanded chapter for the 't Hooft model;
- `monograph/tex/volumes/volume_vii/chapter10_three_dimensional_chern_simons_matter.tex`
- `calculation-checks/` scripts for principal-value kernels and large-N
  color factors.

## Objective

Develop light-front quantization as a mathematically controlled framework
where it is actually useful, then use it for the 't Hooft model and selected
large-N vector/Chern-Simons matter examples.  The chapter must not use
light-front slogans.  It must define the Hilbert space, constraints, zero
modes, gauge choices, principal-value prescriptions, and large-N limit.

## Conceptual Constraints

- Light-front quantization is not automatically equivalent to equal-time
  quantization.  State the hypotheses and zero-mode issues.
- Gauge fixing \(A_-=0\) leaves constraints and residual gauge
  transformations; define them.
- Principal-value prescriptions are part of the definition of the regulated
  problem, not optional notation.
- Large-N factorization is a statement about a limit of correlation functions
  or matrix elements; state the normalization.
- Keep spin-chain planar N=4 SYM separate from this lane except for
  cross-references.

## Required Development Targets

1. Define light-front coordinates, metric convention, momentum variables,
   and the light-front Hamiltonian \(P^-\).
2. Derive canonical commutation relations on a light-front slice and identify
   constrained versus dynamical variables.
3. Analyze zero modes and boundary conditions; state what is controlled and
   what remains a subtlety.
4. Develop light-front gauge in two-dimensional gauge theory.
5. Derive the 't Hooft equation from large-N QCD2:
   color algebra, meson wavefunction, principal-value kernel, quark masses,
   and boundary behavior.
6. Prove basic spectral properties of the 't Hooft integral operator as far
   as feasible, or state precise theorem boundaries.
7. Work out special limits: massless case, large excitation asymptotics, and
   endpoint exponents.
8. Develop baryons in large-N QCD2 if feasible: Hartree equation and status.
9. Add 3D Chern-Simons matter in the 't Hooft limit:
   gauge choice, matter content, exact planar two-point/three-point
   structures where derivable, thermal/free-energy status if included.
10. Cross-link to Volume X only for thermal aspects; avoid duplicating the
    thermal volume.

## Calculation Checks

Add checks for:

- SU(N) color contractions in large-N normalization;
- simple discretized principal-value kernel symmetry;
- endpoint exponent algebra for the 't Hooft equation;
- Chern-Simons level/rank/'t Hooft coupling convention conversions.

## Completion Standard

Do not close #596 until the 't Hooft model is fully worked out and the
light-front framework is defined with its zero-mode and gauge constraints.
3D CS-matter may be a second-stage close condition if the issue text demands
it; otherwise comment explicitly what remains.
