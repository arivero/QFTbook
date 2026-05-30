# 2026-05-30 SU2 Nf2 Plucker Wrapper Pass

## Scope

This pass continues the anti-wrapper audit tracked in issue #691.  The target
was the classical \(SU(2)\), \(N_f=2\) SQCD Pfaffian/Plucker quotient in
Volume VII, Chapter 8.

## Manuscript Change

- Demoted the classical quotient from proposition/proof form to derivation
  prose.  The calculation constructs the antisymmetric invariants
  \(V^{IJ}=\epsilon^{ab}P_a^IP_b^J\), fixes the Pfaffian convention, derives
  \(\operatorname{Pf}(V)=0\), reconstructs a doublet representative on a
  nonzero Plucker chart, and records the invariant-ring generation input and
  dimension count.
- Updated the following quantum-deformation lemma so it refers to the actual
  classical hypersurface equation rather than to a theorem-family wrapper.
- Updated the Volume VII, Chapter 8 dossier to identify the classical
  quotient as derivation material and the quantum-deformation statement as the
  conditional algebraic lemma.
- Added the former title to the theorem-form audit harness so the same
  finite Plucker calculation is not reintroduced as a proposition.

## Status

The invariant-theory material remains in the monograph because it fixes
coordinates and conventions needed for the later supersymmetric dynamics.  It
is no longer presented as if the finite algebra calculation were a deep QFT
theorem.  Issue #691 remains open because the global end-to-end audit still
has other theorem-family wrappers and proof-debt clusters.
