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
- a regulated one-emission endpoint observable for the color-singlet two-jet
  current, with off-light-cone Wilson-line velocities producing the mixed
  denominators \((u+\delta v)(v+\delta u)\), a finite endpoint slice
  \(u+v\ge\lambda\), smeared measurement \(\varphi(u+v)\), three soft
  endpoint Taylor projections \(S_u,S_v,S_0\), auxiliary constant-projection
  allocation cancellation, a mixed-remainder bound
  \(M_\varphi\int K_\delta uv\le M_\varphi(1+\delta^2)\rho^2\), and negative
  controls for additive-denominator replacement, double-counting, unpaired
  projection allocation, and treating the soft square as a hard or collinear
  region;
- controlled approximation `ca:scet-distributional-factorization-estimate`,
  stating leading-power SCET factorization as a bound on smeared physical
  cross-section functionals on a Banach endpoint test space, with the
  physical functional, factorized singular coordinate, endpoint parameter,
  topology, power remainder, perturbative truncation remainder, and finite
  transform-space scheme covariance all explicitly named;
- an occurrence-level claim-status ledger for the factorization material,
  tying concrete manuscript labels in SCET, soft drop, non-global logarithms,
  EEC, DIS, Drell--Yan, TMD, small-\(x\), exclusive-pion, track, and
  shape-function formulae to regulator, source, proof, Glauber, and remainder
  status rather than to historical theorem labels;
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
  bound, the Duhamel commutator estimate for \(U_G=\exp(\ii K_G)\), and the
  explicit two-state rotation example
  \(\Delta_G=(r_2-r_1)\sin^2\theta\);
- controlled approximation `ca:scet-spectator-tmd-color-entanglement`, using
  the Rogers--Mulders nonabelian spectator-model calculation to expose a
  real generalized-TMD factorization obstruction: the one-gluon separate-loop
  anomaly vanishes by \(\operatorname{tr}(t^a)=0\), while the cross-hadron
  two-gluon Glauber term carries
  \(\operatorname{tr}(t^at^b)\operatorname{tr}(t^bt^a)=T_F^2(N_c^2-1)\),
  same/opposite cut phases add, and a source-derived positive-denominator
  finite witness for the \(q_\perp\)-differential double-spin transverse
  skeleton cannot be assigned to separate one-hadron TMD factors;
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
  real-emission term into unmeasured cells and comparing it with the
  global-Sudakov-only ansatz that misses the unmeasured-to-measured cascade;
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
- controlled approximation
  `ca:finite-resolution-eec-observable-assembly`, turning the calorimetric
  coordinate theorem into a detector-level prediction datum: binned positive
  energy measure, Lipschitz binning bound, contact and endpoint convention,
  short-distance coefficient chart, nonperturbative lift, and an explicit
  residual ledger for binning, contact, perturbative, factorization/Glauber,
  nonperturbative, track, and continuum/regulator errors;
- controlled approximation
  `ca:measured-small-angle-eec-endpoint-chart`, spelling out the measured-bin
  interface between small-angle light-ray OPE coefficients and detector EEC
  bins: the pushforward Jacobian
  \((2\rho-\rho^2)^{(d_\perp-2)/2}\), endpoint plus/contact transport,
  retained light-ray operator residuals, matching residuals, and
  nonperturbative lift must be supplied before small-angle powers or anomalous
  dimensions become a physical EEC prediction;
- controlled approximation `ca:measured-eec-global-moment-closure`, requiring
  small-angle, back-to-back, and separated-angle EEC charts to glue to the same
  measured selected-energy zeroth and first moment constraints.  The block
  solves the coincident and back-to-back endpoint atoms from \(A_\omega\),
  \(B_\omega\), and the open moments, and gives the finite endpoint-test bound
  for repairing residual moment defects;
- Definition `def:leading-shape-function-operator-datum`, defining the
  endpoint shape function as a renormalized Wilson-line measurement
  distribution paired with test functions, together with its normalization and
  first soft moment;
- controlled approximation
  `ca:leading-endpoint-shape-function-convolution`, stating the endpoint
  convolution as an equality of distributions on a specified test-function
  space with a stated remainder functional;
