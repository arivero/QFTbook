# Issue #519 / #697 Light-Ray OPE Theorem-Boundary Mechanism Pass

## Scope

This pass strengthens the CFT light-ray OPE boundary used by the
energy-correlator program.  It does not claim to reprove the full Lorentzian
CFT theorem inside the chapter.  It replaces a too-compressed quoted-theorem
use with the proof mechanism and convergence data that make the theorem a
mathematical statement.

## Manuscript Changes

- Expanded Volume III, Chapter 10 after
  `qthm:light-ray-ope-boundary`.
- The text now states the OPE as a transverse distribution statement on
  detector tests approaching the diagonal, with coefficient distributions,
  transverse descendants, and light-ray operators.
- The proof mechanism is separated into Lorentzian contour/analyticity
  control, Regge or operator-growth bounds needed to exchange null integrals
  with the inversion expansion, and a transverse-distribution remainder
  estimate.
- The CFT fixed-point statement is explicitly separated from the
  renormalized QCD small-angle EEC datum, which requires scale, mixing,
  endpoint contact, and mass-gap remainder data.

## Calculation Check

- Extended `calculation-checks/conformal_collider_checks.py` with the finite
  transverse homogeneity ledger for light-ray OPE coefficient distributions.

## Status

This advances GitHub issues #519 and #697.  It should not close either issue:
the full all-order renormalized QCD light-ray OPE/mixing theorem and broader
high-loop/frontier energy-correlator development remain open.
