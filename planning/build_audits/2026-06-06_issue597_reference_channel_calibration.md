# 2026-06-06 Issue #597 Reference-Channel Calibration Audit

## Scope

- Targeted #597 inside Vol II Ch20D, the dedicated instanton
  physical-amplitude chapter.
- Added a reference-channel determinant calibration block after the assembled
  hard-amplitude bound.
- This is a physics-amplitude pass: it clarifies how a reference physical
  channel calibrates a determinant normalization without absorbing source,
  endpoint, or projection data.

## Substance Added

- Added `ca:instanton-hard-reference-channel-calibration`.
- Defined the same-frame retained integrals \(B_\alpha,M_\alpha\) for a source
  family after center conservation, Haar projection, zero-mode overlap
  determinants, amputation residues, source window, and leading physical
  projection are included.
- Proved the exact calibration identity
  \(A_\alpha-\widehat A_\alpha=\Delta_\alpha-(B_\alpha/B_0)\Delta_0\) and the
  residual bound
  \(E_\alpha+|B_\alpha/B_0|E_0\).
- Added the reference noncancellation margin
  \(\kappa_0=|B_0|/M_0\), making nearly canceled reference channels visibly
  poor normalization coordinates.
- Kept source-dependent fluctuation quotients, endpoint tails outside the
  retained kernel, and pole/spectral/OPE bridge data either inside
  \(B_\alpha\) or in the residual \(\Delta_\alpha\).

## Quality Audit

- The pass addresses the user-requested hard instanton frontier: how
  determinant normalization and fluctuation/source data enter physical
  amplitudes, rather than adding more moduli-space infrastructure.
- The companion check builds finite reference and target channel data with
  explicit residuals and negative controls for omitted source-fluctuation
  transport, omitted physical-projection transport, rank-lost references, and
  nearly canceled references.
- The monograph TeX received only reader-facing physics content.  Planning,
  issue, monitoring, and directive material remained in planning files.
- Fresh issue monitoring showed #597 unchanged after the prior normalization
  repair.  Other freshly updated issues had already received owner repairs and
  did not conflict with this pass.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- Focused Ch20D theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

The full Python calculation suite passed; Wolfram Language checks were not
selected.  The full monograph build completed cleanly at 3457 pages.
