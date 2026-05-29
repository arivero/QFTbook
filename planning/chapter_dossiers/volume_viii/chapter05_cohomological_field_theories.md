# Volume VIII, Chapter 5 Dossier: Cohomological Field Theories

## Logical Role

- Role in the monograph: define cohomological QFT at regulator level and
  prove the finite-dimensional Ward, localization, descent, and
  Mathai-Quillen mechanisms that later gauge-theory and sigma-model examples
  use.
- Immediate predecessor: Chern--Simons theory.
- Immediate successor: topological sigma models and twists of supersymmetric
  theories.

## Definitions And Results

- Regulated cohomological QFT datum:
  `A_Lambda`, `Q_Lambda`, action/state, integration cycle, closure
  `Q_Lambda^2=B_Lambda`, invariant subalgebra, and Ward identity.
- Local anomaly and boundary-term decomposition of a failed Ward identity.
- Theorem: cohomological metric independence from a full renormalized
  metric-response insertion that is \(Q\)-exact.
- Proposition: \(Q\)-exact deformation independence for normalized
  expectation values.
- Theorem: compact nondegenerate finite-dimensional localization, with
  inverse equivariant Euler factor from the normal quadratic complex.
- Mathai-Quillen finite-dimensional model with auxiliary field, oscillatory
  Gaussian sign, Thom form, Euler class, and zero-locus localization.
- Descent package:
  \(Q\mathcal O^{(0)}=0\),
  \(Q\mathcal O^{(p)}+\mathrm d\mathcal O^{(p-1)}=0\), integrated
  descendants over cycles, and homology dependence up to \(Q\)-exact shift.
- Cartan-model closure when \(Q^2\) is a compact even symmetry.
- BV formulation of cohomological gauge theories through the quantum master
  equation and BV Stokes.
- Donaldson-Witten as the guiding infinite-dimensional gauge-equivariant
  Mathai-Quillen model for the section \(F_A^+\).
- Ledger of obligations for infinite-dimensional theorem-level localization.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Lambda\) | finite regulator |
| \(\mathcal A_\Lambda\) | regulated insertion algebra |
| \(Q_\Lambda\) | odd regulated cohomological derivation |
| \(B_\Lambda\) | even derivation equal to \(Q_\Lambda^2\) |
| \(\Gamma_\Lambda\) | integration cycle, contour, BV Lagrangian, or trace datum |
| \(S_\Lambda\) | regulated action or weight |
| \(V\) | odd \(Q\)-exact deformation functional |
| \(F\) | compact fixed locus of the localization deformation |
| \(e_{Q^2}(N_F)\) | equivariant Euler factor of the normal quadratic complex |
| \(E\to X\) | finite-dimensional vector bundle in the Mathai-Quillen model |
| \(s\) | section whose zero locus is localized onto |
| \(\chi,H\) | odd antighost and even auxiliary field in Mathai-Quillen form |
| \(\mathcal O^{(p)}\) | \(p\)-form descendant observable |
| \(\gamma_p\) | closed \(p\)-cycle used for an integrated descendant |
| \(d_K\) | Cartan equivariant differential |
| \((\,\cdot\,,\,\cdot\,)\), \(\Delta\) | BV bracket and regulated BV Laplacian |
| \(F_A^+\) | self-dual curvature section in Donaldson-Witten theory |

## Claim Ledger

1. Cohomological QFT requires a regulated Ward identity; formal \(Q\)-algebra
   alone does not define a QFT.
2. If \(Q^2=B\), cohomology is taken on the \(B\)-invariant subalgebra.
3. Metric independence follows from the full metric-response insertion being
   \(Q\)-exact, including contact terms and moving representatives.
4. \(Q\)-exact deformations do not change normalized correlators when the
   Ward identity holds for the deformed measure.
5. Localization is a theorem in finite dimension under compactness,
   positivity/contour, and nondegenerate normal-complex hypotheses.
6. Mathai-Quillen localization gives the finite-dimensional model for
   cohomological equations \(s=0\).
7. Integrated descendants are \(Q\)-closed on closed cycles and depend only on
   homology classes in \(Q\)-cohomology, after the specified contact-term
   convention.
8. Gauge-theoretic cohomological theories must be formulated through BV or an
   equally precise regulator-level gauge framework.
9. Donaldson-Witten theory is the gauge-equivariant Mathai-Quillen model for
   the section \(A\mapsto F_A^+\), with analytic compactness and determinant
   issues supplied later.

## Figures

- No figure added in this pass.  The fixed-locus/normal-bundle localization
  picture is described algebraically; a later visual pass may add it if it
  improves readability.

## Calculation Checks

- `calculation-checks/cohomological_field_theory_checks.py` verifies exact
  finite Cartan-model algebra, Hamiltonian equivariant closure,
  Mathai-Quillen Gaussian square completion, and rank-one zero-locus
  orientation.

## Anti-Wrapper Audit

- 2026-05-29: strengthened the Mathai-Quillen zero-locus statement by
  replacing the compressed Thom-form slogan with a transverse-section
  localization proof: \(t^{1/2}s\) deformation, exponential suppression away
  from the zero locus, tubular normal coordinates, \(t^{-1/2}\) rescaling, and
  cancellation of the Gaussian Jacobian against the Berezin determinant.
