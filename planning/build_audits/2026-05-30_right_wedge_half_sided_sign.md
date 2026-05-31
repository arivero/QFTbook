# 2026-05-30 Right-Wedge Half-Sided Modular Sign Pass

## Scope

- GitHub issue: #695.
- Local target:
  `monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`.
- Goal: tighten the Borchers--Wiesbrock theorem boundary by verifying the
  concrete right-wedge light-ray inclusion and the half-sided sign in the
  monograph's Bisognano--Wichmann convention.

## Edit

- Added the left-half-sided variant to the Borchers--Wiesbrock quoted theorem
  statement, making the sign reversal explicit.
- Replaced the terse right-wedge paragraph by
  `Example~\ref{ex:right-wedge-half-sided-sign}`.
- The example proves \(W_R+a e_+\subset W_R\), records the nesting
  \(b\ge a\Rightarrow W_R+b e_+\subset W_R+a e_+\), and uses
  \(\Delta^{it}_{W_R}=U(\Lambda_R(-2\pi t))\) to derive
  \[
    \sigma_t^{W_R}\mathcal R(W_R+a e_+)
    =
    \mathcal R(W_R+e^{-2\pi t}a e_+).
  \]
- The text now states explicitly that the inward future-lightlike translated
  wedge is left half-sided under this convention, and that changing modular
  sign or light-ray orientation changes the left/right wording.
- Extended `calculation-checks/unruh_boost_geometry_checks.py` with the same
  lightlike nesting and scaling convention check.
- Updated the Volume IV Chapter 4 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/unruh_boost_geometry_checks.py`
- `python3 -m py_compile calculation-checks/unruh_boost_geometry_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- second `tools/build_monograph.sh` pass after label-table update:
  no lingering undefined reference for the new wedge equations.
- `pdfinfo monograph/tex/main.pdf`: 2688 pages.
