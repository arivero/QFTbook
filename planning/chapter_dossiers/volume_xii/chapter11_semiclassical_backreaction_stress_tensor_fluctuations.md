# Chapter 11: Semiclassical Backreaction And Stress-Tensor Fluctuations
Source-File: monograph/tex/volumes/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.tex

## Source Position

This chapter follows the fixed-background horizon and cosmological
applications while consuming the earlier microlocal, locally covariant,
pAQFT, point-splitting, and trace-anomaly machinery.  It turns the
renormalized stress tensor into a source for geometry and records the
fluctuation data required for controlled backreaction.

## Notation Inventory

- `T^{ren}_{mu nu}`: locally covariant renormalized stress tensor.
- `W[g]`: renormalized metric-source functional.
- `E^{grav}_{mu nu}`: metric Euler tensor of the gravitational EFT action.
- `G_N`, `Lambda`, `alpha`, `beta`: gravitational EFT coordinates.
- `H^{(1)}_{mu nu}`, `H^{(2)}_{mu nu}`: metric variations of local curvature
  actions; `H^{(2)}` is the same Ricci-squared tensor as `J` in the
  point-splitting chapter.
- `B`: backreaction datum including metric class, algebras, states,
  renormalization scheme, and initial/boundary data.
- `G^{ret}_{mu nu,rho sigma}`: retarded stress-tensor response kernel.
- `N_{mu nu,rho sigma}`: stress-tensor noise kernel.
- `N(f,k)`, `star_{S,V}`: the unordered algebra covariance of centered
  smeared stress observables and the interacting product used to define it.
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
- `N_sp`, `kappa_N`, `bar kappa`: number of independent matter species, the
  species-dependent gravitational coupling, and the fixed large-species
  semiclassical coupling `bar kappa=N_sp kappa_N`.
- `Sigma_{omega,H}`, `rho_lambda`, `q_a`, `j_a^{(lambda,pot)}`: Wick-square
  variance of a centered quasifree Hadamard state in a chosen Hadamard
  coordinate, the first-order `lambda phi^4` potential-insertion source
  coordinate, and its projection into the retained semiclassical response
  sector.
- `R_{omega,H}(x,y)`, `W_omega(x,y)`, `N_{ab}^{(lambda,pot)}`: smooth
  Wick-coordinate remainder, full separated state two-point function, and
  finite retained potential-noise matrix for the second-order `lambda phi^4`
  stress-noise coordinate.
- `B_T`, `P_{ker B_T}`, `j_min`, `k`, `N_diag`, `N_miss`, `N^{full}`: finite
  retained stress-divergence Ward map, its least-norm diagnostic projector, the unresolved
  conserved source component, the projected diagnostic covariance, the missing
  Ward-clean interacting covariance budget, and the full interacting noise
  covariance tested by the Ward identities.
- `R^{ret}_{Th}`, `Q_T`, `G_h`, `D_sc`: typed retained stress response from
  metric perturbations to stress coordinates, the one-point/contact Ward map,
  the metric gauge generator, and the full linearized semiclassical Hessian.
- `q_h`, `p_T`, `R^{ret}_{red}`: metric reduction, stress projection, and
  intrinsic reduced retarded response, defined only when
  `p_T R^{ret}_{Th}` annihilates the full kernel of `q_h`.
- `T_int^{S,V}`, `K^{ret}`, `N(T^i,T^j)`: the scheme-fixed interacting
  stress tensor, its retained retarded response kernel, and the component
  covariance/cross-covariance entries required to assemble full interacting
  stress-tensor noise.
- `rho_lambda(t)`, `delta p_corr`, `B_FLRW`, `N_zeta`: the homogeneous FLRW
  potential density, Ward-closing interacting pressure correction, retained
  cosmological conservation map, and stress-noise covariance for the
  interacting cosmological source/noise closure.
- `Gamma_IF`, `h_c`, `h_Delta`, `R_IF`: retained closed-time-path influence
  functional, average/difference metric perturbations, and the residual outside
  the quadratic interacting backreaction package.
