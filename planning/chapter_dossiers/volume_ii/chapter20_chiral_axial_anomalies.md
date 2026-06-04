# Volume II, Chiral and Axial Anomalies Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Follows QCD renormalization and the BRST cohomology chapter.
- Precedes global anomalies, spontaneous symmetry breaking, pions, and the
  Wess--Zumino--Witten term.
- Role in the monograph: define local axial and gauge anomalies as
  renormalized Ward identities, derive the two-dimensional and
  four-dimensional contact-term mechanisms, derive the abelian anomaly through
  regulated measure/index language, classify local gauge anomalies through
  BRST descent, and identify which anomalies are inconsistencies and which
  are global symmetry data to be matched.

## Source And Reference Controls

- `SRC-QFT-PDF`: second-sequence handwritten material around QCD, anomalies,
  theta angle, and pions.
- `SRC-STRINGBOOK-APP-O`: local stringbook Appendix O is the primary source
  for anomaly calculations and conventions, especially the dimensional
  reduction treatment of the two-dimensional axial anomaly, the
  four-dimensional axial triangle, chiral gauge anomalies, counterterm/contact
  ambiguity, descent, and anomaly polynomials.
- `SRC-EXTERNAL`:
  `references/sound_references/barnich_brandt_henneaux_local_brst_cohomology_hep-th_0002245.pdf`
  and sidecar, especially Sections 2.3 and 12, for the \(H^{1,n}(s\mid d)\)
  interpretation of anomaly classes.
- `SRC-EXTERNAL`:
  `references/sound_references/bilal_lectures_on_anomalies_0802.0634.pdf`
  and sidecar, especially Sections 3.7, 4.2, 8.3, 9.1--9.4, and 10, for
  measure/index derivations, consistent anomalies, descent equations, and
  anomaly-polynomial normalization.
- Reader-facing bibliographic footnote added for the theorem-level analytic
  inputs: Atiyah--Singer, "The index of elliptic operators. I" for the closed
  spin Dirac index theorem, and Atiyah--Patodi--Singer, "Spectral asymmetry
  and Riemannian geometry" I--III for the boundary spectral correction.  The
  manuscript states the hypotheses and formulas used.  The 2026-05-30
  quoted-theorem expansion now exposes the part of the closed-index mechanism
  used by the anomaly calculation: McKean--Singer cancellation, the local
  Clifford heat-kernel coefficient from the Lichnerowicz endomorphism, and
  the four-form
  normalization
  \(\operatorname{tr}_R(F\wedge F)/(8\pi^2)
  =\epsilon^{\mu\nu\rho\sigma}\operatorname{tr}_R(F_{\mu\nu}F_{\rho\sigma})\,d^4x/(32\pi^2)\).
  It still does not reproduce the full analytic proof of the closed
  Atiyah--Singer or APS theorems.
- The chapter states the descent formulas used for four-dimensional chiral
  fermions but does not reproduce the full proof of the local BRST cohomology
  classification.
- 2026-05-30 quoted-theorem expansion: the cubic gauge-obstruction block now
  exposes the local descent mechanism in the chapter's conventions: the
  symmetric tensor from \(\operatorname{tr}_R(\mathsf F^3)\), the
  ghost-number-one representative \(I_4^{(1)}\), the local counterterm shift,
  and the exact local cohomology input used to turn a nonzero tensor into a
  nontrivial obstruction class.
- The BPST instanton section is a direct in-manuscript derivation.  A
  public-facing check script,
  `calculation-checks/bpst_instanton_normalization_checks.py`, verifies the
  self-dual 't Hooft symbol identities, the quadratic identity entering the
  curvature calculation, the radial integral, topological charge, and
  coupling-coordinate conversion used there, as well as the
  scale-invariant one-instanton center-size measure, zero-mode coupling
  power, one-loop RG exponent, small-instanton boundary-exponent threshold,
  and the general charge-\(k\) framed ADHM quotient dimension,
  quotient-density coarea scaling count, and finite nonzero-mode determinant
  bookkeeping.  The Pauli-Villars determinant-constant continuation adds the
  pure-gauge \(C_N^{\rm PV}\) formula, its
  \(0.466\exp[-1.679N]/[(N-1)!(N-2)!]\) reduction, and the \(SU(3)\)
  value \(1.51\times10^{-3}\).  The 2026-06-03 Uhlenbeck-face continuation
  adds the higher-charge boundary-face codimension and product integrability
  budget.
  The physics-amplitude continuation adds the finite Berezin zero-mode
  saturation check that turns the instanton measure into a correlator
  contribution, including the two-flavor 't Hooft determinant sign.  The
  fluctuation-amplitude continuation adds the proper-time nonzero-mode
  determinant assembly and its multiplication by the zero-mode-projected
  four-fermion source determinant.  The zero-mode-tail continuation adds the
  BPST fundamental zero-mode density envelope, its momentum form factor
  \(zK_1(z)\), its \(R^{-2}\) tail, and the logarithmically infrared-sensitive
  second moment controlling the first nonzero derivative correction to the
  local vertex.  The individual-slot continuation adds the singular-gauge
  fermion zero-mode form factor
  \(F_{\rm zm}(t)=-t\partial_t(I_0K_0-I_1K_1)\), \(t=\rho|p|/2\), and its
  \(3/(4t^3)\) hard tail.  The channel-decomposition continuation derives the
  two-flavor local determinant as scalar/pseudoscalar singlet/triplet channel
  data, including the theta-odd scalar-pseudoscalar mixing sign and the local
  source-curvature splittings \(\chi_\pi-\chi_\delta\) and
  \(\chi_\sigma-\chi_\eta\), together with the finite anomalous axial Ward
  ledger tying those curvatures to the theta shift.  The
  source-typing repair separates independent
  bilinear source
  matrices from ordinary external fermion slots generated by odd sources:
  c-number outer products vanish, while source differentiation gives the
  nonzero four-slot coefficient.  The plane-wave amplitude-assembly
  continuation factors the common instanton-center phase from the
  differentiated right-slot and left-slot determinants, so total momentum
  conservation is produced by the center integral while the individual
  zero-mode form-factor determinants remain inside the size integral.  The
  orientation-projection continuation adds the \(SU(2)\) Haar identities which
  turn two colored zero-mode slots into the antisymmetric invariant tensor and
  replace the four-slot shortcut by the genuine shared-orientation Haar
  projector.  The color-singlet matching continuation adds
  the gauge-invariant source-projection and hadronic pole-residue layer:
  source-to-zero-mode overlaps multiply the hard kernel, while stable-hadron
  amplitudes require a separate spectral/LSZ extraction.  The hard-amplitude
  continuation adds the
  \(N_f=2\) hard-momentum size window, where the same form factors give a
  \(Q^{-2}\) four-fermion coefficient at \(\mu=Q\), the RG-invariant
  \(\Lambda_{\rm ht}^{b_0}Q^{-b_0-2}\) hard falloff, and the large-\(\rho\)
  endpoint distinction between exponential fused-density suppression and the
  individual-slot power test \(b_0+1-3m<-1\).  The hard-size-dominance
  continuation adds the stronger endpoint-tail criterion: convergence of the
  \(SU(3)\), \(N_f=2\) four-slot individual-source kernel leaves only an
  \(R^{-1/3}\) tail after cutting at \(\rho=R/Q\), so dominance near
  \(1/Q\) requires an additional physical source/kinematic estimate.  The
  log-shell continuation restates the same fact per \(\dd\log\rho\): the
  individual-slot shell also decays only as \(R^{-1/3}\), so tenfold
  suppression of the normalized power-tail majorant costs three decades in
  the size cutoff.  The Wilsonian-split continuation makes the
  factorization-scale dependence
  explicit: the short-instanton coefficient and long-distance remainder
  exchange the boundary flux through \(\rho=\mu_I^{-1}\), so the local
  't Hooft vertex is a coefficient, not an observable by itself.  The
  short-OPE continuation then projects that coefficient onto the Ch12
  renormalized-operator bundle, with inverse operator-frame transformation and
  dual operator-mixing RG flow separated from the Wilsonian size-boundary
  flow.  The finite light-fermion determinant frame continuation fixes the
  inverse \( \det Z_R\det Z_L \) transformation law for
  \(\mathcal R_{\rm f}^{\mathcal S}\), separating source-frame covariance from
  local determinant counterterm shifts.  The screened-size continuation adds
  the exact \(I_A(m_{\rm scr})=\frac12m_{\rm scr}^{-A}\Gamma(A/2)\)
  amplitude integral, moment ledger, shell location, and \(SU(3)\), \(N_f=2\)
  mass-saturated \(A=23/3\) specialization when a physical infrared scale is
  supplied.  The thermal-screening continuation ties that abstract scale to
  the high-temperature determinant datum
  \(m_T^2=\pi^2T^2(2N_c+N_f)/3=\pi^2m_D^2/g_{\rm YM}^2\), with an explicit
  residual-window error bound so the Gaussian GPY/HTL coefficient is not
  mistaken for the full finite-temperature determinant.  The thermal-observable
  continuation then pushes that activity into
  \(\chi_{\rm top}^{T,{\rm dig}}=2\zeta_T\), \(b_2=-1/12\), and the
  \(SU(3)\), \(N_f=2\) \(T^{-23/3}\) scaling law for the theta curvature,
  with the determinant residual propagated to the susceptibility.  The 2026-06-03
  verification-contract follow-up records, in the
  calculation-check docstring rather than the TeX, the target claims,
  independent constructions, imported assumptions, negative controls, and
  finite/continuum scope boundary for this instanton companion.
- The index-normalized anomaly-polynomial section is paired with
  `calculation-checks/anomaly_polynomial_descent_checks.py`, which verifies
  the closed four-dimensional Dirac-index coefficient, the local Clifford
  heat-kernel coefficient, the six-form
  \(\widehat A\,\operatorname{ch}\) coefficients, the \(2\pi i\) inflow
  conversion, Standard Model hypercharge sums, and \(SU(N)\)
  fundamental/antifundamental/adjoint cubic-anomaly bookkeeping.  It also
  checks the Abelianized Bardeen--Zumino calibration in which the consistent
  coefficient \(C\) is supplemented by \(\dd(2C\,AF)=2C\,F^2\), giving the
  covariant coefficient \(3C\).  The 2026-06-01 Cartan-restriction
  continuation adds the Abelianized cubic
  counterterm test: a counterterm
  \(H_{ij,k}A^iA^jF^k/2\), \(H_{ij,k}=-H_{ji,k}\), changes
  \(C_{i;jk}\lambda^iF^jF^k\) only by a tensor whose complete
  symmetrization over \(i,j,k\) vanishes.
- `calculation-checks/anomaly_matching_wzw_checks.py` also checks the finite
  Abelianized Bardeen-counterterm algebra used here: shifts of the local
  anomaly representative leave the completely symmetric descent coefficient
  unchanged.  The 2026-06-01 continuation adds the Abelianized cubic descent
  coordinate \(C_{abc}\lambda^aF^bF^c\) and verifies that the homogeneous cubic
  polynomial on commuting backgrounds recovers the symmetric tensor by
  polarization.

## Framework

- Four-dimensional Lorentzian QFT with a Euclidean regulator used for
  heat-kernel and index statements.
