# 2026-06-06 issue #844 BCFT observable-output pass

## Scope

- Added a front-of-chapter observable-output bridge in Vol V Ch14.
- The bridge displays the open annulus partition function, disk one-point
  response, and boundary-gradient susceptibility before the sewing-move
  machinery begins.
- Extended `calculation-checks/bcft_cardy_checks.py` with a finite negative
  control in which the annulus spectrum is fixed while disk response and
  boundary susceptibility change.

## Quality Re-Audit

- Physics depth: the pass ties BCFT formal data to boundary observables rather
  than adding another local sewing cell.
- Coherence control: the new paragraph sits at the chapter entrance and orients
  later annulus, rational, nonrational, and boundary-entropy sections.
- Anti-wrapper check: the finite companion rejects annulus-only reconstruction
  of disk and susceptibility outputs.
- Monograph hygiene: issue/process language stays in this planning note, not in
  the reader-facing TeX.

## Verification Target

- Focused `bcft_cardy_checks.py` run and py_compile.
- Ch14 theorem/display/style/text audits.
- Evidence-contract audit.
- Full Python calculation suite and full monograph build before commit.
