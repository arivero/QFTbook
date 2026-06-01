# Issue #594 N=(4,4) Symmetric-Product Marginal-Tangent Pass

## Scope

This pass advances the two-dimensional worked-example component of GitHub
issue #594.  The previous manuscript had the symmetric-product orbifold and
twist-field deformation machinery, but the D1--D5-style exactly marginal
two-cycle deformation was only sketched.

## Manuscript Changes

- Expanded Volume V, Chapter 11 with
  `constr:n4-symmetric-product-two-cycle-marginal`.
- The construction treats the example as local CFT data: a compact
  \(\mathcal N=(4,4)\), \(c_0=6\), seed; a transposition twist sector; a
  spin-field dressing to a \((1/2,1/2)\) chiral primary; and the top component
  obtained by left and right supercharge modes.
- The text separates the weight calculation, the finite-orbifold
  transposition class projection, and the exact-marginality integrability
  statement.  Exact marginality is tied back to the source-coordinate
  criterion in Volume III rather than inferred from geometric language.
- The local tangent count is recorded as \(d_{\rm seed}+4\), giving
  \(16+4=20\) for a toroidal seed and \(80+4=84\) for a K3 seed, while global
  arithmetic quotients and singular loci are left as additional global CFT
  data.
- Volume III's conformal-manifold framework now cross-links to this
  symmetric-product construction.

## Calculation Check

- Added `calculation-checks/n4_symmetric_product_marginal_checks.py`.
- The check verifies the \(c=6\) length-two twist weight \(3/8\), the
  spin-field dressing to \(h=1/2\), the supercharge top-component weight
  \(h=1\), normalized transposition class sums, and the \(20\)- and
  \(84\)-dimensional local tangent counts.

## Status

This pass should not close #594.  It adds the requested two-dimensional
symmetric-product worked example at the local tangent level.  Remaining work
includes fuller global conformal-manifold geometry, Kähler/special geometry
where it is justified by supersymmetric hypotheses, and non-supersymmetric
examples with actual source-coordinate control.
