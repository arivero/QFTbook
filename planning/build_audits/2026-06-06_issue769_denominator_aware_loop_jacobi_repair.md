# Issue #769 denominator-aware loop Jacobi repair

Date: 2026-06-06

## Scope

This pass addresses the critical review finding on
`ca:loop-level-jacobi-repair-double-copy-null` in Volume II, Chapter 6.  The
previous version repaired a Jacobi defect by the common numerator shift
\(N_\alpha \mapsto N_\alpha - J/3\).  That was only denominator-free algebra:
it did not test the generalized-gauge condition for routed cubic graphs with
different propagator products.

The corrected manuscript block keeps the routed denominators in the criterion.
For a Jacobi triplet with colors \(c_a+c_b+c_c=0\), denominators
\(D_a,D_b,D_c\), defect \(J=N_a+N_b+N_c\), and local surface module
\({\cal S}\), a repair is now required to satisfy both

- numerator repair: \(\Delta_a+\Delta_b+\Delta_c=-J\);
- gauge-nullness:
  \(\sum_\alpha c_\alpha \Delta_\alpha/D_\alpha \in {\cal S}\).

It explicitly rejects the common shift when the denominators differ, because
\(-(J/3)\sum_\alpha c_\alpha/D_\alpha\) is not zero in general.

## Substance Audit

- The replacement is physics-facing: it concerns generalized unitarity,
  generalized gauge transformations, and the validity of double-copy
  numerator repairs at loop level.
- It moves the discussion from a finite color identity to the actual integrand
  object whose graph denominators control gauge-nullness.
- It records a sufficient repair form,
  \(\Delta_\alpha=D_\alpha\alpha\) with
  \(\alpha(D_a+D_b+D_c)=-J\), while keeping the locality/divisibility
  condition visible.
- It separates two claims that the older paragraph had conflated: preserving
  the gauge-theory integrand and producing a gravity-null double-copy
  variation.  The latter still requires a Jacobi-satisfying second copy or a
  separately proved gravity-null surface term.

## Negative Controls

- Unequal denominators make the common \(-J/3\) repair non-null even though it
  fixes \(N_a+N_b+N_c\).
- Clearing denominators does not rescue the common shift; the cleared
  numerator relation is weighted by the complementary products
  \(D_{\rm com}/D_\alpha\).
- A denominator-weighted repair is local only when the Jacobi defect is
  divisible in the declared local quotient or is supplied by declared surface
  generators.
- A graph-dependent gauge-null shift can preserve the gauge integrand without
  repairing the numerator Jacobi relation, and it can still change a defective
  double-copy integrand.

## Evidence Companion

`calculation-checks/generalized_unitarity_reduction_checks.py` now tests the
denominator-aware criterion in
`check_loop_level_jacobi_repair_double_copy_null()`.  The check uses exact
rational arithmetic with an adversarial triplet

\[
  c=(1,2,-3),\qquad D=(2,3,5),\qquad N=(5,7,-2).
\]

It verifies:

- the common repair restores the numerator sum but is not gauge-null;
- the same failure persists after clearing denominators;
- the denominator-weighted repair with \(\Delta_\alpha=-D_\alpha\) is
  gauge-null and repairs the Jacobi defect;
- a nondivisible defect is rejected as nonlocal in the finite local quotient;
- the double-copy variation is null only against a Jacobi-satisfying second
  copy, and is nonzero against a defective one.

## Verification

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
- `tools/run_calculation_checks.sh --python-only`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build completed with a clean log scan at 3456 pages.

No issue-tracking, review-monitoring, or planning directive language was added
to the monograph TeX; those records remain in the planning dossier and audit
trail.
