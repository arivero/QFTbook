# Free Scalar Weyl AQFT Example Pass

## Scope

Volume IV, Chapter 3 now contains an explicit massive free scalar Weyl-net
benchmark immediately after the Haag--Kastler \(C^*\)-net definition.

## Mathematical Content Added

- Defined the mostly-plus Klein--Gordon operator
  \(P_m=\partial^\mu\partial_\mu-m^2\), its retarded/advanced fundamental
  solutions, and the causal propagator.
- Constructed the symplectic quotient
  \(C_c^\infty(M;\mathbb R)/P_mC_c^\infty(M;\mathbb R)\).
- Proved well-definedness, antisymmetry, and nondegeneracy of the symplectic
  form \(\sigma_m([f],[g])=\int f\Delta_m g\).
- Defined the Weyl \(C^*\)-algebra and the local subalgebras
  \(\Obs_m(\mathcal O)\).
- Verified isotony, spacelike commutativity, and Poincare covariance directly
  at the level of bounded Weyl generators.
- Proved the time-slice property by constructing a representative supported
  in a Cauchy-surface collar using retarded/advanced uniqueness.
- Added the quasi-free vacuum state only after the abstract net is defined, so
  the chapter keeps the net/state distinction explicit.

## Accuracy Notes

The pass also corrected the label on Figure `fig:aqft-local-net`: the isotony
arrow now uses the same subscript convention as Definition
`def:haag-kastler-cstar-net`.

## Verification Plan

Run the text and build harness after the edit:

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
