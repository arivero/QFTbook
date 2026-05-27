# Volume XI, Chapter 5 Dossier: Wilson Lattice Gauge Theory

## Logical Role

- Role in the monograph: define compact lattice gauge theory as a
  nonperturbative finite-regulator path integral.
- Immediate predecessor: continuum limits and scaling windows.
- Immediate successor: Monte Carlo/sign problems and rigorous lattice RG.

## Definitions And Results

- Link variables and lattice gauge transformations.
- Plaquette holonomy.
- Wilson plaquette action and Haar-measure partition function.
- Finite periodic \(\mathbb Z_2\) gauge model as a fully explicit compact
  gauge benchmark.
- Exact finite \(\mathbb Z_2\) character expansion: partition function as
  closed plaquette surfaces and Wilson-loop expectation as surfaces with
  prescribed boundary.
- Exact finite surface-counting refinement of the strong-coupling expansion,
  including the minimal lattice area \(A_{\min}(C)\), excess-area counts
  \(N_C(n)\), the entropy-corrected area bound, and the one-cube polynomial
  \((t+t^5)/(1+t^6)\).
- Continuum expansion of plaquette holonomy.
- Wilson loop operators.
- Wilson/gradient flow as a finite-dimensional ODE on the compact link
  manifold, including link-gradient definition, global existence,
  gauge covariance, action monotonicity, continuum linearized heat-kernel
  smoothing, flowed energy-density scale coordinates \(t_0,w_0\), and the
  distinction between geometric/index topological charge definitions and
  numerical flow plateaux.
- Reflection positivity and transfer-matrix statement.
- Fermion and chiral-gauge-theory regulator boundary.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(U_\mu(x)\) | gauge link variable |
| \(U_{\mu\nu}(x)\) | plaquette holonomy |
| \(S_W\) | Wilson lattice action |
| \(\beta\) | lattice gauge coupling parameter |
| \(W_R(C)\) | Wilson loop in representation \(R\) |
| \(T=e^{-aH}\) | transfer matrix |
| \(V_t(\ell)\) | flowed link at flow time \(t\) |
| \(\nabla_\ell S\) | left-link gradient of the lattice action |
| \(\overline E(t)\) | volume-averaged flowed energy density |
| \(t_0,w_0\) | finite-cutoff flowed scale coordinates, when uniquely defined |
| \(Q_{\rm geom}(U)\) | geometric lattice topological charge under an admissibility datum |
| \(U_e,U_p\) | \(\mathbb Z_2\) link variable and plaquette product |
| \(t=\tanh\beta\) | strong-coupling expansion coordinate |
| \(A\subset P\) | plaquette subset / \(\mathbb Z_2\)-two-chain |
| \(A_{\min}(C)\) | minimal plaquette area of a surface with boundary \(C\) |
| \(N_C(n)\) | number of surfaces with boundary \(C\) and excess area \(n\) |
| \(N_0(n)\) | number of closed surfaces of area \(n\) |
| \(\rho,K(C)\) | surface-entropy constants in the finite area estimate |

## Claim Ledger

1. Wilson lattice gauge theory is a gauge-invariant compact group integral at
   finite cutoff.
2. The plaquette expansion matches the continuum Yang--Mills action after
   fixing trace normalization.
3. Wilson loops are finite-regulator gauge-invariant line probes.
4. The finite \(\mathbb Z_2\) character expansion is an exact surface
   representation at finite cutoff: \(Z\) sums closed plaquette surfaces and
   \(\langle W(C)\rangle\) sums surfaces with boundary \(C\).
5. At fixed cutoff and sufficiently small \(t=\tanh\beta\), a surface entropy
   bound \(N_C(n)\leq K(C)\rho^n\) implies an explicit area-law estimate for
   \(\mathbb Z_2\) Wilson loops.  The statement is finite-regulator strong
   coupling, not a continuum confinement theorem.
6. The one-cube calculation gives exactly
   \(\langle W(C)\rangle=(t+t^5)/(1+t^6)\), showing the minimal surface and
   complementary surface contributions before any thermodynamic limit.
7. Wilson flow at finite lattice spacing is the negative-gradient ODE on
   \(G^E\); compactness gives global existence, gauge invariance gives
   covariance, and the chain rule gives
   \(\frac{d}{dt}S(V_t)=-\sum_\ell\|\nabla_\ell S(V_t)\|^2\).
8. Positive physical flow time damps ultraviolet Fourier modes in the
   linearized continuum equation, but flowed scale coordinates and topological
   charge plateaux acquire continuum meaning only after a scaling trajectory
   and a regulator-level topological-charge definition are specified.
9. Smooth continuum gradient flow preserves the Chern--Weil charge on a fixed
   bundle because \(\frac{d}{dt}\operatorname{tr}(F\wedge F)\) is an exact
   differential.
10. Chiral gauge theories require additional determinant-phase and anomaly
   control beyond the vectorlike Wilson action.

## Companion Scripts

- `qft_scripts/z2_gauge_3d_metropolis.py --smoke`: finite periodic
  three-dimensional \(\mathbb Z_2\) gauge sampler for plaquette and
  rectangular Wilson-loop measurements.

## Calculation Checks

- `calculation-checks/z2_gauge_metropolis_checks.py` verifies the local
  link-flip plaquette-score change, detailed balance, gauge invariance, and
  the \(1\times1\) Wilson-loop/plaquette identity used by the companion
  script.
- `calculation-checks/z2_strong_coupling_surface_checks.py` exactly
  enumerates small cubical plaquette complexes over \(\mathbb F_2\),
  verifying the one-cube Wilson-loop polynomial, the \(2\times1\) rectangular
  surface counts, and the finite entropy-bound arithmetic.
- `calculation-checks/lattice_gradient_flow_checks.py` verifies the
  negative-gradient monotonicity identity, adjoint norm covariance,
  linearized heat-kernel damping, the \(w_0\) derivative convention, and the
  Chern--Weil variation factor used in the Wilson-flow section.

## Figures

- Plaquette orientation diagram may be added later.

## Audit Notes

- 2026-05-27 issue #631 pass: added the Wilson/gradient-flow section to close
  the most visible missing lattice-depth topic flagged by the review.  The
  section treats flow first as a finite-regulator ODE, not as a continuum
  slogan, and separates flowed smoothing, scale setting, and topological
  charge definitions.
