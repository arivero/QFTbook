# Build Audit: Issue #592 SUSY Instanton And Nekrasov Expansion

Date: 2026-05-26

Branch/worktree:

- Branch: `codex/susy-gauge-dynamics-localization`
- Worktree used: `/Users/xiyin/QFT_susy_gauge_dynamics_localization`

## Scope

This pass addresses the supersymmetric field-theory part of GitHub issue
#592: ADS instanton generation in four-dimensional `N=1` SQCD, ADHM moduli
for four-dimensional `N=2` instanton calculus, and the Nekrasov
one-instanton expansion for pure `SU(2)`.

The dedicated Volume II instanton-measure expansion from Block N remains a
separate issue.  This pass cross-references the existing BPST normalization
and keeps the development inside the supersymmetric gauge-dynamics lane.
No files from the active SPDE issue #608 were edited.

## Source Review

- Handoff documents:
  `planning/agent_handoffs/00_common_agent_contract.md`,
  `planning/agent_handoffs/README.md`, and
  `planning/agent_handoffs/03_susy_gauge_dynamics_localization.md`.
- Strict harness: `planning/12_strict_writing_harness.md`.
- Review ledger: `claude_review.md`.
- Open GitHub issue reviewed: #592.  Earlier branch work also reviewed and
  commented on #588 and #605.
- Full monograph draft and relevant Volume VII chapters were reviewed before
  editing in the earlier branch setup; this pass re-read Chapters 06, 07, and
  the \(S^4\) localization Nekrasov definition in Chapter 16.
- Stringbook source:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, with
  attention to the D-instanton normalization discussion around lines
  9685-10168 and the supersymmetric gauge-theory appendices around the
  `N=2` and ADS material.
- Downloaded source payloads:
  `references/susy_gauge_dynamics_localization/issue592_instanton_nekr/eprints/`
  contains local arXiv e-print payloads for the instanton-calculus review,
  Nekrasov instanton counting, and the two original Seiberg-Witten papers.

## Files Changed

- `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`
- `monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`
- `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`
- `planning/chapter_dossiers/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.md`
- `calculation-checks/susy_instanton_nekr_checks.py`
- `calculation-checks/README.md`
- `references/susy_gauge_dynamics_localization/issue592_instanton_nekr/README.md`
- `references/susy_gauge_dynamics_localization/issue592_instanton_nekr/eprints/*`

## New Results And Boundaries

- Added the explicit SQCD one-instanton hypothesis ledger: holomorphic
  regulator, maximal-rank Higgs patch, collective-coordinate separation,
  BPST topological normalization, and endpoint treatment by the holomorphic
  scale coordinate.
- Proved the `N_f=N_c-1` ADS one-instanton zero-mode count and derived
  `W = kappa_Nc Lambda_h^(2N_c+1)/det M` from the instanton scale factor,
  flavor invariance, engineering dimension, and \(R\)-charge.
- Added framed `U(N)` ADHM data, both moment-map equations, the stability
  parameter, and the framing at infinity.
- Proved the ADHM dimension count: complex dimension `2kN`, real dimension
  `4kN`, and centered real dimension `4kN-4`.
- Stated the `U(N)` to `SU(N)` specialization and the point-instanton caveat
  for the compactification used by Nekrasov localization.
- Added the equivariant fixed-point theorem boundary for the framed ADHM
  compactification, with fixed points labeled by `N`-tuples of Young
  diagrams.
- Defined the pure vector Nekrasov instanton series and displayed the
  one-instanton `U(N)` fixed-point formula.
- Derived the pure `SU(2)` specialization and the first Nekrasov
  prepotential coefficient `q/(2a^2)`, with `q=Lambda^4`.
- Recorded the limited resurgence/transseries ledger: instanton number,
  action, and theta phase grade the ADHM integral, the \(\Omega\)-background
  partition function, and candidate weak-coupling transseries sectors; a
  theorem-level large-order statement remains outside this pass.

## Verification

- `python3 calculation-checks/susy_instanton_nekr_checks.py`: passed.
- `python3 calculation-checks/sw_su2_periods.py`: passed.
- `python3 calculation-checks/susy_n1_conifold_checks.py`: passed.
- `python3 calculation-checks/susy_localization_matrix_checks.py`: passed.
- `python3 calculation-checks/bpst_instanton_normalization_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed, including the new
  instanton/ADHM/Nekrasov script and the Wolfram gamma-trace check.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed after the internal rerun needed for new
  cross-references; final build/log scan clean.
- `pdfinfo monograph/tex/main.pdf`: 1534 pages.
