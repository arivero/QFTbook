# 2026-05-30 Transfer-Matrix Partial-Trace Proof Pass

## Scope

This pass continues issue #691 by rereading the short transfer-matrix
commutativity proof in Volume VI, Chapter 4A, in light of the standing
anti-wrapper directive.

## Decision

The proposition was retained.  The statement is load-bearing finite-dimensional
integrability algebra: it is the point at which the Yang--Baxter equation
produces commuting Hamiltonians and later Bethe--Yang quantization data.  The
proof needed more precision, not demotion.

## Manuscript Change

- Expanded the partial-trace step so the equality
  \(t(u)t(v)=\operatorname{tr}_{0,0'}(T_0(u)T_{0'}(v))\) is not treated as a
  slogan.
- Made explicit that cyclicity is used only for the finite auxiliary trace
  over \(V_0\otimes V_{0'}\); the quantum-space endomorphism order is
  preserved and is not cycled.
- Wrote the conjugation by \(R_{00'}(u-v)\) on the auxiliary invertibility
  locus and the extension as a meromorphic endomorphism-valued identity.
- Updated the Volume VI, Chapter 4A dossier.

## Status

This pass strengthens a compact but genuine proposition rather than demoting
it.  Issue #691 remains open because other short theorem-family proofs still
need statement-by-statement reading.
