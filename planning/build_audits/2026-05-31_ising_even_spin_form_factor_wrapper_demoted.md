# Ising even spin form-factor wrapper demoted

Date: 2026-05-31

Related issue: GitHub #691, theorem/proof substance and anti-wrapper audit.

## Scope

This pass audited the even Ising spin-field form-factor block in
`volume_vi/chapter04_form_factor_bootstrap_local_operators.tex`.
The formulas are important for the later separated Euclidean spectral-series
reconstruction and for the TFFSA Ising spin-field example, but the local proof
of the product ansatz is a direct verification of Watson exchange,
semi-local cyclicity, the annihilation-pole residue, and the crossed
connected matrix element.

## Change

- Replaced the proposition/proof wrapper titled "Spin-field form factors in
  the free massive fermion" by a paragraph-level worked derivation.
- Preserved the displayed even-family formula
  \(F_{2k}^{\sigma_+}=\bar\sigma i^kP_{2k}\), the semi-local cyclicity
  equation, the annihilation-pole residue equation, the crossed mixed
  \(\coth\)-product formula, and the \(K=N=1\) matrix element used for the
  Fonseca--Zamolodchikov comparison.
- Kept theorem-family rank for the separated Euclidean spectral-series
  convergence statement below, where the analytic reconstruction and
  majorant estimates carry the mathematical content.
- Added a theorem-form audit guard against reintroducing the old title as a
  theorem/proposition/lemma/corollary wrapper.
- Updated the Volume VI Chapter 04 dossier anti-wrapper ledger.

## Status

This is another concrete #691 demotion.  The monograph-wide semantic audit of
theorem-family statements remains open.