- `D_0`, `R^{ret}`, `D_full`, `Omega_EFT,+`, `M_{0,+}`, `eta_+`,
  `eta_X`: the reduced gravitational/local-contact operator, retained
  interacting stress-tensor feedback, full linearized backreaction operator,
  declared EFT analytic domain, dissipative Hardy inverse/small-gain data, and
  finite-window history-space small-gain parameter for neutral propagation.
- `Xcal`, `Ycal`, `G_full`, `M_full`, `B_Xcal(r_h)`, `C_2`, `L_st`,
  `epsilon_nl`, `kappa_nl`, `r_N`, `Delta_N(r_h)`: retained metric/source
  history spaces, the full retained inverse and nonlinear finite-window chart
  data controlling the self-map, state transport, omitted residuals,
  contraction constant, and noise-validity budget.
- `X`, `ell_X`, `Q^X`, `R_X`, `Delta_X^{mean}`: a retained metric observable,
  its linear and quadratic response in the same chart, its controlled
  remainder, and the observable mean shift after Einstein-Langevin metric
  fluctuations are included.
- `H=h_*+Z`, `rho_h`, `E_h`, `r_X^{exit}`: the retained leading-Gaussian metric
  vector around the deterministic nonlinear mean solution, its chart margin,
  chart-exit event, and the out-of-chart observable budget needed before local
  Taylor control is averaged.

## Claim Ledger

- Defines the metric variation convention for the stress tensor and proves
  the diffeomorphism Ward identity by varying a compactly supported flow.
- Defines the renormalized stress tensor as a locally covariant
  operator-valued distribution and records its finite curvature ambiguity.
- Defines the gravitational EFT action, records the curvature-squared Euler
  tensors \(H^{(1)}\) and \(H^{(2)}\) in the metric-variation convention fixed
  earlier in Volume XII, gives the local variational calculation and trace
  checks in four dimensions, and fixes the Ricci-squared derivative signs by
  the Palatini/Weyl convention rather than by self-contraction of the displayed
  formula.  The tensor \(H^{(2)}_{\mu\nu}\) is identified with
  \(J_{\mu\nu}\) from the point-splitting finite-local-freedom basis.
- Links the semiclassical Einstein equation to the Volume XII control-level
  classification and to the chapter's observable-output chain: all
  backreaction statements here are conditional semiclassical control until the
  locally covariant algebra, admissible state class, renormalized stress
  tensor, gravitational EFT coordinates, state transport, response/noise
  window, and retained metric observable are fixed together.
- Defines a semiclassical solution as a pair \((g,\omega)\), not merely a
  metric, and formalizes the backreaction datum.
- Derives the linear-response kernel from the retarded stress-tensor
  commutator plus local contact terms, then differentiates stress conservation
  to obtain the typed linearized diffeomorphism Ward identity
  `div delta<T>[h] + (delta div)_h <T> = 0`.  The response divergence includes
  one-point stress and CTP contact terms; pure metric gauge perturbations
  Lie-differentiate the background stress and are null only for the complete
  semiclassical Hessian on a mean-equation background.
- Defines the noise kernel as the unordered symmetrized connected covariance
  of already renormalized smeared stress observables in one algebra/state,
  proves positivity on real test tensors, and obtains the bidistribution from
  the continuity of that bilinear form.  Time-ordered contact freedom is kept
  on the response/effective-action side; it is not an independent noise
  covariance parameter.
- Derives the KMS fluctuation-dissipation relation for stationary states.
- Defines the Einstein-Langevin approximation as a Gaussian generalized
  random tensor with covariance \(N\), and gives the induced metric
  covariance through a retarded inverse.
