# Volume I, Chapter 2 Dossier: Relativistic Quantum Mechanics And Local Operator Structure
Source-File: monograph/tex/volumes/volume_i/chapter02_quantum_mechanics_relativity_and_locality.tex

## Status

Current status: certified against handwritten 253a pp. 3--9 in the
2026-05-22 source pass, with rendered checks of the new causal figure and
free-field normalization/covariance material.  Formalization upgraded on
2026-05-27 for issue #615.  The 2026-05-29 anti-wrapper pass retained the
joint translation spectrum and free-scalar microcausality as structural
propositions, strengthened their proof text, and demoted the bosonic Fock
inner-product permutation algebra to a worked normalization formula.

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
- Wigner one-particle representations: massive spin tower, massless helicity,
  continuous-spin, and spacelike/tachyonic orbit classes in four dimensions,
  with the massive spinless example used as the first explicit construction.
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
| \(\Phi\subset\Hilb\subset\Phi^\times\) | Gelfand triple | generalized eigenvectors |
| \(E_A\) | spectral measure of self-adjoint \(A\) | continuous spectrum |
| \(\ket{p,\sigma}\) | distributional one-particle momentum ket | mass-shell kernel |
| \(SO^+(1,D-1)\) | connected Lorentz group | spacetime symmetry |
| \(U(a,\Lambda)\) | strongly continuous unitary representation | Poincare symmetry |
| \(P^\mu,J^{\mu\nu}\) | energy-momentum and Lorentz generators | Lie algebra |
| \(\Hilb_1\) | one-particle Hilbert space | Wigner representation |
| \(E_{\vec p}\) | positive energy \((\vec p^{\,2}+m^2)^{1/2}\) | mass shell |
| \(a(\vec p),a^\dagger(\vec p)\) | operator-valued distributions in momentum | free Fock space |
| \(\mathfrak a_{\vec p}^{(\dagger)}\) | noncovariant kernels | source normalization |
| \(K_{r,s}\) | normally ordered interaction kernels | interaction bookkeeping |
| \(\widehat\phi(f)\) | smeared free scalar field | local field |
| \(\Delta\) | Pauli--Jordan distribution | commutator support |

## Definition Ledger

- `def:hilbert-space-quantum-datum`: pure and mixed states, bounded
  expectations, and domain data for unbounded operators.
- `def:hamiltonian-time-evolution`: self-adjoint Hamiltonian and strongly
  continuous unitary time evolution.
- `def:rigged-hilbert-space`: Gelfand triple
  \(\Phi\subset\Hilb\subset\Phi^\times\).
- `def:generalized-eigenvector-rigged-hilbert`: Hilbert-space eigenvalue
  versus generalized eigenvector in continuous spectrum.
- `def:direct-integral-coordinate-ket`: direct-integral spectral
  representation and delta-normalized kernels.
- `def:relativistic-one-particle-rigging`: covariant mass-shell rigging for
  sharp one-particle momentum labels.
- `def:poincare-covariant-vacuum-hilbert-datum`: strongly continuous unitary
  Poincare representation, infinitesimal generators, spectrum condition, and
  invariant vacuum.
- Poincare group law and its unitary implementation.
- `def:invariant-mass-spectral-measure`: invariant mass operator and mass
  spectral projections.
- `def:mass-sector-and-particle-shell`: mass sector and isolated particle
  shell.
- `def:massive-scalar-wigner-one-particle-space`: massive spinless
  one-particle Hilbert space.
- `def:four-dimensional-wigner-orbit-datum`: induced-representation orbit
  datum for the four-dimensional Wigner classification.
- Four-dimensional Wigner orbit classification table for the universal cover
  of the connected Poincare group.
- `def:free-bosonic-fermionic-fock-spaces`: bosonic and fermionic Fock spaces.
- `def:bosonic-creation-operator-tensor-normalization`: bosonic decomposable
  tensor convention
  \(\psi_1\odot\cdots\odot\psi_n=\sqrt{n!}\Pi_{s,n}
  (\psi_1\otimes\cdots\otimes\psi_n)\).
- `def:mass-shell-fock-test-domain-kernels`: covariant momentum-space
  creation/annihilation normalizations and common Fock test domain.
- `def:noncovariant-creation-momentum-ket-normalization`: noncovariant
  creation/annihilation and sharp-momentum ket normalization.
