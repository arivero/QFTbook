# Issue #261 Yang--Mills Mass-Gap Status Pass

## Scope

- Oldest active GitHub issue: `#261`, on the missing explicit statement that
  four-dimensional pure Yang--Mills continuum existence together with a
  positive mass gap is the Clay Millennium problem.
- Required repair: add status remarks in the Yang--Mills setup and QCD
  dimensional-transmutation discussion.

## Content Added

- Added the remark "Status of four-dimensional quantum Yang--Mills" to the
  classical Yang--Mills chapter.
- Stated that the chapter constructs classical local connection, curvature,
  invariant action, and matter couplings, not a completed continuum quantum
  theory.
- Named the pure compact-gauge-group \(D=4\) Yang--Mills existence and
  positive mass-gap problem on \(\mathbb R^4\) as the Clay Millennium problem.
- Stated what such a theorem would need to construct: continuum correlation
  functions or an equivalent operator-algebraic/Hilbert-space theory satisfying
  standard structural axioms and a strictly positive spectral gap above the
  vacuum.
- Added the remark "Mass-gap problem and the status of continuum
  Yang--Mills" after dimensional transmutation in the QCD chapter.
- Clarified that the formal action and perturbative renormalized Green
  functions are separate from a nonperturbative continuum measure or equivalent
  quantum theory with gap.
- Stated that finite-lattice Yang--Mills at nonzero spacing is well-defined
  and gives strong evidence, while the four-dimensional continuum limit plus
  gap remains a separate mathematical problem.
- Updated the Yang--Mills and QCD chapter dossiers.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
