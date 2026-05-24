# Issue #278 Audit: Radial Block Gram-Matrix Inversion

## Scope

- GitHub issue: #278, ``[Vol V Ch 9] Radial-block expansion: Gram-matrix
  inversion glossed''.
- Manuscript file:
  `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.
- Dossier file:
  `planning/chapter_dossiers/volume_iii/chapter09_operator_product_expansion.md`.

## Manuscript Changes

- Replaced the compressed sentence about Gram-matrix inversion with a
  finite-level construction.
- Defined the raw descendant space \(W_{i,n}\), the raw Gram form, and the null
  subspace \(\mathcal N_{i,n}\).
- Explained why reflection positivity makes null descendants invisible in
  physical matrix elements and why the quotient \(Q_{i,n}\) is the space to
  invert on.
- Displayed the quotient Gram matrix \(M^{(n)}\), the level projector
  \(\Pi_{i,n}\), and the explicit level-\(n\) contraction formula.
- Stated that shortening and conservation enter through these null subspaces.

## Verification

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed.
