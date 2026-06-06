# Build Audit: Issue #844 Localization Comparison Demotion

Date: 2026-06-06

## Scope

- Volume VII Chapter 16, finite-order Nekrasov--Pestun comparison surface after
  the Pestun \(S^4\) localization formula.
- Companion check:
  `calculation-checks/susy_instanton_nekr_checks.py`.
- Dossier and calculation-check inventory wording for the same comparison.

## Change

- Demoted the reader-facing `controlledapproximation` block to an ordinary
  finite comparison datum.
- Kept the localized integrand, residual decomposition, and conditional
  inequality, but stated explicitly that the inequality is only propagation of
  already supplied determinant, pole-selection, gluing, Cartan, and tail
  estimates.
- Added a companion negative control for named comparison slots that have no
  supplied bounds.

## Re-Audit

- This is a physics-scope repair, not another ADHM or fixed-point lemma.
- The text now keeps the physical observable boundary visible: a Young-diagram
  coefficient is not an \(S^4\) field-theory observable until the same
  regulator supplies the classical, one-loop, north/south pole, gluing,
  Cartan, tail, and continuum/contact data.
- Process and issue-tracking language remains confined to planning files.

## Verification

- `python3 -m py_compile calculation-checks/susy_instanton_nekr_checks.py`
- `python3 calculation-checks/susy_instanton_nekr_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_instanton_nekr`
- Chapter-local theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits for Volume VII Chapter 16.
- Process-language scan on the touched TeX and companion check.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` clean at 3475 pages.
