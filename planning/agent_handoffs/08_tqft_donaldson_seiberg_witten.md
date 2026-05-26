# Agent Handoff: Witten-Donaldson Theory And The Seiberg-Witten Comparison

## Primary Scope

Issue: #569.
Main file:

- `monograph/tex/volumes/volume_viii/chapter08_witten_donaldson_seiberg_witten_comparison.tex`

Related files:

- `monograph/tex/volumes/volume_viii/chapter01_metric_independence_and_cohomological_observables.tex`
- `monograph/tex/volumes/volume_viii/chapter07_twists_of_supersymmetric_theories.tex`
- `monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`
- `planning/chapter_dossiers/volume_viii/*.md`

## Objective

Develop Witten-Donaldson theory and the Donaldson/Seiberg-Witten comparison
as a serious cohomological-QFT chapter.  The chapter must define the
Donaldson side through instanton moduli spaces and observables, define the
Seiberg-Witten side through monopole equations and invariants, and then
state the physical RG-flow explanation as a conditional argument with
explicit analytic gaps.

## Conceptual Constraints

- Do not present the physics RG argument as a mathematical proof unless the
  analytic hypotheses are actually proved.
- Do not treat the Seiberg-Witten monopole equations as a mysterious
  replacement for instantons.  Explain the effective Abelian theory and its
  topological twist.
- Define every moduli space, compactification issue, orientation line, and
  virtual dimension.
- Keep Donaldson invariants, Seiberg-Witten invariants, and Witten's simple
  type formula distinct.
- The goal is to make the RG-flow explanation as mathematically sharp as
  possible, thereby identifying exactly what remains to be proved.

## Required Development Targets

1. Define four-manifold hypotheses: smooth, closed, oriented, Riemannian,
   \(b_2^+\), spin^c structures, and bundle data.
2. Define the ASD instanton moduli space:
   connections modulo gauge, ASD equation, irreducibles, deformation
   complex, index/virtual dimension, orientation.
3. Define Donaldson observables via descent from the universal bundle and
   the \(\mu\)-map.
4. Define Donaldson invariants and the simple-type condition.
5. Define Seiberg-Witten equations:
   spin^c structure, spinor bundle, determinant line, Dirac operator,
   curvature equation, gauge quotient, deformation complex, expected
   dimension.
6. Define Seiberg-Witten invariants including chamber dependence where
   relevant.
7. State Witten's simple-type formula explicitly, with all coefficients,
   signs, basic classes, and generating functions defined.
8. Derive the physics argument:
   topologically twisted N=2 SU(2) theory, Coulomb branch, singular points,
   monopole/dyon hypermultiplets, low-energy Abelian topological field
   theory, u-plane contribution, and monopole contributions.
9. Identify analytic gaps:
   nonperturbative construction of the twisted theory, rigorous RG flow from
   non-Abelian UV theory to Abelian monopole EFT, measure matching, wall
   crossing, compactification of moduli integrals.
10. Add a theorem/open-problem ledger separating:
    - mathematically proven Donaldson/SW statements;
    - physics-derived comparison formulas;
    - open RG-flow proof obligations.

## Calculation Checks

Add checks for:

- index/virtual dimension formulas for ASD and SW complexes;
- intersection-form sign conventions;
- simple-type generating-function coefficients in toy examples;
- spin^c characteristic class parity checks.

## Completion Standard

Do not close #569 unless Witten's formula is displayed and the Donaldson/SW
comparison is developed with definitions, moduli-space data, and a sharp
status ledger.  A chapter that merely says "RG flow gives SW" is not
acceptable.
