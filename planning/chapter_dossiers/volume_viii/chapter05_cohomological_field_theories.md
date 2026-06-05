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
- Theorem: compact Cartan localization in the Atiyah--Bott--Berline--Vergne
  form over the localized equivariant coefficient ring, with fixed components
  \(F_a\), normal bundles \(N_a\), nonzero symbolic equivariant normal weights,
  a genuine inverse equivariant Euler denominator \(e_T(N_a)^{-1}\), and a
  separate regularity condition before evaluating at a numerical
  \(\xi\in\mathfrak t\).
- Lemma: local super-Gaussian normal form showing when
  \(\operatorname{Pf}(C)/\det(A)^{1/2}\) represents that inverse Euler density,
  and when it is only a one-loop Gaussian factor.
- Explicit \(S^2\) fixed-point denominator example, zero-normal-weight
  obstruction example, and rank-two weight-hyperplane evaluation example.
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
| \(F_a\) | fixed components of the compact torus action |
| \(N_a\) | normal bundle of a fixed component |
| \(e_T(N_a)\) | genuine equivariant Euler class of the normal bundle |
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
5. Localization is a theorem in finite dimension in the compact Cartan model
   after localizing nonzero symbolic normal weights in \(S(\mathfrak t^*)\);
   numerical evaluation at \(\xi\) is a separate regularity step, and on a
   weight hyperplane the fixed locus must be enlarged before normal weights are
   inverted.  A super-Gaussian denominator is an Euler denominator only when it
   represents that normal equivariant Euler class.
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
  Mathai-Quillen Gaussian square completion, rank-one zero-locus orientation,
  and the squared normal inverse-Euler factor in a two-even/two-odd local
  Gaussian model, plus the \(S^2\) direct-integral/fixed-point coefficient
  identity, the noninvertibility of a zero normal weight, and a rank-two torus
  hyperplane example showing that a nonzero symbolic weight can vanish after
  evaluation at a nongeneric \(\xi\).

## Anti-Wrapper Audit

- 2026-05-29: strengthened the Mathai-Quillen zero-locus statement by
  replacing the compressed Thom-form slogan with a transverse-section
  localization proof: \(t^{1/2}s\) deformation, exponential suppression away
  from the zero locus, tubular normal coordinates, \(t^{-1/2}\) rescaling, and
  cancellation of the Gaussian Jacobian against the Berezin determinant.
- 2026-05-30: repaired the compact nondegenerate localization theorem so
  \(S\) is part of the theorem datum, \(QS=0\) is a stated hypothesis, the
  fixed-locus formula follows from a displayed normal quadratic model, and the
  determinant/Pfaffian inverse-Euler factor is no longer an undefined slogan.
- 2026-06-05 issue #811 status pass: replaced the broad superfunction
  localization theorem with the compact Cartan localization theorem, defined
  the fixed components, normal bundle, orientation/Euler denominator, separated
  the local super-Gaussian lemma from the theorem-level Euler class, and added
  positive and negative finite examples.
- 2026-06-05 issue #839 follow-up: separated ABBV localization over the
  localized equivariant coefficient ring from evaluation at a numerical
  \(\xi\).  The theorem now localizes nonzero characters in
  \(S(\mathfrak t^*)\), states that evaluation requires
  \(w(\xi)\ne0\) for every normal weight, explains that \(M^\xi\) enlarges on
  a weight hyperplane, and adds the \(T^2\curvearrowright S^2\times S^2\)
  example where \(\xi=(1,0)\) leaves the second sphere as a residual collective
  coordinate.  The companion check verifies this rank-two hyperplane negative
  example.
