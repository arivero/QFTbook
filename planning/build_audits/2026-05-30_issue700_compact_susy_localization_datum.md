# 2026-05-30 Issue #700 Compact SUSY Localization Datum Pass

## Target

- GitHub issue: #700.
- Local target:
  `monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex`.
- Problem: the chapter cited the earlier generic localization-data definition
  but did not aggregate its own compact-manifold QFT localization datum before
  using \(S^4\), \(S^3\), determinant, instanton, contour, and singular-stratum
  formulae.

## Edit

- Added
  `Definition~\ref{def:compact-supersymmetric-localization-datum}` at the
  chapter opening.
- The datum now records the compact rigid-supergravity background, directed
  regulator, regulated super field-variable space, integration cycle,
  Berezinian/BV density, odd symmetry and square, action, protected
  insertion, localizing functional, fixed locus, normal complex, residual
  finite-dimensional contour/residue/instanton prescription, and continuum
  comparison data.
- The definition explicitly treats fermionic variables as locally
  super-ringed-space coordinates, not as Borel-measure variables, and makes
  singular fixed strata part of the residual prescription rather than an
  automatic consequence of \(\int\mathcal D\Phi\).
- Rewrote the QFT localization datum section so its minimal tuple is a
  shorthand for the full compact datum.
- Updated the Volume VII Chapter 16 dossier.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- second `tools/build_monograph.sh` pass after label-table update:
  no lingering undefined reference for the new datum.
- `pdfinfo monograph/tex/main.pdf`: 2687 pages.
