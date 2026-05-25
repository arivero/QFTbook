# Build Audit: Issue 547 NSVZ Coordinate Relation

Date: 2026-05-25

## Scope

Substantive development pass on
`monograph/tex/volumes/volume_vii/chapter05_nonrenormalization_holomorphy.tex`,
addressing the asserted holomorphic-canonical gauge-coordinate relation used
in the NSVZ beta-function derivation.

## Mathematical Changes

- Promoted the coordinate relation to a proposition with explicit hypotheses
  on the Wilsonian holomorphic coordinate, canonical gauge coordinate, matter
  wave-function coordinates, and regulator-level Jacobians.
- Introduced \(X_h=8\pi^2/g_h^2\) and derived the factor
  \(\Delta X_h=2T(R)\alpha\) from the Konishi Jacobian coefficient.
- Derived the matter contribution
  \(-\sum_iT(R_i)\log Z_i\) from the canonical rescaling
  \(\Phi_i^{\rm hol}=Z_i^{-1/2}\Phi_i^{\rm can}\).
- Added the gauge-multiplet rescaling step in a background-gauge BV complex,
  explaining why the whole vector/ghost/antifield complex must be rescaled
  and why the local chiral Jacobian contributes
  \(C_2(G)\log g^2\).
- Identified \(\kappa\) as the finite \(\mu\)-independent difference between
  the chosen local coordinate charts.
- Updated the Volume VII Chapter 5 dossier.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` was rebuilt
  without log-scan failures.
- `pdfinfo monograph/tex/main.pdf` reports 1268 pages.
