# Issue #700: Anomaly-Inflow Defining Datum

## Target

Volume IX, Chapter 6 was flagged in issue #700 because the chapter used
anomaly lines, relative partition functions, and invertible inflow theories
before aggregating the central object into one defining-property block.

## Edit

- Added `def:anomaly-inflow-datum` at the chapter opening.
- The datum now fixes:
  - background-field groupoids `B(M)`;
  - the background bordism category `Bord_{D+1}^B`;
  - the invertible bulk functor `Z_bulk`;
  - the induced boundary anomaly-line functor `L`;
  - the relative boundary partition vector `Z_partial`.
- Added the section label `sec:inflow-bulk-boundary-lines` and connected the
  filling quotient construction to the new datum.
- Rewrote the first two sections to refer back to the anomaly-inflow datum,
  rather than introducing the ingredients as scattered prose.
- Updated the Chapter 6 dossier.

## Scope

This pass addresses the #700 definition-locality failure for anomaly inflow.
It does not close the deeper anomaly proof-debt cluster in #696; descent,
global anomaly, determinant-line, and BV-anomaly statements still need
separate proof-substance passes where they are used as theorem-level input.
