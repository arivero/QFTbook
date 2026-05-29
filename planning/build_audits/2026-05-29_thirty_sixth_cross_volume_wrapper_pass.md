# Thirty-Sixth Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: continued Issue #691 proof-substance audit.  This pass concentrated on
compact proofs whose statements are genuine structural results but whose proof
bodies had hidden analytic or geometric steps.

Changes made:

- Expanded the Rindler normal-form lemma for nonextremal horizons.  The proof
  now uses Gaussian null coordinates, identifies the surface-gravity
  coefficient in the metric, performs the explicit transformation
  \(r=\kappa\rho^2/2\), \(t=v-(2\kappa)^{-1}\log r\), and verifies the regular
  \(U,V\) null coordinates.
- Expanded the Lichnerowicz formula proof.  The proof now separates the
  connection Laplacian, \(E\)-bundle curvature, and spin-curvature terms, and
  spells out the Clifford contraction using the four-gamma term, Ricci
  cancellation, and scalar-curvature contraction.
- Expanded the pAQFT causal-support proposition for Bogoliubov fields.  The
  proof now constructs the past/future decomposition of the cutoff difference
  \(V'-V\), uses causal factorization to cancel the future factor, and displays
  the relative conjugation by the past factor.
- Expanded the finite-dimensional BV restriction/Stokes proposition.  The
  proof now explains the adapted-Darboux coordinate transformation, the induced
  Berezinian on a Lagrangian, and the divergence form of
  \(\iota_L^*\Delta_{1/2}\eta\).

No theorem-family demotion was made in this pass.  The audited statements above
carry real structural content; the appropriate repair was proof expansion, not
removal of theorem-family status.

Current count after edits:

- theorem: 94
- proposition: 367
- lemma: 29
- corollary: 10
- proof: 495
- theorem-family total: 500

The immediate short-proof queue is now 36 entries at or below 170 proof tokens.
This is lower than the previous 40 because four compact proofs were expanded
past the mechanical threshold.  The threshold remains only a queue heuristic:
the next pass should continue reading statement, hypotheses, dependencies, and
proof body before deciding between demotion and strengthening.
