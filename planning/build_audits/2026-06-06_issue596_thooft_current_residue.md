# 2026-06-06 issue #596/#725 't Hooft current-residue pass

## Scope

- Promoted `calculation-checks/thooft_model_checks.py` to an extended
  evidence contract and manifest entry.
- Added `ca:qcd2-dlcq-current-correlator-residue-contract` to Vol II Ch20c.
- Added an exact finite spectral-measure negative control: two finite mass
  matrices with the same eigenvalues give different Euclidean current
  correlators because the same source vector has different eigenvector
  residues.

## Quality Re-Audit

- Physics depth: the pass moves from finite meson masses to current
  correlators and residues, which are the quantities seen by sources.
- Scope control: no continuum DLCQ convergence theorem, numerical
  extrapolation, or 3D Chern-Simons-matter solution is asserted.
- Anti-wrapper check: the finite check rejects the common shortcut that a
  regulated spectrum alone determines the meson observable.
- Monograph hygiene: issue numbers and process language stay in planning
  files, not in the TeX.

## Follow-up Re-audit

Issue #844 review correctly identified that the finite current-residue block
is an exact finite resolvent/spectral-measure map, not a controlled
approximation to the continuum current correlator.  The monograph surface was
therefore demoted to `rem:qcd2-dlcq-current-correlator-residue-map`, and the
companion evidence contract now describes exact finite spectral-source
bookkeeping rather than a continuum approximation estimate.

## Verification Target

- Focused `thooft_model_checks.py` run and py_compile.
- Evidence-contract audit with the strict backlog reduced by one.
- Ch20c theorem/display/style/text audits.
- Full Python calculation suite and full monograph build before commit.
