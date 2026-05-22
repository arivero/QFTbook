# 2026-05-22 Global Anomalies, SSB, And Pion EFT Audit

## Scope

- Source block: second-sequence handwritten material, pages 226--257.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, from the perturbative
  global-anomaly example through spontaneous symmetry breaking, chiral
  symmetry breaking, pion effective theory, Wess--Zumino--Witten matching,
  mass spurions, and \(\pi^0\to2\gamma\).
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`.

## Source Content Checked

- Four-dimensional perturbative example with one vector current and two axial
  currents, including the \(D=4-\epsilon\) split
  \(\ell=\ell_\parallel+\ell_\perp\), the evanescent trace, the \(1/3\)
  symmetric replacement, the contact-term Ward identity, and the finite
  background variation \((48\pi^2)^{-1}\int \zeta\,\epsilon FF\).
- Finite-dimensional double-well comparison, exponentially small tunneling,
  infinite-volume suppression, and the locality/cluster argument that local
  operators are diagonal between pure homogeneous phases.
- General spontaneous symmetry breaking, \(G/H\) Goldstone coordinates,
  Maurer--Cartan data, and the spectral Goldstone theorem with a current pole
  forced by the Ward identity.
- Explicit \(U(1)\) Goldstone model in polar variables, current
  \(j^\mu=2r^2\partial^\mu\theta\), charge action on \(\theta\), massive
  radial mode, and pseudo-Goldstone mass from a small
  \(-\epsilon\operatorname{Re}\phi\) deformation.
- Massless QCD chiral symmetry, condensate orientation, diagonal
  \(SU(N_f)_V\), Vafa--Witten positivity caveat at \(\theta=0\), and the
  axial phase tied to the \(\theta\)-angle.
- \(SU(2)\) stereographic pion coordinates, nonlinear
  \(SU(2)_L\times SU(2)_R\) transformation, corrected
  \(\vec D_\mu=\partial_\mu\vec\xi/(1+\vec\xi^{\,2})\) building block and
  transformation, and the two four-derivative invariants relevant to
  four-pion scattering.
- Low-energy pion scattering, \(A(s,t,u)=4s/F_{\rm st}^2+O(E^4/F_{\rm st}^4)\),
  the one-loop logarithms, local \(C_4,C'_4\) terms, and the Wilsonian cutoff
  running of \(C_4(\Lambda)\) and \(C'_4(\Lambda)\).
- Two-flavor mass deformation written both in spurion form and in the
  source-specific order-parameter normalization, including the leading
  \(m_\pi^2\) relation and the physical \(135\) MeV and \(140\) MeV pion mass
  values.
- Wess--Zumino functional as a five-dimensional filling, quantization of the
  coefficient, \(n=N_c\) anomaly matching, and the electromagnetic
  specialization giving the microscopic axial-flavor triangle and the local
  neutral-pion two-photon vertex.

## Manuscript Changes

- Expanded the chapter from a general anomaly-matching and pion-EFT overview
  into a source-controlled sequence covering pages 226--257 without skipping
  the explicit calculations that carry conceptual content.
- Added source-specific derivations for the perturbative global-anomaly
  contact term, vacuum-sector superselection, the \(U(1)\) Goldstone model,
  the \(N_f=2\) stereographic chart, pion scattering at \(O(E^4)\), and the
  two-flavor mass normalization.
- Corrected the stereographic building block from an incorrectly normalized
  auxiliary vector to
  \(\vec D_\mu=\partial_\mu\vec\xi/(1+\vec\xi^{\,2})\), and recorded its
  transformation with the \((\vec\xi\times\vec\theta_A)\times\vec D_\mu\)
  structure.
- Added or repaired the double-well, \(U(1)\) vacuum/tilt, pion-scattering,
  WZW filling, electromagnetic axial-flavor triangle, and
  \(\pi^0\gamma\gamma\) figures.

## Rendered Check

Completed after the full build on 2026-05-22.

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/qft253b_ssb_pions_src-226.png` through
  `/tmp/qft253b_ssb_pions_src-257.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_ch47_ssb_pions_final-337.png` through
  `/tmp/qft_ch47_ssb_pions_final-351.png`.
- Rendered figure checks:
  `fig:double-well-finite-volume`,
  `fig:u1-goldstone-vacuum-circle`,
  `fig:pion-scattering-leading-next`,
  `fig:wzw-five-dimensional-filling`,
  `fig:em-axial-flavor-triangle`, and
  `fig:pi-zero-two-photon-decay`.
- The \(U(1)\) panel labels were polished after the initial render so that
  the panel title and potential-axis labels do not overlap.
- The manuscript convention in the stereographic section is
  \(U\mapsto LUR^{-1}\).  The handwritten notes use the opposite left/right
  naming in places; the compiled chapter is self-consistent, and future edits
  should convert all formulas together if the convention is changed.

## Verification

- `tools/build_monograph.sh` completed cleanly after the TeX edits.
- The strict monograph text audit inside the build completed cleanly.
- `git diff --check` and an explicit final strict-text audit should be run
  before committing this pass.

This promotes handwritten 253b pages 226--257 to certified coverage after the
global-anomaly, spontaneous-symmetry-breaking, pion-EFT, WZW, and
electromagnetic-anomaly figure audit.
