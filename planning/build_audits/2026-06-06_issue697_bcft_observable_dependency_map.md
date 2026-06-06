# 2026-06-06 issue #697 BCFT observable dependency map audit

## Target

- Primary issue: #697, Volume V CFT quoted-theorem / sewing proof-debt.
- Cross-cutting issue: #844, formal-status architecture should be consolidated
  and reconnected to physical observables.
- Chapter: Volume V, Chapter 14, `Boundary Conformal Field Theory`.

## Scope Judgment

This is an argument-architecture and physics-output pass, not another finite
sewing cell.  The chapter already contains many local identities.  The weak
point was how a reader should assemble them after repeated insertions: annulus
spectra, disk one-point data, boundary OPE coefficients, classifying
idempotents, two-point pairings, Liouville contour data, and boundary entropy
were all present, but the final map still used proof-status vocabulary and
could read as a collection of local tests.

## Manuscript Change

- Replaced the reader-facing closing "proof-status ledger" paragraph with a
  boundary-observable construction dependency map.
- The revised text starts from physical BCFT outputs:
  \(Z_{ab}(q)\), disk one-point coefficients, bulk-boundary coefficients,
  boundary OPE tensors, two-point pairings, defect endpoints, and
  boundary entropy.
- It states that these outputs are tied together only when they are produced
  from the same boundary Hilbert spaces, operator domains, normalizations, and
  sewing maps.
- It explicitly separates the roles of the diagonal Ising cell, the pointed
  \(G/H\) rational laboratory, the Liouville/FZZT nonrational coordinates, and
  the boundary-entropy gradient result.

## Companion Evidence

- Extended `calculation-checks/bcft_cardy_checks.py` with
  `check_bcft_observable_dependency_separation()`.
- The new exact finite diagnostic keeps the same endpoint annulus shadow while
  changing the boundary two-point observable, and keeps the same semisimple
  multiplication while changing disk idempotent pairings through the Frobenius
  functional.  It also records an exact residual-layer budget so omitting any
  observable layer under-controls the construction claim.
- Updated the calculation-check README and the Ch14 dossier.

## Re-Audit Notes

- This pass deliberately avoids adding another theorem-like statement in the
  manuscript.
- It removes a reader-facing status-vocabulary hotspot from the chapter and
  replaces it with a physical-observable reading order.
- It leaves the full analytic nonrational and generated all-surface sewing
  obligations open.
