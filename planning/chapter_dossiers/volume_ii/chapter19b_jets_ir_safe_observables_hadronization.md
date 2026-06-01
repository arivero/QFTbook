# Volume IV, Jets, Infrared-Safe Observables, And Hadronization Dossier

## Logical Role

- Compiled in Volume IV immediately after the QCD renormalization and DIS
  chapter.
- Purpose in the monograph: formulate jets and final-state QCD observables as
  measurements on physical hadronic states, identify the precise infrared and
  collinear compatibility conditions under which partonic representatives are
  legitimate perturbative coordinates, and separate perturbative predictions
  from fragmentation and hadronization inputs.
- Immediate predecessor: QCD Renormalization, Asymptotic Freedom, And Deep
  Inelastic Scattering.
- Immediate successor: Chiral And Axial Anomalies.

## Definitions And Results

The chapter establishes:

- weighted inclusive cross sections with measurement functions on physical
  final states;
- partonic measurement representatives after choosing an infrared regulator
  and ultraviolet renormalization scheme;
- Definition `def:irc-safe-measurement` of infrared and collinear safety,
  including local estimates near unresolved boundaries;
- Proposition `prop:irc-safety-fixed-order-finiteness`, which derives the
  fixed-order cancellation mechanism from KLN sums and displayed
  soft/collinear factorization hypotheses;
- the Sterman--Weinberg two-jet measurement and its soft/collinear
  compatibility;
- generalized \(k_T\), Cambridge--Aachen, and anti-\(k_T\) sequential
  recombination algorithms;
- Proposition `prop:generalized-kt-irc-safety`, proving IRC safety of the
  generalized \(k_T\) family with four-momentum recombination and finite jet
  transverse-momentum thresholds;
- a factorized event-shape formula separating hard, jet, and soft functions,
  with SCET identified as the operator framework for such factorizations;
- Definition `def:scet-two-jet-operator-datum`, specifying the two-jet SCET
  operator datum: mode scalings as coordinates, collinear Wilson-line building
  blocks, soft Wilson lines, matched currents, renormalized jet/soft matrix
  elements, zero-bin/overlap subtraction, rapidity data, and Glauber-sector
  status;
- finite inclusion--exclusion bookkeeping for zero-bin/overlap subtraction,
  making explicit that an overlap region is subtracted once and that
  regulator-dependent scaleless-zero statements do not remove the need to
  specify the subtraction datum;
- a transform-space SCET renormalization-group transport datum for resummed
  singular coordinates, including hard/jet/soft anomalous-dimension
  consistency, evolution kernels from natural scales to a common scale, and
  the precise boundary of LL/NLL/NNLL accuracy labels;
- a finite Glauber unitarity diagnostic separating inclusive or commuting
  measurements, for which a finite Glauber unitary drops out of the trace,
  from noncommuting spectator/color measurements, where the exchange is a
  genuine factorization obstruction; the diagnostic now includes the exact
  finite remainder
  \(\operatorname{Tr}((U_G^\dagger M U_G-M)\rho_{\rm spec})\), its norm
  bound, and the Duhamel commutator estimate for \(U_G=\exp(\ii K_G)\);
- a massive-vector Sudakov boundary chart for high-energy electroweak jet
  measurements, deriving the triangular soft-collinear area
  \(A_V=\frac14\log^2(Q^2/M_V^2)\) and separating scalar one-line transport
  from the full charge-density-matrix datum;
- a prose derivation of the finite algebraic identity that a soft Wilson-line
  change of variables removes the leading \(n\cdot D_s\) soft connection from
  the collinear kinetic term, with the factorization content kept in the
  subsequent hypothesis rather than hidden in the identity;
- controlled-approximation statements for perturbative jet predictions and
  parton-shower logarithmic accuracy;
- a finite non-global soft-dipole evolution datum for angular veto
  measurements, deriving the first non-global coefficient from the nonlinear
  real-emission term into unmeasured cells;
- the soft-drop grooming definition and an IRC classification that separates
  \(\beta_{\rm SD}>0\) groomed four-momentum safety from the
  \(\beta_{\rm SD}=0\) collinear counterexample for the groomed four-vector;
