# 2026-06-06 Issue 597 Inclusive Cut Projection Audit

## Scope

- Added `ca:instanton-inclusive-cut-quadratic-projection` to Volume II
  Chapter 20D between mixed-source pole extraction and first cluster
  corrections.
- Added an exact finite companion check in
  `calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- Updated the Chapter 20D dossier and calculation-check inventory.

## Depth Audit

- This pass addresses the physics interpretation of an instanton-induced
  amplitude, not the BPST/ADHM moduli geometry.
- The new block separates a \(Q=1\) pole- or OPE-projected amplitude from a
  positive inclusive cut or rate.  The latter requires the conjugate sector,
  a physical final-state measurement matrix, source amputation, and quadratic
  residual propagation.
- The companion check rejects the main overreadings: a signed linear sum
  treated as a rate, unamputated source vectors used in the cut, omission of
  the measurement matrix, and underbudgeting of the amplitude residuals after
  squaring.

## Scope Guard

- No planning directives, review commentary, or GitHub metadata were inserted
  into the monograph TeX.
- The inserted mathematics is finite-dimensional only to expose the physical
  cut/amplitude distinction; it is not a replacement for the continuum
  determinant calculation or for an instanton-pair/valley analysis.
