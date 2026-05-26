# Build Audit: Issue #583 BV Deepening

Date: 2026-05-26.

## Scope

- Expanded `monograph/tex/volumes/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.tex`.
- Expanded `monograph/tex/volumes/volume_viii/chapter10_bv_integration_and_localization.tex`.
- Added `calculation-checks/bv_master_algebra_checks.py`.
- Extended `calculation-checks/bv_localization_checks.py`.
- Updated BV chapter dossiers and calculation-check documentation.

## Mathematical Content

- Added a finite-regulator infinitesimal exact-RG theorem:
  \(\partial_t\rho_t=\Delta_{1/2}(R_t\rho_t)\) preserves the QME and gives
  \(\partial_tS_t=(S_t,R_t)-i\hbar\Delta R_t\).
- Added the local BV--BRST comparison theorem for gauge-fixed Yang--Mills with
  stated Koszul--Tate acyclicity and boundary hypotheses.
- Added a renormalizable ghost-number-zero cohomology ledger for gauge and
  matter counterterms in the monograph trace/coupling convention.
- Added the ghost-number-one perturbative gauge-anomaly ledger from the
  descent of \((i/24\pi^2)\operatorname{Tr}_R\mathsf F^3\).
- Added the regulated local-observable/factorization-algebra boundary:
  \(\operatorname{Obs}_\Lambda(U)\), the quantum BV differential
  \(Q_\Lambda=(S_\Lambda,\cdot)-i\hbar\Delta_\Lambda\), disjoint-support
  products, and homotopy-RG cochain maps.
- Added the compact \(S^2\) Atiyah--Bott fixed-point model to the finite
  BV/localization chapter.

## Verification Plan

- `python3 calculation-checks/bv_master_algebra_checks.py`
- `python3 calculation-checks/bv_localization_checks.py`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

The final verification outputs should be recorded in the commit or issue
comment after the checks run.
