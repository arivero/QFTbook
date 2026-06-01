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
- the reduction from ANEC positivity to positivity of the conformal-collider
  angular energy distribution;
- the four-dimensional stress-tensor one-point energy flux form with
  parameters \(t_2,t_4\);
- the conformal-collider inequalities following from detector positivity;
- the CFT energy-energy correlator and its relation to the QCD EEC;
- the light-ray OPE theorem boundary for separated-angle detector products.

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
| \(\mathrm{EEC}_\Psi(\chi)\) | normalized energy-energy correlator in state \(\Psi\) |
| \(\mathbb L_\alpha\) | light-ray operator appearing in the light-ray OPE |

## Claim Ledger

1. Energy detector operators require a stated null-infinity limit hypothesis as
   quadratic forms on collider states.
2. Energy correlators are distributions; coincident detector directions carry
   contact terms whose finite positive-measure model is the diagonal
   decomposition of detector product measures, indexed for \(k\) insertions by
   partitions of detector labels.
3. The averaged null energy operator is the null-line version of the
   calorimetric energy detector after conformal compactification.
4. The light-transform weight map is derived from embedding-space
   homogeneity and change of null-line integration variable; existence of the
   corresponding operator is kept separate as a Lorentzian analyticity/growth
   hypothesis.
5. ANEC positivity is recorded as a theorem boundary with explicit
   Lorentzian CFT hypotheses, a transversely smeared quadratic form, and the
   modular/causal proof mechanisms stated at the level needed for collider
   applications.
6. Positivity of the energy detector implies the displayed
   Hofman--Maldacena inequalities once the one-point function is put in
   \(t_2,t_4\) normal form.
7. The CFT EEC and the QCD EEC are the same detector construction with
   different dynamical state spaces.
8. The convergent light-ray OPE is used with explicit Lorentzian CFT
   hypotheses rather than treated as a general axiom of QFT.

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
  `calculation-checks/cft_energy_detector_contact_checks.py`.
- The finite helicity reduction of the four-dimensional collider bounds is
  checked by `calculation-checks/conformal_collider_checks.py`, together with
  the finite arithmetic for the light-transform homogeneity map.
- 2026-05-29 seventh anti-wrapper pass: expanded the conformal-collider
  inequality proof so the \(SO(2)\) helicity decomposition, Schur
  diagonalization of the quadratic form, and three polarization eigenvalues
  are visible rather than hidden in a substitution.
