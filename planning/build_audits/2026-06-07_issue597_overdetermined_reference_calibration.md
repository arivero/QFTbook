# Issue #597 Overdetermined Reference-Calibration Audit

## Scope

- Added an instanton physical-amplitude block for overdetermined
  reference-channel determinant calibration.
- The new block requires two same-frame physical reference amplitudes to
  extract the same finite determinant constant within explicit residual and
  noncancellation-margin bounds.
- It makes omitted source-fluctuation quotients and physical-projection factors
  appear as channel-dependent drifts, not as universal determinant data.

## Quality Audit

- This is an amplitude-facing instanton increment, not a moduli-space
  refinement.  Its purpose is to keep determinant calibration tied to the
  physical source/projection coordinate.
- The result strengthens the chapter architecture by making reference
  calibration falsifiable across two physical channels rather than allowing a
  single channel to absorb hidden source or projection factors.
- It still does not compute a continuum Pauli--Villars, minimal-subtraction, or
  named regulator finite determinant constant.  That remains a separate
  regulated fluctuation-measure calculation with zero-mode, normal-mode,
  counterterm, and projection data fixed.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `rg -n "claude|review|directive|monitor|issue #|GitHub|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
  returned no matches.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
