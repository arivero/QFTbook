# Build Audit: Volume VII Supersymmetric Wilsonian BV Pushforward

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 04, `Supersymmetric Wilsonian
Schemes and Exact Dynamics`, by adding an explicit finite model for the BV
pushforward claims used throughout the later holomorphy and exact-dynamics
chapters.  The aim is to make the Wilsonian scheme infrastructure
calculational rather than merely formal.

## Substantive Edits

- Added a finite circle-Darboux model with base pair `(y, eta)` and eliminated
  pair `(x, xi)`, finite Fourier modes, and BV Laplacian
  `Delta = d_y d_eta + d_x d_xi`.
- Proved in the model that the normalized fiber pushforward satisfies
  `P Delta_K = 0` and `P Delta = Delta_B P`, hence sends closed
  half-density representatives to closed representatives.
- Added the product-cycle check showing that two finite fiber pushforwards
  commute and agree with direct pushforward, matching the semigroup
  hypothesis for composable BV Wilsonian towers.
- Added `calculation-checks/susy_wilsonian_bv_checks.py` and updated the
  Chapter 04 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_wilsonian_bv_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_wilsonian_bv_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the new Wilsonian BV
  check and the existing Wolfram gamma-trace check.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed.  The rebuilt
  `monograph/tex/main.pdf` has 1856 pages and size 7,399,801 bytes.
