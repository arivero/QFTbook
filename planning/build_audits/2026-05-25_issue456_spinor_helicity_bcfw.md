# 2026-05-25 Issue #456 Spinor-Helicity and BCFW Audit

## Scope

- GitHub issue: #456, `[Vol II] Spinor-helicity formalism and on-shell tree
  recursion (BCFW) entirely absent`.
- Manuscript target:
  `monograph/tex/volumes/volume_i/chapter17_massless_particles_helicity_and_gauge_redundancy.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_i/chapter17_massless_particles_helicity_gauge_redundancy.md`.

## Manuscript Changes

- Added a four-dimensional spinor-helicity interlude after the polarization
  representative discussion.
- Defined \(p_{a\dot a}=p^0\delta_{a\dot a}+p^i\sigma_{i,a\dot a}\), the
  null factorization \(p_{a\dot a}=\lambda_a\widetilde\lambda_{\dot a}\), and
  the little-group scaling
  \((\lambda,\widetilde\lambda)\mapsto(t\lambda,t^{-1}\widetilde\lambda)\).
- Fixed the mostly-plus invariant convention
  \(\langle ij\rangle[ji]=-2p_i\cdot p_j\), and stated the helicity-amplitude
  weight \(t_i^{-2h_i}\).
- Added spinor-helicity polarization representatives and identified reference
  spinor changes with gauge-representative shifts.
- Introduced color-ordered tree amplitudes, the nonzero complex three-gluon
  amplitudes, and the Parke--Taylor MHV formula.
- Added BCFW shifts, their on-shell and momentum-conservation properties, the
  tree-factorization residue, the recursion with possible boundary term, and a
  factorization figure.
- Included the \(A_5(1^-,2^-,3^+,4^+,5^+)\) MHV example as a BCFW
  factorization channel and displayed the five-point Parke--Taylor result.

## Dossier Changes

- Added spinor-helicity and BCFW to the chapter scope, external-reference
  boundary, symbols, claim ledger, figure requirements, exclusions, and audit
  notes.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 811 pages, PDF 1.5.
