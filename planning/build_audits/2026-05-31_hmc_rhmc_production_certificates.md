# 2026-05-31 HMC/RHMC Production Certificates

## Scope

Continued the Volume XI numerical-evidence development under #631 and #703.
The existing HMC/RHMC section already proved the exact finite
detailed-balance, leapfrog, pseudofermion determinant, and rational-action
identities.  This pass adds the next production layer: finite solver,
reversibility, rationalization, and reweighting certificates that must be
recorded before HMC/RHMC outputs are used as QFT evidence.

## Manuscript Changes

- Expanded `monograph/tex/volumes/volume_xi/chapter06_monte_carlo_and_sign_problems.tex`.
- Added finite diagnostics for HMC/RHMC runs:
  `Delta H`, `Delta_rev`, and `rho_lin`.
- Derived the residual bound for the pseudofermion action,
  `|phi^* A^{-1} phi - phi^* x| <= lambda_-^{-1} ||phi|| ||r||`.
- Derived the finite force-error bound controlled by
  `||dot A||`, the solver residual, and the spectral lower bound.
- Derived the RHMC determinant reweighting coordinate
  `W_rat=det(A)^alpha det r_m(A)` and
  `|log W_rat| <= N eta_*`.
- Added the public-facing finite HMC/RHMC smoke module
  `qft_scripts/hmc_rhmc_finite_demo.py` and wired it into the smoke harness.

## Companion Checks

- Extended `calculation-checks/hmc_pseudofermion_checks.py` to verify:
  - the linear-solver pseudofermion-action residual bound;
  - the linear-solver pseudofermion-force residual bound;
  - the RHMC determinant reweighting log bound;
  - the new HMC/RHMC finite smoke module and rational action helpers.
- Updated `calculation-checks/README.md`, `qft_scripts/README.md`,
  the Volume XI Chapter 6 dossier, and the statmech crosswalk.

## Theorem-Form Note

No new theorem-family environment was introduced.  The new material is finite
algorithmic proof infrastructure and is presented as derivational prose with
numbered estimates.  This avoids inflating diagnostics into theorems while
still making the mathematical bounds explicit.

## Verification

- `python3 qft_scripts/hmc_rhmc_finite_demo.py --smoke`
- `python3 calculation-checks/hmc_pseudofermion_checks.py`
- `python3 -m py_compile qft_scripts/hmc_rhmc_finite_demo.py calculation-checks/hmc_pseudofermion_checks.py`
- `bash -n tools/run_qft_scripts_smoke.sh`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/run_qft_scripts_smoke.sh`
- `tools/build_monograph.sh`

Full monograph build clean at 2747 pages.
