# 2026-05-24 Issue #283 Scale Without Conformal Pass

## Scope

- GitHub issue: #283, "[Vol V] Scale-invariant-but-not-conformal QFT never
  distinguished from CFT".
- Manuscript target:
  `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_iii/chapter01_fixed_points_conformal_data.md`.

## Content Added

- Expanded the scale-versus-conformal remark in the opening CFT chapter.
- Defined, within the stress-tensor framework used in the monograph, a
  scale-invariant but nonconformal local QFT as one with a conserved
  dilatation current
  \(D^\mu=x_\nu T^{\mu\nu}-V^\mu\) and nonzero virial class in the quotient by
  conserved currents and admissible improvement currents.
- Stated the equivalent trace formulation:
  \(T^\mu{}_\mu=\partial_\mu V^\mu\), with no admissible improvement making
  the stress tensor traceless.
- Added the requested Polchinski citation for the virial-current obstruction.
- Updated the chapter dossier so future passes preserve this distinction.

## Harness

- Passed: `git diff --check`
- Passed: `tools/audit_monograph_text.sh`
- Passed: `tools/audit_chapter_dossiers.sh`
- Passed: `tools/build_monograph.sh`
