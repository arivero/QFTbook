# 2026-06-06 Issue #844 Wilsonian Positivity Residual Re-Audit

## Scope

- Target issue: #844, physics-first claim architecture and observable anchoring.
- Chapter touched: Volume II, Chapter 16, conditional scalar positivity in the
  Wilsonian EFT chapter.
- Companion check: `calculation-checks/eft_prediction_calculus_checks.py`.
- Planning companion:
  `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md`.

## Substance Audit

- Physics target: the positivity statement as a comparison between a matched
  forward-amplitude coefficient, finite-window absorptive data, the positive
  high-energy tail, the large-contour coordinate, and the EFT prediction
  remainder.
- The monograph now promotes the finite-window object to the residual
  \[
    \Delta_{\rm pos}(S_0)=a_2-c_\infty-B(S_0)=T(S_0)\ge0 .
  \]
- The EFT side is tied to the prediction datum by
  \(a_2=\kappa_{\rm amp}/\Lambda^4+R_N^{(2)}\), so the finite-window comparison
  tracks the named remainder rather than treating the amplitude coordinate as a
  naked Wilson-coefficient sign.
- Re-audit result: this is architecture repair for an existing physics claim.
  It clarifies what a measurement or matching calculation would test, and it
  rejects the tangential route of adding more formal dispersion machinery.

## Exact Checks Added

- The finite positive spectral model now checks that the finite-window residual
  equals the positive tail after the contour coordinate is subtracted.
- A negative control gives positive spectral weight and positive tail while a
  retained contour makes the shortcut \(a_2-B(S_0)\) negative, demonstrating
  that the contour-subtracted residual is the meaningful observable.

## Verification Plan

- Run the focused EFT prediction-calculus check.
- Run the focused Chapter 16 theorem/display/prose/style audits.
- Run dossier, text, calculation-inventory, and evidence-contract audits.
- Run diff checks, the full Python calculation suite, and the full monograph
  build.

## Verification Results

- `python3 -m py_compile calculation-checks/eft_prediction_calculus_checks.py`
  passed.
- `python3 calculation-checks/eft_prediction_calculus_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only
  eft_prediction_calculus` passed.
- Focused Chapter 16 theorem-form, unnumbered-display-label, negative-scope,
  and style-density audits passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/audit_monograph_text.sh` passed.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `python3 tools/audit_calculation_evidence_contracts.py` passed with the
  standing non-blocking risk report.
- Process-language scan on the edited reader-facing files found no issue,
  directive, review, or monitor language.
- `git diff --check` passed.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` rebuilt cleanly
  at 3483 pages.
