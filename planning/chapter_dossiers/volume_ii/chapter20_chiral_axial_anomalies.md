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
  manuscript states the hypotheses and formulas used; it does not reproduce
  the analytic proof of either theorem.
- The chapter states the descent formulas used for four-dimensional chiral
  fermions but does not reproduce the full proof of the local BRST cohomology
  classification.

## Framework

- Four-dimensional Lorentzian QFT with a Euclidean regulator used for
  heat-kernel and index statements.
- Gauge potentials use the Hermitian convention of the Yang--Mills chapters.
- Characteristic classes are written using the anti-Hermitian connection
  \(\mathsf A=-\ii A\), \(\mathsf F=\dd\mathsf A+\mathsf A^2=-\ii F\).
- Fermion chirality signs are stated relative to the chapter's \(\gamma_5\)
  convention.
- Local anomalies are represented by local functionals modulo BRST-exact
  counterterm shifts and total derivatives.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(j^\mu,j_5^\mu\) | vector and axial currents |
| \(\gamma=\gamma^0\gamma^1\) | two-dimensional chirality matrix |
| \(G_A^{\mu\nu}\) | two-dimensional axial-vector current correlator |
| \(Q_C\) | current charge integrated over a Euclidean contour \(C\) |
| \(\Delta Q_A\) | anomalous axial charge transported between contours |
| \(\mathcal D\) | Euclidean Dirac operator |
| \(J\) | fermion-measure Jacobian |
| \(n_\pm\) | zero modes of chirality \(\pm1\) |
| \(M\) | compact oriented Riemannian spin four-manifold used in the index theorem statement |
| \(S^\pm\) | positive and negative chirality spinor bundles on \(M\) |
| \(E_R,\nabla^E\) | Hermitian bundle and smooth unitary connection associated to the fermion representation \(R\) |
| \(\widehat A(TM)\) | Chern--Weil \(\widehat A\)-form of the tangent bundle |
| \(\operatorname{ch}(E_R,\nabla^E)\) | Chern character form of the gauge bundle |
| \(B_A\) | tangential boundary Dirac operator in the APS collar decomposition |
| \(\eta_{B_A}(0),h_{B_A}\) | eta invariant and boundary zero-mode dimension in the APS formula |
| \(\mathcal A(\zeta,A)\) | gauge variation of the effective action |
| \(\mathsf A,\mathsf F\) | anti-Hermitian connection and curvature for descent |
| \(I_6\) | six-form anomaly polynomial |
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
- The regulated trace of \(\gamma_5\) in a gauge background gives the local
  anomaly density.  Its integral is identified with a Fredholm index only
  under the closed spin Dirac hypotheses of the Atiyah--Singer theorem; in the
  flat tangent specialization this gives
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
- Gauge anomalies are ghost-number-one local BRST cohomology classes.
- In four dimensions the local chiral gauge anomaly descends from the six-form
  polynomial \(I_6\propto \operatorname{tr}\mathsf F^3\).
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
- A nonzero global-symmetry anomaly is data to be matched by the infrared
  theory, while a nonzero gauge anomaly obstructs the gauge theory.
- The strong CP parameter is the anomaly-invariant combination of the
  topological angle and the quark mass phase.

## Open Boundaries

- Gravitational anomalies are not developed here.
- Global anomalies are deferred to the next chapter.
- The Wess--Zumino--Witten functional is introduced in the next chapter, after
  chiral symmetry breaking and pion effective fields have been set up.

## Figure Requirements

- Two-dimensional axial-vector current loop with momentum labels.
- Conserved-current contour deformation and anomalous axial contour
  deformation.
- Four-dimensional one-axial, two-vector triangle pair with both orientations.

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