- controlled approximation `ca:shape-function-smeared-moment-expansion`,
  deriving the smeared-test Taylor expansion in which \(\Omega_1^e/Q\) gives
  the leading shift and \(\Omega_2^e/Q^2\) bounds the first omitted endpoint
  curvature term;
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
8aaa. The regulated one-emission endpoint observable for a color-singlet
      two-jet current supplies a positive fixed-order soft endpoint case: with
      \(\beta_n=n+\delta\bar n\), \(\beta_{\bar n}=\bar n+\delta n\), the
      cut Wilson-line graph has kernel
      \(K_\delta=(1+\delta^2)/((u+\delta v)(v+\delta u))\) on the sliced
      endpoint domain \(0\le u,v\le\rho,\ u+v\ge\lambda\).  That domain has
      both light-cone components small, so it is not a hard, \(n\)-collinear,
      or \(\bar n\)-collinear region.  Taylor-projecting the same soft graph's
      measurement to \(u\), \(v\), and \(0\) gives finite soft endpoint
      coordinates; the exact graph differs by a mixed finite-difference
      remainder bounded by
      \(M_\varphi\int K_\delta uv\le M_\varphi(1+\delta^2)\rho^2\).  The
      additive-denominator model is only an auxiliary algebraic negative
      control, the unsubtracted Taylor projections double-count the constant
      endpoint projection, and an unpaired allocation parameter leaves
      arbitrary split dependence.
8ab. Resummation is a renormalization-group transport datum on a declared
     factorized coordinate.  In transform space the hard, jet, and soft
     anomalous dimensions must sum to zero as convolution kernels, and the
     resummed coordinate is obtained by evolving boundary functions from
     natural scales to a common scale.  Accuracy labels such as LL/NLL/NNLL
     are incomplete without the anomalous-dimension orders, matching orders,
     transform convention, scale choices, and factorization remainder.
8ac. A leading-power factorization claim is an estimate on smeared physical
     cross-section functionals.  The chapter now distinguishes the physical
     measure, the endpoint test-function Banach space, the factorized
     singular coordinate, the power remainder, and any perturbative
     truncation remainder.  Finite multiplicative changes of hard, jet, and
     soft coordinates represent the same singular distribution only when the
     product of the finite factors is one; anomalous-dimension consistency is
     then preserved by the paired logarithmic shifts.
8aca. The SCET/factorization claim-status ledger is now occurrence-level:
      each concrete formula label records the observable, regulator or scheme,
      strongest source used locally, actual proof status, Glauber status, and
      remainder status.  A historical physics phrase such as "factorization
      theorem" is not a proof-status certificate unless the dependency ladder
      and observable-topology remainder are supplied at that occurrence.  The
      2026-06-04 issue #828 pass expands the audit to the omitted
      triple-Regge, Abelian soft-QED, GPD/exclusive, and DIS-threshold
      boundary occurrences; it also classifies pole/residue, large-\(N_c\),
      spinor-helicity, pAQFT causal-factorization, and BV prefactorization
      homonyms outside the QCD/SCET hard-process ledger.  The 2026-06-04
      issue #832 pass makes the audit source-derived: manuscript labels,
      factorization-titled environments, and captions containing
      "factorization" or "factorized" must appear in
      `planning/factorization_occurrence_manifest.tsv` as included, grouped,
      or excluded.  The 2026-06-04 issue #834 pass adds
      `planning/factorization_textual_candidate_review.tsv` for section and
      paragraph titles plus semantic prose-window triggers such as
      "factorization coordinate" and "factorization theorem"; the massive-vector
      electroweak Sudakov chart is promoted to its own ledger row, while
      integrable scattering, instanton determinant/size decompositions,
      conformal/categorical algebra, finite-range Gaussian decompositions,
      Monte Carlo conditional probabilities, split-property tensor
      factorization, and other non-QCD meanings are kept outside the
      hard-process ledger by name.
8acaa. The finite non-global dipole evolution row is a soft-radiation/BMS
       coordinate, not a Glauber replacement.  Its nonlinear product term
       records correlated real--virtual soft radiation under a non-global
       measurement; hadron-hadron Glauber exchange, super-leading logarithms,
       and spectator entanglement remain separate proof coordinates in the
       relevant hard-process factorization statement.
