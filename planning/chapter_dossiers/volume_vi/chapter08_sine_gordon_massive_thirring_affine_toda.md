# Chapter 08: Sine-Gordon, Massive Thirring, And Affine Toda Theories

## Source Position

Volume VI now turns from general integrable machinery to concrete model
families.  This chapter supplies the first exact examples before the later
`O(N)`, Gross-Neveu, and integrable sigma-model chapter.

## Notation Inventory

- `A_UV`, `O_pert`, `lambda`, `Q`, `S`, `F`: UV algebra, perturbing
  coordinate, coupling, conserved charges, scattering data, and form factors.
- `varphi`, `beta`, `mu`: sine-Gordon field, coupling, and potential
  coordinate.
- `Q_top`: sine-Gordon topological charge.
- `xi`, `M_s`, `B_n`, `m_n`: sine-Gordon coupling parameter, soliton mass,
  breather label, and breather mass.
- `m`, `varphi_K`, `K_K`, `delta(k)`: semiclassical small-oscillation mass,
  classical sine-Gordon kink, kink-sector fluctuation operator, and
  reflectionless DHN phase shift.
- `mu_UV`, `beta_UV`: UV-normal-ordered sine-Gordon perturbing coordinate
  and free-boson vertex charge in the \(1/(16\pi)\) kinetic normalization.
- `lambda`, `V`, `S_min`, `b(theta)`, `c(theta)`: inverse sine-Gordon
  coupling parameter, soliton/antisoliton charge doublet, minimal scalar
  factor, and transmission/reflection amplitudes in the exact soliton
  S-matrix.
- `S_{sB_n}(theta)`, `F_a(theta)`, `S_mn(theta)`: soliton-breather scalar
  amplitude, neutral scalar breather block, and minimal diagonal
  breather-breather scattering amplitude.
- `psi_pm`, `K_pm`: Mandelstam soliton-creating fermion fields and Klein
  factors in the massive Thirring equivalence.
- `psi`, `J^mu`, `g_T`, `K`, `phi_0`: massive Thirring fermion, Hermitian
  mostly-plus vector current \(J^\mu=\ii\bar\psi\gamma^\mu\psi\),
  current-current coupling, massless Thirring current-sector kinetic
  coefficient \(K=1+g_T/\pi\), and the free-Dirac bosonization scalar before
  the canonical sine-Gordon rescaling.
- `V_alpha`, `Delta_alpha`: canonical free-boson vertex operator and its
  scaling dimension \(\alpha^2/(4\pi)\).
- `g`, `alpha_i`, `theta`, `n_i`: Lie algebra, roots, highest root, and
  affine Dynkin labels in affine Toda theory.

## Claim Ledger

- Defines an integrable model family as matched UV, perturbing, conserved,
  scattering, and form-factor data.
- Marks compact scalar coordinates, soliton charge, and Thirring current
  dictionaries as current/topological-sector data rather than ordinary
  continuous-symmetry order parameters, cross-referencing the
  Coleman/Mermin--Wagner--Hohenberg boundary.
- Fixes sine-Gordon normalization, topological charge, and the attractive
  regime spectrum.
- Derives the classical sine-Gordon kink mass \(8m/\beta^2\), the
  Pöschl--Teller fluctuation operator, its zero mode and reflectionless
  continuum phase shift, and the DHN/Faddeev--Korepin one-loop correction
  \(M_s=8m/\beta^2-m/\pi+O(\beta^2m)\) in the paired normal-ordering
  convention.  The text emphasizes that this is a fluctuation determinant and
  counterterm calculation, not a moduli-coordinate calculation.
- Checks the same finite DHN mass shift against the exact breather spectrum:
  inserting \(M_s=8m/\beta^2-m/\pi+O(\beta^2m)\) into
  \(m_1=2M_s\sin(\pi\xi/2)\) cancels the \(O(\beta^2m)\) correction and gives
  the perturbative elementary boson mass \(m+O(\beta^4m)\), while omitting or
  halving the finite shift leaves a spurious weak-coupling mass correction.
