# Zhu One-Point Modular Mechanism Pass

Date: 2026-05-30

## Target

GitHub issue #697 flags the remaining Volume V quoted-theorem proof debt.  This
pass targets the Zhu modular covariance theorem for torus one-point blocks in
Volume V, Chapter 12.

## Change

- Expanded the point-of-use explanation of
  `qthm:zhu-one-point-modular-covariance`.
- Explained why the zero mode \(o(v)\) gives a finite-energy trace on each
  ordinary module.
- Described the once-punctured torus coordinate change
  \((z,\tau)\mapsto(z/(c\tau+d),(a\tau+b)/(c\tau+d))\).
- Separated primary insertions, which acquire the scalar factor
  \((c\tau+d)^{h_v}\), from descendant insertions, which mix with
  lower-descendant terms and quasimodular \(G_2\)-type contributions.
- Identified the finite \(C_2\)-cofinite marked-state trace system as the
  algebraic mechanism behind finite modular closure.
- Stated the remaining analytic theorem input: convergence of torus traces,
  continuation of the finite solution space, and invariance under \(S,T\).

## Status

The theorem remains quoted.  The point of this pass is to prevent the
one-point modular covariance formula from functioning as an unexplained black
box; it exposes the algebraic and geometric mechanism used later when torus
one-point functions constrain full-CFT OPE tensors.
