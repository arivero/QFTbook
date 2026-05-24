# Issue 372: Euclidean and Lorentzian Self-Energy Matching

## Scope

GitHub issue #372 noted that Volume I, Chapters 10 and 11 used compatible
Euclidean and Lorentzian self-energy signs, but the equality of the denominator
self-energy under Wick rotation was not displayed explicitly.

## Fix

- Added the label `eq:euclidean-self-energy` to the Euclidean Dyson definition
  \[
    \widetilde G_E(k)=\frac{1}{k^2+m^2-\Sigma_E(k)} .
  \]
- Inserted the Lorentzian/Euclidean matching identity
  \[
    \Sigma(k^0=\ii k_E^D,\vec k=\vec k_E)=\Sigma_E(k_E)
  \]
  in the same regulator and local two-point subtraction convention.
- Displayed the corresponding propagator relation
  \[
    \widetilde G(\ii k_E^D,\vec k_E)=-\ii\,\widetilde G_E(k_E),
  \]
  using \(k^2=k_E^2\) at \(k^0=\ii k_E^D\) for the mostly-plus metric.
- Clarified that the factor \(\ii\) multiplying the Lorentzian insertion in the
  Dyson series is not an additional sign in the scalar denominator function
  \(\Sigma\).
- Updated the Chapter 10 and Chapter 11 dossiers.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
