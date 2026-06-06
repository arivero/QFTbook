# 2026-06-06 Issue #769 Unresolved Measurement-Cell Audit

## Scope

- Target issue: #769, perturbative loop-amplitude development.
- Chapter touched: Volume II, Chapter 6, generalized-unitarity section.
- Companion check: `calculation-checks/generalized_unitarity_reduction_checks.py`.

## Substance Audit

- Physics target: the observable end of one-loop reconstruction.  The new
  block does not add another master coefficient or reduction identity; it
  expands the symbolic real-emission/subtraction term into the local
  unresolved measurement cell that makes a massless observable finite.
- New controlled approximation:
  `ca:one-loop-unresolved-measurement-cell`.
- Main mechanism:
  \[
    \int_0^1 dx\,x^{-1+\epsilon_{\rm ir}}W(x,\zeta)
    =
    {W_0(\zeta)\over\epsilon_{\rm ir}}
    +
    \int_0^1 dx\,{W(x,\zeta)-W_0(\zeta)\over x}
    +O(\epsilon_{\rm ir}).
  \]
  The pole cancels only against a counterevent carrying the reduced-event
  measurement \(W_0\); the finite \(\int(W-W_0)/x\) term is part of the
  physical answer for non-inclusive measurements.
- Re-audit result: aligned with the monograph standard.  It moves loop
  reconstruction toward finite QFT observables, separating virtual hard
  remainders, unresolved real radiation, subtraction measurement data, and
  infrared safety.  It is physics depth rather than tangential reduction
  algebra, and no directives were placed in TeX.

## Exact Checks Added

- Plus-measurement cell:
  for \(W(x)=w_0+w_1x+w_2x^2\), the finite unresolved term is checked as
  \(w_1+w_2/2\).
- Pole cancellation:
  virtual and real cells cancel the \(1/\epsilon_{\rm ir}\) pole only when the
  real counterevent uses the reduced measurement \(W_0\).
- Negative controls:
  using a resolved-event subtraction measurement leaves a pole, freezing the
  measurement to \(W_0\) erases the finite unresolved contribution,
  virtual-only assembly keeps the pole, and a logarithmic non-infrared-safe
  weight grows with the unresolved cutoff.
- Terminology cleanup:
  the nearby one-loop reconstruction material now says data package/component
  rather than overusing "datum" as prose.

## Verification Plan

- Focused syntax and generalized-unitarity checks.
- Chapter 6 text/style audits after the insertion and terminology cleanup.
- Calculation inventory/evidence audits.
- Dossier and monograph text audits.
- Full Python calculation suite and full monograph build.

## Verification Results

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --limit 20`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

All listed checks passed.  The full monograph build completed cleanly at
`monograph/tex/main.pdf` with 3404 pages.
