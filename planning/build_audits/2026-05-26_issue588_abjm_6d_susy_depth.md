# Build Audit: Issue #588 ABJM And Six-Dimensional SUSY Depth Pass

Date: 2026-05-26

Branch/worktree:

- Branch: `codex/susy-gauge-dynamics-localization`
- Worktree used: `/Users/xiyin/QFT_susy_gauge_dynamics_localization`

## Scope

This pass addresses supersymmetric field-theory material in Volume VII for
GitHub issue #588, with emphasis on:

- `3D` `N=2` Chern-Simons-matter as a field-theory datum.
- ABJM as `U(N)_k x U(N)_{-k}` Chern-Simons-matter theory, including matter,
  superpotential, parity, moduli, monopole theorem boundary, and `S^3`
  localization specialization.
- Six-dimensional `(2,0)` theories as non-Lagrangian SCFTs specified by
  representation data, tensor-branch EFT, anomaly polynomial, BPS strings,
  and compactification tests.

No files from the active SPDE issue #608 were edited.

## Source Review

- Handoff documents:
  `planning/agent_handoffs/00_common_agent_contract.md`,
  `planning/agent_handoffs/README.md`,
  and `planning/agent_handoffs/03_susy_gauge_dynamics_localization.md`.
- Strict harness: `planning/12_strict_writing_harness.md`.
- Review ledger: `claude_review.md`.
- Open GitHub issues reviewed: #588, #603, #605, #590, and #592, with this
  edit materially addressing only #588.
- Full monograph draft reviewed through the compiled PDF metadata, main TeX
  volume structure, frontmatter dependency guide, and Volume VII table of
  contents before editing.
- Stringbook source:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  especially lines 14160-14510 for ABJM and lines 14506 onward for
  six-dimensional `(2,0)` material.  Higher-dimensional supersymmetric gauge
  source ranges around lines 23045-23320 were also reviewed for conventions.

## Files Changed

- `monograph/tex/volumes/volume_vii/chapter10_three_dimensional_chern_simons_matter.tex`
- `monograph/tex/volumes/volume_vii/chapter11_six_dimensional_superconformal_theories.tex`
- `planning/chapter_dossiers/volume_vii/chapter10_three_dimensional_chern_simons_matter.md`
- `planning/chapter_dossiers/volume_vii/chapter11_six_dimensional_superconformal_theories.md`
- `calculation-checks/susy_abjm_6d_checks.py`
- `calculation-checks/README.md`

## New Results And Boundaries

- Added a proof of the Chern-Simons shifted auxiliary `D` equation in
  `3D` `N=2` matter.
- Added ABJM gauge-theory data, parity proof for levels `(k,-k)`, one-brane
  quotient proof `C^4/Z_k`, quoted theorem status for the general commuting
  branch and `N=8` enhancement, and the ABJM `S^3` matrix model.
- Added the six-dimensional Yang-Mills dimension argument, `(2,0)`
  tensor-branch quotient, type `A_{N-1}` example, quoted theorem status for
  the `(2,0)` anomaly polynomial, BPS string charge/tension data, and the
  trace-delta proof of `g_5^2=4 pi^2 R`.
- Kept non-Lagrangian and monopole-sector claims at quoted theorem or open
  problem boundaries rather than presenting them as derived from local
  polynomial Lagrangians.

## Verification

- `python3 calculation-checks/susy_abjm_6d_checks.py`: passed.
- `python3 calculation-checks/susy_localization_matrix_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed, including the new ABJM/6D check.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed after shortening one ABJM proposition
  heading/opening that produced an overfull line in the first build attempt.
  Final build/log scan clean.
- `pdfinfo monograph/tex/main.pdf`: 1521 pages.
