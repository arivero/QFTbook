# Volume XI, Chapter 5 Dossier: Wilson Lattice Gauge Theory
Source-File: monograph/tex/volumes/volume_xi/chapter05_wilson_lattice_gauge_theory.tex

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
  prescribed boundary.  The 2026-05-29 anti-wrapper audit keeps this as an
  exact finite algebraic expansion in prose rather than proposition form.
- Exact finite surface-counting refinement of the strong-coupling expansion,
  including the minimal lattice area \(A_{\min}(C)\), excess-area counts
  \(N_C(n)\), the entropy-corrected area bound, and the one-cube polynomial
  \((t+t^5)/(1+t^6)\).
- Compact-group Peter--Weyl character expansion and its finite-cutoff
  nonabelian spin-foam tensor-network form, including the link Haar
  projectors.
- \(SU(N)\), \(N\ge3\), fundamental Wilson-weight normalization:
  \(d\langle N^{-1}\operatorname{Re}\operatorname{Tr}U_p\rangle/d\beta
  |_{\beta=0}=1/(2N^2)\), hence \(1/18\) for \(SU(3)\).
- Continuum expansion of plaquette holonomy.
- Plaquette-plus-rectangle improved gauge actions, including the finite
  regulator meaning of action improvement, the tree-level Symanzik
  coefficients \(c_1=-1/12,c_0=5/3\), the Iwasaki normalization convention,
  and the separation between improvement and reflection positivity.
- Gauge-covariant link smearing as a local map \(G^E\to G^E\), including
  APE preprojection, polar \(SU(N)\) projection equivariance, stout smearing,
  and the locality/scheme status of iterated smearing.
- Lattice perturbative coordinates around the trivial connection, including
  the trace-delta coupling convention \(\beta=N/g_0^2\), the quadratic Wilson
  kernel, covariant gauge fixing, the tree-level propagator, lattice momentum
  artifacts, and plaquette tadpole normalization as a finite coordinate
  convention.
- Wilson loop operators.
- Rectangular Wilson-loop transfer-matrix spectral representation, static
  potential extraction, line self-energy caveat, and Creutz-ratio perimeter
  cancellation, with a companion CSV analysis script for effective-mass and
  Creutz-ratio extraction.
- Finite-volume correlator matrices and the GEVP as a general
  finite-regulator spectral-extraction method, using glueball sources as the
  running example; includes vacuum-subtracted gauge-invariant sources,
  cubic-channel projection, exact finite-state GEVP extraction, source-basis
  covariance, a whitened residual criterion for controlled time windows, and
  a companion GEVP analysis script.
- Wilson/gradient flow as a finite-dimensional ODE on the compact link
  manifold, including link-gradient definition, global existence,
  gauge covariance, action monotonicity, continuum linearized heat-kernel
  smoothing, flowed energy-density scale coordinates \(t_0,w_0\), and the
  distinction between geometric/index topological charge definitions and
  numerical flow plateaux.
- Explicit finite \(SU(3)\) Wilson-score gradient calculation, including the
  staple formula, anti-Hermitian traceless projection, monotonicity identity
  for the normalized plaquette score, and an HDF5 companion flow script for
  saved finite configurations.  The finite derivative check is recorded as
  worked prose rather than theorem-family content.
