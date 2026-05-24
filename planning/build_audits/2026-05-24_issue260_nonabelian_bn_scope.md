# Issue #260 Nonabelian Bloch--Nordsieck Scope Pass

## Scope

- Oldest active GitHub issue: `#260`, on the missing warning that the
  Bloch--Nordsieck construction in the infrared QED chapter is Abelian and
  does not transfer directly to QCD.
- Required repair: flag the Abelian/nonabelian distinction in the QED
  infrared chapter and add a reciprocal cross-reference from the QCD
  factorization discussion.

## Content Added

- Added the remark "Abelian scope of Bloch--Nordsieck cancellation" to the
  infrared QED chapter.
- Stated that the QED derivation relies on scalar commuting soft-photon
  factors depending on hard charges and momenta.
- Stated the nonabelian replacement: soft-gluon factors act as color-space
  operators organized by Wilson lines and color-ordered products.
- Cross-referenced the QCD factorization formula
  \(\eqref{eq:dis-factorization}\) and DGLAP equation
  \(\eqref{eq:dglap-evolution}\).
- Labeled the QCD section "Twist, Parton Distributions, and Factorization."
- Added a QCD paragraph explaining that summing unresolved final-state gluons
  supplies the final-state part of an infrared-collinear safe observable, while
  initial-state collinear singularities of incoming colored partons are
  absorbed into the renormalized Wilson-line light-ray operator defining the
  PDF.
- Stated that the remaining factorization-scale dependence is DGLAP evolution.
- Updated the QED and QCD chapter dossiers.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
