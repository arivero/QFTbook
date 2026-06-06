Issue: #527 charged Haag--Ruelle / Wilson-line LSZ.

Scope of this pass:
- Added a physics-facing controlled approximation in Volume IV Chapter 5 for
  extracting a hard charged coefficient from a renormalized dressed
  boundary value.
- The new text keeps the observable chain explicit: simultaneous shell
  contraction by dressed left inverses, removal of the amplitude soft factor,
  removal of the Dollard comparison phase, and only then the hard
  flux-resolved coefficient.
- The residual budget separates shell-window, endpoint/contact,
  soft-threshold, and same-flux schedule errors.  The negative controls
  reject omitting the soft factor, using a wrong logarithmic Dollard
  coefficient, treating endpoint simple-pole contacts as a new amplitude, and
  reading finite-window threshold branches as isolated-shell residues.

Quality and scope re-audit:
- This is not claimed as the full nonperturbative charged Haag--Ruelle or
  Wilson-line LSZ theorem.
- It addresses a real physical interface: how a nonlocal charged correlator
  is converted into a hard charged scattering coefficient once soft,
  endpoint, phase, and shell limits are separated.
- It avoids a purely mathematical tangent and does not turn the chapter into
  another finite-lemma annex.  The monograph-facing addition is organized
  around the physical observable and its extraction errors.
- Per the independent-verification standard, the companion Python check is a
  finite normalization/regression model for the extraction algebra, not
  independent evidence for the existence of the nonperturbative boundary
  values.
- Planning/review language remains in this audit note and dossier, not in the
  TeX chapter.

Verification completed:
- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
- `python3 calculation-checks/charged_flux_dressing_checks.py`
- `tools/run_calculation_checks.sh --python-only --only charged_flux_dressing`
- Focused Volume IV Chapter 5 theorem-form, display-label, negative-scope,
  and style-density audits.
- Global dossier/text/inventory/evidence audits, full Python calculation
  suite, whitespace checks, and full monograph build.
- `tools/build_monograph.sh` completed with clean log scan at 3457 pages.
