# Build Audit: Volume VII Holomorphy And NSVZ Foundations

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 05, `Nonrenormalization and
Holomorphy`, by making two recurrent foundations explicit: tree-level
elimination of massive chiral coordinates and the differentiation of the
holomorphic-canonical gauge-coordinate relation into the NSVZ beta function.
Both are treated as Wilsonian coordinate statements under stated hypotheses,
not as informal path-integral slogans.

## Substantive Edits

- Added a proposition proving that tree-level elimination of a massive
  chiral block preserves holomorphy when the heavy-field Hessian is
  invertible, using the holomorphic implicit-function theorem.
- Added the quadratic heavy-field formula
  `W_eff = W_0 - (1/2) J_a (M^{-1})^{ab} J_b`, including the boundary where
  `det M=0` means the elimination patch has broken down.
- Promoted the NSVZ beta-function step to a named proposition deriving the
  beta function by differentiating the holomorphic-canonical coordinate
  relation with the monograph anomalous-dimension convention.
- Added `calculation-checks/susy_holomorphy_nsvz_checks.py` and updated the
  Chapter 05 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_holomorphy_nsvz_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_holomorphy_nsvz_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the new holomorphy
  and NSVZ coordinate check and the existing Wolfram gamma-trace check.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` with 1856 pages and file size 7396421 bytes.