- Adds the UV-normal-ordered mass-coupling coordinate
  \(M_s(\mu_{\rm UV},\beta_{\rm UV})\), with the dimension check and the
  canonical-field conversion \(\phi=\sqrt{8\pi}\varphi\).
- Derives the breather mass formula from relativistic bound-state kinematics.
- Displays the exact soliton/antisoliton two-state S-matrix datum, separates
  the matrix part from the minimal scalar factor, proves matrix unitarity, and
  derives the physical-strip pole locations that give the breather masses.
- Proves the Yang-Baxter equation for the soliton matrix part by reducing the
  \(8\times8\) component identities to hyperbolic addition formulae.
- Displays the soliton-breather scalar amplitude, proves unitarity and
  crossing, and identifies the direct soliton pole, its crossed partner, and
  the redundant double poles from the fused constituent description.
- Corrects the lightest-breather pole discussion by separating the direct
  \(B_1B_1\to B_2\) pole from its crossed-channel image.
- Defines the neutral block \(F_a(\theta)\), proves unitarity, crossing, pole
  locations, and residue signs, and uses it to display the minimal
  breather-breather amplitudes.
- Proves that the direct pole of \(S_{mn}\) gives the mass of \(B_{m+n}\)
  whenever \((m+n)\xi<1\).
- Derives the canonical free-boson vertex OPE, separating the
  \(V_\alpha V_{-\alpha}\) short-distance exponent
  \(\alpha^2/(2\pi)\) from the scaling dimension \(\alpha^2/(4\pi)\).
- Derives Coleman's coupling relation in the monograph mostly-plus spinor
  chart by representing the massless Thirring Hermitian-current sector as a
  Gaussian scalar with kinetic coefficient \(K=1+g_T/\pi\), then rescaling the
  free-Dirac bosonization mass operator.
- Derives the sine-Gordon/Thirring current dictionary and shows that fermion
  number equals sine-Gordon topological charge.
- Proves the Mandelstam semi-local exchange phase directly from the
  equal-time commutator of \(\varphi\) and the integrated canonical momentum,
  including the anticommutation of identical Mandelstam fields.
- Gives the operator dictionary for currents, the mass operator, the
  Euclidean current square, and chiral higher-spin bilinears, with a
  generating identity for the latter.
- Checks the free-fermion point, the marginal sine-Gordon endpoint, and the
  relevance threshold in the same coupling convention.
- Places chiral bosonization, \(SU(N)_1\) nonabelian bosonization, and compact
  radius defect formulations as convention-dependent extensions rather than
  as undeclared generic statements.
- Defines affine Toda action data and derives the classical mass matrix from
  the affine-root potential.
- Derives the \(A_r^{(1)}\) classical affine Toda mass spectrum from the
  quadratic Hessian by identifying the mass operator with the cycle-graph
  Laplacian, obtaining
  \(M_a^2=4m^2\sin^2(\pi a/(r+1))\), and then deriving the finite \(A_r\)
  Perron--Frobenius relation for the sine mass vector.
- Works out the first non-\(A\) Coxeter mass cell explicitly: for \(D_4\),
  with central node \(2\), the finite Dynkin adjacency equation
  \(I\mathbf M=\sqrt3\,\mathbf M\) gives
  \(\mathbf M=(1,\sqrt3,1,1)\), while the quantum \(S\)-matrix/local-QFT
  comparison remains a separate model-comparison problem.

## Calculation Checks

