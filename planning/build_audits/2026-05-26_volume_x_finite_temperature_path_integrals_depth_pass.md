# Build Audit: Volume X Finite-Temperature Path Integrals Depth Pass

## Scope

- Branch: `main`.
- Files edited:
  - `monograph/tex/volumes/volume_x/chapter02_finite_temperature_path_integrals.tex`
  - `planning/chapter_dossiers/volume_x/chapter02_finite_temperature_path_integrals.md`
  - `calculation-checks/finite_temperature_path_integral_checks.py`
  - `calculation-checks/README.md`

## Substantive Changes

- Added a regulator-level definition of the thermal path-integral notation,
  separating finite trace-class operator data from any continuum limiting
  procedure.
- Made explicit that fermionic path-integral variables at finite regulator are
  generators of a Grassmann algebra and that Berezin integration is a linear
  functional, not a Borel measure.
- Added a finite Berezin-integral definition with the sign convention
  compatible with the coherent-state identity.
- Expanded the proof of the one-mode fermionic coherent-state trace identity
  so the ordinary trace and graded trace signs are derived rather than
  asserted.
- Added a trace-gluing figure showing the periodic bosonic and ordinary
  thermal antiperiodic fermionic spin structures on \(S^1_\beta\).
- Extended the public finite-temperature calculation check to verify the
  one-mode coherent-state trace sign.

## Verification Plan

- `python3 calculation-checks/finite_temperature_path_integral_checks.py`
- `python3 -m py_compile calculation-checks/finite_temperature_path_integral_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
