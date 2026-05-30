# Doplicher--Roberts Pointed Crossed-Product Example

Date: 2026-05-30.

Scope:
`monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`
and `calculation-checks/dhr_dr_reconstruction_checks.py`.

## Repair

- Expanded the finite pointed Doplicher--Roberts diagnostic beyond the compact
  group output.
- Added an explicit algebraic field-core example for an invertible order-\(N\)
  localized sector:
  \[
    \mathcal F_{\rm alg}
    =
    \bigoplus_{q\in\mathbb Z/N\mathbb Z}\mathcal A u^q,
    \qquad
    uAu^*=\rho(A).
  \]
- Verified in text that multiplication, involution, and the \(\mu_N\) gauge
  action recover the neutral observable algebra as the fixed algebra.
- Extended the calculation check so the finite toy model verifies
  associativity, anti-multiplicativity of the involution, tensor
  automorphisms, and gauge averaging.

## Standard Applied

This is written as an example rather than a theorem.  The algebraic crossed
product is an exact finite diagnostic of the DR output for pointed invertible
sectors; it does not prove the QFT-specific DHR hypotheses.  The manuscript
now makes that separation explicit.