- `def:free-multi-species-fock-representation`: multi-species bosonic and
  fermionic free Fock representation with graded tensor convention.
- Formal interacting Hamiltonian as kernels added to the free Fock
  Hamiltonian, with locality and the Poincare algebra as additional required
  data.
- `def:local-observable-assignment-chapter-two`: local observable assignment.
- `def:free-scalar-field-mass-shell-kernels`: free scalar smeared field.

## Claim Ledger

- Plane-wave kets and sharp energy/momentum eigenstates in continuous spectra
  are distributional vectors in \(\Phi^\times\), not normalizable Hilbert
  vectors.
- Delta-normalization is the weak kernel of the identity relative to a chosen
  spectral or mass-shell measure.
- `prop:schwartz-triple-weak-delta-kernels` proves the Schwartz-triple
  identities for \(\ket{x}\), \(\ket{p}\), and weak resolutions of identity by
  pairing against test functions.
- `prop:joint-translation-spectrum` constructs the single joint spectral
  measure of the translation generators from Stone--Naimark, including the
  distinction between strong commutativity and formal commutation on a common
  domain.
- The Poincare commutator sign
  \([P^\mu,J^{\rho\sigma}]
  =-\ii(\eta^{\mu\rho}P^\sigma-\eta^{\mu\sigma}P^\rho)\) is the
  Hermitian Lorentzian convention whose reversed bracket embeds into the
  Lorentzian conformal charge algebra; it is cross-referenced to the
  conformal Killing vector convention and checked by
  `calculation-checks/poincare_algebra_sign_checks.py` together with
  `calculation-checks/conformal_algebra_sign_checks.py`.
- An isolated mass shell gives a closed invariant one-particle
  subrepresentation by spectral projection and covariance; this is kept as
  prose because the substantive input is the isolation hypothesis.
- Massive spinless one-particle states are realized as \(L^2\) functions on the
  positive mass shell with invariant measure.
- Table `tab:wigner-classification-four-dimensional` separates the vacuum,
  massive, massless finite-helicity, continuous-spin, and tachyonic orbit
  classes.
- Fock space is constructed from one-particle Hilbert space by symmetric or
  antisymmetric tensor powers.
- The bosonic symbol \(\odot\) denotes the creation-operator normalization
  \(\sqrt{n!}\Pi_{s,n}(\otimes_j\psi_j)\).
- Equation `eq:bosonic-fock-odot-inner-product` records the corresponding
  permutation-sum inner product as worked normalization algebra; it is also
  checked by `calculation-checks/haag_ruelle_fock_inner_product_checks.py`.
- The noncovariant creation/annihilation normalization with
  \(\delta^{D-1}(\vec p-\vec q)\) is equivalent to the covariant mass-shell
  normalization.
- A formal \(H_0+H_{\mathrm{int}}\) in Fock kernels is interaction data only
  together with Poincare generators and locality.
- Local observable assignments are additional local data.
- The free scalar covariance calculation is prose because it is the
  second-quantized one-particle covariance check, not a theorem-level
  interacting-field result.  `prop:free-scalar-microcausality-chapter-two`
  labels the locality calculation for later citation and now makes the
  smeared-distribution support argument explicit.

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
- 2026-05-25 issue #448 pass: added the complete four-dimensional Wigner
  classification table, including the higher-spin massive tower,
  massless continuous-spin representations, and spacelike/tachyonic orbits.
- 2026-05-27 issue #615 pass: upgraded the chapter from prose-dominant
  exposition to a labeled foundation: Hilbert data, rigged Hilbert triples,
  joint translation spectrum, invariant mass projections, isolated shells,
  Wigner one-particle spaces, Fock construction, local observable assignment,
  and free scalar covariance/microcausality now have formal environments with
  proofs where the chapter uses a nontrivial construction.
- 2026-06-02 conformal-algebra sign audit: added a manuscript cross-reference
  tying the corrected Poincare \([P,J]\) sign to the Hermitian Lorentzian
  conformal charge convention
  \([Q_X,Q_Y]=-\ii Q_{[X,Y]}\) and to the later radial real-form map.

## Figure Ledger

- `fig:translation-spectrum-mass-shell`: spectrum and isolated particle shell.
- `fig:causal-lightcone-local-operation`: source light-cone/causality figure,
  redrawn as a TikZ causal localization diagram.  Rendered on
  `/tmp/qft_253a_003_009_cert2-049.png` after label adjustment.
