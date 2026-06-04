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
- `D(omega)`: finite retained response matrix for a gauge-fixed or
  gauge-invariant semiclassical sector.
- `M_I`: certified bound on the retained retarded inverse over a frequency
  interval.
- `C_h`: retained metric covariance induced by stress-tensor noise.
- `epsilon_mean`, `epsilon_fluc`: dimensionless mean-response and fluctuation
  smallness diagnostics.
- `Sigma_{omega,H}`, `rho_lambda`, `q_a`, `j_a^{(lambda,pot)}`: Wick-square
  variance of a centered quasifree Hadamard state in a chosen Hadamard
  coordinate, the first-order `lambda phi^4` potential-insertion source
  coordinate, and its projection into the retained semiclassical response
  sector.
- `R_{omega,H}(x,y)`, `W_omega(x,y)`, `N_{ab}^{(lambda,pot)}`: smooth
  Wick-coordinate remainder, full separated state two-point function, and
  finite retained potential-noise matrix for the second-order `lambda phi^4`
  stress-noise coordinate.
- `B`, `P_{ker B}`, `j_perp`, `N_perp`: finite retained Ward map, its
  conserved-sector projector, and the Ward-clean mean/noise data used in the
  interacting backreaction diagnostic.

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
- Links the semiclassical Einstein equation back to the Volume XII
  theorem-status spine: all backreaction statements in this chapter are
  conditional semiclassical control until the locally covariant algebra,
  admissible state class, renormalized stress tensor, gravitational EFT
  coordinates, state transport, and response window are fixed together.
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
- Adds a finite response-window diagnostic for semiclassical backreaction:
  after gauge fixing/constraint projection and reduction of order, the
  retained response matrix must have no unstable poles, a bounded retarded
  inverse, controlled mean response, and controlled noise pushforward.
- Adds a worked retained potential-source coordinate: the explicit potential
  insertion from a first-order `lambda phi^4` interaction in a centered
  quasifree Hadamard state gives
  `delta<T_{mu nu}>^{pot} = -rho_lambda g_{mu nu}` with
  `rho_lambda=lambda Sigma^2/8`, while the text states that the full
  interacting source also requires Bogoliubov/interacting-field corrections,
  time-ordered-product contact terms, interaction-dependent composite
  counterterms, and a conservation-compatible stress-tensor prescription.
  The homogeneous potential coordinate shifts
  `Lambda_eff^{pot}` by `8 pi G_N rho_lambda`, and the retained response
  check uses `||h_lambda^{pot}|| <= M_I |rho_lambda| ||q||`.
- Adds the corresponding retained potential-noise coordinate: the connected
  Wick-four covariance is
  `72 Sigma_x Sigma_y W_omega(x,y)^2 + 24 W_omega(x,y)^4`, where
  `W_omega=omega_2` is the full separated two-point function rather than the
  smooth Wick-coordinate remainder; the real part is taken after forming the
  polynomial for symmetrized Lorentzian noise.  The disconnected term is
  subtracted, the retained stress-noise matrix is positive as a covariance, and
  its metric pushforward satisfies
  `tr C_h^{(lambda,pot)} <= M_I^2 tr N^{(lambda,pot)}`.
- Adds a conservation-completion layer for interacting sources.  The potential
  source has divergence `-partial_nu rho_lambda` when the Wick-square
  coordinate varies, so the Bogoliubov/interacting-field correction and local
  contact/composite counterterms must supply the missing Ward term.  In the
  retained response sector this is encoded by a finite Ward map `B`, the
  condition `B j^{full}=0`, the projector
  `P_{ker B}=I-B^*(B B^*)^{-1}B`, and the Ward-clean noise covariance
  `N_perp=P_{ker B} N^{full} P_{ker B}^*`.  The text treats the projected
  potential coordinate as a diagnostic inside the full Hollands--Wald
  interacting stress tensor and its renormalized square.
- Records validity conditions and the EFT reduction-of-order treatment for
  higher-curvature terms.

## Calculation Checks

