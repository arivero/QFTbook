# 2026-06-07 Issue 597 Same-Coordinate Amplitude-to-Rate Audit

## Scope

- Targeted Volume II, Chapter 20D, the instantons-as-physical-amplitudes
  chapter.
- Added `ca:instanton-same-coordinate-amplitude-rate-gate` after the
  mass-assisted interference block.
- The pass consolidates the 't Hooft hard channel into a typed observable
  chain: all-outgoing Euclidean source vector, crossing/amputation map,
  physical projection, positive measurement matrix, and same-channel
  interference reference.

## Quality Audit

- This is an argument-architecture repair, not a new moduli-space calculation.
  It prevents a Euclidean source coefficient, an unamputated source vector, a
  theta-linear interference term, and a positive cut/rate from being treated as
  the same physical object.
- The companion finite-vector check rejects squaring the all-outgoing source
  vector before crossing/projection, using unamputated source overlaps in the
  quadratic cut, forming wrong-channel formal interference, reading a linear
  theta-charged source sum as a positive rate, and dropping the reference-vector
  residual in the interference budget.
- The TeX contains only the physics calculation and residual obligations.
  Issue/review/directive language remains in planning files.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "directive|claude_review|GitHub|issue #|monitor|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex` (zero matches)
- `bash tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
