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
  - Khudaverdian's semidensity construction on odd symplectic supermanifolds
    and Schwarz's geometric BV quantization for the finite-dimensional
    theorem boundary behind the canonical half-density operator, restriction
    to Lagrangian submanifolds, and BV Stokes theorem.
- These references are used as boundary checks.  The chapter itself gives the
  definitions, master-equation nilpotency proof, gauge-fixing construction,
  and finite-dimensional BV pushforward argument.

## Framework

- Perturbative local gauge theory with regulator or local-jet algebra.
- Field set \(\Phi^A\) includes gauge potentials, ghosts, antighosts,
  Nakanishi--Lautrup variables, and matter fields.
- Antifields \(\Phi^*_A\) have opposite parity and ghost number
  \(-1-\operatorname{gh}(\Phi^A)\).
- Local functional derivatives are defined by the Euler operator after
  integration by parts, with boundary or compact-support assumptions stated.
- The antibracket is derived from the finite-regulator odd symplectic form
  \(\omega=\delta\Phi_A^*\,\delta\Phi^A\), and the Jacobi identity is traced
  to the graded Jacobi identity of Hamiltonian vector fields.
- The minimal BV complex is developed from Noether identities through the
  Koszul--Tate differential, ghosts, field antifields, and ghost antifields
  before specializing to Yang--Mills.
- Local functionals are understood modulo total derivatives when integrated.
- BV Laplacian and quantum master equation require a chosen finite-regulator
  odd symplectic space and a normal reference half-density \(\sigma_0\);
  the induced function Laplacian \(\Delta_{\sigma_0}\) is a divergence
  operator only after this datum has been fixed.
- Continuum Wilsonian effective actions for gauge theories are formulated as
  BV pushforwards with regulated bracket, half-density, Laplacian,
  integration cycle, and master action; the companion finite-cutoff route is a
  lattice gauge integral with compact link variables and gauge-invariant
  blocking maps.
- Yang--Mills is treated as the off-shell closed model case.  Open algebras
  and reducible symmetries are described in condensed field-space notation to
  display the additional antifield-number terms required by the master
  equation.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Phi^A\) | full set of fields, ghosts, nonminimal variables, and matter fields |