- Adds the large-`N_sp` semiclassical scaling window: for independent identical
  matter sectors, `<T^{(N_sp)}>=N_sp t`, `N^{(N_sp)}=N_sp N_1`, and
  `bar kappa=N_sp kappa_N` fixed give a finite mean geometry but metric
  covariance of size `bar kappa^2 N_1/N_sp`.  The text also states the failure
  modes: fixed `G_N`, coherent or pairwise-correlated species noise, growing
  response bounds, growing one-sector cumulants, and species-cutoff violations.
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
- Adds a retained Ward-diagnostic layer for interacting sources.  The potential
  source has divergence `-partial_nu rho_lambda` when the Wick-square
  coordinate varies, so the Bogoliubov/interacting-field correction and local
  contact/composite counterterms must supply the missing Ward term.  In the
  retained response sector this is encoded by a finite stress-divergence Ward
  map `B_T`, the condition `B_T j^{full}=0`, the least-norm diagnostic
  projector `P_{ker B_T}=I-B_T^*(B_T B_T^*)^{-1}B_T`, and the general
  conserved source `j^{full}=P_{ker B_T}j^{raw}+k`, `k in ker B_T`.  The
  physical source/noise are
  the objects constructed by the full pAQFT renormalization procedure;
  projecting a partial source or partial covariance is recorded only as a
  diagnostic/model choice.  The section now cross-links this retained
  diagnostic to the upstream local-coupling Ward ledger in Chapter 10, where a
  nonconstant switching function is treated as an external coupling source
  rather than as a conserved stress tensor.
- Adds a finite retained Ward-completion laboratory.  A two-coordinate retained
  model with `B_T=(1,-1)` turns a nonconserved potential-only source
  `(3,1) rho_*` into the least-norm conserved diagnostic source
  `(2,2) rho_*`, but leaves the transverse conserved component to the full
  interacting stress-tensor construction.  The same example projects a
  positive partial noise matrix to a Ward-clean diagnostic covariance while
  recording that a positive missing Ward-clean covariance changes the metric
  fluctuation budget.  This makes the physics rule concrete: the metric
  response is fed by the scheme-fixed conserved source and full connected
  stress noise, not by a potential-sector coordinate alone.
- Adds the full retained interacting stress-tensor/noise package for
  backreaction.  A scheme-fixed `T_int^{S,V}` supplies the mean source,
  unordered connected symmetrized noise, and retarded response in one
  prescription.  If
  `T_int` is decomposed into potential, Bogoliubov, derivative, and counterterm
  components, the full noise is the double component-covariance sum
  `sum_{i,j} N(T^i,T^j)`, not the sum of separate component variances.  Local
  c-number curvature ambiguities shift the mean but not connected noise, while
  finite composite-operator mixing changes the noise through cross terms.
  Independently adding a local contact directly to the noise is rejected even
  when the contact is Ward-clean, because it can destroy positivity.
  Thus Ward-clean retained data are accepted as physical backreaction inputs
  only after the full pAQFT stress tensor and its renormalized products, or
  controlled residuals for the missing entries, have been supplied.  After the
  issue #854 correction this package also inherits the pAQFT functional-space
  condition: local/equicausal closure is needed for Peierls/star/time-slice
  operations, while bare microcausal admissibility is only a pointwise
  pairing test.
- Adds a homogeneous FLRW interacting source/noise closure.  A time-dependent
  `lambda phi^4` potential density has equation of state `p=-rho` but is not
  conserved when `dot rho_lambda` is nonzero; the Bogoliubov,
  state-transport, derivative, and counterterm pieces must supply the
  correction pressure and density terms making the linearized Bianchi identity,
  Friedmann response, Raychaudhuri response, and stress-noise Ward identities
  agree.  The dot-density noise coordinate is treated as the derivative of the
  density noise, with derivative-consistency conditions on its covariance.  This
  turns the potential coordinate into a cosmological backreaction datum only
  after the full pressure and noise package is present.
