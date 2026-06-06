# 2026-06-06 Issue #630 Finite Shear Spectral-Window Audit

## Scope

- Added `ca:qcd-finite-shear-spectral-window` to
  `monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`.
- Extended `calculation-checks/qcd_phase_checks.py` with
  `check_finite_shear_spectral_window_bookkeeping()`.
- Updated the calculation-check README and the Volume X Ch12 dossier.

## Quality Intent

This pass deepens the QCD transport bridge by separating the Kubo slope from a
finite-frequency spectral extraction.  The manuscript now states the
hydrodynamic transverse-momentum peak, the scale separation
`gamma_k << Omega << tau_micro^{-1}`, the peak-area residue bound, and the
width/residue error propagation needed before a QCD shear-viscosity estimate is
claimed.  The point is to make finite-window transport comparisons accountable
to retarded spectral data rather than to hydrodynamic vocabulary or plotted
peaks alone.

## Verification

- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `python3 calculation-checks/qcd_phase_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_phase_checks`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --fail`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/build_monograph.sh`

All commands passed.  The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` at 3402 pages.
