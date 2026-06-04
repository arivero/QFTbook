# Chapter 11: Finite-Volume Form Factors And Spectral Expansions

## Source Position

This chapter closes the finite-volume bridge in the integrable-QFT volume.  It
connects bootstrap form factors to normalizable finite-volume matrix elements,
then derives the zero-temperature and thermal spectral expansions with the
normalization and convergence obligations explicit.

## Notation Inventory

- `L`: spatial circumference, used as a finite-volume infrared regulator.
- `a`, `b`, `a_j`: particle species labels in \(\mathcal I\).
- `m_a`: mass of species \(a\).
- `theta_j`: rapidity variables.
- `S_ab(theta) = exp(i delta_ab(theta))`: diagonal two-body scattering
  eigenvalue and phase.
- `varphi_ab(theta)`: derivative \(\partial_\theta\delta_{ab}(\theta)\).
- `Q_j(theta)`: Bethe-Yang phase.
- `I_j`: Bethe integer or half-integer.
- `G_ij`: Gaudin matrix \(\partial Q_i/\partial\theta_j\).
- `rho_n(theta)`: Gaudin determinant \(\det G\).
- `rho_A`: principal Gaudin minor on subset \(A\).
- `F^O_n`: infinite-volume vacuum-to-\(n\)-particle form factor.
- `F^O_{2n,c}`: connected diagonal form factor.
- `m_*`: lightest mass in the theory.
- `n_a(theta)`: TBA occupation factor.
- `epsilon_a(theta)`: TBA pseudoenergy.

## Claim Ledger

1. Defines finite-volume Bethe-Yang states in a massive diagonal integrable
   sector.
2. Proves Bethe-Yang quantization by moving one particle around the circle
   and collecting scattering phases.
3. Defines the Gaudin matrix and density, including the two-particle formula.
4. Proves the state-counting measure from the Jacobian of the Bethe-Yang map.
5. Explains the leading normalization of finite-volume unit vectors by
   \(\rho_n^{-1/2}\).
6. Proves the off-diagonal finite-volume form-factor formula under regular
   crossing and no-coincident-rapidity hypotheses.
7. Proves the cancellation of the Gaudin density between finite-volume
   matrix elements and Bethe-state sums.
8. Defines connected diagonal form factors by subtracting kinematic poles.
9. Defines principal Gaudin minors and proves the diagonal finite-volume
   matrix-element subset expansion.
10. Displays the one- and two-particle diagonal formulas explicitly.
11. Derives the zero-temperature finite-volume spectral expansion and its
    infinite-volume rapidity-integral limit.
12. Gives a sufficient convergence criterion for the Euclidean spectral
    series.
13. Works out the free-Majorana energy-density two-particle spectral term and
    its Bessel-kernel reduction.
14. Adds a separated-window reconstruction control for the same
    free-Majorana local energy-density observable: the particle-number tail is
    zero only because the local free-field bilinear is already constructed,
    while the finite rapidity cutoff has an explicit Bessel-tail error bound.
15. States the thermal connected-diagonal Leclair-Mussardo type series with
    the TBA and convergence dependencies explicit.
16. Labels the reconstruction chain arrow by arrow: on-shell scattering data,
    operator bootstrap/crossing, finite-volume Gaudin-normalized matrix
    elements, and the final analytic reconstruction of distributions.
17. Separates finite-volume calculability from the open construction theorem
    for local QFT from form-factor data, with the free Majorana chain
    identified as theorem-level only because the local free field is already
    constructed.
18. Adds a separated-Euclidean reconstruction package and residual budget:
    finite-volume-to-rapidity error, particle-number tail, diagonal/contact
    extension, domain/positivity, locality, and sector-completeness residuals
    must all be controlled before a Gaudin-normalized finite-volume approximant
    becomes a local-QFT reconstruction statement.

## Calculation Checks

- `calculation-checks/finite_volume_form_factor_checks.py` verifies the
  finite algebra and normalization bookkeeping used in the chapter:
  two-particle Gaudin determinant, Gaudin-density cancellation in the
  sum-integral limit, connected diagonal subset expansion through three
  particles, subset counting, the free-Majorana Bessel prefactor, and the
  free-Majorana separated-window rapidity-tail prefactor and primitive, and
  the finite reconstruction residual budget with a deliberately nonzero
  analytic and operator-level defect.

## Figure Ledger

No figure is included in this pass.  Future figures should show: a particle
circling the finite spatial circle and crossing all other particles; the
rapidity-wall crossing for off-diagonal form factors; and the subset
decomposition of diagonal disconnected contractions.

## Audit Notes

- 2026-05-26 finite-volume depth pass: rewrote the chapter from a short
  normalization summary into a theorem-led derivation of Bethe-Yang
  quantization, Gaudin state counting, finite-volume matrix-element
  normalization, diagonal connected-form-factor combinatorics, spectral
  expansion convergence criteria, and the free-Majorana energy-density
  example.
- 2026-06-03 reconstruction-spine point-of-use pass: expanded the
  reconstruction boundary so finite-volume matrix-element convergence is not
  conflated with positivity, covariance, locality or wedge-locality,
  clustering, domain control, and scattering compatibility of the continuum
  QFT.
- 2026-06-04 issue #728 reconstruction-budget pass: added the separated
  Euclidean reconstruction package and finite residual budget, with companion
  arithmetic verifying that exact Gaudin bookkeeping does not remove
  finite-volume, tail, diagonal/contact, domain, locality, or completeness
  residuals.
- 2026-06-04 issue #728 local-observable pass: upgraded the free-Majorana
  energy-density example from a Bessel reduction to a separated-window
  approximation with an explicit rapidity-tail bound, while keeping the
  theorem-level claim tied to the already constructed free local field.