- Clover curvature and clover topological-charge diagnostics, with oriented
  plaquette conventions, gauge-invariance proof, admissibility-distance
  diagnostic, and an HDF5 companion script for raw or flowed configurations.
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
| \(Q_{\rm clover}(U)\) | finite clover diagnostic for the Chern--Weil density |
| \(F_{\mu\nu}^{\rm cl}(x)\) | anti-Hermitian traceless clover curvature at site \(x\) |
| \(e_{\rm clover}(U)\) | clover action-density diagnostic |
| \(Q(U)\) | normalized finite \(SU(3)\) Wilson plaquette score |
| \(C_\mu(x;U)\) | \(SU(3)\) Wilson-flow staple matrix for a selected link |
| \(Z_\mu(x;U)\) | left-gradient generator for the normalized \(SU(3)\) plaquette score |
| \(U_e,U_p\) | \(\mathbb Z_2\) link variable and plaquette product |
| \(t=\tanh\beta\) | strong-coupling expansion coordinate |
| \(A\subset P\) | plaquette subset / \(\mathbb Z_2\)-two-chain |
| \(A_{\min}(C)\) | minimal plaquette area of a surface with boundary \(C\) |
| \(N_C(n)\) | number of surfaces with boundary \(C\) and excess area \(n\) |
| \(N_0(n)\) | number of closed surfaces of area \(n\) |
| \(\rho,K(C)\) | surface-entropy constants in the finite area estimate |
| \(D_\lambda,\chi_\lambda,c_\lambda\) | irreducible representation, character, and character-expansion coefficient |
| \(P_\ell\) | link Haar projector in the nonabelian spin-foam expansion |
| \(c_0,c_1\) | plaquette and rectangle coefficients in a local improved gauge action |
| \(\mathcal S\) | local gauge-covariant smearing map on lattice links |
| \(C_\ell,X_\ell,Q_\ell\) | staple sum, APE preprojection matrix, and stout algebra element |
| \(g_0,\xi,\widehat p_\mu\) | lattice perturbative coupling coordinate, gauge-fixing parameter, and lattice momentum |
| \(u_0,g_{\rm TI}\) | plaquette mean link and boosted/tadpole-improved coupling coordinate |
| \(W_S(n,m)\) | normalized rectangular Wilson loop in representation \(S\) |
| \(V_{a,S}(n)\) | finite-cutoff static potential in a static-source sector |
| \(C_{ij}^{(n,S)}(m)\) | static-source transporter correlator matrix at separation \(n\) |
| \(\Lambda_\alpha^{(n,S)}(m,m_0)\) | static-source GEVP eigenvalue |
| \(\chi(n,m)\) | Creutz ratio |
| \(O_i,\widetilde O_i\) | glueball time-slice source and its vacuum-subtracted version |
| \(C_{ij}(n)\) | finite-lattice glueball correlator matrix |
| \(Z_i^{(\alpha)}\) | source overlap with a transfer-matrix eigenvector |
| \(\Lambda_\alpha(n,n_0)\) | generalized eigenvalue of the GEVP |
| \(B(n,n_0)\) | whitened GEVP matrix \(C(n_0)^{-1/2}C(n)C(n_0)^{-1/2}\) |

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
7. The compact-group character expansion rewrites the finite-regulator
   nonabelian gauge integral as a representation-labeled tensor-network sum
   with Haar projectors on links; Wilson-loop insertions add a boundary spin
   network.
8. For \(SU(N)\), \(N\ge3\), with Wilson weight
   \(\exp[(\beta/N)\operatorname{Re}\operatorname{Tr}U]\), the normalized
   fundamental plaquette has slope \(1/(2N^2)\) at \(\beta=0\), so the
   \(SU(3)\) coefficient is \(1/18\).
9. In the plaquette-plus-rectangle action, leading continuum normalization
   gives \(c_0+8c_1=1\); cancellation of the abelian quadratic \(O(a^2)\)
   derivative artifact gives \(c_0+20c_1=0\); hence the tree-level Symanzik
   coefficients are \(c_1=-1/12,c_0=5/3\).
10. Improved action coefficients, continuum normalization, and
    reflection-positivity/transfer-matrix reconstruction are separate
    regulator requirements.
11. A smearing map used for line operators or actions is part of the regulator
    datum.  Gauge covariance requires
    \(\mathcal S_\ell(g\cdot U)=g(x)\mathcal S_\ell(U)g(y)^{-1}\).
12. Polar projection is gauge equivariant on its smooth branch, and stout
    smearing gives a smooth \(SU(N)\)-valued gauge-covariant link map because
    its algebra element is anti-Hermitian, traceless, and transforms by
    endpoint conjugation.
13. The Wilson action with \(\beta=N/g_0^2\) has tree-level quadratic kernel
    \(K_{\mu\nu}^{(\xi)}=\delta_{\mu\nu}\widehat p^2
    -(1-\xi^{-1})\widehat p_\mu\widehat p_\nu\) after covariant gauge fixing,
    with inverse \(D_{\mu\nu}=\widehat p^{-2}[\delta_{\mu\nu}
    -(1-\xi)\widehat p_\mu\widehat p_\nu/\widehat p^2]\).
14. The lattice momentum obeys
    \(\widehat p^2=p^2-\frac{a^2}{12}\sum_\mu p_\mu^4+O(a^4p^6)\), giving an
    explicit tree-level cutoff artifact.
15. Plaquette tadpole normalization defines finite perturbative coordinates
    \(O_{\rm TI}=u_0^{-L}O\) and \(g_{\rm TI}^2=g_0^2/u_0^4\); matching
    statements require a specified observable and truncation order.
16. Rectangular Wilson loops are transfer-matrix correlators in static-source
   sectors; an isolated lowest state gives the finite-lattice static
   potential by the effective-mass ratio.  In an exact finite static-source
   matrix subspace, the GEVP eigenvalues are
   \(e^{-a(m-m_0)E_\alpha(n,S)}\) and are invariant under invertible
   source-basis changes.
17. Creutz ratios cancel the area-plus-perimeter ansatz down to the lattice
    string-tension coordinate plus a second finite difference of correction
    terms.
