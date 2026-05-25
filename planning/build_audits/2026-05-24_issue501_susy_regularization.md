# Issue #501 Supersymmetric Regularization Pass

## Scope

- Oldest verified open GitHub issue: `#501`, on regularization schemes and
  their compatibility or incompatibility with supersymmetry.
- Manuscript locus:
  `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Planning locus:
  `planning/chapter_dossiers/volume_ii/chapter18_gauge_fixing_ghosts_brst.md`.

## Content Added

- Added Section `Supersymmetric Ward Identities and Regulator Data`.
- Defined a supersymmetry datum on a gauge-fixed local theory, including the
  closure formula with translations, gauge transformations, BRST-exact terms,
  and Euler--Lagrange terms.
- Introduced the extended algebraic-renormalization differential
  \(s_{\mathrm{ext}}\) with constant supersymmetry and translation ghosts.
- Separated four kinds of data: path-integral or graph regulator, gauge-fixing
  and BV data, operator-insertion regulator, and renormalized coordinate
  scheme.
- Proved the cohomological restoration criterion for supersymmetry Ward
  identities using \(H^{1,D}(s_{\mathrm{ext}}\mid d)\).
- Classified DRED, CDR/HV, superspace and higher-derivative regulators,
  Pauli--Villars-type auxiliary determinants, lattice/twisted regulators, and
  localization-compatible regulators by the data required for a symmetry
  statement.
- Reframed holomorphy and nonrenormalization as Wilsonian superspace
  source-chart statements with explicit locality, chirality, charge, and
  regularity hypotheses.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 771 pages.