- The Fujikawa-style measure statement is a finite-mode Berezinian
  change-of-coordinates calculation: the transformed object is the ordered
  Berezinian density of the odd coefficient variables defined in Volume I's
  fermionic path-integral chapter.  The heat kernel is a gauge-covariant
  spectral regulator for the Berezinian trace, not a Pauli--Villars regulator
  field or determinant-ratio prescription.
- Gauge potentials use the Hermitian convention of the Yang--Mills chapters.
- Generator and coupling conventions are repeatedly cross-referenced to
  \(\operatorname{tr}(t^a t^b)=\delta^{ab}\),
  \([t^a,t^b]=i f^c{}_{ab}t^c\), and
  \(-\frac1{4g_{\mathrm{YM}}^2}\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})\).
- Characteristic classes are written using the anti-Hermitian connection
  \(\mathsf A=-\ii A\), \(\mathsf F=\dd\mathsf A+\mathsf A^2=-\ii F\).
- Fermion chirality signs are stated relative to the chapter's \(\gamma_5\)
  convention.
- The \(\gamma_5\), trace, two-dimensional chirality, and
  dimensional-continuation conventions are now centralized in
  `monograph/tex/volumes/volume_i/chapter16a_spinor_conventions.tex`, and the chapter links to
  the spinor-field chapter and that appendix before starting the anomaly
  calculation.
- Local anomalies are represented by local functionals modulo BRST-exact
  counterterm shifts and total derivatives.
- A finite-regulator background-field chart now explicitly realizes this
  statement as a groupoid cochain: \(C_\Lambda(g;A)=W_\Lambda[A^g]-W_\Lambda[A]\)
  obeys a cocycle identity, and changing the regulated Lagrangian or
  determinant-line frame by a local \(B_\Lambda[A]\) adds the coboundary
  \(B_\Lambda[A^g]-B_\Lambda[A]\).
- An early coordinate-comparison proposition now ties the finite-regulator
  cochain, local BRST descent representative, exponentiated anomaly-line
  transport, inverse inflow line, and determinant/Pfaffian global holonomy
  together as coordinates on one obstruction-to-descent problem.  Local BRST
  cancellation controls the identity component, while flat global holonomies
  are separate based-loop data.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(j^\mu,j_5^\mu\) | vector and axial currents |
| \(\gamma=\gamma^0\gamma^1\) | two-dimensional chirality matrix |
| \(G_A^{\mu\nu}\) | two-dimensional axial-vector current correlator |
| \(Q_C\) | current charge integrated over a Euclidean contour \(C\) |
| \(\Delta Q_A\) | anomalous axial charge transported between contours |
| \(\mathcal D_A\) | Euclidean Dirac operator in a background gauge field |
| \(P_\Lambda,V_\Lambda\) | finite spectral projector and cutoff eigenspace used to define the odd coefficient variables |
| \(\Omega_\Lambda\) | ordered finite-dimensional Berezinian density for the cutoff fermion variables |
| \(J_\Lambda,J_M\) | finite-mode and heat-kernel-regulated Berezinian Jacobian factors |
| \(n_\pm\) | zero modes of chirality \(\pm1\) |
| \(M\) | compact oriented Riemannian spin four-manifold used in the index theorem statement |
| \(S^\pm\) | positive and negative chirality spinor bundles on \(M\) |
| \(E_R,\nabla^E\) | Hermitian bundle and smooth unitary connection associated to the fermion representation \(R\) |
| \(\widehat A(TM)\) | Chern--Weil \(\widehat A\)-form of the tangent bundle |
| \(\operatorname{ch}(E_R,\nabla^E)\) | Chern character form of the gauge bundle |
| \(B_A\) | tangential boundary Dirac operator in the APS collar decomposition |
| \(\eta_{B_A}(0),h_{B_A}\) | eta invariant and boundary zero-mode dimension in the APS formula |
| \(\mathcal A(\zeta,A)\) | gauge variation of the effective action |
| \(\delta_\zeta,D_\mu\zeta\) | infinitesimal gauge-variation derivation on background-field functionals and covariant derivative of the gauge parameter |
| \(\Omega_{\mathrm{loc}}^{p,q}\) | local \(p\)-forms of ghost number \(q\) in the anomaly descent bicomplex |
| \(a_4^{(1)},a_3^{(2)}\) | relative BRST cocycle representative and its descent partner for a four-dimensional anomaly |
| \(b_4^{(0)},b_3^{(1)}\) | local counterterm density and total-derivative ambiguity in the relative coboundary relation |
| \(\mathsf A,\mathsf F\) | anti-Hermitian connection and curvature for descent |
| \(\mathsf c\) | odd anti-Hermitian ghost used in the descent complex |
| \(I_6\) | six-form anomaly polynomial |
| \(\mathcal I_6\) | index-normalized six-form anomaly polynomial whose descent is multiplied by \(2\pi i\) in the Euclidean effective action |
| \(p_1(TM)\) | first Pontryagin Chern--Weil form of the tangent bundle |
| \(I_5^{(0)}\) | Chern--Simons five-form in the descent sequence |
| \(I_4^{(1)}\) | ghost-number-one four-form anomaly representative |
| \(X,\mathsf A_X\) | five-dimensional inflow manifold and extension of the background connection |
| \(W_X^{\mathrm{bulk}}\) | local five-dimensional Chern--Simons response whose boundary variation cancels the consistent anomaly |
| \(d^{abc}\) | symmetric cubic gauge-anomaly tensor |
| \(J_{\mathrm{cons}}\) | consistent current, \(\delta W/\delta A\) |
| \(J_{\mathrm{cov}}\) | covariant current after Bardeen--Zumino improvement |
| \(J_{\mathrm{BZ}}\) | Bardeen--Zumino local polynomial current |
| \(T_R^a\) | anti-Hermitian generator in representation \(R\) used in the Bardeen--Zumino and descent formulas |
| \(\bar\theta\) | anomaly-invariant QCD CP-odd parameter |
| \(Q[A]\) | instanton/topological charge |
| \(Z_{\Lambda,V_4,Q}\) | finite-regulator sector partition weight at topological charge \(Q\) |
| \(E_{\Lambda,V_4}(\theta)\) | finite-regulator vacuum-energy density near \(\theta=0\) |
| \(\mathcal K_Q,\kappa_n^{(Q)},b_{2,\Lambda,V_4},b_{4,\Lambda,V_4}\) | finite-regulator topological-charge cumulant generator, charge cumulants, and branchwise theta-expansion coefficients |
| \(q_{\Lambda,V_4}(x)\) | regulated local topological-charge density integrating to \(Q\) |
| \(\chi_{\rm top}\), \(\chi_{\rm YM}\) | continuum topological susceptibility, and its pure-Yang--Mills specialization |
| \(\mathcal B,\beta\) | theta-branch label set and branch label in a finite-regulator or thermodynamic branch datum |
| \(E_\beta(\theta)\) | theta-branch energy density |
| \(\omega_\beta\) | local state associated with a selected theta branch |
| \(\eta^a_{\mu\nu}\) | self-dual 't Hooft symbol in the BPST construction |
| \(a^\mu,\rho,U\) | instanton center, size, and global gauge-orientation collective coordinates |
| \(B_1,B_2,I,J,W,K\) | ADHM variables and vector spaces, with \(K\simeq\mathbb C^k\) and \(W\simeq\mathbb C^{N_c}\) |
| \(\mu_{\mathbb C},\mu_{\mathbb R}\) | complex and real ADHM moment maps |
| \(M_{AB}(X)\) | orbit Gram matrix for the \(U(K)\) action on the ADHM level set |
| \(J_\mu(X)\) | coarea Jacobian for the ADHM moment-map submersion |
| \(L_{\Lambda,z}^{\rm bos},M_{\Lambda,z}^{\rm gh},\mathcal D_{\Lambda,z}^{R}\) | finite-regulator bosonic Hessian, ghost operator, and fermion kinetic operator in the instanton background |
| \(\mathcal W_{\Lambda}^{\rm nz}(z)\) | finite-regulator nonzero-mode determinant datum in the instanton chart |
| \(K_\Lambda(P_z,P_0;\mu)\) | proper-time logarithmic determinant ratio between the instanton and trivial-sector nonzero-mode operators |
| \(\mathcal W_{\Lambda,{\rm pt}}^{\rm nz}(z;\mu)\) | proper-time representative of the instanton nonzero-mode determinant density |
| \(\mathcal R_{{\rm f},\Lambda}^{\mathcal S}(z;\mu)\) | finite light-fermion nonzero-mode determinant factor after trivial-sector normalization and scheme-\(\mathcal S\) local counterterms |
| \(Z_R,Z_L,\Delta C_{\rm f}\) | finite right/left zero-mode source-frame changes and finite local light-fermion determinant counterterm controlling the frame law of \(\mathcal R_{\rm f}^{\mathcal S}\) |
| \(C_N^{\rm PV}\) | orientation-integrated pure-gauge Pauli-Villars one-instanton determinant constant |
| \(\mathcal Z_{\mathcal O,\Lambda}^{0}(z)\) | finite Berezin coefficient of the zero-mode part of insertions, masses, and sources in a \(Q=1\) instanton background |
| \(M_{ff'},B_{ff'}\) | mass-overlap and external-source matrices whose finite Berezin determinant and minor expansion give the QCD 't Hooft amplitudes |
| \(\Phi,S,P,s_0,\vec s,p_0,\vec p\) | two-flavor chiral, scalar, and pseudoscalar bilinear coordinates used to decompose the local 't Hooft determinant into physical channels |
| \(\kappa_{\rm inst}^{(2)}\) | finite local two-flavor instanton source-density coefficient after the size/orientation/nonzero-mode determinant integral has been controlled |
| \(\mathcal D_A\) | finite singlet-axial Ward vector \(4\partial_\theta+2p\partial_s-2s\partial_p\) acting on the two-flavor local instanton source coordinates |
| \(J_{ff'},J^0_{ff'},\mathcal V_{\rm inst}^0\) | renormalized chiral scalar source coordinate, its zero-mode projection, and the zero-mode source functional used to state the mass/source RG transport of the instanton vertex |
| \(\bar\chi_A,\chi_B\) | odd generating coordinates for differentiated external fermion slots in the instanton zero-mode sector |
| \(R_{Af}(z),L_{fB}(z)\) | right-slot and left-slot zero-mode overlap matrices whose differentiated coefficient is \(\det R\,\det L\) |
| \(G^{(4)}_{\eta,\Lambda,Q=1}\) | source-differentiated finite-regulator one-instanton contribution to the smeared four-fermion amplitude |
| \(h_\rho(y),\widehat h_\rho(q),M_2(R)\) | normalized BPST zero-mode density radial envelope, momentum form factor \(zK_1(z)\), and truncated second moment in the local-vertex expansion |
| \(F_{\rm zm}(t)\) | individual singular-gauge BPST fermion zero-mode slot form factor, \(F_{\rm zm}(t)=-t\partial_t(I_0K_0-I_1K_1)\) with \(t=\rho|p|/2\) |
| \(\mathcal P\) | total right-minus-left external momentum carried by a plane-wave instanton four-fermion source coefficient |
| \(\mathfrak A_2^{\rm lin}(\rho,U;\{p_R,p_L\})\) | product of the right-slot and left-slot individual zero-mode form-factor determinants left after the instanton center phase is factored out |
| \(U_i{}^\alpha\) | \(SU(2)\) instanton core-orientation matrix element whose Haar integral projects colored zero-mode slots onto invariant tensors |
| \(A_{i_1i_2j_1j_2},B_{i_1i_2j_1j_2}\) | two invariant four-fundamental \(SU(2)\) tensors used in the shared-orientation Haar projector |
| \(\mathcal K_{\rm ex},\mathcal K_{\rm lead},\mathcal C_{\rm pg}^{\mathcal S},R_{\rm det},R_{\rm zm},R_{\rm src},R_{\rm Schur},R_{\rm end}\) | exact and leading one-instanton source-amplitude densities, pure-gauge collective/determinant density, and the finite error-budget pieces for determinant, zero-mode/source, source matching, Schur, and endpoint residuals |
| \(B^{\mathcal J}_{AB},\Phi^R,\Phi^L\) | color-singlet source-projected zero-mode matrix and source-to-zero-mode overlap maps used to match the auxiliary hard instanton kernel to gauge-invariant correlators |
| \(\mathcal I_{\rm hard}(Q),\mathcal J_{b_0}(\mathbf c;\mathcal F)\) | hard-momentum \(N_f=2\) instanton size factor and its dimensionless selected-form-factor integral |
| \(\mathfrak s_{\rm hard}(s),\Delta\) | hard instanton log-size shell density and its power-tail suppression exponent \(\Delta=\sigma-b_0-2\) |
| \(C_{\rm inst}^{(4)}(Q;R),\mathcal P_{\rm orient}\) | specialized \(SU(3)\), \(N_f=2\) hard four-fermion instanton coefficient and shared orientation projector, with the Pauli-Villars pure-gauge constant, light-fermion determinant factor, and explicit endpoint residual |
| \(\mu_I,\rho_I,K_\Lambda(\rho)\) | Wilsonian instanton factorization scale, cutoff \(\rho_I=\mu_I^{-1}\), and fully paired finite-regulator size integrand whose boundary flux transfers between the short coefficient and long-distance remainder |
| \(C_I^{<},[O_I]_\mu,\gamma_{IK}\) | short-instanton OPE coefficient, retained renormalized operator basis, and operator-mixing anomalous-dimension matrix used to distinguish composite-operator RG transport from size-factorization flow |
| \(\zeta_\Lambda\), \(n_\pm\), \(E_{\rm dig}\), \(b_2^{\rm dig}\) | dilute instanton/anti-instanton activity, occupation numbers, conditional dilute-gas vacuum energy, and fourth-order theta-curvature coefficient |
| \(\zeta_m^{[\rho_-,\rho_+]}\) | mass-saturated one-instanton vacuum activity in a finite size window |
| \(m_{\rm scr},A,\mathcal A_{\rm scr}^{(0)}\) | physical infrared screening scale, screened size-integral power \(A=b_0+\beta_{\mathcal X}-4\), and leading screened one-instanton amplitude |
| \(m_T,R_T,\mathcal A_T^G\) | high-temperature determinant screening scale, finite-temperature determinant residual, and Gaussian thermal one-instanton approximation |
| \(\zeta_T^G,\chi_{\rm top}^{T,G}\) | Gaussian high-temperature dilute one-instanton activity and its induced topological susceptibility |
| \(T,\mathcal D_{\rm zm},E_{\rm zm},\rho_{\rm zm}\) | instanton--anti-instanton near-zero-mode overlap matrix, projected Dirac block, remainder, and singular-value density used in the instanton-liquid criterion |
| \(\beta_{\mathcal X}\) | small-instanton boundary exponent of a specified scalar insertion datum \(\mathcal X\) |
| \(A_\alpha(\mathcal X),G_\beta(\mathcal X)\) | Uhlenbeck bubbling-scale and collision-face exponents in the multi-instanton boundary budget |
| \(\mathcal O_{N_c}\) | embedded one-instanton orientation orbit \(U(N_c)/(U(N_c-2)\times U(1))\) |
| \(g_{\rm ht},g_{\rm YM}\) | common half-trace coupling and active trace-delta monograph coupling, related by \(g_{\rm ht}=\sqrt2\,g_{\rm YM}\) for the displayed \(SU(2)\) instanton |
| \(b_0\) | one-loop coefficient of the half-trace Yang--Mills beta function in the instanton-density subsection |
| \(\dd\Omega_{N_c}\) | chosen invariant density on the embedded one-instanton orientation orbit |
| \(\psi_{0,\alpha},\xi_\alpha\) | fermion zero-mode wavefunction and its Grassmann coefficient |

