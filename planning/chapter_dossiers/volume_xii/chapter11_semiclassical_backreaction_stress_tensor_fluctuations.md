# Chapter 11: Semiclassical Backreaction And Stress-Tensor Fluctuations

## Source Position

This chapter follows perturbative algebraic QFT on curved backgrounds by
turning the renormalized stress tensor into a source for geometry and by
recording fluctuation data required for controlled backreaction.

## Notation Inventory

- `T^{ren}_{mu nu}`: locally covariant renormalized stress tensor.
- `W[g]`: renormalized metric-source functional.
- `E^{grav}_{mu nu}`: metric Euler tensor of the gravitational EFT action.
- `G_N`, `Lambda`, `alpha`, `beta`: gravitational EFT coordinates.
- `H^{(1)}_{mu nu}`, `H^{(2)}_{mu nu}`: metric variations of local curvature
  actions.
- `B`: backreaction datum including metric class, algebras, states,
  renormalization scheme, and initial/boundary data.
- `G^{ret}_{mu nu,rho sigma}`: retarded stress-tensor response kernel.
- `N_{mu nu,rho sigma}`: stress-tensor noise kernel.
- `xi_{mu nu}`: classical stochastic source in the Einstein-Langevin
  approximation.
- `L`: gauge-fixed linearized gravitational operator including local
  response terms.

## Claim Ledger

- Defines the metric variation convention for the stress tensor and proves
  the diffeomorphism Ward identity by varying a compactly supported flow.
- Defines the renormalized stress tensor as a locally covariant
  operator-valued distribution and records its finite curvature ambiguity.
- Defines the gravitational EFT action, records the curvature-squared Euler
  tensors \(H^{(1)}\) and \(H^{(2)}\) in the metric-variation convention fixed
  earlier in Volume XII, and gives the local variational calculation and trace
  checks in four dimensions without presenting the duplicated formula block as
  a new theorem.
- Defines a semiclassical solution as a pair \((g,\omega)\), not merely a
  metric, and formalizes the backreaction datum.
- Derives the linear-response kernel from the retarded stress-tensor
  commutator plus local contact terms.
- Defines the noise kernel as a renormalized symmetrized connected
  stress-tensor two-point distribution, proves positivity on real test
  tensors, and states the distributional conservation Ward identity.
- Derives the KMS fluctuation-dissipation relation for stationary states.
- Defines the Einstein-Langevin approximation as a Gaussian generalized
  random tensor with covariance \(N\), and gives the induced metric
  covariance through a retarded inverse.
- Records validity conditions and the EFT reduction-of-order treatment for
  higher-curvature terms.

## Calculation Checks

- `calculation-checks/semiclassical_backreaction_checks.py`: verifies the
  four-dimensional traces of \(H^{(1)}\) and \(H^{(2)}\), the KMS
  fluctuation-dissipation factor, positivity of a finite noise covariance,
  and the low-energy root selected by reduction of order in a toy
  higher-derivative equation.

## Figure Ledger

No figure is included in this pass.  Future figures should show the
stress-tensor response kernel, the noise-kernel pairing, and the hierarchy of
curvature, microscopic, and EFT scales.

## Anti-Wrapper Audit

- 2026-05-29: expanded the stress-tensor linear-response proof into a
  separated-point retarded-response derivation with explicit source-sign
  convention, causal support, microcausality, and the local diagonal terms
  coming from metric variation of composite fields and time-ordered-product
  extensions.
- 2026-05-30: demoted the duplicated curvature-squared Euler-tensor block from
  proposition/proof form to a variational-formula paragraph.  The formulae
  remain because they fix the gravitational EFT coordinates used in the
  semiclassical equation, but the theorem-level classification belongs to the
  point-splitting stress-tensor chapter.
