# Issue #729 Cosmological Backreaction-Window Pass

## Scope

- Volume XII, Chapter 08: `ca:cosmology-produced-stress-backreaction-window`.
- Companion evidence: `calculation-checks/cosmological_particle_creation_checks.py`.
- Dossier/inventory updates: Ch08 dossier and calculation-check README.

## Substance

- Added a finite homogeneous FLRW window that distinguishes produced particle
  diagnostics from a usable semiclassical source.
- The retained coordinate is
  \(\Delta H_{\rm ret}^2=C_d\rho_n\), but the chapter now requires:
  scheme-consistent stress subtraction and finite counterterm transport,
  explicit vacuum/geometric/tail/gravitational response budgets, the
  continuity source \(S_n\), pressure-dependent drift control, perturbative
  smallness on the background curvature scale, and stress-noise control.
- The text explicitly rejects number-density-only, pressure-free,
  untransported-scheme, tail-free, and mean-only-noise shortcuts.
- The scope remains a finite free-field produced-stress diagnostic, not a
  proof of the full nonlinear semiclassical Einstein equation or an
  interacting cosmological QFT construction.

## Verification

Completed:

- `python3 -m py_compile calculation-checks/cosmological_particle_creation_checks.py`
- `python3 calculation-checks/cosmological_particle_creation_checks.py`
- `tools/run_calculation_checks.sh --python-only --only cosmological_particle_creation_checks`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_xii/chapter08_cosmological_spacetimes_particle_creation.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_xii/chapter08_cosmological_spacetimes_particle_creation.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xii/chapter08_cosmological_spacetimes_particle_creation.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii/chapter08_cosmological_spacetimes_particle_creation.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- metadata-leak scan for process language in touched monograph/check files
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` (clean build/log scan, 3375 pages)
