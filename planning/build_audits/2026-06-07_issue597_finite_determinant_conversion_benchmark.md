# 2026-06-07 Issue #597 Finite Determinant Conversion Benchmark

## Scope

- Responds to the review that the previous finite determinant scheme-transport
  block tested covariance typing but did not independently compute a determinant
  conversion.
- Keeps directive and review bookkeeping in planning material; the TeX chapter
  carries only the mathematical and physical content.

## Changes

- Demoted the old Ch20D finite determinant transport block to
  `rem:instanton-finite-determinant-scheme-transport-architecture`.
  It now states explicitly that choosing action/orientation/gamma multipliers
  and defining \(C_{{\mathcal S}'}^{\rm inst}\) from the transport identity is
  not a Pauli--Villars-to-\(\overline{\rm MS}\), or other named continuum,
  determinant conversion.
- Added `ca:instanton-finite-determinant-conversion-benchmark`, a finite
  regulator benchmark which computes two universal determinant densities before
  source projection.  The benchmark retains action weight, \(x^{2N_c}\), the
  orientation volume, the bosonic zero-mode Jacobian, and the zero-mode-deleted
  determinant ratio.
- Added `check_finite_determinant_conversion_benchmark()` to the instanton
  companion.  It verifies the independent density ratio \(50176/50625\), the
  residual in a fixed source channel, the inverse matching factor, and negative
  controls for determinant-constant-only and omitted-factor shortcuts.
- Updated the calculation README and Ch20D dossier so the evidence boundary is
  recorded as architecture plus finite benchmark, not continuum determinant
  normalization closure.

## Quality Re-Audit

- Physics scope: the change keeps the focus on instanton amplitudes rather than
  moduli geometry.  It asks what data have to be integrated into a physical
  determinant density before a source channel or amplitude matching statement is
  meaningful.
- Evidence boundary: the benchmark is deliberately finite.  It closes the review
  complaint about a tautological transport identity, but it does not claim a
  continuum Pauli--Villars/\(\overline{\rm MS}\) conversion.
- Coherence: the new block follows the reference-channel calibration and
  precedes physical projection, so it remains part of the amplitude-assembly
  architecture rather than a free-standing lemma annex.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `bash tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `bash tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
