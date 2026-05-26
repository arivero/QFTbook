# Agent Handoff: Planar N=4 SYM Integrability Depth Pass

## Primary Scope

Issue: #607
Main files:

- `monograph/tex/volumes/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.tex`
- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `planning/chapter_dossiers/volume_vii/*.md`
- `calculation-checks/planar_n4_integrability_checks.py`

Secondary source spine:

- the two planar-integrability chapters in the stringbook;
- `planning/source_inventory/stringbook_crosswalk.md`;
- `claude_review.md`, especially the Block C planar-integrability depth-pass
  notes.

## Objective

Bring the planar N=4 SYM material above stringbook depth.  The current
chapters establish a scaffold but are much thinner than the internal source.
The pass must turn the scaffold into a rigorous, convention-stable, worked
development of the spectral problem, asymptotic Bethe ansatz, finite-size
TBA/Y-system, quantum spectral curve, hexagon program, and Maldacena-Wilson
line/cusp/bremsstrahlung interface.

## Conceptual Constraints

- Planar integrability is not the same subject as two-dimensional relativistic
  integrable QFT.  Keep the distinction explicit.
- Do not present integrability as a proof of N=4 SYM's nonperturbative
  existence.
- State clearly which objects are perturbative spin-chain limits, which are
  all-coupling conjectural/bootstrapped formulae, and which are checks
  against gauge/string computations.
- Do not use AdS/CFT claims as load-bearing proof unless the local statement
  is a conditional comparison.
- Avoid fashionable material unless it contributes to the foundational
  spectral problem.

## Required Development Targets

1. Define the planar single-trace Hilbert space/cohomological sector with
   cyclic trace identification and large-N inner-product normalization.
2. Derive the one-loop dilatation operator in at least one closed sector
   from explicit Wick contractions and color algebra.
3. Show the mapping to a nearest-neighbor integrable spin chain, including
   the normalization of the Hamiltonian and cyclicity/momentum constraint.
4. Derive the coordinate Bethe ansatz in the simplest sector and then
   explain the algebraic/nested Bethe ansatz extension without treating it as
   magic.
5. State the all-loop asymptotic Bethe equations with every symbol defined:
   Zhukovsky variables, rapidities, mode numbers, dressing phase, length,
   charges, and cyclicity.
6. Give a rigorous status ledger for the BES/BHL dressing phase:
   perturbative derivation, crossing equation, strong-coupling matching,
   and what is conjectural.
7. Develop finite-size corrections:
   Luescher corrections, mirror theory, TBA kernels, Y-system, and wrapping
   interactions.  Include at least one explicit small-length example.
8. Develop the QSC:
   Q-functions, analyticity strips/cuts, gluing conditions, asymptotics,
   Pfaffian/QQ constraints, and how anomalous dimensions are extracted.
9. Develop hexagon form factors:
   pair-of-pants decomposition, mirror particles, measure, crossing/mirror
   moves, and finite-size corrections.
10. Add Maldacena-Wilson line material:
    \[
      W_{\rm MW}=\operatorname{Tr} P\exp\int
      (iA_\mu \dot x^\mu+\Phi_I\theta^I|\dot x|)\,ds .
    \]
    Derive the local cusp setup, define the cusp anomalous dimension, and
    explain the small-angle Bremsstrahlung function relation with proof
    status.

## Calculation Checks

Add or extend checks for:

- one-loop SU(2) spin-chain Hamiltonian normalization;
- cyclicity/momentum constraint for short chains;
- weak-coupling expansion of Zhukovsky variables;
- selected low-loop Bethe root energies;
- simple Y-system functional relations;
- cusp small-angle coefficient arithmetic where finite.

Prefer Python for algebraic finite checks.  Keep Mathematica optional unless
the expression is much clearer in Wolfram Language.

## Dossier Updates

For each chapter touched, update:

- notation inventory for spin-chain sites, rapidities, Zhukovsky variables,
  Q-functions, Y-functions, mirror variables, and Wilson-line parameters;
- claim ledger with proof status;
- source position explaining which stringbook sections were absorbed and how
  the monograph goes further.

## Completion Standard

Do not close #607 unless all four chapters are substantially deepened and the
Maldacena-Wilson/cusp/bremsstrahlung material is integrated.  Partial passes
should comment on #607 but leave it open.