- a finite-tree formulation of soft drop as a deterministic map on a
  Cambridge--Aachen declustering tree, with explicit soft-drop decision
  margins, harder-branch margins, and clustering-margin qualifications;
- a measured-mMDT finite-event test separating positive-angular-power groomed
  moments, which pass the one-prong collinear check, from retained-energy
  fraction, which fails it;
- a fixed-coupling soft-collinear soft-drop groomed-mass radiator geometry,
  including the logarithmic phase-space area, the mMDT single-log limit, and
  the scope boundary between this controlled approximation and a full
  renormalized factorization theorem;
- Definition `def:soft-drop-mass-factorization-datum`, promoting the
  fixed-coupling soft-drop mass chart to a renormalized datum with hard,
  global-soft, collinear-jet, and collinear-soft coordinates, the boundary
  scales \(\theta_*,z_*,\mu_H,\mu_G,\mu_J,\mu_{\rm cs}\), the
  hard/global-soft/jet/collinear-soft anomalous-dimension consistency equation,
  and an explicit remainder functional rather than an unqualified
  "resummed prediction";
- controlled approximation `ca:soft-drop-mass-factorized-resummation`,
  requiring perturbative scale separation, a topology for the factorization
  remainder, declared accuracy data, and replacement by a nonperturbative shape
  coordinate when the collinear-soft scale reaches \(\Lambda_{\rm QCD}\);
- controlled approximation `ca:sudakov-conditioned-zg`, defining the groomed
  momentum-sharing coordinate \(z_g\) as a first-accepted-split stopping-time
  observable and deriving its joint \((z_g,\theta_g)\) Sudakov density in the
  strongly ordered soft-collinear chart;
- the minimized-\(N\)-subjettiness value functional on a compact angular jet
  patch, with existence of minimizing axes and soft/collinear continuity of
  the minimized value rather than of a chosen axis label;
- a finite-kernel track-function evolution datum and a worked moment-coordinate
  derivation proving normalization preservation and the first-moment evolution
  formula under paired real--virtual track-function RG;
- Definition `def:track-function-operator-datum`, defining the track function
  itself as a renormalized gauge-invariant collinear source matrix element
  paired with a charged-track energy-fraction measurement operator;
- a track-function moment-generating equation and full moment-tower RG
  identity, making clear why a single average charged fraction is not a stable
  replacement for the nonperturbative track distribution;
- Definition `def:finite-track-observable-lift`, defining the finite lift of
  calorimetric energy polynomials to track-based observables by conditional
  expectation over track functions, including the diagonal moment terms;
- a measure-theoretic formulation of energy correlators as continuous
  functionals of the calorimetric energy measure;
- Lemma `lem:smeared-energy-correlator-continuity`, proving soft and
  collinear continuity bounds for Lipschitz smeared energy-correlator
  functionals;
- Theorem `thm:energy-correlator-polynomial-density`, proving by
  Stone--Weierstrass that the algebra generated by smeared energy moments is
  uniformly dense in continuous finite-resolution calorimetric observables on
  the compact energy-measure ball;
- Definition `def:leading-shape-function-operator-datum`, defining the
  endpoint shape function as a renormalized Wilson-line measurement
  distribution paired with test functions, together with its normalization and
  first soft moment;
- controlled approximation
  `ca:leading-endpoint-shape-function-convolution`, stating the endpoint
  convolution as an equality of distributions on a specified test-function
  space with a stated remainder functional;
- a light-ray operator definition of quark fragmentation functions with Wilson
  lines;
- the status of Lund string and cluster hadronization models as
  phenomenological nonperturbative inputs with fitted parameters;
- a classification table separating inclusive rates, IRC-safe event shapes,
  IRC-safe jet cross sections, energy correlators, identified hadron spectra,
  and fully exclusive hadronization patterns by required QCD input.

## Claim Ledger

1. A detector observable is first a function, distribution, or positive
   functional of physical final states; partonic formulae are perturbative
   representatives, not definitions of the observable.
2. IRC safety requires soft and collinear limits with local integrability
   estimates sufficient to pair the measurement difference with the singular
   factorization kernels.
