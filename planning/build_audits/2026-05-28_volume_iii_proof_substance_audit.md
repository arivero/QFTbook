# 2026-05-28 Volume III Proof-Substance Audit

Scope: first substance-read pass through the proof environments in Volume III.
The pass inspected whether each proof actually derives its statement from the
stated hypotheses, rather than merely naming standard CFT lore.

## Standard Applied

- Kinematic conformal statements are retained as theorem/proposition material
  only when the proof constructs the relevant conformal frame, solves the
  weight equations, computes the contour residue, or gives the representation-
  theoretic Gram calculation.
- Conditional reconstruction and OPE convergence statements may remain theorem
  statements only when the hypotheses explicitly include the needed radial
  Hilbert-space, finite-multiplicity, associativity, tube-domain, and boundary-
  value data.
- Deep Lorentzian results not proved in the chapter are marked as quoted
  theorem inputs.
- Quotient and irreducibility claims are stated at the level actually proved:
  the radical quotient is proved, while irreducibility requires the additional
  maximal-submodule/no-further-invariant-subspace condition.

## Main Repairs

- Chapter 2: narrowed the universal-cover statement to the precise descent
  obstruction \(\exp(-2\pi iD_{\rm rad})=1\), replacing the generic-CFT phrase
  by the condition that a sector with nonintegral scaling dimension cannot
  descend to the \(SO(2)\) quotient.
- Chapter 2: narrowed the null-quotient proposition so the proof establishes a
  nondegenerate cyclic descendant quotient; irreducibility is now tied to the
  explicit absence of a further invariant orthogonal subspace.
- Chapter 3: demoted the four-dimensional \(TTT\)-to-anomaly map from a
  proposition to a remark, since the text records normalization data and Ward
  identity consequences rather than proving the full Osborn--Petkou/anomaly
  map.
- Chapter 6: narrowed the primary-multiplet proposition so quotienting by the
  radial radical is the proved construction, while irreducibility is stated
  only under the maximal-proper-submodule condition.
- Chapter 10: marked ANEC and the light-ray OPE as quoted theorem inputs.  The
  chapter proves the rotational tensor basis and conformal-collider
  inequalities, but it does not prove the deep Lorentzian analyticity theorem
  behind ANEC or the full light-ray OPE.

## Proofs Retained After Reading

- The conformal Killing vector classification, charge algebra, ambient
  conformal group, radial cylinder, parabolic stabilizer, and two-dimensional
  conformal Killing field proofs contain explicit differential-geometric or
  Lie-algebra calculations.
- The stress-tensor Weyl, improvement, conformal Laplacian, and Ward-identity
  proofs contain explicit metric/source variations and Weyl transformation
  calculations.
- The radial state--operator correspondence is conditional on the stated
  radial reconstruction data and proves the dense-local-operator version rather
  than the false assertion that every Hilbert-space state is a local operator.
- The Virasoro, Schwarzian, finite-primary, conformal-kinematics, OPE
  convergence, conformal-block, Mellin-pole, radial-block convergence, mixed
  Ising crossing, and finite-functional-certificate proofs contain the relevant
  contour, cocycle, frame, spectral, Gram-matrix, or linear-positivity
  derivations.

## Follow-Up

The quoted ANEC and light-ray OPE inputs are genuine proof obligations for a
future Lorentzian-CFT/light-ray appendix if the monograph aims to prove these
results internally rather than record them as external theorem boundaries.
