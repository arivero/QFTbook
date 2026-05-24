# Issue #317: Ising and Phi-Four Continuum-Limit Status

## Issue

The Ising/universality chapter constructed the lattice scaling-limit
framework, but did not record the dimension-dependent theorem status of the
continuum limits being invoked.

## Resolution

- Added a dimension-dependent status table to the scaling-limit section.
- Separated rigorous two-dimensional planar Ising scaling-limit results from
  constructive scalar \(P(\phi)_2\) and massive \(\phi^4_3\) Wightman
  constructions.
- Stated explicitly that massive \(\phi^4_3\) is a constructed Wightman QFT
  after OS reconstruction, while the three-dimensional Ising fixed point as a
  CFT is not presently constructed by a complete theorem.
- Recorded the Aizenman--Duminil-Copin four-dimensional marginal triviality
  theorem and the above-four-dimensional triviality boundary for standard
  reflection-positive Ising/\(\phi^4\) scaling problems.
- Updated the chapter dossier so later passes preserve this theorem-status
  distinction.

## Verification

Run from a clean worktree:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
