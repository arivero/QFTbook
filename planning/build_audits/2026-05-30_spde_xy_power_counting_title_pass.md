# SPDE XY Power-Counting Title Pass

## Scope

- Continued the #691 theorem/proof substance audit in Volume XI, Chapter 9.
- Read the tested \(XY\) covariance-graph power-counting proposition as a
  statement-proof unit.

## Decision

The proposition should remain theorem-family material.  Its proof is not
merely arithmetic: after listing the three finite graph types, it proves the
marginal total degree, checks strict proper-subgraph deficits, invokes the
multiscale sector summability theorem for relative scale gaps, and derives
the remaining overall logarithm.

## Change

- Retitled the proposition from a "ledger" to
  `Logarithmic power-counting bound for tested XY covariance graphs`.
- Renamed the label to `prop:spde-xy-tested-graph-log-bound`.
- Updated the downstream reference and chapter dossier language so the
  theorem-family wrapper advertises the actual analytic estimate.

## Status

This is a strengthening of statement boundaries, not a demotion.  The global
#691 proof-substance audit remains open.
