# 2026-06-06 Issue #597 Hard-Window Tail Subtraction Audit

## Scope

- Targeted #597 inside the dedicated instanton physical-amplitude chapter.
- Added endpoint control for the hard four-source instanton benchmark.
- This is amplitude physics, not an ADHM or moduli-space expansion.

## Substance Added

- Added `ca:instanton-hard-window-tail-subtraction` after the SU(3), `N_f=2`
  hard-source slow-tail proposition.
- The new block expands the differentiated BPST zero-mode slot one order
  beyond the leading hard tail:
  \(F_\ell(c_\ell s)=6c_\ell^{-3}s^{-3}+45c_\ell^{-5}s^{-5}+O(s^{-7})\).
- It derives the hard-window integrand tail coefficients
  \(A_0\) and \(A_1\), and rewrites the hard size integral as a finite core
  plus analytic endpoint tails:
  \(3A_0R^{-1/3}+(3/7)A_1R^{-7/3}+E_{\rm tail}(R)\).
- The text keeps the result downstream of the assembled channel and physical
  projection; the tail-subtracted source coefficient is not treated as a
  standalone hadronic amplitude.

## Quality Audit

- The pass addresses the hard part of instanton physics: controlling the
  fluctuation/source endpoint integral, not only describing the moduli space.
- The new calculation sharpens an existing physical benchmark by exposing the
  endpoint term that must be retained for a controlled amplitude.
- The companion check uses exact rational tail algebra and negative controls
  rather than a heavy numerical quadrature, so the public check remains fast
  while still testing the coefficient logic.
- No directives, GitHub issue text, monitoring language, or planning language
  were inserted into the monograph TeX.

## Verification

- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- Process-language scan of the touched TeX and calculation-check surfaces.
- `tools/build_monograph.sh`
- `tools/run_calculation_checks.sh --python-only`

The full monograph build completed with `monograph/tex/main.pdf` at 3446 pages.
The full Python calculation-check run passed; Wolfram checks were not selected.
