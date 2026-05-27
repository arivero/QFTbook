# Build Audit: ADS Yukawa Lifting Berezin Determinant

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issues: #562, #597, and #606.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Companion files:
  - `calculation-checks/susy_instanton_nekr_checks.py`.
  - `calculation-checks/README.md`.
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.

## Source Leads

- Internal monograph source: the BPST instanton normalization in Volume II
  and the `N_f=N_c-1` SQCD one-instanton ADS derivation in Volume VII
  Chapter 06.
- The pass is intrinsic supersymmetric gauge theory.  No superstring,
  compactification, brane, or holographic argument is used.

## Substantive Changes

- Added a finite-dimensional diagonal-patch Berezin determinant proposition
  for the Yukawa lifting matrix in the `N_f=N_c-1` SQCD instanton.
- Proved explicitly that the block action
  `sum_i a_i chi_i zeta_i + b_i tilde chi_i tilde zeta_i` saturates all
  lifted matter and non-Goldstino adjoint Grassmann coordinates.
- Recorded that the block determinant is nonzero precisely on `det M != 0`
  and leaves exactly the two Goldstino coordinates used as the `d^2 theta`
  superpotential measure.
- Separated the anti-holomorphic lifting determinant from the final
  holomorphic ADS denominator, which still depends on the regulated measure,
  the Higgs cutoff, and the holomorphic `F`-term hypothesis.
- Extended the SUSY instanton calculation check with bilinear-count,
  Grassmann-saturation, Goldstino, determinant-degree, and coefficient
  factorization tests.

## Verification

- `python3 calculation-checks/susy_instanton_nekr_checks.py` passed.
- `python3 -m py_compile calculation-checks/susy_instanton_nekr_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram gamma-trace
  check.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- Output PDF metadata after the build: 1824 pages, 7273042 bytes.

## Status

This pass replaces another compressed instanton-calculus step by an explicit
finite-dimensional computation.  It does not claim a complete mathematical
construction of the instanton measure or remove the analytic hypotheses
already stated for the ADS one-instanton calculation.
