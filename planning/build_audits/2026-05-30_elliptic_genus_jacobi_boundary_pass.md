# Elliptic Genus Jacobi Boundary Pass

Date: 2026-05-30.

GitHub context: #697 and #691.

Purpose: reduce one remaining Volume V CFT quoted-theorem boundary without
pretending that the full spin modular-functor theorem has been proven in this
pass.

Files edited:

- `monograph/tex/volumes/volume_v/chapter15_two_dimensional_superconformal_algebras.tex`
- `calculation-checks/superconformal_algebra_checks.py`
- `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`
- `planning/chapter_dossiers/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.md`
- `planning/chapter_dossiers/volume_v/chapter15_two_dimensional_superconformal_algebras.md`

Substance:

- Expanded the local mechanism behind the elliptic-genus Jacobi modular
  factor.  The manuscript now explains the elliptic genus as a section of the
  \(U(1)_R\) anomaly determinant line over elliptic curves with flat
  \(R\)-background, with index \(m_{\rm ell}=c/6\) fixed by the
  `J J` OPE coefficient.
- Kept the theorem boundary honest: the quadratic automorphy factor and its
  cocycle are local current-algebra/anomaly algebra, while the existence of
  the spin modular functor and anomaly-cancelled \(R\)-background remains the
  quoted theorem input.
- Extended `superconformal_algebra_checks.py` to verify the modular quadratic
  cocycle for the Jacobi automorphy factor, in addition to the preexisting
  elliptic spectral-flow cocycle checks.
- Replaced inappropriate string-worldsheet terminology in the Volume V
  sigma-model chapter with intrinsic two-dimensional QFT language such as
  source surface, \(\Sigma\), source supermanifold, and two-dimensional
  fermions.  This keeps QFT sigma models distinct from string-theory
  worldsheet constructions.

Status:

- This pass does not close #697; it removes one black-box edge in the
  elliptic-genus modular theorem boundary.  Liouville, VOA, and sewing
  theorem-boundary work remains.
