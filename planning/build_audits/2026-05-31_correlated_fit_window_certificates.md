# 2026-05-31 Correlated Fit Window Certificates

## Scope

Continued the #703 numerical-evidence absorption lane in Volume XI,
Chapter 10.  The preceding Krylov and variational passes certified finite
spectral vectors and finite ansatz states.  This pass addresses the next
production-numerics gap: correlated extrapolation data and fit-window
stability must be finite evidence coordinates, not implicit continuum claims.

## Manuscript Changes

- Added a correlated-fit and window-stability paragraph to the
  finite-regulator extrapolation section of
  `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`.
- The new text defines the fit window, covariance matrix, fit functions,
  design matrix, and systematic remainder envelopes.
- It derives the finite correlated least-squares coordinate, the exact
  decomposition of intercept error into deterministic remainder and
  stochastic noise, the finite covariance propagation formula, the systematic
  row-amplifier coordinate, and the correlated residual diagnostic.
- It states explicitly that window stability is evidence about a declared
  finite regulator family and does not replace the analytic estimate
  producing the remainder envelopes.

## Companion Checks

- Extended `calculation-checks/numerical_extrapolation_checks.py` with a
  deterministic positive-definite covariance example verifying:
  - exact fit-error decomposition;
  - coefficient covariance propagation;
  - intercept variance equality;
  - systematic envelope bound;
  - finite nonnegative correlated residual coordinate.
- Updated `calculation-checks/README.md`, the Volume XI Chapter 10 dossier,
  and `planning/source_inventory/statmech_crosswalk.md`.

## Theorem-Form Note

No new theorem-family environment was introduced.  The identities are useful
finite linear algebra for numerical evidence standards, so the manuscript
presents them as derivational prose and numbered equations rather than as
inflated proposition/proof wrappers.

## Verification

- `python3 calculation-checks/numerical_extrapolation_checks.py`
- `python3 -m py_compile calculation-checks/numerical_extrapolation_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

Full monograph build clean at 2746 pages.