- Adds the closed-time-path consistency layer for the interacting package.  The
  retained quadratic influence functional in `h_Delta,h_c` has one mean source,
  one retarded kernel, and one positive connected-noise covariance, with no
  standalone `h_c h_c` term after equal-branch normalization.  The same package
  must satisfy retarded support, typed Ward identities for source/noise, the
  contact-corrected linearized Ward identity for response, the full-Hessian
  gauge identity on the mean-equation background, and the KMS
  fluctuation-dissipation relation in stationary states; otherwise the Langevin
  noise and dissipative feedback have been assembled from different theories
  rather than from one interacting stress tensor.  The reduced response is
  intrinsic only after a quotient-factorization theorem: a unique
  `R^{ret}_{red}` satisfying `R^{ret}_{red} q_h=p_T R^{ret}_{Th}` exists iff
  `p_T R^{ret}_{Th}` vanishes on the full kernel of `q_h`.  Gauge, constraint,
  and truncation kernels are kept as separate obligations.
- Adds the retained causal small-gain layer for interacting backreaction:
  after the full source/noise/response package is fixed in one scheme, the
  full linearized operator is `D_full=D_0-R^{ret}`.  A real-frequency
  small-gain number is recorded only as a diagnostic.  The dissipative route
  requires `D_0^{-1}` and `R^{ret}` to be Hardy/causal on a declared EFT
  analytic domain, with no uncontrolled high-frequency conclusion and
  `eta_+<1`.  Neutral stable propagation with physical real-axis boundary
  poles uses a finite-window Volterra/energy estimate in named history spaces
  instead.  Both routes produce a concrete `M_full` for the mean/noise
  amplification bounds, and covariance traces are read only as finite,
  smeared, trace-class, or spectral-density statements.
- Adds the nonlinear finite-window backreaction chart.  The retained equation
  is written as a Ward-clean fixed-point map
  `h=h_lin+G_full(Q_2(h,h)+S_st(h)+R_nl(h))` in one declared pair of history
  spaces `Xcal,Ycal`; the self-map and contraction tests combine the linear
  causal inverse bound with quadratic metric/source feedback, state-transport
  Lipschitz control, omitted residual size, and residual Lipschitz control.
  Bare `L^2` multiplier control is explicitly insufficient for the quadratic
  product estimate.
  The same chart refines the stochastic validity condition by adding missing
  connected-noise trace and nonlinear/state-transport noise budgets before
  the metric fluctuations are compared with the chart radius.
- Adds the retained metric-observable output layer.  A backreaction statement
  now has to pass from the controlled deterministic mean metric and
  leading-Gaussian Einstein-Langevin covariance to a gauge-invariant retained
  observable `X`: the text keeps the linear response, quadratic deterministic
  response, fluctuation bias `1/2 tr(Q^X C_h)`, observable covariance, Gaussian
  chart-exit probability, out-of-chart tail/integrability budget, and
  signal-to-noise test in the same Ward-clean chart.  The Gaussian law is a
  stated truncation about `h_*`, not the exact nonlinear stochastic pushforward,
  and the signal-to-noise denominator includes the declared quadratic, higher,
  and chart-exit covariance budgets.
- Records validity conditions and the EFT reduction-of-order treatment for
  higher-curvature terms.

## Calculation Checks

