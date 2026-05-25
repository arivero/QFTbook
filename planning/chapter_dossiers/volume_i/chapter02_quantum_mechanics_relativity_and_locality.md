# Volume I, Chapter 2 Dossier: Relativistic Quantum Mechanics And Local Operator Structure

## Status

Current status: certified against handwritten 253a pp. 3--9 in the
2026-05-22 source pass, with rendered checks of the new causal figure and
free-field normalization/covariance material.

## Logical Role

The chapter constructs and separates:

1. Hilbert-space quantum mechanics;
2. rigged Hilbert spaces for generalized eigenvectors and continuous spectra;
3. unitary Poincare representations and one-particle state spaces;
4. free Fock representations;
5. local observable assignments;
6. the free scalar local field as an explicit example.

The chapter should not use a negative framing. It should define each object and
state the relation among them.

## Frameworks

- Hilbert-space quantum mechanics with bounded and unbounded observables.
- Gelfand triples \(\Phi\subset\Hilb\subset\Phi^\times\), direct integrals,
  and weak distributional identities for plane-wave kernels.
- Strongly continuous unitary representation of the connected Poincare group
  or its double cover.
- Wigner one-particle representation for the massive spinless example.
- Bosonic or fermionic Fock-space construction.
- Local observable assignment on Minkowski space.
- Free scalar operator-valued distribution.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`: relativistic particles, local field
  operators, Poincare covariance, and microcausality.
- `references/253a lectures 2022.pdf`, pp. 3--9: free relativistic particles,
  creation/annihilation normalization, interaction Hamiltonian question,
  causal light-cone figure, Poincare covariance, and free-field
  microcausality.

## External Reference Needs

- Wigner classification of Poincare representations.
- Pauli--Jordan commutator support.
- Wightman free scalar field construction.

## Notation Inventory

| Symbol | Type | Framework |
| --- | --- | --- |
| \(\rho\) | positive trace-class operator with trace one | quantum state |
| \(A\) | bounded observable or specified unbounded operator | quantum mechanics |
| \(H\) | self-adjoint Hamiltonian | time evolution |
| \(\Phi\subset\Hilb\subset\Phi^\times\) | rigged Hilbert space/Gelfand triple | generalized eigenvectors |
| \(E_A\) | projection-valued spectral measure of a self-adjoint operator \(A\) | continuous spectrum |
| \(\ket{p,\sigma}\) | distributional one-particle momentum ket in \(\Phi_1^\times\) | mass-shell kernel |
| \(SO^+(1,D-1)\) | connected Lorentz group | spacetime symmetry |
| \(U(a,\Lambda)\) | strongly continuous unitary representation | Poincare symmetry |
| \(P^\mu,J^{\mu\nu}\) | self-adjoint generators on common invariant domains, with \(P_\mu=\eta_{\mu\nu}P^\nu\) in the translation exponent | Lie algebra |
| \(\Hilb_1\) | one-particle Hilbert space | Wigner representation |
| \(E_{\vec p}\) | positive energy \((\vec p^{\,2}+m^2)^{1/2}\) | mass shell |
| \(a(\vec p),a^\dagger(\vec p)\) | operator-valued distributions in momentum | free Fock space |
| \(\mathfrak a_{\vec p},\mathfrak a_{\vec p}^\dagger\) | noncovariantly normalized creation/annihilation kernels | source normalization |
| \(K_{r,s}\) | interaction kernels in formal normally ordered Hamiltonian terms | interaction bookkeeping |
| \(\widehat\phi(f)\) | smeared free scalar field | local field |
| \(\Delta\) | Pauli--Jordan distribution | commutator support |

## Definition Ledger

- Pure and mixed states.
- Rigged Hilbert space/Gelfand triple.
- Hilbert-space eigenvalue versus generalized eigenvector in continuous
  spectrum.
- Direct-integral spectral representation and delta-normalized kernels.
- Strongly continuous unitary Poincare representation.
- Poincare group law and its unitary implementation.
- Spectrum condition.
- Massive spinless one-particle Hilbert space.
- Bosonic and fermionic Fock spaces.
- Bosonic decomposable tensor convention
  \(\psi_1\odot\cdots\odot\psi_n=\sqrt{n!}\Pi_{s,n}
  (\psi_1\otimes\cdots\otimes\psi_n)\), with the corresponding permutation-sum
  inner product.
- Covariant and noncovariant momentum-space creation/annihilation
  normalizations.
- Formal interacting Hamiltonian as kernels added to the free Fock
  Hamiltonian, with locality and the Poincare algebra as additional required
  data.
- Local observable assignment.
- Free scalar smeared field.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| Plane-wave kets and sharp energy/momentum eigenstates in continuous spectra are distributional vectors in \(\Phi^\times\), not normalizable Hilbert vectors. | Definition/construction | Established from rigged Hilbert space and spectral-measure definitions |
| Delta-normalization is the weak kernel of the identity relative to a chosen spectral or mass-shell measure. | Definition/construction | Established by the Gelfand triple/direct-integral discussion |
| Massive spinless one-particle states are realized as \(L^2\) functions on the positive mass shell with invariant measure. | Construction | Derived from representation choice; external Wigner reference needed |
| Fock space is constructed from one-particle Hilbert space by symmetric or antisymmetric tensor powers. | Definition/construction | Defined in chapter |
| The bosonic symbol \(\odot\) denotes the creation-operator normalization \(\sqrt{n!}\Pi_{s,n}(\otimes_j\psi_j)\), so decomposable symmetric tensors have the permutation-sum inner product. | Convention | Added to make the Haag--Ruelle Fock inner product normalization explicit |
| The noncovariant creation/annihilation normalization with \(\delta^{D-1}(\vec p-\vec q)\) is equivalent to the covariant mass-shell normalization. | Calculation/convention | Added from handwritten pp. 3--4 and checked in the chapter |
| A formal \(H_0+H_{\mathrm{int}}\) written in Fock kernels is part of the interaction data only together with Poincare generators and locality. | Framework statement | Added from handwritten pp. 4--5 with positive formulation |
| Local observable assignments are additional local data. | Framework statement | Definition of local QFT data |
| The free scalar field is Poincare covariant and its commutator vanishes at spacelike separation. | Proposition | Computed in chapter from the second-quantized one-particle representation, invariant mass-shell measure, and odd-integrand spacelike frame argument |

## Required Revisions

- Completed: typed all operators and domains more carefully.
- Completed: stated that \(a(\vec p)\) and \(a^\dagger(\vec p)\) are distributional
  annihilation and creation operators.
- Completed: propagated the source normalization through sharp momentum kets,
  \(H_0\), and \(\vec P_0\).
- Propagate the rigged-Hilbert-space convention to later chapters that use
  sharp-momentum kernels.
- Ensure the local algebra language is consistent with Chapter 1.
- Completed: replaced the conclusion with a positive summary of constructed
  structures.
- 2026-05-24 issue #368 pass: declared the \(\odot\) normalization for bosonic
  decomposable Fock tensors and displayed the corresponding inner product.
- 2026-05-24 issue #424 pass: aligned the infinitesimal Poincare expansion
  with the opening translation convention
  \(U(a)=\exp(i a_\mu P^\mu)=\exp(i a^\mu P_\mu)\), keeping the spectrum
  condition on contravariant \(P^\mu\).

## Figure Ledger

- `fig:translation-spectrum-mass-shell`: spectrum and isolated particle shell.
- `fig:causal-lightcone-local-operation`: source light-cone/causality figure,
  redrawn as a TikZ causal localization diagram.  Rendered on
  `/tmp/qft_253a_003_009_cert2-049.png` after label adjustment.
