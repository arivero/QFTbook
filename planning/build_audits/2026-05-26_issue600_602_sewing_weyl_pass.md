# Build Audit: Issues #600 and #602, BCFT Sewing and NLSM Weyl-Anomaly Pass

Date: 2026-05-26

Branch: `codex/2d-cft-liouville-bcft-nlsm`

Worktree: `/Users/xiyin/QFT_2d_cft`

## Scope

- Deepened Volume V Chapter 14 by adding explicit rational BCFT sewing
  hypotheses, boundary-condition-changing OPE coefficients, the
  Cardy--Lewellen four-boundary-field sewing equation, the diagonal Cardy
  boundary-field multiplicity statement, and the corrected fusion-ring
  character normalization for disk one-point data.
- Deepened Volume V Chapter 11 by adding the one-loop Weyl-anomaly
  variational package for \((G,B,\Phi)\), including the \(B\)-field
  integration-by-parts derivation, the \(H^2\) metric coefficient, the scalar
  anomaly representative, the heterotic Green--Schwarz \(H\)-field package,
  the heterotic gauge beta representative, and the \(\mathcal N=(2,2)\)
  Kähler one-loop beta tensor.
- Added `calculation-checks/nlsm_weyl_anomaly_checks.py`.
- Extended `calculation-checks/bcft_cardy_checks.py`.
- Updated Volume V chapter dossiers for Chapters 11 and 14.

## Local References Consulted

- `references/02_2d_cft/frs_tft1_hep-th-0204148/hep.tex`
- `references/02_2d_cft/frs_tft4_hep-th-0412290/IV.tex`
- `references/02_2d_cft/duality_invariant_beta_2103_15931/Beta_functions_duality_BCH_JHEP.tex`

These ignored local TeX references were used to check theorem boundaries and
coefficient conventions.  The monograph text does not quote them at length;
it gives local derivations where feasible and marks the all-surface rational
sewing and higher-loop supersymmetric sigma-model results as theorem/status
boundaries.

## Verification To Run

- `python3 calculation-checks/bcft_cardy_checks.py`
- `python3 calculation-checks/nlsm_weyl_anomaly_checks.py`
- `python3 calculation-checks/nlsm_buscher_checks.py`
- `python3 calculation-checks/liouville_bpz_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check origin/main..HEAD`
- `tools/build_monograph.sh`