8acb. Generalized TMD factorization for nearly back-to-back high-\(p_T\)
      hadron production is explicitly narrower than "change each Wilson line
      separately."  In the Rogers--Mulders spectator-model obstruction, the
      separate color-traced order-\(g\) anomaly vanishes, but the two-hadron
      color-entangled order-\(g^4\) Glauber contribution survives with the
      same sign across same/opposite cuts.  The gauge-theory graph is kept
      massless and regulated upstream by dimensional regularization plus
      off-lightcone Wilson-line rapidity directions; the finite numerical
      check is only a positive-denominator deformation of the reduced
      transverse skeleton.  With source-derived spectator mass functions, the
      \(l_{1\perp}\) and \(l_{2\perp}\) integrations reduce to positive scalar
      weights multiplying
      \(\epsilon_\perp(s_1,k_{1\perp})\epsilon_\perp(s_2,q_\perp-k_{1\perp})\);
      for \(s_1=s_2=\hat x\) and \(q_\perp=Q_T\hat x\) this gives a strictly
      negative integrated finite-window contribution.  The failure is of the
      separate-hadron generalized TMD ansatz; it does not by itself rule out
      inclusive collinear factorization, color-singlet Drell--Yan TMD
      factorization with its proof obligations, or process-specific joint
      Glauber/color-density coordinates.
8ad. Massive electroweak vector corrections to high-energy jet observables are
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
     assertion that Glauber exchanges cancel.  In the two-state rotation
     negative control, \(\Delta_G=(r_2-r_1)\sin^2\theta\), so a
     noncommuting measurement generically detects the exchange.
8c. Non-global angular measurements are not governed by a single linear soft
    anomalous dimension.  In a finite soft-dipole cell datum, unmeasured
    emissions are real--virtual balanced at first order but split the original
    dipole into two dipoles; differentiating the finite evolution at \(L=0\)
    yields the first non-global coefficient
    \(\sum_u K_{ij}^u(A_{iu}+A_{uj}-A_{ij})\).  A global-Sudakov-only ansatz
    has the correct first derivative but misses the second-order coefficient by
    one half of this path-decomposed cascade term; the additive boundary where
    each bracket vanishes is the negative control.
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
10aa. A finite-resolution EEC prediction is a tested functional statement on
      the binned calorimetric measure, with diagonal contact and endpoint atoms
      transported in the same convention as the short-distance chart.  The
      coordinate theorem supplies completeness of detector variables; dynamics
      enter through light-ray or hard/jet/soft coefficients,
      nonperturbative lifts, and a residual ledger that includes detector
      binning, contact, perturbative, factorization/Glauber,
      nonperturbative, track, and continuum/regulator errors.
10ab. A small-angle EEC endpoint prediction is not just a list of powers.
      The two-detector light-ray distribution must be pushed forward to
      \(\rho=1-\mathbf n_1\cdot\mathbf n_2\) with the angular Jacobian,
      extended across \(\rho=0\) with the declared plus/contact convention,
      and paired with detector tests.  Omitted light-ray labels, non-flat
      mixing transport, endpoint matching, nonperturbative lifts, and binning
      errors remain explicit residuals.
10ac. Local EEC endpoint charts must satisfy the global detector moment
      identities.  For selected weights \(\omega_r\), the endpoint atoms are
      fixed by the measured \(A_\omega=(\sum_r\omega_r z_r)^2\),
      \(B_\omega=|\sum_r\omega_r z_r\mathbf n_r|^2\), and the open-chart
      moments; full-calorimeter atoms or zeroth-moment-only repairs generally
      give the wrong measured observable.
10a. Shape functions are renormalized Wilson-line measurement coordinates.
     Their leading endpoint convolution preserves total weight and shifts the
     first event-shape moment by \(\Omega_1^e/Q\) only after the observable,
     Wilson-line orientation, regulator, and subtraction scheme are fixed.
     For \(C^2\) endpoint tests the next controlled term is bounded by
     \(\Omega_2^e\|f''\|_\infty/(2Q^2)\) times the perturbative total
     variation, so first-moment fits do not determine curved or localized
     endpoint smearings.
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
- 2026-06-05 issue #519 finite-resolution EEC assembly pass: added
  `ca:finite-resolution-eec-observable-assembly`, separating coordinate
  completeness from a physical QCD prediction.  The new block defines the
  detector-binned energy measure, proves the Lipschitz binning estimate, and
  requires contact/endpoint conventions, short-distance coefficient charts,
  nonperturbative lifts, and residual budgets to be transported together.
  The companion `energy_correlator_sum_rule_checks.py` now verifies the
  finite-resolution bound and a negative control where omitting the binning
  budget undercounts the measured residual.
