# 2026-05-26 Volume XII Hawking Effect Depth Pass

## Scope

- Rewrote `monograph/tex/volumes/volume_xii/chapter05_hawking_effect.tex`
  into a fixed-background Hawking-effect derivation organized by horizon
  geometry, Euclidean regularity, collapse ray tracing, wave-packet
  Bogoliubov mixing, two-dimensional flux, greybody propagation, and
  semiclassical boundary conditions.
- Added the definition of a Killing horizon and the surface-gravity
  convention `chi^nu nabla_nu chi^mu = kappa chi^mu`.
- Proved the Rindler normal form for a nonextremal horizon and checked the
  Schwarzschild normalization `kappa=1/(4M)`, `T_H=1/(8 pi M)`.
- Reframed Euclidean regularity as a conditional KMS conclusion, separating
  it from the collapse-state theorem.
- Added a late-time ray-tracing lemma deriving
  `v_0-v = C exp(-kappa u) + O(exp(-2 kappa u))` from regular Kruskal data.
- Preserved and deepened the singular Bogoliubov coefficient calculation.
- Added wave-packet observables, the packet occupation proposition, and the
  exact Planck-bin average.
- Added the two-dimensional Schwarzian flux computation and matched it to the
  chiral Planck energy flux.
- Added the trans-Planckian precursor-frequency estimate as a
  domain-of-validity statement.
- Expanded the discussion of Boulware, Hartle-Hawking, and Unruh states as
  state-selection properties requiring construction in each model.
- Added the Schwarzschild scalar radial equation, greybody transmission
  factors, number/energy flux formulae, and a precise semiclassical
  back-reaction boundary.
- Updated the Volume XII Chapter 5 dossier and calculation-check README.

## Calculation Check

- Extended `calculation-checks/hawking_bogoliubov_checks.py`.
- New checks cover the wave-packet Planck-bin average, the exponential-map
  Schwarzian derivative, the equality of Schwarzian and chiral Planck fluxes,
  and the Schwarzschild temperature convention.
- The check also continues to verify the Gamma-function norm, thermal
  `alpha/beta` ratio, negative-frequency density, continuum normalization
  density, and precursor blueshift.

## Verification

- `python3 calculation-checks/hawking_bogoliubov_checks.py`
  - Passed: `All Hawking Bogoliubov coefficient checks passed.`
- `python3 -m py_compile calculation-checks/hawking_bogoliubov_checks.py`
  - Passed.
- `tools/audit_chapter_dossiers.sh`
  - Passed.
- `git diff --check`
  - Passed.
- `tools/build_monograph.sh`
  - Passed with a clean log scan.
- `pdfinfo monograph/tex/main.pdf`
  - Pages: 1826.

## Residual Work

- Add a collapse Penrose diagram showing `I^-`, `I^+`, the last escaping ray
  `v_0`, the future horizon, and the exponential relation between `u` and
  `v`.
- A later theorem pass should sharpen the interacting Hawking open problem
  against concrete constructions of Hadamard Unruh states on collapse
  backgrounds.
