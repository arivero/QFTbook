# Build Audit: Buscher Dilaton Measure Ledger

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 2D CFT rigor audit.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`
  - `calculation-checks/nlsm_buscher_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.md`

## Content

This pass expands the Buscher path-integral derivation at the determinant
step.  The chapter now gives a finite cell-regulator ledger for the
`G_00`-dependent factors in the gauged first-order path integral: edge
Gaussian variables, vertex gauge-volume/Faddeev--Popov normalization, and
face multiplier/dual-scalar measure.  The net exponent is
`(N_0 - N_1 + N_2)/2 = chi(Sigma)/2`, which is exactly the path-integral
effect of the Buscher dilaton shift
`Phi -> Phi - log(G_00)/2`.

The calculation check mirrors this ledger in exact rational arithmetic for
sphere, torus, and higher-genus cell decompositions.

## Verification

- `python3 calculation-checks/nlsm_buscher_checks.py`
- `python3 -m py_compile calculation-checks/nlsm_buscher_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `c178d91a`, the TeX build and final log
scan completed cleanly at 1859 pages.