- 2026-06-05 issue #519 measured-small-angle endpoint pass: added
  `ca:measured-small-angle-eec-endpoint-chart` so the jet/detector chapter now
  connects small-angle light-ray OPE data to measured EEC bins through the
  angular pushforward Jacobian, endpoint plus/contact convention, retained
  operator residuals, matching residuals, and nonperturbative lift.  The
  companion `energy_correlator_light_ray_ope_checks.py` now verifies the
  pushforward Jacobian and a negative control where omitting it underbudgets a
  measured bin.
- 2026-06-06 issue #519 measured EEC moment-closure pass: added
  `ca:measured-eec-global-moment-closure` so the local small-angle,
  back-to-back, and separated-angle endpoint charts are required to satisfy the
  same measured selected-energy zeroth and first moment identities.  The
  companion `energy_correlator_track_checks.py` now verifies the endpoint-only
  correction, its detector-test bound, and negative controls against
  full-calorimeter atoms and zeroth-only repair.
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
- 2026-06-01 issue #526/#630 distributional-factorization pass: added
  controlled approximation `ca:scet-distributional-factorization-estimate`,
  defining a leading-power factorization claim as a bound on smeared physical
  cross-section functionals and recording finite transform-space
  hard/jet/soft scheme covariance; extended
  `calculation-checks/scet_factorization_checks.py` with exact finite
  total-variation remainder and multiplicative scheme-covariance checks.
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
- 2026-06-05 issue #526/#630 non-global residual pass: upgraded the finite
  angular-cell datum from a coefficient identity to an observable-level
  factorization diagnostic, comparing the full soft-dipole expansion with a
  global-Sudakov-only ansatz, decomposing the missed term into
  unmeasured-to-measured paths, promoting
  `calculation-checks/qcd_non_global_log_checks.py` to an evidence-contract
  companion, and preserving the explicit boundary between BMS non-global soft
  evolution, Glauber exchange, and super-leading logarithms.
- 2026-06-04 issue #783 proof-status pass: replaced the remaining
  construction-overstating SCET language with conditional operator-coordinate
  language; added the fixed-regulator endpoint projection with a nonzero
  remainder and negative controls; added the factorization
  claim-status ledger tying SCET, QCD factorization, soft-drop, non-global,
  massive-vector, HQET/NRQCD, and thermal matching uses to explicit status
  categories; strengthened the finite Glauber obstruction with the two-state
  \((r_2-r_1)\sin^2\theta\) example; and promoted
  `calculation-checks/scet_factorization_checks.py` to a high-risk
  evidence-contract check.
- 2026-06-04 issue #819 SCET factorization-breaking pass: added the
  source-anchored Rogers--Mulders spectator-model color-entanglement
  calculation, including the measured high-\(p_T\) double-spin \(q_\perp\)
  setup, the precise separate-hadron generalized TMD ansatz ruled out,
  one-gluon trace-zero negative control, two-gluon entangled color factor,
  same/opposite cut eikonal sign accounting, fixed-\(q_\perp\) transverse
  integral, and narrower surviving factorization statements; replaced the
  broad claim-status ledger by an occurrence-level formula audit; and extended
  `calculation-checks/scet_factorization_checks.py` with finite SU(2)
  color/eikonal checks.  The integrated transverse check was added in the
  issue #826 pass below.
- 2026-06-04 issue #826 pass: replaced the fixed-recoil point sample by an
  integrated transverse obstruction witness.  The monograph introduced the
  compact finite window, positive Feynman-parameter reduction of the
  \(l_{1\perp},l_{2\perp}\) integrations, and sign-definite double-spin
  \(k_y^2\) contribution for a declared recoil/spin projection.  The #833
  pass below narrows the regulator interpretation and source-derives the
  model parameters.
- 2026-06-04 issue #833 spectator-regulator pass: re-audited the #826
  integrated witness and separated the massless Rogers--Mulders graph
  calculation from the finite positive-denominator deformation.  The monograph
  now uses dimensional regularization plus off-lightcone Wilson-line rapidity
  directions as the gauge-compatible graph regulator, displays the
  separate-hadron subtraction terms that vanish in the double-spin channel,
  derives \(L_i^2(x_i)\) and \(M_i(x_i)\) from one explicit spectator-model
  parameter point, bounds the Rogers--Mulders hard factor on the selected
  transverse window, and states that the compact integral is a nonzero witness
  for the reduced entangled skeleton, not a normalized gauge-theory observable.
  The companion check consumes the same source parameters and uses a
  conservative quadrature-error sign separation instead of an absolute
  numerical threshold.