18. Finite-volume spectroscopy at finite cutoff is a transfer-matrix spectral
    problem for time-slice sources in a declared symmetry channel.  In an
    exact finite-state source subspace, the GEVP eigenvalues are exactly
    \(e^{-a(n-n_0)E_\alpha}\), are invariant under invertible source-basis
    changes, and with higher-state contamination require a residual bound
    after whitening by \(C(n_0)\).  Glueball sources are the running example,
    not the scope of the method.
19. Wilson flow at finite lattice spacing is the negative-gradient ODE on
   \(G^E\); compactness gives global existence, gauge invariance gives
   covariance, and the chain rule gives
   \(\frac{d}{dt}S(V_t)=-\sum_\ell\|\nabla_\ell S(V_t)\|^2\).
20. Positive physical flow time damps ultraviolet Fourier modes in the
   linearized continuum equation, but flowed scale coordinates and topological
   charge plateaux acquire continuum meaning only after a scaling trajectory
   and a regulator-level topological-charge definition are specified.
21. Smooth continuum gradient flow preserves the Chern--Weil charge on a fixed
   bundle because \(\frac{d}{dt}\operatorname{tr}(F\wedge F)\) is an exact
   differential.
22. For finite \(SU(3)\) Wilson links, the force
    \(Z_\mu(x;U)=-\frac13[U_\mu(x)C_\mu(x;U)]_{\mathfrak{su}(3)}\) is the
    left-gradient of the normalized plaquette score \(Q\), and the normalized
    score-flow equation satisfies
    \(\frac{d}{dt}Q(V_t)=\sum_{x,\mu}\|Z_\mu(x;V_t)\|^2\ge0\).
23. The clover curvature \(F_{\mu\nu}^{\rm cl}\) transforms by conjugation at
    its base point, so \(Q_{\rm clover}\), \(e_{\rm clover}\), and
    \(\max_p\|1-U_p\|\) are gauge-invariant finite-regulator diagnostics.
    They are not integer topological charges without a separate admissible
    geometric or index-theoretic construction.
24. Chiral gauge theories require additional determinant-phase and anomaly
   control beyond the vectorlike Wilson action.

## Companion Scripts

- `qft_scripts/z2_gauge_3d_metropolis.py --smoke`: finite periodic
  three-dimensional \(\mathbb Z_2\) gauge sampler for plaquette and
  rectangular Wilson-loop measurements.
- `qft_scripts/static_potential_from_wilson_loops.py --smoke`: finite
  Wilson-loop analysis tool for transfer-matrix effective masses and Creutz
  ratios from positive rectangular-loop data, including a sample-level
  correlated jackknife/bootstrap mode for CSV or HDF5 sampler output and a
  static-source matrix GEVP mode for smeared transporter correlators.
- `qft_scripts/glueball_gevp_from_correlators.py --smoke`: finite
  correlator-matrix GEVP analysis tool.  The smoke mode uses an exact
  two-state transfer-matrix spectral matrix and verifies that whitening by
  \(C(n_0)\) recovers the input energies.
- `qft_scripts/su3_wilson_flow_hdf5.py --smoke`: finite \(SU(3)\)
  Wilson-score gradient-flow evolution for hot/cold links or HDF5
  checkpoints, with trajectory output when `h5py` is available.
- `qft_scripts/su3_ape_smearing_hdf5.py --smoke`: finite \(SU(3)\)
  APE-smearing utility for raw, flowed, or already-smeared HDF5 checkpoints,
  with spatial and all-direction modes.
- `qft_scripts/su3_topological_charge_diagnostics_hdf5.py --smoke`: finite
  \(SU(3)\) clover topological-charge and action-density diagnostic for raw
  or flowed HDF5 checkpoints.

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
- `calculation-checks/su3_wilson_flow_checks.py` verifies the explicit
  finite \(SU(3)\) Wilson-score gradient by directional derivatives, one-step
  gauge covariance, small-step monotonicity, group preservation, HDF5
  trajectory layout, and sampler-checkpoint input.
- `calculation-checks/su3_ape_smearing_checks.py` verifies the cold fixed
  point, spatial-mode preservation of temporal links, gauge covariance of the
  APE map, and HDF5 sampler-to-smearing plus smearing-to-smearing checkpoint
  layout.
- `calculation-checks/su3_topological_charge_diagnostics_checks.py` verifies
  oriented plaquette conventions, cold-configuration vanishing, clover-field
  anti-Hermiticity/tracelessness/antisymmetry, gauge invariance of the
  diagnostics, and the sampler-to-flow-to-topology HDF5 pipeline.