3. Under displayed soft and collinear factorization hypotheses, IRC safety
   makes the real--virtual KLN cancellation local on unresolved final-state
   phase-space boundaries.
4. Initial-state collinear singularities in hadron collisions are absorbed
   into renormalized PDFs rather than canceled inside the hard subprocess.
5. Sterman--Weinberg jets are IRC safe because soft emissions change the
   out-of-cone energy continuously and collinear splittings preserve cone
   membership or out-of-cone energy in the collinear limit.
6. The generalized \(k_T\), Cambridge--Aachen, and anti-\(k_T\) algorithms are
   IRC safe with four-momentum recombination and finite transverse-momentum
   thresholds.
7. Seed-based cone algorithms with transverse-momentum seed thresholds may
   fail soft safety because a soft seed can alter the stable-cone set.
8. A fixed-order finite observable may still require resummation in regions
   with hierarchical measured scales.
8a. SCET mode labels are controlled coordinates on momentum regions, not
    physical colored Hilbert-space sectors.  A factorized formula must specify
    operator definitions, Wilson lines, overlap subtractions, rapidity data
    when present, Glauber status, and a topology for its remainder estimate.
8aa. Zero-bin subtraction is finite inclusion--exclusion at regulator level:
     collinear and soft approximants on a common soft-collinear corner are not
     both counted.  A convention change is harmless only when paired between
     collinear and soft coordinates; a scaleless integral in a particular
     regulator is not an invariant absence of overlap.
8ab. Resummation is a renormalization-group transport datum on a declared
     factorized coordinate.  In transform space the hard, jet, and soft
     anomalous dimensions must sum to zero as convolution kernels, and the
     resummed coordinate is obtained by evolving boundary functions from
     natural scales to a common scale.  Accuracy labels such as LL/NLL/NNLL
     are incomplete without the anomalous-dimension orders, matching orders,
     transform convention, scale choices, and factorization remainder.
8ac. Massive electroweak vector corrections to high-energy jet observables are
     controlled by a physical mass boundary \(M_V\), while the QCD sector
     retains its own operator and regulator datum.  In the one-line
     soft-collinear chart the finite phase-space area is
     \(A_V=\frac14\log^2(Q^2/M_V^2)\); a full electroweak jet prediction also
     requires the external charge-density matrix, real-emission inclusiveness,
     resonance or narrow-width status, and separate QCD/nonperturbative
     remainder data.
8b. The leading soft Wilson-line decoupling is an algebraic identity at finite
    regulator, transferring leading soft interactions from the collinear
    Lagrangian to Wilson lines in external operators and soft matrix elements.
    It does not by itself prove subleading-power factorization or Glauber
    cancellation.
8ba. Finite Glauber cancellation has a quantitative remainder coordinate:
     \(\Delta_G(M,\rho)=\operatorname{Tr}((U_G^\dagger M U_G-M)\rho)\).
     Exact cancellation requires the measured algebra to be invariant under
     \(U_G\); approximate cancellation requires a small commutator in the
     topology used for the smeared cross section, not merely a verbal
     assertion that Glauber exchanges cancel.
8c. Non-global angular measurements are not governed by a single linear soft
    anomalous dimension.  In a finite soft-dipole cell datum, unmeasured
    emissions are real--virtual balanced at first order but split the original
    dipole into two dipoles; differentiating the finite evolution at \(L=0\)
    yields the first non-global coefficient
    \(\sum_u K_{ij}^u(A_{iu}+A_{uj}-A_{ij})\).
9. Parton showers are controlled approximations whose logarithmic accuracy is
   observable- and scheme-dependent.
9a. Soft drop with \(\beta_{\rm SD}>0\) has a collinear-safe groomed
    four-vector, while for \(\beta_{\rm SD}=0\) the groomed four-vector itself
    is not collinear safe; mMDT safety statements must name the measured
    groomed functional.
