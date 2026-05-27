# Build Audit: Parafermion Orbit Modular Data

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 2D CFT rigor audit.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`
  - `calculation-checks/wzw_sugawara_coset_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.md`

## Content

This pass strengthens the compact `SU(2)_k/U(1)` parafermion coset modular
data.  The chapter now proves that the displayed orbit-level modular
`S`-matrix is unitary after the fixed-point-free simple-current quotient and
that the Verlinde formula recovers exactly the truncated `SU(2)_k` fusion
rule together with `U(1)` charge conservation.  The calculation check now
tests the orbit `S`-matrix unitarity and Verlinde coefficients directly for
small levels, in addition to the existing exact rational checks for
selection rules, weights, and fusion.

## Verification

- `python3 calculation-checks/wzw_sugawara_coset_checks.py`
- `python3 -m py_compile calculation-checks/wzw_sugawara_coset_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `d89f6fa6`, the TeX build and final log
scan completed cleanly at 1863 pages.
