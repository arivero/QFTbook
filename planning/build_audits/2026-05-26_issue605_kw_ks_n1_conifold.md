# Build Audit: Issue #605 KW/KS N=1 Conifold Gauge Dynamics

Date: 2026-05-26

Branch/worktree:

- Branch: `codex/susy-gauge-dynamics-localization`
- Worktree used: `/Users/xiyin/QFT_susy_gauge_dynamics_localization`

## Scope

This pass addresses the supersymmetric field-theory content requested in
GitHub issue #605, with emphasis on the Klebanov-Witten conifold SCFT and the
Klebanov-Strassler cascade as four-dimensional `N=1` gauge dynamics.

No files from the active SPDE issue #608 were edited.

## Source Review

- Handoff documents:
  `planning/agent_handoffs/00_common_agent_contract.md`,
  `planning/agent_handoffs/README.md`, and
  `planning/agent_handoffs/03_susy_gauge_dynamics_localization.md`.
- Strict harness: `planning/12_strict_writing_harness.md`.
- Review ledger: `claude_review.md`.
- Open GitHub issues reviewed: #588, #603, #605, #590, and #592; this edit
  materially addresses #605.
- Full monograph draft reviewed before editing through the compiled PDF,
  main TeX structure, frontmatter guide, and Volume VII table of contents.
- Stringbook source:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  especially lines 18380-18670 for KW/KS and lines 23170-23215 for the
  Wilsonian/NSVZ convention.  The monograph now states the conversion between
  its `gamma=d log Z/d log mu` convention and the stringbook
  `mathcal C=(1/2)d log Z/d log mu` convention.

## Files Changed

- `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`
- `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`
- `calculation-checks/susy_n1_conifold_checks.py`
- `calculation-checks/README.md`
- `references/susy_gauge_dynamics_localization/issue605_kw_ks/README.md`
- `references/susy_gauge_dynamics_localization/issue605_kw_ks/eprints/*`

## New Results And Boundaries

- Added self-contained superconformal SQCD bookkeeping: the relation
  `Delta=3R/2`, the anomalous-dimension convention, NSVZ cancellation at the
  candidate fixed point, and the meson unitarity-bound test.
- Added explicit hypothesis boundaries for the use of SCFT shortening, the
  KW Lagrangian/branch analysis, and the KS cascade duality step.
- Added KW field content, global symmetries, baryon-charge normalization,
  and quartic superpotential.
- Derived the KW F-term equations explicitly from the expanded
  superpotential.
- Proved the KW anomaly-free R-charge assignment and checked the
  superpotential R-charge.
- Proved the KW NSVZ numerator cancellation with the monograph's gamma
  convention and the stringbook half-gamma conversion made explicit.
- Performed the baryonic-mixing `a`-maximization calculation and derived the
  exact finite-N `a` and `c` central charges.
- Proved the one-brane conifold quotient and recorded the general commuting
  mesonic branch with a clear branch limitation.
- Added protected meson and baryon dimensions.
- Quoted the KW local conformal-manifold statement as a continuum SCFT input
  after deriving the anomaly and marginality arithmetic.
- Added the KS `SU(N+M) x SU(N)` NSVZ numerator signs, Seiberg-dual rank
  step with local magnetic meson integration, cascade Euclidean division
  count, unequal-rank `U(1)_R` anomaly remnant, endpoint symmetry breaking,
  and an explicit quoted-theorem boundary for the Seiberg-duality input.
- Downloaded arXiv TeX source payloads for KW, KT, KS, Seiberg duality,
  Leigh-Strassler marginality, and a-maximization.  The payloads were
  unpacked locally for inspection; the committed reference directory keeps
  the original source payloads because `references/**/*.tex` is ignored by
  the repository.

## Verification

- `python3 calculation-checks/susy_n1_conifold_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed, including the new conifold
  SCFT/cascade checks and the Wolfram gamma-trace check.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed after two internal LaTeX runs for new
  cross-references; final build/log scan clean.
- `pdfinfo monograph/tex/main.pdf`: 1530 pages.
