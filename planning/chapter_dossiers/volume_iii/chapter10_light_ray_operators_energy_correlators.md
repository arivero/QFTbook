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
  \(\mathcal G_2(1,1;\Psi)=\langle\Psi|(P^0)^2|\Psi\rangle\), with
  bin-resolved diagonal contact measures rather than only a scalar total
  contact mass;
- the averaged null energy light-ray operator
  \(\mathcal A_n(x_\perp)\);
- the relation between calorimeter detectors and null-integrated stress-tensor
  light transforms;
- the embedding-space light transform
  \(\mathbb L[\mathcal O_{\Delta,J}]\) of a symmetric traceless primary, its
  homogeneity map \((\Delta,J)\mapsto(1-J,1-\Delta)\), and the convention
  check tying this map to the Euclidean conformal charge algebra and the
  separate radial real form used for Gram matrices;
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
  nonnegativity of the three spectral eigenvalues, with the fixed-total-energy
  normalization recorded as only the zeroth spherical moment rather than the
  positivity condition;
- the four-dimensional \(\mathcal N=1\) supersymmetric specialization
  \(t_4=0\), \(t_2=6(1-a/c)\), converting the helicity inequalities into
  \(1/2\le a/c\le 3/2\) with the free chiral and vector multiplets saturating
  opposite endpoints;
- the CFT energy-energy correlator and its relation to the QCD EEC;
- the light-ray OPE theorem boundary for separated-angle detector products,
  now accompanied by the distributional proof mechanism: transverse detector
  tests approaching the diagonal, coefficient distributions, transverse
  descendants, Lorentzian contour control, Regge/growth bounds, and the
  type of remainder estimate needed to turn the formal light-ray series into
  a convergent operator-distribution statement.
- finite CFT light-ray OPE charts: retained coefficient distributions,
  diagonal/contact extensions, induced center-coordinate tests, continuity
  estimates for retained light-ray quadratic forms, and a detector-test
  topology remainder bound.  The chapter now states explicitly that a finite
  retained representation list is not a controlled EEC approximation unless
  these chart and remainder data are supplied, and that retained-basis changes
  are distinct from diagonal-contact coordinate changes.
- one-parameter finite chart transport: a basis velocity
  \(A_s=B_s^{-1}\partial_sB_s\) acts with opposite signs on retained
  light-ray columns and coefficient rows, while a moving diagonal-extension
  row requires a matching derivative of the explicit contact coordinate.
- endpoint distribution charts in the one-variable EEC coordinate
  \(z=(1-\cos\chi)/2\), including subtracted extensions of singular
  small-angle densities, explicit \(\delta^{(j)}(z)\) contact coordinates,
  and the endpoint-resolution shift that fixes the sign of contact
  coordinate changes.

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
| \(a,c\) | four-dimensional trace-anomaly coefficients used in the \(\mathcal N=1\) supersymmetric collider specialization |
| \(\mathcal V_2,\mathcal V_1,\mathcal V_0\) | helicity \(2,1,0\) subspaces of the symmetric traceless polarization space relative to a detector direction |
| \(\lambda_2,\lambda_1,\lambda_0\) | detector quadratic-form eigenvalues in the helicity \(2,1,0\) sectors |
| \(\mathrm{EEC}_\Psi(\chi)\) | normalized energy-energy correlator in state \(\Psi\) |
| \(\mathbb L_\alpha\) | light-ray operator appearing in the light-ray OPE |
| \(\mathfrak A_N\) | finite retained label set in a CFT light-ray OPE chart |
| \(C_{\alpha,m}\) | relative-coordinate coefficient distribution in a finite light-ray OPE chart |
| \(\psi_{\alpha,m,\Phi}\) | center-coordinate test induced from a two-detector test \(\Phi\) by \(C_{\alpha,m}\) |
| \(R_N(\Phi;\Psi)\) | finite-chart light-ray OPE remainder functional in state \(\Psi\) |
| \(B_s\), \(A_s\) | one-parameter finite chart basis change and velocity \(A_s=B_s^{-1}\partial_sB_s\) |
| \(d_{s,\Phi}\), \(k_{s,\Phi}\) | diagonal-extension shift row and matching explicit contact coordinate in a moving finite chart |
| \(z=(1-\cos\chi)/2\) | small-angle EEC endpoint coordinate |
| \([f]_{J,z_0,+}\) | Taylor-subtracted endpoint extension of a singular one-variable density |
| \(K_j^{(N)}\) | explicit endpoint contact coordinate multiplying \(\delta^{(j)}(z)\) |

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
   partitions of detector labels.  The constant-detector Ward identity fixes
   only the total diagonal mass; localized calorimeter bins require the
   measure-valued contact distribution along the diagonal.
6. The averaged null energy operator is the null-line version of the
   calorimetric energy detector after conformal compactification.
