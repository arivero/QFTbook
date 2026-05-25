# Build Audit: Issue 576 Debye Mass One-Loop Coefficients

Date: 2026-05-25

## Scope

Addressed GitHub issue #576 in
`monograph/tex/volumes/volume_x/chapter07_thermal_gauge_theory_screening.tex`.

## Mathematical Changes

- Replaced the merely stated Debye mass coefficient by an explicit one-loop
  derivation from a constant temporal background `A_0`.
- Added the thermal susceptibility integrals
  `(1/T) int_p n_B(1+n_B)=T^2/6` and
  `(1/T) int_p n_F(1-n_F)=T^2/12`, with the integration-by-parts proof.
- Derived the matter coefficients by expanding the thermal free energy with
  imaginary chemical potential and summing weights:
  Dirac fermion `T_R/3`, complex scalar `T_R/3`, real scalar `T_R/6`.
- Derived the gauge coefficient from the background-field determinant
  `1/2 Tr_vec log(-D^2)-Tr_gh log(-D^2)`, leaving two adjoint transverse
  bosonic degrees and hence `C_A/3`.
- Corrected the scalar convention: with the monograph definition
  `tr_R(T^aT^b)=T_R delta^{ab}` on a complex representation, a complex scalar
  contributes `T_R/3`.  The coefficient `T_R/6` belongs to one real scalar
  degree of freedom in a real representation.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean after replacing the undefined local
  `\Tr` notation by explicit `\operatorname{Tr}`.
- `pdfinfo monograph/tex/main.pdf`: 1257 pages.
