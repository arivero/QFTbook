# Build Audit: Massive SQCD Konishi Source Ledger

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

- Internal monograph source: the Konishi rescaling anomaly in Volume VII
  Chapter 05 and the massive-SQCD decoupling proposition in Volume VII
  Chapter 06.
- The pass is intrinsic four-dimensional supersymmetric QFT.  No superstring,
  compactification, brane, or holographic argument is used.

## Substantive Changes

- Added a mass-source/Konishi ledger proposition for massive
  \(N_f=n<N_c\) SQCD on the same branches used for pure-SYM decoupling.
- Derived the holomorphic source identity
  `dW_eff/dm_i^j=<M^i_j>` by the finite-dimensional envelope theorem at the
  \(F_M=0\) critical point.
- Used the previously derived matrix equation
  `m_i^j = Y (M^{-1})^j_i` to prove
  `<M^a_j> m_i^j = <S> delta_i^a` and
  `m_i^j <M^i_j> = n <S>`.
- Separated this Wilsonian chiral-coordinate realization from the stronger
  regulator-level local Konishi-current identity, which belongs to the
  Chapter 05 current-anomaly framework.
- Extended the SQCD calculation check with branch, trace, dimension, and
  spurionic \(R\)-charge tests for the mass-source/Konishi ledger.

## Verification

- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py`
  passed.
- `python3 -m py_compile calculation-checks/susy_n1_sqcd_duality_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including the SQCD and pure-SYM
  checks.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.  The resulting
  `monograph/tex/main.pdf` has 1817 pages and file size 7242610 bytes.

## Status

This pass closes another common logical shortcut in the massive-SQCD route to
pure-SYM condensates.  It remains conditional on the ADS/threshold
description and does not claim a standalone operator-product theorem for the
local Konishi current.
