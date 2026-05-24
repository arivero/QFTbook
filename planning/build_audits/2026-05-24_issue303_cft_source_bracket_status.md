# Build Audit: Issue #303 CFT Source-Bracket Status

Date: 2026-05-24

Scope:

- `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`
- `planning/chapter_dossiers/volume_iii/chapter01_fixed_points_conformal_data.md`

Issue addressed:

- GitHub #303 asked that the fixed-point source functional
  \(W_\ast[g,J]\) and the associated angle brackets be classified explicitly:
  constructive measure, formal Wilsonian/lattice limit, abstract CFT
  correlator data, or perturbative formal notation.

Mathematical changes:

- Added Definition `def:cft-fixed-point-source-bracket-status`.
- The definition identifies \(Z_\ast[g,J]=\exp\{-W_\ast[g,J]\}\) as
  source-functional data of the fixed point.
- The bracket
  \(\langle\exp(\int\sqrt g\,J^A\mathcal O_A)\rangle_{g,\ast}\) is now
  defined as shorthand for \(Z_\ast[g,J]\), with its mathematical type
  supplied by the fixed-point construction.
- The definition separates four cases:
  constructive Euclidean measure/generalized random field, lattice or
  Wilsonian continuum-limit source functional, abstract CFT generating
  functional for Schwinger distributions and contact terms, and perturbative
  formal source series.
- The chapter dossier now records the bracket status in both the definitions
  and claims.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.
