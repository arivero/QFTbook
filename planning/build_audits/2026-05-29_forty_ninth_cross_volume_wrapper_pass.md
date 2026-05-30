# Forty-Ninth Cross-Volume Wrapper Pass

Date: 2026-05-29

Purpose: continue issue #691 after checkpoint `1049f7a2` by reading another
short-proof/high-risk batch where theorem-family rank could be disguising a
calculation, a support identity, or a controlled approximation.

## Demoted Out Of Proposition/Theorem Rank

- Volume I, Chapter 14:
  `Sharp-momentum density limit` is now an example.  It is the regulated
  delta-square density check behind the plane-wave cross-section formula, not a
  theorem about scattering theory.
- Volume II, Chapter 14:
  `Large-\(N\) critical saddle` is now an example.  The derivation remains
  explicit, but the item is a model calculation at the \(N=\infty\) saddle
  rather than an independent proposition.
- Volume II, Chapter 24:
  `Infinitesimal BV RG preserves the QME` is now a lemma.  The content is the
  immediate nilpotency consequence of defining a BV-compatible infinitesimal
  step as a \(\Delta_{1/2}\)-exact half-density variation; theorem rank would
  overstate the result.
- Volume V, Chapter 12:
  `Screenings produce Virasoro intertwiners` is now a lemma.  It is a reusable
  Coulomb-gas support fact: weight-one screening currents integrate to
  Virasoro intertwiners when the cycle boundary term vanishes.
- Volume VII, Chapter 12:
  `Two-magnon BMN quantization at one loop` is now an example.  The finite
  Bethe-equation algebra and BMN limit remain, but the item is explicitly a
  normalization calculation.
- Volume II, Chapter 19c:
  `Dispersive form of leading HVP` is now a lemma.  It is a formula lemma from
  the once-subtracted spectral representation plus the one-loop Pauli-kernel
  insertion.
- Volume X, Chapter 12:
  `UV continuous flavor anomaly polynomial` is now a lemma.  It is the
  convention-sensitive Chern-character ledger for CFL anomaly matching.
- Volume XII, Chapter 5:
  `Late-time packet occupation` is now a controlled approximation.  The
  statement explicitly depends on the stationary late-time ray-tracing
  approximation and should not be presented as an unconditional proposition.

## Harness Update

`tools/audit_theorem_form.py` now rejects recurrence of the newly demoted
calculation-wrapper titles if they reappear as theorem-family statements.

## Retained After Reading

This pass also reread several neighboring compact statements.  The
two-dimensional anomaly contact term, Schwinger-model anomaly-induced electric
field, Haag--Ruelle scalar wave-operator isometry, optical theorem, exact
spectral-pole statements, RTT/transfer-matrix algebra, and BV pushforward/QME
statements remain structurally meaningful in their present ranks.  They are
short because they sit on earlier definitions or constructions, not because
they are decorative algebra.

## Remaining Work

The audit is still not finished.  The remaining queue is now dominated less by
obvious substitution proofs and more by conditional statements whose substance
may be hidden in hypotheses.  The next pass should continue reading local-net,
constructive/RG, integrability, microlocal, and localization statements as
complete statement-hypothesis-proof units.
