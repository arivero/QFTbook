# 2026-05-30 pAQFT Local-Net Proof Pass

## Scope

This pass continues the proof-substance audit for issue #691 and also touches
the foundational/AQFT proof-debt lane #695.  The target was Volume IV,
Chapter 3, `Perturbative interacting local net`.

## Decision

The statement is retained as proposition-level material.  It is a structural
pAQFT construction from Epstein--Glaser time-ordered products, causal
factorization, relative \(S\)-matrices, and the time-slice quotient, not a
calculation wrapper.  The previous proof was too compressed, especially at
the relative \(S\)-matrix locality step.

## Manuscript Change

- Clarified covariance: a symmetry sends the \(V\)-net to the \(gV\)-net, and
  becomes covariance of a single net only when the interaction is invariant.
- Stated the three-functional causal-factorization identity used by the
  relative \(S\)-matrix proof, rather than relying on an unstated shorthand.
- Expanded isotony as the inclusion-induced homomorphism on generators and
  quotient relations.
- Spelled out the time-slice quotient as the identification of generators in
  a region with representatives supported in a subregion containing a Cauchy
  surface.
- Derived the relative causal-factorization identity
  \(\mathcal S_V(F+G)=\mathcal S_V(F)\star_H\mathcal S_V(G)\) by placing the
  interaction \(V\) as the middle functional in causal factorization.
- Used the two available causal orderings for spacelike separated supports to
  prove commutativity of the relative \(S\)-matrix generators.

## Verification Plan

Run the standard text/proof-form audits and rebuild the monograph before
committing, since the TeX source changed.
