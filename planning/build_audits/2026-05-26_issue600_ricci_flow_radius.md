# Build Audit: Issue #600 Ricci-Flow and Radius-Flow NLSM Pass

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

## Scope

- Volume V, Chapter 11 NLSM perturbative renormalization.
- GitHub issue: #600.

## Substantive Changes

- Added a proposition identifying the one-loop metric RG equation
  `partial_{log mu} G = alpha' Ric(G)` with Hamilton Ricci flow only after
  the explicit time change `t = - alpha' log(mu)/2`.
- Stated the ultraviolet/infrared orientation carefully: increasing
  Hamilton Ricci-flow time is the infrared orientation of the sigma-model RG
  convention used in the chapter.
- Added a constant-curvature radius-flow derivation for
  `G = r^2 gamma`, with `sigma = +1` for the sphere and `sigma = -1` for the
  hyperbolic sign.
- Derived
  `d r^2/d log(mu) = (n-1) alpha' (sigma + alpha'/r^2)` and
  `d lambda/d log(mu) = -(n-1) lambda^2 (sigma + lambda)` in the two-loop
  pure-metric minimal-subtraction representative.
- Updated the Chapter 11 dossier, stringbook crosswalk, and calculation
  check inventory.

## Calculation Checks

- Extended `calculation-checks/nlsm_buscher_checks.py` with exact rational
  checks of the spherical and hyperbolic constant-curvature radius/coupling
  beta functions.

## Verification

- `python3 calculation-checks/nlsm_buscher_checks.py`
- `python3 -m py_compile calculation-checks/nlsm_buscher_checks.py`
- `python3 calculation-checks/nlsm_weyl_anomaly_checks.py`
- `python3 calculation-checks/nlsm_scheme_redefinition_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

Result: clean monograph build and log scan at 1588 pages.

## Remaining Status

Issue #600 remains open.  This pass sharpens the one-loop Ricci-flow
interpretation and supplies a two-loop constant-curvature convention check,
but the full Tseytlin-school higher-loop \(G+B+\Phi\), heterotic, and
supersymmetric renormalization program remains broader.
