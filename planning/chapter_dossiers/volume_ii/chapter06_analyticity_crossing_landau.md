# Volume II, Chapter 6 Dossier: Analyticity, Crossing, and Landau Singularities

## Scope

- Begins the general analytic-structure portion after bound states and
  resonances.
- Defines the physical \(s\)-channel region for identical massive scalar
  \(2\to2\) scattering and the first-sheet boundary value.
- States real analyticity and crossing as analytic properties of the
  continued amplitude under the standard massive-local-QFT hypotheses.
- Records the partial-wave unitarity boundary condition on the physical
  \(s\)-channel cut before using analytic continuation away from it.
- Derives the Landau equations from Feynman-parameter pinches.
- Works out the two-particle threshold and triangle/anomalous-threshold
  examples.

## Source Spine

- `transcription/tex/253b/scattering_rg_qcd.tex`, subsection "Analyticity,
  Crossing, and Landau Singularities", through the Coleman--Thun/anomalous
  threshold discussion.
- `references/253b transcribed lecture notes.tex`, corresponding
  analyticity/Landau section, used cautiously to compare figures and source
  ordering.
- Volume I chapters on LSZ, partial waves, and unitarity.
- Volume II Chapters 3--5 for bound-state poles, resonance poles, and
  four-point pole factorization.
- Veltman's largest-time equation and the 't Hooft--Veltman Diagrammar
  treatment are used as theorem-boundary controls for graph-level Cutkosky
  line replacement.

## Definitions and Symbols

| Symbol | Meaning |
| --- | --- |
| \(s,t,u\) | Mandelstam invariants for identical scalar \(2\to2\) scattering |
| \(\mathcal M(s,t)\) | connected invariant amplitude, analytically continued where defined |
| \(\mathfrak S_m\) | complexified on-shell invariant surface \(s+t+u=4m^2\) |
| \(\mathcal O_{\mathrm{poly}}(\mathcal D)\) | holomorphic functions on a complex kinematic domain with local polynomial-growth boundary estimates |
| \(\operatorname{bv}F\) | boundary-value distribution of a holomorphic germ, tested in \(C_c^\infty\) locally and in Schwartz topology when polynomial growth controls noncompact edges |
| first sheet | branch reached from the physical Feynman prescription without crossing a cut |
| \(\alpha_i\) | Feynman parameters for internal lines |
| \(q_i(\ell,p)\) | internal momentum on line \(i\), affine in loop momenta and external momenta |
| \(S_\ell(s)\) | angular-momentum-\(\ell\) partial-wave scattering eigenvalue in the two-particle sector |
| \(\beta(s)\) | local square-root variable for a two-particle threshold, whose sign changes on the adjacent sheet |
| \(M_{\mathrm{inel}}\) | invariant mass threshold of the lightest inelastic channel |
| \(\Delta_m^\pm(x)\) | positive/negative-frequency on-shell Wightman distributions for mass \(m\) |
| \(G_\sigma\) | circled graph associated to a vertex circling \(\sigma\) in the largest-time identity |
| \(C\) | set of internal lines crossed by a perturbative physical cut |
| Landau equations | on-shell and stationary conditions for a contour pinch |
| anomalous threshold | first-sheet singularity from a compatible positive-parameter Landau pinch |

## Assumptions

- The external particles are the lightest identical stable scalars of mass
  \(m\) unless stated otherwise.
- Mostly-plus metric: an on-shell mass-\(m_i\) internal line satisfies
  \(q_i^2+m_i^2=0\).
- Perturbative diagrams are considered with Feynman denominators
  \(q_i^2+m_i^2-\ii0\).
- Partial-wave unitarity is stated as a boundary condition on the upper edge
  of the physical cut; angular analyticity and high-energy boundedness are
  deferred.
- Physical-cut discontinuities are separated into the exact Hilbert-space
  unitarity identity, which sums exact on-shell intermediate states, and the
  perturbative Cutkosky line-replacement rule, which is obtained only after a
  regulator, graph expansion, and perturbative ordering have been chosen.
- Graph-level Cutkosky replacement is derived from the largest-time identity:
  the sum over all circlings of a scalar graph vanishes, mixed circlings carry
  on-shell Wightman distributions, and the \(s\)-channel physical cut is the
  subsum whose mixed lines separate the external labels into the chosen
  subprocesses.
