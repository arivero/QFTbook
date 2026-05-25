# Volume III, Chapter 1 Dossier: Fixed Points And Conformal Data

## Logical Role

- Role in the monograph: open the core CFT volume by formulating fixed points
  as local QFT data, with stress-tensor assumptions, renormalized operator
  coordinates, source-dependent distributions, and the Ising fixed point as
  the first organizing example.
- Immediate predecessor: Volume II universality and source-dependent
  observable limits.
- Immediate successor: conformal Killing vectors and the conformal group.

## Definitions And Results

The chapter establishes:

- Lorentzian local QFT data used in fixed-point analysis: Hilbert space,
  Poincare representation, vacuum, local operator-valued distributions, and
  stress tensor;
- renormalized deformation operators and the trace equation
  \(T^\mu{}_\mu=\beta_I[O_I]+\partial_\mu V^\mu\), including the role of
  contact terms and improvements;
- the scale-versus-conformal obstruction as the local virial class at a
  fixed point, including the definition of a scale-invariant but
  nonconformal local QFT in this stress-tensor framework and Polchinski's
  virial-current criterion; the dimension-dependent status is stated with
  theorem formulations in two dimensions only under explicit analytic
  hypotheses, conditional four-dimensional anomaly/dilaton constraints with no
  unconditional theorem used here, and no assumed general theorem in other
  dimensions;
- fixed points as zeros of the beta-function vector field in a chosen local
  coordinate chart;
- scaling dimensions from the linearized RG eigenvalues
  \(y_a=D-\Delta_a\);
- endpoint RG monotones as data attached to a stated class of unitary RG
  trajectories, with length scale \(R\) increasing toward the infrared and
  \(\mathfrak M_{\rm UV}\geq\mathfrak M_{\rm IR}\);
- the two-dimensional \(c\)-function status: a stress-tensor two-point
  construction whose derivative is negative by reflection positivity under
  the Zamolodchikov--Polchinski hypotheses;
