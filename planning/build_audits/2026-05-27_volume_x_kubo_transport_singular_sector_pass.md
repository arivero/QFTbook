# Build Audit: Volume X Kubo Transport Singular-Sector Pass

## Scope

- Branch: `main`.
- Files edited:
  - `monograph/tex/volumes/volume_x/chapter04_spectral_functions_kubo_transport.tex`
  - `planning/chapter_dossiers/volume_x/chapter04_spectral_functions_kubo_transport.md`
  - `calculation-checks/thermal_kubo_checks.py`
  - `calculation-checks/README.md`

## Substantive Changes

- Added a formal transport-limit datum specifying the regulator sequence,
  operator normalization, contact/projection prescription, and order of
  thermodynamic, momentum, and zero-frequency limits.
- Added a zero-frequency singular-sector discussion before conductivity,
  emphasizing that finite dc transport is not a finite-volume operation.
- Proved a finite-volume Mazur projection bound using the real symmetrized
  thermal inner product on Hermitian operators.
- Defined the Drude-weight normalization in the chapter's
  fluctuation--dissipation convention and separated it from the regular dc
  dissipative slope.
- Added a figure showing the required order of limits and prior separation
  of conserved singular sectors.
- Extended the public Kubo calculation check to verify the finite Mazur
  projection and Drude-weight normalization in a two-level example.

## Verification Plan

- `python3 calculation-checks/thermal_kubo_checks.py`
- `python3 -m py_compile calculation-checks/thermal_kubo_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

## Verification Results

- `python3 calculation-checks/thermal_kubo_checks.py`: passed.
- `python3 -m py_compile calculation-checks/thermal_kubo_checks.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed, including final log scan.
- Generated PDF: `monograph/tex/main.pdf`, 1946 pages.
