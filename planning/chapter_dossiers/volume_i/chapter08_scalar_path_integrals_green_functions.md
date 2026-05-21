# Volume I, Chapter 8 Dossier: Scalar Path Integrals and Green Functions

## Status

Current status: ready for TeX rewrite.

## Logical Role

This chapter follows the Noether-current chapter and precedes the
Kallen-Lehmann spectral representation. Its role is to formulate the scalar
field path integral as a regulated extension of the time-sliced quantum
mechanical construction, then explain how Euclidean, Wightman, and
time-ordered Green functions are related by analytic continuation.

The chapter does not introduce scattering amplitudes or Feynman diagrams for
scattering. It also does not organize perturbation theory; that belongs after
the spectral and Green-function structure is in place.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, section "Path Integral
  Quantization of Scalar Field Theory", from the field wave functional through
  the definitions of Wightman, time-ordered, and Euclidean Green functions.
- `references/253a_notes.tex`, corresponding section, used only as a
  comparison layer for figures and formulas.
- `monograph/tex/volumes/volume_i/chapter04_lagrangian_formalism_and_quantum_mechanical_path_integrals.tex`,
  for the finite-dimensional time-slicing construction.
- `monograph/tex/volumes/volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex`,
  for Euclidean correlation functions and Gaussian functional integrals.
- `monograph/tex/volumes/volume_i/chapter06_relativistic_scalar_fields_and_canonical_quantization.tex`,
  for the free scalar Hamiltonian and field normalization.

## External Reference Boundary

- Schmidt, "Euclidean Reconstruction in Quantum Field Theory", is kept as a
  theorem-boundary reference for the relation between Schwinger and Wightman
  functions. The chapter only states the elementary analytic-continuation
  construction and its assumptions.

## Framework

Working framework:

- real scalar field on \(\mathbb M^D\);
- \(\hbar=1\) unless displayed;
- finite spatial volume or spatial momentum cutoff whenever a functional
  integral is treated as an actual finite-dimensional integral;
- field eigenstates are distributional generalized vectors, used only as a
  regulated heuristic bridge to the path-integral kernel;
- Euclidean correlators are initially defined either by a regulated Euclidean
  functional expression or by analytic continuation of Wightman functions when
  the required analyticity is available.

## Notation Inventory

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(\Psi[\varphi]\) | generalized wave functional | state represented on a fixed-time field configuration |
| \(\ket{\varphi}\) | generalized vector | field-configuration eigenstate |
| \(U(t_f,t_i)\) | unitary operator | Hamiltonian time evolution |
| \(C\) | contour | complex-time contour for the Lorentzian action |
| \(x_E=(\tau,\vec x)\) | coordinate | Euclidean spacetime point |
| \(S_E[\phi]\) | functional | Euclidean action |
| \(G_E\) | distribution | Euclidean/Schwinger Green function |
| \(W\) | distribution | Wightman function |
| \(G_T\) | distribution | time-ordered Green function |
| \(\Delta_E\) | distribution | free Euclidean scalar propagator |
| \(\Delta_F\) | distribution | free Lorentzian Feynman propagator |
| \(\epsilon\) | positive regulator | pole-displacement parameter in the Feynman prescription |

## Definition Ledger

- regulated scalar-field path-integral kernel with fixed boundary field
  configurations;
- field wave functional and field-configuration generalized eigenstate;
- Euclidean scalar action and Euclidean correlation function;
- uniform Wick rotation preserving imaginary-time ordering;
- free Euclidean propagator as the inverse of \(-\partial_E^2+m^2\);
- Feynman \(i\epsilon\) prescription from momentum-contour rotation;
- Wightman, time-ordered, and Euclidean Green functions.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The field path-integral kernel is obtained as the regulated continuum limit of time-sliced quantum mechanics. | Construction | Spatial cutoff plus Chapter 4 time slicing |
| Euclidean ordering of insertion times gives analytic continuation to time-ordered Lorentzian correlators under spectral/analytic assumptions. | Framework statement with derivation in free case | Complex-time contour and uniform Wick rotation |
| The free Euclidean two-point function is the Green function of \(-\partial_E^2+m^2\). | Derived | Gaussian functional integral |
| Rotating the Euclidean momentum contour gives the Feynman denominator \(k^2+m^2-i\epsilon\). | Derived in free theory | Pole tracking |
| Wightman, time-ordered, and Euclidean Green functions are distinct distributions related by ordering and analytic continuation. | Definition plus framework statement | Explicit definitions |

## Figure Ledger

Figures to include:

- complex-time contour with insertion ordering;
- uniform Wick rotation from Euclidean insertions to ordered Lorentzian times;
- pole motion in the complex \(k^0\)-plane that records the \(i\epsilon\)
  prescription.

## Audit Targets

- Keep all path-integral formulas marked as regulated constructions or formal
  expressions until a regulator is specified.
- Do not say the Euclidean functional expression is positive in all theories.
- Do not introduce perturbative graph expansion in this chapter.
- Do not use scattering language.
- Preserve the transition into the Kallen-Lehmann chapter.