- `calculation-checks/semiclassical_backreaction_checks.py`: verifies the
  four-dimensional traces of \(H^{(1)}\) and \(H^{(2)}\), the Ricci-squared
  \(H^{(2)}\) Weyl-variation sign, a conformally flat derivative fixture that
  rejects the old derivative sign pattern, the KMS fluctuation-dissipation
  factor, positivity of a finite noise covariance,
  the Einstein-Langevin pushforward covariance identity, large-`N_sp`
  semiclassical scaling of finite mean source, `1/N_sp` source-noise and metric
  covariance, and `1/N_sp^2` third connected metric-source cumulant with
  negative controls for fixed `G_N`, coherent `N_sp^2` noise, pair-correlated
  species, and wrong higher-cumulant scaling, exact retained-sector
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
  metric-covariance trace bound, the typed linearized diffeomorphism Ward
  check with nonzero separated response divergence, one-point/contact
  cancellation, pure-gauge Lie-stress response, and full-Hessian gauge-null
  negative controls, the retained Ward-diagnostic projector for
  interacting source/noise coordinates with wrong-sign, transverse-ambiguity,
  projection-versus-physical-completion, projected-partial-noise versus
  full-noise, and unprojected-longitudinal-noise negative controls, the finite
  retained Ward-completion laboratory with explicit source repair,
  Ward-reduced metric response, projected partial covariance, missing
  Ward-clean covariance, and fluctuation-undercounting negative controls, the
  full
  retained interacting stress-tensor/noise package with component
  cross-covariances, finite composite-operator-mixing cross terms, and a
  c-number connected-noise negative control that can still pass the Ward test,
  plus a Ward-clean local-contact negative control that destroys positivity,
  the homogeneous FLRW interacting closure with correction pressure,
  Friedmann/Raychaudhuri compatibility, Ward-clean stress noise,
  derivative-consistent dot-density covariance, and potential-only source/noise
  negative controls, the closed-time-path influence-package test tying mean
  source, contact-corrected retarded response, and connected noise to
  equal-branch normalization, retarded support, typed Ward identities,
  positivity, and KMS/FDT compatibility, the reduced-response descent check
  with a strict inclusion `im G_h < ker q_h` negative control where two
  sections produce different matrices despite the gauge Ward identity, the
  compatible full-kernel factorization case, the causal small-gain
  feedback inverse for the full retained backreaction operator,
  Ward-clean source/noise inputs, mean-response and noise-amplification
  bounds, residual missing-noise trace propagation, retarded finite Neumann
  support, neutral finite-window propagation that fails global bounded-Hardy
  control, and singular-feedback, overlarge-feedback, hidden-upper-half-plane
  pole, globally bounded-Hardy neutral-propagation, unconserved-input, and
  conserved-but-unstable amplification negative controls, the nonlinear
  fixed-point chart self-map,
  residual-Lipschitz contraction, correction, Ward-clean nonlinear source,
  missing-noise, and
  stochastic validity budgets with negative controls for signed residual
  cancellation, omitted state transport, omitted residual variation, bounded
  non-Lipschitz residuals with multiple fixed points, overlarge quadratic
  feedback, bare-L2 product bounds, and linear-noise-only validity, the retained metric-observable
  output check that converts the mean metric and covariance to observable mean
  shift, leading-Gaussian truncation, fluctuation bias, covariance, Gaussian chart-exit/tail budgets, and
  signal-to-noise with negative controls for gauge-variant coordinate probes,
  omitted fluctuation bias, divergent out-of-chart remainders despite small
  variance, omitted chart-exit variance, nonlinear Gaussian pushforwards
  mislabeled as exact Gaussian laws, partial-covariance undercounting, and confusing noise domination
  with invalidity, and the low-energy root selected
  by reduction of order in a toy higher-derivative equation.
- `calculation-checks/curvature_squared_euler_convention_checks.py`: verifies
  the shared \(H^{(2)}_{\mu\nu}=J_{\mu\nu}\) convention with the
  point-splitting chapter and the trace-anomaly \(R^2\) scheme coordinate.

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
- 2026-06-08 issue #929 pass: added the explicit
  \(H^{(2)}_{\mu\nu}=J_{\mu\nu}\) cross-reference back to the point-splitting
  finite-local-freedom basis and moved the Ricci-squared sign regression into
  a shared cross-chapter check.  The finite-scheme transport now uses the same
  tensor basis as the point-splitting ambiguity and the trace-anomaly
  \(R^2\)-coboundary coordinate audit.
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
  source decomposition and Hollands--Wald conservation requirements, separating
  the restricted Wick-square shift from independent `Phi^4`/stress-tensor
  finite renormalizations, and replacing the signed response estimate by an
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
- 2026-06-04 issue #729 control-level linkage: added an explicit backlink from
  the semiclassical Einstein equation to the Volume XII control-level matrix.
  This keeps the chapter's mean-response and noise calculations inside their
  conditional backreaction status rather than letting them read as a general
  interacting semiclassical existence theorem.
