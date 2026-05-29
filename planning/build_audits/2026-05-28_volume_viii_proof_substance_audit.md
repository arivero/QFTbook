# Volume VIII Proof-Substance Audit

Date: 2026-05-28.

Scope: `monograph/tex/volumes/volume_viii`.

This pass read the proof bodies in the TQFT/cohomological/BV volume.  The
main repair was to remove theorem weight from identities whose proof only
unpacked a variation, a finite trigonometric check, an imported
modular-functor formula, or a structural normal-form description.

## Repairs Made

- `chapter03_bf_theory.tex`: demoted the BF Euler-Lagrange equations and the
  \(B\)-field shift-symmetry variation to remarks.  The variation and boundary
  term remain explicit, but the finite Fourier partition function and linking
  phase retain theorem-like form because their proofs perform cochain
  summation and homological counting.
- `chapter04_chern_simons_theory.tex`: demoted exponentiated Chern-Simons
  gauge invariance, \(SU(2)_k\) sine-matrix orthogonality, and the Verlinde
  dimension formula to remarks.  The transgression and Polyakov-Wiegmann
  lemmas remain theorem-like because the proof bodies carry the actual
  convention-sensitive differential-form algebra.
- `chapter06_topological_sigma_models.tex`: demoted the B-model
  complex-structure dependence statement to a remark.  It is the local
  Maurer-Cartan expansion of the deformed \(\bar\partial\)-operator, not a
  theorem about the full quantum B-model.
- `chapter08_witten_donaldson_seiberg_witten_comparison.tex`: demoted
  Donaldson coefficient extraction and the Kotschick-Morgan polynomial normal
  form to remarks.  The \(u\)-plane wall-crossing boundary mechanism is now a
  controlled approximation, since its proof rests on the assumed Abelian
  Wilsonian description, singular-fiber matching, theta-kernel decay, contact
  normalization, and determinant-line phase matching.
- `chapter09_boundaries_defects_and_categories.tex`: demoted the
  one-dimensional interval-gluing associativity statement to a remark.  It is
  a useful unpacking of functoriality, but not an independent theorem.
- `chapter10_bv_integration_and_localization.tex`: demoted the BV product
  identity to a remark.  The BV Stokes theorem, pushforward theorem, boundary
  obstruction, and singular-stratum obstruction remain theorem/proposition
  material because their proofs construct the finite-dimensional BV
  integration mechanism used elsewhere in the monograph.

## Statements Retained

- The Atiyah-Segal state-space duality, Frobenius identities, and
  two-dimensional TQFT/Frobenius-algebra classification were retained because
  the proofs use the cap-cylinder triangular identities, dual-basis
  nondegeneracy, Cerf moves, and gluing generators.
- Finite BF and finite gauge theory results were retained where the proof
  performs finite Fourier projection, homology cardinality, cochain linking,
  groupoid push-pull gluing, cocycle/Pachner cancellation, or character
  expansion.
- Cohomological localization statements were retained where the proof uses a
  Ward identity with a specified regulated Stokes property, compact
  nondegenerate normal coordinates, Gaussian/Berezin normal integration, or the
  Mathai-Quillen Thom representative.
- Topological sigma-model statements were retained where the proof computes
  the A-model pointwise energy identity, the fixed-domain Fredholm index, or
  associativity from the splitting axiom for genus-zero virtual classes.
- Donaldson-Witten and Seiberg-Witten statements were retained where the proof
  uses Atiyah-Singer index formulae, the topology of \(\operatorname{Spin}^c\)
  structures, monopole deformation index arithmetic, or the BV boundary
  formula applied to Uhlenbeck and reducible strata.
- Boundary/defect statements were retained where the proof gives primitive
  central idempotents by Schur orthogonality, finite biset quotient
  associativity, or the algebra-object criterion for Lagrangian subgroups in a
  pointed modular category.

## Remaining Proof Obligations

- The Chern-Simons modular functor and the Verlinde formula are still treated
  as modular-functor input rather than derived from the nonperturbative
  Chern-Simons path integral.  A future pass should either give the
  representation-theoretic construction in detail or mark the full modular
  functor theorem as external input.
- The Donaldson/Seiberg-Witten comparison chapter still contains a frontier
  QFT goal: make the RG-flow route from twisted \(\mathcal N=2\) Yang-Mills
  to the Abelian monopole effective theory mathematically controlled enough
  that the \(u\)-plane and monopole boundary terms are not merely a
  controlled approximation.
- Cohomological localization in field theory remains conditional on a
  regulator, contour, compactness theorem, and BV QME preservation.  The
  finite-dimensional theorems are proved, but the infinite-dimensional
  promotion must be supplied separately in each QFT example.
- The topological sigma-model discussion still depends on virtual fundamental
  class technology.  The associativity proof derives the algebraic conclusion
  from the splitting axiom, but the construction and compatibility of virtual
  classes remain external geometric input unless later appendices develop them.
