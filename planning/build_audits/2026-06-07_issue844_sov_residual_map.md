# 2026-06-07 Issue #844 SoV Residual-Map Re-Audit

## Scope

- Target issue: #844, formal status machinery should not overstate physical
  control.
- Target chapter: Volume VI Chapter 5B, the SoV-to-observable reconstruction
  surface after the finite-chain spectral trace identity.

## Changes

- Demoted the reader-facing block from a controlled approximation to
  `rem:sov-observable-reconstruction-map`.
- Rephrased the display as an exact residual decomposition.  The epsilon
  inequality is now explicitly conditional on separate component estimates in
  one Euclidean-correlator norm.
- Clarified the status of the residuals: finite SoV completeness can make
  `R_comp = 0`; regulator convergence, spectral tails, operator matrix
  elements, and state replacement remain model-specific physical estimates.
- Renamed the nested-integrability companion from residual-budget language to
  residual-map language and added a status guard that rejects treating named
  differences as controlled estimates.

## Re-Audit

- This is a status/architecture repair, not a new integrable-model theorem.
- The finite SoV trace identity remains a genuine finite-dimensional
  proposition.
- No physical local-QFT correlator is claimed from SoV algebra alone.
