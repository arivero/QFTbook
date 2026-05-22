# Volume I, Chapter 2 Dossier: Relativistic Quantum Mechanics And Local Operator Structure

## Status

Current status: rewritten once, now requires re-audit under symbol and
definition integrity rules.

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
- handwritten source PDF for sign and normalization checks.

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
| \(P_\mu,J^{\mu\nu}\) | self-adjoint generators on common invariant domains | Lie algebra |
| \(\Hilb_1\) | one-particle Hilbert space | Wigner representation |
| \(E_{\vec p}\) | positive energy \((\vec p^{\,2}+m^2)^{1/2}\) | mass shell |
| \(a(\vec p),a^\dagger(\vec p)\) | operator-valued distributions in momentum | free Fock space |
| \(\widehat\phi(f)\) | smeared free scalar field | local field |
| \(\Delta\) | Pauli--Jordan distribution | commutator support |

## Definition Ledger

- Pure and mixed states.
- Rigged Hilbert space/Gelfand triple.
- Hilbert-space eigenvalue versus generalized eigenvector in continuous
  spectrum.
- Direct-integral spectral representation and delta-normalized kernels.
- Strongly continuous unitary Poincare representation.
- Spectrum condition.
- Massive spinless one-particle Hilbert space.
- Bosonic and fermionic Fock spaces.
- Local observable assignment.
- Free scalar smeared field.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| Plane-wave kets and sharp energy/momentum eigenstates in continuous spectra are distributional vectors in \(\Phi^\times\), not normalizable Hilbert vectors. | Definition/construction | Established from rigged Hilbert space and spectral-measure definitions |
| Delta-normalization is the weak kernel of the identity relative to a chosen spectral or mass-shell measure. | Definition/construction | Established by the Gelfand triple/direct-integral discussion |
| Massive spinless one-particle states are realized as \(L^2\) functions on the positive mass shell with invariant measure. | Construction | Derived from representation choice; external Wigner reference needed |
| Fock space is constructed from one-particle Hilbert space by symmetric or antisymmetric tensor powers. | Definition/construction | Defined in chapter |
| Local observable assignments are additional local data. | Framework statement | Definition of local QFT data |
| The free scalar commutator vanishes at spacelike separation. | Proposition | Computed in chapter; support theorem reference desirable |

## Required Revisions

- Type all operators and domains more carefully.
- State that \(a(\vec p)\) and \(a^\dagger(\vec p)\) are distributional
  annihilation and creation operators.
- Propagate the rigged-Hilbert-space convention to later chapters that use
  sharp-momentum kernels.
- Ensure the local algebra language is consistent with Chapter 1.
- Replace the conclusion with a positive summary of constructed structures.

## Figure Ledger

No required figure in the current chapter.
