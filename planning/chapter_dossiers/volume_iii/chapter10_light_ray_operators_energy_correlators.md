# Volume III, Chapter 10 Dossier: Light-Ray Operators And Energy Correlators

## Logical Role

- Role in the monograph: introduce nonlocal detector observables in CFT after
  local operator structure and the OPE have been developed, and connect them
  to the gauge-theory energy correlators of the QCD chapter.
- Immediate predecessor: operator product expansion.
- Immediate successor: later CFT developments on crossing, Lorentzian
  inversion, and special structures.

## Source And Reference Controls

- `SRC-EXTERNAL-HOFMAN-MALDACENA`: conformal collider energy and charge
  correlations, used for the stress-tensor-state one-point energy flux normal
  form and the \(t_2,t_4\) positivity inequalities.
- `SRC-EXTERNAL-ANEC-MODULAR`: Faulkner--Leigh--Parrikar--Wang's
  deformed-half-space modular Hamiltonian proof of ANEC, used as the theorem
  boundary for the relative-entropy monotonicity derivation.
- `SRC-EXTERNAL-ANEC-CAUSALITY`: Hartman--Kundu--Tajdini's Lorentzian
  causality proof of ANEC, used as the theorem boundary for the Regge
  analyticity sign argument.
- `SRC-EXTERNAL-LIGHT-RAY-OPE`: Kologlu--Kravchuk--Simmons-Duffin--Zhiboedov,
  used as theorem boundary for the convergent light-ray OPE under Lorentzian
  CFT hypotheses.
- `SRC-EXTERNAL-LIGHT-TRANSFORM`: Caron-Huot and
  Kravchuk--Simmons-Duffin light-transform formalism, used for the
  embedding-space definition of the light transform and the
  \((\Delta,J)\mapsto(1-J,1-\Delta)\) representation-theoretic weight map.
- `SRC-INTERNAL-QCD-DETECTORS`: Volume IV QCD detector-observable section,
  used to keep the CFT and QCD definitions of energy correlators aligned.

## Definitions And Results

The chapter establishes:

- normalizable collider states as wavepacket-smeared local-operator states;
- the CFT energy detector \(\mathcal E(f)\) as a stress-tensor flux limit at
  future null infinity;
- the statewise positive detector measure \(\mu_\Psi\) obtained from the
  detector quadratic form by the Riesz representation theorem, together with
  the finite-bin Cauchy--Schwarz inequalities that follow from one-detector
  positivity;
- angular moment data for \(\mu_\Psi\) on the compact detector sphere and the
  compact moment-reconstruction criterion: a positive finite moment functional
  on a uniformly dense separating angular algebra extends uniquely to a
  finite positive Borel measure, while finite moment lists remain
  finite-resolution projections;
- \(k\)-point energy correlators as distributions on \((S^{D-2})^k\);
- finite positive-measure detector products, their off-diagonal and diagonal
  contact decomposition, the partition stratification of \(k\)-detector
  contacts, and the Ward identity
  \(\mathcal G_2(1,1;\Psi)=\langle\Psi|(P^0)^2|\Psi\rangle\);
- the averaged null energy light-ray operator
  \(\mathcal A_n(x_\perp)\);
- the relation between calorimeter detectors and null-integrated stress-tensor
  light transforms;
- the embedding-space light transform
  \(\mathbb L[\mathcal O_{\Delta,J}]\) of a symmetric traceless primary and
  its homogeneity map \((\Delta,J)\mapsto(1-J,1-\Delta)\);
- the smeared ANEC quadratic form \(\mathcal A_n(\varphi)\), its Lorentzian
  CFT hypotheses, and the modular/causal proof mechanisms that fix the sign;
- the one-sided null-cut modular-variation formulas for a deformed half-space
  and its complement, together with the entropy-variation squeeze whose
  compatibility gives the full null-generator ANEC inequality;
- the ANEC-to-detector bridge: positivity for smooth transverse null-plane
  tests must be supplemented by conformal null-infinity limiting and bounded
  extension to \(C(S^{D-2})\) before it becomes a statewise angular detector
  measure; detector products still require separate domain/contact data;
- the reduction from ANEC positivity to positivity of the conformal-collider
  angular energy distribution;
- the four-dimensional stress-tensor one-point energy flux form with
  parameters \(t_2,t_4\);
- the helicity \(2,1,0\) spectral decomposition of the stress-tensor
  detector quadratic form, and the conformal-collider inequalities as the
  nonnegativity of the three spectral eigenvalues;
