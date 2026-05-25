# Volume V, Chapter 11 Dossier: Two-Dimensional Sigma Models, Orbifolds, and Twist Fields

## Logical Role

- Place nonlinear sigma-model CFTs, finite orbifolds, twisted sectors, and
  twist-field deformations inside the CFT volume rather than treating them as
  string-theory side material.
- Immediate predecessors: Virasoro/stress-tensor Ward identities, radial
  state--operator construction, conformal perturbation theory, and OPE
  convergence.
- Later successors: full two-dimensional CFT development, supersymmetric
  models, symmetric products, defects, boundary CFT, and gauge/string
  large-\(N\) applications.

## Definitions And Results

- Defines bosonic sigma-model data as maps \(X:\Sigma\to M\), target metric,
  gerbe \(B\)-field, and dilaton coupling.
- Defines a conformal sigma-model point by the continuum QFT and its
  Weyl-anomaly coefficients modulo target diffeomorphism and \(B\)-field
  gauge redundancy.
- Derives the one-loop Ricci divergence in background-field dimensional
  regularization.
- Records the one-loop \(G\) and \(B\) hatted Weyl-anomaly coefficients with
  \(H\)-flux and dilaton terms.
- Defines finite orbifolds using anomaly-free topological symmetry lines,
  twisted Hilbert spaces, centralizer projection, and discrete torsion.
- Derives the finite-orbifold torus partition function and its modular label
  transformations.
- Defines twist fields as endpoints of monodromy lines and derives cyclic
  permutation twist weights by the Schwarzian covering map.
- Records complex-boson rotation twist weights and the real
  \(\mathbb Z_2\) value \(h=\bar h=1/16\).
- Defines twist-field deformations as regulated integrated local-operator
  perturbations with OPE/contact-term beta functions.

## Claims To Verify

1. The sigma-model action is stated as a regularized representative; the
   intrinsic \(B\)-field datum is a gerbe connection.
2. The one-loop metric divergence follows from the covariant background-field
   quadratic action and the coincident heat-kernel pole.
3. The hatted beta tensors are defined modulo target diffeomorphism and
   \(B\)-field gauge directions.
4. The orbifold Hilbert space is
   \(\bigoplus_{[g]}\mathcal H_g^{C_g}\) after an \(H^3(G,U(1))\) anomaly
   trivialization is chosen.
5. The torus partition function is the finite gauge sum over commuting
   holonomies and is modular invariant with the stated label action.
6. The cyclic twist weight equals \(c_0(K-K^{-1})/24\), and the real
   reflection twist field has \(h=1/16\).
7. Twist-field deformations are conformal perturbations by projected local
   fields; exact marginality requires the full beta-function/contact-term
   analysis.

## Figures

- No figure is required for the first pass.
- Future figures should draw defect-line endpoints, torus holonomies
  \((g,h)\), and the \(K\)-sheeted cover \(z=t^K\) used in the twist-weight
  derivation.

## Checks

- `calculation-checks/orbifold_twist_weight_checks.py` verifies the finite
  rational arithmetic of the cyclic permutation and rotation twist weights.
- Later calculation checks should cover covering-space twist correlators and
  symmetric-product joining/splitting selection rules.
