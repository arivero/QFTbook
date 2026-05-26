# Issue #582 Modelled-Distribution Fixed-Point Pass

## Scope

- GitHub issue: `#582`.
- Manuscript locus:
  `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Calculation-check locus:
  `calculation-checks/constructive_scalar_spde_checks.py`.

## Content Added

- Added an abstract local fixed-point theorem for modelled distributions on
  a parabolic time slab.  The theorem defines:
  - the Banach space \(E_T\) of modelled distributions,
  - the forcing space \(F_T\),
  - the zero-initial-time abstract heat integration map \(\mathcal K_T\),
  - the lifted stochastic-plus-initial datum \(P_Tu_0+X_T\), and
  - the nonlinear map
    \[
      \Psi_T(U)=P_Tu_0+X_T+\mathcal K_T(-\lambda U^3+MU).
    \]
- Proved the ball-mapping estimate
  \[
    A T^\theta(B|\lambda|R^3+D|M|R)\le R/2
  \]
  and the contraction estimate
  \[
    A T^\theta(2B|\lambda|R^2+D|M|)<1.
  \]
- Gave the Picard-iteration proof internally: the proof derives the
  geometric tail bound \(q^n(1-q)^{-1}\|U_1-U_0\|\), uses completeness of
  \(E_T\), proves the fixed-point equation by continuity, and proves
  uniqueness from \(q<1\).
- Added Lipschitz dependence on the lifted initial data plus stochastic
  convolution.
- Replaced a previous invocation of the contraction theorem in the
  Da Prato--Debussche Sobolev fixed-point proof with the corresponding
  Picard-iteration argument.
- Updated the quoted theorem boundary so that the remaining analytic task is
  the verification of the Schauder and product estimates for the concrete
  BPHZ model, not the abstract contraction argument itself.
- Added exact calculation checks for the ball condition, contraction
  constant, and Picard tail arithmetic.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- Independent log scan passed:
  `rg -n "LaTeX Warning: Reference|LaTeX Warning: Citation|Latex failed to resolve|Undefined control sequence|Overfull|Underfull|Fatal error|Emergency stop|Missing .* inserted|Token not allowed" monograph/tex/main.log monograph/tex/build/latexmk.out`
  returned no matches.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1458`.

## Issue Status

This pass advances issue `#582` but does not close it.  Remaining components
include construction and convergence of the BPHZ-renormalized random model,
verification of the concrete Schauder/product hypotheses for that model, and
the SPDE-to-OS passage.