- the CFT energy-energy correlator and its relation to the QCD EEC;
- the light-ray OPE theorem boundary for separated-angle detector products,
  now accompanied by the distributional proof mechanism: transverse detector
  tests approaching the diagonal, coefficient distributions, transverse
  descendants, Lorentzian contour control, Regge/growth bounds, and the
  type of remainder estimate needed to turn the formal light-ray series into
  a convergent operator-distribution statement.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(D\) | spacetime dimension of the CFT |
| \(S^{D-2}\) | celestial sphere of detector directions |
| \(\mathbf n\) | unit spatial detector direction |
| \(n^\mu=(1,\mathbf n)\) | future null vector associated to \(\mathbf n\) |
| \(f\) | smooth angular detector test function |
| \(\mathcal E(f)\), \(\mathcal E(\mathbf n)\) | smeared and distributional energy detector |
| \(\mathcal G_k\) | \(k\)-point energy correlator |
| \(\mu_\Psi\) | statewise positive finite detector measure associated to a finite-energy collider state \(\Psi\) |
| \(\mathcal P=\{B_a\}\) | finite Borel partition of the detector sphere used for finite-resolution calorimetry |
| \(\mathcal A_{\rm ang}\) | uniformly dense separating real angular algebra used for detector moments |
| \(m_\Psi(a)\) | angular moment \(\int a\,\dd\mu_\Psi\) of the statewise detector measure |
| \(\varepsilon_X\) | finite positive calorimetric measure associated to a detector configuration |
| \(\mathsf P_k\) | set of partitions of \(k\) detector labels, indexing diagonal contact strata |
| \(\mathcal A_n(x_\perp)\) | averaged null energy operator on a null line |
| \(P,Z\) | embedding-space null point and auxiliary polarization vectors |
| \(\mathcal O_{\Delta,J}(P,Z)\) | symmetric traceless primary encoded in embedding space |
| \(\mathbb L[\mathcal O_{\Delta,J}]\) | light transform of a local primary, when the Lorentzian integral is defined |
| \(N_n=n^\perp/\mathbb R n\) | transverse quotient to the null direction \(n\) |
| \(\varphi\) | compactly supported nonnegative test function on \(N_n\) |
| \(\mathcal A_n(\varphi)\) | transversely smeared ANEC quadratic form |
| \(x^\pm=x^0\pm x^1\), \(y\) | light-cone and transverse coordinates used in the modular proof mechanism |
| \(R_f\), \(K_f\) | null-cut domain of dependence and its vacuum modular Hamiltonian |
| \(t_2,t_4\) | parity-even four-dimensional stress-tensor three-point coordinates in conformal collider normalization |
| \(\mathcal V_2,\mathcal V_1,\mathcal V_0\) | helicity \(2,1,0\) subspaces of the symmetric traceless polarization space relative to a detector direction |
| \(\lambda_2,\lambda_1,\lambda_0\) | detector quadratic-form eigenvalues in the helicity \(2,1,0\) sectors |
| \(\mathrm{EEC}_\Psi(\chi)\) | normalized energy-energy correlator in state \(\Psi\) |
| \(\mathbb L_\alpha\) | light-ray operator appearing in the light-ray OPE |

## Claim Ledger

1. Energy detector operators require a stated null-infinity limit hypothesis as
   quadratic forms on collider states.
2. For a fixed finite-energy state, detector positivity and
   \(\mathcal E(1)=P^0\) give a bounded positive functional on angular tests,
   hence a statewise finite positive measure by Riesz; operator-valued-measure
   structure and product positivity require additional domain and
   polarization data.
3. Complete detector moments on a uniformly dense angular algebra determine
   the statewise detector measure uniquely by bounded positive extension to
   \(C(S^{D-2})\) and Riesz--Markov uniqueness.  Finite moment truncations
   are finite-resolution projections and must not be treated as complete
   detector data.
4. Finite detector partitions approximate the statewise positive measure only
   with a stated resolution estimate: for Lipschitz test functions the error
   is bounded by the partition diameter times the Lipschitz constant and total
   detector mass, and the corresponding \(k\)-detector statement uses the
   product metric and the total \(k\)-detector mass.  These bounds are
   finite-resolution consequences of an already constructed positive measure;
   the construction of detector products remains the separate domain question.
5. Energy correlators are distributions; coincident detector directions carry
   contact terms whose finite positive-measure model is the diagonal
   decomposition of detector product measures, indexed for \(k\) insertions by
   partitions of detector labels.
6. The averaged null energy operator is the null-line version of the
   calorimetric energy detector after conformal compactification.
