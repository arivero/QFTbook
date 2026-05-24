# Volume III, Chapter 4 Dossier: Radial Quantization And State--Operator Correspondence

## Logical Role

- Role in the monograph: construct the radial Hilbert space from Euclidean
  reflection positivity and identify local insertions at the origin with
  finite-energy cylinder states.
- Immediate predecessor: stress tensor, Weyl structure, and improvement.
- Immediate successor: conformal charges and Ward identities.

## Definitions And Results

The chapter establishes:

- the radial reflection map \(x\mapsto x/|x|^2\) and the associated
  anti-linear operation on smeared insertions;
- the positive semidefinite radial inner product, null quotient, and Hilbert
  completion;
- the Weyl map \(\mathbb R^D\setminus\{0\}\simeq\mathbb R_\tau\times S^{D-1}\);
- the local orthonormal-frame rotation for spinning operators under the Weyl
  map, including the vector-primary construction
  \(\widetilde V_{\hat a}=\ee^{\Delta\tau}R_{\hat a}{}^\mu V_\mu\);
- the cylinder Hamiltonian \(\widehat D_{\rm rad}\) and its relation to
  scaling dimensions;
- the explicit bridge between Hermitian Lorentzian generators and radial
  Euclidean generators;
- the cylinder sewing identity on ordered constant-\(\tau\) slabs and its
  Heisenberg-operator form;
- the assumptions needed for discreteness, finite multiplicity, unique
  conformal vacuum, cluster factorization, tube-domain continuation, and radial
  local completeness;
- Theorem `thm:state-operator-correspondence`, which states that origin
  insertion gives an isometric linear isomorphism
  \(\mathcal V_{\rm loc}\simeq\mathcal H_{\rm fin}\), and after Hilbert
  completion an isomorphism onto \(\mathcal H_{S^{D-1}}\).

## Claims To Verify

1. Radial quantization is a Hilbert-space construction only after radial
   reflection positivity and null quotient have been specified.
2. The state--operator map is a theorem under reconstruction assumptions,
   including radial local completeness, not a notation convention.
3. Euclidean time \(\tau_E\) from Wick rotation is distinct from cylinder time
   \(\tau=\log r\).
4. \(\widehat D_{\rm rad}\) is the positive Euclidean cylinder Hamiltonian;
   Hermitian Lorentzian commutators differ by the stated analytic continuation.
5. The state--operator correlation formula follows from explicit cylinder
   sewing: insert constant-\(\tau\) cuts, compose the positive-time semigroup
   through ordered slabs, project the outgoing boundary to the vacuum, and
   apply the Weyl map to the punctured flat-space correlator.
6. Spinning operators require a local frame on \(S^{D-1}\).  The manuscript
   must keep the patchwise \(SO(D)\) rotation \(R^{\hat a}{}_\mu(n)\) separate
   from the Weyl scale and must state the transition-function dependence on
   overlaps.
7. Cluster decomposition is part of the consolidated radial reconstruction
   hypothesis, with the large-translation factorization limit displayed
   explicitly.

## Figures

- Keep figures that fix the Weyl map, radial reflection, and contour
  convention.
- Any angular coordinate should be denoted by \(n\) or a decorated unit vector
  when the vacuum \(\vac\) is nearby.

## Checks

- State all reconstruction assumptions in labeled form.
- Do not identify cylinder Hilbert-space statements with flat-space
  distributions without the radial reflection-positivity bridge.
- The proof of the state--operator theorem must retain the slab-sewing
  construction; the correlation formula is not to be treated as a formal
  consequence of a drawing of the cylinder.
- 2026-05-24 issue #268 pass: removed the conditional surjectivity clause from
  the theorem by moving radial local completeness into the labeled hypothesis
  block.  The theorem now states the isometric isomorphism directly and proves
  extension to the full radial Hilbert space by density of finite-energy
  spectral projections.
- 2026-05-24 issue #269 pass: added the patchwise cylinder coframe
  \(\widehat e^{\hat a}{}_\mu\), the rotation \(R^{\hat a}{}_\mu\), the vector
  primary cylinder map, and the corresponding spin-one state map.
- 2026-05-24 issue #270 pass: expanded the hypothesis block to state unique
  conformal vacuum and the explicit cluster-factorization limit for separated
  Euclidean local correlators.
