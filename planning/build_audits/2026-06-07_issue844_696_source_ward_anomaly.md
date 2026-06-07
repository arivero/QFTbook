# 2026-06-07 Issue #844/#696 Source-Ward Anomaly Audit

## Scope

This pass targets the anomaly proof-debt and formal-architecture overlap:
the cubic descent class should be visible as a physical source Ward identity,
not only as an abstract relative BRST class.

## Change

Added `prop:source-ward-test-cubic-anomaly` in Volume II Chapter 20.  The
new proposition restricts the consistent anomaly to an Abelianized Cartan
background, differentiates the anomalous variation with respect to two
background gauge sources, and identifies the resulting coefficient with the
divergence/contact part of the consistent three-current correlator.

The pass separates three quantities:

- the individual consistent contact coefficient `D_{i;jk}=2 C_{i;jk}`;
- the local cubic counterterm shift, which can move contact terms among
  currents;
- the fully polarized coordinate `(D_{i;jk}+D_{j;ik}+D_{k;ij})/6`, which is
  counterterm invariant and equals the Cartan restriction of the cubic anomaly
  tensor.

## Companion

Extended `calculation-checks/anomaly_polynomial_descent_checks.py` with a
finite source-Ward contact-polarization check.  The check verifies that a
single current contact remains counterterm-dependent, while the polarized
coordinate recovers the invariant cubic class and a counterterm-only contact
has zero class coordinate.

## Quality Boundary

This is not a proof of the full local BRST cohomology classification, the
analytic index theorem, or the existence of a nonperturbative chiral gauge
theory.  It closes one physics-architecture gap: the descent coefficient is
now tied directly to a source Ward contact term that a QFT reader can follow
from background coupling to physical obstruction or anomaly matching datum.

## Verification Plan

- Run the focused anomaly-polynomial companion and focused harness entry.
- Run Chapter 20 local theorem/display/prose/style audits and TeX leakage scan.
- Run evidence-contract, calculation-inventory, dossier, JSON, and diff checks.
- Run the full Python calculation-check suite and full monograph build before
  committing if the focused pass is clean.

## Verification Result

Completed on 2026-06-07. The focused anomaly-polynomial companion, focused
harness entry, Chapter 20 local audits, TeX leakage scan, evidence-contract
audit, calculation-inventory audit, chapter-dossier audit, full Python
calculation-check suite, and full monograph build/log scan all passed before
staging.
