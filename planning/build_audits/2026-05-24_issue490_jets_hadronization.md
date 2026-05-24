# Issue #490 Jets And Hadronization Pass

## Scope

- Addressed GitHub issue #490:
  `[Vol IV] Jets and hadronization — careful treatment beyond sloppy particle-physics-literature presentation`.
- Added the compiled chapter
  `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
  to the Volume IV include sequence after the QCD chapter.

## Content Added

- Physical-state definition of weighted final-state cross sections.
- Partonic measurement functions as perturbative representatives after
  regulator and renormalization choices.
- IRC safety definition with soft and collinear limits plus local
  integrability estimates.
- Fixed-order finiteness criterion under displayed soft/collinear
  factorization hypotheses and KLN summation.
- Sterman--Weinberg two-jet observable.
- Generalized \(k_T\), Cambridge--Aachen, and anti-\(k_T\) algorithms, with
  an IRC-safety proof for the sequential recombination family.
- Factorization and resummation discussion with hard, jet, and soft functions.
- Controlled-approximation statements for perturbative jet predictions and
  parton showers.
- Fragmentation-function operator definition and status of hadronization
  models.
- Classification of final-state observables by the QCD input each requires.

## Planning Updates

- Updated the Volume IV chapter list and development targets in
  `planning/04_master_architecture.md`.
- Added the 2026-05-24 project decision on jets and hadronization in
  `planning/11_project_decisions.md`.
- Updated Volume IV dependency-map supplies and immediate targets in
  `planning/13_development_dependency_map.md`.
- Added the chapter dossier
  `planning/chapter_dossiers/volume_ii/chapter19b_jets_ir_safe_observables_hadronization.md`.

## Verification Targets

- The chapter must compile as part of Volume IV.
- The monograph text audit must remain clean.
- The new dossier must satisfy the chapter-dossier metadata audit.
