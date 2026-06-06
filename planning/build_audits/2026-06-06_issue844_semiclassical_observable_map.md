# Issue #844: Semiclassical Backreaction Observable Map

## Scope

This pass audits Volume XII Chapter 11 against the claim-architecture concern
that formal status machinery can detach from physical observables.  The
reader-facing entrance now states the physical question directly: whether a
specified quantum state, renormalized stress tensor, and stress-tensor
fluctuation law produce a controlled retained metric observable.

The new chapter chain is

```text
locally covariant algebra/state/stress tensor
  -> gravitational EFT coordinates and state transport
  -> Ward-clean source/noise/retarded response
  -> mean metric shift and Einstein-Langevin covariance
  -> retained metric observable
```

The semiclassical Einstein equation is correspondingly described as conditional
semiclassical control, not as an interacting quantum-gravity theorem or a
standalone physical prediction.  I also replaced local reader-facing
"ledger"-style wording around the interacting first-order stress source with
decomposition/construction language while leaving existing TeX labels stable.

## Companion Evidence

`calculation-checks/semiclassical_backreaction_checks.py` now includes
`check_semiclassical_observable_chain_boundary()`.  The check is intentionally
finite and architectural: it verifies the ordering and required side data for a
retained metric-observable claim, then rejects formal-equation-only, mean-only,
noise-without-metric-covariance, wrong-order, and no-signal-to-noise shortcuts.

The calculation-check README and Volume XII Chapter 11 dossier were updated to
record the same observable boundary.

## Verification

- `python3 -m py_compile calculation-checks/semiclassical_backreaction_checks.py`
- `python3 calculation-checks/semiclassical_backreaction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only semiclassical_backreaction`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii --limit 40`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` clean, producing `monograph/tex/main.pdf` at 3403 pages.
