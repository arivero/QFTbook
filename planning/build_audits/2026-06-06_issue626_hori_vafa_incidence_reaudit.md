# 2026-06-06 Issue #626 Hori--Vafa Incidence Re-Audit

## Scope

- Target: Volume VII Chapter 09, the protected
  \(\mathbb P^{N-1}\) GLSM/Hori--Vafa residue and direct A-model/vortex
  comparison.
- Related issues: #626 Vol VII depth-pass-B and #597 instanton physics depth.
- Companion: `calculation-checks/susy_2d_lg_glsm_checks.py`.

## Substance Audit

- The existing comparison correctly warned that the Hori--Vafa mirror residue
  is not the regulated vortex/A-model path integral.  However, the companion's
  Hori--Vafa comparison still represented the retained direct measure integral
  as a chosen near-unit scalar.
- This pass makes the direct side more independent: the degree-one
  projective-space incidence package is computed before the mirror comparison.
  The direct package includes the incidence orientation determinant, the
  insertion-degree gate, the compactification exclusion gate, and the operator
  normalization.
- The monograph now states that \(I_{\Lambda,1}=1+R_{\rm meas}\) only after
  those finite direct gates, the determinant-line orientation, zero-mode
  measure, compactification/contact convention, and operator normalization
  have been transported to the same regulator.

## Negative Controls Added

- A mirror residue with the transported \(q\) does not hide a flipped direct
  incidence orientation.
- A mirror residue does not bypass a failed compactification gate.
- The existing stale-FI, zero-mode, line-count-only, orientation-flip, and
  off-pairing controls remain active in the same comparison.

## Scope Boundary

- This is a protected finite comparison for the degree-one
  \(\mathbb P^{N-1}\) observable.  It does not prove Hori--Vafa mirror
  equivalence as a full continuum QFT statement, does not derive the vortex
  fluctuation spectra from first principles, and does not close the broader
  Vol VII depth-pass issue.

## Verification Results

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
  passed.
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
  passed.
- Focused Chapter 09 audits passed:
  `audit_theorem_form.py`, `audit_unnumbered_display_labels.py`,
  `audit_negative_scope_prose.py --fail`, and
  `audit_style_density.py --fail`.
- Repository audits passed: `tools/audit_chapter_dossiers.sh`,
  `tools/audit_monograph_text.sh`,
  `tools/audit_calculation_check_inventory.py`, and
  `tools/audit_calculation_evidence_contracts.py`.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- Full `tools/build_monograph.sh` passed; `main.pdf` built cleanly at
  3404 pages.
- `git diff --check` passed after this audit note was finalized.
