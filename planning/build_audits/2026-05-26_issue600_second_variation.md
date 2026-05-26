# Build Audit: Issue #600 NLSM Second-Variation Pass

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

## Scope

- Volume V, Chapter 11 NLSM perturbative renormalization.
- GitHub issue: #600.

## Substantive Changes

- Added a self-contained second-variation proposition for the pure-metric
  sigma-model action along the geodesic variation \(X_s=\exp_x(s\xi)\).
- Fixed the punctuation in the exponential-map split paragraph from the
  previous background-field pass.
- Derived the first-variation density on a closed worldsheet:
  \(L_i=-(2\pi\alpha')^{-1}G_{ij}\nabla^a\partial_a x^j\).
- Derived the quadratic fluctuation action
  \((4\pi\alpha')^{-1}\int(|D\xi|^2-\langle R(\xi,\partial x)\partial x,\xi\rangle)\),
  including the torsion-free identity \(\nabla_sW_a=\nabla_aV\), the
  geodesic-variation identity \(\nabla_sV=0\), and the curvature convention.
- Updated the Chapter 11 dossier, stringbook crosswalk, and calculation-check
  inventory.

## Calculation Checks

- Extended `calculation-checks/nlsm_background_field_checks.py` to verify the
  pure-metric first-variation normalization, the quadratic-action
  normalization, and the sign of the curvature vertex in exact rational
  arithmetic.

## Verification

- `python3 calculation-checks/nlsm_background_field_checks.py`
- `python3 -m py_compile calculation-checks/nlsm_background_field_checks.py`
- `python3 calculation-checks/nlsm_buscher_checks.py`
- `python3 calculation-checks/nlsm_weyl_anomaly_checks.py`
- `python3 calculation-checks/nlsm_scheme_redefinition_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

Result: clean monograph build and log scan at 1590 pages.

## Remaining Status

Issue #600 remains open.  The local background-field derivation is now more
self-contained, but the full higher-loop \(G+B+\Phi\), heterotic, and
supersymmetric sigma-model renormalization program remains open.
