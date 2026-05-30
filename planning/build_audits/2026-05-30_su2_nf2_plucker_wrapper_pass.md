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
- Updated the Volume VII, Chapter 8 dossier to identify the classical
  quotient as derivation material.
- Added the former title to the theorem-form audit harness so the same
  finite Plucker calculation is not reintroduced as a proposition.

## Follow-Up In Same Cluster

The next read found that the quantum-deformation block itself still had
lemma/proof form even though its own statement identified
\(\operatorname{Pf}(V)=\Lambda_h^4\) as the Wilsonian dynamical input and
the rest as algebra.  That block has also been demoted to prose.  Smoothness
of the hypersurface, Darboux reduction of the antisymmetric mass matrix, the
two-vacuum \(F\)-term solution, the superpotential values, and holomorphic
threshold matching remain explicit, but no longer appear as a theorem-family
claim.

## Status

The invariant-theory and deformation-algebra material remains in the
monograph because it fixes coordinates and conventions needed for the later
supersymmetric dynamics.  It is no longer presented as if these finite algebra
calculations were deep QFT theorems.  Issue #691 remains open because the
global end-to-end audit still has other theorem-family wrappers and
proof-debt clusters.
