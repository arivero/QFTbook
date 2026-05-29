# Build Audit: Pure SYM VY Glueball Ledger

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Issue focus: #588, with foundational support for the Chapter 06 `N=1` gauge
dynamics spine.

## Scope

This pass strengthens the pure `SU(N_c)` supersymmetric Yang--Mills portion
of Volume VII Chapter 06.  The previous text stated the gaugino condensate
and its `N_c` phases compactly.  The revised text separates the anomaly
calculation, the glueball \(F\)-term hypothesis, the VY superpotential
derivation, and the Witten-index consistency check.

## Source And Convention Notes

- This is entirely QFT-internal.  No superstring, compactification, D-brane,
  or holographic argument is used.
- The trace and instanton-index convention is the Chapter 06 convention:
  `T(adj)=N_c`, so the adjoint Weyl anomaly coefficient is `2N_c`.
- The glueball coordinate is
  `S=-(1/(32 pi^2)) tr(W^alpha W_alpha)`.
- The VY derivation is stated under an explicit Wilsonian chiral-sector
  hypothesis.  It is not presented as a constructive proof of confinement or
  a mass gap.

## Substantive Changes

- Added the pure-SYM discrete chiral-anomaly derivation, later demoted from
  proposition form to prose while retaining the anomalous reduction to
  `Z_{2N_c}` and the condensate breaking `Z_{2N_c}->Z_2`.
- Added Hypothesis `hyp:pure-sym-glueball-f-term-description`, stating the
  one-coordinate glueball \(F\)-term assumptions, source normalization, and
  finite-normalization caveat.
- Added the VY glueball-superpotential derivation, deriving the standard
  VY representative
  `S(log(Lambda_h^(3N_c)/S^N_c)+N_c)` from the dimensionless holomorphic
  ratio and the source identity.
- Derived the critical equation `S^N_c=Lambda_h^(3N_c)`, the `N_c` relative
  condensate phases, and the nonzero Hessian in the glueball coordinate.
- Added `calculation-checks/susy_n1_pure_sym_checks.py` and updated the
  calculation-check README and Chapter 06 dossier.

## Verification

- `python3 calculation-checks/susy_n1_pure_sym_checks.py`: passed.
- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed with a clean TeX log scan.
- `pdfinfo monograph/tex/main.pdf`: 1554 pages, 6142790 bytes.

## Status

This advances #588 by making the pure `N=1` gauge dynamics foundation more
self-contained.  It closes no issue by itself.