- 2026-06-04 issue #746 Ward-diagnostic correction: revised the retained
  Ward-map passage so the orthogonal projector is only an admissible-subspace
  diagnostic or explicit least-norm model.  The text now parameterizes
  \(j^{\rm full}=j_{\rm min}+k\), assigns \(k\) and the missing noise
  cross-covariances to the full pAQFT construction, and the companion includes
  source/noise counterexamples showing that projection can erase physical
  conserved source and fluctuation data.
- 2026-06-04 issue #729 interacting-package pass: added
  `ca:semiclassical-interacting-stress-noise-package`, which upgrades the
  retained Ward-clean diagnostics into a full backreaction-ready package:
  mean source, connected noise, and retarded response must all come from the
  same scheme-fixed interacting stress tensor.  The new finite companion checks
  that component variances alone fail, cross-covariances restore the
  Ward-clean full noise, finite operator mixing changes noise through cross
  terms, and c-number curvature counterterms must not be inserted into
  connected noise even when the resulting wrong covariance remains Ward-clean.
- 2026-06-04 issue #729 influence-package pass: added
  `ca:semiclassical-interacting-influence-package`, which requires the
  interacting mean source, retarded response, and connected noise to arise as
  the quadratic closed-time-path derivative data of one scheme-fixed influence
  functional.  The companion checks equal-branch normalization, Ward-clean
  source/response/noise, retarded time support, positive noise, a pure-Ward
  decoupling direction, KMS/FDT noise normalization, and negative controls for
  advanced support, independent noise spectra, and spurious `h_c h_c` terms.
- 2026-06-04 issue #729 small-gain pass: added
  `ca:semiclassical-backreaction-small-gain-stability`, which turns the
  scheme-fixed interacting source/noise/response package into an actual
  retained backreaction control test.  The new companion checks the exact
  feedback inverse, the bounded-response and covariance trace estimates,
  residual missing-noise propagation, and the fact that Ward-clean data can
  still fail through singular or strongly amplifying metric feedback.
- 2026-06-04 issue #729 nonlinear-chart pass: added
  `ca:semiclassical-nonlinear-backreaction-chart`, which extends the linear
  small-gain layer into a finite retained-sector existence/stability criterion
  for the mean solution and its fluctuations.  This is architecture work: the
  text now requires one matched chart containing the interacting
  source/noise/response package, Ward-clean constraint reduction, quadratic
  nonlinear feedback, state transport, residual size budgets, residual
  Lipschitz budgets, and a fluctuation radius.  The companion rejects signed
  residual cancellations, omitted state-transport Lipschitz control, omitted
  residual variation, bounded non-Lipschitz residuals with multiple fixed
  points, overlarge nonlinear feedback, and linear-noise-only validity
  estimates.
- 2026-06-04 issue #749 residual-Lipschitz repair: re-audited
  `ca:semiclassical-nonlinear-backreaction-chart` after the bounded-residual
  counterexample.  The controlled approximation now separates the residual
  size needed for the self-map estimate from the residual Lipschitz constant
  needed for Picard uniqueness, revises
  \(\kappa_{\rm nl}=M_{\rm full}(2C_2r_h+L_{\rm st}+L_{\rm R})\), and states
  that a purely bounded \(h\)-dependent residual cannot by itself support a
  contraction claim.  The companion adds an omitted-residual-variation negative
  control and the one-dimensional bounded non-Lipschitz residual with three
  fixed points.
