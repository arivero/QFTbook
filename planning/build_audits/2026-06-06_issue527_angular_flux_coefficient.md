# 2026-06-06 Issue #527 Angular-Flux Coefficient Audit

## Scope

- File touched: `monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`.
- Companion evidence: `calculation-checks/charged_flux_dressing_checks.py`.
- Planning inventory: Ch05 dossier and calculation-check README.
- Target: sharpen the charged Haag--Ruelle coefficient problem by making the
  Dollard logarithmic coefficient an angular Gauss-law flux pairing, not a
  charge-only convention.

## Substance

- Added the finite angular-partition extraction formula
  `kappa_P(Gamma_i,Gamma_j)=sum_{a,b} F_i^a B_{ij}^{ab} F_j^b`.
- Recorded that total boundary charge is only the zero mode of the angular
  flux profile and cannot generally determine the long-range pair coefficient.
- Added the finite-cell coefficient-stability identity with two linear
  flux-error terms and one quadratic error term.
- Stated the theorem-level burden as uniform regulator/refinement/same-flux
  schedule control of the coefficient, with nonzero limiting coefficient error
  producing a nonintegrable `1/t` exchange term.

## Quality And Scope Judgment

- This is physics-facing scattering architecture rather than lemma-density:
  it identifies the long-range Gauss-law tail datum that a Wilson-line/Dollard
  Haag--Ruelle theorem must compute.
- It does not claim closure of the nonperturbative charged scattering theorem.
- It improves the open #527 burden by turning the symbolic `kappa` into a
  concrete angular-flux pairing target and by recording adversarial failure
  modes for charge-only shortcuts.
- The monograph TeX contains no GitHub, directive, monitoring, or planning
  language.

## Verification

- Passed: `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`.
- Passed: `python3 calculation-checks/charged_flux_dressing_checks.py`.
- Passed: focused Ch05 theorem/display/negative/style/process scans.
- Passed: `tools/run_calculation_checks.sh --python-only --only charged_flux_dressing`.
- Passed: calculation inventory and evidence-contract audits.
- Passed: chapter dossier and monograph text audits.
- Passed: full Python calculation suite; Wolfram checks were not selected.
- Passed: `tools/build_monograph.sh` at 3451 pages.
