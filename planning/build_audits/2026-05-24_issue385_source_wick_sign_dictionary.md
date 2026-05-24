# Issue #385 Source Wick-Sign Dictionary Audit

GitHub issue #385 asked for the Lorentzian \(iJ\phi\) versus Euclidean
\(+J\phi\) source relation to be displayed in the boundary-value dictionary.
The issue body proposed a \(Z_L[-J]\) relation.  Rechecking the manuscript's
fixed Wick convention shows that the sign depends on the contour orientation.

## Manuscript Convention

Volume I uses the lower-half-plane imaginary-time convention
\[
  z^0=-i\tau,\qquad dz^0=-i\,d\tau .
\]
For the Lorentzian source convention
\[
  Z_L^{(+)}[J]
  =
  \langle0|T\exp(i\int J\phi)|0\rangle ,
\]
the source exponent rotates as
\[
  i\int_{C_-} dz^0\,J_C(z^0,\vec x)\phi(z^0,\vec x)
  =
  \int d\tau\,J_C(-i\tau,\vec x)\phi_E(\tau,\vec x).
\]
Thus the Euclidean source convention \(+\int J_E\phi_E\) is the
\(C_-\) boundary value of \(Z_L^{(+)}\) with
\[
  J_E(\tau,\vec x)=J_C(-i\tau,\vec x).
\]
There is no extra minus sign in this convention.

## Opposite-Contour Convention

For the opposite contour \(C_+\), \(z^0=+i\tau\), one has
\[
  i\,dz^0=-d\tau .
\]
In that convention \(+\int J_E\phi_E\) is represented by
\(Z_L^{(+)}[-J_C]\), equivalently \(Z_L^{(-)}[J_C]\), after the corresponding
source relabelling.

## Files Changed

- `monograph/tex/volumes/volume_i/chapter11_lorentzian_green_functions_and_analytic_continuation.tex`
- `planning/chapter_dossiers/volume_i/chapter11_lorentzian_green_functions_analytic_continuation.md`

This closes the sign gap without importing an incompatible convention into
the manuscript's existing lower-half-plane analytic-continuation setup.