- 2026-06-04 issue #828 occurrence-ledger completion: expanded the ledger to
  include the omitted triple-Regge, soft-QED, GPD/exclusive, and threshold
  rows; added explicit source locations and non-process homonym exclusions;
  corrected the finite non-global row so BMS soft evolution and Glauber
  exchange are separate coordinates; and extended
  `calculation-checks/scet_factorization_checks.py` with a source-label
  inventory guard for the ledger.
- 2026-06-04 issue #832 source-derived ledger pass: moved the occurrence audit
  classification out of the checker and into
  `planning/factorization_occurrence_manifest.tsv`; the companion check now
  mechanically scans manuscript labels, factorization-titled environments, and
  captions, failing if a candidate lacks a manifest disposition.  The ledger
  now has separate rows for the generic smeared SCET coordinate, perturbative
  soft-drop resummation with RG-consistency grouped as the same observable
  datum, the common QCD factorization budget with the DIS figure grouped as
  operator-coordinate evidence, and separate Abelian rows for the
  amplitude-level Weinberg soft theorem and inclusive Bloch--Nordsieck factor.
- 2026-06-04 issue #834 semantic occurrence pass: replaced the single
  unlabeled-search attestation row with
  `planning/factorization_textual_candidate_review.tsv`, a source-line review
  of section/paragraph titles and semantic prose windows around theorem-like
  environments.  The checker now scans those textual candidates, rejects stale
  or missing review rows, promotes included textual labels into
  `planning/factorization_occurrence_manifest.tsv`, and carries a synthetic
  negative control for an in-scope semantic factorization assertion whose
  label and environment title lack the lexical trigger.  The massive-vector
  electroweak Sudakov chart now has its own ledger status.
- 2026-06-05 issue #817 endpoint-positive-case pass: replaced the generic
  one-dimensional endpoint lemma from the #783 proof-status pass with a
  regulated color-singlet one-emission endpoint observable.  The monograph now
  starts from the finite Wilson-line/eikonal graph paired with the smeared
  event-shape measurement \(\varphi(u+v)\), derives finite endpoint
  projections, subtracts the constant endpoint projection, proves cancellation
  of an auxiliary allocation parameter, and bounds the finite mixed remainder.
  The later issue #840 pass below narrows the interpretation: these are soft
  endpoint projections, not collinear matrix elements or a hard-region
  derivation.
- 2026-06-05 issue #835 endpoint-graph repair: replaced the additive
  \((u+\lambda)(v+\lambda)\) graph identification by an actual off-light-cone
  Wilson-line cut graph with mixed denominators \((u+\delta v)(v+\delta u)\)
  and a separate finite endpoint slice \(u+v\ge\lambda\).  The monograph now
  derives the eikonal kernel from \(\beta_n=n+\delta\bar n\) and
  \(\beta_{\bar n}=\bar n+\delta n\), obtains soft endpoint Taylor projections
  by measurement expansion on the same regulated graph, and bounds the mixed
  finite-difference remainder in the same sliced observable.  The companion
  check verifies the graph kernel, rejects the old additive replacement,
  integrates the sliced domain by deterministic quadrature, and refreshes the
  textual factorization review anchors shifted by the new derivation.
- 2026-06-05 issue #840 soft-endpoint scope repair: corrected the
  one-emission endpoint block so the sliced domain
  \(0\le u,v\le\rho,\ u+v\ge\lambda\) is identified as a soft Wilson-line
  endpoint square rather than a domain containing energetic collinear regions.
  The TeX now states the SCET scalings explicitly, renames the local
  projections to \(S_u,S_v,S_0\), replaces the hard-region remainder by a mixed
  endpoint remainder, and leaves the full hard/collinear operator derivation as
  a separate factorization-theorem input.  The companion check now tests the
  mode scalings exactly: \(n\)-collinear has energetic \(\bar n\cdot k\),
  \(\bar n\)-collinear has energetic \(n\cdot k\), and hard has both
  components energetic, so none lies in the soft endpoint square.
- 2026-06-05 issue #526/#630 shape-function moment pass: added the smeared
  endpoint moment expansion after the leading shape-function convolution.  The
  pass shows precisely where \(\Omega_1^e/Q\) acts as a leading shift, where
  \(\Omega_2^e/Q^2\) enters the endpoint-curvature remainder, and why two
  fitted shape families with the same normalization and first moment need not
  agree on quadratic endpoint tests.  The companion shape-function check now
  verifies the second-order smeared expansion, same-first-moment/different-
  second-moment control, and wrong-scheme first-moment failure.
