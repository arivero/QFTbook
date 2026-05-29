# Forty-Second Cross-Volume Wrapper Pass

Date: 2026-05-29.

This pass continued the end-to-end anti-wrapper audit for theorem-family
statements whose proof bodies risk overstating their substance.

## Changes Made

- Reclassified the Euclidean spectral-continuation and long-time projection
  facts in Volume I, Chapter 5 from propositions to lemmas.  They are genuine
  spectral-calculus tools, but their mathematical level is lemma-level rather
  than proposition-level.
- Reclassified the scalar three-point and four-point cross-ratio kinematic
  results in Volume III, Chapter 8 from theorems to propositions, with label
  and reference updates.
- Demoted `Fusion of a Bethe string` in Volume VII, Chapter 13 from a
  proposition with proof to a construction with a derivation paragraph.  The
  result is a convention-sensitive fusion calculation and endpoint
  telescoping identity, not a proposition in the theorem-family sense.
- Converted `First Seeley--DeWitt coefficients` in Volume XII, Chapter 6 from
  a proposition with an incomplete proof to a quoted heat-kernel theorem,
  retaining only the parametrix origin as prose.  The previous proof sketched
  the recursion but did not explicitly carry the full \(a_4\) coefficient
  calculation.
- Added theorem-form guardrails so that `Fusion of a Bethe string` and
  `First Seeley--DeWitt coefficients` do not re-enter proposition/theorem
  form accidentally.

## Candidates Read And Retained

- `Local P-Q bridge` followed by the unimodular bridge calculation in the QSC
  chapter is already in the right shape: an assumption followed by local
  algebra, not a proposition wrapper.
- `Zhukovsky Fourier transform`, `Twist-two Baxter family`, the flat
  conformal Killing vector classification, the narrow second-sheet pole
  contraction argument, the Ising BPZ four-point derivation, and the two
  stochastic-quantization telescoping estimates were read and retained.  Each
  contains a real contour, finite-sum, differential, contraction-mapping, BPZ,
  or probabilistic estimate rather than a vacuous proof.

## Estimate Update

After this pass, the phrase-based audit has six remaining
theorem/proposition proof bodies containing suspicious words such as
`direct substitution`, `immediate`, or `telescoping`; all six were read in
this pass and retained as substantive.  The broader heuristic scan is still
noisy and produces many real theorems, so the actionable remainder is best
estimated at roughly 20--35 semantic candidates, plus the harder
assumption-heavy category that requires reading rather than grep.

