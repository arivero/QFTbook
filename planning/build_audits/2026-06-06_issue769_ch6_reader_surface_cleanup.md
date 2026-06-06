# 2026-06-06 Issue #769 Ch6 Reader-Surface Cleanup

## Scope

- Re-audited the reader-facing surface of Volume II Chapter 6's
  generalized-unitarity and loop-reduction section.
- Replaced visible process vocabulary with physics-facing workflow language:
  named-tool roles, reconstruction-package entries, color--kinematics
  comparison data, master-discontinuity closure comparison, and two-loop
  infrared-pole consistency tests.
- Kept equation labels and cross-reference labels stable.
- Updated the Chapter 6 dossier with the cleanup and its reason.

## Quality Intent

This pass addresses coherence drift in a heavily developed amplitude section.
The chapter already contains substantial reconstruction, rational-term, IBP,
master-transport, discontinuity, and observable-assembly machinery.  The
reader-facing prose should therefore emphasize the physical computation chain
from cuts to representatives, rational/regulator data, reduction, boundary
values, subtraction, and measured observables, not planning vocabulary.

## Verification

All checks passed before landing:

- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh` (clean log scan; `monograph/tex/main.pdf`, 3404 pages)
