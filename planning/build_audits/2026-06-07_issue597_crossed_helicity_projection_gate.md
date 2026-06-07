# 2026-06-07 Issue 597 Crossed Helicity Projection Audit

## Scope

- Targeted Volume II, Chapter 20D, the instantons-as-physical-amplitudes
  chapter.
- Added `ca:instanton-crossed-helicity-projection-gate` after the crossed
  chiral hard-channel block.
- The pass projects the scalar \(RR\to LL\) crossed source coefficient onto
  fixed external Weyl spinors before treating it as a physical helicity
  amplitude.

## Quality Audit

- This is a physical external-state pass, not another moduli-space or ADHM
  expansion.
- The scalar instanton source coefficient is kept separate from the
  fixed-helicity amplitude and from spin-summed or inclusive rates.
- The block records the antisymmetric left/right spinor contractions,
  slot-order signs, collinear-bin zeroes, phase-space spin sums, and an
  explicit helicity residual.
- The TeX contains only the physics calculation and its residual obligations.
  Issue/review/directive language remains in planning files.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
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
