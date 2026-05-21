# Volume I, Chapter 9 Dossier: Kallen-Lehmann Spectral Representation

## Status

Current status: ready for TeX rewrite.

## Logical Role

This chapter is the first full nonperturbative bridge from local fields to
particle content. It uses only Hilbert-space positivity, translation
invariance, the spectrum condition, scalar-field covariance, and the spectral
theorem for the energy-momentum operators. It precedes perturbative
correlation-function diagrams and precedes all scattering theory.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, section "Spectral Representations
  and Particle Content", through the Kallen-Lehmann representation and the
  decomposition into one-particle and continuum spectral support.
- `references/253a_notes.tex`, corresponding Kallen-Lehmann and particle
  content sections, used only as a comparison layer.
- `monograph/tex/volumes/volume_i/chapter08_scalar_path_integrals_and_euclidean_green_functions.tex`,
  for the definitions of Wightman, time-ordered, and Euclidean Green
  functions.
- `monograph/tex/volumes/volume_i/chapter02_quantum_mechanics_relativity_and_locality.tex`,
  for invariant one-particle normalization.

## Framework

Working framework:

- Hilbert space \(\Hilb\) with unitary representation of the proper
  orthochronous Poincare group;
- invariant vacuum \(\Omega\);
- commuting self-adjoint translation generators \(P^\mu\);
- joint spectrum contained in the closed forward cone;
- scalar operator-valued distribution \(\widehat\phi\) with
  \(\langle\Omega|\widehat\phi|\Omega\rangle=0\) after shifting by a constant
  when necessary;
- matrix elements understood after smearing, with point notation used for the
  corresponding distributions.

## Notation Inventory

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(E(\Delta)\) | projection-valued measure | joint spectral measure of \(P^\mu\) |
| \(\nu_\phi\) | positive measure | spectral measure of \(\widehat\phi(0)\Omega\) |
| \(W_2(x)\) | distribution | scalar Wightman two-point function |
| \(G_T(x)\) | distribution | time-ordered two-point function |
| \(G_E(x_E)\) | distribution | Euclidean two-point function |
| \(\Delta_+(x;\mu^2)\) | distribution | positive-frequency free scalar two-point function of mass \(\mu\) |
| \(\Delta_F(x;\mu^2)\) | distribution | Feynman propagator of mass \(\mu\) |
| \(d\rho(\mu^2)\) | positive measure | Kallen-Lehmann spectral measure |
| \(Z\) | nonnegative number | atom of \(d\rho\) at an isolated one-particle mass \(m^2\) |
| \(d\rho_{\mathrm c}\) | positive measure | continuum part of the spectral measure |

## Definition Ledger

- spectral measure associated to a local scalar field acting on the vacuum;
- positive-frequency scalar two-point function \(\Delta_+\);
- Kallen-Lehmann spectral measure \(d\rho\);
- time-ordered and Euclidean Kallen-Lehmann representations;
- isolated one-particle atom and field-strength overlap \(Z\);
- continuum spectral support and threshold assumptions.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The two-point Wightman function is the Fourier transform of a positive measure supported in the forward cone. | Theorem/construction | Joint spectral theorem and spectrum condition |
| Scalar covariance makes the spectral measure a positive measure over invariant masses. | Derived | Lorentz invariance of the vacuum and scalar field |
| \(W_2(x)=\int d\rho(\mu^2)\Delta_+(x;\mu^2)\). | Derived | Disintegration of the positive spectral measure |
| \(G_T(x)=\int d\rho(\mu^2)\Delta_F(x;\mu^2)\). | Derived | Definition of time ordering and linearity |
| \(G_E(x_E)=\int d\rho(\mu^2)\Delta_E(x_E;\mu^2)\) under analytic continuation. | Framework statement/derived from Chapter 8 conditions | Spectral positivity and Euclidean continuation |
| An isolated one-particle mass created by \(\widehat\phi\) is an atom \(Z\delta(\mu^2-m^2)\) of the spectral measure. | Definition plus derivation | Projection onto the isolated mass shell |
| \(Z\) depends on the local field normalization and is intrinsic once the field is fixed. | Definition/consequence | Matrix element normalization |

## Figure Ledger

Figures to include:

- spectral projection of \(\widehat\phi(f)\Omega\) into vacuum, one-particle,
  and continuum spectral components;
- spectral measure with an isolated atom at \(m\) and continuum support
  beginning at a stated threshold.

## Audit Targets

- Use a positive measure \(d\rho\), not only a smooth function, so delta
  contributions are properly represented.
- State the assumptions behind the \(2m\) threshold.
- Do not define scattering or asymptotic states in this chapter.
- Keep \(Z\) as a field-overlap datum, not a slogan.
