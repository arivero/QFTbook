# Volume V Proof-Substance Audit

Date: 2026-05-28.

Scope: `monograph/tex/volumes/volume_v`.

## Repairs Made

- `chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`:
  expanded `prop:unitary-minimal-model-fusion-check`.  The proof now derives
  the finite \(SU(2)_k\) fusion rule from the sine-matrix inner product,
  ordinary \(SU(2)\) character multiplication, and the affine-wall relation
  \(\chi_{k+1+r}=-\chi_{k+1-r}\) on the Verlinde grid before taking the
  fixed-point-free Kac-table quotient.
- `chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`:
  demoted the torus self-sewing trace statement from proposition to remark.
  The calculation is useful bookkeeping, but its proof is the definition of an
  operator trace in a homogeneous basis.
- `chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`:
  demoted the direct-integral OPE identity from proposition to remark.  The
  formula is the Plancherel identity for the specified direct-integral
  decomposition rather than an independent theorem.
- `chapter14_boundary_conformal_field_theory.tex`: demoted the direct-sum
  Chan-Paton statement from proposition to remark.  The displayed matrix-unit
  formulas are retained, but the argument only unpacks finite biproducts in the
  boundary category.
- `chapter15_two_dimensional_superconformal_algebras.tex`: demoted the
  rank-one spectral-flow formula check from proposition to remark.  The
  substitution is retained in full, but it is not elevated to a proposition.

## Statements Retained

- The KZ equation remains a theorem: its proof derives the differential
  equation from the translation Ward identity, the Sugawara expression for
  \(L_{-1}\), and contour deformation of the current insertion.
- The Verlinde formula from modular diagonalization remains a theorem: it is
  explicitly a linear-algebra result conditional on the deep diagonalization
  input, which is separately identified in the surrounding text.
- The Cardy diagonal solution remains a theorem: the proof is the direct
  substitution of the Cardy coefficients into the annulus equation together
  with the already isolated Verlinde input.
- Calculation propositions in the sigma-model, WZW, Liouville, orbifold, and
  boundary-CFT sections were retained when their proofs perform an actual
  variation, OPE computation, Ward-identity derivation, modular transformation,
  Schwarzian computation, or finite algebraic check.

## Remaining Proof Obligations

- The analytic sewing theorem for rational chiral data remains a hypothesis,
  as it should: trace-class edge estimates are not the full theorem that local
  sewing series assemble into globally compatible finite-rank bundles over
  moduli.
- The quoted VOA/net, Zhu, Virasoro classification, rational modularity, and
  noncompact cigar spectrum results remain external structural inputs.  A
  future foundational appendix could choose selected results for internal
  proof, but they are no longer presented as if the manuscript had already
  proved them.
