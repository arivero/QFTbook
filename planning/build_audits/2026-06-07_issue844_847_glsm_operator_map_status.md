# 2026-06-07 Issue #844/#847 GLSM Operator-Map Status Audit

## Scope

This pass re-audits the Hori--Vafa common-flux operator-map surface in Volume
VII Chapter 09.  It responds to #844's warning that residual maps should not
be promoted to controlled approximations when the component estimates have not
been constructed, while preserving #847's compact-flux and operator-map
scrutiny.

## Change

`ca:glsm-common-flux-operator-map-diagnostic` was demoted to
`rem:glsm-common-flux-operator-map-diagnostic`.  The text now says the
operator-map inequality is a target estimate only after the operator, source,
span, flavor, assembly, and continuum component bounds have been supplied in
one source topology.

The companion check keeps the finite span/null-direction diagnostic, but adds
a status guard: residual slot names alone are not a controlled estimate, and
omitting the span component prevents the finite bound from being promoted.

## Quality Boundary

This is a status and coherence repair, not a new continuum Hori--Vafa theorem.
It keeps the finite common-flux diagnostic as useful evidence while preventing
the monograph from overstating a proof-obligation map as an estimate.

## Verification Plan

- Run the focused GLSM companion and harness entry.
- Run chapter-local theorem/display/prose/style audits for Chapter 09.
- Run evidence-contract, calculation-inventory, dossier, and diff checks.
- Run the full Python calculation-check suite and full monograph build before
  committing.

## Verification Result

Completed on 2026-06-07.  The focused GLSM checks, Chapter 09 local audits,
evidence-contract audit, calculation-check inventory audit, chapter-dossier
audit, full Python calculation-check suite, and full monograph build/log scan
all passed before staging.
