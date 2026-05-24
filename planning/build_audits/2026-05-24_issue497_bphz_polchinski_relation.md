# Build Audit: Issue #497 BPHZ--Polchinski Relation

Date: 2026-05-24

Scope:

- `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`
- `monograph/tex/volumes/volume_ii/chapter09_subdivergences_and_bphz_subtractions.tex`
- `monograph/tex/volumes/volume_ii/chapter12_renormalized_operators_and_minimal_subtraction.tex`
- `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md`
- `planning/chapter_dossiers/volume_ii/chapter11_subdivergences_forest_formulas.md`
- `planning/chapter_dossiers/volume_ii/chapter13_renormalized_operators_minimal_subtraction.md`

Issue addressed:

- GitHub #497 asked for a deep synthesis of the precise relationship between
  BPHZ forest-formula renormalizability and Polchinski-style Wilsonian
  renormalizability.

Mathematical changes:

- Added Definition `def:bphz-wilsonian-comparison-datum`, fixing the BPHZ
  subtraction scheme, low-source test space, Wilsonian covariance split,
  Wilsonian Banach chart, local coordinate projectors, 1PI projectors, and
  matching ratio.
- Added Proposition `prop:bphz-local-parts-wilsonian-coordinates`, proving
  that a BPHZ Taylor local part is a finite external-momentum polynomial whose
  Fourier transform is a local vertex.  Minimal BPHZ subtractions land in
  relevant/marginal Wilsonian coordinates by power counting; oversubtractions
  give a finite retained list of higher-derivative local coordinates.
- Expanded the matching theorem by displaying the recursive loop-order
  construction of the finite coordinate map
  \(u_A=G_A(g,u_{\bar A};\Lambda/\mu,\mathfrak b)\), with the selected
  tree-level Jacobian inverted at each order.
- Added a status remark separating the exact finite-regulator identity,
  finite-dimensional Legendre-transform hypothesis, fixed-loop BPHZ theorem,
  Wilsonian norm estimates, scheme changes, and nonperturbative existence
  requirements.
- Added cross-links from the BPHZ finite-parts chapter and the
  renormalized-operator/normal-product chapter to the Wilsonian comparison.

Verification:

- `git diff --cached --check`: clean after reconciliation onto `origin/main`.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; generated
  `monograph/tex/main.pdf` with 739 pages.
