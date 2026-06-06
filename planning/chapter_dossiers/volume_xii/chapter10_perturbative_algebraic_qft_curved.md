# Chapter 10: Perturbative Algebraic QFT On Curved Backgrounds

## Source Position

Volume XII follows the microlocal spectrum condition with perturbative
algebraic QFT, the local curved-background perturbation framework built from
Hadamard functions and causal factorization.

## Notation Inventory

- `E(M)`, `F^(n)`, `WF`: configuration space, functional derivatives, and
  wavefront sets.
- `F_loc(M)`, `F_muc(M)`: local and microcausal functionals.
- `H`, `star_H`, `Gamma_H`: Hadamard two-point function, star product, and
  contraction bidifferential.
- `w`, `alpha_w`: smooth Hadamard difference and induced algebra isomorphism.
- `H_F`: Feynman bidistribution used away from diagonals.
- `T_n`: time-ordered products.
- `sd(t)`: scaling degree of a distribution near a diagonal.
- `S(F)`, `S_V(F)`, `R_V(F)`: time-ordered exponential, relative S-matrix,
  and interacting Bogoliubov field.
- `Z`: local renormalization map between time-ordered-product choices.
- `V_{lambda,H}(g)`, `w_Delta`, `c`, `a_m`, `a_R`: compactly supported
  `lambda phi^4` interaction in a Hadamard Wick coordinate, smooth diagonal
  Hadamard-coordinate difference, and the separate local covariant finite
  Wick-renormalization scalar with its mass/curvature components.
- `chi`, `O_{lambda,H}`, `T^{(chi)}_{mu nu}`: local coupling/switching
  function, the corresponding renormalized interaction-density insertion, and
  the stress tensor satisfying the local-coupling Ward balance.
- `Sigma_{omega,H}`, `M_tad`, `E_ret^0`, `E_adv^0`: state Wick square,
  retained local tadpole mass coordinate, and free retarded/advanced Green
  operators used in the first Born response of the interacting two-point
  function.
- `W_omega^>`, `W_omega^<`, `Pi_sun^ret`, `Ext_EG`: greater/lesser
  two-point functions, the retained nonlocal sunset self-energy kernel with the
  closed-time-path `-i` retardedization, and the Epstein--Glaser extension map
  separating off-diagonal propagation from local diagonal counterterms.
- `S_BV`, `Delta_BV`: BV action and renormalized BV second-order operator.

## Claim Ledger

- Defines Bastiani-smooth functionals, functional support, local
  jet-dependent functionals, and their diagonal functional derivatives.
- Defines microcausal functionals through wavefront-set avoidance with the
  future/past covector convention inherited from the microlocal chapter.
- Defines the Hadamard star product, proves associativity by commuting
  tensor-factor contractions, and derives the Peierls bracket commutator.
- Proves the smooth-Hadamard-change isomorphism by the second-order
  Laplacian product rule.
- Defines time-ordered products as extensions from configuration space with
  partial diagonals removed; states and proves the finite scaling-degree
  extension theorem and identifies the local contact-term ambiguity.
- Explains Epstein--Glaser induction by causal factorization away from the
  total diagonal.
- Defines interacting fields by the relative S-matrix and proves the causal
  support statement for Bogoliubov fields.
- Records the Stueckelberg--Petermann local renormalization map and the BV
  quantum master equation as the gauge-theory consistency condition.
- Adds a worked interacting scalar coordinate: a compactly supported
  `lambda phi^4` interaction is transported under a smooth
  Hadamard-coordinate isomorphism with typed state transport, so expectation
  values are invariant for the same abstract observable.  Separately, a
  local covariant finite Wick-renormalization scalar produces finite mass and
  curvature-coupling coordinate shifts, geometric source terms, and a
  fixed-state Wick-square prescription shift.  The chapter now states that
  this is only the Wick-coordinate subfamily: a full interacting stress-tensor
  construction also fixes time-ordered products, Bogoliubov-field contact
  terms, independent `Phi^4` finite counterterms, and the conserved local
  stress-tensor tensors.  This gives the Volume XII interacting-example lane a
  concrete renormalization/state/output calculation without mistaking a
  Wick-square coordinate check for the full conserved interacting source.
- Adds a worked local-coupling Ward ledger for the same interacting scalar
  model.  The chapter treats the compact switching function as a background
  coupling with density insertion `O_lambda=delta V_lambda(chi)/delta chi` and
  derives the balance
  `nabla^mu T^{(chi)}_{mu nu}=<O_lambda^{(chi)}> nabla_nu chi` in the fixed
  variation convention.  It separates constant-coupling/adiabatic regions
  where the Ward source vanishes, compact switching edges where the external
  coupling injects four-momentum, and semiclassical backreaction where the
  full scheme-fixed interacting stress tensor or an explicit Ward
  residual/error budget is required.  The passage also records that finite
  density renormalizations must be transported through the Ward source
  together with stress-tensor counterterms.
