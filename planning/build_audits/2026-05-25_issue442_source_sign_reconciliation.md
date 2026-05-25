# Issue #442 Source-Sign Reconciliation

## Scope

- GitHub issue #442: the opening Lorentzian source convention
  \(+\ii\langle J,\phi\rangle\) in the generating-functional chapter could be
  read as inconsistent with the later Euclidean convention
  \(-\langle J,\phi\rangle\), and with the plus-source convention used in the
  fixed-point CFT source chart.

## Resolution

- The monograph now states the Wick-rotation chain at the first Lorentzian
  source definition:
  \[
    \ii S_L+\ii\langle J_L,\phi\rangle_L
    \mapsto
    -S_E+\langle J_L^{\rm W},\phi_E\rangle_E .
  \]
- Therefore a Euclidean plus-source convention has \(J_E^+=J_L^{\rm W}\),
  while the positive-measure/free-energy convention
  \[
    Z_E[J_E]=\int \exp\{-S_E-\langle J_E,\phi\rangle_E\}
  \]
  has \(J_E=-J_L^{\rm W}\).
- The CFT opening chapter now explicitly identifies its source \(J^A\) as the
  Euclidean plus-source coordinate.  Hence \(J^A=J_L^{{\rm W},A}\) for scalar
  insertions in the Lorentzian lower-half-plane convention, but
  \(J^A=-J_E^A\) relative to a Euclidean source written with a minus sign in
  the exponent.

## Guardrail

The sign is a source-coordinate convention, not a difference of Green
functions.  Connected correlators are recovered only after applying the
derivative normalizations stated in the Lorentzian--Euclidean source bridge.
Operators with Lorentz, spinor, or time-derivative indices still require their
own Wick-rotation matrices.
