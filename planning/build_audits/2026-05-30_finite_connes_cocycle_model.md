# Finite Connes Cocycle Model

Date: 2026-05-30.

Scope:
`monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`
and `calculation-checks/tomita_standard_form_checks.py`.

## Repair

- Replaced the finite type-I Connes cocycle remark by a proved proposition.
- Derived directly in the Hilbert-Schmidt standard representation that
  \[
    \Delta_{\psi|\omega}^{\ii t}\Delta_\omega^{-\ii t}
  \]
  is left multiplication by
  \[
    u_t=\rho_\psi^{\ii t}\rho_\omega^{-\ii t}.
  \]
- Proved inside the manuscript that \(u_t\in\mathcal R\) is unitary, satisfies
  \(u_{t+s}=u_t\sigma_t^\omega(u_s)\), and implements
  \(\sigma_t^\psi(A)=u_t\sigma_t^\omega(A)u_t^*\).
- Extended the finite modular calculation check to a noncommuting pair of
  faithful density matrices, verifying the relative modular product, unitarity,
  cocycle law, and flow implementation.

## Standard Applied

The general Connes Radon--Nikodym theorem remains a theorem boundary.  The
finite standard-form model is now fully derived, so the reader sees the
algebra element constructed by the theorem and the order of the noncommuting
density-matrix factors before the type-\(\mathrm{III}\) statement is used in
local QFT.
