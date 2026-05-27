# 2026-05-27 Issue #630 TMD And GPD Operator Data

## Scope

- Upgraded Volume II, Chapter 19 around rapidity-sensitive and off-forward QCD
  light-ray observables.
- Added a TMD operator datum with transverse separation, staple Wilson-line
  orientation, finite rapidity and ultraviolet regulators, unsubtracted beam
  matrix elements, vacuum soft factors, finite-part subtraction, and the
  scales \(\mu\) and \(\zeta\).
- Proved finite-regulator gauge invariance of the subtracted TMD datum.
- Added Collins--Soper evolution and proved the mixed-derivative consistency
  relation with the lightlike cusp coefficient in the monograph trace-delta
  normalization.
- Added finite TMD scheme-change covariance and a small-\(q_\perp\)
  color-singlet TMD factorization datum, including the need to state Glauber
  status and a distributional power-remainder topology.
- Added GPD definitions as off-forward light-ray matrix elements and proved
  polynomiality of Mellin moments from local twist-two Lorentz covariance.
- Added a symbolic calculation check for the Collins--Soper algebra, TMD
  rapidity-scale cancellation, and GPD polynomiality.

## Checks

- `python3 calculation-checks/qcd_tmd_gpd_checks.py`
- `python3 -m py_compile calculation-checks/qcd_tmd_gpd_checks.py`
- `git diff --check -- ...` on the changed manuscript, calculation-check,
  README, dossier, and audit files.
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 2157 pages, 8735470 bytes, PDF 1.5.

## Status

This pass addresses the GPD/TMD part of #630 at the level of operator
definitions, regulator data, and exact evolution consistency identities.  It
does not claim a nonperturbative proof of Drell--Yan or DVCS factorization in
four-dimensional continuum QCD.