## Issue-Pass Notes

- 2026-05-24 issue #397 pass: verified that no stale reference to a
  "preceding QCD chapter" remains for the \(\gamma_5\) convention.  The
  anomaly chapter now explicitly links the convention to the spinor-field
  chapter and the chapter-local spinor-convention section.

## Claims Established

- The axial anomaly is a renormalized composite-operator identity, not a
  classical equation of motion.
- In two dimensions the anomalous Ward identity is the finite remnant of a
  regulated axial-vector current contact term.
- The contour-charge interpretation of the two-dimensional anomaly identifies
  the anomalous phase as the integral of the divergence through the domain
  crossed by the deformed contour.
- In four dimensions the one-axial, two-vector triangle coefficient is carried
  by the evanescent \(\ell_\perp\) part of the dimensionally regulated loop
  momentum when vector Ward identities are preserved.
- The regulated trace of \(\gamma_5\) in a gauge background is the
  heat-kernel limit of finite-mode Berezinian traces and gives the local
  anomaly density.  Its integral is identified with a Fredholm index only
  under the closed spin Dirac hypotheses of the Atiyah--Singer theorem; in the
  flat tangent specialization this is tied to the McKean--Singer supertrace,
  the local Clifford heat-kernel coefficient
  \((4\pi)^{-2}\frac12(\frac12)^2
   \operatorname{tr}_{\rm spin}(\Gamma_5\Gamma\Gamma\Gamma\Gamma)\), and the
  Chern--Weil normalization
  \[
    \operatorname{index}\mathcal D_{A,+}
    =
    (32\pi^2)^{-1}\int_M
    \epsilon^{\mu\nu\rho\sigma}
    \operatorname{tr}_R(F_{\mu\nu}F_{\rho\sigma})\,d^4x .
  \]
- With boundary and APS spectral boundary condition, the index is
  \[
    \int_M[\widehat A(TM)\operatorname{ch}(E_R,\nabla^E)]_4
    -
    \frac{\eta_{B_A}(0)+h_{B_A}}2,
  \]
  up to the standard local transgression term when the data are not product
  near the boundary.
- The Wess--Zumino consistency condition is derived as an integrability
  condition: the gauge-variation derivations obey
  \([\delta_{\zeta_1},\delta_{\zeta_2}]A_\mu
  =D_\mu[\zeta_1,\zeta_2]\), and applying the same commutator to
  \(W[A]\) gives
  \[
    \delta_{\zeta_1}\mathcal A(\zeta_2,A)
    -
    \delta_{\zeta_2}\mathcal A(\zeta_1,A)
    =
    \mathcal A([\zeta_1,\zeta_2],A).
  \]
- Gauge anomalies are ghost-number-one local BRST cohomology classes.
- The finite-regulator cochain \(C_\Lambda(g;A)\) is the additive coordinate
  of the anomaly line: it satisfies the groupoid cocycle law, local
  counterterms add groupoid coboundaries, exponentiation gives the anomaly
  line transport cocycle, and inflow supplies the inverse line coordinate.
- The descent construction is now stated as a bicomplex:
  \(\Omega_{\mathrm{loc}}^{p,q}\) carries \(d\) of bidegree \((1,0)\) and
  \(s\) of bidegree \((0,1)\), with \(d^2=s^2=sd+ds=0\).
- A four-dimensional local anomaly density is a relative cocycle
  \(a_4^{(1)}\) obeying \(s a_4^{(1)}-d a_3^{(2)}=0\), modulo
  \(a_4^{(1)}\sim a_4^{(1)}+s b_4^{(0)}+d b_3^{(1)}\), hence a class in
  \(H^{1,4}(s\mid d)\).
- The text proves the local-functional identification: Wess--Zumino
  consistency gives the relative cocycle condition, local counterterms give
  relative coboundaries, and any relative cocycle gives a consistent local
  anomalous variation after integration.  The proof now makes explicit the
  Chevalley--Eilenberg role of the ghost, the local variational-bicomplex
  step turning integrated zero into a total derivative, and the boundary or
  inflow hypotheses.
- In four dimensions the local chiral gauge anomaly descends from the six-form
  polynomial \(I_6\propto \operatorname{tr}\mathsf F^3\).
- The index-normalized anomaly polynomial for a left-handed Weyl fermion is
  \([\widehat A(TM)\operatorname{ch}_R(E)]_6\), whose four-dimensional
  expansion is
  \[
    \frac16\operatorname{tr}_R(\ii\mathsf F/2\pi)^3
    -
    \frac1{24}p_1(TM)\operatorname{tr}_R(\ii\mathsf F/2\pi).
  \]
  The first term is the cubic gauge/flavor anomaly; the second is the mixed
  gauge-gravitational anomaly.
- For a \(U(1)\) symmetry, the gauged local anomaly constraints include both
  \(\sum q_i^3=0\) and \(\sum q_i=0\), plus mixed nonabelian-\(U(1)\)
  constraints.  One Standard Model generation satisfies these sums.
- For \(SU(N)\), \(N\ge3\), the cubic anomaly coordinate obeys
  \(A(\square)=1\), \(A(\overline\square)=-1\), and
  \(A(\operatorname{adj})=0\), so vectorlike fundamentals cancel in a
  left-handed description.
- Anomaly matching is formulated as equality of anomaly lines under an RG flow
  that preserves the background-field groupoid up to local counterterms.
- The BRST descent is displayed as
  \(\dd I_5^{(0)}=I_6\), \(sI_5^{(0)}=\dd I_4^{(1)}\), and
  \(sI_4^{(1)}=\dd I_3^{(2)}\), with the even gauge parameter obtained by
  replacing the odd ghost \(\mathsf c\) by \(\lambda\).
- The five-form Chern--Simons representative is now derived from the
  Chern--Weil path \(\mathsf A_t=t\mathsf A\), including the explicit
  integrals that give the coefficients \(1,\frac32,\frac35\).  The same
  homotopy gives the \(n=2\) descent coefficients \(1,\frac12\) in
  \(I_4^{(1)}\), so these numbers are no longer hidden in the word
  "standard."
