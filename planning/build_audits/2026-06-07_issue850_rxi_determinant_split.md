# 2026-06-07 Issue #850 R_xi Determinant Split

## Scope

This pass continues the Higgs-branch metric repair for Volume VII Chapter 08.
The previous issue #850 pass correctly demoted the
`4 + 2 + 4 - 2 + 0 - 8` component balance, but its companion still checked a
hand-entered gauge-parameter ledger rather than deriving the cancellation from
the gauge-fixed fluctuation operators.

## Change

Chapter 08 now includes `ex:higgs-branch-rxi-determinant-split`, which works in
the explicit rank-one positive-FI Higgs patch and factors the constant-background
massive-vector operator into transverse and longitudinal projectors,
`eq:higgs-branch-rxi-gauge-vector-split`.

The example derives the field-dependent `R_xi` determinant cancellation
`eq:higgs-branch-rxi-xi-sector-cancellation`:

- one longitudinal vector mode contributes `+1/2 log(p^2 + xi M^2)`;
- one real Goldstone contributes `+1/2 log(p^2 + xi M^2)`;
- the complex Faddeev--Popov ghost pair contributes `-log(p^2 + xi M^2)`.

The text states explicitly that this is a gauge-fixing consistency checkpoint,
not the completed value of the Higgs two-derivative coefficient
`Pi_mn^{1-loop}`.

## Companion

`susy_moduli_space_checks.py` now generates the constant-background spectrum in
`d=4,3,2` from operator classes and field statistics.  The check derives the
trace-log weights from field type and mode count, verifies the generated
`R_xi` cancellation, and uses negative controls that remove the ghost,
Goldstone, or longitudinal-vector sector.  It also derives the
dimension-specific split between vector components and reduced connection
scalars, instead of reusing the four-dimensional gauge-field count.

## Quality Boundary

This is genuine background-field infrastructure: it replaces a fragile
multiplicity/cancellation ledger with the determinant algebra forced by the
quadratic operators.  It does not yet compute the full tangent-dependent
supertrace with all seagulls, mixed diagrams, fermions, and auxiliary contacts,
and it does not prove the all-order Higgs-branch metric theorem.

## Verification Plan

- Run the focused `susy_moduli_space_checks.py` companion.
- Run Chapter 08 theorem/display/prose/style audits.
- Run dossier and calculation inventory/evidence audits.
- Run `git diff --check`, the full Python calculation suite, and the full
  monograph build/log scan before staging.

## Verification Result

Completed on 2026-06-07.  The focused moduli-space companion,
`py_compile`, Chapter 08 theorem-form, display-label, negative-scope, and
style-density audits, calculation evidence-contract and inventory audits,
chapter-dossier audit, full strict monograph text harness, full Python
calculation suite, `git diff --check`, and full monograph build/log scan all
passed before staging.
