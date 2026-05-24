# Issue #316: BPHZ Path-Integral Status Declaration

## Issue

The BPHZ chapter began directly with graph integrands and momentum-space
subtractions, without first stating the path-integral status of the objects
being renormalized.

## Resolution

- Added a first section, `Path-Integral Status: Formal Coefficientwise
  Renormalization`, before the graph-theoretic definitions.
- Stated the regulated Euclidean source-functional setting and the formal
  expansion in local couplings.
- Identified BPHZ as a graph-by-graph operation on coefficient distributions
  \(G^{(\nu)}_{\Lambda,n}\) and 1PI kernels.
- Explicitly ruled out reading the chapter as a construction of an unregulated
  continuum measure or as a nonperturbative definition of the QFT.
- Updated the chapter dossier so future passes preserve this status boundary.

## Verification

Run from a clean worktree:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
