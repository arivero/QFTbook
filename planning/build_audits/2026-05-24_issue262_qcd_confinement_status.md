# Issue #262 QCD Confinement Status Pass

## Scope

- Oldest active GitHub issue: `#262`, on the QCD chapter stating confinement
  without explicitly marking the derivation from the four-dimensional
  continuum QCD Lagrangian as open.
- Required repair: revise confinement language so the spectral
  color-singlet-asymptotic-state property is presented as a nonperturbative
  hypothesis/physical input, not a theorem currently derived from the
  continuum Lagrangian.

## Content Added

- Revised the infrared-possibilities discussion to say that the confining
  regime is a conditional infrared scenario.
- Replaced the unqualified confinement statement by a spectral and observable
  hypothesis: isolated finite-energy asymptotic particles carry no color, and
  physical states are created by gauge-invariant operators.
- Added the explicit statement that deriving this spectral property from the
  four-dimensional continuum QCD Lagrangian is an open nonperturbative problem.
- Revised the "Color and Physical External States" section so confinement is
  described as a nonperturbative physical input supported by the observed
  hadron spectrum and lattice evidence, rather than a theorem presently
  derived from the continuum Lagrangian.
- Updated the QCD chapter dossier.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
