# Issue #318: Source-Functional Logarithm Status

## Issue

The generating-functional chapter introduced \(W=-i\log Z\) at finite
regulator without classifying the meaning of the logarithm.  Formal
perturbation theory, positive Euclidean constructions, and Lorentzian
oscillatory source functionals require different interpretations.

## Resolution

- Added `def:source-functional-log-status` before the first use of \(W\).
- Classified \(\log Z\) as:
  - the algebraic logarithm in a completed formal perturbative ring;
  - the ordinary real logarithm for a positive finite Euclidean source
    functional with \(0<Z_E[J]<\infty\);
  - a locally chosen branch of the logarithm for a zero-free Lorentzian
    complex source functional.
- Stated that changing the Lorentzian branch on a connected zero-free source
  neighborhood changes \(W\) only by a source-independent constant and hence
  does not affect connected correlators of positive order.
- Updated the chapter dossier so later passes preserve the classification.

## Verification

Run from a clean worktree:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
