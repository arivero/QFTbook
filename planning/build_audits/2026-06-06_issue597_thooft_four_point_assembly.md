# 2026-06-06 Issue 597 't Hooft Four-Point Assembly Audit

## Scope

- Targeted Volume II, Chapter 20D, the instantons-as-physical-amplitudes
  chapter.
- Added an amputated four-source assembly block inside the hard benchmark.
- The edit packages the density, Haar tensor, chiral source determinants,
  individual zero-mode slots, nonzero-mode source quotient, amputation,
  physical projection, endpoint tail, and sector isolation as one
  common-regulator amplitude claim.

## Quality Audit

- This is a physics-amplitude consolidation, not another ADHM or moduli-space
  expansion.
- It responds to the risk that the hard benchmark's local ingredients could be
  read as adjacent facts rather than the pieces of one 't Hooft-style
  amputated Green-function calculation.
- The TeX names only the physical calculation and residuals; issue tracking and
  review-language bookkeeping remain in planning files.
- The companion check adds negative controls for density-only assembly,
  rank-lost source determinants, symmetric Haar sources, omitted nonzero-mode
  source quotients, unamputated source overlaps, and missing projection
  residuals.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- Zero-match scan for `directive|GitHub|issue #|claude|monitor|review` in
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
