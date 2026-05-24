# Issue 377: Source-Functional Wick Matching

## Scope

GitHub issue #377 noted that the relation between the Lorentzian source
functional
\[
  Z[J]=\langle\Omega|T\exp(i\int J\phi)|\Omega\rangle
\]
and the Euclidean source functional with \(+\int J_E\phi_E\) was not displayed
where the connected cumulant factor \(i^{-N}\) is introduced.

## Fix

- Added the label `eq:lsz-connected-cumulant` to the connected Lorentzian
  cumulant formula.
- Defined the local Euclidean ordered source functional
  \(Z_E[J_E]\) with source term \(+\int J_E\phi_E\).
- Displayed the source-term rotation in the manuscript's convention
  \(x^0=-i\tau\):
  \[
    i\int dx^0\,J_L(x^0)\phi(x^0)
    \mapsto
    \int d\tau\,J_L(-i\tau)\phi_E(\tau).
  \]
- Stated the resulting identification
  \(J_E(\tau,\vec x)=J_L(-i\tau,\vec x)\).
- Explained that, before contour rotation, \(N\) derivatives of the Lorentzian
  source exponential produce \(i^N\), and the prefactor \(i^{-N}\) compensates
  this to give the connected time-ordered distribution itself.
- Updated the Chapter 13 dossier.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