- `calculation-checks/gauge_action_improvement_checks.py` verifies the
  plaquette-plus-rectangle tree-level improvement arithmetic: rectangle flux
  moments, \(c_0+8c_1=1\), \(c_0+20c_1=0\), and the normalization convention
  for one-parameter rectangle actions.
- `calculation-checks/link_smearing_checks.py` verifies polar-projection
  equivariance, the anti-Hermitian traceless stout algebra projection, and
  endpoint-conjugation covariance of the stout algebra element.
- `calculation-checks/lattice_perturbation_tadpole_checks.py` verifies the
  tree-level gauge-fixed kernel inverse, the \(\widehat p^2\) expansion
  coefficient, and tadpole-normalization bookkeeping.
- `calculation-checks/static_potential_analysis_checks.py` verifies the
  static-potential companion script on synthetic area-plus-perimeter
  Wilson-loop data, including elementary ratio-error propagation and
  correlated delete-one jackknife errors for nonlinear Wilson-loop ratios;
  it verifies exact finite static-source GEVP trace/determinant invariants and
  a CSV matrix-mode round trip; it also checks the HDF5 bridge from
  `measurements/wilson_loops[sample,R-1,T-1]`.
- `calculation-checks/qcd_glueball_spectrum_checks.py` verifies the exact
  finite GEVP trace/determinant invariants, large-\(N\) glueball counting,
  and the cubic-group dimension split used in the glueball extraction
  discussion.
- `calculation-checks/nonabelian_lattice_observable_checks.py` verifies the
  \(SU(N)\) fundamental plaquette strong-coupling slope, the single-state
  transfer-matrix ratio for static-energy extraction, and Creutz-ratio
  cancellation of area-plus-perimeter ansatz terms.

## Figures

- Plaquette orientation diagram may be added later.

## Audit Notes

- 2026-05-27 issue #631 pass: added the Wilson/gradient-flow section to close
  the most visible missing lattice-depth topic flagged by the review.  The
  section treats flow first as a finite-regulator ODE, not as a continuum
  slogan, and separates flowed smoothing, scale setting, and topological
  charge definitions.
- 2026-05-27 issue #631 pass: added the explicit finite \(SU(3)\)
  Wilson-score gradient force and a theorem-anchored HDF5 Wilson-flow
  companion script with directional-derivative and gauge-covariance checks.
- 2026-05-27 issue #631 pass: added the clover topological-charge diagnostic
  as a finite-regulator observable, explicitly separated from integer
  geometric/index topological charge, with HDF5 pipeline checks.
- 2026-05-27 issue #631 pass: added tree-level plaquette-plus-rectangle gauge
  improvement with an explicit rectangle-flux derivation, while flagging that
  loop-level improvement and transfer-matrix positivity are distinct
  regulator questions.
- 2026-05-27 issue #631 pass: added gauge-covariant smearing as regulator data
  with polar projection and stout smearing proofs, keeping the operator-scheme
  and locality assumptions explicit.
- 2026-05-27 issue #631 pass: added a theorem-anchored \(SU(3)\) APE-smearing
  HDF5 companion script, with gauge-covariance and checkpoint-layout checks.
- 2026-05-27 issue #631 pass: added lattice perturbative coordinates and
  tadpole normalization, deriving the tree-level gauge-fixed kernel and
  boosted-coupling coordinate as finite perturbative conventions whose
  continuum use requires a stated matching problem.
- 2026-05-27 issue #631 pass: added a theorem-anchored static-potential
  companion script for effective-mass and Creutz-ratio extraction from
  rectangular Wilson-loop data.
- 2026-05-27 issue #631 pass: extended the static-potential companion script
  with sample-level correlated jackknife/bootstrap analysis for the nonlinear
  logarithmic ratios, avoiding independent-error propagation when Monte Carlo
  rectangles are correlated.
- 2026-05-27 issue #631 pass: connected the static-potential analysis
  directly to the HDF5 SU(3) sampler dataset
  `measurements/wilson_loops[sample,R-1,T-1]`, with an HDF5 calculation check.
- 2026-05-29 issue #631 pass: added a finite transfer-matrix GEVP treatment
  for glueball correlator matrices, including exact finite-state extraction,
  a whitened residual criterion, and a theorem-anchored correlator-matrix
  analysis script.
- 2026-05-30 general-method placement pass: reframed the GEVP section as the
  general finite-volume correlator-matrix method, added source-basis
  covariance, and clarified that pure Yang--Mills glueballs are only the
  running example.  QCD and pure-SYM chapters now reference this section
  rather than duplicating the linear algebra.
- 2026-06-03 issue #631 pass: added the static-source variational matrix GEVP
  for smeared/path-varied spatial transporters at fixed separation, plus
  theorem-anchored script and exact rational calculation checks.
