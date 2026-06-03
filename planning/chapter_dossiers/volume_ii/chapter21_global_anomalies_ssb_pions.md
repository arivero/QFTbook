# Volume II, Global Anomalies, Spontaneous Symmetry Breaking, And Pions Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`.
- Follows the local anomaly chapter.
- Role in the monograph: pass from local anomaly cocycles to finite
  background anomalies, state anomaly matching as equality of cocycle classes,
  derive the Goldstone pole from a Ward identity and spectral support, derive
  the soft-pion Ward identity and Adler zero, and construct the leading pion
  effective action and Wess--Zumino--Witten term.

## Source And Reference Controls

- `SRC-QFT-PDF`: second-sequence handwritten material on global anomalies,
  spontaneous symmetry breaking, pions, the Wess--Zumino--Witten term, and
  chiral perturbation theory; in the page register this is 253b pages
  226--257.
- `SRC-QFT-RENDERED`: handwritten pages
  `/tmp/qft253b_ssb_pions_src-226.png` through
  `/tmp/qft253b_ssb_pions_src-257.png`, checked against compiled pages
  `/tmp/qft_ch47_ssb_pions_final-337.png` through
  `/tmp/qft_ch47_ssb_pions_final-351.png` in the 2026-05-22 audit.
- `SRC-STUDENT`: Ben Lou transcription around Goldstone theorem, chiral
  symmetry breaking, and the WZW term; used only as a comparison aid.
- `SRC-EXTERNAL`:
  `references/sound_references/bilal_lectures_on_anomalies_0802.0634.pdf`
  and sidecar for descent, finite anomaly discussion, and index language.
- `SRC-EXTERNAL`:
  `references/sound_references/witten_fermion_path_integrals_topological_phases_1508.04715.pdf`
  and sidecar, especially Sections 2.1.2, 2.2.1, 3.2, and 4.2, for
  determinant/Pfaffian lines, mapping tori, global anomalies, eta invariants,
  mod-two indices, APS boundary conditions, and the Dai--Freed theorem.
- `SRC-EXTERNAL`:
  `references/sound_references/leutwyler_foundations_chiral_perturbation_hep-ph_9311274.pdf`
  and sidecar, especially Sections 2, 4, 7, 9, and 10, for current
  generating functionals, external fields, Ward identities, Goldstone
  effective Lagrangians, anomalies, and spurions.

## Framework

- Lorentzian local QFT in a chosen phase, with Euclidean compact-manifold
  formulations used for finite anomaly and index statements.
- Background gauge fields are fixed external data; they are not summed over in
  the global-symmetry generating functional.
- Anomalies are equivalence classes of finite background-gauge cocycles modulo
  local counterterms.
- Goldstone claims use locality, current conservation, an order parameter,
  Lorentz invariance, the spectrum condition, and uniqueness of the vacuum in
  the chosen phase.
- Chiral effective theory is a derivative expansion for current generating
  functionals at momenta below the chiral-symmetry-breaking scale.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(G_{\mathrm f}\) | internal global symmetry group |
