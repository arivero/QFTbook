# Issue #502 Dimensional Regularization Pass

## Scope

- Oldest active GitHub issue: `#502`, on a rigorous modern treatment of
  dimensional regularization consistency in perturbative gauge theory.
- Manuscript locus:
  `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Planning locus:
  `planning/chapter_dossiers/volume_ii/chapter18_gauge_fixing_ghosts_brst.md`.

## Content Added

- Defined dimensional regularization as a perturbative meromorphic assignment
  of Feynman graph distributions, with \(\dd^Dq\) interpreted through
  Schwinger/Feynman parameter continuation rather than as a Borel measure on a
  noninteger-dimensional space.
- Separated the scalar analytic continuation from tensor, spinor,
  polarization, and external-state algebraic prescriptions.
- Distinguished CDR, HV, DRED, and FDH.  DRED is recorded with formal
  projectors \(\eta_4=\hat\eta+\tilde\eta\) and evanescent scalar coordinates.
- Stated the \(\gamma_5\) and Levi-Civita scheme data, including the
  Breitenlohner--Maison/'t Hooft--Veltman prescription and the
  dimensional-reduction bookkeeping used for anomaly calculations.
- Added Proposition `prop:dimreg-st-control`, identifying locality of pole
  parts, the local Slavnov--Taylor breaking cocycle, the exact-cohomology
  counterterm restoration case, and the nonzero-cohomology anomaly obstruction.
- Separated regularization, renormalization, and operator-insertion/source
  regularization.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
