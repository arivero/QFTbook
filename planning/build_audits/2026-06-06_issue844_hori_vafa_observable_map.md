# Issue #844: GLSM/Hori--Vafa Observable Comparison Map

## Scope

This pass audits the Volume VII Chapter 09 Hori--Vafa/GLSM hotspot under the
canonical claim-architecture rule.  The reader-facing entrance to the mirror
comparison now states the physical question first: whether a protected GLSM
correlator computed with a regulated vortex measure agrees with the proposed
mirror residue in the same FI, determinant-line, and operator coordinates.

The TeX change keeps the existing mathematical labels stable while rephrasing
the local architecture as an observable comparison map:

- `D_loc` and `D_pert` are local/protected algebraic checks.
- `D_vort` is the direct regulated vortex-amplitude layer.
- `D_obs` is the protected observable comparison layer.
- `E_cont`, `E_op`, `E_top`, `E_bg`, and `E_sing` remain full-QFT proof debts.

The point is to prevent a Hori--Vafa expression, mirror residue, or stable-map
count from looking like an independent proof of the full QFT mirror statement
or of the direct vortex amplitude.

## Companion Evidence

`calculation-checks/susy_2d_lg_glsm_checks.py` was updated so the relevant
check is named as an observable-boundary check rather than a status ledger.  It
now explicitly rejects a mirror-residue-only comparison that bypasses the
direct `D_vort` data before the protected observable comparison.

The calculation-check README and Chapter 09 dossier were updated to use the
same comparison-map language.  Process and audit notes remain in planning
files, not in the monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` clean, producing `monograph/tex/main.pdf` at 3403 pages.
