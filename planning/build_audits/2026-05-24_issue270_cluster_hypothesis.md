# Issue #270 Cluster Hypothesis Audit

## Scope

- Oldest active GitHub issue addressed: `#270`, on cluster decomposition for
  the conformal vacuum being invoked without a consolidated hypothesis.
- Manuscript files:
  - `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
  - `monograph/tex/volumes/volume_iii/chapter07_unitarity_bounds_and_short_multiplets.tex`
- Dossiers:
  - `planning/chapter_dossiers/volume_iii/chapter04_radial_quantization_state_operator.md`
  - `planning/chapter_dossiers/volume_iii/chapter07_unitarity_bounds_short_multiplets.md`

## Content Added

- Expanded Hypothesis `hyp:radial-reconstruction-data` so the zero-energy
  radial eigenspace being \(\mathbb C\ket{\vac}\) is stated as uniqueness of the
  conformally invariant vacuum.
- Replaced the inline cluster phrase by a displayed large-translation
  factorization condition for separated Euclidean local correlators:
  \[
    \lim_{\lambda\to+\infty}
    \langle A(x_i+\lambda a)B(y_j)\rangle_E
    =
    \langle A(x_i)\rangle_E\,\langle B(y_j)\rangle_E .
  \]
- Updated the scalar \(\Delta=0\) branch in the unitarity-bounds chapter to
  cite Hypothesis `hyp:radial-reconstruction-data` when identifying a
  spacetime-constant scalar local field with the identity operator.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

All checks completed cleanly on 2026-05-24.
