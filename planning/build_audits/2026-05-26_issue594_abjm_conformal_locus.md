# Build Audit: Issue #594 ABJM Conformal Locus Pass

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`
- Issue: #594, partial ABJM worked-example component
- Files:
  - `monograph/tex/volumes/volume_vii/chapter10_three_dimensional_chern_simons_matter.tex`
  - `planning/chapter_dossiers/volume_vii/chapter10_three_dimensional_chern_simons_matter.md`
  - `calculation-checks/susy_abjm_6d_checks.py`
  - `calculation-checks/README.md`
  - `planning/build_audits/2026-05-26_issue594_abjm_conformal_locus.md`

## Mathematical Content Added

- Added a fixed-QFT-datum definition of a local conformal manifold, with
  tangent vectors represented by dimension-\(d\) scalar-primary deformations
  modulo redundant directions.
- Stated the standard ABJM conformal-class hypotheses: fixed
  `U(N)_k x U(N)_{-k}` gauge datum, integer level, standard line lattice,
  zero masses/FI coordinates, and preserved `N=6`, `SU(4)` structure.
- Proved that the standard ABJM conformal locus at fixed `(N,k)` is
  zero-dimensional: the Chern-Simons level is integral, the enhanced
  supersymmetry fixes `h_ABJM=2 pi/k`, real masses/FI coordinates are
  dimension-one deformations, Yang-Mills terms are dimensionful regulator or
  UV-completion data, and background contact terms are quantized scheme data.
- Added an explicit limitation: less-symmetric `N=2` marginal candidates are
  separate theories requiring their own beta-function, current-moment-map,
  and monopole-sector analysis.

## Calculation Checks

- Extended `calculation-checks/susy_abjm_6d_checks.py` with exact finite
  checks for:
  - the quartic ABJM superpotential's engineering marginality in `3D`;
  - the normalized `h*k` relation;
  - the zero tangent dimension of the integer level lattice and the standard
    `N=6` superpotential coefficient;
  - the dimension-one status of real masses, FI coordinates, and `g_YM^2`.

## Verification

- `python3 calculation-checks/susy_abjm_6d_checks.py` passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram
  gamma-trace/anomaly-normalization check.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before staging.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf` with 1779 pages.
- A final log scan found no unresolved-reference, citation, TeX insertion,
  overfull/underfull box, fatal, emergency-stop, or undefined-control-sequence
  warnings in `monograph/tex/main.log`.
- No `references/`, `.claude/`, or `claude_review.md` file is part of the
  intended staged set for this pass.
