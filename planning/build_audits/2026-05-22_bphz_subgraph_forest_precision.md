# BPHZ Subgraph And Forest Precision Pass

Date: 2026-05-22

Scope:

- `monograph/tex/volumes/volume_ii/chapter09_subdivergences_and_bphz_subtractions.tex`
- `planning/chapter_dossiers/volume_ii/chapter11_subdivergences_forest_formulas.md`

Substantive changes:

- Stated the chapter's 1PI-kernel convention explicitly, so connected Green
  functions remain downstream of the Legendre tree reconstruction.
- Replaced the compressed subgraph description by a momentum-subgraph
  definition using internal lines, external half-lines, componentwise momentum
  conservation, and contraction \(\Gamma/\gamma\).
- Clarified that \(p_\gamma\) variables from the contracted graph are held
  fixed during the ultraviolet test and Taylor subtraction.
- Tightened spinney and forest definitions to connected divergent subgraphs,
  with disconnected divergent subtractions treated as products over connected
  components.
- Clarified the recursive \(C_\gamma\), \(\overline R_\Gamma\), and forest
  formula ordering from smaller subgraphs to larger contracted graphs.
- Strengthened the BPHZ proof sketch by spelling out that external-momentum
  derivatives lower the superficial ultraviolet degree, giving a negative
  degree for each forest-sector boundary after Taylor subtraction.
- Cleaned the oversubtraction and finite-coordinate transition into the 1PI RG
  chapter.

Verification:

- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- Visual inspection of rendered Chapter 31 pages and Figures 31.1--31.3.
