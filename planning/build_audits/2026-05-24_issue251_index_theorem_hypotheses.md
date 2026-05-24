# Issue #251 Index Theorem Hypotheses Pass

## Scope

- Oldest active GitHub issue: `#251`, on the local index-density paragraph in
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Required repair: name and cite the Atiyah--Singer theorem, state the
  hypotheses under which the integrated density is a Fredholm index, and
  display the Atiyah--Patodi--Singer boundary correction needed when a boundary
  is present.

## Content Added

- Replaced the informal integrated-index paragraph by a theorem-level
  statement for the spin Dirac operator on a smooth compact oriented
  Riemannian spin four-manifold without boundary.
- Defined the chiral spinor bundles \(S^\pm\), the Hermitian gauge bundle
  \(E_R\), the smooth unitary connection \(\nabla^E\), the elliptic operator
  \(\mathcal D_{A,+}\), and its opposite-chirality partner.
- Stated the Chern--Weil formula
  \[
    \operatorname{index}\mathcal D_{A,+}
    =
    \int_M[\widehat A(TM)\operatorname{ch}(E_R,\nabla^E)]_4
  \]
  and then specialized it to the flat tangent/gauge-anomaly normalization used
  in the local heat-kernel calculation.
- Added a reader-facing bibliographic footnote for Atiyah--Singer and
  Atiyah--Patodi--Singer.
- Added the APS boundary setup with product collar, tangential boundary Dirac
  operator \(B_A\), spectral projection boundary condition, eta function,
  boundary zero-mode count, and formula
  \[
    \operatorname{index}\mathcal D^{\mathrm{APS}}_{A,+}
    =
    \int_M[\widehat A(TM)\operatorname{ch}(E_R,\nabla^E)]_4
    -
    \frac{\eta_{B_A}(0)+h_{B_A}}2 .
  \]
- Updated the anomaly chapter dossier with the new symbols, theorem status,
  and audit note.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