- Bardeen counterterms shift four-form representatives but not the symmetric
  cohomology coordinate of the anomaly polynomial: in an Abelianized chart
  \(d'_{abc}=d_{abc}+\frac12(h_{ab,c}+h_{ac,b})\) with
  \(h_{ab,c}=-h_{ba,c}\), hence \(d'_{(abc)}=d_{(abc)}\).  This is the
  coefficient later compared with the Wess--Zumino--Witten level.
- Local anomaly inflow is displayed as the bulk-boundary identity
  \[
    \delta_\lambda\left(W_M[\mathsf A]+W_X^{\mathrm{bulk}}[\mathsf A_X]\right)
    =
    \int_M I_4^{(1)}(\lambda,\mathsf A)
    -
    \int_{\partial X}I_4^{(1)}(\lambda,\mathsf A_X)
    =
    0,
  \]
  with \(W_X^{\mathrm{bulk}}=-\int_X I_5^{(0)}\) and
  \(\partial X=M\).
- The Callan--Harvey mechanism is identified as the domain-wall realization of
  this identity: localized chiral modes carry the boundary anomaly and the
  bulk Chern--Simons response supplies the opposite variation.
- Local gauge-anomaly cancellation is the vanishing of the symmetric cubic
  tensor \(d^{abc}\) for the gauged symmetry.
- The consistent current is obtained from the effective action and obeys the
  Wess--Zumino consistency condition.
- The covariant current differs from the consistent current by a
  Bardeen--Zumino current and need not be a functional derivative of a local
  effective action.
- The Bardeen--Zumino current is displayed both as a dual three-form and as
  explicit component polynomials:
  \[
    J_{\mathrm{BZ}}^{a\mu}
    =
    \frac{\kappa}{2}\epsilon^{\mu\nu\rho\sigma}
    \operatorname{tr}_R
    T_R^a(\mathsf A_\nu\mathsf F_{\rho\sigma}
    +\mathsf F_{\rho\sigma}\mathsf A_\nu
    -\mathsf A_\nu\mathsf A_\rho\mathsf A_\sigma)
  \]
  and the expanded \(\partial\mathsf A\) form with the noncommutative ordering
  written explicitly in the manuscript.
- In a one-generator Abelianized coordinate, the descent
  \(I_6=C F^3\), \(I_5^{(0)}=C A F^2\), and
  \(I_4^{(1)}=C\lambda F^2\) gives the consistent coefficient \(C\), while
  the Bardeen--Zumino current has
  \(\star J_{\rm BZ}=2C AF\) and
  \(\dd\star J_{\rm BZ}=2C F^2\).  The covariant Ward representative
  therefore has coefficient \(3C\).  This is a local current-representative
  calibration, not a second anomaly class.
- A nonzero global-symmetry anomaly is data to be matched by the infrared
  theory, while a nonzero gauge anomaly obstructs the gauge theory.
- The strong CP parameter is the anomaly-invariant combination of the
  topological angle and the quark mass phase.
- The topological susceptibility is defined as a thermodynamic and continuum
  limit of a finite-regulator cumulant.  At finite regulator,
  \[
    E_{\Lambda,V_4}''(0)
    =
    V_4^{-1}
    \left(\langle Q^2\rangle-\langle Q\rangle^2\right),
  \]
  and the CP-invariant case has \(\langle Q\rangle=0\).  The finite identity,
  the existence of the continuum limit, and its use in large-\(N_c\) chiral
  matching are kept logically separate.
- The finite-regulator theta expansion is now tracked through the full charge
  cumulant generator: \(E(\theta)-E(0)=-V_4^{-1}\mathcal K_Q(i\theta)\),
  \(E^{(n)}(0)=-i^n\kappa_n^{(Q)}/V_4\), and in a CP-invariant finite volume
  \(b_2=-\kappa_4/(12\kappa_2)\), \(b_4=\kappa_6/(360\kappa_2)\).  The dossier
  flags the branch/counterterm scope: these are exact finite identities, while
  continuum theta coefficients require a selected analytic branch and a fixed
  local theta-counterterm convention.
- When the finite regulator supplies a local density
  \(q_{\Lambda,V_4}(x)\) whose integral is \(Q\), the same susceptibility is
  the finite double integral of the connected density correlator, reducing in
  a periodic translation-invariant volume to the zero-momentum
  \(\int\langle q(x)q(0)\rangle^{\rm c}\).  The continuum version includes
  the contact term fixed by the local \(\theta\)-counterterm convention; a
  shift \(\frac12c_\theta\theta^2\) in the vacuum energy shifts both
  \(E''(0)\) and the integrated density contact term by \(c_\theta\).
- Theta branches are formulated as a datum, not presumed as folklore.  A
  unique branch of smallest energy density dominates the thermodynamic limit
  under the stated uniform free-energy asymptotics.  Convex mixtures of pure
  theta branches fail cluster decomposition by the branch-space covariance
  of local one-point functions unless no local observable distinguishes the
  branches or the mixture is supported on one branch.
- The BPST connection
  \(A_\mu=2\eta^a_{\mu\nu}(x-a)^\nu[(x-a)^2+\rho^2]^{-1}T_a\) has curvature
  \(F_{\mu\nu}=-4\rho^2\eta^a_{\mu\nu}[(x-a)^2+\rho^2]^{-2}T_a\), is
  self-dual, has \(Q=1\), and saturates the instanton action bound.
- The familiar one-instanton action \(8\pi^2/g_{\rm ht}^2\) in the common
  half-trace coupling equals \(4\pi^2/g_{\rm YM}^2\) in the monograph's
  trace-delta coupling coordinate.
- The \(SU(2)\), \(k=1\) instanton has eight bosonic zero modes:
  translations, size, and \(SU(2)/\mathbb Z_2\) orientation.  The
  \(SU(N_c)\) embedded one-instanton moduli count is \(4N_c\).
- The general framed charge-\(k\) ADHM quotient is defined by
  \(\mu_{\mathbb C}=0\), \(\mu_{\mathbb R}=0\), stability, and quotient by
  \(U(K)\).  At smooth stable transverse points its local real dimension is
  \(4kN_c\), with the four center coordinates given by the trace parts of
  \(B_1,B_2\).  Small-instanton boundary strata correspond to charge
  collapsing to point configurations in the Uhlenbeck compactification.
- The ADHM quotient density is defined as the Riemannian density on the
  horizontal quotient of the regular moment-map level set.  Its coarea form
  divides the level-set density by the square root of the orbit Gram
  determinant and, equivalently, inserts the moment-map coarea Jacobian in an
  ambient delta-function representation.  This density is only the classical
  zero-mode part of the instanton measure; nonzero-mode determinants,
  operator renormalization, and boundary estimates remain separate analytic
  data.
- The finite-regulator nonzero-mode datum \(\mathcal W_\Lambda^{\rm nz}\)
  separates the bosonic Hessian determinant, ghost determinant, and
  fermion determinant/Pfaffian-line factor.  It is a scalar only after the
  anomaly-line and fermion-zero-mode pairings have been specified.  Local
  counterterms are part of the regulated Lagrangian and shift the determinant
  datum by the corresponding finite counterterm difference in the instanton
  background.
- The proper-time representative of \(\mathcal W_\Lambda^{\rm nz}\) is a
  heat-kernel trace difference with collective-coordinate, residual-gauge,
  and fermion zero modes removed before determinant formation.  Its small-time
  asymptotics supply local counterterms and the universal
  \((\mu\rho)^{b_0}\) running factor, while the finite remainder is the
  determinant constant of the selected scheme.
- A physical instanton contribution is not the moduli space alone.  In a
  finite regulator it is the collective-coordinate integral of
  \(\exp[-S_\Lambda(A_z)+\ii\theta]\mathcal W_\Lambda^{\rm nz}(z)\) multiplied
  by the zero-mode Berezin coefficient
  \(\mathcal Z_{\mathcal O,\Lambda}^{0}(z)\) of the operator insertions,
  masses, or sources.  If the zero-mode top monomial is absent, the instanton
  sector contribution to that correlator vanishes.
- The QCD 't Hooft determinant is derived as the finite Berezin determinant
  of the flavor source matrix pairing the instanton zero modes.  For slowly
  varying external quark fields \(B_{ff'}=\rho^3\bar\psi_{Rf}\psi_{Lf'}\);
  for complete mass saturation the same determinant has the phase of
  \(\det M\), so the one-instanton vacuum term depends on
  \(\bar\theta=\theta+\arg\det M\).
- More generally \(\det(M+B)\) expands as complementary minors
  \(\det M_{I^c,J^c}\det B_{I,J}\).  Differentiating with respect to
  external zero-mode-pair sources therefore inserts the antisymmetric source
  minor and leaves precisely the complementary mass minor to saturate the
  unobserved zero modes.
- For \(N_f=2\), the smeared four-fermion instanton amplitude is the
  source-differentiated collective-coordinate integral of the proper-time
  nonzero-mode determinant times the zero-mode coefficient.  An independent
  even bilinear source contributes \(\det B\); ordinary c-number external
  fermion slots are generated by odd sources and give the differentiated
  coefficient \(\det R\,\det L\).  A single c-number outer product
  \(u_fv_{f'}\) has zero two-flavor determinant and is not the physical
  four-slot amplitude.
- The BPST fundamental zero-mode density has normalized radial envelope
  \(h_\rho(y)=2\rho^2/[\pi^2(y^2+\rho^2)^3]\).  Its zeroth moment is finite
  and its momentum-space form factor is \(zK_1(z)\), \(z=\rho|q|\).  The
  mass outside \(|y|<R\) is
  \((1+2(R/\rho)^2)/(1+(R/\rho)^2)^2\), while its truncated second moment
  grows like \(4\rho^2\log(R/\rho)\).  Thus the local 't Hooft vertex is the
  zeroth adiabatic term; derivative corrections require the external
  wave-packet or infrared cutoff data, equivalently the small-\(q\rho\)
  expansion contains \(q^2\rho^2\log(q\rho)\).
- The individual singular-gauge fermion zero-mode slot has dimensionless
  momentum form factor
  \(F_{\rm zm}(t)=-t\partial_t(I_0K_0-I_1K_1)\), \(t=\rho|p|/2\).  It is
  normalized by \(F_{\rm zm}(0)=1\) and has hard tail
  \(F_{\rm zm}(t)\sim3/(4t^3)\).  This power tail is distinct from the
  exponential \(zK_1(z)\) tail of the fused bilinear density.
- For \(N_f=2\), the local determinant vertex has the channel decomposition
  \[
    e^{i\theta}\det\Phi+e^{-i\theta}\det\Phi^\dagger
    =
    \frac{\cos\theta}{2}
    (s_0^2-\vec s^{\,2}-p_0^2+\vec p^{\,2})
    -
    \sin\theta(s_0p_0-\vec s\cdot\vec p).
  \]
  Thus the zero-mode determinant distinguishes scalar singlet/triplet and
  pseudoscalar singlet/triplet channels while retaining the same anomalous
  \(U(1)_A\) phase ledger.  The coefficient remains the regulated
  size/orientation/nonzero-mode determinant integral, so this is channel
  content, not a bound-state mass prediction.
- If the regulated local source calculation supplies a finite coefficient
  \(\kappa_{\rm inst}^{(2)}\), then the instanton contribution to the local
  source curvatures is
  \(\chi_\sigma^{\rm inst}=\chi_{\pi_a}^{\rm inst}
  =\kappa_{\rm inst}^{(2)}\cos\theta\) and
  \(\chi_{\delta_a}^{\rm inst}=\chi_\eta^{\rm inst}
  =-\kappa_{\rm inst}^{(2)}\cos\theta\), with CP-odd
  \(\sigma\)-\(\eta\) and \(\delta\)-\(\pi\) mixings proportional to
  \(\sin\theta\).  At \(\theta=0\) this gives the local
  \(U(1)_A\)-violating splittings
  \(\chi_{\pi_a}-\chi_{\delta_a}=\chi_\sigma-\chi_\eta
  =2\kappa_{\rm inst}^{(2)}\).  These are source-curvature contributions in a
  controlled local window, not the full zero-momentum QCD susceptibilities.
  The same finite functional obeys the anomalous singlet-axial Ward vector
  identity \( (4\partial_\theta+2p\partial_s-2s\partial_p)\mathcal W=0 \)
  to the declared local order; differentiating it gives
  \(\partial_\theta\chi_s=m_{sp}\), \(\partial_\theta\chi_p=-m_{sp}\), and
  \(\chi_s-\chi_p=-2\partial_\theta m_{sp}\).  Thus the local susceptibility
  splitting is tied to the anomalous theta shift rather than being an
  independent channel-label assertion.
- The source-amputated instanton four-fermion kernel is obtained by removing
  only adjacent external pole-residue factors.  For differentiated linear
  sources these are source-slot residues multiplying \(\det R\,\det L\); for
  an independent bilinear source they are row and column factors multiplying
  \(\det B\).  Amputation does not remove the selected zero-mode form factors,
  spin-color orientation tensors, the nonzero-mode determinant, or the
  collective-coordinate integral.  Because colored quarks are not physical
  asymptotic states in confining QCD, this is a source-amputated/partonic
  coordinate, not a gauge-invariant quark \(S\)-matrix element.
- For plane-wave source probes of the same \(N_f=2\) kernel, the right-slot
  determinant carries \(\exp(i(p_{R,1}+p_{R,2})\cdot a)\) and the left-slot
  determinant carries \(\exp(-i(p_{L,1}+p_{L,2})\cdot a)\).  The center
  collective-coordinate integral therefore supplies total momentum
  conservation with \(\mathcal P=\sum p_R-\sum p_L\), while the individual
  zero-mode form-factor determinants, nonzero-mode determinant, and size
  density stay inside the amplitude integral.  This records the actual
  four-point-amplitude assembly rather than only the local selection rule.
- The embedded \(SU(2)\) color-orientation coordinate acts as a Haar
  projection on the zero-mode tensor, not only as a volume factor.  The
  two-slot identity
  \(\int U_i{}^\alpha U_j{}^\beta dU=\frac12
  \varepsilon_{ij}\varepsilon^{\alpha\beta}\) turns a pair of source covectors
  into the antisymmetric color tensor times their determinant.  The four-slot
  \(N_f=2\) core coefficient now uses the single shared-orientation projector
  on the two-dimensional invariant subspace of four fundamentals:
  the \(A,B\) Gram matrix is \(\begin{psmallmatrix}4&2\\2&4\end{psmallmatrix}\)
  and \(G^{-1}=\begin{psmallmatrix}1/3&-1/6\\-1/6&1/3\end{psmallmatrix}\).
  Any further determinant factor or vanishing statement belongs to the Berezin
  source coefficient and color-singlet contraction, not to a factorized Haar
  average.
- Gauge-invariant color-singlet source matching is now separated from colored
  source amputation.  In the selected \(N_f=2\) chirality-violating channel,
  the zero-mode source matrix has the projected form
  \(B^{\mathcal J}=\Phi^R B^{\rm amp}\Phi^L+B^{\rm rem}\).  The determinant
  identity is pointwise in the instanton collective coordinate, so
  \(z\)-dependent source overlaps must remain inside the \((a,\rho,U)\)
  integral.  Stable-hadron amplitudes require the usual color-singlet
  spectral/LSZ residue extraction; BPST data do not determine the hadron
  residues or the long-distance matrix element of the induced 't Hooft
  operator.
- In an \(N_f=2\) hard four-fermion kinematic window, retaining the selected
  zero-mode form factors turns the universal one-loop size factor into
  \[
    Q^{b_0}\int_0^\infty
    \rho^{b_0+1}
    \prod_{\ell=1}^{m}\mathcal F_\ell(c_\ell Q\rho)\,d\rho
    =
    Q^{-2}\int_0^\infty
    s^{b_0+1}
    \prod_{\ell=1}^{m}\mathcal F_\ell(c_\ell s)\,ds .
  \]
  Here \(m=4\) for differentiated external fermion slots, while the fused
  bilinear-source specialization has \(m=2\) and
  \(\mathcal F_\ell(z)=zK_1(z)\).
  This \(Q^{-2}\) is the engineering dimension ledger at \(\mu=Q\).  Rewriting
  the one-loop action as
  \(\exp[-8\pi^2/g_{\rm ht}^2(Q)]=(\Lambda_{\rm ht}/Q)^{b_0}\) gives the full
  hard asymptotic factor
  \(\Lambda_{\rm ht}^{b_0}Q^{-b_0-2}\mathcal J_{b_0}(\mathbf c;\mathcal F)\), up to the
  logarithmic collective-coordinate prefactor and higher-loop matching.  Fused
  bilinear density form factors exponentially suppress large instantons, but
  four individual singular-gauge fermion slots give only
  \((Q\rho)^{-12}\).  The \(SU(3)\), \(N_f=2\) differentiated hard kernel
  passes the large-\(\rho\) power test by the margin \(10-b_0=1/3\); a soft
  slot or a failed test leaves a real infrared endpoint problem.  The
  mass-saturated vacuum theta term below has no hard external cutoff, which is
  why its large-\(\rho\) behavior is an infrared input rather than a
  semiclassical output.
- The instanton size integral now has an explicit Wilsonian split.  For the
  fully paired finite-regulator integrand \(K_\Lambda(\rho)\),
  \[
    \mathcal A_\Lambda^{<}(\mu_I)=\int_0^{\mu_I^{-1}}K_\Lambda(\rho)\,d\rho,
    \qquad
    \mathcal A_\Lambda^{>}(\mu_I)=\int_{\mu_I^{-1}}^{\rho_{\max}}
    K_\Lambda(\rho)\,d\rho ,
  \]
  and
  \(\partial_{\log\mu_I}\mathcal A_\Lambda^{<}
  =-\rho_IK_\Lambda(\rho_I)\),
  \(\partial_{\log\mu_I}\mathcal A_\Lambda^{>}
  =+\rho_IK_\Lambda(\rho_I)\).  The short-size 't Hooft coefficient becomes
  physical only after the long-distance remainder or matching matrix element
  cancels this artificial boundary flux.
- The short-size coefficient is now also tied to the renormalized local
  operator bundle:
  \[
    G_{\mathcal J,\Lambda}^{<}
    =
    \sum_I C_I^{<}(\mu_I,\mu)
    \langle\mathcal J[O_I]_\mu\rangle
    +R_{\rm OPE}^{<}.
  \]
  With the chapter-12 convention
  \(\partial_{\log\mu}[O_I]_\mu=-\gamma_{IK}[O_K]_\mu\), the coefficient row
  obeys
  \(\partial_{\log\mu}C_K^{<}=C_I^{<}\gamma_{IK}\), while a finite operator
  frame change \([\widetilde O_A]=M_{AI}[O_I]\) gives
  \(\widetilde C_A^{<}=C_I^{<}(M^{-1})_{IA}\).  This operator-scheme transport
  is distinct from the size-factorization flow
  \(\partial_{\log\mu_I}C_I^{<}=-\rho_IK_I^{\rm OPE}(\rho_I)\).
- For massive vectorlike QCD, the vacuum instanton term is now separated as a
  finite-size-window activity:
  \[
    \zeta_m^{[\rho_-,\rho_+]}
    \propto
    |\det M(\mu)|\,\mu^{b_0}
    \int_{\rho_-}^{\rho_+}\rho^{b_0+N_f-5}\,d\rho .
  \]
  Each mass-saturated Dirac zero-mode pair supplies \(m_f\rho\), the phase is
  \(\theta+\arg\det M\), and a massless unsourced flavor kills the vacuum
  activity.  The small-\(\rho\) endpoint is finite iff \(b_0+N_f>4\); for
  \(SU(3)\) the margin is \(7+N_f/3\), while extending the same one-loop
  formula to \(\rho=\infty\) gives an infrared power divergence.  A finite
  dilute activity therefore requires extra infrared physics or a separate
  controlled window.
- If a physical infrared mechanism supplies a positive Gaussian screening
  factor \(\exp[-m_{\rm scr}^2\rho^2]\) in the same regulated amplitude, the
  leading screened size integral is
  \(\frac12K_0m_{\rm scr}^{-A}\Gamma(A/2)\), with
  \(m_{\rm scr}^2\langle\rho^2\rangle=A/2\).  For \(SU(3)\), \(N_f=2\)
  mass-saturated QCD, \(A=23/3\), so the screened leading activity scales as
  \(m_{\rm scr}^{-23/3}\Gamma(23/6)\).  This is a controlled formula only
  when the resulting dominant size shell remains in the weak-coupling window;
  it does not justify the unscreened large-\(\rho\) integral.
- At high temperature, the leading periodic-instanton fluctuation determinant
  supplies the physical screening scale
  \(m_T^2=\pi^2T^2(2N_c+N_f)/3=\pi^2m_D^2/g_{\rm YM}^2\) in the trace-delta
  Debye convention.  If the remaining determinant/caloron-shape residual obeys
  \(|R_T|\le\varepsilon_T\) in the chosen amplitude window, then the Gaussian
  instanton amplitude has multiplicative error bounded by
  \(e^{\varepsilon_T}-1\).  For \(SU(3)\), \(N_f=2\) mass saturation,
  \(\pi^2T^2\rho_{\rm shell}^2=23/16\).  This is a finite-temperature
  determinant statement, not a zero-temperature instanton-liquid prediction.
- Combining the thermal activity with the dilute-gas hypothesis gives the
  leading thermal theta curvature
  \(\chi_{\rm top}^{T,{\rm dig}}=2\zeta_T\) and \(b_2^{T,{\rm dig}}=-1/12\).
  The residual bound on the determinant activity propagates unchanged to
  \(\chi_{\rm top}\).  In the \(SU(3)\), \(N_f=2\) mass-saturated channel the
  Gaussian susceptibility scales as
  \(|m_um_d|\Lambda_{\rm ht}^{29/3}T^{-23/3}\) up to finite determinant,
  source-frame, and running-mass coordinates.
- The dilute instanton gas is now stated only as a controlled amplitude
  expansion after the regulated one-instanton calculation has supplied a
  finite activity \(\zeta_\Lambda\).  Under Poisson factorization it gives
  \(E_{\rm dig}(\bar\theta)-E_{\rm dig}(0)=2\zeta_\Lambda(1-\cos\bar\theta)\),
  \(\chi_{\rm top}^{\rm dig}=2\zeta_\Lambda\), even Skellam cumulants
  \(\kappa_{2m}=2V_4\zeta_\Lambda\), and \(b_2^{\rm dig}=-1/12\).  The chapter
  explicitly states the failure modes: unsaturated massless zero modes,
  infrared-divergent size integrals, uncontrolled small-instanton boundaries,
  and non-negligible instanton interactions.
- The instanton-liquid bridge is now formulated as finite zero-mode overlap
  algebra rather than moduli geometry.  For \(n_+\) instantons and \(n_-\)
  anti-instantons, the chiral near-zero-mode block contains a rectangular
  overlap matrix \(T\) and gives
  \(m^{|n_+-n_-|}\prod_\alpha(m^2+s_\alpha^2)\), plus the resolvent
  \(|n_+-n_-|/m+2m\sum_\alpha(m^2+s_\alpha^2)^{-1}\), in the leading
  projected block \(E_{\rm zm}=0\).  Exact full-operator zero modes require an
  index-preserving regulator and a full background charge \(Q=n_+-n_-\);
  generic chirality-breaking remainders may lift the projected block zero.
  The follow-on
  instanton-liquid statement is explicitly conditional: only after the ensemble
  measure, fluctuation determinants, interactions, determinant reweighting, and
  regulator remainders are controlled does a nonzero singular-value density
  \(\rho_{\rm zm}(0)\) imply \(\Sigma_{\rm zm}=\pi\rho_{\rm zm}(0)\) by the
  Banks--Casher kernel.  A dilute Poisson gas is not claimed to prove this
  density.
- A one-instanton boundary exponent datum records the small-\(\rho\)
  behavior of a specified scalar insertion datum \(\mathcal X\) in the form
  \(\rho^{b_0+\beta_{\mathcal X}-5}\).  The local Uhlenbeck-boundary
  integrability threshold is \(b_0+\beta_{\mathcal X}>4\), so asymptotic
  freedom \(b_0>0\) is separated from local integrability of the particular
  instanton integral.
- A higher-charge Uhlenbeck boundary-face integrability datum records the
  residual smooth charge, pointlike ideal-instanton centers, bubbling scales,
  collision distances, and the exponents \(A_\alpha(\mathcal X)\) and
  \(G_\beta(\mathcal X)\) controlling the product density near that face.
  The open stratum with \(\ell\) distinct ideal instantons has codimension
  \(4\ell(N_c-1)\), diagonal collision of the ideal points adds
  \(4(\ell-r)\), and local absolute integrability follows from positivity
  of every displayed face exponent.  The charge-one threshold above is the
  special case \(A_1=b_0+\beta_{\mathcal X}-4\).
- The centered \(k=1\) ADHM quotient is derived directly from
  \(IJ=0\), \(II^\dagger-J^\dagger J=0\): for \(\rho>0\) it is the cone
  over \(U(N_c)/(U(N_c-2)\times U(1))\), has orientation dimension
  \(4N_c-5\), and has radial volume factor
  \(\rho^{4N_c-5}\dd\rho\,\dd\Omega_{N_c}\).  The endpoint \(\rho=0\) is
  identified as the small-instanton boundary where the two-frame collapses.
- The universal one-loop scale and running-coupling dependence of the
  one-instanton density is
  \[
    \frac{\dd^4a\,\dd\rho}{\rho^5}\,\dd\Omega_{N_c}
    \left(\frac{8\pi^2}{g_{\rm ht}^2(\mu)}\right)^{2N_c}
    (\mu\rho)^{b_0}
    \exp[-8\pi^2/g_{\rm ht}^2(\mu)+i\theta],
  \]
  up to the finite determinant/orientation-volume constant and higher-loop
  corrections in the chosen scheme.
- In pure \(SU(N)\) Yang-Mills with the Pauli-Villars convention and
  orientation orbit integrated in the corresponding Haar normalization, that
  finite one-loop constant is
  \[
    C_N^{\rm PV}
    =
    {2^{2-2N}\over \pi^2 (N-1)!(N-2)!}
    \exp[-\alpha(1)-2(N-2)\alpha(1/2)],
  \]
  with \(\alpha(1)=0.443307\ldots\) and
  \(\alpha(1/2)=0.145873\ldots\).  Equivalently,
  \(C_N^{\rm PV}=0.466\exp[-1.679N]/[(N-1)!(N-2)!]\) to the displayed
  precision, giving \(C_3^{\rm PV}\simeq1.51\times10^{-3}\).  This is a
  pure-gauge scheme constant; light-fermion amplitudes still require their own
  mass/source determinant normalization.
- The logarithmic \((\mu\rho)^{b_0}\) factor is traced to the
  background-field heat-kernel coefficient of the nonzero-mode fluctuation
  complex:
  \((11/3)C_2(G)\) from the vector-plus-ghost sector and
  \(-(4/3)\sum_{\rm Dirac}T(R)\) from Dirac matter.  For vectorlike QCD this
  gives \(b_0=(11/3)N_c-(2/3)N_f\), and the cutoff expression
  \(e^{-X_\Lambda}(\Lambda\rho)^{b_0}\) becomes
  \(e^{-X_\mu}(\mu\rho)^{b_0}\) at one-loop logarithmic accuracy.
- The Dirac index gives \(2T_Rk\) chiral zero modes for a Weyl fermion in
  representation \(R\) in common half-trace notation.  For a fundamental Weyl
  fermion of \(SU(N_c)\) at \(k=1\), this is one zero mode.
- The 't Hooft vertex follows from Berezin integration over fermion zero-mode
  coefficients: QCD receives the chiral flavor determinant
  \(\det_{f f'}(\rho^3\bar\psi_{Rf}\psi_{Lf'})\) with
  \(\Delta Q_A=2N_f\), while electroweak \(SU(2)_L\) receives
  \(\prod_r(q_{Lr}q_{Lr}q_{Lr}\ell_{Lr})\) with
  \(\Delta B=\Delta L=N_g\).
- The light-fermion determinant factor is separated into a finite
  nonzero-mode spectral factor
  \(\mathcal R_{{\rm f},\Lambda}^{\mathcal S}(z;\mu)\) and a zero-mode
  Schur/Berezin determinant.  In the leading local source approximation this
  zero-mode determinant is \(\det(M^0+B^0)\), with
  \(M^0_{ff'}=\rho M_{ff'}(\mu)\) and
  \(B^0_{ff'}=\rho^3\bar\psi_{Rf}\psi_{Lf'}+\cdots\).  Thus
  \(\prod_f(m_f\rho)\) is the mass-saturated zero-mode factor, not the finite
  nonzero-mode determinant constant; the latter is a separate fluctuation
  calculation in the chosen scheme.
- The renormalized mass/source instanton vertex is now stated as a source
  functional:
  \[
    \mathcal V_{\rm inst}^0
    =
    \mathcal R_{\rm f}^{\mathcal S}(\mu)
    \det(M^0+J^0).
  \]
  With \(\mu\,dM/d\mu=-\gamma_m M\) and
  \(\mu\,dJ/d\mu=-\gamma_m J\) in source-coordinate notation and
  \((\mu\partial_\mu+\beta\partial_g)\log\mathcal R_{\rm f}^{\mathcal S}
  =N_f\gamma_m\), the full source functional is RG covariant.  The vacuum
  product \(\mathcal R_{\rm f}^{\mathcal S}\prod_f m_f\) is therefore
  invariant at this anomalous-dimension layer, while \(r\)-fold source
  derivatives carry the Callan--Symanzik covariance of \(r\) scalar-density
  insertions.
- The one-instanton source amplitude now has an explicit assembly/error
  ledger:
  \[
    \mathcal A_{\Lambda,Q=1}^{\mathcal J}
    =
    \mathcal A_{\rm lead}^{\mathcal J}
    +R_{\rm det}+R_{\rm zm}+R_{\rm src}+R_{\rm Schur}+R_{\rm end}.
  \]
  The leading density contains the pure-gauge collective/determinant density
  \(\mathcal C_{\rm pg}^{\mathcal S}\), which specializes to the
  orientation-integrated \(C_{N_c}^{\rm PV}\) convention when that orbit has
  already been integrated, together with the light-fermion nonzero-mode factor
  \(\mathcal R_{\rm f}^{\mathcal S}\), the universal running factor, and the
  selected zero-mode source coefficient.  The residuals separately track
  finite determinant remainders, zero-mode/source truncation, color-singlet or
  hadronic matching, nonzero-mode Schur corrections, and endpoint tails.  This
  makes precise that the collective-coordinate measure is only one input to the
  QFT amplitude.
- The hard four-fermion instanton coefficient is now specialized to
  \(SU(3)\), \(N_f=2\) in the Pauli-Villars pure-gauge convention:
  \(b_0=29/3\), the collective prefactor is
  \((8\pi^2/g^2)^6\), the RG-invariant hard falloff is
  \(\Lambda_{\rm ht}^{29/3}Q^{-35/3}\), and the individual-slot endpoint tail
  is
  \(3\cdot6^4(\prod_\ell c_\ell^{-3})R^{-1/3}+O(R^{-7/3})\).  The text keeps
  the light-fermion determinant factor, shared orientation projector, and five
  residuals explicit, so this is a declared hard-source coefficient rather than
  a claim of a complete hadronic amplitude.
- The hard-size endpoint diagnostic now includes the log-shell density
  \(s^{b_0+2}|\mathcal F_{\rm hard}(s)|\).  For the \(SU(3)\), \(N_f=2\)
  differentiated four-slot kernel the shell/tail exponent is only
  \(\Delta=1/3\); the normalized power-tail majorant \(3R^{-1/3}\) falls
  below \(0.1\) only after \(R>27000\).  This is recorded as a physics
  endpoint-control warning, not as a new moduli-space fact.

## Open Boundaries

- Pure gravitational anomalies in dimensions \(4k+2\) are not developed here.
  This chapter includes only the mixed gauge-gravitational four-dimensional
  anomaly polynomial needed for chiral fermions with \(U(1)\) charges.
- Global anomalies are deferred to the next chapter.
- The Wess--Zumino--Witten functional is introduced in the next chapter, after
  chiral symmetry breaking and pion effective fields have been set up.

## Figure Requirements

- Two-dimensional axial-vector current loop with momentum labels.
- Conserved-current contour deformation and anomalous axial contour
  deformation.
- Four-dimensional one-axial, two-vector triangle pair with both orientations.
- BPST instanton data figure linking the explicit connection, self-dual
  curvature, action saturation, bosonic zero modes, and fermion-zero-mode
  saturation of the semiclassical vertex.

## Audit Notes

- On 2026-05-22 the source block corresponding to handwritten pp. 211--225 was
  expanded to include the two-dimensional contact-term calculation,
  contour-charge interpretation, and four-dimensional triangle contact-term
  derivation before the measure/index and descent sections.
- 2026-05-24 issue #250 pass: made the Bardeen--Zumino current explicit in
  components, including both the curvature form and the derivative-expanded
  nonabelian polynomial with ordering fixed.
- 2026-05-24 issue #251 pass: replaced the informal integrated-index sentence
  by the closed spin Dirac Atiyah--Singer theorem with hypotheses, the
  flat-gauge specialization used in the anomaly calculation, and the
  Atiyah--Patodi--Singer boundary formula with eta-invariant correction.
- 2026-05-24 issue #252 pass: inserted the local anomaly-inflow section,
  including the Chern--Simons bulk response, the bulk-boundary cancellation
  identity, the Callan--Harvey domain-wall interpretation, and the transition
  from local descent to finite invertible anomaly theories.
- 2026-05-24 issue #253 pass: expanded the descent discussion into an explicit
  \((s,d)\) bicomplex, proved the local-functional relation between
  Wess--Zumino consistency and \(H^{1,4}(s\mid d)\), and derived the first two
  descent equations from \(sI_6=0\) and the algebraic Poincare lemma.
- 2026-05-24 issue #254 pass: inserted the missing integrability derivation of
  Wess--Zumino consistency from the gauge-algebra commutator acting on the
  effective action, including the closure calculation on the background
  connection and the differentiability/regulator qualification.
- 2026-05-24 issue #306 pass: rewrote the Fujikawa measure derivation as a
  finite-dimensional Berezinian change-of-variables calculation tied to
  Volume I's fermionic path-integral framework; classified the heat kernel as
  a gauge-covariant spectral regulator for the Berezinian trace and added a
  harness check against the old untyped "measure changes by a Jacobian"
  phrasing.
- 2026-05-24 issue #314 pass: cross-referenced the regulator catalog and
  stated explicitly that the anomaly computation uses dimensional reduction
  and heat-kernel/spectral trace regulation, not Pauli--Villars auxiliary
  fields.
- 2026-05-25 issue #465 pass: added the explicit BPST instanton construction,
  action saturation with the half-trace/trace-delta coupling comparison,
  bosonic and fermionic zero-mode counts, the QCD and electroweak 't Hooft
  vertices, and a BPST normalization calculation-check script.
- 2026-05-29 issue #597 pass: derived the universal one-loop
  one-instanton density factors that had previously been compressed into
  \(C_{N_c,N_f}(\rho,\mu)\): the scale-invariant
  \(\dd^4a\,\dd\rho/\rho^5\) center-size measure, the \(4N_c\) zero-mode
  coupling power, and the RG determination of \((\mu\rho)^{b_0}\).
- 2026-05-29 issue #597 ADHM pass: added the finite-dimensional \(k=1\)
  ADHM quotient derivation, orientation orbit, cone-volume power, and
  small-instanton boundary statement, with the BPST check script extended to
  verify the dimension and radial-power arithmetic.
- 2026-05-27 issue #630 theta pass: added the finite-regulator topological
  susceptibility datum and finite-volume cumulant proof, paired with
  `calculation-checks/qcd_theta_witten_veneziano_checks.py`.
- 2026-05-27 follow-up: added the theta-branch and cluster-decomposition
  datum, including thermodynamic branch selection and the exact covariance
  obstruction for mixed branch states.
- 2026-06-03 issue #630 local-density pass: derived the finite-regulator
  density-correlator form of the topological susceptibility, including the
  periodic zero-momentum reduction and the contact-term/\(\theta\)-counterterm
  convention.  The paired theta/Witten--Veneziano check script now verifies
  the charge-variance/density-double-cumulant equality and contact shift
  exactly.
- 2026-06-04 issue #630 theta-cumulant hierarchy pass: extended the
  finite-regulator theta ledger from the susceptibility to all charge
  cumulants, with explicit \(b_2,b_4\) signs, branchwise differentiability
  caveat, and local theta-counterterm derivative shifts.  The paired
  theta/Witten--Veneziano check script verifies the hierarchy from a concrete
  CP-symmetric charge distribution.
- 2026-05-30 issue #696 dequote pass: converted the cubic gauge obstruction
  from a `quotedtheorem` to a local proposition with proof from the
  perturbative BRST bicomplex, descent of
  \(\operatorname{tr}_R(\mathsf F^3)\), local counterterm coboundaries, and
  the relative cohomology classification of the cubic gauge-anomaly class.
- 2026-06-01 issue #696 Chern--Weil descent-coefficient pass: inserted the
  homotopy calculation for the Chern--Simons five-form coefficients
  \(1,\frac32,\frac35\) and the \(n=2\) consistent-descent coefficients
  \(1,\frac12\); extended
  `calculation-checks/anomaly_polynomial_descent_checks.py` to verify the
  latter rational integrals exactly.
- 2026-06-01 issue #696 Cartan-restriction pass: strengthened the cubic
  gauge-obstruction proof by restricting a nonzero invariant cubic tensor to
  a Cartan subalgebra, deriving directly that Abelianized cubic local
  counterterms cannot change the fully symmetric Cartan coefficient, and
  leaving the full local BRST classification only for the converse
  cohomology statement that no semisimple cubic class remains after the
  invariant-polynomial coefficient vanishes.
- 2026-06-01 issue #696 Bardeen--Zumino calibration pass: added the
  Abelianized factor-three check for the distinction between the consistent
  descent representative and the covariant current representative, and paired
  it with an exact rational calculation check.
- 2026-06-01 issue #701 warning-scope pass: added a convention warning at the
  start of the anomaly chapter tying anomaly signs and factors to the entire
  datum \((\bar\psi,\gamma_5,\epsilon^{0123},D_\mu,F_{\mu\nu},\operatorname{tr})\),
  the topological-charge normalization, and the chosen local counterterm
  representative.  The warning also reiterates that dimensional reduction is
  used only as a perturbative regulator for the Ward-identity representative,
  not as a nonperturbative fermionic path-integral definition.
- 2026-06-02 issue #696 finite-regulator scheme pass: inserted the
  background-groupoid cochain interpretation of the local anomaly class after
  Proposition~\ref{prop:local-anomalies-relative-brst-classes}.  The chapter
  now derives the finite cocycle identity
  \(C_\Lambda(gh;A)=C_\Lambda(h;A^g)+C_\Lambda(g;A)\), identifies local
  counterterm or determinant-frame changes with the coboundary
  \(B_\Lambda[A^g]-B_\Lambda[A]\), and states explicitly that regulator and
  subtraction choices within one local background-field scheme move the
  representative but not the relative class.  The companion
  `calculation-checks/inflow_anomaly_line_checks.py` now verifies this
  coboundary arithmetic exactly.
- 2026-06-03 issue #696 anomaly-coordinate architecture pass: added an early
  proposition comparing finite-regulator cochains, local BRST descent,
  anomaly-line transport, inverse inflow coordinates, and global holonomy.
  The companion `calculation-checks/inflow_anomaly_line_checks.py` now also
  checks a finite model where the local/descent subgroup is trivial but a flat
  large-transformation holonomy remains nontrivial.
- 2026-06-03 issue #597 physics-amplitude pass: inserted the physical
  correlator assembly proposition after the instanton density/determinant
  setup.  The pass states the finite-regulator collective-coordinate integral,
  separates the nonzero-mode determinant from the zero-mode Berezin
  coefficient, and records that moduli-space geometry is only the integration
  domain; physical amplitudes require insertion/mass/source saturation and
  boundary-face integrability.  The BPST check script now verifies unsaturated
  zero-mode vanishing, mass/source lifting, and the two-flavor 't Hooft
  determinant sign.
- 2026-06-03 issue #597 QCD vertex pass: promoted the local 't Hooft vertex
  from a displayed determinant to a proved finite Berezin determinant of the
  flavor source matrix.  The pass identifies the \(2N_f\)-fermion operator,
  the mass-saturated phase \(\theta+\arg\det M\), and the \(U(1)_A\) selection
  rule as the same instanton zero-mode calculation.  The BPST check script now
  verifies the three-flavor determinant, the mixed mass/source minor
  expansion, and the strong-CP phase ledger.
- 2026-06-03 issue #597 fluctuation-amplitude pass: added the proper-time
  representative of the instanton nonzero-mode determinant and the
  finite-regulator \(N_f=2\) smeared four-fermion amplitude.  The pass makes
  the 't Hooft amplitude calculation depend on the regulated fluctuation
  spectrum, local counterterms, zero-mode source projection, and the final
  collective-coordinate integral, with the local vertex appearing as the
  slow-field limit.  The BPST check script now verifies exact determinant
  powers, zero-mode removal, and the source-determinant multiplication for a
  finite toy four-fermion amplitude.
- 2026-06-03 issue #597 zero-mode-tail pass: added the normalized BPST
  zero-mode radial envelope, the momentum-space form factor \(zK_1(z)\), and
  the local-vertex moment calculation.  The result exposes both the
  \(q^2\rho^2\log(q\rho)\) small-momentum correction and the \(R^{-2}\) tail /
  logarithmic second-moment sensitivity in position space, tying derivative
  corrections to the physical wave-packet or IR regulator.  The BPST check
  script verifies the cumulative mass, tail expansion, form-factor ODE
  coefficient, large-\(z\) coefficient, determinant insertion of form factors,
  second-moment derivative, and rotational tensor trace.
- 2026-06-03 issue #597 dilute-gas physics pass: added the conditional
  instanton/anti-instanton Poisson sum from the regulated one-instanton
  amplitude to theta-dependent vacuum energy and cumulants.  The BPST check
  script now verifies the Skellam cumulant ledger, \(\chi_{\rm top}=2\zeta\),
  \(b_2=-1/12\), and the vanishing of the vacuum activity when a massless
  flavor leaves zero modes unsaturated.
- 2026-06-03 issue #597 mass-saturation size-integral pass: added the
  finite-window mass-saturated QCD instanton vacuum activity, deriving the
  \(\prod_f(m_f\rho)\) zero-mode factor, the
  \(\theta+\arg\det M\) phase, the \(b_0+N_f>4\) small-\(\rho\) criterion,
  and the large-\(\rho\) obstruction to a zero-temperature dilute activity.
  The BPST check script now verifies the finite-window integral and endpoint
  classifications exactly.
- 2026-06-03 issue #597 external-amputation pass: added
  `prop:instanton-external-leg-amputation-kernel`, which separates the
  unamputated zero-mode source matrix from the source-amputated hard kernel.
  The pass proves that external row/column pole-residue factors cancel under
  amputation but the BPST form factor, orientation tensor, nonzero-mode
  determinant, and collective-coordinate integral remain.  The BPST check
  script now verifies this determinant row/column arithmetic and a finite
  two-cell collective-coordinate integral.
- 2026-06-03 issue #597 fluctuation-log pass: added
  `prop:instanton-heat-kernel-beta0-logarithm`, which identifies the
  \((\mu\rho)^{b_0}\) factor with the background-field heat-kernel logarithm
  of the nonzero-mode fluctuation complex and the one-loop coupling-scale
  trade.  The BPST check script now verifies the vector-plus-ghost
  \(11C_A/3\) coefficient, the Dirac matter subtraction, charge-\(k\)
  scaling, and the cancellation of cutoff-scale dependence.
- 2026-06-03 issue #597 hard-size pass: added
  `ca:hard-momentum-instanton-size-window`, which shows how hard external
  zero-mode form factors make the \(N_f=2\) four-fermion size integral
  scale as a \(Q^{-2}\) coefficient, while distinguishing this hard correlator
  from the infrared-sensitive mass-saturated vacuum activity.  After the
  individual-slot repair below, the large-\(\rho\) endpoint is read as either
  exponential fused-density suppression or the individual-slot power test.
  The BPST check script verifies the small-\(\rho\) margin, \(Q\)-power ledger,
  endpoint classification, and absence of such a cutoff in the vacuum term.
- 2026-06-03 issue #597 hard-RG scaling pass: extended the same hard-size
  window by separating the \(\mu=Q\) engineering \(Q^{-2}\) ledger from the
  RG-invariant one-loop asymptotic form
  \(\Lambda_{\rm ht}^{b_0}Q^{-b_0-2}\mathcal J_{b_0}\).  The BPST check script
  now verifies the additional running-exponential \(Q^{-b_0}\), the
  \(\Lambda_{\rm ht}^{b_0}\) mass dimension, and the resulting net
  four-fermion coefficient dimension.
- 2026-06-03 issue #597/#630 Wilsonian-size split pass: added
  `ca:instanton-wilsonian-size-factorization`, which writes the finite
  instanton size integral as a short coefficient plus a long-distance
  remainder at \(\rho_I=\mu_I^{-1}\).  The new block derives the exact
  boundary-flow cancellation
  \(\partial_{\log\mu_I}\mathcal A^<=-\rho_IK(\rho_I)\),
  \(\partial_{\log\mu_I}\mathcal A^>=+\rho_IK(\rho_I)\), making clear that
  the local 't Hooft vertex is a Wilsonian coefficient unless the long-size
  remainder is matched or bounded.  The BPST check script verifies the
  boundary-flux cancellation and finite shell-transfer arithmetic.
- 2026-06-03 issue #597/#630 short-instanton OPE pass: added
  `ca:short-instanton-ope-coefficient`, which projects the short-size
  instanton contribution onto the retained renormalized local operator basis
  before calling it a local 't Hooft vertex.  The block records the coefficient
  RG equation dual to
  \(\partial_{\log\mu}[O_I]_\mu=-\gamma_{IK}[O_K]_\mu\), the inverse finite
  operator-frame transformation, and the separate
  \(\mu_I\)-boundary flux
  \(-\rho_IK_I^{\rm OPE}(\rho_I)\).  The companion BPST check verifies the
  finite coefficient/operator pairing, transformed connection law, and
  distinction between operator RG and size-factorization flow.
- 2026-06-03 issue #597 color-singlet matching pass: added
  `ca:instanton-color-singlet-hadronic-matching`, which places the auxiliary
  source-amputated instanton kernel inside gauge-invariant source correlators
  and stable-hadron residue extraction.  The new block distinguishes the BPST
  hard kernel from source-to-zero-mode overlaps, long-distance hadronic matrix
  elements, and pole residues.  The BPST check script now verifies the
  source-projection determinant identity, the need to keep
  collective-coordinate-dependent overlaps inside the instanton integral, and
  the separate finite pole-residue division for a stable hadron.
- 2026-06-03 issue #597/#630 plane-wave amplitude-assembly pass: inserted
  `prop:instanton-plane-wave-four-fermion-assembly`, which factors the common
  instanton-center phase from the \(N_f=2\) source coefficient, producing total
  momentum conservation and leaving the selected zero-mode form factors inside
  the size integral.  Extended
  `bpst_instanton_normalization_checks.py` to verify the center-phase
  permutation identities, coefficient after phase factoring, \(\rho^6\)
  zero-mode source power, and finite-volume momentum-selection rule.
- 2026-06-03 issue #597/#724 orientation-projection repair: inserted and then
  corrected
  `prop:instanton-color-orientation-haar-projection`, which shows that the
  embedded \(SU(2)\) instanton orientation is an amplitude projection rather
  than an inert moduli-space volume.  The chapter derives the Haar identities
  sending two colored zero-mode slots to
  \(\frac12\varepsilon_{ij}\det(v_A,v_B)\) and replaces the earlier incorrect
  factorized four-slot shortcut by the genuine shared Haar projector with
  \(G^{-1}=\begin{psmallmatrix}1/3&-1/6\\-1/6&1/3\end{psmallmatrix}\).
  Extended `bpst_instanton_normalization_checks.py` to verify one-slot
  vanishing, mixed-trace normalization, epsilon projection, the explicit
  \(1/3\) counterexample to the factorized \(1/4\) shortcut, the
  source-contracted shared projector, and the fact that a rank-one right pair
  need not vanish before the remaining source/color contractions are imposed.
- 2026-06-03 issue #712 source-typing repair: revised the four-fermion
  instanton chain so ordinary c-number external wave packets are not treated as
  a nonzero determinant of a rank-one matrix.  The chapter now separates
  independent even bilinear source matrices from differentiated linear
  Grassmann sources, derives the four-slot coefficient as
  \(\det R\,\det L\), and reserves \(zK_1(z)\) for the fused bilinear density
  form factor rather than the individual external-zero-mode form factor.
  Extended `bpst_instanton_normalization_checks.py` to verify the zero
  determinant of the c-number outer product, the nonzero differentiated
  Grassmann-source coefficient, source-slot amputation, and the corrected
  plane-wave center-phase ledger.
- 2026-06-03 issue #597/#712 individual-zero-mode repair: added the standard
  singular-gauge momentum-space zero-mode slot form factor
  \(F_{\rm zm}(t)=-t\partial_t(I_0K_0-I_1K_1)\), \(t=\rho|p|/2\), with
  \(F_{\rm zm}(0)=1\) and \(F_{\rm zm}(t)\sim3/(4t^3)\).  The hard-size window
  now distinguishes the exponential fused-bilinear density \(zK_1(z)\) from the
  power-law individual-fermion slots.  For \(SU(3)\), \(N_f=2\), four hard
  individual slots pass the large-\(\rho\) test only by margin \(1/3\), while a
  soft slot fails.  The companion check verifies the Bessel derivative identity,
  the large-\(t\) cancellation through \(t^{-2}\), and the endpoint power
  inequalities.
- 2026-06-03 issue #597/#712 determinant-constant pass: added the pure-gauge
  Pauli-Villars one-instanton normalization constant
  \(C_N^{\rm PV}\) from the orientation-integrated zero-mode coefficient and
  the finite nonzero-mode determinant
  \(\exp[-\alpha(1)-2(N-2)\alpha(1/2)]\).  The companion check verifies the
  reduction to the rounded \(0.466\exp[-1.679N]\) form and the \(SU(3)\)
  value \(1.51\times10^{-3}\), while leaving the full light-fermion
  't Hooft amplitude normalization as separate work.
- 2026-06-03 issue #597/#630/#712 light-fermion determinant-factor pass:
  inserted the finite block-determinant/Schur-complement statement separating
  the light-fermion nonzero-mode spectral determinant from the zero-mode
  mass/source determinant.  The text now states that \(\prod_f(m_f\rho)\) is
  the mass-saturated zero-mode factor and that
  \(\mathcal R_{{\rm f},\Lambda}^{\mathcal S}\) is an independent
  fluctuation determinant datum requiring the chosen regulator, counterterms,
  and normalization.  The BPST check script verifies the Schur factorization,
  the projected determinant product, and the independence of zero-mode minors
  from the finite nonzero-mode scheme factor.  The 2026-06-04 source-frame
  continuation added the finite covariance law
  \(\mathcal R_{\rm f}'=\mathcal R_{\rm f}/(\det Z_R\det Z_L)\) under
  \(K_{00}^{\rm eff}\mapsto Z_RK_{00}^{\rm eff}Z_L\), together with the
  separate local counterterm multiplier \(\exp[-\Delta C_{\rm f}]\); the
  companion check verifies both the matrix and scalar-frame cases.
- 2026-06-03 issue #597/#630 mass-source RG pass: added the
  source-functional RG transport of the instanton vertex.  The new block
  states the renormalized zero-mode source functional
  \(\mathcal R_{\rm f}^{\mathcal S}\det(M^0+J^0)\), the compensating
  anomalous-dimension equation for \(\mathcal R_{\rm f}^{\mathcal S}\), the
  vacuum invariance of
  \(\mathcal R_{\rm f}^{\mathcal S}\prod_fm_f\), and the distinct
  Callan--Symanzik covariance of source-differentiated correlators.  The BPST
  check script verifies determinant homogeneity, anomalous-dimension
  cancellation, source-derivative covariance weights, and the invariance of
  \(\theta+\arg\det M\) under anomalous chiral rotations.
- 2026-06-03 issue #597/#630 amplitude-architecture pass: inserted
  `prop:instanton-amplitude-assembly-error-budget`, which decomposes the
  finite one-instanton source amplitude into the leading determinant/zero-mode
  density plus determinant, zero-mode/source, source-matching, Schur, and
  endpoint residuals.  The BPST check script verifies the finite-cell residual
  decomposition, the absolute error bound, finite source-convention
  invariance, and the fact that the collective-coordinate measure alone is not
  the amplitude.
- 2026-06-03 issue #597 hard-coefficient specialization pass: added
  `ca:su3-two-flavor-hard-instanton-coefficient`, which packages the
  \(SU(3)\), \(N_f=2\) source-amputated hard coefficient with the PV
  pure-gauge constant, light-fermion determinant factor, orientation projector,
  \(\Lambda_{\rm ht}^{29/3}Q^{-35/3}\) scaling, and the explicit
  \(R^{-1/3}\) individual-slot endpoint tail.  The BPST check script now
  verifies the exponent ledger and tail coefficient exactly.  Remaining #597
  scope still includes fuller light-fermion determinant normalization in a
  declared scheme, multi-instanton/boundary estimates, and the broader
  soliton/monopole/instanton chapter architecture.
- 2026-06-03 issue #597 log-shell endpoint pass: surfaced the hard-size
  endpoint evidence per logarithmic size shell, making explicit that the
  individual-slot \(SU(3)\), \(N_f=2\) hard kernel has only \(R^{-1/3}\)
  shell/tail suppression.  The companion BPST check verifies the shell power,
  three-decade cost for tenfold power-tail suppression, and \(R>27000\)
  normalized-tail threshold.
- 2026-06-04 issue #597 screened-size amplitude pass: added
  `prop:screened-one-instanton-size-integral`, which turns the prior
  large-size warning into an explicit amplitude calculation when a physical
  infrared screening scale is part of the same regulated problem.  The block
  computes the gamma-function size integral, size moments, dominant shell, and
  \(SU(3)\), \(N_f=2\) mass-saturated specialization \(A=23/3\), while stating
  that the formula is controlled only if the screened shell remains in the
  weak-coupling window.  Extended
  `bpst_instanton_normalization_checks.py` to verify the exact power, moment,
  saddle, and mass-dimension bookkeeping.  This is amplitude-side progress,
  not additional moduli-space infrastructure.
- 2026-06-04 issue #597 thermal determinant-screening pass: added
  `ca:thermal-instanton-determinant-screening`, which specializes the generic
  Gaussian screening scale to the high-temperature QCD determinant coefficient
  \(m_T^2=\pi^2T^2(2N_c+N_f)/3\), records its Debye-susceptibility convention
  conversion, and adds a residual-window bound
  \(|\mathcal A_T-\mathcal A_T^G|\le(e^{\varepsilon_T}-1)\mathcal A_T^G\).
  The companion BPST check verifies the \(SU(3)\), \(N_f=2\) shell
  \(\pi^2T^2\rho_{\rm shell}^2=23/16\), the half-trace/trace-delta conversion,
  the \(T^{-23/3}\) scaling, and the finite residual ledger.  This is a
  physical fluctuation-determinant bridge, not a moduli-space addition.
- 2026-06-04 issue #597/#630 thermal theta-observable pass: added
  `ca:thermal-dilute-instanton-susceptibility`, carrying the screened thermal
  activity into the dilute topological susceptibility and fourth theta
  curvature.  The block derives \(\chi_{\rm top}^{T,{\rm dig}}=2\zeta_T\),
  \(b_2=-1/12\), the inherited residual bound, and the \(SU(3)\), \(N_f=2\)
  mass-saturated scaling
  \(|m_um_d|\Lambda_{\rm ht}^{29/3}T^{-23/3}\).  The BPST companion check now
  verifies the dimension, temperature power, Poisson curvature, and residual
  propagation.  This converts the instanton-size work into a theta-curvature
  observable while preserving the near-crossover and zero-temperature scope
  boundary.