9aa. The finite-event meaning of being away from grooming boundaries is now
     explicit: along the visited Cambridge--Aachen declustering path, the
     soft-drop inequality, the harder-child choice at failed vertices, and the
     clustering comparisons must have positive margins.  On such a chart the
     retained leaf set is locally constant, and any smooth functional of the
     retained momenta inherits the corresponding local soft/collinear
     behavior.  Boundary hypersurfaces require separate distributional
     treatment.
9ab. For mMDT, collinear safety is a property of the measured functional, not
     of the groomed constituent set by itself.  A positive-angular-power
     groomed moment can vanish on the deleted one-prong collinear branch,
     while retained-energy fraction jumps from \(1\) to \(1-z\).
9ac. The fixed-coupling soft-drop mass radiator is a logarithmic phase-space
     coordinate, not a QCD factorization theorem.  In the soft-collinear chart
     the veto area is cut out by \(u+t<L_\rho\) and
     \(u<L_z+\beta_{\rm SD}t/2\), giving the mMDT single-log area
     \(L_\rho L_z-L_z^2/2\) below the grooming scale.
9ad. A soft-drop groomed-mass resummation claim is meaningful only after the
     hard, global-soft, jet, and collinear-soft distributions, overlap and
     rapidity data, anomalous-dimension consistency, natural scale profiles,
     and a remainder functional have been specified.  The measurement and
     grooming equations give
     \(\theta_*=(\rho/z_{\rm cut})^{1/(2+\beta_{\rm SD})}\) and
     \(z_*=z_{\rm cut}^{2/(2+\beta_{\rm SD})}
     \rho^{\beta_{\rm SD}/(2+\beta_{\rm SD})}\); if
     \(Q\sqrt{\rho z_*}\) is nonperturbative, the collinear-soft entry is no
     longer a perturbative function and must be replaced by a stated
     nonperturbative coordinate.
9ae. Groomed momentum sharing \(z_g\) is a stopping-time coordinate, not an
     ordinary IRC-safe measurement on all finite events.  In the leading
     strongly ordered chart, its distribution is the first-accepted-split rate
     multiplied by the Sudakov probability for no earlier accepted split; for
     \(\beta_{\rm SD}=0\) this gives the normalized splitting-kernel
     distribution, while for \(\beta_{\rm SD}>0\) sub-\(z_{\rm cut}\) values
     are supported only at correspondingly small angles and are meaningful
     only together with the all-order Sudakov factor and remainder datum.
9b. Globally minimized \(N\)-subjettiness is a well-defined continuous
    calorimetric value functional on finite-energy jet measures; selected
    minimizing axes are auxiliary data and can jump at degenerate events
    without making the minimized value discontinuous.
10. Smeared energy correlators are continuous functionals of the positive
    calorimetric energy measure; their polynomial algebra separates
    finite-energy calorimetric measures and is dense in continuous
    finite-resolution calorimetric observables.
10a. Shape functions are renormalized Wilson-line measurement coordinates.
     Their leading endpoint convolution preserves total weight and shifts the
     first event-shape moment by \(\Omega_1^e/Q\) only after the observable,
     Wilson-line orientation, regulator, and subtraction scheme are fixed.
10b. Track functions are nonperturbative operator coordinates with paired
     real--virtual evolution; the pairing, not a slogan of IRC safety, is what
     preserves normalization and gives the charged-energy moment RG.
10c. A track-based energy polynomial is defined by lifting the energy measure
     to a random charged-track energy measure and then taking conditional
     expectation.  Diagonal terms in a two-point energy polynomial depend on
     the second track moment \(m_i^{(2)}\), and higher repeated parton labels
     require higher track moments.  The general finite \(k\)-point formula is
     a sum over maps from detector slots to short-distance labels; each label
     appearing \(r\) times contributes \(m_i^{(r)}\).  Replacing every energy
     by the first charged fraction changes the observable.
11. Fragmentation functions are nonperturbative light-ray matrix elements with
    perturbative scale evolution; their finite-scale boundary data are not
    produced by fixed-order perturbation theory.
12. Hadronization models supply phenomenological nonperturbative data and
    carry model and tuning uncertainties.
13. Lattice QCD supplies a regulator-level nonperturbative definition of the
    gauge theory, while real-time fragmentation and exclusive hadronization
    require additional reconstruction or matching ideas.

