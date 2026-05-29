# Volume XI Proof-Substance Audit

Date: 2026-05-28

Scope: read the theorem-like statements and the bodies of their proofs in
`monograph/tex/volumes/volume_xi`.  This was a proof-substance pass, not a
regular-expression pass.  I kept wrappers whose proof bodies construct an
object, prove an estimate, identify a limit, control a remainder, or execute a
nontrivial finite calculation.  I demoted wrappers whose proof was only direct
definition-unpacking, finite-dimensional bookkeeping, or an immediate
application of a previous result.

## Demoted wrappers

- `chapter04_continuum_limits_scaling_windows.tex`: demoted tree-level scalar
  Symanzik improvement to `Remark~\ref{rem:tree-level-scalar-symanzik-improvement}`.
  The verification is the explicit cancellation of the already computed
  \(a^2\sum_\mu p_\mu^4\) term.
- `chapter05_wilson_lattice_gauge_theory.tex`: demoted the tree-level lattice
  propagator and clover-diagnostic gauge invariance to
  `Remark~\ref{rem:lattice-tree-level-propagator}` and
  `Remark~\ref{rem:su3-clover-diagnostic-gauge-invariance}`.  Both remain in
  the text as useful convention checks, but the proofs are projector inversion
  and plaquette conjugation.
- `chapter06_monte_carlo_and_sign_problems.tex`: demoted delete-one-block
  jackknife for the mean to `Remark~\ref{rem:block-jackknife-mean-identity}`.
  The result is a direct algebraic identity for block means.
- `chapter07_rigorous_renormalization_group.tex`: demoted the irrelevant-tail
  warning and the universality equivalence-relation check to
  `Remark~\ref{rem:irrelevant-tail-part-of-rg-theorem}` and
  `Remark~\ref{rem:universality-equivalence-relation}`.  Their content is
  important, but the verification is coordinate projection bookkeeping and
  reflexivity/symmetry/transitivity after the actual reconstruction theorem is
  assumed.
- `chapter09_stochastic_quantization_singular_spde.tex`: demoted common finite
  Wick-coordinate vectors, Wick quartic potential convergence, the \(L^q\)
  density route to \(\Phi^4_2\) tightness, the dynamic \(\Phi^4_3\) negative
  drift ledger, and the SPDE invariant-law OS checklist to remarks:
  `rem:spde-common-wick-coordinate-limits`,
  `rem:spde-wick-quartic-potential-convergence`,
  `rem:spde-phi-four-two-density-tightness-route`,
  `rem:spde-phi-four-three-negative-drift-ledger`, and
  `rem:spde-invariant-law-os-reconstruction-criterion`.
- `chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`: demoted the finite
  Majorana benchmark, the connected TFFSA block check, and finite-data
  interpolation ambiguity to `Remark~\ref{rem:ising-energy-tcsa-benchmark}`,
  `Remark~\ref{rem:zero-momentum-connected-tffsa-hermitian}`, and
  `Remark~\ref{rem:finite-data-do-not-determine-continuum-limit}`.

## Statements kept after reading the proof bodies

- Constructive scalar and reflection-positivity chapters were kept: their
  theorem-like statements prove Wick coefficient formulae, cluster and
  Kotecky-Preiss bounds, reflection positivity, character expansions, OS
  positivity, multiscale stability, and finite-cutoff local estimates.
- Lattice continuum-limit and gauge-theory statements were kept when their
  proofs control Fourier tails, random-walk resolvents, spin-foam expansions,
  rectangle improvement, polar projection, stout-smearing covariance, Wilson
  flow, static-energy extraction, and Chern-Weil charge conservation.
- Monte Carlo and sign-problem statements were kept when their proofs establish
  detailed balance, exact heat-bath sampling, subgroup invariance, leapfrog
  reversibility, pseudofermion determinant identities, correlated jackknife
  ratio formulas, phase-reweighting variance bounds, or \(\gamma_5\)-Hermiticity.
- Rigorous RG statements were kept when their proofs use stable-manifold,
  Newton-Kantorovich, hierarchical Gaussian eigenvalue, or projected-zero
  lifting arguments with actual Banach-space hypotheses.
- The stochastic quantization chapter was read end-to-end.  I kept the analytic
  estimates and proof infrastructure: finite-dimensional Langevin invariance,
  OU covariance, Wick-power convergence, mixed covariance criteria, heat and
  Besov smoothing, DPD fixed points, energy estimates, compactness and
  lower-semicontinuity passages, invariant-measure limits, Sobolev tightness,
  Brascamp-Lieb covariance domination, OS-positivity closure, lattice regulator
  positivity, regulator-comparison criteria, regularity-structure
  reconstruction, random-model Cauchy criteria, finite-chaos and projective
  kernel estimates, dyadic convolution and Taylor-subtraction gains, multiscale
  sector summability, dyadic-net upgrades, negative-sector convergence
  criteria, Fourier counterterm calculations, and the abstract modelled
  fixed-point theorem.
- Hamiltonian truncation and lattice-fermion statements were kept when the
  proofs establish Rayleigh-Ritz convergence, gap-stable Ritz counting, Schur
  complement formulas, residual bounds, finite PV positivity, Richardson
  extrapolation bounds, Berezin Gaussian identities, Brillouin-torus index
  cancellation, Wilson doubler lifting, fermion reflection positivity, Ginsparg-
  Wilson chiral Jacobians, overlap identities, and overlap index formulae.

## Remaining standard

This pass removes theorem-like wrappers whose proofs were not theorem-level.
It does not certify the quoted theorem boundaries in the constructive and
singular-SPDE chapters as proved; those remain explicitly marked proof
boundaries or open proof stacks until the monograph supplies the missing
estimates.
