# Finite Tomita Standard-Form Model

Date: 2026-05-30.

Scope:
`monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`
and `calculation-checks/tomita_standard_form_checks.py`.

## Repair

- Added a fully proved finite-dimensional model of the standard form for
  \(\mathcal B(K)\) with faithful state \(\omega(A)={\rm Tr}(\rho A)\).
- Derived cyclicity and separatingness of \(\Omega=\rho^{1/2}\) in the
  Hilbert-Schmidt GNS space.
- Computed the Tomita operator, modular conjugation, and modular operator:
  \[
    S(X)=\rho^{-1/2}X^*\rho^{1/2},
    \qquad
    J(X)=X^*,
    \qquad
    \Delta(X)=\rho X\rho^{-1}.
  \]
- Verified \(J\pi(\mathcal R)J=\pi(\mathcal R)'\), the modular automorphism
  \(\sigma_t(A)=\rho^{\ii t}A\rho^{-\ii t}\), and the sign relation between
  this modular flow and the KMS convention used in the chapter.

## Standard Applied

The general Tomita--Takesaki theorem remains a theorem boundary, but the
finite matrix-algebra case is now constructed directly from Hilbert-Schmidt
linear algebra.  This gives the reader a concrete standard-form calculation
before the infinite-dimensional theorem boundary and fixes the modular/KMS
sign convention by an explicit trace identity.
