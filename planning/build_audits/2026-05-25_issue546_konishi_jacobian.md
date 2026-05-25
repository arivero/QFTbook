# Build Audit: Issue 546 Konishi Jacobian

Date: 2026-05-25

## Scope

Substantive development pass on
`monograph/tex/volumes/volume_vii/chapter05_nonrenormalization_holomorphy.tex`,
addressing the missing derivation of the Konishi-type rescaling anomaly.

## Mathematical Changes

- Defined \(T(R)\) before it is used in the Konishi section, with direct
  reference to the monograph's gauge trace convention.
- Replaced the asserted Konishi Jacobian paragraph by a proposition with an
  explicit regulator hypothesis.
- Derived the local Jacobian as a regulated finite-mode/spectral
  Berezinian statement, reducing the gauge-dependent chiral part to the
  Weyl-fermion heat-kernel density already computed in the anomaly chapter.
- Used chirality, gauge invariance, locality, and the superspace gauge kinetic
  normalization to identify the unique chiral representative
  \(\int d^2\theta\,\operatorname{tr}(W^\alpha W_\alpha)\) and fix the
  coefficient.
- Added a convention remark explaining how the sign of the Jacobian depends on
  whether it is exponentiated into the action or kept in the measure.
- Updated the Volume VII Chapter 5 dossier.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` built cleanly.
- `pdfinfo monograph/tex/main.pdf` reports 1266 pages.