- 2026-06-04 issue #729 large-species scaling pass: added
  `ca:semiclassical-large-n-scaling-window`, which states the physical
  parametric regime behind the semiclassical mean equation and
  Einstein-Langevin fluctuations.  With \(N_{\rm sp}\) independent identical
  matter sectors and \(\bar\kappa=N_{\rm sp}\kappa_N\) fixed, the mean geometry
  remains finite while metric covariance is \(O(1/N_{\rm sp})\) and higher
  connected metric cumulants are further suppressed.  The text also records
  the failure modes: fixed \(G_N\), correlated or coherent species noise,
  growing response bounds/cumulants, and species-cutoff violations.  The
  companion checks the finite mean, `1/N_sp` covariance, `1/N_sp^2` third
  cumulant, and negative controls for each false large-`N_sp` shortcut.
- 2026-06-05 issue #729 Ward-completion laboratory: added
  `ex:semiclassical-retained-ward-completion-laboratory`, a concrete
  two-coordinate retained source/noise model showing that a potential-only
  source can be repaired as a least-norm diagnostic but cannot be treated as
  the physical conserved stress source.  The paired finite check verifies the
  explicit projector algebra, Ward-reduced response, positive projected
  covariance, and the missing Ward-clean noise contribution that must remain in
  the Einstein--Langevin fluctuation budget.
- 2026-06-05 issue #729 finite scheme-transport pass: added
  `prop:semiclassical-finite-scheme-transport`, which turns the chapter's
  statement that stress-tensor finite ambiguities are gravitational-coordinate
  changes into an explicit invariant residual identity.  The pass uses
  \(M_{\rm P}^2\) and \(\lambda_{\rm grav}=M_{\rm P}^2\Lambda\) as the clean
  coordinates, transports the local linear-response/contact term with the
  curvature-squared gravitational operator, and states that deterministic
  c-number curvature shifts cancel from connected noise.  The paired finite
  check rejects stress-only transport, gravity-only transport, one-sided
  local-response transport, and adding deterministic curvature shifts to
  connected Einstein--Langevin noise.  This is still a scheme-coordinate
  consistency result; it does not construct the interacting stress tensor,
  state-transport map, or infinite-dimensional semiclassical existence theorem.
- 2026-06-05 issue #729 observable-output pass: added
  `ca:semiclassical-retained-metric-observable-output`, which closes the
  finite backreaction chain at the level of retained physical observables
  rather than metric-coordinate size.  The pass records the observable mean
  shift, the quadratic fluctuation bias, the induced covariance, and a
  signal-to-noise criterion.  This is architecture work aimed at physics
  interpretation: a projected noise or a coordinate perturbation is not
  promoted to a self-averaging semiclassical prediction.
- 2026-06-05 issue #729 interacting FLRW closure pass: added
  `ca:semiclassical-flrw-interacting-source-noise-closure`, which turns the
  time-dependent `lambda phi^4` potential coordinate into a cosmological
  conservation problem.  The text derives the correction-pressure Ward closure,
  shows why potential-only `p=-rho` conflicts with simultaneous Friedmann and
  Raychaudhuri response when `dot rho_lambda` is nonzero, and imposes the
  corresponding Ward-clean stress-noise condition before Hubble noise is
  interpreted.
- 2026-06-06 issue #844 semiclassical observable-map pass: replaced the
  reader-facing control-level wording by a physics observable chain from
  locally covariant algebra/state/stress tensor through gravity coordinates,
  state transport, source/noise/response, mean metric/covariance, and retained
  observable output.  The paired finite check rejects the formal-equation-only,
  mean-only, noise-without-metric-covariance, wrong-order, and missing
  validity/detectability shortcuts.
- 2026-06-08 issue #729 printed-order pass: updated the source-position
  dossier and added an opening dependency map that names the upstream
  microlocal Hadamard state class, locally covariant algebra, pAQFT/free-field
  composite-stress prescription, point-splitting choices, and anomaly
  counterterm budget.  Backreaction remains conditional on joining those
  inputs to gravitational EFT coordinates and a response/noise window.
- 2026-06-08 issue #924 chart-exit pass: repaired the retained
  metric-observable output layer so local Taylor control is not averaged under
  an unstopped Gaussian without an exit budget.  The chapter now states the
  retained law `H=h_*+Z`, the chart margin and Gaussian exit bounds, the
  stopped/global/conditional alternatives for out-of-chart remainders, and the
  distinction between stochastic-law validity and signal-to-noise
  self-averaging.
