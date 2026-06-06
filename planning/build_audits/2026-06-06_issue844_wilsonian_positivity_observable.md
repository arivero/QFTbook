# 2026-06-06 Issue #844 Wilsonian Positivity Observable Audit

## Scope

- Target issue: #844, formal status machinery reconnected to physical
  observables.
- Chapter touched: Volume II, Chapter 16, Wilsonian EFT / positivity section.
- Companion check: `calculation-checks/eft_prediction_calculus_checks.py`.

## Substance Audit

- Physics target: the forward positivity coefficient as an absorptive
  scattering observable, not as a free-standing sign rule for a Wilson
  coordinate.
- The pass keeps the existing twice-subtracted dispersion derivation and adds
  the operational translation:
  \[
    a_2 =
    \frac2\pi\int_{4m^2}^\infty ds\,
    \frac{\sqrt{s(s-4m^2)}\sigma_{\rm abs}^{\rm sub}(s)}
         {(s-2m^2)^3}
    + c_\infty .
  \]
- A finite energy window now has reader-facing content:
  \(a_2=B(S_0)+T(S_0)+c_\infty\), with \(T(S_0)\ge0\) under the stated
  positivity assumptions.  If a matched low-energy coefficient lies below
  \(B(S_0)\), the text identifies the possible physical failures: wrong
  normalization, missing subtraction or infrared prescription, nonzero contour
  term, failed analyticity/unitarity assumption, or an EFT-to-observable
  mismatch.
- Re-audit result: this is physics anchoring of an existing theorem-status
  block.  It does not add tangential mathematics or claim a UV-completion
  theorem.  The companion check is a finite normalization/regression test, not
  independent empirical evidence for a scattering amplitude.

## Exact Checks Added

- The finite positive spectral model is converted to cross-section bins using
  the optical-theorem prefactor \(\sqrt{s(s-4m^2)}\).
- The cross-section moment is checked to equal the existing dispersive
  \(a_2\) coefficient.
- A finite window plus positive tail is checked as a lower-bound mechanism.
- A negative control rejects omitting the optical-theorem flux factor.

## Verification Plan

- Run the focused EFT prediction-calculus check.
- Run the chapter-local theorem/display/prose/style audits.
- Run dossier, text, calculation-inventory, and evidence-contract audits.
- Run the full Python calculation suite and full monograph build.

## Verification Results

- `python3 -m py_compile calculation-checks/eft_prediction_calculus_checks.py`
  passed.
- `python3 calculation-checks/eft_prediction_calculus_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only
  eft_prediction_calculus` passed.
- Chapter-local theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/audit_monograph_text.sh` passed.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `python3 tools/audit_calculation_evidence_contracts.py` passed with the
  standing non-blocking risk report.
- `git diff --check` passed.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` rebuilt cleanly
  at 3404 pages.
