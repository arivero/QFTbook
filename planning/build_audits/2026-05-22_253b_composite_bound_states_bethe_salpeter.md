# 2026-05-22 253b Composite Bound States and Bethe--Salpeter Audit

## Source Block

- Primary handwritten source: `references/253b lecture notes 2023.pdf`,
  pp. 27--33.
- Source visual trace:
  `monograph/tex/build/source_visual_trace/253b_trace-027.png` through
  `monograph/tex/build/source_visual_trace/253b_trace-033.png`.
- Operational transcription cross-check:
  `transcription/tex/253b/scattering_rg_qcd.tex`, lines 1186--1635.
- Student transcription comparison aid:
  `references/253b transcribed lecture notes.tex`, lines 1751--2179.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter05_composite_bound_states_and_bethe_salpeter_amplitudes.tex`.
- Updated the chapter dossier and the 253a/253b no-skip coverage register.

## Certified Content

- Below-threshold first-sheet pole for a stable composite two-particle
  species, with \(s=-(k_1+k_2)^2\) and \(t=-(k_1-k_3)^2\) stated.
- \(D=2\) \(\phi^4\) bubble integral, Feynman-parameter form, geometric
  bubble-chain denominator, and the fact that external \(Z_\phi^{1/2}\) factors
  do not change the pole position.
- Threshold estimate
  \(f(4m^2-\delta)\simeq \pi/(m\sqrt\delta)\), weak attractive pole
  \(\delta\simeq(g/(8m))^2\), and
  \(M_B\simeq2m-g^2/(256m^3)\).
- Stabilized-potential caveat for the negative local quartic coefficient,
  including the sine-Gordon local expansion with
  \(g_{\mathrm{local}}=-m^2\beta^2\).
- Bethe--Salpeter amplitude as a time-ordered matrix element with explicit
  plane-wave normalization and distributional-state warning.
- Four-point spectral factorization through the bound-state pole and the
  residue product
  \(\widetilde\Phi_B(k_1,k_2;P)\widetilde\Phi_B^*(-k_3,-k_4;P)\).
- Two-particle irreducible kernel definition, excluded two-particle cuts,
  inhomogeneous scattering-block recursion, and homogeneous
  Bethe--Salpeter equation
  \((\mathbf 1-\widehat V_P)\Psi_B=0\).
- Relation between amputated and unamputated Bethe--Salpeter amplitudes and
  the corresponding unamputated integral equation.

## Figure Audit

- Compared the source-page pole sketch, bubble-chain diagram, four-point
  factorization diagram, and two-particle-kernel/Bethe--Salpeter diagrams with
  the compiled TikZ figures.
- Revised the kernel figure to show the allowed two-particle-irreducible block,
  the excluded two-kernel diagram with a two-particle cut, the
  \(\mathcal T=\mathcal K+\mathcal K\mathcal G\mathcal T\) recursion, and the
  homogeneous zero-mode equation.
- Rendered manuscript physical pages 186--191, corresponding to printed
  pages 169--174, and checked that the figures were present and legible.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- `pdftoppm -png -f 186 -l 191 -r 170 monograph/tex/main.pdf /tmp/qft_ch26_bethe_exact`
- `pdftoppm -png -f 190 -l 190 -r 170 monograph/tex/main.pdf /tmp/qft_ch26_bethe_fixed2`