- The analytic amplitudes are exact Hilbert-space boundary values when
  spectral/locality/LSZ hypotheses are being used; Landau and
  Feynman-parameter discussions are coefficientwise perturbative graph
  analyses with the status declared in
  `def:scattering-time-ordered-correlator-status`.
- Analyticity and crossing are used as structural hypotheses supported by
  locality, spectral support, LSZ, and perturbation theory; existing rigorous
  theorem sets cover only parts of the desired physical domain.
- Analytic continuation means continuation of a polynomial-growth holomorphic
  germ on the complexified on-shell invariant surface.  Equality on a real
  edge is equality of boundary-value distributions, and uniqueness is by
  edge-of-the-wedge plus the identity theorem on connected holomorphic
  domains.

## Claims to Derive

- The physical \(s\)-channel region has
  \[
    s=4(k^2+m^2),\qquad
    t=-2k^2(1-\cos\theta),\qquad
    s\ge4m^2-t,\quad t\le0.
  \]
- For fixed \(t<0\), the first sheet has a right-hand \(s\)-channel cut
  starting at \(4m^2\), a left-hand crossed-channel cut starting at \(-t\),
  and possible bound-state poles.
- The notation \(\mathcal M(s,t)\) must always specify whether it denotes the
  physical boundary-value distribution or the holomorphic germ on the relevant
  connected complex domain; no perturbative Borel summation is part of this
  definition.
- On the physical \(s\)-channel cut,
  \[
    \mathcal M(s,t)
    =
    -16\pi i\sqrt{\frac{s}{s-4m^2}}
    \sum_{\ell=0}^{\infty}(2\ell+1)P_\ell(\cos\theta)(S_\ell(s)-1),
    \qquad
    \cos\theta=1+\frac{2t}{s-4m^2},
  \]
  with \(|S_\ell(s)|\le1\) for \(s\ge4m^2\) and
  \(|S_\ell(s)|=1\) below the first inelastic threshold.
- The Cutkosky theorem must contain both pieces: the Hilbert-space
  discontinuity from \(S^\dagger S=1\) and the largest-time/circling argument
  that identifies a graph cut with on-shell line replacements.
- 2026-05-24 issue #391 pass: corrected the exact discontinuity identity to
  use \(\mathcal M_{X\alpha}\mathcal M_{X\beta}^*\), where
  \(\mathcal M_{\gamma\delta}\) denotes \(\delta\to\gamma\).  The conjugated
  factor is the adjoint matrix element for \(\beta\to X\), not the reversed
  amplitude \(X\to\beta\); replacing it by \(\mathcal M_{\beta X}^*\) would
  assume a separate reciprocity or time-reversal statement.
- Feynman-parameter pinches obey
  \[
    \alpha_i(q_i^2+m_i^2)=0,\qquad
    \sum_i \alpha_i q_i\cdot{\partial q_i\over\partial \ell_a^\mu}=0
  \]
  for every loop momentum \(\ell_a\).
- The two-propagator Landau equations give the ordinary two-particle
  threshold \(P^2=-4m^2\) in the equal-mass example.
- Triangle diagrams can produce first-sheet anomalous thresholds, including
  the equal-internal-mass criterion \(M_1,M_2<\sqrt2m\) versus
  \(M_1,M_2>\sqrt2m\), and the Coleman--Thun type mechanism.

## Figures

- Physical \(2\to2\) region and first-sheet \(s\)-plane.
- Crossing regions in the real \((s,t)\)-plane.
- Contour pinch leading to Landau equations.
- Bubble threshold Landau solution.
- Triangle Landau vector test and anomalous threshold.

## Boundaries

- No Lehmann ellipse, partial-wave convergence, Froissart--Martin mechanism,
  dispersion relations, or polynomial boundedness; those belong to the next
  chapter.
- No attempt to make an axiomatic foundation out of perturbative Landau
  analysis.

## Audit Notes

- 2026-05-24 issue #319 pass: added a chapter-opening status reminder
  separating exact Hilbert-space analytic boundary values from
  coefficientwise perturbative Landau/Feynman-parameter graph analysis.
- 2026-05-24 issue #425 pass: renamed the threshold square-root variable from
  \(\rho(s)\) to \(\beta(s)\) so it cannot be confused with the
  Kallen--Lehmann spectral measure \(d\rho\).
