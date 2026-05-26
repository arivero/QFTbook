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
- `xi_lat`, `kappa_a`: correlation length in lattice units and physical pole
  mass extracted from the lattice pole.
- `R_b`, `B`, `S_*`, `y_i`: block-spin map, Banach interaction space, fixed
  point, and RG eigenvalues.
- `t`, `y_t`, `nu`: one relevant coordinate, its RG eigenvalue, and
  correlation-length exponent.

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
5. The exact free lattice pole mass is
   \(\kappa_a=2a^{-1}\operatorname{arcsinh}(am_a/2)\), so
   \(a\xi_{\rm lat}\to m^{-1}\).
6. Composite-operator continuum coordinates require Wick/contact-term
   subtractions; finite changes of subtraction are identity contact
   coordinates after smearing.
7. Reflection positivity passes to the continuum limit by closedness of the
   positive cone when the distributions converge on positive-time tests.
8. Hypercubic invariance becomes Euclidean invariance only after
   rotation-breaking local operators are controlled or tuned away.
9. The relation \(\nu=1/y_t\) follows from a controlled one-relevant-coordinate
   RG chart and stable-manifold estimates.
10. The constructive status of massive \(\phi^4_3\), the 3D Ising CFT, and
    four-dimensional \(\phi^4_4\) are logically distinct.

## Calculation Checks

- `calculation-checks/continuum_scaling_window_checks.py` verifies the
  lattice Laplacian expansion, free-scalar pole-mass expansion and physical
  correlation length, Gaussian relevant-coordinate scaling, the
  \(\nu=1/y_t\) relation, and finite Wick-subtraction contact shifts.

## Figure Ledger

No figure is included in this pass.  Future figures should show the scaling
window \(a\ll r\lesssim a\xi_{\rm lat}\), Brillouin-zone-to-continuum
momentum convergence, and the relevant/irrelevant decomposition near a
fixed point.
