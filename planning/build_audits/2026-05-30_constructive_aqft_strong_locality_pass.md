# Constructive AQFT Strong-Locality Pass

Date: 2026-05-30.

Scope:
`monograph/tex/volumes/volume_iv/chapter03_algebraic_qft_local_nets_and_states.tex`.

## Repair

- Expanded the massive \(P(\phi)_2\) interacting checkpoint from a compressed
  example into an explicit AQFT verification route.
- Added Lemma `lem:analytic-vector-strong-locality`, which proves that a
  common invariant domain, essential self-adjointness, joint entire
  analytic-vector estimates, and domain commutativity imply strong
  commutation of self-adjoint closures.
- Clarified that Wightman locality of unbounded smeared fields is not itself
  locality of the generated von Neumann algebras; spectral-projection
  locality requires the strong-commutation step.
- Separated the data obtained directly from OS reconstruction from the
  additional model estimates needed for nuclearity, split inclusions, Haag
  duality, and DHR reconstruction.
- Added the missing Volume IV Chapter 3 dossier so the local-net chapter is
  covered by the chapter-dossier audit surface.

## Standard Applied

The added lemma is retained as theorem-level material because the proof
constructs a genuine operator-algebraic bridge: it turns domain commutativity
of unbounded fields into commutation of bounded spectral projections.  The
model-specific AQFT consequences are written as proof obligations and
verification route, not as automatic theorems hidden inside the phrase
`constructive \(P(\phi)_2\)`.