## Figure Requirements

- Measurement-function flow figure:
  physical final state \(\to\) measurement \(F(X)\) \(\to\) soft/collinear
  compatibility \(\to\) fixed-order, factorization, and resummation.
- Future refinements may add algorithmic jet-clustering diagrams only if the
  diagrams distinguish physical measurements from partonic coordinates.

## Checks

- Keep jet observables tied to physical final-state measurements before
  introducing partons.
- Do not treat hadronization models as derivations from continuum QCD.
- State the accuracy and matching assumptions whenever parton showers are used.
- Preserve the separation between IRC-safe observables, fragmentation
  functions, and fully exclusive hadronization patterns.
- 2026-05-24 issue #490 pass: compiled the jets/hadronization chapter into
  Volume IV, strengthened the IRC safety definition with local estimates,
  made the fixed-order finiteness statement conditional on displayed
  factorization hypotheses, and updated planning documents to record the
  chapter in the gauge-theory volume.
- 2026-05-25 issue #519/#526 pass: added the calorimetric-coordinate theorem
  for energy correlators, proving soft/collinear continuity of smeared
  \(k\)-point kernels and Stone--Weierstrass density of energy-correlator
  polynomials on the compact finite-energy measure space.  This supplies a
  rigorous reason energy correlators are natural jet-substructure
  coordinates, without treating partonic histories as observables.
- 2026-05-26 issue #526 pass: corrected the soft-drop IRC classification by
  separating the \(\beta_{\rm SD}>0\) groomed-four-vector statement from the
  \(\beta_{\rm SD}=0\) collinear counterexample, and added
  `calculation-checks/soft_drop_irc_checks.py`.
- 2026-06-01 issue #526 soft-drop finite-tree pass: added the
  Cambridge--Aachen declustering-tree datum and the decision-margin ledger
  \(m_v^{\rm SD}\), \(m_v^{\rm hard}\), together with the finite-event
  stability interpretation of "away from grooming boundaries"; extended
  `calculation-checks/soft_drop_irc_checks.py` to verify fixed-tree retained
  leaves, off-boundary perturbation stability, and boundary-crossing behavior
  with exact rational data.
- 2026-06-01 issue #526 measured-mMDT pass: added the finite angular moment
  \(G_\kappa\) as a test functional, separated its one-prong collinear
  behavior from the retained-energy fraction, and extended
  `calculation-checks/soft_drop_irc_checks.py` with exact rational checks of
  the \(2z(1-z)\theta^\kappa\) scaling and the mMDT energy-fraction jump.
- 2026-06-01 issue #526 soft-drop mass-radiator pass: added the
  fixed-coupling soft-collinear groomed-mass radiator as a controlled
  approximation, derived the logarithmic area formula and mMDT single-log
  limit, and extended `calculation-checks/soft_drop_irc_checks.py` with exact
  rational checks of the phase-space geometry.
- 2026-06-01 issue #526 soft-drop mass factorization-datum pass: added the
  renormalized hard/global-soft/jet/collinear-soft datum for groomed mass,
  derived the boundary scales from \(z\theta^2=\rho\) and
  \(z=z_{\rm cut}\theta^{\beta_{\rm SD}}\), stated the scale and
  anomalous-dimension consistency requirements, and extended
  `calculation-checks/scet_factorization_checks.py` with exact rational checks
  of the boundary-scale identities and RG transport consistency.
- 2026-06-01 issue #526 groomed-sharing pass: added the \(z_g\) stopping-time
  coordinate and the Sudakov-conditioned first-accepted-split density,
  including the mMDT normalized-kernel limit and the \(\beta_{\rm SD}>0\)
  angular-domain support condition; extended
  `calculation-checks/soft_drop_irc_checks.py` with exact rational checks of
  the normalization and support bookkeeping.
- 2026-06-01 issue #526/#630 continuation: added the minimized
  \(N\)-subjettiness measure-functional definition, proved existence of
  minimizing axes and continuity of the minimized value under weak, soft, and
  collinear variations, and added
  `calculation-checks/n_subjettiness_continuity_checks.py`.
