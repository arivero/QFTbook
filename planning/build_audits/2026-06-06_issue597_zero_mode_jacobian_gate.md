# 2026-06-06 Issue 597 Zero-Mode Jacobian Gate Audit

## Scope

- Added `ca:instanton-collective-jacobian-gauge-slice` to Volume II
  Chapter 20D inside the density-normalization section.
- Extended `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  with a finite gauge-sliced zero-mode Gram determinant check.
- Updated the Chapter 20D dossier and calculation-check inventory.

## Depth Audit

- This pass addresses the path-integral normalization behind the
  instanton measure, not ADHM geometry or moduli-space bookkeeping for its own
  sake.
- The new block makes the bosonic collective-coordinate measure a horizontal
  zero-mode Gram determinant with a stabilizer quotient and a metric-stability
  bound.  This is the normalization step that multiplies a source kernel before
  amputation and physical projection.
- The companion check rejects the main shortcuts: dimension-only zero-mode
  counting, raw gauge-vertical tangent vectors, use of `det G` instead of
  `sqrt(det G)`, omission of a stabilizer quotient, and uncontrolled
  Gram-metric perturbations.

## Scope Guard

- No planning directives, review commentary, or GitHub metadata were inserted
  into the monograph TeX.
- The finite algebra is only a regulator-cell model for the measure
  normalization.  It does not replace the continuum BPST determinant constant,
  the large-size endpoint analysis, the source fluctuation quotient, or the
  instanton-pair/valley problem.
