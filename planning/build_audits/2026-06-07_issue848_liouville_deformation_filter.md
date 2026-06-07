# 2026-06-07 Issue #848 Liouville Deformation Filter Audit

## Scope

This pass extends the Volume VII Chapter 09 cigar/Liouville full-QFT lane.  It
targets the deformation-classification acceptance item in #848: excluding a
fake Liouville endpoint requires more than the protected superpotential and
local rigidity.

## Change

Added `ca:cigar-liouville-asymptotic-deformation-filter` after the normalized
asymptotic Liouville action.  The text classifies the integer
`Y`-periodic protected `F`-term exponentials:

- `ell=1` is the primitive marginal Liouville wall;
- `ell>=2` is irrelevant;
- fractional relevant-looking exponentials are not single-valued under the
  primitive `Y` period unless the global mirror datum is changed.

The same block then separates this protected filter from real `D`-term,
wall-domain, and source/contact deformations.  A Robin half-line response
shows explicitly that a boundary-domain parameter can move the continuous
reflection density while leaving the protected `F`-term inventory unchanged.

## Companion

Added `check_cigar_liouville_asymptotic_deformation_filter()` to
`calculation-checks/susy_2d_lg_glsm_checks.py`.  The finite check verifies the
integer-mode weights, rejects a fractional non-single-valued relevant mode,
rejects omission of the dual-circle contribution to the primitive weight, and
checks that the wall-domain response is a separate residual term.

## Quality Boundary

This is not a proof of the cigar/Liouville mirror equivalence, the full
Plancherel measure, or the finite-field Kahler rigidity theorem.  It is a
local asymptotic deformation filter plus an observable spectral-response gate
that makes one missing full-QFT obligation concrete.

## Verification Plan

- Run the focused SUSY GLSM companion and harness entry.
- Run Chapter 09 local theorem/display/prose/style audits and TeX leakage scan.
- Run evidence-contract, calculation-inventory, dossier, JSON, and diff checks.
- Run the full Python calculation-check suite and full monograph build before
  committing if the focused pass is clean.

## Verification Result

Completed on 2026-06-07.  The focused SUSY GLSM companion, focused harness
entry, Chapter 09 local audits, TeX leakage scan, evidence-contract audit,
calculation-inventory audit, chapter-dossier audit, full Python
calculation-check suite, and full monograph build/log scan all passed before
staging.