| \(B\) | fixed background \(G_{\mathrm f}\)-connection |
| \(\mathcal B\) | space of allowed background fields |
| \(\mathcal G_{\mathrm f}\) | background gauge transformation group |
| \(\mathcal A_g[B]\) | finite anomaly cocycle representative |
| \(C[B]\) | local background counterterm |
| \(\sigma_M,\sigma_g,\sigma_Y\) | chosen spin structures on the four-manifold, mapping torus, and five-dimensional inflow manifold |
| \(X_g\) | mapping torus associated to a gauge transformation \(g\) |
| \(Y,B_Y\) | closed or filling five-manifold and its extended background field |
| \(\mathcal I_5[Y,\sigma_Y,B_Y]\) | five-dimensional invertible anomaly-theory phase on structured backgrounds |
| \(B_g\) | induced background field on the mapping torus \(X_g\) |
| \(\zeta(X_g,\sigma_g,E_g)\) | mod-two index of the coupled real Dirac operator on the spin mapping torus |
| \(\operatorname{Hol}_{\mathrm{DF}}\) | Dai--Freed holonomy of the determinant/Pfaffian line |
| \(G,H\) | symmetry group and unbroken subgroup in a phase |
| \(\xi(\pi)\) | coset representative for Goldstone coordinates |
| \(e^a,\omega^i\) | broken vielbein and unbroken connection in the Maurer--Cartan form |
| \(F_{Aa}\) | Goldstone decay-constant matrix |
| \(m_A=gv\) | Abelian Higgs vector mass used in the Goldstone-versus-gauge-direction caveat |
| \(\Sigma_{IJ}\), \(\Sigma_0\) | QCD chiral condensate matrix and its flavor-singlet value, used as a conjectural dynamical input for the pion EFT |
| \(U(x)\) | pion field valued in \(SU(N_f)\) |
| \(\widehat U(x)\) | local \(U(N_f)\) chiral field used for the singlet large-\(N_c\) theta datum |
| \(T^0,\eta_0\) | normalized flavor-singlet generator \(\mathbf 1/\sqrt{2N_f}\) and the corresponding pseudoscalar field |
| \(\chi_{\rm YM}\) | pure Yang--Mills topological susceptibility entering the large-\(N_c\) Witten--Veneziano matching datum |
| \(\ell_\mu,r_\mu\) | external left and right flavor gauge fields |
| \(F_{\rm st}\) | stereographic-coordinate pion normalization used for the explicit \(N_f=2\) scattering calculation |
| \(\vec D_\mu=\partial_\mu\vec\xi/(1+\vec\xi^{\,2})\) | covariant stereographic building block for the \(N_f=2\) four-derivative invariants |
| \(\Pi^a\) | local pion interpolating field used in the soft-pion Ward identity |
| \(Z_\pi\) | one-pion pole residue of \(\Pi^a\) |
| \(\mathcal L_{\{p_j\}}\) | hard external-pion LSZ operation in the soft-pion theorem |
| \(\mathcal C_a(q;\{p_j,a_j\})\) | LSZ-reduced contact-term sum generated by the axial Ward identity |
| \(A(s,t,u)\) | invariant scalar function in the \(SU(2)_V\) pion scattering amplitude |
| \(C_4(\mu),C'_4(\mu)\) | local four-derivative low-energy constants in the \(N_f=2\) pion EFT |
| \(\Phi^I{}_{J}=\bar q_L^I q_{R,J}\) | microscopic chiral order-parameter field used to match the two-flavor mass deformation |
| \(M,\chi,B_0\) | quark mass spurion, chiral spurion, and low-energy constant |
| \(F^L_{\mu\nu},F^R_{\mu\nu}\) | left and right external flavor field strengths in the chiral generating functional |
| \(L_1,\ldots,L_{10}\) | Gasser--Leutwyler three-flavor even-parity \(O(p^4)\) low-energy constants |
| \(H_1,H_2\) | source-contact \(O(p^4)\) constants in the Gasser--Leutwyler functional |
| \(\Gamma_i\) | one-loop divergence/running coefficients of the \(L_i^r(\mu)\) |
| \(l_3^r(\mu)\) | two-flavor NLO low-energy constant governing the local contribution to \(M_\pi^2\) |
| \(Q\) | electromagnetic flavor-charge matrix embedded as a vector flavor background |
| \(\Gamma_{\mathrm{WZ}}\) | ungauged Wess--Zumino functional |
| \(\Gamma_{\mathrm{WZW}}\) | gauged Wess--Zumino--Witten functional |
| \(n\) | integer WZW level; QCD anomaly matching forces \(n=N_c\) |
| \(\dd\nu_{m,\Lambda}(A)\) | finite-regulator Euclidean vectorlike gauge-field measure with positive quark mass \(m\), used only under the Vafa--Witten positivity hypotheses |
| \(\dd\nu_m(A)\) | continuum limiting functional or measure for the same vectorlike theory, assumed only when a continuum Vafa--Witten conclusion is claimed |

## Claims Established

- A global anomaly is represented by a finite background-gauge cocycle modulo
  local counterterm shifts.
- Infinitesimal local anomalies are differentials of this cocycle on the
  identity component; finite anomalies may remain after the local density
  vanishes.
- The source-level perturbative example with a vector current and two axial
  currents is included: the \(D=4-\epsilon\) evanescent numerator gives the
  contact term proportional to
  \(-\epsilon^{\nu\rho\alpha\beta}\partial_\alpha\delta(x-z)
  \partial_\beta\delta(y-z)/(6\pi^2)\), and the corresponding finite
  background-field variation is \((48\pi^2)^{-1}\int \zeta\,\epsilon FF\).
- A single four-dimensional left-handed \(SU(2)\) fundamental Weyl fermion is
  defined on a spin four-manifold \((M,\sigma_M)\); the spin structure is part
  of the background datum and can affect the Pfaffian line and global anomaly.
- The finite \(SU(2)\) anomaly is presented in the Dai--Freed/APS framework:
  the Pfaffian-line holonomy around a loop of backgrounds is computed on the
  spin mapping torus, and in the pseudoreal fundamental case reduces to
  \[
    \operatorname{Hol}_{\mathrm{DF}}(X_g,\sigma_g,E_g)
    =
    (-1)^{\zeta(X_g,\sigma_g,E_g)}.
  \]
- Finite anomaly inflow is stated through the mapping-torus phase
  \[
    Z[M,\sigma_M,B^g]/Z[M,\sigma_M,B]
    =
    \mathcal I_5[X_g,\sigma_g,B_g],
  \]
  after a local counterterm convention is chosen.
- The \(SU(2)\) global anomaly is identified with the invertible phase
  \[
    \mathcal I_5^{SU(2)}[X_g,\sigma_g,E_g]
    =
    (-1)^{\zeta(X_g,\sigma_g,E_g)}.
  \]
- The SPT/cobordism interpretation is stated with hypotheses: it is a
  framework for invertible, symmetry-protected, short-range-entangled
  responses with specified tangential and background structures, not a
  substitute for defining the QFT determinant or Pfaffian line.
- Anomaly matching is equality of the background anomaly cocycle class between
  UV and IR descriptions.
- Anomaly matching is developed as an infrared constraint: after the symmetry,
  background fields, and counterterm convention are fixed, one computes the UV
  cocycle, writes the possible IR responses from massless fields, Goldstone
  WZW terms, and topological/invertible sectors, and compares cocycle classes.
  A unique trivial gapped symmetric IR phase has zero class and is excluded
  whenever the UV class is nonzero.
- Infinite-volume vacuum sectors are separated from finite-dimensional
  tunneling by the scaling of the instanton action with spatial volume; local
  operators act diagonally on pure homogeneous phases by locality and cluster
  decomposition.
- The Goldstone theorem is derived as a massless spectral contribution forced
  by the Ward identity and a nonzero order parameter.
- The Goldstone theorem is explicitly scoped to global charges acting on a
  positive physical Hilbert space.  For gauged directions, the Abelian Higgs
  quadratic term \((\partial_\mu\pi-m_AA_\mu)^2/2\), \(R_\xi\) gauge fixing,
  and the BRST doublet/quartet structure explain why the would-be Goldstone
  coordinate is absent from the positive BRST cohomology as an independent
  massless particle.
- The explicit \(U(1)\) Goldstone model is developed in polar variables, with
  \(j^\mu=2r^2\partial^\mu\theta\), \([Q,\theta]=i\), a massive radial mode,
  and a pseudo-Goldstone mass from a small \(-\epsilon\operatorname{Re}\phi\)
  deformation.
- The QCD chiral condensate and breaking pattern
  \(SU(N_f)_L\times SU(N_f)_R\to SU(N_f)_V\) are stated as a conjectural
  dynamical property of small-\(N_f\) QCD, not as a theorem derived from the
  continuum Lagrangian or from a completed lattice continuum construction.
- The singlet axial direction is treated through a large-\(N_c\) hypothesis,
  not as an exact finite-\(N_c\) Goldstone coordinate.  Assuming pure
  Yang--Mills has \(\chi_{\rm YM}=O(1)\), the local Yang--Mills theta branch
  has curvature \(\chi_{\rm YM}\), and the chiral field is enlarged locally to
  \(U(N_f)\), the singlet potential
  \[
    \frac12\chi_{\rm YM}
    \left(\theta-\sqrt{2N_f}\eta_0/f_\pi\right)^2
  \]
  gives the chiral-limit Witten--Veneziano mass
  \(m_{\eta_0}^2=2N_f\chi_{\rm YM}/f_\pi^2\).  The text also states why the
  full massless-QCD topological susceptibility vanishes after \(\eta_0\) is
  minimized, so \(\chi_{\rm YM}\) must not be confused with the full-QCD
  susceptibility.
- The leading pion Lagrangian is the invariant two-derivative functional of
  the \(SU(N_f)\)-valued Goldstone field and external flavor backgrounds.
- The non-singlet axial-current Ward identity with one current insertion and
  \(n\) pion interpolating fields is stated as a distributional identity with
  contact terms:
  \[
    \partial_\mu
    \langle T A_a^\mu(x)\Pi^{a_1}(x_1)\cdots\Pi^{a_n}(x_n)\rangle
    =
    -i\sum_j\delta(x-x_j)
    \langle T\Pi^{a_1}\cdots\delta_A^a\Pi^{a_j}\cdots\Pi^{a_n}\rangle .
  \]
- Isolating the current-channel pion pole and applying hard-pion LSZ gives the
  soft-pion theorem
  \[
    f_\pi\mathcal M_{n+1}^{a,a_1,\ldots,a_n}(q,p_1,\ldots,p_n)
    =
    \mathcal C_a(q;\{p_j,a_j\})+O(q).
  \]
  For the chiral coset
  \(SU(N_f)_L\times SU(N_f)_R/SU(N_f)_V\),
  \(\delta_A^a\pi^b=f_\pi\delta^{ab}+O(\pi^2/f_\pi)\) has no linear pion
  term, so the contact term has no one-pion-to-one-pion component after hard
  LSZ.  Therefore purely pionic connected amplitudes obey the Adler zero
  \[
    \mathcal M_{n+1}^{a,a_1,\ldots,a_n}(q,p_1,\ldots,p_n)=O(q).
  \]
- For \(N_f=2\), the stereographic-coordinate expansion of the nonlinear sigma
  model gives the leading pion scattering amplitude
  \(A(s,t,u)=4s/F_{\rm st}^2+O(E^4/F_{\rm st}^4)\), and the next order is the
  sum of one-loop two-derivative graphs and local four-derivative terms with
  low-energy constants \(C_4,C'_4\), including the source logarithms and the
  Wilsonian cutoff running of these two coefficients.
- Quark masses enter the chiral effective action through a spurion with the
  same chiral transformation law as the microscopic mass matrix.
- The two-flavor mass expansion is also matched directly to the microscopic
  order parameter, giving
  \(m_{ab}^2=\delta_{ab}\,4(m_u+m_d)\langle-\bar q q/2\rangle_0/F_{\rm st}^2\)
  in the stereographic normalization, with the observed pion masses recorded
  as a normalization check.
- Chiral perturbation theory is named as the derivative/source/quark-mass
  expansion of the QCD current generating functional, with power counting
  \(D_\mu U,\ell_\mu,r_\mu=O(p)\), \(F_{\mu\nu}^{L,R},\chi=O(p^2)\), and
  graph order
  \(\nu=2+2L+\sum_iV_i(d_i-2)\).
- The chiral power-counting formula is now separated from the approximation
  claim: the graph identity is exact, while truncating at \(O(p^4)\) requires
  a compact low-energy source window and a seminorm remainder estimate.  The
  first omitted families are explicitly recorded as two-loop \(\mathcal L_2\),
  one-loop \(\mathcal L_4\)-with-\(\mathcal L_2\), and tree
  \(\mathcal L_6\) graphs, all of order \(p^6\).
- The three-flavor Gasser--Leutwyler even-parity NLO basis
  \(L_1,\ldots,L_{10}\), together with source-contact \(H_1,H_2\), is displayed
  in the chapter's left/right convention
  \(U\mapsto LUR^{-1}\) and
  \(D_\mu U=\partial_\mu U-i\ell_\mu U+iUr_\mu\).
- The \(L_i^r(\mu)\) are identified as renormalized coordinates for local
  \(O(p^4)\) counterterms, with the displayed \(\Gamma_i\) table governing
  \(\mu\,dL_i^r/d\mu=-\Gamma_i/(16\pi^2)\).
- The two-flavor pion mass chiral logarithm is computed:
  \[
    M_{\pi,\rm phys}^2
    =
    M^2\left[
      1+\frac{M^2}{32\pi^2f^2}\log\frac{M^2}{\mu^2}
      +\frac{2l_3^r(\mu)M^2}{f^2}
    \right]+O(M^6),
  \]
  and the scale dependence of the logarithm is shown to cancel against
  \(\mu\,dl_3^r/d\mu=1/(32\pi^2)\).
- The Wess--Zumino--Witten coefficient is quantized and equals \(N_c\) for QCD
  with fundamental quarks, so the pion functional reproduces the microscopic
  flavor anomaly.
- The same equality is used as a worked 't Hooft anomaly-matching test:
  the UV left-flavor anomaly
  \(N_c(48\pi^2)^{-1}\int\operatorname{Tr}(\alpha\,\dd A\,\dd A)+O(A^3)\)
  is matched by a level-\(n\) WZW term only when \(n=N_c\).  A pion sigma model
  without WZW response fails the test.
- The WZW level comparison is now tied explicitly to the descent-coordinate
  discussion of the preceding anomaly chapter: local counterterms may change
  the four-form representative and the displayed \(O(A^3)\) completion, but
  not the completely symmetric coefficient of the six-form anomaly polynomial.
  The quadratic \(\operatorname{Tr}(\alpha\,\dd A\,\dd A)\) term is used as
  the lowest-background coordinate of that fixed cohomology class.
- The vector subgroup is anomaly-free in the local flavor anomaly coefficient
  because the left and right components of a Dirac quark contribute equally and
  with opposite signs.  The Vafa--Witten positivity argument is recorded as a
  separate input selecting the vector-aligned condensate under its hypotheses;
  anomaly matching then fixes the broken-axial WZW response.
- The electromagnetic specialization includes the microscopic quark triangle,
  the anticommutator factor
  \(\operatorname{Tr}(T^3\{q,q\})=2\operatorname{Tr}(T^3q^2)=1/3\), and the
  local \(\pi^0\gamma\gamma\) vertex in the gauged WZW functional with
  coefficient \(e^2/(16\pi^2f_\pi)\) for \(N_c=3\).
- The Vafa--Witten positivity argument is conditional on a well-defined
  finite-regulator gauge-invariant Euclidean vectorlike measure, a continuum
  scaling limit when a continuum conclusion is claimed, reflection positivity of
  the full gauge-plus-fermion regulator, the vectorlike Dirac determinant
  positivity condition, and existence of the volume/mass limits used to select
  a phase.

## Figure And Render Checks

- `fig:double-well-finite-volume`: double-well potential, localized
  wavepacket labels \(\ket{-a},\ket{+a}\), and the finite-dimensional
  tunneling comparison render legibly.
- `fig:u1-goldstone-vacuum-circle`: exact vacuum circle and tilted
  explicitly-broken potential render without title/axis collisions after the
  2026-05-22 polish.
- `fig:pion-scattering-leading-next`: leading four-pion vertex, one-loop
  two-derivative graph, and \(C_4,C'_4\) local term are visible and aligned
  with the source scattering discussion.
- `fig:soft-pion-ward-adler-zero`: axial-current insertion, current-channel
  pion pole, Ward-identity contact terms, and the hard-LSZ Adler-zero
  conclusion are displayed in the order used in the proof.
- `fig:wzw-five-dimensional-filling`: \(M_4=\partial B_5\) and the extension
  of \(U\) into \(B_5\) are included rather than only described in prose.
- `fig:em-axial-flavor-triangle` and `fig:pi-zero-two-photon-decay`: the
  microscopic axial-flavor triangle and the induced local pion vertex render
  with the current/photon labels in place.

## Open Boundaries

- The full global form of QCD flavor symmetry, higher-form symmetries, and
  complete cobordism classification of invertible responses are deferred to the
  global-structure volume.
- The complete gauged WZW functional is not expanded term by term here; only
  the defining variation and the neutral-pion two-photon coefficient are used.
  The WZW level matching itself is now derived in the manuscript as coefficient
  matching in the fixed flavor-trace convention, not left as a quoted theorem.
- A rigorous theorem proving the QCD chiral condensate pattern is not supplied;
  the pattern is an explicit dynamical input for the effective theory.
- The manuscript uses the self-consistent convention \(U\mapsto LUR^{-1}\) in
  the stereographic section; the handwritten notes use the opposite left/right
  naming in places, so future edits must not mix the two conventions without
  converting all formulas simultaneously.
- 2026-05-24 issue #252 pass: added the finite anomaly-inflow section with the
  mapping-torus identity, connected the \(SU(2)\) mod-two index to the
  five-dimensional invertible phase, and tied the gauged WZW functional to the
  same inflow class.
- 2026-05-24 issue #255 pass: named the Dai--Freed/APS framework for finite
  fermion anomalies, made the spin structures \(\sigma_M,\sigma_g,\sigma_Y\)
  explicit in the SU(2) mapping-torus and inflow formulas, and stated that the
  mod-two index is a function of the complete structured background rather
  than of an oriented manifold alone.
- 2026-05-24 issue #264 pass: promoted the Vafa--Witten caveat into an
  explicit hypothesis block.  The manuscript now states the required Euclidean
  measure, reflection positivity/OS reconstruction input, determinant
  positivity, and volume/mass-limit assumptions, and identifies continuum QCD
  measure construction as part of the open four-dimensional problem.
- 2026-05-24 issue #345 pass: sharpened the same Vafa--Witten hypothesis to
  distinguish finite-regulator measures \(\dd\nu_{m,\Lambda}\) from a continuum
  limiting functional \(\dd\nu_m\), and to state that reflection positivity must
  hold for the full regulator action and is not automatic for arbitrary
  regulators or gauge-fixed formulae.
- 2026-05-24 issue #265 pass: added a named chiral-symmetry-breaking
  conjecture before the pion construction.  The manuscript now states that
  \(\langle\bar q_R q_L\rangle\neq0\) and the
  \(SU(N_f)_L\times SU(N_f)_R\to SU(N_f)_V\) pattern are dynamical inputs for
  the low-energy pion EFT, supported by lattice/phenomenology but not proved
  from the four-dimensional QCD Lagrangian.
- 2026-05-24 issue #266 pass: added the Goldstone/gauged-direction caveat with
  the Abelian Higgs quadratic mixing, \(R_\xi\) gauge fixing, and BRST
  doublet/quartet interpretation, cross-referenced to the BRST chapter.
- 2026-05-25 issue #455 pass: added the soft-pion Ward identity, current-pole
  decomposition, hard-pion LSZ reduction, Adler-zero theorem for purely pionic
  amplitudes, the four-pion Adler-point check, and the corresponding schematic
  figure.
- 2026-05-25 issue #469 pass: expanded 't Hooft anomaly matching from a
  structural statement into a calculational IR constraint with the QCD
  UV-to-IR WZW level match as a worked example, explicit exclusion of a
  trivial symmetric gapped candidate absent an additional anomaly-carrying
  sector, vector-subgroup anomaly cancellation, and
  `calculation-checks/anomaly_matching_wzw_checks.py`.
- 2026-05-30 issue #696 pass: removed the WZW-level matching quoted theorem.
  The chapter now states the flavor trace convention and derives \(n=N_c\) by
  comparing the \(SU(N_f)_L\) descent coefficient of one color copy with the
  unit-level gauged WZW variation; Wess--Zumino consistency is identified as
  the reason the higher-background terms are fixed in the same cocycle class.
- 2026-06-01 issue #696 descent-coordinate pass: clarified that the
  quadratic WZW comparison fixes the symmetric anomaly-polynomial coordinate,
  while Bardeen counterterms only change representatives; extended
  `calculation-checks/anomaly_matching_wzw_checks.py` to verify the finite
  counterterm algebra.
- 2026-06-01 issue #696 Abelianized-descent continuation: cross-linked the WZW
  level comparison to the explicit Abelianized descent coordinate
  \(C_{abc}\alpha^aF^bF^c\) and the cubic polarization identity in the anomaly
  chapter, making clear why commuting-background tests fix the symmetric
  descent class but not a preferred current representative.
- 2026-05-30 issue #696 finite-\(SU(2)\) pass: removed the finite-doublet
  anomaly quoted theorem from the chapter.  The QFT conclusion is now a local
  proposition proved from Dai--Freed/Pfaffian-line holonomy, tensor-product
  multiplicativity for \(n\) doublets, and the five-dimensional mod-two index
  input for the Witten mapping torus; the proof explicitly separates gauged
  inconsistency from global-symmetry anomaly matching and explains why the
  obstruction is invisible to cubic local descent.
- 2026-05-25 issue #472 pass: added a named chiral perturbation theory section
  with Weinberg power counting, the full three-flavor Gasser--Leutwyler
  \(L_1,\ldots,L_{10}\) even-parity \(O(p^4)\) basis plus \(H_1,H_2\), the
  \(\Gamma_i\) running table, a worked two-flavor \(M_\pi^2\) chiral logarithm
  with scale cancellation, and `calculation-checks/chpt_nlo_checks.py`.
- 2026-06-03 issue #630 ChPT rigor pass: added the controlled-approximation
  ledger `ca:chiral-eft-truncation-seminorm`, making the \(O(p^4)\) ChPT
  calculation a compact-source-window seminorm statement rather than a bare
  power-counting slogan.  Extended `chpt_nlo_checks.py` to verify the
  topological Weinberg graph identity, the NLO retained graph inventory, and
  the first \(O(p^6)\) omitted-family budget.
