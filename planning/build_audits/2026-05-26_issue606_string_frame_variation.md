# Build Audit: Issue #606 String-Frame NLSM Variation Pass

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

## Scope

- Volume V, Chapter 11 NLSM Weyl-anomaly and string-frame variational
  package.
- GitHub issue: #606 stringbook-depth meta-audit.

## Substantive Changes

- Expanded the one-loop string-frame target-space functional derivation so
  the fixed-dilaton metric variation is displayed before passing to the
  hatted beta-function representative.
- Defined the tensors
  `E_ij = R_ij + 2 nabla_i nabla_j Phi - H_i{}^{kl}H_jkl/4`
  and
  `S_Phi = R + 4 nabla^2 Phi - 4 |grad Phi|^2 - H^2/12`
  and proved that the full metric variation is
  `E_ij - G_ij S_Phi/2`.
- Derived the dilaton variation as `-2 S_Phi` after integration by parts
  with the `sqrt(G) exp(-2 Phi)` density.
- Made explicit that the scalar equation removes exactly the trace part of
  the fixed-dilaton metric variation, leaving the chosen hatted metric
  Weyl-anomaly representative.
- Updated the Chapter 11 dossier, stringbook crosswalk, and calculation-check
  inventory.

## Calculation Checks

- Extended `calculation-checks/nlsm_weyl_anomaly_checks.py` to verify the
  string-frame metric trace decomposition, cancellation of the nontrace
  `grad_i Phi grad_j Phi` term, and scalar dilaton variation coefficients in
  exact rational arithmetic.

## Verification

- `python3 calculation-checks/nlsm_weyl_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/nlsm_weyl_anomaly_checks.py`
- `python3 calculation-checks/nlsm_background_field_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

Result: clean monograph build and log scan at 1767 pages.

## Remaining Status

Issue #606 remains open.  This pass closes another local derivation gap in
the NLSM part of the shared stringbook-depth program, but the global audit is
broader than this single variational calculation.
