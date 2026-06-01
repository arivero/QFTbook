# Eta Jump / Determinant-Chart Compatibility Pass

## Scope

- GitHub issue context: #696, anomaly proof-debt around APS eta conventions
  and determinant-line holonomy.
- Edited chapter: `monograph/tex/volumes/volume_xii/chapter07_eta_invariants_global_anomalies.tex`.

## Change

- Added a mechanism paragraph, not a theorem, explaining how a single
  eigenvalue crossing changes the reduced eta invariant by an integer while
  leaving the exponentiated eta phase unchanged.
- Connected that integer spectral-flow bookkeeping to the Quillen
  determinant-line spectral-cut chart transition: the low-mode determinant
  transition and the zeta determinant of the complement compensate so that
  the fermion object is a vector in the determinant line rather than a
  cut-dependent scalar.
- Updated the chapter dossier and calculation-check inventory.

## Calculation Check

- Extended `calculation-checks/eta_global_anomaly_checks.py` with an exact
  one-mode check:
  \[
    \xi_\lambda=-1/2,\;1/2,\;1/2
  \]
  for negative, zero, and positive eigenvalue signs respectively, so an upward
  crossing changes \(\xi\) by \(+1\), a downward crossing by \(-1\), and the
  phase is unchanged modulo integers.

## Status

This narrows the eta-convention and determinant-line chart boundary.  It does
not claim to prove the APS, Bismut--Freed, or real mod-two-index theorem.
