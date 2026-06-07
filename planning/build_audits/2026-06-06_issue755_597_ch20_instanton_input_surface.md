# 2026-06-06 Issue #755/#597 Ch20 Instanton Input Surface

## Scope

- Focused reader-surface and coherence pass on the opening one-instanton
  amplitude assembly block in Volume II Chapter 20.
- Retitled the visible definition heading from "one-instanton amplitude datum"
  to "one-instanton amplitude inputs" while preserving
  `def:one-instanton-amplitude-datum` and
  `eq:one-instanton-amplitude-datum`.
- Replaced repeated datum/coordinate/slot language with ordered input,
  source-coefficient, density-part, and residual-group language.
- No formula, label, factor, residual group, or physics claim was changed.

## Quality Intent

This pass addresses coherence drift after the recent instanton amplitude
developments.  The monograph should not read as though BPST/ADHM moduli-space
geometry is the main physical result.  The revised surface keeps that geometry
as the classical/collective-density input and foregrounds the harder QFT
chain: nonzero-mode determinant, fermion zero-mode saturation, source or state
matching, size-window control, and the physical observable projection.

## Verification Passed

- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- Process-language scan against the touched TeX: no matches.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_negative_scope_prose.py`
- `git diff --check`.
- `tools/build_monograph.sh`, clean at 3478 pages.
