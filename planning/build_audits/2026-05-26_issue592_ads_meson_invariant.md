# Build Audit: ADS Meson Determinant Invariant

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Issue focus: #592, supersymmetric instanton calculus and ADS superpotential.

## Scope

This pass strengthens the \(N_f=N_c-1\) ADS derivation in Volume VII
Chapter 06.  The previous text already contained the one-instanton zero-mode
ledger and Higgs-patch collective-coordinate count.  This pass removes a
compressed flavor-invariance step by proving the finite-dimensional
invariant-theory statement that the reduced holomorphic instanton factor on
the maximal-rank meson patch is forced to be proportional to `1/det M`.

## Source And Convention Notes

- This is QFT-internal SQCD material.  No superstring, D-brane,
  holographic, or string-compactification argument is used.
- The proof uses the monograph's SQCD meson convention
  `M^i_j = tilde Q_j Q^i`.
- The flavor action is the complexified special-flavor action
  `M -> L M R^{-1}` with `L,R in SL(N_f,C)`.
- The determinant step is separated from the analytic instanton-calculus
  hypothesis: the analytic hypothesis supplies a holomorphic reduced factor
  on `det M != 0`; the new proposition supplies the algebraic uniqueness.

## Substantive Changes

- Added Proposition `prop:ads-maximal-rank-meson-invariant`.
- Proved that `SL_n(C)_L x SL_n(C)_R` invariance makes the reduced factor
  constant on determinant fibers of `GL_n(C)`.
- Proved determinant-fiber transitivity explicitly using
  `D_delta=diag(delta,1,...,1)` and `M D_delta^{-1} in SL_n(C)`.
- Used the ADS engineering dimension to state the homogeneous scaling
  `F(sM)=s^{-n}F(M)`, then derived `F(M)=C/det M`.
- Rewrote the one-instanton ADS proof to invoke this proposition rather than
  relying on the compressed phrase that flavor invariance allows powers of
  the determinant.
- Extended `calculation-checks/susy_instanton_nekr_checks.py`, the
  calculation-check README, and the Chapter 06 dossier.

## Verification

- `python3 calculation-checks/susy_instanton_nekr_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed, including the Wolfram
  gamma-trace check.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed with a clean final log scan.
- `pdfinfo monograph/tex/main.pdf`: 1562 pages, 6175050 bytes, PDF 1.5.

## Status

This advances #592 by making a convention-sensitive algebraic step in the
ADS one-instanton derivation self-contained.  The broader instanton-measure
and cross-volume instanton-calculus program remains open.
