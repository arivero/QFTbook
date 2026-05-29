# 2026-05-28 Volume II Proof-Substance Audit

Scope: Volume II proof bodies were read for mathematical content, not merely
matched by theorem/proof environment scans.  The pass asked whether each proof
constructs, estimates, computes, or reduces the stated claim to a previously
established theorem with the relevant hypotheses visible.

## Standard Applied

- A theorem/proposition/corollary environment is retained only when the proof
  performs substantive work appropriate to the statement.
- Algebraic bookkeeping, definition unpacking, status statements, and
  conditional applications of deep external theorems are moved to remarks or
  controlled-approximation form.
- Deep results whose proof is not supplied in the chapter are marked as quoted
  theorem inputs rather than silently presented as proved results.
- Structural RG, anomaly, and matching claims are not treated as theorems unless
  locality, cohomology, regulator, and limiting hypotheses are operationally
  present.

## Main Repairs

- Chapter 15b: demoted the scaling-limit-as-continuum-QFT wrapper to a remark,
  since it is an application of OS reconstruction under hypotheses rather than
  a proof performed there.
- Chapter 20: marked the spin Dirac index theorem and cubic gauge obstruction as
  quoted theorem inputs; demoted anomaly-matching and theta-branch algebraic
  identities to remarks.
- Chapter 20b: marked current-sector bosonization as a quoted theorem because
  the text checks the normalization and quadratic current functional but does
  not construct the full compact current algebra.
- Chapter 21: marked finite \(SU(2)\) anomaly and WZW-level matching as quoted
  theorem inputs; demoted anomaly-matching background-response statements,
  \(U(1)\) toy-model mass algebra, SSB anomaly matching, and electromagnetic
  anomaly specialization to remarks.
- Chapter 22: kept the leading soft photon/graviton proofs, but demoted the
  Bloch--Nordsieck binomial identity and finite-degeneracy KLN trace identity
  to remarks; marked Buchholz infraparticle obstruction as a quoted theorem.
- Chapter 23: retained the Legendre, Schwinger--Dyson, exact 1PI tree, and
  finite-regulator convexity proofs; demoted the brief diagrammatic
  one-particle-reducible statement to a remark.
- Chapter 24: retained finite-dimensional BV algebra, pushforward, and QME/RG
  computations; marked the ghost-number-one anomaly calculation as a quoted
  theorem input because the proof relies on local BRST cohomology
  classification beyond the displayed descent bookkeeping.

## Follow-Up

The quoted anomaly/cohomology and bosonization inputs are not defects by
themselves, but they mark proof obligations for later appendix-level
development if the monograph wants these statements proved internally rather
than imported as mathematical or perturbative-cohomological theorems.
