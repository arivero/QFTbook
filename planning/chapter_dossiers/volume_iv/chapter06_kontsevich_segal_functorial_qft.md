# Chapter 06: Kontsevich--Segal Functorial Quantum Field Theory

## Source Position

This chapter develops the Kontsevich--Segal functorial framework as a
foundational path-integral and OPE-oriented axiom system.  It belongs in the
Volume I foundations sequence after OS reconstruction because it compares
directly with OS, Wightman, and local-net data, while its source file lives in
the `volume_iv` framework cluster.

## Notation Inventory

- `D`: spacetime dimension.
- `V`: real tangent vector space at a point of an admissible background.
- `g`: nondegenerate complex symmetric bilinear form on `V`.
- `Q_{q,g}`: quadratic density \(\alpha\mapsto\alpha\wedge *_g\alpha\) on
  real \(q\)-forms.
- `lambda_a`: diagonal coefficients of an allowable complex metric.
- `theta_a = Arg(lambda_a)`: principal arguments used in the K-S angle
  criterion.
- `Bord_D^adm`: admissible complex-metric bordism category.
- `E(Y)`: topological state space assigned to a boundary germ `Y`.
- `Z(M)`: continuous amplitude map assigned to an admissible bordism.
- `H_Y`: Hilbert completion obtained from reflection positivity.

## Claim Ledger

- Defines Segal sewing for two-dimensional CFTs as a symmetric monoidal
  assignment from parametrized-boundary Riemann surfaces to topological
  vector spaces.
- Defines K-S allowability by positivity of
  \(\operatorname{Re}(\alpha\wedge *_g\alpha)\) for every real \(q\)-form.
- Proves the diagonal argument criterion
  \(\sum_a|\operatorname{Arg}\lambda_a|<\pi\).
- Defines the K-S functorial QFT datum: admissible complex bordisms,
  holomorphic metric/source dependence, collar locality, reflection, and
  reflection positivity.
- Derives the route from K-S data to OS Schwinger functions under explicit
  temperedness, covariance, and spectral clustering assumptions.
- States the Lorentzian-boundary theorem as a quoted theorem, with precise
  dependence on Kontsevich--Segal analytic hypotheses.
- Derives OPE from sewing under a stated annular spectral/nuclear expansion
  hypothesis.
- Records open construction problems for free fields, \(P(\phi)_2\),
  Liouville, two-dimensional Yang--Mills, three-dimensional constructive
  models, four-dimensional Yang--Mills, fermions/gauge fields, and extended
  K-S structures.

## Figure Ledger

- No figures in the first K-S chapter pass.  The geometric content is carried
  by equations and theorem/proposition environments.

## Calculation Checks

- `calculation-checks/ks_allowability_checks.py` verifies the angle criterion
  on representative diagonal metrics and checks positivity of all diagonal
  \(q\)-form coefficients for finite examples.

## Audit Notes

- 2026-05-26 issue #599 pass: added the K-S chapter, included it in the
  Volume I foundations sequence, linked it from Volume I chapter 1, Volume
  III radial quantization, and Volume VIII Atiyah--Segal TQFT, and added the
  finite allowability calculation check.