- `calculation-checks/semiclassical_backreaction_checks.py`: verifies the
  four-dimensional traces of \(H^{(1)}\) and \(H^{(2)}\), the KMS
  fluctuation-dissipation factor, positivity of a finite noise covariance,
  the Einstein-Langevin pushforward covariance identity, exact retained-sector
  mean-response and noise trace bounds for the finite response-window
  diagnostic, the first-order `lambda phi^4` potential-insertion source
  coordinate, its restricted local Wick-renormalization/cosmological-coordinate
  shifts, negative controls for independent quartic/stress-tensor finite
  counterterms and signed negative-density norm bounds, its retained response
  bound, the retained `lambda phi^4` potential-noise kernel with the
  connected Wick-four covariance using the full separated two-point function,
  disconnected-subtraction, dropped-mixed-term, same-state Wick-coordinate,
  smooth-remainder-only, and premature-real-part negative controls, quadratic
  coupling scaling, positivity of the retained noise matrix, its
  metric-covariance trace bound, the retained Ward-completion projector for
  interacting source/noise coordinates with wrong-sign, transverse-ambiguity,
  and unprojected-longitudinal-noise negative controls, and the low-energy root
  selected by reduction of order in a toy higher-derivative equation.

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
- 2026-06-03: added the finite response-window diagnostic for issue #729.  This
  is a physics-control insertion rather than a formal annex: it connects the
  semiclassical equation to bounded retarded response, absence of unstable
  poles, stress-tensor noise amplification, and small dimensionless metric
  fluctuation criteria.
- 2026-06-04: added a first-order retained potential-source coordinate for
  issue #729.  The calculation follows the explicit `lambda phi^4` potential
  insertion to a quasifree Hadamard-state output, its renormalization
  coordinate dependence, its cosmological-coordinate interpretation, and its
  retained metric-response bound; it explicitly states the conservation
  limitation of the potential-only display.
- 2026-06-04: aligned the interacting source example with issue #740 by
  stating that pure Hadamard-coordinate transport preserves expectations when
  states are transported, while the displayed density shift belongs to a
  fixed-state comparison of local Wick-renormalization prescriptions.
- 2026-06-04: repaired issue #741 by relabeling the example as a retained
  potential-insertion coordinate, adding the full interacting stress-tensor
  source ledger and Hollands--Wald conservation requirements, separating the
  restricted Wick-square shift from independent `Phi^4`/stress-tensor finite
  renormalizations, and replacing the signed response estimate by an
  absolute-value norm bound.
- 2026-06-04 issue #729 retained-noise pass: added the potential-sector
  stress-noise coordinate for the same `lambda phi^4` example.  This extends
  the mean-source response into an Einstein--Langevin fluctuation input:
  the text derives the connected Wick-four covariance, records the
  disconnected subtraction and the mixed `Sigma Sigma W_omega^2` term, feeds the
  retained noise through the response-window trace bound, and states that the
  full interacting noise also requires Bogoliubov, derivative, contact, and
  composite-counterterm pieces.
- 2026-06-04 issue #742 Wick-four cross-contraction correction: revised the
  retained potential-noise coordinate so separated contractions use the full
  quasifree two-point function \(W_\omega(x,y)=\omega_2(x,y)\).  The text now
  derives this from the typed \(\star_H\)/state Wick-exponential calculation:
  the \(H_+\) cross contraction from the product and the smooth state remainder
  \(R_{\omega,H}\) combine to \(W_\omega\).  The symmetrized Lorentzian noise
  takes the real part after the square and fourth power.  The finite companion
  now checks that a same-state Wick coordinate still has nonzero separated
  fourth-power noise, while smooth-remainder-only and premature-real-part
  formulas fail.
- 2026-06-04 issue #729 status-spine linkage: added an explicit backlink from
  the semiclassical Einstein equation to the Volume XII control-level matrix.
  This keeps the chapter's mean-response and noise calculations inside their
  conditional backreaction status rather than letting them read as a general
  interacting semiclassical existence theorem.
- 2026-06-04 issue #729 conservation-completion pass: added a retained Ward
  map for interacting source and noise coordinates.  This converts the earlier
  caveat about the nonconserved potential-only source into a concrete
  backreaction gate: the source/noise entering the response window must be
  projected to the conserved sector, while the missing longitudinal piece is
  assigned to the Bogoliubov, contact, and composite-counterterm part of the
  full interacting stress tensor rather than silently absorbed into the
  potential calculation.
