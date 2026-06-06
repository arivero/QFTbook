# 2026-06-06 Issue #519 Supersymmetric Collider Central-Charge Bound

## Target

- Open issue: #519, modern energy-correlator/light-ray/conformal-collider depth.
- Chapter touched: Volume III, Chapter 10, conformal-collider one-point
  functions.
- Companion touched: `calculation-checks/conformal_collider_checks.py`.

## Change

- Added the four-dimensional \(\mathcal N=1\) supersymmetric central-charge
  specialization after the Hofman--Maldacena helicity inequalities.
- The text now states the supercurrent Ward-identity input in the same
  detector normalization:
  \[
    t_4=0,\qquad t_2=6(1-a/c).
  \]
- Substituting into the helicity eigenvalues gives
  \[
    \lambda_2=2a/c-1,\qquad
    \lambda_1=2-a/c,\qquad
    \lambda_0=3-2a/c,
  \]
  and hence \(1/2\le a/c\le3/2\).
- The text identifies the free chiral multiplet as the lower endpoint and the
  free vector multiplet as the upper endpoint.
- Extended `conformal_collider_checks.py` with
  `check_n1_susy_collider_central_charge_bound()`, which verifies the exact
  rational eigenvalue map, endpoint saturations, and negative controls for
  wrong \(t_2\) normalization or nonzero \(t_4\) at the supersymmetric identity
  point.
- Updated the calculation-check inventory and the Chapter 10 dossier.

## Re-Audit

This is physics-facing depth, not a tangential central-charge exercise.  The
new paragraph converts detector positivity into a constraint on physical
trace-anomaly data and shows which free multiplets saturate the bound.  The
supercurrent Ward identity is treated as the input map; the derivation then
uses the already-proved helicity diagonalization.  No issue or planning
metadata was inserted into TeX.

## Verification Plan

- Focused conformal-collider companion syntax/run and targeted harness.
- Focused Chapter 10 theorem/display/prose/style audits.
- Dossier, text, inventory, and evidence-contract audits.
- Relevant CFT detector companions.
- Full monograph build.
