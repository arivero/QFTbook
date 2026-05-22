# 2026-05-22 QCD Infrared and DIS Block Repair

## Scope

- Source block: second-sequence handwritten material, pages 202--210.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, around the Banks--Zaks,
  confinement, Wilson-line, and deep-inelastic scattering discussion.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`.

## Source Content Checked

- Dimensional transmutation and the one-loop running-coupling form.
- Banks--Zaks two-loop diagnostic, including the perturbative control
  condition and the \(SU(N)\) fundamental-window inequality.
- Confinement expectation for smaller \(N_f\), stated through color-neutral
  physical states and gauge-invariant operators.
- Open Wilson-line operator \(\bar q(x_2)W_R(C)q(x_1)\) and rectangular
  Euclidean Wilson-loop extraction of a static potential.
- Inclusive DIS process \(e^-+N\to e^-+X\) with \(q=k-k'\).
- Leading electromagnetic amplitude proportional to
  \(\bra X J^\mu(0)\ket N\).
- Inclusive hadronic tensor as a sum over final hadronic states and as a
  non-time-ordered current-current matrix element.
- Current-conservation tensor decomposition into two scalar functions.
- Physical support \(0<x_B\le1\) in the inclusive region.
- Relation between the time-ordered forward Compton amplitude and the
  inclusive tensor through a discontinuity.
- OPE of the current product, local twist-two quark and gluon operators,
  light-ray/Wilson-line operator definitions, factorization, and logarithmic
  scaling violation.

## Manuscript Changes

- Added an inclusive DIS kinematics figure.
- Expanded the hadronic tensor section from a compressed definition to the
  source-level chain: amplitude, inclusive sum, Wightman tensor,
  tensor decomposition, support, forward-Compton discontinuity, and OPE.
- Added an OPE/local-tower/light-ray figure that separates operator
  definitions from parton-model language.
- Added the source logarithmic scaling-violation formula in terms of the
  one-loop anomalous-dimension coefficient and the QCD beta-function
  coefficient.

## Rendered Check

Completed after the full build on 2026-05-22.

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/qft253b_ir_dis_src-202.png` through
  `/tmp/qft253b_ir_dis_src-210.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_ir_dis_compiled2-318.png` through
  `/tmp/qft_ir_dis_compiled2-326.png`.
- The DIS kinematics figure was checked against the handwritten scattering
  diagram on source page 206.  It preserves the incoming and outgoing
  electron momenta, the virtual photon momentum \(q=k-k'\), the target
  hadron, and the inclusive summed hadronic final state.
- The Wightman tensor, tensor decomposition, support statement, forward
  Compton relation, OPE/light-ray figure, local twist-two operators, and
  logarithmic scaling-violation formula all render without overlap or
  missing labels.

This promotes the pp. 202--210 block to `certified after infrared/DIS
figure audit`.
