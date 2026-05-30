# Finite-N Circular Wilson-Loop Localization Pass

## Scope

- Continued the Volume VII issue #626 localization-depth lane.
- Targeted the \(\mathcal N=4\) \(S^4\) Gaussian matrix-model subsection,
  where the planar Bessel result was present but the exact finite-\(N\)
  localization output was not derived.

## Change

- Added the exact finite-\(N\) formula
  \[
    \left\langle {1\over N}\operatorname{Tr} e^X\right\rangle
    =
    {1\over N}e^{\lambda/(8N)}
    L_{N-1}^{(1)}\!\left(-{\lambda\over4N}\right)
  \]
  in the circular-loop Gaussian coupling convention of the chapter.
- Derived the formula from the Hermite orthogonal-polynomial kernel for the
  finite \(U(N)\) Gaussian matrix model, including the Hermite
  generating-function integral and the finite Laguerre summation identity.
- Extended `calculation-checks/susy_n4_scft_checks.py` with exact rational
  checks for \(N=1\), \(N=2\), and the first finite-\(N\) weak coefficients.

## Status

This pass strengthens the \(S^4\) localization application once the Gaussian
matrix model has been obtained.  It does not change the separate
field-theoretic matching hypothesis for the \(S^4\) path integral or the
Nekrasov instanton compactification.
