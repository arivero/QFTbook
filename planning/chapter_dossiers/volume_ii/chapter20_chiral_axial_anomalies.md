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
  bookkeeping.  The 2026-06-03 Uhlenbeck-face continuation adds the
  higher-charge boundary-face codimension and product integrability budget.
  The physics-amplitude continuation adds the finite Berezin zero-mode
  saturation check that turns the instanton measure into a correlator
  contribution, including the two-flavor 't Hooft determinant sign.  The
  fluctuation-amplitude continuation adds the proper-time nonzero-mode
  determinant assembly and its multiplication by the zero-mode-projected
  four-fermion source determinant.  The zero-mode-tail continuation adds the
  BPST fundamental zero-mode envelope, its momentum form factor \(zK_1(z)\),
  its \(R^{-2}\) tail, and the logarithmically infrared-sensitive second
  moment controlling the first nonzero derivative correction to the local
  vertex.
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
| \(\mathcal Z_{\mathcal O,\Lambda}^{0}(z)\) | finite Berezin coefficient of the zero-mode part of insertions, masses, and sources in a \(Q=1\) instanton background |
| \(M_{ff'},B_{ff'}\) | mass-overlap and external-source matrices whose finite Berezin determinant and minor expansion give the QCD 't Hooft amplitudes |
| \(B_{\eta,ff'}(z)\) | zero-mode-projected source matrix for smeared four-fermion wave packets in the instanton background |
| \(G^{(4)}_{\eta,\Lambda,Q=1}\) | finite-regulator one-instanton contribution to the smeared four-fermion amplitude |
| \(h_\rho(y),\widehat h_\rho(q),M_2(R)\) | normalized BPST zero-mode radial envelope, momentum form factor \(zK_1(z)\), and truncated second moment in the local-vertex expansion |
| \(\zeta_\Lambda\), \(n_\pm\), \(E_{\rm dig}\), \(b_2^{\rm dig}\) | dilute instanton/anti-instanton activity, occupation numbers, conditional dilute-gas vacuum energy, and fourth-order theta-curvature coefficient |
| \(\zeta_m^{[\rho_-,\rho_+]}\) | mass-saturated one-instanton vacuum activity in a finite size window |
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
  collective-coordinate integral of the proper-time nonzero-mode determinant
  times the determinant of the zero-mode-projected source matrix
  \(B_{\eta,ff'}(z)\).  The familiar local 't Hooft vertex is its slow-field
  limit.
- The BPST fundamental zero-mode line has normalized radial envelope
  \(h_\rho(y)=2\rho^2/[\pi^2(y^2+\rho^2)^3]\).  Its zeroth moment is finite
  and its momentum-space form factor is \(zK_1(z)\), \(z=\rho|q|\).  The
  mass outside \(|y|<R\) is
  \((1+2(R/\rho)^2)/(1+(R/\rho)^2)^2\), while its truncated second moment
  grows like \(4\rho^2\log(R/\rho)\).  Thus the local 't Hooft vertex is the
  zeroth adiabatic term; derivative corrections require the external
  wave-packet or infrared cutoff data, equivalently the small-\(q\rho\)
  expansion contains \(q^2\rho^2\log(q\rho)\).
- The source-amputated instanton four-fermion kernel is obtained by removing
  only the adjacent external pole-residue factors from the zero-mode source
  matrix.  Row and column residue factors multiply the flavor determinant and
  cancel under amputation, while the BPST form factor \(zK_1(z)\), the
  spin-color orientation tensor, the nonzero-mode determinant, and the
  collective-coordinate integral remain part of the hard instanton kernel.
  Because colored quarks are not physical asymptotic states in confining QCD,
  this is a source-amputated/partonic coordinate, not a gauge-invariant quark
  \(S\)-matrix element.
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
- The dilute instanton gas is now stated only as a controlled amplitude
  expansion after the regulated one-instanton calculation has supplied a
  finite activity \(\zeta_\Lambda\).  Under Poisson factorization it gives
  \(E_{\rm dig}(\bar\theta)-E_{\rm dig}(0)=2\zeta_\Lambda(1-\cos\bar\theta)\),
  \(\chi_{\rm top}^{\rm dig}=2\zeta_\Lambda\), even Skellam cumulants
  \(\kappa_{2m}=2V_4\zeta_\Lambda\), and \(b_2^{\rm dig}=-1/12\).  The chapter
  explicitly states the failure modes: unsaturated massless zero modes,
  infrared-divergent size integrals, uncontrolled small-instanton boundaries,
  and non-negligible instanton interactions.
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
