# 2026-06-07 Issue #850 Higgs-Metric Background-Field Gate

## Scope

This pass responds to the review that the previous Higgs-branch metric block
treated the signed component balance
`4 + 2 + 4 - 2 + 0 - 8 = 0` as a background-field derivation of the
two-derivative sigma-model counterterm.

## Change

Volume VII Chapter 08 now makes smooth Higgs-branch metric protection a
theorem-boundary input, `hyp:smooth-higgs-branch-metric-protection`, rather
than a result derived from component multiplicities.  The rank-one
background-field repair adds
`constr:higgs-branch-background-field-derivation-target` and the trace-log
coefficient `eq:higgs-branch-background-field-trace-log`.

The construction fixes an explicit four-dimensional `N=2` rank-one model,
a positive-FI smooth patch, a supersymmetric Wilsonian regulator, and a
background-field `R_xi` gauge.  It lists the nonminimal gauge operator,
Goldstone/eaten-hyper operator, ghost operator, vector-scalar/radial partners,
fermion operator, linear tangent vertices, seagulls, mixed diagrams, and
gauge-parameter cancellation that an actual determinant calculation must keep.

The old long-multiplet balance is retained as
`eq:higgs-branch-heavy-multiplet-balance-heuristic`, explicitly after the Ward
identity or trace-log calculation has supplied the pairing.  It is now a
diagnostic for missing sectors, not the computation of `Pi_mn`.

## Companion

`check_higgs_branch_background_field_derivation_gate()` now verifies that:

- the explicit rank-one model, regulator, patch, and gauge are specified;
- a bare component ledger lacks the required generated-operator, vertex,
  seagull, mixed-diagram, ghost, Goldstone, fermion, auxiliary-contact,
  gauge-parameter, and dimension-reduction slots;
- a complete operator blueprint has all slots and cancels a finite toy
  gauge-parameter residual only when ghosts and Goldstone/eaten-hyper data are
  included;
- the four-dimensional signed long-multiplet balance is only a diagnostic;
- dimensionally reduced `3d` and `2d` arguments cannot reuse the fixed
  four-dimensional gauge-field entry.

## Quality Boundary

This pass satisfies the acceptance criterion that the local metric equality is
not presented as a derived perturbative theorem from the multiplicity ledger.
It does not prove the all-order Higgs-branch metric theorem and does not
complete the full rank-one trace-log determinant calculation.  Those remain
larger theorem/proof obligations.

## Verification Plan

- Run the focused `susy_moduli_space_checks.py` companion and focused harness.
- Run Chapter 08 local theorem/display/prose/style audits and TeX leakage scan.
- Run dossier, calculation inventory, diff, full Python calculation checks, and
  full monograph build/log scan before staging.

## Verification Result

Completed on 2026-06-07.  The focused moduli-space companion, focused harness,
Chapter 08 strict text, negative-scope, style-density, theorem-form, and
display-label audits, TeX leakage scan, evidence-contract audit,
calculation-inventory audit, chapter-dossier audit, full Python
calculation-check suite, `git diff --check`, and full monograph build/log scan
all passed before staging.
