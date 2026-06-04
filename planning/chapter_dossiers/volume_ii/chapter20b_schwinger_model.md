# Volume II, Schwinger Model Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter20b_schwinger_model_two_dimensional_qed.tex`.
- Compiled in Volume IV immediately after the local-anomaly chapter and before
  global anomalies, spontaneous symmetry breaking, and pions.
- Logical role: provide an exactly solvable gauge-theory example in which the
  local anomaly, bosonization, mass generation, screening of external flux,
  and massive-fermion confinement of fractional probes can be computed in a
  single convention-controlled model.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(a_\mu\) | real Abelian gauge representative in \(1+1\) dimensions |
| \(e\) | dynamical Dirac-field charge; \(e a_\mu\) is the compact \(U(1)\) connection |
| \(F_{\mu\nu}\) | Abelian curvature \(\partial_\mu a_\nu-\partial_\nu a_\mu\) |
| \(E\) | electric field \(F_{01}\) |
| \(J^\mu,J_A^\mu\) | unit vector and axial currents of the Dirac field |
| \(\varphi\) | compact boson with period \(\sqrt\pi\) in the chosen normalization |
| \(m_{\rm Sch}\) | exact Schwinger mass, \(m_{\rm Sch}^2=e^2/\pi\) |
| \(Q\) | external static probe charge coupling to \(a_\mu\) |
| \(G_m(x)\) | one-dimensional Green function of \(-\partial_x^2+m^2\) |
| \(M,\kappa\) | fermion mass and composite-mass-operator normalization constant |
| \(\sigma(Q)\) | large-distance string tension for a fractional probe in the massive model |

## Claims Established

- The local anomaly chapter's two-dimensional anomaly gives
  \(\partial_\mu J_A^\mu=(e/\pi)E\) for the dynamical gauge field.
- The gauge group is normalized so that \(e a_\mu\) is the compact \(U(1)\)
  connection; external probes of charge \(Q\) couple to \(a_\mu\), and
  \(Q/e\) determines whether the probe lies in the dynamical charge lattice.
- Canonical variation of \(a_0\) gives the Gauss-law constraint
  \(\partial_xE+eJ^0+\rho_{\rm ext}=0\).
- With \(\epsilon^{01}=+1\) and mostly-plus metric, the bosonization current
  dictionary
  \(J^\mu=\pi^{-1/2}\epsilon^{\mu\nu}\partial_\nu\varphi\) implies
  \(J_A^\mu=-\pi^{-1/2}\partial^\mu\varphi\).
- The bosonized scalar is explicitly interpreted as current/line-sector
  data, not as an ordinary local continuous-symmetry order parameter; this is
  aligned with the Coleman obstruction recorded in the following SSB chapter.
- Maxwell's equations together with the exact anomaly give directly
  \((\Box-e^2/\pi)E=0\), before using the bosonized action.
- The massless Dirac current-generating functional is exactly reproduced by
  the compact free scalar current algebra with the stated normalization.
- Eliminating the algebraic electric field in two dimensions gives the exact
  massive scalar action and the anomaly-induced mass
  \(m_{\rm Sch}^2=e^2/\pi\).
- The gauge-invariant electric field satisfies
  \((\Box-m_{\rm Sch}^2)E=0\) away from insertions.
- Static external charges are screened in the massless model:
  \(V_{\rm Sch}(R)=Q^2(1-e^{-m_{\rm Sch}R})/(2m_{\rm Sch})\).
- Adding a fermion mass gives the sine-Gordon perturbation
  \(\kappa M\cos(2\sqrt\pi\varphi+\theta)\).
- Fractional external probes shift the effective theta angle in the interval
  between probes by \(2\pi Q/e\).
- For a fractional probe in the massive model, the leading large-distance
  energy density is
  \(\sigma(Q)=\kappa M(1-\cos(2\pi Q/e))+O(M^2)\), while integer probes are
  screened by dynamical unit-charged fermions.

## Figure Requirements

- Schwinger-model exact-solution figure: massless Dirac field and Abelian
  gauge representative, current algebra, and the resulting massive scalar.
- Render check must verify that the current-algebra formula, anomaly equation,
  and mass formula are legible and do not overlap arrows or boxes.

## Audit Notes

- 2026-05-25 issue #466 pass: added the chapter to the compiled Volume IV
  sequence, tightened exact-bosonization, compact-gauge, Gauss-law, and
  probe-charge conventions, and added `calculation-checks/schwinger_model_checks.py`
  for the current-duality, anomaly-plus-Maxwell mass, screening-potential,
  and massive-probe string-tension normalizations.
- 2026-05-30 current-sector dequoting pass: replaced the quoted
  bosonization theorem by a local theorem/proof for the gauge-invariant
  derivative current algebra.  The proof fixes the normalization from the
  Schwinger term, derives the exact current source functional by Hodge
  decomposing the background one-form and removing the transverse source by
  an axial rotation with the two-dimensional anomaly Jacobian, and matches the
  result to the scalar Gaussian integral.  The compact period is stated as
  vertex-sector data, not as something determined by derivative current
  correlators alone.
- 2026-06-04 issue #770 re-audit: added the Coleman-compatible reading of the
  bosonized scalar as current/line-sector data rather than a continuous local
  order parameter.