7. The light-transform weight map is derived from embedding-space
   homogeneity and change of null-line integration variable; existence of the
   corresponding operator is kept separate as a Lorentzian analyticity/growth
   hypothesis.
8. ANEC positivity is recorded as a theorem boundary with explicit
   Lorentzian CFT hypotheses, a transversely smeared quadratic form, and the
   modular/causal proof mechanisms stated at the level needed for collider
   applications.  The modular route displays the region/complement
   relative-entropy derivative inequalities and the common entropy-variation
   squeeze, so the sign of the full null integral is not hidden in the phrase
   "entropy variations cancel."
9. ANEC positivity for smooth transverse tests is not by itself a Borel
   detector-bin construction.  The chapter now requires the null-infinity
   limiting map and a bounded positive extension from smooth angular tests to
   \(C(S^{D-2})\), after which Riesz--Markov gives the statewise detector
   measure.  Products of detectors remain a separate domain/contact-extension
   problem.
10. Positivity of the energy detector in the stress-tensor collider state is
   equivalent to nonnegativity of the three helicity-sector eigenvalues of
   the detector quadratic form; these are precisely the displayed
   Hofman--Maldacena inequalities once the one-point function is put in
   \(t_2,t_4\) normal form.
11. The CFT EEC and the QCD EEC are the same detector construction with
   different dynamical state spaces.
12. The convergent light-ray OPE is used with explicit Lorentzian CFT
   hypotheses rather than treated as a general axiom of QFT.  The chapter now
   records the proof mechanism and the needed transverse-distribution
   convergence estimate, and separates the fixed-point CFT statement from the
   renormalized QCD small-angle EEC factorization datum.

## Figures

- Detector-at-null-infinity figure: local operator creates a state, energy
  flux reaches a calorimeter direction on \(S^{D-2}\).
- Null-line/light-ray figure: conformal map between a null generator and a
  detector at future null infinity.
- Conformal-collider polarization figure: helicity \(2,1,0\) stress-tensor
  polarizations relative to a detector direction.
- Energy-energy correlator figure: two detectors at opening angle \(\chi\)
  with coincidence locus marked.

## Checks

- Do not import AdS/CFT, supersymmetry, or integrability as part of the core
  CFT energy-correlator construction.
- Keep all sharp-momentum collider states as wavepacket limits.
- Do not conflate contact terms in detector products with counterterms in a
  regulated action.
- Keep theorem boundaries visible for ANEC positivity and the light-ray OPE.
- The finite detector-contact partition algebra is checked by
  `calculation-checks/cft_energy_detector_contact_checks.py`, which now also
  checks the statewise Riesz bound and finite-bin Cauchy--Schwarz positivity
  that precede detector products, together with finite-grid compact moment
  reconstruction, a truncated-moment ambiguity example, and finite-resolution
  Lipschitz partition estimates for one-detector and detector-product
  measures.
- The finite helicity reduction of the four-dimensional collider bounds is
  checked by `calculation-checks/conformal_collider_checks.py`, together with
  the full helicity-projector spectral decomposition of a generic polarization,
  the finite arithmetic for the light-transform homogeneity map, the null-cut
  modular ANEC sign bookkeeping, and the transverse homogeneity ledger for
  light-ray OPE coefficient distributions.
- 2026-06-02 conformal-collider spectral-diagonalization pass: upgraded the
  Hofman--Maldacena positivity derivation from testing representatives in the
  three little-group sectors to a displayed orthogonal spectral decomposition
  of the detector quadratic form on the full symmetric-traceless polarization
  space.  The companion check verifies the generic rational decomposition.
- 2026-06-02 anti-wrapper follow-up: demoted the separate
  Hofman--Maldacena-inequalities proposition/proof shell.  The substantive
  result is the preceding spectral diagonalization; the inequalities are now
  presented as its immediate positivity consequence rather than as an
  additional theorem-family claim.
- 2026-05-29 seventh anti-wrapper pass: expanded the conformal-collider
  inequality proof so the \(SO(2)\) helicity decomposition, Schur
  diagonalization of the quadratic form, and three polarization eigenvalues
  are visible rather than hidden in a substitution.
- 2026-06-02 #519 ANEC bridge pass: inserted a non-theorem paragraph after the
  modular ANEC derivation explaining the extra bounded-extension step needed
  to turn smooth transverse ANEC positivity into the statewise angular
  detector measure.  The pass keeps one-detector positivity, Riesz measure
  construction, and \(k\)-detector product/contact data as separate
  mathematical layers.
