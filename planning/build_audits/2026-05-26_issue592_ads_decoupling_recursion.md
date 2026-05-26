# Build Audit: ADS Holomorphic Decoupling Recursion

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Issue focus: #592, with foundational overlap for #605 SQCD dynamics.

## Scope

This pass strengthens Volume VII Chapter 06 in the SQCD ADS section.  The
previous chapter state had a direct `N_f=N_c-1` one-instanton seed and the
holomorphic threshold equation, but the finite-dimensional elimination step
propagating the ADS superpotential to all `N_f<N_c` was only described in
words.  This audit records the insertion of that missing derivation.

## Source And Convention Notes

- The derivation is internal to QFT: no string compactification, D-brane, or
  superstring argument is used.
- The scale convention is the holomorphic Wilsonian convention already used
  in Chapter 06.
- The proof is local on a holomorphic branch because fractional powers of
  chiral coordinates are present.
- The standard representative `C_n=N_c-n` is stated only after fixing the
  one-instanton seed normalization `C_{N_c-1}=1`; otherwise the coefficient
  recursion records the scheme-dependent nonzero constants.

## Substantive Changes

- Added Proposition `prop:ads-holomorphic-decoupling-recursion`.
- Displayed the mass deformation from the `(n+1)`-flavor ADS
  superpotential, the light-branch determinant factorization
  `det Mcal = X det M`, and the one-variable superpotential
  `C_{n+1}(A/X)^(1/(d-1))+mX`.
- Solved the `F_X=0` equation explicitly via the auxiliary variable
  `Y=(A/X)^(1/(d-1))`.
- Derived the effective `n`-flavor ADS form, the holomorphic scale matching,
  and the coefficient recursion
  `C_n=d(C_{n+1}/(d-1))^((d-1)/d)`.
- Updated the SQCD phase-ledger status paragraph so the runaway entries cite
  both the scale-threshold proposition and the new finite-dimensional
  elimination proof.
- Extended `susy_instanton_nekr_checks.py`, the calculation-check README,
  and the Chapter 06 dossier.

## Verification

- `python3 calculation-checks/susy_instanton_nekr_checks.py`: passed.
- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed with a clean TeX log scan.
- `pdfinfo monograph/tex/main.pdf`: 1552 pages, 6135824 bytes.

## Status

This advances #592 by making the supersymmetric ADS instanton/decoupling
chain more self-contained.  It does not close #592, because the dedicated
cross-volume instanton-measure program remains open.
