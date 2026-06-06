# 2026-06-06 Issue #844 Factorization Reference-Map Audit

## Scope

- Added the claim-architecture and observable-anchor rule to
  `planning/12_strict_writing_harness.md`.
- Reframed the large factorization status table in
  `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
  as a physical-observable reference map.
- Updated the Chapter 19b dossier and calculation-check inventory text.

## Quality Intent

This pass responds to the architecture risk that formal status vocabulary can
become more visible than the physics it is meant to protect.  The reader-facing
SCET table now says explicitly that it is navigation, not independent evidence:
each row starts from an observable, records the regulated mathematical object
and local status, and treats a named remainder as a residual slot until an
estimate or uniform bound is cited.  The planning harness now requires future
load-bearing developments to expose physical question, object, status,
derivation, physical output, and verification boundary in that order.

## Verification

- `git diff --check`
- `python3 -m py_compile calculation-checks/scet_factorization_checks.py`
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- focused Chapter 19b theorem-form, unnumbered-display-label,
  negative-scope, and style-density audits
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/build_monograph.sh`

All commands passed.  The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` at 3402 pages.
