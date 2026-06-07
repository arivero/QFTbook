# Issue #597 instanton source RG frame audit

## Scope

This pass addressed the live issue #597 concern that the Ch20D
mass/source RG transport block used the `+r gamma_m` law for an object that
had been defined with running inserted source directions.

The repair is physics-facing rather than moduli-space-facing: it keeps the
finite light-fermion nonzero-mode determinant, the zero-mode source
determinant, and the external source/projection coordinates in the same
amplitude channel.  No directive or issue-process language was added to the
monograph TeX.

## Re-audit

- The TeX now distinguishes the fixed-coordinate coefficient tensor
  `K^comp_{A_1...A_r}` from the contracted running-source object
  `K^phys[B_1,...,B_r]`.
- The finite source-bundle connection is written before suppressing basis
  transport.  The component tensor carries `+r gamma_m`; the running source
  vectors carry `-gamma_m` each; their contraction is invariant, up to named
  residuals.
- The two-flavor example was reread against this split: fixed-basis
  coefficients such as `R_f m_d` and `R_f` carry `+gamma_m` and
  `+2 gamma_m`, while `R_f m_d B_uu` and
  `R_f (B_uu B_dd - B_ud B_du)` with running physical source components are
  invariant in this source RG bookkeeping.
- The companion check now tests both frames and rejects the old running-source
  shortcut.  It also tests one-source and two-source finite connection
  cancellation, with negative controls for omitted connection terms.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii --fail --limit 40`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
