# 2026-06-07 Issue #597 Normal-Propagator Insertion Pass

## Scope

- Target issue: #597, instantons as physical amplitudes rather than
  moduli-space-only infrastructure.
- Monograph target:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Inserted `ca:instanton-normal-propagator-source-insertion` in the
  normal-fluctuation section.

## Quality Audit

- This pass does not add ADHM or moduli-space geometry.  It adds the
  source-facing Green-function part of the fluctuation calculation: an
  instanton-background nonzero-mode propagator is projected away from zero
  modes, paired with amputated source vectors, and multiplied by the zero-mode
  determinant only after the bilinear has been formed.
- The block separates five data types that are often collapsed in compressed
  instanton expositions: determinant constant, determinant trace response,
  zero-mode source determinant, full source-overlap amputation, and the
  primed Green-operator bilinear.
- The residual bound is absolute and channel-facing.  It rejects the idea that
  a moduli density times a determinant constant controls the physical
  spectator-pair insertion.
- Directive and issue-tracking material remains in planning files, not in the
  monograph TeX.

## Verification

- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed before documentation staging.
- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`.
- Ch20D theorem/display/prose/negative-scope/style/text audits.
- Zero-match TeX scan for directive, review, issue, and monitoring terms.
- `python3 tools/audit_calculation_evidence_contracts.py`.
- `python3 tools/audit_calculation_check_inventory.py`.
- `tools/audit_chapter_dossiers.sh`.
- `git diff --check`.
- Full `tools/run_calculation_checks.sh --python-only`.
- Full `tools/build_monograph.sh`, clean log scan, producing
  `monograph/tex/main.pdf`.