- `calculation-checks/sine_gordon_smatrix_checks.py` verifies the soliton
  matrix unitarity and Yang-Baxter equation, free-fermion point,
  soliton-breather unitarity/crossing/pole kinematics, lightest-breather
  direct and crossed poles, neutral-block residue signs, and breather-breather
  fusion mass formulae.  It also verifies the semiclassical soliton
  fluctuation calculation: kink trigonometry, Pöschl--Teller zero and
  continuum modes, phase-shift derivative, cutoff/counterterm cancellation,
  and the finite \(-m/\pi\) one-loop mass shift, with negative controls for
  omitted counterterms, half phase shifts, and double-counted zero modes.  It
  also verifies the weak-coupling breather-mass consistency check: the DHN
  finite shift cancels the \(O(\beta^2)\) term in \(m_{B_1}/m\), while the
  classical or half-shift choices fail.  It also verifies the \(A_r^{(1)}\)
  cycle-Laplacian eigenvalues, finite \(A_r\)
  Perron--Frobenius sine-mass relation, and exact \(\mathbb Q[\sqrt3]\)
  \(D_4\) Perron--Frobenius mass cell.
- `calculation-checks/sg_thirring_bosonization_checks.py` verifies the
  vertex-OPE exponent versus scaling dimension, Coleman's coupling map,
  current-dictionary coefficient, Mandelstam exchange phase, free-fermion
  point, and relevance threshold using exact rational arithmetic.  It also
  checks the mostly-plus Clifford/current convention and rejects the old
  anti-Hermitian-current sign by showing that it would move the marginal
  endpoint from \(g_T/\pi=-1/2\) to \(+1/2\).

## Figure Ledger

No figure is included in this pass.  Future figures should include the
sine-Gordon periodic potential with soliton sectors, the soliton-antisoliton
bound-state pole in the rapidity strip, and affine Dynkin diagrams for the
first simply-laced examples.

## Audit Notes

- 2026-06-02 affine-Toda mass-matrix pass: replaced the thin
  Perron--Frobenius/Coxeter mass-ratio sentence by an explicit \(A_r^{(1)}\)
  Hessian calculation, cycle-Laplacian diagonalization, and finite
  Dynkin-adjacency eigenvector check.  The general \(D/E\) Coxeter mass datum
  is now stated as additional algebraic bootstrap input rather than inferred
  from the displayed Hessian.
- 2026-06-03 #562 non-\(A\) affine-Toda mass-cell pass: added the explicit
  \(D_4\) adjacency calculation
  \(I(1,\sqrt3,1,1)=\sqrt3(1,\sqrt3,1,1)\) and the Cartan
  \(2-\sqrt3\) eigenvalue check, with an exact \(\mathbb Q[\sqrt3]\)
  companion verification.  This narrows the assertion-as-derivation gap
  without claiming the quantum affine-Toda construction.
- 2026-06-04 issue #761 convention pass: translated the massive-Thirring
  action, vector current, current square, current dictionary, and Coleman
  coupling coordinate into the monograph mostly-plus spinor convention.  The
  section now uses the Hermitian current
  \(J^\mu=\ii\bar\psi\gamma^\mu\psi\), removes the extra \(\ii\) from the
  Lorentzian kinetic term, and records that the Coleman \(g_T\) coordinate is
  attached to \(-g_T J_\mu J^\mu/2\), equivalently \(+g_T B_\mu B^\mu/2\) for
  the anti-Hermitian bilinear \(B^\mu=\bar\psi\gamma^\mu\psi\).
- 2026-06-04 issue #770 re-audit: added the low-dimensional
  continuous-symmetry caveat so the sine-Gordon/Thirring compact-boson
  dictionary is read as a current/topological-sector equivalence, not as a
  hidden continuous order parameter.
- 2026-06-05 issue #597 DHN fluctuation pass: added the semiclassical
  sine-Gordon soliton mass calculation from the fluctuation operator,
  reflectionless phase shift, normal-ordering counterterm, and zero-mode
  removal.  This addresses the soliton-quantization side of the
  soliton/monopole/instanton backlog at the determinant level rather than by
  adding another moduli-space cell.
- 2026-06-05 issue #728/#597 DHN-to-spectrum pass: added the weak-coupling
  breather-mass consistency proposition showing that the finite DHN shift is
  required for the exact \(B_1\) pole mass to match the perturbative boson
  mass through \(O(\beta^2m)\).  This ties the fluctuation determinant to the
  physical on-shell spectrum rather than treating it as an isolated soliton
  correction.
