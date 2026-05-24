# 2026-05-24 Issue #281 Cardy Operator Entropy Pass

## Scope

- GitHub issue: #281, "[Vol V] Cardy formula and entropy/dimension relation
  absent".
- Manuscript target:
  `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_iii/chapter04_radial_quantization_state_operator.md`.

## Content Added

- Added `High-Temperature Operator Entropy and the Cardy Limit` after the free
  scalar operator partition function.
- Defined the cylinder thermal trace
  \(Z_{\rm cyl}(\beta)=\operatorname{Tr}\exp(-\beta D_{\rm rad})\) as a
  Laplace--Stieltjes transform of the positive spectral counting measure, its
  relation to \(Z_{\rm op}(q)\), and the integrated spectral counting function
  \(N(\Delta)\).
- Derived the general \(D\)-dimensional microcanonical asymptotic from
  \(\log Z_{\rm cyl}(\beta)=A\beta^{-(D-1)}+o(\beta^{-(D-1)})\):
  \[
    \log N(\Delta)=
    D A^{1/D}\left(\frac{\Delta}{D-1}\right)^{(D-1)/D}
    +o(\Delta^{(D-1)/D}).
  \]
  The manuscript states the Hardy--Littlewood Tauberian implication used to
  pass from the positive canonical trace to the integrated microcanonical
  count.
- Added the \(D=2\) modular-invariance specialization:
  \(Z(\beta)=Z(4\pi^2/\beta)\),
  \(\log Z(\beta)=\pi^2(c_L+c_R)/(6\beta)+o(\beta^{-1})\), and for
  \(c_L=c_R=c\),
  \(\log N(\Delta)=2\pi\sqrt{c\Delta/3}+o(\sqrt{\Delta})\).
- Added the spin-resolved Cardy form
  \(2\pi\sqrt{c_Lh/6}+2\pi\sqrt{c_R\bar h/6}\), with the effective-central
  charge caveat when the lowest weights are not vacuum weights.

## Harness

- Passed: `git diff --check`
- Passed: `tools/audit_monograph_text.sh`
- Passed: `tools/audit_chapter_dossiers.sh`
- Passed: `tools/build_monograph.sh`
