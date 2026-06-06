# 2026-06-06 Issue #527 Endpoint/Cusp Residue RG Audit

## Scope

- Targeted #527 inside Volume IV Chapter 5, the charged Haag--Ruelle and
  Wilson-line LSZ chapter.
- Addressed the dressed external-residue normalization problem: \(Z_{\rm
  dressed}\) includes the nonlocal charged coordinate, not only the local
  matter field.
- This pass is external-state physics and LSZ bookkeeping.  It does not claim
  the full nonperturbative charged Haag--Ruelle theorem.

## Substance Added

- Added `Endpoint Renormalization and Dressed External Residues` after the
  dressed-residue coordinate algebra.
- The new subsection states the finite renormalization law for dressed
  coordinates:
  \(z' = Rz\), \(Z'=RZR^\dagger\), and \(L'=LR^{-1}\).
- It extends the law to multi-leg dressed-correlator residue tensors and gives
  the differential anomalous-dimension equations for \(z\), \(L\), and the
  residue tensor.
- It separates finite same-flux coordinate changes from changes of
  asymptotic ray, Coulomb tail, or angular flux sector.

## Quality Audit

- The pass deepens the physical LSZ interface for charged gauge sectors rather
  than adding a formal charged-sector slogan.
- It targets an explicit substance item from #527: Wilson-line endpoint/cusp
  renormalization changes the dressed external residue.
- The monograph text keeps the load-bearing theorem debt honest: the
  nonperturbative charged scattering theorem remains open.
- No process directives, monitoring language, or planning text were inserted
  into monograph TeX.

## Verification

- `git diff --check`
- `python3 calculation-checks/charged_flux_dressing_checks.py`
- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
- `tools/run_calculation_checks.sh --python-only --only charged_flux_dressing`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --window 120 --stride 60 --fail --limit 20`
- Process-language scan of the touched TeX and calculation-check surfaces.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/build_monograph.sh`
- `tools/run_calculation_checks.sh --python-only`

The full monograph build completed with `monograph/tex/main.pdf` at 3447 pages.
The full Python calculation-check run passed; Wolfram checks were not selected.
