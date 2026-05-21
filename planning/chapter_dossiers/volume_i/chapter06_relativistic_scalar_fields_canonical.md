# Volume I, Chapter 6 Dossier: Relativistic Scalar Fields and Canonical Quantization

## Status

Current status: ready for TeX rewrite.

## Logical Role

This chapter is the transition from quantum-mechanical path integrals for a
finite number of coordinates to relativistic fields as infinitely many coupled
canonical degrees of freedom. It introduces the classical scalar field action,
the free massive scalar equation, the canonical Hamiltonian formalism, and the
free quantum scalar field obtained by diagonalizing the Hamiltonian.

It remains before the Noether-current chapter and before the scalar field path
integral chapter.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, section "A Manifestly
  Relativistic Theory of Fields", through the free scalar canonical
  quantization and Hamiltonian diagonalization.
- `monograph/tex/volumes/volume_i/chapter02_quantum_mechanics_relativity_and_locality.tex`,
  for already established Poincare and free Fock-space conventions that must
  remain consistent.
- `references/253a_notes.tex`, the corresponding scalar-field and
  microcausality sections, used only as a comparison layer.

## Framework

Working framework:

- \(D\)-dimensional Minkowski spacetime \(\mathbb M^D\);
- mostly-plus metric \(\eta=\operatorname{diag}(-1,+1,\ldots,+1)\);
- coordinates \(x^\mu=(x^0,\vec x)\) with \(x^0=t\);
- real scalar field \(\phi:\mathbb M^D\to\mathbb R\) classically;
- Lagrangian density depending on \(\phi\) and \(\partial_\mu\phi\);
- canonical field coordinate \(\phi(t,\vec x)\) and conjugate momentum
  \(\Pi(t,\vec x)\);
- quantum fields as operator-valued distributions on a dense finite-particle
  domain.

## Notation Inventory

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(D\) | integer | spacetime dimension |
| \(d=D-1\) | integer | spatial dimension |
| \(x^\mu=(t,\vec x)\) | coordinate | spacetime point |
| \(\eta_{\mu\nu}\) | bilinear form | mostly-plus Minkowski metric |
| \(\mathcal L\) | scalar density | Lagrangian density |
| \(S[\phi]\) | functional | classical action |
| \(\Pi(t,\vec x)\) | field density | canonical momentum conjugate to \(\phi(t,\vec x)\) |
| \(\mathcal H\) | density | Hamiltonian density |
| \(\omega_{\vec k}\) | positive function | \(\sqrt{\vec k^2+m^2}\) |
| \(b_{\vec k},b^\dagger_{\vec k}\) | operator-valued distributions | canonical-normalized annihilation and creation operators |
| \(a(\vec k),a^\dagger(\vec k)\) | operator-valued distributions | invariant-measure normalization used earlier |
| \(\Delta(x)\) | distribution | Pauli--Jordan commutator distribution |
| \(\mathcal D_0\) | dense domain | finite-particle vectors |

## Definition Ledger

- classical real scalar field;
- Euler-Lagrange derivative for first-derivative Lagrangian densities;
- free massive scalar Lagrangian and Klein-Gordon equation;
- Cauchy data for the free scalar field;
- canonical momentum and Hamiltonian density;
- equal-time Poisson brackets and equal-time commutation relations;
- canonical oscillator normalization and invariant mass-shell normalization;
- finite-regulator vacuum-energy shift;
- free scalar operator-valued distribution and smeared field;
- Pauli-Jordan commutator distribution and microcausality.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The free scalar Euler-Lagrange equation is \((\partial^\mu\partial_\mu-m^2)\phi=0\). | Derived | Variation of the action |
| Classical free solutions are supported on the mass shell \(k^2+m^2=0\). | Derived | Fourier transform of Klein-Gordon equation |
| Cauchy data \(\phi(0,\vec x)\), \(\partial_t\phi(0,\vec x)\) determine the free solution. | Derived | Positive/negative frequency decomposition |
| Equal-time CCR determine the oscillator algebra once a mode normalization is fixed. | Derived | Fourier inversion |
| The free Hamiltonian selects \(\omega_{\vec k}=\sqrt{\vec k^2+m^2}\) as the diagonal oscillator frequency. | Derived | Substitution into \(H_0\) |
| The free scalar field is an operator-valued distribution on finite-particle vectors. | Construction | Fock-space formula |
| The Pauli-Jordan distribution vanishes at spacelike separation. | Derived | Lorentz invariance and equal-time reduction |

## Figure Ledger

Included figure:

- mass shell \(k^2+m^2=0\) with positive and negative energy branches, used to
  explain the support of classical Fourier modes.

## Audit Targets

- Maintain the already established mostly-plus convention.
- State all normalizations of creation and annihilation operators explicitly.
- Avoid letting the word "particle" carry unexplained content; identify the
  one-particle interpretation through the diagonalized Fock representation.
- Present normal ordering/vacuum-energy subtraction as a regulated scalar
  energy shift, not as an informal deletion.
