# Volume XI Continuum Limits Deepening Audit

## Scope

This pass addresses the later-volume thinness directive for Volume XI,
Chapter 4.  The chapter is rewritten from a short conceptual sketch into a
definition-and-derivation treatment of regulated families, Schwinger
distributional limits, scaling trajectories, free lattice scalar continuum
limits, scaling windows, operator coordinates, contact terms, OS targets,
and Wilsonian scaling manifolds.

## Edits

- Rewrote
  `monograph/tex/volumes/volume_xi/chapter04_continuum_limits_scaling_windows.tex`.
- Defined regulated expectation functionals, scaling trajectories, and
  renormalized smeared lattice observables.
- Stated continuum Schwinger limits as distributional limits in a specified
  topology.
- Added a worked free massive lattice scalar example with the lattice action,
  Brillouin-zone covariance, Poisson-summation proof of continuum covariance
  convergence, and Gaussian higher-point convergence.
- Derived the exact free lattice pole mass
  \(\kappa_a=2a^{-1}\operatorname{arcsinh}(am_a/2)\), the lattice
  correlation length, and the continuum physical correlation length.
- Clarified scaling windows for massive and scale-invariant limits.
- Added operator-coordinate and contact-term bookkeeping through finite Wick
  subtraction shifts.
- Strengthened the OS reconstruction target, including reflection positivity
  as a closed-cone limit and the need for growth bounds.
- Derived \(\nu=1/y_t\) from a one-relevant-coordinate Wilsonian chart with
  stable irrelevant directions.
- Clarified the distinct statuses of constructive \(\phi^4_3\), the 3D
  Ising CFT, and four-dimensional \(\phi^4_4\).
- Added `calculation-checks/continuum_scaling_window_checks.py` and
  documented it in `calculation-checks/README.md`.
- Rewrote the Volume XI Chapter 4 dossier.

## Verification

- `python3 calculation-checks/continuum_scaling_window_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; the generated
  `monograph/tex/main.pdf` has 1330 pages.
