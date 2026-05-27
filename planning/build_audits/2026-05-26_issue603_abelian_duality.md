# Build Audit: Issue #603 Abelian Duality Pass

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`
- Issue: #603
- Files:
  - `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  - `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`
  - `calculation-checks/susy_2d_lg_glsm_checks.py`
  - `calculation-checks/README.md`
  - `planning/build_audits/2026-05-26_issue603_abelian_duality.md`

## Mathematical Content Added

- Added an intrinsic two-dimensional QFT section on abelian duality and
  circle T-duality, explicitly excluding string-theoretic mirror-duality
  arguments from the proof content.
- Stated the compact scalar first-order duality hypotheses: winding-sector
  sum, integral-period normalization, Gaussian contour, and
  field-independent determinant normalization.
- Proved the local radius inversion \(R \mapsto R^{-1}\) by eliminating
  either the dual periodic scalar or the first-order one-form.
- Added the momentum-winding spectrum ledger showing that
  \((n,w,R)\mapsto(w,n,R^{-1})\) preserves \(p_L^2+p_R^2\) and flips
  \(p_R\).
- Defined the local \(\mathcal N=(2,2)\) chiral/twisted-chiral Legendre
  transform datum and proved \(\widetilde K''=1/K''\).
- Recorded the GLSM charged-chiral dualization ledger and separated
  nonperturbative exponential twisted-superpotential terms into a
  vortex-instanton status boundary.

## Calculation Checks

- Extended `calculation-checks/susy_2d_lg_glsm_checks.py` with exact rational
  checks for:
  - circle-duality involutivity;
  - momentum-winding exchange and left/right momentum behavior;
  - zero-mode quadratic-form preservation;
  - Legendre-Hessian inversion, including affine shifts of the Legendre
    coordinate.

## Verification

- `python3 calculation-checks/susy_2d_lg_glsm_checks.py` passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram
  gamma-trace/anomaly-normalization check.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before staging.
- `tools/build_monograph.sh` passed after rebasing onto `origin/main` and
  produced `monograph/tex/main.pdf` with 1776 pages.
- A final log scan found no unresolved-reference LaTeX warnings in
  `monograph/tex/main.log`.
- A reference/prohibited-path guard found no staged, modified, or untracked
  `references/`, `.claude/`, or `claude_review.md` files in this pass.
