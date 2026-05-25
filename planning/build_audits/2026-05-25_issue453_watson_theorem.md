# 2026-05-25 Issue #453 Watson Theorem Audit

## Scope

- GitHub issue: #453, `[Vol II] Watson's theorem (final-state interactions /
  form-factor phases) absent`.
- Manuscript target:
  `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_ii/chapter07_partial_waves_dispersion_froissart.md`.

## Manuscript Changes

- Added `Elastic Form Factors and Watson's Theorem` after the partial-wave
  normalization and optical theorem, before the Froissart--Martin mechanism.
- Stated the one-channel elastic hypotheses, the boundary-value convention for
  the form factor, the Hermiticity/real-analyticity relation
  \(\mathcal F_A^-=(\mathcal F_A^+)^*\), and the scattering normalization
  \(S_A=1+2i\beta a_A=e^{2i\delta_A}\).
- Derived the form-factor unitarity discontinuity
  \[
    \mathcal F_A^+-\mathcal F_A^-
    =
    2i\beta a_A^*\mathcal F_A^+
  \]
  and the Watson phase relation
  \[
    \mathcal F_A^+=e^{2i\delta_A}\mathcal F_A^-,
    \qquad e^{-i\delta_A}\mathcal F_A^+\in\mathbb R .
  \]
- Added the standard two-pion examples: the isovector vector form factor with
  phase \(\delta^1_1\), and the isoscalar scalar form factor with phase
  \(\delta^0_0\), each only in the corresponding elastic interval.
- Added an elastic-cut figure showing the upper/lower boundary values,
  complex conjugation from real analyticity, and multiplication by
  \(S_A=e^{2i\delta_A}\).
- Added the coupled-channel matrix replacement
  \(\mathbf F^+=S_A\mathbf F^-\), explicitly separating it from the
  one-channel phase theorem.
- Added the Omnes construction as a consequence requiring additional
  analyticity, zero/pole, and growth hypotheses; Watson's theorem is stated as
  fixing only the elastic-cut boundary phase.

## Dossier Changes

- Added Watson-theorem hypotheses, symbols, claims, figure requirement, and
  audit note to the chapter dossier.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 803 pages.