- the three-dimensional entropic \(F\)-monotone
  \(\mathcal F(R)=R S'(R)-S(R)\), its strong-subadditivity/Lorentz-invariance
  monotonicity, and its endpoint identification with the \(S^3\) free energy
  when the CFT and counterterm hypotheses are satisfied;
- the four-dimensional Komargodski--Schwimmer \(a_{\rm W}\)-monotonicity
  mechanism: Wess--Zumino anomaly matching for a weak spectator dilaton,
  the forward four-dilaton amplitude, the dispersion relation, and the
  positive cross-section sum rule for \(a_{\rm UV}-a_{\rm IR}\);
- CFT data as local operator space, stress tensor, conformal-algebra action,
  and Euclidean separated-point distributions;
- source functionals \(W_\ast[g,J]\) whose derivatives define stress
  tensor insertions and local-operator insertions;
- the explicit existence hypothesis for the fixed-point source chart:
  \(W_\ast[g,J]\) is used only when all metric/source derivatives exist as
  distributions in a specified test-function topology, and when regulated
  realizations converge after local source counterterms;
- the status of fixed-point source brackets
  \(\langle\exp(\int\sqrt g\,J^A\mathcal O_A)\rangle_{g,\ast}\): constructive
  measure expectation, regulated continuum-limit source functional, abstract
  CFT generating functional for Schwinger distributions, or perturbative
  formal source series, depending on the supplied fixed-point construction;
- the curved-background meaning of \(\langle\cdots\rangle_{g,\ast}\): it is
  evaluation by \(Z_\ast[g,J]\), and when only flat separated-point data are
  supplied the compatible metric/source extension is an additional datum or
  theorem, not an automatic consequence of the notation;
- diffeomorphism and Weyl Ward identities as identities of
  source-dependent distributions, with contact terms fixed by the source
  chart;
- dependence of the CFT contact-term chart on the source-functional trace
  identity and Wess--Zumino anomaly consistency inherited from the RG/fixed-point
  construction;
- Ising universality as a fixed-point example, while distinguishing the
  finite statistical trace space from any reconstructed continuum Hilbert
  space.
- the \(D\geq4\) existence status: explicit free Gaussian CFTs, formal
  Wilson--Fisher \(\epsilon\)-expansion data, scalar triviality constraints in
  four dimensions, and gauge/supersymmetric fixed-point constructions used
  only with their stress-tensor, positivity, locality, spectrum, and Ward-data
  hypotheses stated.
- The displayed \(D=3\) Ising numerical entries are rounded from
  mixed-correlator numerical conformal-bootstrap data.  The manuscript states
  the operative input: crossing symmetry and reflection positivity for mixed
  correlators of \(\sigma\), \(\varepsilon\), and \(T_{\mu\nu}\), finite
  semidefinite relaxations, and gap assumptions defining the numerical search.
  The computation cited is "Bootstrapping the 3d Ising Stress Tensor" by
  Chang, Dommes, Erramilli, Homrich, Kravchuk, Liu, Mitchell, Poland, and
  Simmons-Duffin, JHEP 03 (2025) 136 (arXiv:2411.15300), which reports
  \(\Delta_\sigma=0.518148806(24)\) and
  \(\Delta_\varepsilon=1.41262528(29)\), giving
  \(\nu=1/(3-\Delta_\varepsilon)=0.629970975\ldots\).
- Universal Ising scaling functions are defined as separated-point continuum
  limits of normalized lattice observables after analytic changes of relevant
  scaling coordinates, field normalizations, and analytic-background
  subtractions.  The manuscript distinguishes these universal functions from
  critical temperatures, metric factors, contact extensions, and bootstrap
  numerical uncertainties.

## Claims To Verify

1. CFT correlators are restrictions of source-dependent distributions to
   noncoincident configurations.
2. Contact-term extensions are part of the source-coordinate convention and
   are not determined by separated-point kernels alone.
3. Stress-tensor Ward identities are distributional identities obtained by
   differentiating the background-metric/source functional.
3a. The fixed-point brackets used in \(W_\ast[g,J]\) are typed
    source-functional data; they are measure expectations only in constructive
    measure settings, continuum-limit brackets in lattice/Wilsonian settings,
    distributional generating brackets in abstract CFT settings, and formal
    source series in perturbative settings.
3b. The metric and source derivatives of \(W_\ast[g,J]\) are legitimate only
    inside a source chart satisfying the explicit existence hypothesis:
    distributional Gateaux derivatives exist, regulated derivatives converge
    when a regulator presentation is used, and regulator changes are tracked by
    local source counterterms.
4. The trace equation at a fixed point becomes a conformal trace condition
   only after improvement and contact-term conventions have been specified.
5. The statement that scale invariance implies conformal invariance is used
   only after the local virial obstruction class has been proved or included
   in the fixed-point data.
5a. RG monotonicity statements must specify their class of trajectories and
    analytic assumptions.  The chapter may use \(c_{2d}\), \(F\), and
    \(a_{\rm W}\) as endpoint-ordering data only with the corresponding
    positivity, entanglement, or S-matrix hypotheses stated.
6. The Ising fixed point supplies a statistical-mechanics example whose
   continuum CFT data are obtained from scaling limits of correlators, not
   from the finite lattice trace space.
6a. Complete fixed-point CFT data determine critical separated-point scaling
    functions conditionally on CFT/OPE convergence; off-critical scaling
    functions require the constructed relevant deformation, and the \(D=3\)
    lattice-to-CFT identification remains a conditional continuum-limit
    statement.
7. Claims about interacting \(D\geq4\) CFTs must distinguish exact free
   conformal theories, formal perturbative fixed-point data, scalar
   triviality theorems, and physical gauge-theory constructions whose
   nonperturbative CFT data are additional hypotheses in this volume.

## Figures

- Existing Ising fixed-point figures may remain.
- Add figures only when they clarify a construction not already captured by
  equations; avoid decorative diagrams.

## Checks

- Keep the CFT opening chapter tied to local QFT data and source
  distributions.
- Do not promote bootstrap, two-dimensional, topological, supersymmetric, or
  integrable special structures into this opening volume.
- State reconstruction assumptions instead of identifying Euclidean
  correlators with Lorentzian Hilbert-space data without hypotheses.
- 2026-05-22 source-functional Ward pass: added the source functional
  \(W_\ast[g,\eta]\), stress-tensor and operator derivative conventions, the
  diffeomorphism Ward identity, and smeared translation/Weyl contact Ward
  identities.
- 2026-05-24 issue #232 pass: tied \(W_\ast[g,\eta]\) explicitly to the
  contact-distribution trace identity and Wess--Zumino consistency condition in
  the stress-tensor trace chapter, so the CFT source-functional Ward identities
  no longer rest only on separated-point trace data.
- 2026-05-24 issue #271 pass: added the scale-versus-conformal remark in the
  opening CFT chapter, defining the dilatation current, removable virial class,
  scalar stress-tensor improvement, and the dimension-dependent status with a
  cross-reference to the fuller stress-tensor treatment.
- 2026-05-24 issue #272 pass: added the \(D\geq4\) existence-status remark,
  separating free Gaussian CFTs, noninteger-dimensional Wilson--Fisher
  perturbative data, four-dimensional scalar triviality, and gauge/supersymmetric
  fixed-point constructions with explicit data requirements.
- 2026-05-24 issue #280 pass: added the RG-monotone section covering the
  formulated \(2D\) \(c\)-function, \(3D\) entropic \(F\)-monotone, and
  \(4D\) Komargodski--Schwimmer \(a_{\rm W}\)-monotonicity argument, with
  assumptions and endpoint meanings stated.
- 2026-05-24 issue #282 pass: strengthened the \(D=3\) Ising numerical
  provenance remark to identify the conformal-bootstrap constraints and
  semidefinite relaxations behind the displayed values, and to separate those
  numerical CFT data from a constructive proof of the lattice scaling limit.
- 2026-05-24 issue #283 pass: expanded the scale-versus-conformal remark to
  define scale-invariant but nonconformal local QFTs by a nonzero virial class
  in the improvement quotient and to cite Polchinski's virial-current
  obstruction.
- 2026-05-24 issue #303 pass: added
  `def:cft-fixed-point-source-bracket-status`, classifying the fixed-point
  source brackets and \(Z_\ast[g,J]\) by construction type instead of leaving
  them as untyped continuum expectation notation.
- 2026-05-24 issue #321 pass: sharpened the same definition to state that
  \(\langle\cdots\rangle_{g,\ast}\) denotes evaluation by the curved-background
  source functional \(Z_\ast[g,J]\); if a CFT is supplied only by flat
  separated-point correlators, the metric/source extension and Weyl-anomaly
  contact chart must be separately supplied or proved.
- 2026-05-24 issue #331 pass: added a definition of universal Ising scaling
  functions, a conditional proposition proving that complete CFT data determine
  critical separated-point scaling functions under OPE convergence, and a
  status remark separating \(D=3\) bootstrap numerical uncertainties from
  lattice convergence rates or constructive continuum-limit error bounds.
- 2026-05-24 issue #343 pass: added
  `hyp:cft-fixed-point-source-chart-existence`, which states the distributional
  existence, regulated convergence, and regulator-independence-modulo-local
  counterterm requirements before \(W_\ast[g,J]\) is differentiated.
- 2026-05-24 issue #409 pass: made the sign convention in
  `eq:cft-source-derivative-conventions` explicit from \(W_\ast=-\log Z_\ast\)
  and the metric variation
  \(\delta_g S_\ast=-\frac12\int\sqrt g\,T^{\mu\nu}\delta g_{\mu\nu}\).
  This aligns the opening CFT source chart with the stress-tensor chapter.
