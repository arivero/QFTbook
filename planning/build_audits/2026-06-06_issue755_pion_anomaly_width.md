## Scope

Addressed a focused anomaly-to-observable handoff in Volume II Chapters 20 and
21.  Chapter 20 now points from the local axial contact term to the Chapter 21
WZW/pion-pole calculation rather than leaving the anomalous pion coupling as a
bare slogan.  Chapter 21 now derives the leading neutral-pion two-photon width
from the matched \(g_{\pi\gamma\gamma}\pi^0F\widetilde F/4\) vertex, the
tensor amplitude, the polarization sum, and the identical-photon two-body phase
space.

## Quality Intent

The change turns a chapter-ending consequence of the anomaly into a physical
prediction with normalization and phase-space conventions exposed.  It avoids
duplicating the local anomaly derivation and keeps the observable calculation
where the pion effective theory is developed.

## Verification

All checks passed before landing:

- `python3 -m py_compile calculation-checks/anomaly_matching_wzw_checks.py`
- `python3 calculation-checks/anomaly_matching_wzw_checks.py`
- `tools/run_calculation_checks.sh --python-only --only anomaly_matching_wzw`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail --limit 40`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex --fail --limit 40`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py` (clean, with standing non-blocking risk report)
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` (clean log scan; `monograph/tex/main.pdf`, 3404 pages)
