# Volume IV, BV Master Formalism For Gauge Effective Actions Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.tex`.
- Compiled in Volume IV immediately after
  `chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Precedes QCD renormalization and anomaly chapters.
- Role in the monograph: replace the provisional Slavnov--Taylor source
  discussion by a full field-antifield framework for gauge-theory 1PI and
  Wilsonian effective actions.

## Source And Reference Controls

- Local source control:
  - preceding BRST chapter, especially the Slavnov--Taylor identity and the
    sources \(K^{a\mu},L^a\);
  - 253b generating-functional, 1PI, Wilsonian, and gauge-fixing blocks as
    already audited in the source-coverage register.
- External theorem-boundary controls:
  - `references/sound_references/barnich_brandt_henneaux_local_brst_cohomology_hep-th_0002245.txt`
    for antifields, local BRST cohomology, and counterterm/anomaly roles;
  - `references/sound_references/fredenhagen_rejzner_paqft_1208.1428.txt`
    for BV as a functional and perturbative algebraic framework.
- These references are used as boundary checks.  The chapter itself gives the
  definitions, master-equation nilpotency proof, gauge-fixing construction,
  and finite-dimensional BV pushforward argument.

## Framework

- Perturbative local gauge theory with regulator or local-jet algebra.
- Field set \(\Phi^A\) includes gauge potentials, ghosts, antighosts,
  Nakanishi--Lautrup variables, and matter fields.
- Antifields \(\Phi^*_A\) have opposite parity and ghost number
  \(-1-\operatorname{gh}(\Phi^A)\).
- Local functionals are understood modulo total derivatives when integrated.
- BV Laplacian and quantum master equation require a chosen regulator and
  measure.
- Yang--Mills is treated as the off-shell closed model case.  Open algebras
  and reducible symmetries are described in condensed field-space notation to
  display the additional antifield-number terms required by the master
  equation.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Phi^A\) | full set of fields, ghosts, nonminimal variables, and matter fields |
| \(\Phi^*_A\) | antifield paired with \(\Phi^A\) |
| \(\epsilon_A\) | Grassmann parity of \(\Phi^A\) |
| \(\mathcal F_{\rm BV}\) | graded algebra of local BV functionals |
| \((F,G)\) | BV antibracket |
| \(S_{\rm BV}\) | classical BV action |
| \(s_{\rm BV}\) | BV differential \((S_{\rm BV},\cdot)\) |
| \(S_{\rm min}\) | minimal BV action |
| \(S_{\rm nm}\) | nonminimal contractible-pair BV action |
| \(\Psi\) | gauge-fixing fermion |
| \(\mathcal L_\Psi\) | gauge-fixing Lagrangian submanifold |
| \(\Delta_{\rm BV}\) | regulator-dependent BV Laplacian |
| \(S_\Lambda\) | Wilsonian BV action at cutoff \(\Lambda\) |
| \(R^i{}_\alpha\) | gauge generator in condensed field-space notation |
| \(E_i\) | Euler--Lagrange derivative \(\delta S_0/\delta\Phi^i\) |
| \(C^\gamma{}_{\alpha\beta}\) | structure function for the gauge-generator commutator |
| \(M^{ij}{}_{\alpha\beta}\) | coefficient of equation-of-motion closure in an open gauge algebra |
| \(Z^\alpha{}_{a_1}\) | first-stage reducibility operator for gauge parameters |

## Claims Established

- The antibracket pairs each field with its antifield and has parity \(+1\)
  and ghost number \(+1\).
- A classical BV action is an even ghost-number-zero functional satisfying
  \(\frac12(S_{\rm BV},S_{\rm BV})=0\).
- The BV differential \(s_{\rm BV}=(S_{\rm BV},\cdot)\) is nilpotent by the
  odd Jacobi identity.
- The Yang--Mills minimal BV action couples antifields to the BRST variations
  \(sA=Dc\) and \(sc=-\frac12[c,c]\).
- Off-shell closure is stated as the field-space identity
  \(R_\beta^j\delta_jR_\alpha^i-R_\alpha^j\delta_jR_\beta^i
  =R_\gamma^iC^\gamma{}_{\alpha\beta}\).  Open closure is stated as the same
  identity plus an Euler--Lagrange term \(M^{ij}{}_{\alpha\beta}E_j\).
- The chapter explains why a linear antifield coupling gives only on-shell
  nilpotency for open algebras and why quadratic and higher antifield-number
  terms are required to solve the classical master equation off shell.
- Reducible symmetries are identified by \(R^i{}_\alpha Z^\alpha{}_{a_1}=0\)
  and require ghosts-for-ghosts and corresponding antifields.
- The nonminimal sector \((\bar c,B)\) and gauge-fixing fermion reproduce the
  Faddeev--Popov gauge-fixed action by restriction to a Lagrangian
  submanifold.
- The quantum master equation is the regulated statement
  \(\Delta_{\rm BV}\exp(\ii S/\hbar)=0\).
- The 1PI effective action satisfies \(\frac12(\Gamma,\Gamma)=0\) when the
  regularized measure and action obey the quantum master equation.
- The chapter now points back to
  `thm:all-order-slavnov-taylor-restoration`, identifying it as the
  gauge-fixed Yang--Mills form of the perturbative BV master-equation
  restoration theorem under vanishing ghost-number-one local obstruction.
- Finite-dimensional BV pushforward preserves the quantum master equation;
  this is the regulated core of the Wilsonian BV identity.
- Counterterms, anomalies, and physical operators are classified by local BV
  cohomology at ghost numbers \(0\), \(1\), and \(0\), respectively.

## Figure Requirements

- One framework diagram, `fig:bv-field-antifield-master-map`, ties fields,
  antifields, master equation, gauge fixing, and effective-action identities.
- The diagram is structural, not decorative: it records the dependency map
  used by the following gauge-theory chapters.

## Open Boundaries

- Global Gribov problems and nonperturbative BV integration cycles are not
  solved here.
- The cutoff-dependent Wilsonian master equation is stated at the framework
  level; later work should deepen explicit exact-RG realizations in gauge
  theory.
- 2026-05-24 issue #245 pass: replaced the opaque open-algebra sentence by
  explicit off-shell/open closure formulae, showed the equation-of-motion term
  that obstructs naive BRST nilpotency, and stated the associated reducible
  symmetry data.
- 2026-05-24 issue #267 pass: added an explicit cross-reference from the 1PI
  master equation to the all-order Slavnov--Taylor restoration theorem in the
  preceding BRST chapter.