- 2026-06-01 issue #526 shape-function pass: replaced the short
  phenomenological shape-function paragraph with an operator datum,
  distributional endpoint-convolution controlled approximation,
  normalization and first-moment diagnostics, scheme-translation bookkeeping,
  and `calculation-checks/shape_function_convolution_checks.py`.
- 2026-05-26 issue #526 track-function pass: added the paired finite-kernel
  RG datum, proved normalization preservation and first-moment evolution, and
  added `calculation-checks/track_function_moment_checks.py`.
- 2026-06-01 issue #526/#630 track-operator/moment-tower pass: promoted the
  track function from a named nonperturbative input to an explicit
  gauge-invariant collinear operator datum with a charged-track measurement
  insertion, derived the moment-generating RG equation and moment tower, and
  extended `calculation-checks/track_function_moment_checks.py`.
- 2026-06-01 issue #526 track-observable lift pass: added the finite
  track-lift definition for energy-measure polynomials, exposed the diagonal
  second-moment term and collinear composition law, and added
  `calculation-checks/track_observable_lift_checks.py`.
- 2026-06-01 issue #526 track-lift \(k\)-point pass: expanded the finite
  track-observable lift from the displayed two-point case to the full
  \(k\)-point map formula and the explicit three-point decomposition into
  distinct, partial-diagonal, and full-diagonal terms.  The paired check now
  verifies a nontrivial three-point kernel by exact enumeration and catches
  the false first-moment replacement.
- 2026-05-29 anti-wrapper pass: demoted the track-function normalization and
  first-moment proposition to a worked paragraph because the proof is the
  finite-kernel moment algebra; the substantive QFT datum remains the
  nonperturbative operator coordinate and the real--virtual paired evolution
  definition.
- 2026-05-27 issue #630 SCET pass: upgraded the factorization/resummation
  section with a two-jet SCET operator datum, finite soft Wilson-line decoupling
  proof, explicit overlap/zero-bin and rapidity-regulator requirements, and
  `calculation-checks/scet_factorization_checks.py`.
- 2026-06-01 issue #630/#526 zero-bin pass: added finite
  inclusion--exclusion bookkeeping for SCET overlap subtraction and extended
  `calculation-checks/scet_factorization_checks.py` with exact zero-bin
  double-counting and paired scheme-reshuffling checks.
- 2026-06-01 issue #630/#526 resummation-transport pass: upgraded the
  logarithmic-accuracy paragraph into a transform-space RG transport datum
  with hard/jet/soft anomalous-dimension consistency and common-scale
  independence; extended `calculation-checks/scet_factorization_checks.py`
  with exact rational RG-transport checks.
- 2026-06-01 issue #526/#630 massive-vector Sudakov pass: added a
  high-energy electroweak jet boundary chart with physical vector mass
  \(M_V\), derived the one-line area
  \(A_V=\frac14\log^2(Q^2/M_V^2)\), separated scalar Sudakov transport from
  charge-density-matrix evolution and boosted-resonance approximations, and
  extended `calculation-checks/scet_factorization_checks.py` with exact
  rational phase-space-area checks.
- 2026-06-01 issue #630 Glauber diagnostic pass: added the finite
  operator-trace mechanism for inclusive/commuting Glauber cancellation versus
  noncommuting measurement obstruction, and extended
  `calculation-checks/scet_factorization_checks.py`.
- 2026-06-01 issue #526/#630 Glauber remainder pass: sharpened the diagnostic
  by adding the exact finite remainder
  \(\operatorname{Tr}((U_G^\dagger M U_G-M)\rho)\), its operator/trace-norm
  bound, and the Duhamel commutator estimate; extended
  `calculation-checks/scet_factorization_checks.py` with exact rational
  checks of the cyclic remainder identity and Hilbert--Schmidt bound.
- 2026-06-01 issue #630/#526 non-global pass: added a finite angular-cell
  soft-dipole evolution datum for non-global veto measurements, derived the
  second-order coefficient separating the global Sudakov square from the
  first non-global term, and added
  `calculation-checks/qcd_non_global_log_checks.py`.
