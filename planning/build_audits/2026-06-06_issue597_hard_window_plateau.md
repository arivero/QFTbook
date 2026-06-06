# Issue #597 hard instanton window plateau

Date: 2026-06-06

## Scope

This pass addresses the instanton-physics depth concern by developing the
hard four-fermion amplitude extraction rather than adding moduli-space
infrastructure.  The new block in Volume II, Chapter 20 turns the leading
individual-slot endpoint coefficient into an operational two-cutoff plateau
test for the source-amputated instanton coefficient.

The manuscript insertion is
`ca:instanton-tail-subtracted-hard-window-plateau`.  It sits after
`prop:individual-slot-instanton-tail-subtraction` and before the finite-window
bound, so the flow is:

- compute the individual-slot endpoint coefficient \(A_{\rm ind}\);
- subtract \(3A_{\rm ind}R^{-1/3}\) from the retained hard window;
- compare two accelerated windows against the \(R^{-7/3}\) residual bound;
- propagate determinant, zero-mode/source, source-fluctuation, Schur,
  matching, projection, and endpoint residuals to the accelerated coefficient;
- retain the noncancellation margin before making a relative amplitude claim.

This keeps the physical amplitude object in view: source projection,
orientation, form factors, fluctuation determinant, and finite-window residuals
are all part of the quoted coefficient.

## Evidence Companion

`calculation-checks/bpst_instanton_normalization_checks.py` now includes
`check_tail_subtracted_hard_window_plateau()`.  The check uses the exact
rational variable \(u=R^{-1/3}\) to verify:

- \(J_R^{\rm acc}=J_\infty-(3/7)B_{\rm ind}u^7\);
- two-window plateau drift equals the residual interval integral;
- raw truncation retains the leading \(R^{-1/3}\) drift;
- a wrong leading-tail coefficient fails the plateau bound;
- the accelerated coefficient still needs the finite determinant/source
  window budget and a noncancellation margin for relative control.

## Verification

- `python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py`
- `python3 calculation-checks/bpst_instanton_normalization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only bpst_instanton_normalization_checks`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail --limit 20`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full build completed with a clean log scan at 3389 pages.
