# Issue #266 Goldstone/Higgs/BRST Caveat Audit

## Scope

- Updated the Goldstone theorem section in the global anomalies, spontaneous
  symmetry breaking, and pions chapter.
- Updated the chapter dossier symbol and claim ledgers.

## Content Added

- Added `rem:goldstone-gauge-brst-higgs` immediately after the positive
  Hilbert-space Goldstone spectral argument.
- Stated that the Goldstone theorem used there concerns global charges acting
  on the physical positive Hilbert space.
- Separated gauged directions from global symmetries: covariant gauge fixing
  uses a Krein space before the BRST quotient.
- Displayed the Abelian Higgs quadratic term
  \[
    |D_\mu\phi|^2
    =
    \frac12(\partial_\mu h)^2
    +
    \frac12(\partial_\mu\pi-m_AA_\mu)^2+\cdots ,
    \qquad m_A=gv,
  \]
  and the gauge-invariant vector coordinate
  \(\mathcal A_\mu=A_\mu-m_A^{-1}\partial_\mu\pi\).
- Added the \(R_\xi\) gauge-fixing functional
  \(F_\xi=\partial^\mu A_\mu-\xi m_A\pi\), the gauge-dependent unphysical
  masses, and the BRST doublet/quartet interpretation.

## Verification Target

- The issue requested a remark on the Higgs/Kibble mechanism in gauge theory
  and the BRST-quartet structure.  The manuscript now states both at the
  point where the Goldstone theorem is used.
