# Build Audit: Issue #844 Coulomb-Gas/BPZ Demotion

Date: 2026-06-06

## Scope

- Volume V Chapter 12, Dotsenko--Fateev / Coulomb-gas
  screening-to-BPZ comparison surface.
- Companion check:
  `calculation-checks/cft_virasoro_minimal_checks.py`.
- Volume V Chapter 12 dossier and calculation-check inventory wording.

## Change

- Retitled the reader-facing surface from a construction budget to a
  comparison datum.
- Kept the finite coordinates, residual decomposition, and conditional
  inequality, but stated that the inequality has content only after the
  screening, twisted-cycle, BPZ-basis, continuation, and nonchiral-pairing
  estimates are separately supplied.
- Added a companion negative control for named comparison slots with no
  supplied bounds.

## Re-Audit

- This is a status/physics-output repair, not a new Coulomb-gas integral.
- The Dotsenko--Fateev formulas remain concrete coordinates on chiral block
  spaces; the text no longer lets the comparison identity look like the
  theorem-level construction of the minimal-model correlator.
- Process and issue-tracking language remains confined to planning files.

## Verification

- `python3 -m py_compile calculation-checks/cft_virasoro_minimal_checks.py`
- `python3 calculation-checks/cft_virasoro_minimal_checks.py`
- `tools/run_calculation_checks.sh --python-only --only cft_virasoro_minimal`
- Chapter-local theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits for Volume V Chapter 12.
- Process-language scan on the touched TeX and companion check.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` clean at 3475 pages.
