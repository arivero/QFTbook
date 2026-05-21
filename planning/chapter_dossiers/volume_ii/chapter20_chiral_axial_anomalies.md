# Volume II, Chiral and Axial Anomalies Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Follows QCD renormalization and the BRST cohomology chapter.
- Precedes global anomalies, spontaneous symmetry breaking, pions, and the
  Wess--Zumino--Witten term.
- Role in the monograph: define local axial and gauge anomalies as
  renormalized Ward identities, derive the abelian anomaly through regulated
  measure/index language, classify local gauge anomalies through BRST descent,
  and identify which anomalies are inconsistencies and which are global
  symmetry data to be matched.

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
| \(\mathcal D\) | Euclidean Dirac operator |
| \(J\) | fermion-measure Jacobian |
| \(n_\pm\) | zero modes of chirality \(\pm1\) |
| \(\mathcal A(\zeta,A)\) | gauge variation of the effective action |
| \(\mathsf A,\mathsf F\) | anti-Hermitian connection and curvature for descent |
| \(I_6\) | six-form anomaly polynomial |
| \(I_5^{(0)}\) | Chern--Simons five-form in the descent sequence |
| \(I_4^{(1)}\) | ghost-number-one four-form anomaly representative |
| \(d^{abc}\) | symmetric cubic gauge-anomaly tensor |
| \(J_{\mathrm{cons}}\) | consistent current, \(\delta W/\delta A\) |
| \(J_{\mathrm{cov}}\) | covariant current after Bardeen--Zumino improvement |
| \(J_{\mathrm{BZ}}\) | Bardeen--Zumino local polynomial current |
| \(\bar\theta\) | anomaly-invariant QCD CP-odd parameter |
| \(Q[A]\) | instanton/topological charge |

## Claims Established

- The axial anomaly is a renormalized composite-operator identity, not a
  classical equation of motion.
- The regulated trace of \(\gamma_5\) in a gauge background gives the local
  anomaly density and the integrated index theorem.
- Gauge anomalies are ghost-number-one local BRST cohomology classes.
- In four dimensions the local chiral gauge anomaly descends from the six-form
  polynomial \(I_6\propto \operatorname{tr}\mathsf F^3\).
- Local gauge-anomaly cancellation is the vanishing of the symmetric cubic
  tensor \(d^{abc}\) for the gauged symmetry.
- The consistent current is obtained from the effective action and obeys the
  Wess--Zumino consistency condition.
- The covariant current differs from the consistent current by a
  Bardeen--Zumino current and need not be a functional derivative of a local
  effective action.
- A nonzero global-symmetry anomaly is data to be matched by the infrared
  theory, while a nonzero gauge anomaly obstructs the gauge theory.
- The strong CP parameter is the anomaly-invariant combination of the
  topological angle and the quark mass phase.

## Open Boundaries

- Gravitational anomalies are not developed here.
- Global anomalies are deferred to the next chapter.
- The Wess--Zumino--Witten functional is introduced in the next chapter, after
  chiral symmetry breaking and pion effective fields have been set up.
