# Liouville Elliptic-Recursion Mechanism Pass

Date: 2026-05-30

## Target

GitHub issue #697 flags the remaining CFT quoted-theorem proof debt.  This
pass targets the Zamolodchikov elliptic-recursion quoted theorem in Volume V,
Chapter 13.

## Change

- Added the Verma-module mechanism behind the recursion rather than leaving the
  displayed formula as a black box.
- Wrote the all-level Gram/Shapovalov projector form for Virasoro block
  coefficients.
- Identified Kac-determinant simple zeros at \(h=h_{m,n}\) and the singular
  vector \(\chi_{m,n}\) at level \(mn\).
- Explained why the null submodule is a highest-weight module of weight
  \(h_{m,n}+mn\).
- Displayed the rank-one singular part of the inverse Shapovalov form and
  the factorization of the residue into left/right fusion polynomials.
- Explained the origin of the \((16q)^{mn}\) factor from the level shift
  \(z^{mn}\) and the leading relation \(z=16q+O(q^2)\).
- Stated the remaining theorem boundary precisely: large-\(h\) bounds,
  convergence of the iterated Mittag-Leffler expansion, and compatibility of
  singular-vector normalization with the DOZZ normalization.

## Status

The quoted theorem remains a theorem boundary.  This pass exposes the
representation-theoretic mechanism used by the monograph and prevents the
recursion from reading as an unsupported formula.  It does not close #697:
Liouville analytic sewing, DOZZ/FZZT construction boundaries, VOA modularity
boundaries, and rational/nonrational sewing remain open development tasks.
