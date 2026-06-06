# Issue #597 instanton chapter-flow pass

Date: 2026-06-06

## Scope

- Performed a chapter-flow and coherence pass on Volume II, Chapter 20D, with the explicit aim of keeping the instanton material physics-first: physical amplitudes, determinants, zero-mode saturation, source response, and observable maps before any temptation to make the moduli-space geometry the center of gravity.
- Added a front-loaded order-of-calculation paragraph that tells the reader how the chapter moves from the one-loop density to collective-coordinate separation, normal fluctuations, zero-mode saturation, LSZ/source insertion, finite-volume cluster corrections, and observable projections.
- Replaced remaining reader-facing "observable handoff" language in the monograph surface by observable-map language. Stable internal labels were left unchanged to avoid unnecessary cross-reference churn.
- Updated the paired chapter dossier to record the new flow paragraph and the terminology cleanup.

## Re-audit

- This was deliberately not another finite-identity annexation. The limiting return in this chapter was argument architecture: making the physical-amplitude order visible enough that the existing hard cells read as one calculation rather than as adjacent local mechanisms.
- The edit keeps directives, issue-tracking language, and monitoring/process language out of the monograph TeX.
- The new wording was checked against the surrounding instanton sections so that it points toward the physically hard objects: the measure, fluctuation determinant, zero-mode source saturation, and observable projection.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`

Full Python calculation checks passed; Wolfram Language checks were not selected. The full monograph build completed cleanly at 3452 pages.
