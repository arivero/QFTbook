# Build Audit: Issues #600, #601, #602 Assumption-Ledger Pass

Date: 2026-05-26
Branch: `codex/2d-cft-liouville-bcft-nlsm`

## Scope

- Chapter 14 BCFT:
  - Added the relation between bulk-boundary identity OPE coefficients, disk
    one-point coefficients, raised/lowered bulk two-point conventions, and
    boundary-state normalization.
  - Added finite direct sums of boundary conditions and Chan--Paton matrix
    units, including annulus multiplicity and boundary entropy scaling.
- Chapter 11 NLSM:
  - Added a finite local scheme-redefinition theorem for beta-vector fields,
    making the `beta' = beta + [beta,F]` transformation law explicit in
    condensed DeWitt notation.
- Chapter 13 Liouville:
  - Displayed the Gauss hypergeometric connection formula used in the BPZ
    degenerate-crossing argument and made its genericity/meromorphic
    continuation assumptions explicit.

## Calculation Checks

- Extended `calculation-checks/bcft_cardy_checks.py` with Chan--Paton
  direct-sum multiplicity, matrix-unit composition, and boundary-entropy
  scaling checks.
- Added `calculation-checks/nlsm_scheme_redefinition_checks.py` for the sign
  and order of the finite scheme-redefinition bracket.
- Extended `calculation-checks/liouville_bpz_checks.py` with
  hypergeometric connection-matrix exponent and gamma-argument bookkeeping.

## Required Verification

- Run the updated calculation checks, then the full
  `tools/run_calculation_checks.sh` pass before finalizing.
- Run `tools/audit_monograph_text.sh`.
- Run `tools/audit_chapter_dossiers.sh`.
- Run `git diff --check origin/main..HEAD && git diff --check`.
- Because TeX changed, run `tools/build_monograph.sh` and require a clean log
  scan.
