# Issue #527 many-body Cook-budget pass

Date: 2026-06-06

## Scope

- Advanced the charged Haag--Ruelle / Wilson-line LSZ development in Volume IV, Chapter 05.
- Added a non-theorem bridge from pair-tail extraction to the actual modified-Cook estimate: once the charged pair kernels have been identified, the same leading kernels must be subtracted in one comparison phase, leaving only core residuals, pair \(L^1\) remainders, and finite same-flux schedule errors.
- Added the negative test in the monograph surface: any nonzero limiting mismatch in a pair coefficient leaves a dyadic \(1/t\) obstruction, while a decaying same-flux coefficient error is allowed only when \(\delta\kappa(t)/t\in L^1\).
- Extended `charged_flux_dressing_checks.py` with an exact finite many-body Cook-budget model, including an omitted-pair negative control and a summable same-flux coefficient-error control.
- Updated the calculation-check README and the chapter dossier.

## Re-audit

- This is physics-facing argument architecture for the open charged-scattering theorem, not a wrapper theorem and not a claim that the nonperturbative Wilson-line large-time estimate has been proved.
- The added text keeps the physical charged-scattering target visible: angular Gauss-law flux, pairwise long-range exchange, the Dollard/Faddeev--Kulish comparison phase, dressed-correlator residue normalization, and detector flux sectors must all use the same extracted coefficient.
- No directive, issue-tracking, GitHub, monitoring, or planning-process language was added to the monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
- `python3 calculation-checks/charged_flux_dressing_checks.py`
- `tools/run_calculation_checks.sh --python-only --only charged_flux_dressing`
- `tools/run_calculation_checks.sh --python-only`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/build_monograph.sh`

Full Python calculation checks passed; Wolfram Language checks were not selected. The full monograph build completed cleanly at 3453 pages.
