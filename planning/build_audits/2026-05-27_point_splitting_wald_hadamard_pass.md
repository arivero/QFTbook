# 2026-05-27 Point-Splitting Hadamard/Wald Pass Audit

## Scope

- Expanded Volume XII Chapter 2 with an explicit local Hadamard subtraction
  datum for the scalar Klein--Gordon operator.
- Added the derivation of the leading Hadamard transport equation for
  \(U_H=\Delta^{1/2}\) from the Synge identities.
- Added a precise point-split stress-tensor prescription: local
  bidifferential construction, local covariance, state-dependence through the
  smooth Hadamard remainder, conservation, scaling, and flat-vacuum
  normalization.
- Added the finite local freedom formula
  \(a_0m^4g_{\mu\nu}+a_1m^2G_{\mu\nu}+a_2I_{\mu\nu}+a_3J_{\mu\nu}\), with
  \(I_{\mu\nu}\) and \(J_{\mu\nu}\) defined by metric variation of
  \(R^2\) and \(R_{\mu\nu}R^{\mu\nu}\).
- Tightened the chapter dossier and calculation-check README.
- Extended `calculation-checks/point_splitting_stress_checks.py` to verify
  the flat Synge identities and leading \(U_H\)-transport equation.

## Checks

- `python3 calculation-checks/point_splitting_stress_checks.py`: passed.
- `python3 -m py_compile calculation-checks/point_splitting_stress_checks.py`:
  passed.
- `git diff --check -- ...`: passed on all touched files in this pass.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf`: 2174 pages.
