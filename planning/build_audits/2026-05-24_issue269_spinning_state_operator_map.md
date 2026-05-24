# Issue #269 Spinning State-Operator Map Audit

## Scope

- Oldest active GitHub issue addressed: `#269`, on the missing explicit
  spinning-operator construction in the radial-quantization chapter.
- Manuscript file:
  - `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
- Dossier:
  - `planning/chapter_dossiers/volume_iii/chapter04_radial_quantization_state_operator.md`

## Content Added

- Added a patchwise orthonormal tangent frame \(E_A^\mu(n)\) on
  \(S^{D-1}\), with the necessary transition-function caveat.
- Displayed the pulled-back cylinder coframe:
  \[
    \widehat e^{\hat\tau}{}_\mu=r^{-1}n_\mu,\qquad
    \widehat e^{\hat A}{}_\mu=r^{-1}E_A{}_\mu(n).
  \]
- Displayed the local \(SO(D)\) rotation
  \[
    R^{\hat a}{}_\mu(n)=r\,\widehat e^{\hat a}{}_\mu(x),
    \qquad
    R^{\hat\tau}{}_\mu=n_\mu,\quad R^{\hat A}{}_\mu=E_A{}_\mu.
  \]
- Added the vector-primary cylinder map
  \[
    \widetilde V_{\hat a}(\tau,n)
    =
    \ee^{\Delta\tau}R_{\hat a}{}^\mu(n)V_\mu(\ee^\tau n).
  \]
- Added the spin-one state map obtained by the radial limit of the cylinder
  operator, with the direction dependence identified as the frame rotation:
  \[
    \lim_{\tau\to-\infty}
    \ee^{-\Delta\tau}\widetilde V_{\hat a}(\tau,n)\ket{\vac}
    =
    R_{\hat a}{}^\mu(n)\ket{V_\mu}.
  \]

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

All checks completed cleanly on 2026-05-24.
