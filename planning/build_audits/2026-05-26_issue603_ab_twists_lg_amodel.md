# Build Audit: Issue #603 A/B Twist And LG/A-Model Pass

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`
- Issue: #603
- Files:
  - `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  - `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`
  - `calculation-checks/susy_2d_lg_glsm_checks.py`
  - `calculation-checks/README.md`
  - `planning/build_audits/2026-05-26_issue603_ab_twists_lg_amodel.md`

## Mathematical Content Added

- Defined the two-dimensional A/B twist spin-shift convention with explicit
  Lorentz, vector-`R`, and axial-`R` charge table for the four supercharges.
- Proved that `Q_A = bar Q_+ + Q_-` and
  `Q_B = bar Q_+ + bar Q_-` are scalar nilpotent supercharges in the
  central-charge-free local sector.
- Stated the vector and axial anomaly requirements for the A and B twists,
  including the axial GLSM charge-sum obstruction.
- Replaced the earlier compressed B-sector paragraph with a theorem-quality
  B-twisted Landau-Ginzburg section:
  - connected the twist scalar to the already-defined `Q_B` local
    differential;
  - proved that the Morse residue functional descends to `Jac(W)`;
  - proved nondegeneracy of the residue pairing for nondegenerate critical
    points;
  - recorded the genus-`g` zero-mode formula as a finite determinant
    calculation conditional on regulator, determinant-line, and boundary
    hypotheses.
- Added an A-twisted sigma-model zero-mode section:
  - proved that the constant-map algebra is the de Rham complex of the target;
  - stated the classical holomorphic-map energy decomposition and named the
    compactification/orientation/contact-term inputs needed for full
    A-model correlators.
- Kept the presentation intrinsic to two-dimensional QFT.  No mirror-duality,
  D-brane, superstring, or string-compactification argument is used.

## Calculation Checks

- Extended `calculation-checks/susy_2d_lg_glsm_checks.py` with the A/B twist
  spin-shift ledger and scalar-supercharge nilpotence checks.

## Verification

- `python3 calculation-checks/susy_2d_lg_glsm_checks.py` passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram
  gamma-trace/anomaly-normalization check.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before staging.
- `tools/build_monograph.sh` passed after rebasing onto `origin/main` and
  produced `monograph/tex/main.pdf` with 1771 pages.
- A reference-folder guard found no staged, modified, or untracked
  `references/` files in this pass.
