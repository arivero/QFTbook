# Issue #844/#755 Phi4_3 Status Split Audit

## Scope

- Rewrote the dynamic \(\Phi^4_3\) theorem-boundary passage in Volume XI Ch09.
- Removed constructive Euclidean measure identification from the quoted SPDE
  theorem.
- Added a separate common-regulator SPDE/constructive identification
  hypothesis with matched field/mass coordinates, bounded-cylinder convergence,
  polynomial-window tail control, Schwinger-moment equality, and constructive
  OS inputs.
- Extended `constructive_scalar_spde_checks.py` with a finite status-split
  negative control: SPDE construction slots alone cannot certify the
  constructive OS hierarchy.

## Architecture Re-Audit

- Old interrupted route: the quoted theorem packaged SPDE well-posedness,
  BPHZ convergence, invariant laws, and equality with the constructive measure,
  while the following paragraph said the equality still had to be proved.
- New canonical route: BPHZ SPDE construction gives a candidate stationary
  law; a separate common-regulator comparison supplies Schwinger-hierarchy
  equality; only then does OS positivity transfer through the common-hierarchy
  construction.
- Material merged or relocated: no theorem content was deleted; the
  constructive-identification clause was moved from the quoted theorem into a
  hypothesis with explicit required inputs.
- Independent evidence retained: finite stationary-law coupling arithmetic,
  polynomial truncation, SPDE/constructive hierarchy-transfer, finite-window
  OS defect, finite-rate assembly, cross-route phase-cell budget, and directed
  OS pre-Hilbert comparison.
- Unresolved theorem boundary: the actual BPHZ model estimates, fixed-point
  model bounds, common-regulator constructive comparison, polynomial
  uniform-integrability tails, and full OS assembly remain open.

## Verification

- `python3 -m py_compile calculation-checks/constructive_scalar_spde_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/constructive_scalar_spde_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `tools/run_calculation_checks.sh --python-only --only constructive_scalar_spde`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
