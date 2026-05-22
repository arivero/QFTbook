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

## Claims Established

- The antibracket pairs each field with its antifield and has parity \(+1\)
  and ghost number \(+1\).
- A classical BV action is an even ghost-number-zero functional satisfying
  \(\frac12(S_{\rm BV},S_{\rm BV})=0\).
- The BV differential \(s_{\rm BV}=(S_{\rm BV},\cdot)\) is nilpotent by the
  odd Jacobi identity.
- The Yang--Mills minimal BV action couples antifields to the BRST variations
  \(sA=Dc\) and \(sc=-\frac12[c,c]\).
- The nonminimal sector \((\bar c,B)\) and gauge-fixing fermion reproduce the
  Faddeev--Popov gauge-fixed action by restriction to a Lagrangian
  submanifold.
- The quantum master equation is the regulated statement
  \(\Delta_{\rm BV}\exp(\ii S/\hbar)=0\).
- The 1PI effective action satisfies \(\frac12(\Gamma,\Gamma)=0\) when the
  regularized measure and action obey the quantum master equation.
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

- Reducible gauge symmetries and open algebras are only described by their BV
  requirement: additional ghosts and higher antifield terms are needed.
- Global Gribov problems and nonperturbative BV integration cycles are not
  solved here.
- The cutoff-dependent Wilsonian master equation is stated at the framework
  level; later work should deepen explicit exact-RG realizations in gauge
  theory.
