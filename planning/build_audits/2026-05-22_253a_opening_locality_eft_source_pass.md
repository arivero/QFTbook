# 2026-05-22 253a Opening Locality/EFT Source Pass

## Source Block

- Primary source: `references/253a lectures 2022.pdf`, pp. 1--2.
- Rendered source images inspected:
  - `/tmp/253a_001_002-001.png`
  - `/tmp/253a_001_002-002.png`
- Operational transcription cross-check:
  - `transcription/tex/253a/foundations.tex`
- Student transcription cross-check:
  - `references/253a_notes.tex`

## Source Content Checked

- The opening conceptual answer: QFT is quantum mechanics equipped with
  spacetime locality data.
- The fork between local continuum QFT and effective field theory.
- Local-continuum-side data: Poincare symmetry, local field operators, and
  microcausality.
- EFT-side data: perturbative path-integral presentation over fields and
  long-distance/low-energy observables.
- Examples: low-dimensional \(\phi^4\), statistical Ising near criticality,
  Yang--Mills/QCD, \(\phi^4\) in \(D=4\), QED, Standard Model, chiral
  perturbation theory, and perturbative gravity.
- Initial dependency plan: Lagrangian path integrals, regularization,
  perturbation theory, Feynman diagrams, counterterms, scalar fields, Green
  functions, asymptotic states, S-matrix/LSZ, spin, fermions/gauge bosons,
  QED, and precision-observable applications.

## Manuscript Changes

- `monograph/tex/volumes/volume_i/chapter01_what_is_qft.tex`
  - Added `Local Continuum Theories And Effective Presentations`.
  - Defined continuum local QFT and EFT presentation with explicit status and
    scale-window qualifications.
  - Added `fig:opening-local-qft-eft`, a course-label-free replacement for
    the handwritten opening fork.
  - Extended the logical-order section to record the three dependency bands
    while preserving the monograph rule that perturbative scattering diagrams
    are interpreted only after nonperturbative scattering and LSZ.
- `planning/source_inventory/253a_253b_no_skip_coverage_register.md`
  - Marked pp. 1--2 certified.
- `planning/chapter_dossiers/volume_i/chapter01_what_is_qft.md`
  - Updated source anchors, definition/claim ledgers, and figure ledger.

## Verification Run

- `tools/build_monograph.sh`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `git diff --check`: clean.
- Rendered manuscript pages inspected:
  - `/tmp/qft_ch1_opening_cert2-020.png`: definitions of continuum local QFT
    and EFT presentation.
  - `/tmp/qft_ch1_opening_cert2-021.png`: `fig:opening-local-qft-eft`,
    checked after a first render exposed label overlap; the revised figure has
    separated branch headers and body boxes.
