# Issue #597 Instanton Physical-Amplitudes Chapter Pass

## Scope

- Added a compiled dedicated chapter:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Included it in
  `monograph/tex/volumes/volume_iv/volume_iv_current.tex` immediately after
  Ch20.
- Updated the frontmatter source map and added a chapter dossier.
- Added `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  plus README and evidence-contract entries.

## Physics Substance

- The pass starts the dedicated instanton chapter requested by #597 without
  adding more ADHM/moduli-space mathematics.
- It defines the physical-amplitude channel as the assembled finite-regulator
  object: retained window, collective density, nonzero-mode determinant,
  zero-mode Berezin coefficient, source/matching map, endpoint factor, and
  physical projection.
- It proves that channels with the same moduli measure can have different or
  zero amplitudes because the zero-mode source determinant and projection data
  differ.
- It expands the two-flavor `det(M+B)` coordinate to separate mass-saturated
  vacuum activity, mass-assisted source terms, and the four-source coefficient.
- It adds a finite-cell residual and determinant-stability model, making clear
  why endpoint, spectral/projection, cut, infrared, and scheme residuals are
  part of the physical amplitude rather than decoration.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture_checks`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --list | rg "instanton_physical_amplitude_architecture|Total|Python|Wolfram"`
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`
- `tools/build_monograph.sh` clean; final PDF page count 3418.
