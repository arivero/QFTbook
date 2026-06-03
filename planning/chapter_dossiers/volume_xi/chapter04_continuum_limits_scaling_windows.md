# Volume XI, Chapter 4 Dossier: Continuum Limits and Scaling Windows

## Logical Role

- Role in the monograph: define continuum limits of regulated lattice or
  cutoff theories as distributional limits with reconstruction data, and
  make scaling windows operational rather than slogan-level.
- Immediate predecessor: lattice reflection positivity.
- Immediate successor: Wilson lattice gauge theory and numerical regulator
  frameworks.

## Notation Inventory

- `D`: Euclidean spacetime dimension.
- `a`, `Lambda_a`: lattice spacing and lattice \(a\mathbb Z^D\).
- `mu_a`, `S_a`, `c(a)`: regulated expectation functional, regulated
  action, and scaling trajectory.
- `O_a^I`, `Z^I_J(a)`, `O_a^I(f)`: bare lattice observables, operator
  renormalization/mixing matrix, and smeared renormalized observables.
- `S^{I_1...I_k}`: limiting Schwinger distribution.
- `B_a`, `hat p_a^2`, `m_a`: Brillouin zone, lattice Laplacian symbol, and
  free lattice mass parameter.
- `K_a^imp`, `delta m_2`: tree-level improved scalar kernel and the
  \(a^2\) mass-coordinate coefficient in the free Symanzik expansion.
- `xi_lat`, `kappa_a`: correlation length in lattice units and physical pole
  mass extracted from the lattice pole.
- `R_b`, `B`, `S_*`, `y_i`: block-spin map, Banach interaction space, fixed
  point, and RG eigenvalues.
- `t`, `y_t`, `nu`, `omega`: one relevant coordinate, its RG eigenvalue,
  correlation-length exponent, and an irrelevant correction exponent.
- `N`, `L`, `u_N`, `F`, `sigma_s`: finite lattice size, physical box size,
  finite-size endpoint variable, finite-size scaling kernel, and step-scaling
  coordinate.

## Claim Ledger

1. Continuum limits are distributional limits of renormalized smeared
   lattice observables, not pointwise limits of unsmeared correlators.
2. A scaling trajectory includes all regulator-dependent local terms in the
   regulated action.
3. For the free massive lattice scalar with
   \(\hat p_a^2=4a^{-2}\sum_\mu\sin^2(ap_\mu/2)\), smeared two-point
   functions converge to the continuum massive Gaussian covariance
   \((p^2+m^2)^{-1}\).
4. The proof of the free limit uses Poisson summation, compact-momentum
   dominated convergence, and rapid-decay bounds on the Brillouin-zone tail.
5. Defines a Symanzik expansion datum as an actual distributional expansion
   with a controlled remainder, not merely a list of compatible local
   operators.
6. Derives the tree-level free-scalar cutoff expansion
   \((p^2+m^2)^{-1}
   +a^2(\sum_\mu p_\mu^4/12-\delta m_2)(p^2+m^2)^{-2}+O(a^4)\),
   identifying the leading hypercubic rotation-breaking artifact.
7. Proves that adding
   \(a^2\sum_\mu \hat p_{\mu,a}^4/12\) to the quadratic kernel cancels the
   \(O(a^2)\) free two-point artifact when the mass coordinate is tuned.
8. The exact free lattice pole mass is
   \(\kappa_a=2a^{-1}\operatorname{arcsinh}(am_a/2)\), so
   \(a\xi_{\rm lat}\to m^{-1}\).
9. Finite-size scaling is derived from an RG chart with a locally Lipschitz
   endpoint kernel, endpoint-coordinate control, irrelevant decay, and
   operator-coordinate stability:
   \(N^{\sum\Delta_I}G_N=F(tN^{y_t})+O(N^{-\omega})\).
10. If \(t(a)=(aM)^{y_t}+O(a^{y_t+\epsilon})\), the finite-volume scaling
    variable tends to \((ML)^{y_t}\) at fixed physical size.
11. Step scaling is defined by a finite-volume observable coordinate and a
    continuum \(a/L\to0\) limit at fixed \(g_L=u\); its Symanzik
    extrapolation must state exponents and a remainder bound.
12. A numerical scaling-window evidence package must state the observable
    coordinate, regulator schedule, covariance/autocorrelation data, fit
    windows, exponent and remainder hypotheses, rank/conditioning diagnostics,
    and the statistical, systematic, and window-stability components of the
    finite evidence budget \(B_{\rm num}\).
13. The finite numerical evidence ledger is a weighted least-squares identity:
    \(\widehat c_W-c=P_WR_W+P_W\eta_W\), with propagated covariance
    \(P_W\Sigma_WP_W^T\) and deterministic intercept envelope
    \(\sum_i |(P_W)_{0i}|\epsilon_i\).
14. Composite-operator continuum coordinates require Wick/contact-term
   subtractions; finite changes of subtraction are identity contact
   coordinates after smearing.
15. Reflection positivity passes to the continuum limit by closedness of the
   positive cone when the distributions converge on positive-time tests.
16. Hypercubic invariance becomes Euclidean invariance only after
   rotation-breaking local operators are controlled or tuned away.
17. The relation \(\nu=1/y_t\) follows from a controlled one-relevant-coordinate
   RG chart and stable-manifold estimates.
18. The constructive status of massive \(\phi^4_3\), the 3D Ising CFT, and
    four-dimensional \(\phi^4_4\) are logically distinct.

## Calculation Checks

- `calculation-checks/continuum_scaling_window_checks.py` verifies the
  lattice Laplacian expansion, tree-level Symanzik artifact and improved
  kernel cancellation, free-scalar pole-mass expansion and physical
  correlation length, Gaussian relevant-coordinate scaling, the
  \(\nu=1/y_t\) relation, finite-size endpoint variables, irrelevant
  corrections, physical finite-volume scaling variables, and finite
  Wick-subtraction contact shifts.
- `calculation-checks/numerical_extrapolation_checks.py` verifies exact
  finite-regulator extrapolation identities, including Lagrange
  nonuniqueness, Richardson and integer-power weights, correlated
  least-squares covariance/error propagation, and the finite evidence-budget
  decomposition used by `qft_scripts/finite_regulator_extrapolation.py`.

## Figure Ledger

No figure is included in this pass.  Future figures should show the scaling
window \(a\ll r\lesssim a\xi_{\rm lat}\), Brillouin-zone-to-continuum
momentum convergence, and the relevant/irrelevant decomposition near a
fixed point.
