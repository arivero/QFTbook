# 2026-06-06 Issue #755/#597 Ch20 Reader-Surface Cleanup

## Scope

- Re-audited the reader-facing surface of Volume II Chapter 20 after the recent
  instanton amplitude passes.
- Replaced visible process vocabulary in the anomaly/instanton entrance with
  physics-facing scope and assembly language.
- Kept labels stable to avoid cross-reference churn.
- Updated the Chapter 20 dossier with the cleanup and its reason.

## Quality Intent

The pass addresses coherence drift rather than adding another instanton cell.
The chapter already contains substantial fluctuation, zero-mode, determinant,
source, tail, and physical-projection machinery.  The reader-facing surface now
emphasizes the actual QFT chain: named anomaly/instanton inputs have declared
roles, and the one-instanton section is organized as an amplitude assembly
from collective coordinates through determinants, source saturation, size
control, and observable projection.  Process terms that belonged in planning
were removed from the TeX prose.

## Verification

- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh` (clean; `main.pdf`, 3404 pages)

All checks passed before landing.
