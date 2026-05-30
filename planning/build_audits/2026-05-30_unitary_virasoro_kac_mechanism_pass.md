# Unitary Virasoro Kac-Mechanism Pass

Date: 2026-05-30.

Scope:
`monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
and `calculation-checks/cft_virasoro_minimal_checks.py`.

## Repair

- Expanded the quoted-theorem boundary for the unitary Virasoro
  highest-weight classification.
- Added the Kac-determinant mechanism in the \(c<1\) parametrization:
  \[
    c=1-6(b^{-1}-b)^2,\qquad
    h_{r,s}(b)=
    \frac{(r b^{-1}-s b)^2-(b^{-1}-b)^2}{4}.
  \]
- Stated the level-\(N\) determinant factorization
  \[
    \det M^{(N)}(c,h)
    =
    C_N
    \prod_{rs\le N}
    (h-h_{r,s}(b))^{p(N-rs)}
  \]
  and explained how unitarity converts this algebraic singular-vector
  information into all-level positivity and the discrete
  \(b^2=m/(m+1)\) minimal-series classification.
- Extended the exact minimal-model calculation companion to check that the
  level-two Gram determinant vanishes at \(h_{1,2}^{(m)}\) and
  \(h_{2,1}^{(m)}\) for \(m=3,\ldots,11\).

## Standard Applied

The Friedan--Qiu--Shenker/Goddard--Kent--Olive classification remains a
quoted theorem because the all-level positivity and exhaustion argument is not
proved in full in this pass.  The manuscript now exposes the determinant and
interlacing mechanism instead of using the theorem as an unexplained
black-box classification.
