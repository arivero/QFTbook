# QCD2 Closed-Form Spectral Pass

## Scope

This pass advances GitHub issue #596 on the two-dimensional large-\(N\) QCD
side.  The earlier chapter derived the light-front constraint, planar
color-singlet equation, endpoint exponents, and DLCQ matrix.  The missing
mathematical layer was the continuum spectral object itself: the formal
principal-value equation needs to be tied to a closed positive quadratic form
and a self-adjoint mass operator before one speaks of its spectrum.

## Changes

- Added Section `Closed Form Domain and Discrete Spectrum` to
  `monograph/tex/volumes/volume_ii/chapter20c_large_n_two_dimensional_qcd_light_front.tex`.
- Defined the Hilbert space \(L^2(0,1)\), the closed form
  \(\mathfrak q_{m_1,m_2,\gamma_2}\), and the form domain with explicit
  endpoint weights.
- Proved that for \(\gamma_2>0\) the form is densely defined, nonnegative,
  and closed, and therefore defines a unique nonnegative self-adjoint
  operator.
- Checked that the operator acts by the displayed subtracted principal-value
  expression on smooth functions where the finite part exists.
- Proved compact resolvent by the \(H^{1/2}\) form-domain compact embedding
  into \(L^2(0,1)\), giving a discrete spectrum with finite multiplicities.
- Identified the massless constant zero eigenspace and the positive-endpoint
  mass exclusion of zero eigenvectors.
- Added the finite Rayleigh--Ritz/min-max interpretation connecting the
  continuum form to DLCQ matrices without treating finite matrices as
  continuum evidence by themselves.

## Calculation Check

Extended `calculation-checks/thooft_model_checks.py` with an exact rational
finite-form monotonicity check.  The check verifies that increasing the
endpoint masses and \(\gamma_2\) changes the DLCQ quadratic form by exactly
the positive increment form, matching the continuum closed-form coordinate.

## Status

This is not a closure of #596.  It closes a real continuum spectral-definition
gap for the 2D large-\(N\) QCD chapter.  The issue still requires deeper
Chern--Simons vector-model continuum solutions, broader light-front examples,
and model-specific zero-mode analyses.
