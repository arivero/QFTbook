# Build Audit: SQCD Conformal-Window Central Charges

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Issue focus: #588, with overlap for #605's four-dimensional `N=1` gauge
dynamics foundation.

## Scope

This pass strengthens Volume VII Chapter 06 in the superconformal SQCD
bookkeeping section.  The chapter already derived the candidate
superconformal \(R\)-charge and meson unitarity-bound test.  This pass adds
the associated \(a,c\) anomaly calculation and a conditional comparison of
the free ultraviolet \(a\)-value with the candidate infrared SCFT value.

## Source And Convention Notes

- This is a field-theoretic anomaly calculation inside four-dimensional
  supersymmetric QFT.
- No superstring, compactification, D-brane, or holographic derivation is
  used.
- The calculation is explicitly conditional on the chapter's SCFT-input
  hypothesis: the infrared fixed point, chiral-primary status, and correct
  superconformal \(R\)-current are assumptions being tested, not proved.
- The comparison is not presented as a proof of a general \(a\)-theorem or
  of RG-flow existence.  The monograph records only the finite anomaly
  arithmetic under stated hypotheses.

## Substantive Changes

- Added the SQCD central-charge bookkeeping calculation.
- Derived the SQCD superconformal traces
  `Tr R=-N_c^2-1` and `Tr R^3=N_c^2-1-2N_c^4/N_f^2`.
- Derived the corresponding central charges using the \(N=1\) formulas
  `a=(3/32)(3 Tr R^3-Tr R)` and
  `c=(1/32)(9 Tr R^3-5 Tr R)`.
- Computed the free ultraviolet value
  `a_UV=3(N_c^2-1)/16+N_c N_f/24`.
- Factored
  `a_UV-a_IR=N_c^2(3-y)^2(2y+3)/(48y^2)` with `y=N_f/N_c`,
  recording positivity in `3/2<y<3` and equality at the Gaussian edge as a
  consistency check, not as a proof of monotonicity.
- Extended `susy_n1_sqcd_duality_checks.py`, the calculation-check README,
  and the Chapter 06 dossier.

## Verification

- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed with clean TeX log scan.
- `pdfinfo monograph/tex/main.pdf`: 1557 pages, 6156078 bytes.

## Status

This advances the supersymmetric gauge-theory foundation requested in #588
and supports the #605 SQCD/conifold cascade material.  It closes no issue by
itself.
