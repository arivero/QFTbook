# Volume III, Chapter 7 Dossier: Unitarity Bounds And Short Multiplets

## Logical Role

- Role in the monograph: derive CFT unitarity bounds from radial Hilbert-space
  positivity, the adjointness \(P_\mu^\dagger=K_\mu\), and conformal
  representation theory.
- Immediate predecessor: primary operators and finite conformal
  transformations.
- Immediate successor: correlation functions and conformal frames.

## Definitions And Results

The chapter establishes:

- the radial Hilbert-space domain on which finite descendant Gram matrices are
  formed;
- the null-state quotient and its interpretation as operator equations;
- the level-one Gram form
  \(\langle\mathcal O|K_\mu P_\nu|\mathcal O\rangle\), recorded as a
  calculation rather than a theorem-family wrapper because it is the norm
  identity plus the conformal commutator;
- the relation between finite descendant Gram matrices and the Shapovalov form
  on conformal generalized Verma modules, with the finite conformal-algebra
  Kac determinant locating singular vectors;
- the scalar level-two trace descendant and the scalar unitarity bound;
- the labeled spinor unitarity-bound theorem and gamma-trace Dirac
  shortening;
- the \(\Delta=0\) scalar branch, tied explicitly to the unique-vacuum and
  cluster-decomposition assumptions in the radial reconstruction hypothesis;
- the \(SO(D)\) decomposition
  \(\mathcal H_1\otimes\mathcal H_\ell
    =\mathcal H_{\ell+1}\oplus\mathcal H_{\ell,1}\oplus
     \mathcal H_{\ell-1}\);
- the first-level Casimir computation of the spin-\(\ell\) eigenvalues;
- the general first-level test for arbitrary irreducible \(SO(D)\)
  representations;
- the worked two-row mixed-symmetry tensor computation for
  \(\mathcal H_{a,b}\), including the vector-tensor decomposition, Casimir
  table, non-rectangular bound \(\Delta\ge a+D-2\), rectangular bound
  \(\Delta\ge a+D-3\), and the corresponding projected-divergence shortening
  equations;
- conservation and free-field equations as null-state equations in the
  quotient local-operator space.
- the scalar Laplace shortening as the representation-theoretic source of the
  \(1-q^2\) subtraction in the free-scalar single-letter character of
  Chapter 4.
- A collected reference list for the scalar, spinor, and symmetric-traceless
  bounds and their saturation equations, pointing to the individual
  Gram-matrix derivations rather than wrapping them in a duplicate theorem.
- Section `sec:short-multiplets-operator-equations`, which records that
  saturated bounds become null-descendant operator equations in the quotient
  local-operator space.

## Claims To Verify

1. Positivity of finite descendant Gram matrices is inherited from radial
   reflection positivity.
2. The adjointness \(P_\mu^\dagger=K_\mu\) converts descendant norms into
   conformal-algebra matrix elements.
3. Scalar non-identity primaries obey
   \(\Delta\ge(D-2)/2\), with saturation giving
   \(\partial^2\phi=0\).
4. Symmetric traceless spin-\(\ell\ge1\) primaries obey
   \(\Delta\ge\ell+D-2\), with saturation giving the divergence shortening.
5. General first-level bounds are computed by
   \(\Delta+\frac12(C_Q-C_1-C_\rho)\ge0\) for
   \(Q\subset\mathcal H_1\otimes\rho\).
6. For two-row traceless tensor representations \(\mathcal H_{a,b}\), the
   displayed Casimir table gives the correct first-level lower bound and
   identifies the projected null descendant at saturation.
7. The Kac-determinant framework may be named, but each bound used in the
   chapter must still be derived from a displayed finite Gram matrix.

## Figures

- No figure is required; the chapter is algebraic.  Future diagrams should be
  reserved for representation decompositions only if they clarify notation.

## Checks

- Keep all bounds tied to a positive radial Hilbert space and a specified
  null quotient.
- Avoid treating conservation as an assumption at saturation; it is the
  resulting null-state operator equation.
- 2026-05-23 Casimir pass: added the Hilbert-space convention for descendant
  Gram matrices, derived the symmetric-traceless level-one eigenvalues from
  \(SO(D)\) Casimirs, and added the general first-level irreducible
  representation test.
- 2026-05-24 issue #270 pass: the \(\Delta=0\) scalar discussion now points
  back to Hypothesis `hyp:radial-reconstruction-data` for unique vacuum and
  cluster decomposition, avoiding an unstated identity-branch assumption.
- 2026-05-24 issue #285 pass: connected the descendant Gram forms to the
  Shapovalov form on conformal generalized Verma modules and named the finite
  conformal-algebra Kac determinant framework while retaining explicit
  Gram-matrix derivations.
- 2026-05-24 issue #286 pass: promoted the spinor result to a theorem and
  added the labeled basic unitarity-bounds/short-multiplets theorem collecting
  scalar Laplace, spinor Dirac, and symmetric-traceless divergence
  shortenings.
- 2026-05-24 issue #287 pass: added the two-row mixed-symmetry tensor
  first-level computation, including all vector-tensor channels in the stable
  range and the separate rectangular/non-rectangular shortening equations.
- 2026-05-24 issue #294 pass: recorded that the scalar Laplace null descendant
  at the unitarity bound is the null submodule subtracted in the free-scalar
  single-letter character of Chapter 4.
- 2026-05-24 issue #410 pass: cross-referenced the explicit
  Lorentzian-to-radial generator map in Chapter 4 and stated that the
  positive sign in the radial \([K_\mu,P_\nu]\) commutator is not obtained by
  a naive deletion of Lorentzian factors of \(\ii\).
- 2026-05-24 issue #417 pass: cross-referenced the Chapter 4 BPZ
  Hilbert-space derivation of \(P_\mu^\dagger=K_\mu\), so level-one descendant
  positivity rests on the reflection-positive radial completion rather than on
  an unexplained inversion slogan.
- 2026-05-24 issue #422 pass: labeled the short-multiplet operator-equation
  discussion so the conformal-block construction can reference the precise
  source of the null descendants that must be subtracted level-by-level.
