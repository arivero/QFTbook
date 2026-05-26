# Build Audit: Massive SQCD To Pure SYM Decoupling

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issues: #562 and #606.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Companion files:
  - `calculation-checks/susy_n1_sqcd_duality_checks.py`.
  - `calculation-checks/README.md`.
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.

## Source Leads

- Internal monograph source: the ADS superpotential and holomorphic
  decoupling recursion already developed in Volume VII Chapter 06.
- The pass is intrinsic four-dimensional supersymmetric QFT.  No superstring,
  compactification, brane, or holographic argument is used.

## Substantive Changes

- Added a finite-dimensional Wilsonian chiral-coordinate derivation of pure
  SYM branch superpotentials from massive \(N_f=n<N_c\) SQCD.
- Stated the assumptions explicitly: the standard ADS representative on the
  maximal-rank meson patch, an invertible holomorphic mass matrix, legitimate
  elimination of massive meson coordinates, and holomorphic threshold
  matching to pure SYM.
- Derived the matrix \(F_M=0\) equation
  `m_i^j = Y (M^{-1})^j_i` with
  `Y=(Lambda_n^(3N_c-n)/det M)^(1/(N_c-n))`.
- Took traces and determinants to prove
  `W_eff=N_c Y` and
  `Y^N_c=det(m) Lambda_n^(3N_c-n)=Lambda_0^(3N_c)`.
- Derived the pure-SYM branch source identity by differentiating
  `W_eff,k=N_c (Lambda_0^(3N_c))^(1/N_c) exp(2 pi i k/N_c)`.
- Extended the SQCD calculation check to verify the determinant exponent,
  branch count, critical superpotential coefficient, source identity,
  dimension, and spurionic \(R\)-charge arithmetic.

## Verification

- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py` passed.
- `python3 -m py_compile calculation-checks/susy_n1_sqcd_duality_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram Language
  gamma-trace backend.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed after the final rebase; final `main.pdf`
  has 1809 pages and size 7213262 bytes.

## Status

This pass makes one standard holomorphic-decoupling route to the pure-SYM
condensate self-contained at the chiral-coordinate level.  It remains
conditional on the ADS input and threshold assumptions and does not claim a
constructive pure-SYM mass-gap theorem.
