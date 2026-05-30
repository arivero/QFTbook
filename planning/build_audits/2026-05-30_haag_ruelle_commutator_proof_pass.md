# 2026-05-30 Haag--Ruelle Commutator Proof Pass

## Scope

This pass continues the proof-substance audit for #691 and the foundational
Haag--Ruelle layer related to #695, #527, and #528.  The target was
`prop:almost-locality-gives-hr-commutator` in Volume IV, Chapter 5.

## Manuscript Change

- Retained the proposition as genuine Haag--Ruelle proof infrastructure: the
  estimate is the locality input that turns separated velocity supports into
  Cook estimates.
- Expanded the proof from a compressed locality sentence to the full norm
  estimate:
  - selected disjoint velocity neighborhoods with distance `delta`;
  - split each Haag--Ruelle packet into near and tail pieces;
  - converted stationary-phase pointwise decay into an \(L^1\) tail bound by
    choosing the decay exponent larger than the spatial dimension;
  - chose local approximants at radius \(R=\delta |t|/8\);
  - checked the translated double cones are spacelike by comparing the minimum
    spatial separation \(\delta |t|-2R\) with the maximum time separation
    \(2R\);
  - bounded the approximant replacement error using polynomial growth of the
    near-packet \(L^1\) norm and arbitrary-power almost locality;
  - recorded the adjoint case through localization of \(B_R^*\) and
    preservation of the approximation norm.

## Status

This does not close any issue.  It removes one more compressed proof body from
the foundational scattering spine and keeps the ordinary massive
Haag--Ruelle theorem sharply separated from the unresolved charged-sector
replacement problem.
