# 2026-06-07 Issue #847 Vortex-Core Disorder Audit

## Scope

This pass targets the remaining Hori--Vafa operator-map risk in Volume VII
Chapter 09: the primitive dual monomial `exp(-Y_i)` should not be inferred from
the local chart `Phi_i=exp(Psi_i)`, because that chart excludes the vortex
core where `Phi_i=0`.

## Change

Added `ca:glsm-vortex-core-disorder-insertion`.  The text now defines the
original disorder insertion by a punctured-disk core boundary condition:

- a unit core has phase degree one around the small boundary circle;
- finite angular energy requires the charged scalar to vanish at the core;
- `log Phi_i` has monodromy around the core and cannot be a single-valued
  local field through the insertion;
- the original path integral uses a core-domain/source normalization before
  the dual-frame operator map identifies the image with `exp(-Y_i)`.

The block also records that equal-charge flavor rotations permute disorder
source rows while the compact gauge-flux sector remains common.

## Companion

Added `check_vortex_core_disorder_insertion_gate()` to
`calculation-checks/susy_2d_lg_glsm_checks.py`.  The finite check verifies the
core energy criterion, logarithmic monodromy obstruction, primitive dual
orientation, flavor-row covariance, and the residual budget term for the core
domain.

## Quality Boundary

This is not a proof of Hori--Vafa mirror equivalence or of the continuum
operator map.  It closes one local-domain gap: the original vortex/disorder
operator is a core boundary condition and source-normalized limit, not a
regular local expression in the logarithmic chart.

## Verification Plan

- Run the focused SUSY GLSM companion and harness entry.
- Run Chapter 09 local theorem/display/prose/style audits and TeX leakage scan.
- Run evidence-contract, calculation-inventory, dossier, JSON, and diff checks.
- Run the full Python calculation-check suite and full monograph build before
  committing if the focused pass is clean.

## Verification Result

Completed on 2026-06-07. The focused SUSY GLSM companion, focused harness
entry, Chapter 09 local audits, TeX leakage scan, evidence-contract audit,
calculation-inventory audit, chapter-dossier audit, full Python
calculation-check suite, and full monograph build/log scan all passed before
staging.
