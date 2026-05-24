# 2026-05-24 Issue #282 Ising Bootstrap Provenance Pass

## Scope

- GitHub issue: #282, "[Vol V Ch 1] 3D Ising data: operative
  numerical-bootstrap context missing".
- Manuscript target:
  `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_iii/chapter01_fixed_points_conformal_data.md`.

## Content Added

- Strengthened the \(D=3\) Ising numerical provenance remark.
- Stated that the quoted \(\Delta_\sigma\), \(\Delta_\varepsilon\), and
  \(\nu\) values come from mixed-correlator numerical conformal bootstrap
  constraints, not from a derivation in the opening chapter.
- Identified the operative bootstrap input: crossing symmetry,
  reflection-positivity constraints, mixed correlators of \(\sigma\),
  \(\varepsilon\), and \(T_{\mu\nu}\), finite semidefinite relaxations, and
  gap assumptions defining the search.
- Separated the numerical CFT-data statement from a constructive proof of the
  lattice scaling limit.
- Updated the cited source to the JHEP publication data for Chang, Dommes,
  Erramilli, Homrich, Kravchuk, Liu, Mitchell, Poland, and Simmons-Duffin,
  "Bootstrapping the 3d Ising Stress Tensor", JHEP 03 (2025) 136,
  arXiv:2411.15300.

## Harness

- Passed: `git diff --check`
- Passed: `tools/audit_monograph_text.sh`
- Passed: `tools/audit_chapter_dossiers.sh`
- Passed: `tools/build_monograph.sh`
