# Build Audit: Issue #594 KW Exact Marginality Pass

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`
- Issue: #594, partial supersymmetric `4D` `N=1` conformal-manifold component
- Files:
  - `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`
  - `calculation-checks/susy_n1_conifold_checks.py`
  - `calculation-checks/README.md`
  - `planning/build_audits/2026-05-26_issue594_kw_exact_marginality.md`

## Mathematical Content Added

- Replaced the previous quoted KW conformal-manifold statement with a
  conditional finite-dimensional exact-marginality chart.
- Stated the local `N=1` source-chart hypotheses: holomorphic marginal
  sources, a beta map whose zero locus is the conformal locus, fixed or
  quotient redundant field-coordinate directions, current-moment-map
  obstructions, and constant-rank behavior.
- Stated the KW exact-marginality assumptions explicitly: local sources
  `(tau_1,tau_2,h)`, preserved `SU(2)_A x SU(2)_B x U(1)_B`, continuum SCFT
  existence, completeness of the NSVZ/superpotential beta ledger, fixed
  contact-term/source-normalization data, and nonzero differential of the
  common defect `E=1+gamma_A+gamma_B`.
- Proved, under those hypotheses, that the KW conformal locus is locally a
  complex two-dimensional submanifold: the three beta functions factor as
  `(N E, N E, E)`, so the zero set is one equation in the three-source chart.

## Calculation Checks

- Extended `calculation-checks/susy_n1_conifold_checks.py` with exact finite
  checks for:
  - the rank-one common beta-map coefficient vector `(N,N,1)`;
  - the local dimension count `3-1=2`;
  - two independent tangent vectors annihilating a normalized common defect.

## Verification

- `python3 calculation-checks/susy_n1_conifold_checks.py` passed, including the
  KW local exact-marginality rank and tangent-kernel checks.
- `tools/run_calculation_checks.sh` passed, including the Wolfram gamma-trace
  backend.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before staging.
- The first `tools/build_monograph.sh` run found an overfull paragraph in the
  new KW exact-marginality discussion; the paragraph was reflowed and the
  build was rerun.
- `tools/build_monograph.sh` then passed with a clean log scan and produced
  `monograph/tex/main.pdf` with `1784` pages before rebasing.
- After rebasing the branch on the latest `origin/main`, the targeted conifold
  check, full calculation-check harness, text audit, chapter-dossier audit,
  `git diff --check`, and `tools/build_monograph.sh` were rerun.  The rebuilt
  PDF passed the log scan and contains `1789` pages.
- No `.claude/`, `claude_review.md`, or `references/` files were edited or
  staged for this pass.
