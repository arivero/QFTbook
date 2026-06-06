# Issue #629 Determinant-Line Transport Build Audit

Date: 2026-06-06

## Scope

- Addressed the singular-instanton regulator gap in Volume VII, Chapter 16 by
  adding a pole-local determinant-line transport layer after the Uhlenbeck
  collar-flux selection test.
- The pass is intentionally QFT-facing: the Gieseker fixed-point Euler
  denominator is treated as the target of a regulated normal Gaussian, with
  orientation phase, ghost/slice normalization, zero-mode split, pole-coordinate
  reflection, and regulator-limit residuals explicitly separated.
- Updated `susy_instanton_nekr_checks.py` with exact finite failures for stale
  orientation, omitted slice factors, leaked zero modes, and untransported
  south-pole coordinates.

## Verification

- `python3 -m py_compile calculation-checks/susy_instanton_nekr_checks.py`
- `python3 calculation-checks/susy_instanton_nekr_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_instanton_nekr`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex --fail --limit 20`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

## Result

- All targeted and full Python calculation checks passed.
- Monograph build and log scan passed cleanly:
  `/Users/xiyin/QFT/monograph/tex/main.pdf`.
- Built PDF length: 3389 pages.
- The evidence-contract audit emitted its standing non-blocking risk report but
  no contract failure.
