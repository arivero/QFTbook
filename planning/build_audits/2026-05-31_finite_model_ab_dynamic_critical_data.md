# 2026-05-31 Finite Model A/B Dynamic-Critical Data

Scope: GitHub issue #703, dynamic-critical/statmech-to-QFT absorption lane.

Changes:

- Added Volume X, Chapter 10 section `Finite Data for Model A and Model B`.
- Formulated Model A/B as finite mobility-gradient stochastic field data:
  slow variable, finite free energy `F`, mobility matrix `M`, noise square
  root, and scaling-limit boundary.
- Derived the finite generator
  `Lf = -M grad F . grad f + T M : Hess f` and the Fokker--Planck current
  `J = -M(grad F p + T grad p)`.
- Proved at the finite-regulator level that the Gibbs density
  `p_eq proportional exp(-F/T)` has zero probability current on each affine
  sector.
- Defined Model A as positive local mobility and Model B as graph-incidence
  mobility `M=B^T C B`, making total-order-parameter conservation and
  divergence-form noise explicit before continuum notation.
- Wrote the finite Model A/B MSRJD action as the specialization of the
  finite-step Gaussian/Fourier identity.
- Extended `calculation-checks/nonequilibrium_open_system_checks.py` with a
  finite three-site graph check: local Model A drift/noise, symmetric
  positive Model B mobility, zero row sums, conserved drift, no constant
  noise mode, and zero Gibbs Fokker--Planck current.
- Updated the Volume X Chapter 10 dossier, calculation-check README,
  statmech crosswalk, and active review ledger.

The pass avoids treating Hohenberg--Halperin labels as theorem labels.
Dynamic exponents, scaling functions, and continuum stochastic fixed points
remain theorem-boundary outputs of a regulator/RG construction.

Verification:

- `python3 -m py_compile calculation-checks/nonequilibrium_open_system_checks.py`
- `python3 calculation-checks/nonequilibrium_open_system_checks.py`
- `git diff --check`
- `tools/build_monograph.sh`

The monograph build is clean at 2764 pages.
