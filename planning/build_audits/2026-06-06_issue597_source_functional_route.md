# Issue #597: Source-Functional Route For Instanton Amplitudes

## Scope

This pass addresses the instanton-depth concern that a physical amplitude is
not the moduli space or density alone.  It adds a front-loaded route block to
Volume II, Chapter 20D so the reader sees the finite-regulator source
functional before any density, hard slot, Wilsonian split, or observable map is
interpreted.

The TeX addition is reader-facing physics architecture, not process language.
It makes the ordered calculation explicit:

- collective instanton density and determinant normalization;
- zero-mode source functional;
- source-dependent normal-fluctuation average;
- collective-coordinate integration;
- source differentiation and physical projection.

## Companion Evidence

`calculation-checks/instanton_physical_amplitude_architecture_checks.py` now
contains `check_source_functional_route_order()`, an exact finite check that
rejects the three shortcut routes named in the new block:

- replacing source differentiation by mass saturation;
- replacing source-dependent fluctuation response by a determinant-only
  Gaussian mean;
- replacing the physical projection by a raw Euclidean source sum.

The chapter dossier and calculation-check README were updated to record this
as an argument-architecture improvement, not another local instanton cell.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "issue #|directive|claude_review|GitHub|planning/build_audits|monitor" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` clean, producing `monograph/tex/main.pdf` at
  3459 pages.
