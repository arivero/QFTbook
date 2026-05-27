# 2026-05-26 Volume XI Lattice-Continuum Bridge Audit

## Scope

- Deepened Volume XI, Chapter 8 from a checklist into a theorem-level bridge
  between finite lattice data and continuum local QFT data.
- Added cell-average scaling maps and proved the cell-average test-function
  approximation estimate.
- Added a formal scaling-limit datum: regulator states, scaling trajectory,
  test spaces, operator maps, normalizations, and convergence topology.
- Proved a dense-test convergence criterion under uniform seminorm control.
- Added and proved the finite-graph random-walk resolvent for a massive
  lattice covariance, giving a concrete path-expansion model for the
  lattice-to-continuum estimates.
- Proved closedness of reflection positivity under entrywise convergence of
  reflected Gram matrices.
- Proved that tensor-factor locality for spin lattice algebras passes to the
  limiting GNS dense domain under convergence of local correlations, while
  keeping the gauge-theory Gauss-law/center caveat explicit.

## Calculation Checks

- Added `calculation-checks/lattice_continuum_bridge_checks.py`, which checks:
  - exact cell-average product arithmetic for \(f(x)=x\);
  - the finite-graph random-walk resolvent on the four-cycle;
  - equality between adjacency powers and enumerated path counts;
  - closedness of reflection-positive Gram matrices in a finite example;
  - tensor-product locality for disjoint spin factors.

## Verification

- `python3 calculation-checks/lattice_continuum_bridge_checks.py`
- `python3 -m py_compile calculation-checks/lattice_continuum_bridge_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build and log scan were clean.  `pdfinfo` reports
`Pages: 1846` for `monograph/tex/main.pdf`.

## Residual Work

- Interacting lattice gauge scaling limits still need a genuine construction
  of continuum local algebras with Gauss-law center choices and charged
  sectors.  The chapter now states the obstruction precisely rather than
  treating the spin-system tensor-factor argument as universal.
