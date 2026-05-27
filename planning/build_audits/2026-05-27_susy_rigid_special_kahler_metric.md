# Build Audit: SUSY Rigid Special-Kahler Metric

Date: 2026-05-27

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass incorporates and expands the stringbook appendix formula for the
two-derivative Abelian `4D` `N=2` vector-multiplet Wilsonian action inside
Volume VII Chapter 07, as an intrinsic QFT derivation rather than as a cited
Seiberg-Witten convention.

## Substantive Edits

- Added the local `N=1` superspace representation of Abelian `N=2`
  Wilsonian vector multiplets by vector superfields `V^I` and chiral
  superfields `Phi^I`.
- Stated the rigid special-Kahler potential
  `K_F=(2 pi)^(-1) Im(bar a^I F_I)` with the chapter's normalization.
- Proved
  `g_{I bar J}=partial_I partial_barJ K_F=(2 pi)^(-1) Im tau_IJ`.
- Recorded the precise effects of linear prepotential shifts and real
  quadratic prepotential shifts: the former are Kahler transformations, while
  the latter shift theta-angle coordinates but not the scalar metric.
- Extended `calculation-checks/sw_su2_periods.py`, the calculation-check
  README, and the Chapter 07 dossier with an exact finite check of the
  rigid special-Kahler metric identity and real theta-shift invariance.

## Verification

- `python3 calculation-checks/sw_su2_periods.py`: passed.
- `python3 -m py_compile calculation-checks/sw_su2_periods.py`: passed.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean before this audit note; rerun after adding the
  note before finishing.
- `tools/build_monograph.sh`: passed and produced
  `monograph/tex/main.pdf` with 1976 pages and file size 7912688 bytes.
