# Issue 370: Spectral-Transfer Translation Convention

## Scope

GitHub issue #370 pointed out that the spectral-transfer formula in
`volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex` used a
Fourier-support sign determined by the translation convention, but the chapter
had not declared that convention locally.

## Fix

- Added the standing convention
  \(U(a)=U(a,\mathbf 1)=\exp(\ii a_\mu P^\mu)\) at the start of the chapter.
- Declared that the Fourier phase uses the same contraction
  \(q\cdot x=q_\mu x^\mu\).
- Stated explicitly that the opposite sign convention for translations would
  replace \(\operatorname{supp}\widehat f\) by
  \(-\operatorname{supp}\widehat f\) in the transfer statement.
- Added the spectral-projection derivation
  \(E(\dd p)A(f)E(\dd r)=\widehat f(p-r)E(\dd p)AE(\dd r)\), so that the
  support condition follows from the joint spectral theorem rather than from
  an implicit convention.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