7. The light-transform weight map is derived from embedding-space
   homogeneity and change of null-line integration variable.  Its signs are
   tied to the Euclidean conformal charge algebra and the radial real form is
   obtained by the separate Lorentzian-to-radial generator map used in the
   Gram-matrix chapters.  Existence of the corresponding operator is kept
   separate as a Lorentzian analyticity/growth hypothesis.
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
   \(t_2,t_4\) normal form.  The total-energy normalization fixes the average
   angular flux, while the positivity claim requires all three sector
   inequalities.
10a. In four-dimensional \(\mathcal N=1\) SCFTs, the supercurrent Ward
     identity gives \(t_4=0\), \(t_2=6(1-a/c)\).  The same helicity
     eigenvalues therefore become
     \(2a/c-1\), \(2-a/c\), and \(3-2a/c\), yielding
     \(1/2\le a/c\le3/2\) after the stress-tensor normalization is transported.
11. The CFT EEC and the QCD EEC are the same detector construction with
   different dynamical state spaces.
12. The convergent light-ray OPE is used with explicit Lorentzian CFT
   hypotheses rather than treated as a general axiom of QFT.  The chapter now
   records the proof mechanism and the needed transverse-distribution
   convergence estimate, and separates the fixed-point CFT statement from the
   renormalized QCD small-angle EEC factorization datum.
13. A finite light-ray OPE chart for detector products must state coefficient
    distributions, their diagonal extensions, induced center tests, continuity
    of retained light-ray forms, and a remainder functional.  Separated-angle
    chart data alone do not determine the full detector moment with contact
    terms.
14. Retained-basis changes and diagonal-contact reshufflings are different
    coordinate operations in a finite light-ray OPE chart.  Basis changes obey
    row/column covariance of the retained finite vector space.  Adding
    diagonal distributions to retained coefficient maps changes the full
    detector distribution unless the explicit contact coordinate is shifted
    by the corresponding retained light-ray matrix element.
15. A one-parameter finite chart transport differentiates this covariance:
    \(A_s=B_s^{-1}\partial_sB_s\) gives
    \(\partial_s\ell_s=-A_s\ell_s\) and
    \(\partial_sc_s=c_sA_s+(\partial_sd_s)B_s\), while
    \(\partial_sk_s=-(\partial_sd_s)B_s\ell_s\).  These identities preserve
    \(c_s\ell_s+k_s\) and are fixed-point chart identities, not QCD anomalous
    dimensions.
16. The small-angle EEC distribution is the angular pushforward of the
    two-detector light-ray distribution.  The kernel
    \(\delta(\cos\chi-\cos\theta)\) contributes the Jacobian
    \((\sin\chi)^{D-4}\); a retained coefficient homogeneous of degree
    \(-\lambda\) therefore contributes \(\chi^{D-4-\lambda}\) in the
    \(\chi\)-density, with the leading exponent halved in
    \(z=(1-\cos\chi)/2\).
17. The pushed-forward small-angle density must be extended across
    \(z=0\) as a distribution with explicit endpoint contact coordinates.
    Separated-angle light-ray coefficients do not determine those contacts;
    changing the endpoint resolution interval shifts the explicit
    \(\delta(z)\) coordinate by the annulus constant so that the
    constant-detector Ward identity is preserved.

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
  measures.  It also checks the bin-resolved diagonal contact distribution:
  a shifted contact measure can preserve \(\mathcal G_2(1,1)\) while changing
  a localized same-bin detector product.  It also checks the finite light-ray
  OPE chart bound from coefficient-map norms, light-ray form bounds, and a
  declared remainder, and detects the separated-angle-only loss of the
  diagonal contact coordinate;
  the same script checks retained-basis covariance and the compensating
  contact-coordinate shift under diagonal-distribution reshuffling, together
  with the one-parameter finite-chart transport equation and its wrong-sign
  contact defect.  It also checks the one-variable endpoint
  distribution-gluing sign: moving a
  small-angle annulus from the bulk representative into the endpoint plus
  chart requires a positive contact-coordinate shift by the annulus constant,
  while the opposite sign changes the constant-detector moment.
- 2026-06-06 issue #725 detector-contact evidence-contract pass: promoted
  `cft_energy_detector_contact_checks.py` to an extended evidence contract and
  added the bin-resolved contact-distribution control.  The pass records that
  the finite companion imports detector existence, one-detector positivity,
  detector-product domains, diagonal distributional extensions, and the
  Lorentzian light-ray OPE theorem boundary; the exact rational checks only
  guard the finite partition/contact/chart algebra after those QFT inputs have
  been supplied.
- 2026-06-03 #519 finite-chart transport pass: added the
  one-parameter CFT light-ray chart transport equations and paired exact
  rational checks for row/column covariance, moving diagonal-extension rows,
  and the contact-coordinate derivative sign.
