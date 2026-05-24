# Issue 374: Wick-Rotation Jacobian

## Scope

GitHub issue #374 noted that Volume I, Chapter 11 used the contour rotation
\(\ell^0=\ii\ell_E^D\) in the one-loop tadpole calculation but did not display
the Jacobian and sign chain.

## Fix

- Added the explicit rotation data
  \[
    \ell^0=\ii\ell_E^D,\qquad
    \dd\ell^0=\ii\,\dd\ell_E^D,\qquad
    \dd^D\ell=\ii\,\dd^D\ell_E .
  \]
- Displayed the denominator transformation
  \[
    \ell^2+m^2-\ii\epsilon
    \to
    \ell_E^2+m^2 .
  \]
- Displayed the measure-propagator sign cancellation
  \[
    \dd^D\ell\,\frac{-\ii}{\ell^2+m^2-\ii\epsilon}
    \to
    \dd^D\ell_E\,\frac{1}{\ell_E^2+m^2}.
  \]
- Left the final tadpole equality in the existing convention,
  \(-\ii g/2\) times the Euclidean integral equals
  \(\ii[-g/2]\) times the Euclidean integral.
- Updated the Chapter 11 dossier.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
