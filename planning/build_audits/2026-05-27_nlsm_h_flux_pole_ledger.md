# Build Audit: NLSM H-Flux One-Loop Pole Ledger

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 2D CFT rigor audit.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`
  - `calculation-checks/nlsm_weyl_anomaly_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.md`

## Content

This pass replaces the former prose remark on the one-loop origin of the
`H`-dependent NLSM beta-function coefficients by a proposition with explicit
local assumptions.  The new derivation states the dimensional-regularization
and epsilon-tensor convention, expands the `B`-field coupling through the
`H xi D xi dx` and `nabla H xi xi dx dx` vertices, computes the tadpole pole
for the `B` counterterm, and computes the connected bubble pole for the
metric counterterm.

The displayed counterterms are

- `delta B_ij = -alpha' nabla^k H_kij/(2 epsilon)`;
- `delta G_ij = -alpha' H_i{}^{kl}H_jkl/(4 epsilon)`.

These are the local worldsheet-pole origins of the non-dilaton
`-1/2 nabla^k H_kij` and `-1/4 H_i{}^{kl}H_jkl` coefficients in the hatted
one-loop Weyl-anomaly representatives.

## Verification

- `python3 calculation-checks/nlsm_weyl_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/nlsm_weyl_anomaly_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `c5f19ebf`, the TeX build and final log
scan completed cleanly at 1855 pages.
