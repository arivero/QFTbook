# 2026-05-22 Noether and Stress-Tensor Source/Figure Audit

## Scope

- Source block: `references/253a lectures 2022.pdf`, pp. 63--71.
- Monograph target:
  `monograph/tex/volumes/volume_i/chapter07_symmetries_noether_theorem_and_stress_tensors.tex`.
- Rendered PDF: `monograph/tex/main.pdf`, physical pages 72--78, printed
  pages 56--62.

## Source Trace Reviewed

Rendered handwritten source images:

- `monograph/tex/build/source_visual_trace/253a_trace-063.png`
- `monograph/tex/build/source_visual_trace/253a_trace-064.png`
- `monograph/tex/build/source_visual_trace/253a_trace-065.png`
- `monograph/tex/build/source_visual_trace/253a_trace-066.png`
- `monograph/tex/build/source_visual_trace/253a_trace-067.png`
- `monograph/tex/build/source_visual_trace/253a_trace-068.png`
- `monograph/tex/build/source_visual_trace/253a_trace-069.png`
- `monograph/tex/build/source_visual_trace/253a_trace-070.png`
- `monograph/tex/build/source_visual_trace/253a_trace-071.png`

## Content Checks

- The Poincare transformation of a scalar field, including
  \(\phi'(x')=\phi(x)\) and the fixed-coordinate infinitesimal variation
  \(-\left(a^\mu+\omega^\mu{}_\nu x^\nu\right)\partial_\mu\phi\), is present.
- The Noether derivation states the variational framework, the
  Euler--Lagrange expression, the total-derivative term \(K_R^\mu\), and the
  current \(j_R^\mu=\partial\mathcal L/\partial(\partial_\mu\phi^A)R^A-K_R^\mu\).
- The compactly supported local-parameter derivation has been added:
  the current is identified as the coefficient of \(\partial_\mu\epsilon\).
- The charge conservation statement is represented both algebraically and by a
  TeX time-slab figure with boundary flux.
- The canonical-generator statement now includes the direct first-order check
  and the velocity-dependent time-translation example \(Q=-\tau H\).
- Translation currents, the canonical stress tensor, and the scalar
  \(T^{00}=\mathcal H\) calculation are included.
- The localized-translation derivation of \(T^\mu{}_\nu\) has been added as
  the coefficient of \(\partial_\mu\xi^\nu\).
- Lorentz currents and angular-momentum/boost charges are included, with
  conservation derived from stress-tensor conservation and symmetry.
- The source statement that the stress tensor is a well-defined local quantum
  operator is kept in qualified monograph form: a renormalized stress tensor is
  used when it exists as an operator-valued distribution in the chosen
  framework.

## Figure/Render Checks

- Rendered pages inspected:
  `/tmp/qft_ch10_noether_audit-072.png` through
  `/tmp/qft_ch10_noether_audit-078.png`.
- The time-slab charge-flux diagram is legible, labels do not collide, and the
  figure conveys the boundary-flux content of the source derivation.
- No overcrowded display equations or visual collisions were observed in the
  newly added local-parameter, Poincare, or localized-translation material.

## Build

- `tools/build_monograph.sh` completed successfully after the chapter edits.
- The build log scan was clean apart from the pre-existing hyperref warning in
  a later chapter.
