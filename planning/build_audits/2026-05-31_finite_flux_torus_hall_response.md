# Finite Flux-Torus Hall Response Pass

Date: 2026-05-31

## Trigger

GitHub issue #703 tracks statmech-to-QFT absorption.  The finite-locality
laboratory lane still needed an interacting Hall-response formulation that
does not collapse the many-body problem into a single-particle Chern-number
slogan.

## Edits

- Added a finite flux-torus Hall-response section to Volume IX, Chapter 7,
  immediately after the Lieb--Robinson and quasi-adiabatic machinery.
- Defined the finite many-body flux datum \(H_\Lambda(\phi)\), flux-current
  operators \(I_a=\partial_{\phi_a}H_\Lambda\), isolated band projection
  \(P_\Lambda(\phi)\), trace Berry curvature, finite Chern number, and
  flux-averaged dimensionless Hall coefficient.
- Proved the finite integer Chern-number formula by local frames, determinant
  transition functions, and winding on the flux torus.
- Derived the exact finite Kubo resolvent formula for the curvature when the
  band is an exact finite degenerate eigenvalue.
- Stated the additional locality, gap, quasi-adiabatic, and thermodynamic
  hypotheses required before the finite curvature average can be identified
  with a phase-stable Hall conductance.
- Added `calculation-checks/hall_flux_curvature_checks.py` for projector
  curvature/Kubo equality and two-band Chern-number normalization.
- Updated the calculation-check manifest, chapter dossier, and statmech
  crosswalk.

## Verification Plan

- Run the new Hall flux-curvature calculation check.
- Run theorem-form, display-label, text, negative-scope, and chapter-dossier
  audits.
- Build the monograph and scan the log.
- Comment on #703 as another completed finite-locality subpass while keeping
  the issue open for finite-gauge/TQFT boundary examples and deeper
  thermodynamic Hall-stability estimates.
