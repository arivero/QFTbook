# su(2|2)c intertwiner row-rank wrapper demoted

Date: 2026-05-31

Related issue: GitHub #691, theorem/proof substance and anti-wrapper audit.

## Scope

This pass audited the generic one-copy `su(2|2)_c` intertwiner row-rank block
in `volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`.  The row
chart is useful because it records how the dynamic-frame symmetry equations
fix the ten amplitudes up to one scalar factor on the generic open set.
However, after those equations have been reduced, the proof is finite
row-echelon bookkeeping: nine equations have pivots in the nine non-`A`
columns.

## Change

- Replaced the lemma/proof shell titled "Generic rank certificate for the
  one-copy intertwiner" by the paragraph "Generic row-rank certificate for the
  one-copy intertwiner."
- Preserved the generic open set, row-reduced coefficients, rank-nine
  statement, one-dimensional solution space, normalization
  `A_{12}=mathcal S_{12} n_{12}/d_{12}`, and the warning that zero
  denominators belong to reducible, bound-state, or pole analyses.
- Added an explicit sentence distinguishing the finite dynamic-frame row
  certificate from theorem-level statements about the planar gauge theory.
- Added a theorem-form audit guard so the old title is rejected if it returns
  as theorem/proposition/lemma/corollary content.
- Updated the Volume VII Chapter 13 dossier.

## Status

This is another concrete #691 demotion.  The paired calculation check
`check_su2c_intertwiner_rank_certificate()` remains the right place for exact
finite rational verification of the row chart.
