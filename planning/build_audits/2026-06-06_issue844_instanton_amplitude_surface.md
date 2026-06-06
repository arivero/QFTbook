# 2026-06-06 Issue #844 Instanton Amplitude Surface Pass

## Scope

- Volume II Chapter 20d, `Instantons as Physical Amplitudes`.
- Target: repair reader-facing architecture vocabulary in the chapter most
  exposed to the moduli-space-versus-physical-amplitude concern.

## Substance

- Changed visible chapter language from density gates, benchmark ledgers, and
  handoff ledgers to density normalization, channel data, hard channel
  comparison, hard amplitude assembly, and observable handoff maps.
- Kept equations and labels stable so existing cross-references still resolve.
- Renamed the visible hard-channel prefactor from `\mathcal K_{\rm gate}` to
  `\mathcal K_{\rm ch}`, emphasizing that the prefactor belongs to the chosen source,
  orientation, amputation, and projection channel.
- Updated the companion check metadata and dossier language to match the
  physical-amplitude framing.

## Quality Audit

- This pass does not add another instanton formula.  It consolidates the
  chapter's reader surface so the physical output chain is easier to see:
  fluctuation density, zero-mode/source saturation, hard-window integration,
  normal-fluctuation source response, assembled channel coefficient, and final
  observable projection.
- The monograph still preserves the theorem/status discipline through the
  existing controlled-approximation blocks and residual bounds; only the
  reader-facing architecture vocabulary changed.
- The remaining `gate`/`ledger` strings in the TeX are stable labels, not prose
  shown to readers.

## Verification

- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `tools/run_calculation_checks.sh --python-only`
- Focused theorem-form, display-label, negative-scope, and style-density
  audits for Chapter 20d
- Process-language scan on touched monograph/check files
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/build_monograph.sh`
