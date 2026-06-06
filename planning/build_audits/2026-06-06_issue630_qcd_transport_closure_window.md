# Issue #630 QCD transport-closure window pass

Date: 2026-06-06

## Scope

- Advanced the QCD phase-structure chapter's hydrodynamics-from-QCD layer.
- Added `ca:qcd-transport-closure-window` after the finite shear, bulk/sound,
  and charge-diffusion spectral windows.
- The new gate assembles the same-state first-order QCD transport datum
  \(\mathfrak T_{\rm QCD}^{(1)}=(w,c_s^2,\eta,\zeta,\chi^\perp,\Sigma^{\rm inc})\)
  and its combined residual
  \(R_{\rm hydro}=R_{\rm shear}+R_{\rm bulk}+R_{\rm charge}+R_{\rm therm}
  +R_{\rm frame}+R_{\rm cross}+R_{\rm cont}\).
- Extended `qcd_phase_checks.py` with an exact rational closure check:
  shear, sound, and charge poles are reconstructed from one transport datum,
  while incomplete data, mixed phase/frame assembly, missing shear subtraction,
  missing susceptibility residue, and raw-current Drude contamination are
  rejected.
- Updated the calculation-check README and the chapter dossier.

## Re-audit

- This is argument architecture rather than another isolated transport cell:
  it forces the existing shear, bulk/sound, and diffusion windows to assemble
  into a physical QCD hydrodynamic response prediction.
- The added TeX remains conditional on the microscopic QCD response-window
  estimate; it does not claim to prove that continuum QCD always has isolated
  hydrodynamic poles.
- The physics target is the amplitude-level response of QCD correlators in a
  common low-energy window, with pressure data, Kubo data, frame projection,
  current projection, and cross-channel consistency all kept visible.
- No directive, issue-tracking, GitHub, monitoring, or planning-process
  language was added to the monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `python3 calculation-checks/qcd_phase_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_phase`
- `tools/run_calculation_checks.sh --python-only`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_python_runner_selection.sh`
- `git diff --check`
- `tools/build_monograph.sh`

Full Python calculation checks passed; Wolfram Language checks were not
selected.  The full monograph build completed cleanly at 3454 pages.
