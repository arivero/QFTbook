# Issue #275 Audit: Lorentzian Inversion and Radial Coordinates

## Scope

- GitHub issue: #275, ``[Vol V Ch 9] Lorentzian inversion formula
  (Caron-Huot) never mentioned''.
- Manuscript file:
  `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.
- Dossier file:
  `planning/chapter_dossiers/volume_iii/chapter09_operator_product_expansion.md`.

## Manuscript Changes

- Added a subsection on Lorentzian inversion after the distinction between
  OPE-channel conformal blocks and conformal partial waves.
- Defined the identical-scalar crossed-channel double discontinuity and stated
  the scalar Caron-Huot inversion integral with its kernel normalization.
- Recorded how poles of the spin-analytic coefficient recover squared OPE
  coefficients.
- Stated the analytic, reflection-positivity, Euclidean OPE convergence, and
  Regge-boundedness hypotheses needed before the formula is used.
- Identified the radial coordinate used later in the chapter as the
  Hogervorst--Rychkov radial variable and tied \(|\rho|<1\) to radial ordering.

## Verification

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed.
