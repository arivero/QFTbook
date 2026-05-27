# Build Audit: Issue #606 NLSM Heat-Kernel Pole Pass

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

## Scope

- Volume V, Chapter 11 NLSM perturbative renormalization.
- GitHub issue: #606 stringbook-depth meta-audit.

## Substantive Changes

- Rebased the lane branch onto latest `origin/main` before editing.
- Expanded the pure-metric one-loop Ricci-divergence proof so the local
  coincident Green-kernel pole is derived rather than quoted.
- Added the frozen-background local frame, the kinetic operator
  `(-partial^2)/(2 pi alpha')`, the auxiliary-mass heat-kernel integral, and
  the pole
  \((-\partial^2)^{-1}(\sigma,\sigma)_{\mathrm{div}}=(2\pi\epsilon)^{-1}\).
- Derived the fluctuation contraction
  \(\langle\xi^k\xi^\ell\rangle_{\mathrm{div}}=
  \alpha'G^{k\ell}/\epsilon\), the sign from
  \(-\log\langle e^{-S_{\mathrm{curv}}}\rangle\), and the resulting
  minimal-subtraction counterterm
  \(\delta G_{ij}=(\alpha'/\epsilon)R_{ij}\).
- Updated the Chapter 11 dossier, stringbook crosswalk, and calculation-check
  inventory.

## Calculation Checks

- Extended `calculation-checks/nlsm_background_field_checks.py` to verify the
  heat-kernel residue, kinetic prefactor, one-loop Ricci divergence sign,
  minimal-subtraction metric counterterm coefficient, and a finite Ricci
  contraction model in exact rational arithmetic.

## Verification

- `python3 calculation-checks/nlsm_background_field_checks.py`
- `python3 -m py_compile calculation-checks/nlsm_background_field_checks.py`
- `python3 calculation-checks/nlsm_buscher_checks.py`
- `python3 calculation-checks/nlsm_weyl_anomaly_checks.py`
- `python3 calculation-checks/nlsm_scheme_redefinition_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

Result: clean monograph build and log scan at 1766 pages.

## Remaining Status

Issue #606 remains open.  This pass strengthens one local NLSM derivation
inside the stringbook-depth program; the global shared-topic audit is broader.