- The finite helicity reduction of the four-dimensional collider bounds is
  checked by `calculation-checks/conformal_collider_checks.py`, together with
  the full helicity-projector spectral decomposition of a generic polarization,
  the \(\mathcal N=1\) supersymmetric \(a/c\) specialization and endpoint
  multiplet checks, adversarial controls showing that average-energy
  normalization and any two-helicity shortcut miss negative-flux polarizations,
  the finite arithmetic for the light-transform homogeneity map, the null-cut
  modular ANEC sign bookkeeping with a one-sided-cut counterexample, and the
  transverse homogeneity ledger for light-ray OPE coefficient distributions.
- The conformal-algebra sign convention behind the light transform is checked
  by `calculation-checks/conformal_light_transform_algebra_checks.py`, which
  verifies the Euclidean conformal Killing vector bracket table, the
  \(U(s)=\exp(i sQ)\) charge sign conversion, the radial real-form conversion,
  and the resulting \((\Delta,J)\mapsto(1-J,1-\Delta)\) weight map.
- 2026-06-02 conformal-collider spectral-diagonalization pass: upgraded the
  Hofman--Maldacena positivity derivation from testing representatives in the
  three little-group sectors to a displayed orthogonal spectral decomposition
  of the detector quadratic form on the full symmetric-traceless polarization
  space.  The companion check verifies the generic rational decomposition.
- 2026-06-06 issue #519 supersymmetric collider central-charge pass: added
  the four-dimensional \(\mathcal N=1\) specialization
  \(t_4=0,\ t_2=6(1-a/c)\) after the Hofman--Maldacena helicity inequalities.
  The new paragraph converts the detector eigenvalues to
  \(2a/c-1\), \(2-a/c\), and \(3-2a/c\), deriving
  \(1/2\le a/c\le3/2\) and identifying the free chiral/vector endpoint
  saturations.  The companion check verifies the rational map, the two endpoint
  multiplets, and normalization mistakes that would hide the endpoint
  saturations.
- 2026-06-06 issue #725 conformal-collider evidence-contract pass: promoted
  `conformal_collider_checks.py` to an extended evidence contract and added
  adversarial finite controls for the two common shortcuts in this section:
  treating the fixed total energy as positivity, and checking only two of the
  three helicity sectors.  The pass also records the companion's imported
  physics inputs: ANEC, the null-infinity/bounded-extension detector bridge,
  the Wightman/Ward derivation of the \(t_2,t_4\) normal form, and the
  \(\mathcal N=1\) supercurrent Ward identity.
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
- 2026-06-02 #519 finite light-ray chart pass: inserted the finite CFT
  light-ray OPE chart after the theorem-boundary remainder paragraph.  The
  pass states the retained coefficient distributions, diagonal extension,
  induced center-coordinate tests, light-ray form continuity estimates, and
  detector-test remainder bound needed before a truncated light-ray expansion
  is a controlled approximation to an EEC distribution.  The companion finite
  detector/contact script checks the displayed finite bound and the failure
  of a separated-angle-only chart to determine the contact coordinate.
- 2026-06-02 #519 finite chart covariance/contact pass: added the retained
  finite chart formula \(V_\Psi(\Phi)=c_\Phi\ell_\Psi+k_\Phi+R_N\), separated
  retained-basis covariance from diagonal-contact reshuffling, and recorded
  that a Ward identity fixes only the full constant-detector moment rather
  than a separated-angle coefficient convention.  The companion exact rational
  check verifies \(cB\,B^{-1}\ell=c\ell\), the compensating shift
  \(k\mapsto k-d\ell\), and the unshifted-contact defect \(16/15\).
- 2026-06-02 #519 small-angle EEC pushforward pass: added the missing
  geometric step from a local relative-coordinate light-ray OPE coefficient to
  the one-variable EEC density.  The manuscript derives the
  \((\sin\chi)^{d_\perp-2}\) factor from the
  \(\delta(\cos\chi-\cos\theta)\) kernel and records the resulting
  \(\chi^{d_\perp-2-\lambda}\) power for a homogeneous coefficient of degree
  \(-\lambda\), including the \(z=(1-\cos\chi)/2\) exponent conversion.  The
  companion check verifies the finite exponent arithmetic and detects the
  one-power difference from a \(\delta(\chi-\theta)\) convention.
- 2026-06-02 #519 CFT endpoint distribution-chart pass: added the
  Taylor-subtracted endpoint extension \([f]_{J,z_0,+}\), the finite
  one-variable endpoint chart with explicit \(\delta^{(j)}(z)\) contacts,
  and the \(D_{z_b}=D_{z_a}+\mathbf1_{z_a<z<z_b}/z-\log(z_b/z_a)\delta(z)\)
  resolution-shift identity.  The pass makes the CFT light-ray endpoint
  contact logic self-contained instead of relying on the QCD chapter's
  running-coupling endpoint convention.
