# Build Audit: Issue #605 SQCD NSVZ Coordinate Audit

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issue: #605, with overlap to the #588 supersymmetric gauge-dynamics
  foundations.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Companion files:
  - `calculation-checks/susy_n1_sqcd_duality_checks.py`.
  - `calculation-checks/README.md`.
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.

## Source Leads

- Internal monograph source: Chapter 05,
  `prop:nsvz-coordinate-relation-derived`, which derives the
  holomorphic-canonical gauge-coordinate relation from the Konishi
  rescaling anomaly and vector-multiplet BV Jacobian.
- Stringbook convention comparison:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex` around
  the supersymmetric Wilsonian/NSVZ convention discussion.
- No string compactification, D-brane, holographic, or superstring argument
  was imported.

## Substantive Changes

- Expanded the Chapter 06 SQCD NSVZ section from a quoted specialization into
  a self-contained coordinate audit.
- Added explicit assumptions for specializing the Chapter 05
  holomorphic-canonical relation to SQCD.
- Derived
  `X_h=X_c+N_c log g^2-N_f log Z_Q+kappa` from the half-trace convention and
  the \(N_f\) fundamental plus \(N_f\) antifundamental chiral multiplets.
- Differentiated the coordinate relation to obtain the specialized NSVZ beta
  function and identified the denominator pole as a coordinate-chart feature,
  not an invariant physical event.
- Extended the exact SQCD calculation check to verify the matter-index
  factors and the differentiated-coordinate algebra.

## Verification

- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py` passed.
- `tools/run_calculation_checks.sh` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed after shortening the section heading to
  remove an overfull line; the final PDF has 1551 pages.

## Status

This pass advances #605 and #588 but does not close either issue.  The
broader nonperturbative continuum construction of the infrared SQCD theories
and Seiberg duality remains outside the proved content of this pass.
