# Issue #329 Fock-Space Construction Pass

Date: 2026-05-24

## Files Touched

- `monograph/tex/volumes/volume_i/chapter12_haag_ruelle_scattering_theory.tex`
- `monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `planning/chapter_dossiers/volume_i/chapter12_haag_ruelle_scattering_theory.md`

## Mathematical Point

The manuscript now displays the missing construction step:

- the scalar one-particle sector is represented by a unitary
  \(W_1:L^2(\Sigma_m^+,d\mu_m)\to\Hilb_1\);
- translations act by multiplication by \(\exp(i a\cdot p)\) in this model;
- generalized kets are identified as distributional notation for this spectral
  representation;
- internal multiplicity or spin replaces \(L^2(\Sigma_m^+,d\mu_m)\) by
  \(L^2(\Sigma_m^+,d\mu_m;\mathfrak k)\);
- the bosonic Fock space is the Hilbert completion of the finite symmetric
  tensor algebra and, in the spectral model, is
  \[
    \mathbb C\Omega_F\oplus
    \bigoplus_{n\ge1}
    L^2_{\rm sym}((\Sigma_m^+)^n,d\mu_m^{\otimes n}).
  \]

## Consequence

The Haag--Ruelle wave operators are now stated as maps from an explicitly
constructed free asymptotic many-particle Hilbert space into the physical
Hilbert space.  The isometry statement is tied to the displayed symmetrized
Fock inner product.