- 2026-06-08 issue #923 noise/contact separation pass: repaired the noise
  kernel and interacting package so stress noise is the unordered covariance of
  centered stress observables in one declared algebra/state.  Time-ordered and
  metric-variation contact freedom is reserved for response/effective-action
  data.  The paired finite check rejects an independently added Ward-clean
  local noise contact that makes a positive covariance indefinite.
- 2026-06-08 issue #922 typed Ward-response pass: repaired the response and
  influence-package architecture rather than adding another retained cell.  The
  chapter now derives the linearized diffeomorphism Ward identity with the
  connection variation of the background one-point stress, separates
  `B_T:V_T -> V_{div T}` from the metric gauge generator and full
  semiclassical Hessian, assigns gauge null directions to the complete
  gravitational-plus-matter operator, and treats FLRW dot-density noise as a
  derivative-consistent coordinate.  The paired finite check includes a
  nonzero-background negative control where naive response transversality fails
  but the contact-corrected Ward identity and full-Hessian gauge identity hold.
- 2026-06-08 issue #921 Ricci-squared sign pass: corrected the
  \(H^{(2)}_{\mu\nu}\) derivative signs for the inverse-metric variation of
  the half-normalized Ricci-squared gravitational action.  The chapter now has
  \(g^{\mu\nu}H^{(2)}_{\mu\nu}=+2\Box R\) and records the matching Weyl
  variation of the un-halved action.  The paired finite check no longer merely
  contracts the displayed tensor: it tests the Weyl coefficient and a
  non-Einstein conformally flat derivative fixture, both of which reject the
  old sign pattern.  Downstream uses of the \(\beta H^{(2)}\) term were audited
  as coordinate-level scheme-transport and response inputs using the corrected
  convention.
- 2026-06-08 issue #920 causal small-gain pass: replaced the real-window
  small-gain conclusion by a causal Hardy/upper-half-plane small-gain
  hypothesis.  Real-frequency samples are now explicitly only diagnostics; the
  retarded inverse follows from analytic Neumann convergence and the
  Paley-Wiener/Hardy boundary-value theorem, with no unstable poles in the
  reduced sector.  The text distinguishes forced-response/noise-pushforward
  control from full initial-value stability and requires omitted-mode residual
  budgets before retained covariance is interpreted physically.  The paired
  finite check adds both a causal lower-triangular Neumann inverse and an
  adversarial scalar transfer function whose real samples pass while an
  upper-half-plane pole makes the evolution unstable.
- 2026-06-08 issues #937/#938/#935/#931 pass: repaired the Vol XII Ch11
  backreaction architecture rather than adding another finite cell.  The
  causal inverse layer now separates strictly dissipative bounded-Hardy control
  from neutral finite-window retarded propagation, restricts complex-frequency
  claims to a declared EFT domain, and types covariance traces as finite,
  smeared, trace-class, or spectral-density statements.  The nonlinear chart
  now uses named history spaces `Xcal,Ycal` with a product hypothesis, so the
  fixed-point map no longer borrows a bare `L^2` multiplier norm.  The
  observable law is explicitly the leading-Gaussian truncation about the
  deterministic nonlinear mean, and the final signal-to-noise denominator uses
  the declared higher and chart-exit covariance budgets.
- 2026-06-08 issue #933 reduced-response descent pass: replaced the
  section-based reduced response claim by the universal factorization
  criterion `ker q_h <= ker(p_T R^{ret}_{Th})`.  The pure gauge quotient is
  now only a special case; extra constraint, discarded, or truncation kernels
  must be checked separately before the reduced feedback, small-gain number,
  and covariance are interpreted as intrinsic.  The paired finite check rejects
  the old insufficient hypothesis with `im G_h` strictly contained in
  `ker q_h` and two sections that give different projected responses.