| \(\Phi^*_A\) | antifield paired with \(\Phi^A\) |
| \(B^a\) | Nakanishi--Lautrup even auxiliary integration variable in the nonminimal sector |
| \(\epsilon_A\) | Grassmann parity of \(\Phi^A\) |
| \(\mathcal F_{\rm BV}\) | graded algebra of local BV functionals |
| \(E_i\) | Euler--Lagrange derivative of a classical action |
| \(R^i{}_\alpha\) | gauge generator in condensed field-space notation |
| \(\delta_{\rm KT}\) | Koszul--Tate differential resolving the equations of motion |
| \((F,G)\) | BV antibracket |
| \(S_{\rm BV}\) | classical BV action |
| \(s_{\rm BV}\) | BV differential \((S_{\rm BV},\cdot)\) |
| \(S_{\rm min}\) | minimal BV action |
| \(S_{\rm nm}\) | nonminimal contractible-pair BV action |
| \(\Psi\) | gauge-fixing fermion |
| \(\mathcal L_\Psi\) | gauge-fixing Lagrangian submanifold |
| \(\iota_\Psi\) | embedding of the gauge-fixing Lagrangian submanifold |
| \(\sigma_0\) | normal reference BV half-density |
| \(\Delta_{1/2}\) | canonical BV operator on half-densities |
| \(\Delta_{\sigma_0}\) | divergence operator on functions induced by \(\sigma_0\) |
| \(D_{\sigma_0,\Psi}\Phi\) | density on \(\mathcal L_\Psi\) obtained by restricting \(\sigma_0\) |
| \(S_\Lambda\) | Wilsonian BV action at cutoff \(\Lambda\) |
| \(\mathcal L_{\Psi,\Lambda}\) | cutoff gauge-fixing Lagrangian submanifold |
| \(Z_{\Lambda,\Psi}[J]\) | gauge-fixed Wilsonian source functional obtained by restricting the BV half-density |
| \(C^\gamma{}_{\alpha\beta}\) | structure function for the gauge-generator commutator |
| \(M^{ij}{}_{\alpha\beta}\) | coefficient of equation-of-motion closure in an open gauge algebra |
| \(Z^\alpha{}_{a_1}\) | first-stage reducibility operator for gauge parameters |
| \(R_t\) | odd ghost-number \(-1\) generator of a BV-compatible infinitesimal exact-RG step |
| \(\rho_t\) | finite-regulator BV half-density \(\exp(\ii S_t/\hbar)\sigma_0\) in an RG family |
| \(s_\Psi\) | gauge-fixed BRST differential after restriction to the Lagrangian \(\Phi^*=\delta\Psi/\delta\Phi\) |
| \(h_{\rm nm}\) | contracting homotopy for the nonminimal BRST doublet |
| \(d_R^{abc}\) | symmetric cubic invariant controlling the local four-dimensional perturbative gauge anomaly |
| \(\operatorname{Obs}_\Lambda(U)\) | regulated BV cochain complex of quantum observables supported in \(U\) |
| \(Q_\Lambda\) | quantum BV observable differential \((S_\Lambda,\cdot)-\ii\hbar\Delta_\Lambda\) |
| \(W_{\Lambda\Lambda'}\) | homotopy-RG cochain map between observable complexes at two cutoffs |

## Claims Established

- The antibracket pairs each field with its antifield and has parity \(+1\)
  and ghost number \(+1\).
- The antibracket is the Hamiltonian bracket of the finite-regulator odd
  symplectic form; the biderivation and Jacobi identities are proved from
  Hamiltonian vector fields.
- A classical BV action is an even ghost-number-zero functional satisfying
  \(\frac12(S_{\rm BV},S_{\rm BV})=0\).
- The BV differential \(s_{\rm BV}=(S_{\rm BV},\cdot)\) is nilpotent by the
  odd Jacobi identity.
- Noether identities determine the first Koszul--Tate differential; closure
  and Jacobi data appear as successive antifield-number components of the
  classical master equation.
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
- The nonminimal \(B^a\) variable is explicitly part of the gauge-fixed BV
  integration sector, not an external source.  Its Gaussian integral is written
  out and shown to remove \(B\) from the remaining path integral while
  producing the standard covariant-gauge quadratic term.
- A half-density on the odd symplectic BV space restricts canonically to a
  Berezin density on every gauge-fixing Lagrangian submanifold; this is the
  precise finite-regulator meaning of the BV integration measure.
- The canonical Khudaverdian BV operator \(\Delta_{1/2}\) acts on
  half-densities; a normal reference half-density \(\sigma_0\) induces the
  function operator \(\Delta_{\sigma_0}\) used in the quantum master equation.
- The quantum master equation is the regulated half-density statement
  \(\Delta_{1/2}(\exp(\ii S/\hbar)\sigma_0)=0\), equivalently
  \(\frac12(S,S)-\ii\hbar\Delta_{\sigma_0}S=0\) for normal \(\sigma_0\).
- The equivalence between the half-density QME and its component form is
  derived using the second-order identity for the BV Laplacian.
- Gauge-fixed Wilsonian path-integral consistency is defined by restricting a
  cutoff BV half-density satisfying the quantum master equation to a
  gauge-fixing Lagrangian submanifold; cutoff Slavnov-Taylor identities are
  the gauge-fixed projection of this master equation.
- The 1PI effective action satisfies \(\frac12(\Gamma,\Gamma)=0\) when the
  regularized half-density integrand and action obey the quantum master
  equation.
- The chapter now points back to
  `thm:all-order-slavnov-taylor-restoration`, identifying it as the
  gauge-fixed Yang--Mills form of the perturbative BV master-equation
  restoration theorem under vanishing ghost-number-one local obstruction.
- Finite-dimensional BV pushforward preserves the quantum master equation;
  this is the regulated core of the Wilsonian BV identity.
- A BV-compatible infinitesimal exact-RG step has
  \(\partial_t\rho_t=\Delta_{1/2}(R_t\rho_t)\); \(\Delta_{1/2}^2=0\) then
  proves preservation of the quantum master equation.  In action coordinates
  this gives \(\partial_tS_t=(S_t,R_t)-\ii\hbar\Delta_{\sigma_0}R_t\).
- Continuum Wilsonian gauge-theory flow must preserve the gauge-fixed
  BV-consistency datum by BV pushforward of the cutoff half-density.
- Gauge-theory Wilsonian claims are routed through either BV finite-cutoff
  data or finite lattice gauge data, with any comparison stated through
  observables, BV cohomology classes, and a limiting topology.
- Counterterms, anomalies, and physical operators are classified by local BV
  cohomology at ghost numbers \(0\), \(1\), and \(0\), respectively.
- The gauge-fixed BRST complex for Yang--Mills with matter is obtained from
  the BV complex by a canonical transformation generated by \(\Psi\), followed
  by Lagrangian restriction and removal of the contractible nonminimal pair.
- Under Koszul--Tate acyclicity in positive antifield number, the local
  BV cohomology \(H^{g,D}(s_{\rm BV}\mid d)\) agrees with the gauge-fixed
  BRST cohomology \(H^{g,D}(s_\Psi\mid d)\) for \(g\ge0\).
- The ghost-number-zero renormalizable representatives are gauge-invariant
  covariant densities built from \(F_{\mu\nu}\), covariant derivatives, and
  matter fields, with the pure-gauge entries
  \(\frac14\operatorname{tr}F_{\mu\nu}F^{\mu\nu}\) and
  \(\frac14\operatorname{tr}F_{\mu\nu}\widetilde F^{\mu\nu}\) in the
  monograph trace convention.
- The ghost-number-one perturbative local gauge-anomaly class is represented
  by descent from \(\frac{\ii}{24\pi^2}\operatorname{Tr}_R\mathsf F^3\), and
  vanishes exactly when the total symmetric tensor \(d_R^{abc}\) vanishes in
  the chiral matter content.
- The local-observable side of perturbative BV is expressed as a regulated
  prefactorization algebra \(U\mapsto\operatorname{Obs}_\Lambda(U)\).  The
  QME implies \(Q_\Lambda^2=0\), disjoint-support products are cochain maps,
  and BV pushforward gives homotopy-RG cochain maps
  \(W_{\Lambda\Lambda'}\).

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
- 2026-05-24 issue #311 pass: inserted the finite-dimensional half-density
  framework for the BV integration measure, defined the canonical
  \(\Delta_{1/2}\), the normal datum \(\sigma_0\), the induced divergence
  operator \(\Delta_{\sigma_0}\), the restriction
  \(D_{\sigma_0,\Psi}\Phi=\iota_\Psi^*\sigma_0\), and rewrote the 1PI and
  Wilsonian BV integrals in semidensity form.
- 2026-05-24 issue #320 pass: declared the Nakanishi--Lautrup field \(B^a\) to
  be a nonminimal auxiliary integration variable and added its Gaussian
  elimination after BV gauge fixing.
- 2026-05-26 issue #583 pass: added the infinitesimal BV exact-RG theorem,
  the local BV--BRST comparison theorem for Yang--Mills, a renormalizable
  ghost-number-zero cohomology ledger, a ghost-number-one anomaly ledger, the
  local-observable/factorization-algebra boundary, and the companion
  `bv_master_algebra_checks.py` script for ghost-number, nilpotency, and
  doublet-homotopy algebra.
