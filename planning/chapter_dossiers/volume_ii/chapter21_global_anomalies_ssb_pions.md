# Volume II, Global Anomalies, Spontaneous Symmetry Breaking, And Pions Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`.
- Follows the local anomaly chapter.
- Role in the monograph: pass from local anomaly cocycles to finite
  background anomalies, state anomaly matching as equality of cocycle classes,
  derive the Goldstone pole from a Ward identity and spectral support, and
  construct the leading pion effective action and Wess--Zumino--Witten term.

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
  and mod-two indices.
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
| \(X_g\) | mapping torus associated to a gauge transformation \(g\) |
| \(\zeta(X_g,E_g)\) | mod-two index of the coupled real Dirac operator |
| \(G,H\) | symmetry group and unbroken subgroup in a phase |
| \(\xi(\pi)\) | coset representative for Goldstone coordinates |
| \(e^a,\omega^i\) | broken vielbein and unbroken connection in the Maurer--Cartan form |
| \(F_{Aa}\) | Goldstone decay-constant matrix |
| \(U(x)\) | pion field valued in \(SU(N_f)\) |
| \(\ell_\mu,r_\mu\) | external left and right flavor gauge fields |
| \(F_{\rm st}\) | stereographic-coordinate pion normalization used for the explicit \(N_f=2\) scattering calculation |
| \(\vec D_\mu=\partial_\mu\vec\xi/(1+\vec\xi^{\,2})\) | covariant stereographic building block for the \(N_f=2\) four-derivative invariants |
| \(A(s,t,u)\) | invariant scalar function in the \(SU(2)_V\) pion scattering amplitude |
| \(C_4(\mu),C'_4(\mu)\) | local four-derivative low-energy constants in the \(N_f=2\) pion EFT |
| \(\Phi^I{}_{J}=\bar q_L^I q_{R,J}\) | microscopic chiral order-parameter field used to match the two-flavor mass deformation |
| \(M,\chi,B_0\) | quark mass spurion, chiral spurion, and low-energy constant |
| \(Q\) | electromagnetic flavor-charge matrix embedded as a vector flavor background |
| \(\Gamma_{\mathrm{WZ}}\) | ungauged Wess--Zumino functional |
| \(\Gamma_{\mathrm{WZW}}\) | gauged Wess--Zumino--Witten functional |

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
- A single four-dimensional left-handed \(SU(2)\) fundamental Weyl fermion has
  a finite anomaly detected by a mod-two index on a mapping torus.
- Anomaly matching is equality of the background anomaly cocycle class between
  UV and IR descriptions.
- Infinite-volume vacuum sectors are separated from finite-dimensional
  tunneling by the scaling of the instanton action with spatial volume; local
  operators act diagonally on pure homogeneous phases by locality and cluster
  decomposition.
- The Goldstone theorem is derived as a massless spectral contribution forced
  by the Ward identity and a nonzero order parameter.
- The explicit \(U(1)\) Goldstone model is developed in polar variables, with
  \(j^\mu=2r^2\partial^\mu\theta\), \([Q,\theta]=i\), a massive radial mode,
  and a pseudo-Goldstone mass from a small \(-\epsilon\operatorname{Re}\phi\)
  deformation.
- The leading pion Lagrangian is the invariant two-derivative functional of
  the \(SU(N_f)\)-valued Goldstone field and external flavor backgrounds.
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
- The Wess--Zumino--Witten coefficient is quantized and equals \(N_c\) for QCD
  with fundamental quarks, so the pion functional reproduces the microscopic
  flavor anomaly.
- The electromagnetic specialization includes the microscopic quark triangle,
  \(\operatorname{Tr}(\sigma_3Q^2/2)=e^2/6\), and the local
  \(\pi^0\gamma\gamma\) vertex in the gauged WZW functional.

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
- `fig:wzw-five-dimensional-filling`: \(M_4=\partial B_5\) and the extension
  of \(U\) into \(B_5\) are included rather than only described in prose.
- `fig:em-axial-flavor-triangle` and `fig:pi-zero-two-photon-decay`: the
  microscopic axial-flavor triangle and the induced local pion vertex render
  with the current/photon labels in place.

## Open Boundaries

- The full global form of QCD flavor symmetry, higher-form symmetries, and
  anomaly inflow are deferred to the global-structure volume.
- The complete gauged WZW functional is not expanded term by term here; only
  the defining variation and the neutral-pion two-photon coefficient are used.
- A rigorous theorem proving the QCD chiral condensate pattern is not supplied;
  the pattern is an explicit dynamical input for the effective theory.
- The manuscript uses the self-consistent convention \(U\mapsto LUR^{-1}\) in
  the stereographic section; the handwritten notes use the opposite left/right
  naming in places, so future edits must not mix the two conventions without
  converting all formulas simultaneously.
