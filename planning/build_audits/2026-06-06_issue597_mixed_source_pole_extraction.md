# Issue #597 Mixed-Source Pole Extraction Pass

## Scope

- Added `ca:instanton-pole-normalized-four-source-extraction` to
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- The pass targets physical amplitude extraction, not ADHM or moduli-space
  expansion: a Euclidean instanton four-source window becomes a hadronic
  matrix element only after full overlap-matrix pole amputation, source mixing
  control, and a residual bound for excited-state/continuum leakage.
- Extended
  `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  with an exact finite mixed-source matrix-amputation check.  The negative
  controls reject raw-kernel extraction, diagonal-overlap division, rank-lost
  source bases, and determinant constants used to absorb pole leakage.
- Updated `calculation-checks/README.md` and the Vol II Ch20D dossier.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- Focused Ch20D theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits.
- Ch20D process/directive scan: no new planning/directive/review text in the
  monograph TeX; remaining `gate`/`ledger` hits are existing labels.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- Full `tools/run_calculation_checks.sh --python-only`
- Full `tools/build_monograph.sh`, clean at 3462 pages.

## Re-Audit

This is an amplitude-facing development.  It closes part of the gap between
source-functional instanton coefficients and physical QFT amplitudes by
making pole isolation and mixed-source LSZ-style amputation explicit.  It does
not claim to compute the continuum determinant constant or prove the full
Lorentzian scattering theorem.
