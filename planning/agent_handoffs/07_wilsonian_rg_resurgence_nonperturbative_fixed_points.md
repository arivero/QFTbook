# Agent Handoff: Wilsonian RG, Nonperturbative Fixed Points, Resurgence

## Primary Scope

Issues: #503 and #505.
Main files:

- `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`
- `monograph/tex/volumes/volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`
- `monograph/tex/volumes/volume_xi/chapter07_rigorous_renormalization_group.tex`
- possible new chapter/appendix on asymptotics and resurgence;
- `calculation-checks/borel_laplace_checks.py` and related scripts.

## Objective

Deepen Wilsonian RG beyond perturbative slogans and develop asymptotic
analysis/resurgence carefully.  The lane should clarify nonperturbative
fixed-point theory, rigorous RG state of the art, BPHZ/Polchinski relations,
Borel-Laplace summation, Lefschetz thimbles, and renormalons without
propagating informal lore.

## Conceptual Constraints

- The existence of a nonperturbative Wilsonian fixed point is a theorem only
  in a specified framework with a topology and map.  Do not state it
  abstractly as fact.
- "Universality class" must be defined as an equivalence relation or as a
  controlled basin-of-attraction statement with specified observables.
- BPHZ is perturbative.  Polchinski RG can be perturbative or
  finite-regulator exact depending on the statement.  Do not conflate them.
- A formal asymptotic series is not a function.  State summability and
  analytic-continuation hypotheses.
- Renormalons must be presented with precise status; do not use them as
  slogans for "nonperturbative ambiguity."

## Required Development Targets

### Wilsonian RG

1. Define the Wilsonian effective action as a finite-regulator object first.
2. Define RG maps on a Banach or Frechet space of coordinates when possible;
   otherwise label formal power-series status.
3. Define fixed points, relevant/irrelevant directions, stable manifolds, and
   scaling operators with actual linearization data.
4. Develop the state of rigorous nonperturbative RG, including work by
   Rychkov and collaborators, but do not import claims without checking
   hypotheses.
5. Rewrite "universality class" in precise terms:
   basin of attraction modulo redundant coordinates and observable matching.
6. Add examples: Gaussian fixed point, Wilson-Fisher in \(4-\epsilon\) as a
   formal perturbative fixed point, and lattice/constructive examples with
   proven status.

### BPHZ / Polchinski

1. State BPHZ as an all-orders formal perturbative renormalization theorem.
2. State Polchinski's renormalizability theorem in its precise perturbative
   form and finite-cutoff exact RG identity separately.
3. Construct coordinate maps only where the map is actually displayed or
   recursively defined.
4. If proving equivalence at fixed loop order, give remainder estimates and
   specify the norm/topology.  Otherwise downgrade to a conditional theorem
   or open problem.

### Resurgence

1. Define Gevrey asymptotics, Borel transform, Borel summability, lateral
   sums, Stokes automorphisms, and alien calculus only to the extent needed.
2. Work out zero-dimensional and one-dimensional examples fully.
3. Develop Lefschetz thimbles:
   complexification, Morse function, downward/upward flows, intersection
   numbers, and Stokes jumps.
4. Discuss perturbative QFT Borel summation only where the analytic theorem
   exists or the statement is labeled formal.
5. Treat renormalons as a precise singularity problem in the Borel plane with
   stated assumptions, not as an explanation-by-name.

## Calculation Checks

Add/extend checks for:

- Borel transform coefficients in toy integrals;
- saddle/thimble intersection signs in finite examples;
- one-loop Polchinski flow in a finite-dimensional toy model;
- Wilson-Fisher beta-function fixed-point algebra;
- coordinate-change Jacobian arithmetic where finite.

## Completion Standard

Do not close #505 unless nonperturbative fixed-point language is made precise
and the rigorous status is clearly developed.  Do not close #503 unless
Borel-Laplace and Lefschetz-thimble sections contain full definitions,
worked examples, and status labels for QFT applications.
