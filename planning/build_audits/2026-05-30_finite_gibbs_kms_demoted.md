# Finite Gibbs KMS Anti-Wrapper Pass

## Scope

- Continued issue #691, the semantic theorem/proof audit.
- Targeted Volume IV, Chapter 4, in the KMS states and modular equilibrium
  section.

## Finding

The trace-class Gibbs calculation is useful because it shows exactly how
trace cyclicity becomes the KMS boundary condition.  It is nevertheless a
finite or semifinite normalization model.  The theorem-level operator-
algebraic content is the subsequent modular KMS property, where the
Tomita--Takesaki relation replaces literal trace cyclicity for type-III
local algebras.

## Change

- Demoted `Gibbs traces satisfy KMS` from proposition to example.
- Replaced the proof environment by a verification paragraph.
- Preserved the strip function, the two boundary-value computations, and the
  explanation of the two trace-cyclicity moves.
- Updated the modular KMS proof to refer to the example rather than a
  proposition.
- Added a theorem-form audit guard so the same title cannot reappear as a
  theorem/proposition/lemma/corollary wrapper.
- Updated the chapter dossier and historical KMS build audit.

## Verification

- `python3 calculation-checks/kms_foundation_checks.py`
- `python3 -m py_compile calculation-checks/kms_foundation_checks.py`

## Status

This pass reduces theorem-form presentation debt.  It does not close #691,
because the broader audit of theorem-family statements, quoted-theorem
boundaries, and method placement remains open.
