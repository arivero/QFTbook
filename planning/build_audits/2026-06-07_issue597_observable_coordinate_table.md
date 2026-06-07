# Issue #597 Observable-Coordinate Coherence Audit

## Scope

- Added a physical-coordinate checklist to Volume II Ch20D's observable-map section.
- The checklist names the extra physical map required before instanton source data
  can be called a hard source amplitude, theta curvature, \(U(1)_A\)-odd
  susceptibility, or real-time axial relaxation rate.
- Extended the instanton physical-amplitude companion with a finite requirement
  classifier rejecting density-only hard amplitudes, hard-source data used as
  theta curvature, theta curvature used as a real-time rate, and \(U(1)_A\)
  susceptibility claims with the order of limits omitted.

## Quality Audit

- This is a coherence and physical-output pass, not another ADHM/moduli-space
  cell.
- It follows the user's instanton directive by making the final observable map
  explicit: the saddle, density, and source determinant are inputs, while the
  physical claim requires projection, positivity/continuation, and residual
  data in the chosen observable row.
- Scope boundary retained: the pass does not compute the continuum determinant
  constant, prove a full LSZ theorem for instanton amplitudes, or close the
  larger dedicated soliton/monopole/instanton issue.

## Architecture Re-Audit

- Fresh issue #844 review was checked before staging.  The warning is correct:
  a future hotspot pass must rewrite sustained arguments, not merely add local
  formal blocks.
- Before this pass, the chapter's opening source-functional spine was strong,
  but the final observable handoff still left room for treating the hard
  coefficient, theta curvature, \(U(1)_A\)-odd susceptibility, and real-time
  relaxation rate as adjacent outputs of the same density.
- After this pass, the closing observable-map section now completes the same
  chapter-level chain started at the opening: source functional, zero-mode
  saturation, fluctuation/source response, endpoint/Haar/LSZ or OPE projection,
  then a named observable coordinate.  The companion check turns this handoff
  into finite negative controls rather than another moduli-space cell.
- Material removed or merged: the initial narrow table form was replaced by a
  prose checklist after the build log exposed bad typography; no extra
  mathematical side route was added.
- Independent evidence retained: the source-functional route, hard \(SU(3)\)
  channel assembly, same-coordinate amplitude/rate residual, neutral-pair
  valley prescription, and the new finite observable-coordinate classifier.
- Unresolved theorem boundary: the full continuum determinant normalization,
  continuum LSZ theorem for instanton-mediated hard amplitudes, uniform
  endpoint/cluster estimates, and a chapter-wide #844 structural rewrite remain
  open.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
