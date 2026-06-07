# 2026-06-07 Issue #847 Gauge-Covariant Vortex-Core Repair

## Scope

This pass responds to the review that the previous vortex-core disorder block
used ordinary scalar winding data for a gauge-charged field and conflated a
smooth vortex core with a singular punctured-disk disorder defect.

## Change

Volume VII Chapter 09 replaces the earlier controlled-approximation block by a
construction, `constr:glsm-vortex-core-disorder-datum`.  The construction
defines the local datum as a principal `U(1)` bundle with connection and a
charge-`Q_i` associated section on the punctured disk, modulo gauge
transformations.  The invariant local period is now
`h_i=(2 pi)^{-1} int(d theta_i + Q_i A)`.

The text separates:

- smooth extendable vortex saddles with regular holonomy and integral divisor
  order;
- singular holonomy defects on the punctured disk, which require their own
  singularity, counterterm, bosonic/fermionic domain, and source normalization;
- flavor/source-row labels from the common compact gauge-flux sector.

It also derives the primitive `exp(-Y_i)` orientation from the first-order
compact-scalar boundary term on the excised disk rather than asserting it from
the local logarithmic chart.

## Companion

`check_vortex_core_disorder_insertion_gate()` now verifies:

- ordinary scalar winding and connection holonomy change under large gauge
  transformations while `h_i` is invariant;
- smooth core extension requires regular holonomy and an integral divisor
  zero;
- singular holonomy can cancel scalar winding but is not a smooth vortex core;
- the excised-disk boundary action gives `exp(-Y_i)` for the primitive positive
  orientation and `exp(+Y_i)` for the opposite orientation;
- equal-charge core labels are projective flavor/source data rather than new
  topological flux sectors;
- omitting either the core-domain residual or the first-order boundary-term
  residual underbudgets the operator comparison.

## Quality Boundary

This is still not a proof of the continuum Hori--Vafa operator map or of a
uniform vortex-regulator limit.  It is a gauge-covariant local-domain repair
that removes the previous ordinary-winding shortcut and makes the boundary-term
sign a checked finite datum.

## Verification Plan

- Run the focused SUSY GLSM companion and focused harness entry.
- Run Chapter 09 local theorem/display/prose/style audits and TeX leakage scan.
- Run evidence-contract, calculation-inventory, dossier, JSON, and diff checks.
- Run the full Python calculation-check suite and full monograph build before
  staging if the focused pass is clean.

## Verification Result

Completed on 2026-06-07.  The focused SUSY GLSM companion, focused harness
entry, Chapter 09 local audits, TeX leakage scan, evidence-contract audit,
calculation-inventory audit, chapter-dossier audit, full Python
calculation-check suite, and full monograph build/log scan all passed before
staging.
