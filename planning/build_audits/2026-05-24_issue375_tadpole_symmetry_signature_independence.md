# Issue 375: Tadpole Symmetry Factor and Signature

## Scope

GitHub issue #375 noted that Volume I, Chapter 11 asserted that the tadpole
factor \(1/2\) is the same in Euclidean and Lorentzian signature, but did not
explain why.

## Fix

- Added the explicit reason: the symmetry factor is a Wick-contraction and
  residual-automorphism count determined by the polynomial \(\phi^4\), hence
  independent of whether the perturbative weight is Euclidean or Lorentzian.
- Separated this combinatorial factor from the signature-dependent factors,
  which enter through the labelled Lorentzian vertex \(-\ii g\) and propagator
  numerator \(-\ii\).
- Updated the Chapter 11 dossier.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