- Adds a second worked interacting scalar example: the retained local
  one-loop tadpole from `lambda phi^4` is converted into a state-dependent
  mass coordinate `lambda Sigma_{omega,H}/2` and then into the first Born
  correction to a retarded two-point response.  The chapter keeps the local
  Wick square inside the spacetime integral when it is nonconstant, records
  the finite Wick-renormalization shift of the response coordinate, and
  explicitly separates this retained tadpole term from the full nonlocal
  interacting self-energy, cutoff-edge corrections, and higher-loop physics.
- Adds a third worked interacting scalar response layer: the order
  `lambda^2` sunset self-energy is written off diagonal as a retarded
  greater/lesser causal difference with coefficient `-lambda^2/6` and the
  closed-time-path factor `-i`, then inserted into the bilocal Born response for
  the retarded two-point function.  The chapter derives the coefficient from the
  second cumulant, checks that Hermitian Wightman data give a real time-domain
  inverse-kernel insertion, and explicitly separates the off-diagonal kernel
  from the Epstein--Glaser extension and local two-point counterterms needed for
  a renormalized interacting propagator.

## Calculation Checks

- `calculation-checks/paqft_algebra_checks.py`: verifies the finite
  polynomial model of star-product associativity, the smooth-Hadamard-change
  intertwiner, the combinatorics of scaling-degree extension ambiguity, and
  the `lambda phi^4` Hadamard-coordinate/local-Wick-renormalization
  coefficients: quartic tadpole, vacuum term, transported-state expectation
  invariance, fixed-state Wick-square prescription shift, mass/curvature
  coordinate shifts, geometric-source coordinates, and the local-coupling Ward
  balance for a compact switching function, including exact cancellation
  between metric and coupling variations, zero source for a constant switching
  function, finite Wick-density transport through the Ward source, and
  negative controls for treating a compact switching edge as conserved or
  averaging a nonconstant density.  It also checks the retained one-loop
  tadpole mass response, including the `lambda Sigma/2` combinatorial factor,
  the inverse-operator Born sign, linearity in coupling/state Wick square,
  finite Wick-square scheme shifts, and rejection of constant averaging for a
  nonconstant local tadpole density.  It verifies the off-diagonal sunset
  response: the quadratic-action-to-kernel factor, retarded support, the `-i`
  retardedization on Hermitian-compatible complex Wightman samples, bilocal
  Born sign, rejection of the wrong symmetry factor, omitted `i` factor, and
  acausal symmetric kernel, and separation of diagonal local counterterm
  response from the nonlocal sunset kernel.

## Figure Ledger

No figure is included in this pass.  Future figures should include causal
factorization regions, diagonal extensions in configuration space, and
Hadamard star-product comparison maps.

## Anti-Wrapper Audit

- 2026-06-04: added a worked interacting scalar example for issue #729.  The
  passage follows a concrete `lambda phi^4` interaction through a
  Hadamard-coordinate change and a separate local Wick-renormalization
  comparison to mass, curvature-coupling, geometric-source, and Wick-square
  outputs; it does not present the pAQFT machinery as a nonperturbative
  curved-spacetime construction.
- 2026-06-04: corrected the worked example for issue #740 by typing
  `omega_H` and `omega_Hprime`, recording expectation invariance under
  coordinate/state transport, and reserving c-number Wick-square shifts for
  fixed-state comparisons of local covariant Wick prescriptions.
- 2026-06-04: extended the scheme discussion for issue #741 so the
  `lambda phi^4` passage distinguishes the restricted Wick-coordinate
  subfamily from the full finite-renormalization and conservation budget of an
  interacting stress tensor.
- 2026-06-04: added the retained tadpole response example for issue #729.
  The addition is a physical-output calculation, not another algebraic
  coordinate cell: it turns the state Wick square into a local mass insertion
  and then into a retarded two-point Born shift while marking the nonlocal
  self-energy and adiabatic-limit pieces as outside the retained
  approximation.
- 2026-06-04: added the off-diagonal sunset response example for issue #729.
  This moves beyond the local tadpole by deriving the first nonlocal two-point
  memory kernel and by marking the diagonal extension/counterterm problem as
  required extra data, so the section does not present a separated-point
  kernel as a full renormalized propagator.
- 2026-06-04 issue #744: restored the closed-time-path `-i` factor in the
  retarded sunset kernel.  The companion now uses Hermitian-compatible complex
  Wightman samples, verifies that the retarded kernel is real on real test
  data, and rejects the old omitted-`i` convention as an imaginary
  inverse-kernel insertion.
- 2026-06-06 issue #729: added the local-coupling Ward ledger upstream of the
  semiclassical Ward diagnostics.  This is architecture rather than another
  diagram cell: it explains why compact switching functions are construction
  devices with edge Ward sources, why finite density renormalizations must
  move with the stress prescription, and why backreaction needs a full
  conserved interacting stress tensor or a declared residual budget.
