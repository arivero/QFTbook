# 2026-06-07 Issue #769 Event-Shape Plus-Distribution Audit

## Scope

This pass extends the Volume II Chapter 06 loop-amplitude-to-observable
bridge after the one-emission event-shape cumulant.  The new material is a
local soft-collinear singular-chart statement: it turns the cumulant into a
differential event-shape plus distribution and records the virtual endpoint
delta needed for pole cancellation.

## Change

Added `ca:one-loop-event-shape-plus-distribution`.  The text differentiates
the product-measurement cumulant for `tau=alpha beta`, displays
`tau^(-1+epsilon) log(1/tau)` as
`epsilon^(-2) delta(tau) + [log(1/tau)/tau]_+`, and shows that after the
virtual endpoint delta cancels the double pole the plus distribution
integrates to `-1/2 log^2(1/tau_0)` on the cumulant window.

The companion exact check encodes the endpoint double-pole delta, finite
delta, `[1/tau]_+`, and `[log(1/tau)/tau]_+` coefficients separately.  It
rejects ordinary positive-density integration, omitted virtual endpoint
delta, frozen reduced-event measurement, and one-coordinate endpoint plus
shortcuts.

## Quality Boundary

This is not a complete event-shape factorization theorem.  It fixes the local
measurement distribution that virtual generalized unitarity and master
reconstruction do not provide.  A full observable still needs the hard, jet,
soft, overlap, nonsingular, recoil, and global-factorization data appropriate
to the chosen event shape.

## Verification Plan

- Run the focused generalized-unitarity companion and harness entry.
- Run Chapter 06 local theorem/display/prose/style audits and TeX leakage
  scan.
- Run evidence-contract, calculation-inventory, dossier, JSON, and diff
  checks.
- Run the full Python calculation-check suite and full monograph build before
  committing if the focused pass is clean.

## Verification Result

Completed on 2026-06-07.  The focused generalized-unitarity companion,
focused harness entry, Chapter 06 local audits, evidence-contract audit,
calculation-inventory audit, chapter-dossier audit, full Python
calculation-check suite, and full monograph build/log scan all passed before
staging.
