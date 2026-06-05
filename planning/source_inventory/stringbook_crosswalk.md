# String Book Crosswalk

Source snapshot for this crosswalk:

- Source repository: `xiyin137/stringbook`.
- Audited source revision: `9fbd771d17945ce502ee030fdb7936061cef01d6`
  (`main`; reachable at
  `https://github.com/xiyin137/stringbook/commit/9fbd771d17945ce502ee030fdb7936061cef01d6`).
- QFT monograph repository baseline reviewed against this source snapshot:
  `259a2005c84b64e5f23a12e065cf5ff69ce956f6`; the present crosswalk update
  records the resulting #745 reproducibility ledger.
- Primary source anchors are repository-relative paths:
  `texsource/string notes.tex` and `codes/*.nb`.  The generated
  `texsource/string notes.toc` in the audited checkout was used only as an
  extraction aid; source citations below point back to the TeX source line
  ranges.
- Older generated extraction aids under `PhysicsLogic/docs/stringbook/` may be
  useful for comparison, but they are not authoritative for this QFT monograph
  crosswalk because their last recorded inventory predates the current
  stringbook source head.
- Current companion-notebook inventory at the audited source revision: 18
  Mathematica notebooks in `codes/`, as listed in the notebook table below.
- Reproducibility verification on 2026-06-04: a fresh clone of
  `https://github.com/xiyin137/stringbook.git` resolved
  `9fbd771d17945ce502ee030fdb7936061cef01d6` as `HEAD`, `git cat-file -t`
  returned `commit`, `git ls-tree -r --name-only <sha> -- codes` listed the 18
  notebooks below, and
  `git show <sha>:'texsource/string notes.tex' | wc -l` returned `24946`.
  The formerly pinned local-only commit
  `4262f9c821859ace1b6ee43b31afa72fc1542ecd` has identical tree objects for
  the authoritative anchors (`texsource/string notes.tex` and `codes/`) to the
  reachable commit above, so the notebook and prose inventories below are
  repinned without changing their source content.  The prose-section inventory
  below was rerun against this reachable 24,946-line TeX source; all recorded
  source ranges remain inside the verified file.

The string book is an adjacent high-value source. It may supply mature
appendix material, examples, convention checks, and source leads for any
QFT-relevant topic. It is not an import source in the ordinary textbook sense:
the QFT monograph must give an independent development, with its own order,
definitions, hypotheses, proofs, examples, and external reference boundaries.

The stringbook may inspire what to include and may help detect convention
conflicts. It must not determine the monograph's exposition, chapter sequence,
or theorem status.

Coverage directive: essentially all purely QFT content in the stringbook is
source-coverage material for the QFT monograph.  The material is not to be
copied or treated as authoritative prose; it must be rebuilt in the monograph
with independent definitions, hypotheses, derivations, convention checks, and
examples, and in most cases expanded far beyond its stringbook form.  When a
stringbook calculation is convention-sensitive, the monograph should either
include the calculation in full or supply a public calculation-check script
that verifies the finite algebra used in the derivation.

Current high-priority QFT blocks to absorb are:

- bosonic and fermionic path-integral constructions, including coherent-state
  Berezin integrals and the distinction between supergeometric field variables
  and Hilbert-space fermion operators;
- gauge fixing, BRST/BV, anomalies, and dimensional-reduction anomaly
  calculations, with all trace and gamma-matrix conventions checked against
  the monograph conventions;
- two-dimensional CFT: chiral stress-tensor Ward identities, Virasoro
  symmetry, BPZ/radial pairing, OPE convergence, modular/Riemann-surface
  structure, free fields, nonlinear sigma models, defects, orbifolds,
  twist-field deformations, boundary CFT, and superconformal symmetry;
- supersymmetry: spinor conventions, super-Poincare representation theory,
  the distinction between particle multiplets and off-shell field-variable
  multiplets, superspace, nonrenormalization arguments, and Wilsonian/BV
  scheme issues;
- planar integrability and large-\(N\) gauge-theory spectral problems,
  including the precise separation from relativistic factorized scattering;
- QFT aspects of strings, Wilson lines, flux tubes, confinement, branes as
  defects, and gauge/string large-\(N\) limits, only after their QFT
  assumptions have been stated without relying on a string-theory framework.

## Import Rules

For any string-book import, record:

- source section;
- object consulted;
- role: inspiration, convention check, source lead, example, or calculation to
  rederive;
- framework;
- definitions needed before use;
- theorem or formal status;
- notation changes;
- whether figures or diagrams are reused or redrawn;
- monograph chapter placement.

Do not reuse prose or rely on the string-theory context as the logical
setting. Rebuild the material as QFT: state the local quantum framework,
operator or path-integral status, symmetry algebra, representation category,
regularization, and analytic assumptions before using any
stringbook-motivated formula.

## Classification Vocabulary

- `Incorporated`: the QFT monograph contains an independent development with
  definitions, hypotheses, derivation/proof boundary, and a calculation
  companion when the finite algebra is convention-sensitive.
- `Boundary linked`: the monograph has the topic only up to an explicit
  theorem, conjecture, construction, or approximation boundary, and the owed
  development is linked to a focused open issue.
- `Contextual`: the material is mostly string-theory or geometry context; it
  may suggest examples or convention checks, but it is not a pure-QFT floor
  item unless the QFT monograph independently reconstructs it.
- `Outside pure-QFT scope`: the material belongs to the stringbook as string
  background, brane, or supergravity material and should not be imported into
  the QFT monograph except as explicitly labeled comparison context.

No row is allowed to sit in an untracked middle state.  If a pure-QFT topic is
not incorporated, the row must name the focused issue that owns the missing
physics.

## Current-Head Companion-Notebook Audit

The following notebook pass is the current-head reproducibility inventory for
#731/#745.  Together with the prose-section audit below, it removes the old
notebook path ambiguity and routes each notebook to a verifiable QFT status.

| Source notebook | QFT classification | Monograph evidence or focused issue |
| --- | --- | --- |
| `codes/2D local susy variations.nb` | Contextual | Worldsheet local supersymmetry is string-context material.  QFT-side superconformal algebra and spectral-flow conventions are rebuilt in Volume V Chapter 15 and checked by `calculation-checks/superconformal_algebra_checks.py`; no direct import is needed unless a later worldsheet-gauge comparison is explicitly opened. |
| `codes/2D superspace.nb` | Incorporated with boundary | Two-dimensional superspace/LG/GLSM material is rebuilt in Volume VII Chapter 9 and checked by `calculation-checks/susy_2d_lg_glsm_checks.py`; continuum mirror/Hori--Vafa proof obligations remain tracked under #626, with Hori--Vafa formulas treated as derivations to scrutinize and recheck rather than as authority, as described in the Appendix K row below. |
| `codes/4D superspace.nb` | Incorporated | Four-dimensional superspace and component conventions are rebuilt in Volume VII Chapters 2--4, with checks in `calculation-checks/susy_superspace_component_checks.py`, `calculation-checks/susy_vector_superfield_checks.py`, and `calculation-checks/susy_superfield_operator_algebra_checks.py`. |
| `codes/BES equation.nb` | Boundary linked | Weak-coupling BES coefficient checks are incorporated in Volume VII Chapter 13 and `calculation-checks/planar_n4_integrability_checks.py`; the remaining notebook-to-Python audit and strong/global BES branch construction are routed to #624 and the planar crosswalk. |
| `codes/Conformal blocks and bootstrap demo.nb` | Incorporated with boundary | Global-block kinematics, BPZ equations, Virasoro blocks, and crossing examples are rebuilt in Volumes III and V with `calculation-checks/conformal_block_companion.py`, `calculation-checks/cft_virasoro_minimal_checks.py`, and `calculation-checks/liouville_bpz_checks.py`; numerical SDP/bootstrap-tool depth remains routed to #631. |
| `codes/G2 conical geometry.nb` | Outside pure-QFT scope | Special-holonomy cone geometry is string/M-theory background material.  It should not be imported into the QFT monograph except as comparison context in a later string-geometry project. |
| `codes/GS kappa symmetry.nb` | Outside pure-QFT scope | Green--Schwarz kappa symmetry is a worldsheet string gauge-symmetry check, not a pure-QFT floor item for this monograph. |
| `codes/Instanton and anomalies.nb` | Boundary linked | Anomaly-polynomial finite algebra is rebuilt in the anomaly chapters and checked by `calculation-checks/anomaly_polynomial_descent_checks.py` and `calculation-checks/gamma_trace_checks.py`.  The Yang--Mills instanton part is routed to #597/#629/#630: the QFT monograph must prioritize determinant measures, zero modes, operator insertions, and physical amplitudes over moduli-space description alone. |
| `codes/Liouville CFT.nb` | Incorporated with theorem boundary | Liouville spectrum, DOZZ/BPZ boundaries, block recursion interface, and boundary Liouville checks are rebuilt in Volume V Chapters 13--14 and checked by `calculation-checks/liouville_bpz_checks.py` and `calculation-checks/bcft_cardy_checks.py`.  DOZZ/completeness remain theorem-boundary inputs rather than notebook-derived results. |
| `codes/Type II basic worldsheet calculations.nb` | Contextual | OPE and free-field worldsheet calculations inform CFT examples only when rebuilt from QFT-side chiral algebra and Ward identities.  Tree-level graviton string amplitudes are outside the pure-QFT floor. |
| `codes/Type II torus 4-graviton amplitude check.nb` | Outside pure-QFT scope | Type-II genus-one graviton amplitudes belong to string perturbation theory, not the QFT monograph's pure-QFT incorporation floor. |
| `codes/conifold geometry.nb` | Contextual | Conifold geometry is relevant only as background/motivation for supersymmetric gauge dynamics; the QFT material is rebuilt in Volume VII through moduli, duality, and gauge-dynamics chapters without importing the geometry notebook as proof. |
| `codes/gamma matrices.nb` | Incorporated | Spinor and gamma-matrix conventions are rebuilt in Volume I/II spinor and anomaly chapters, with checks in `calculation-checks/gamma_trace_checks.py`, `calculation-checks/spinor_convention_checks.py`, and `calculation-checks/standard_model_anomaly_checks.py`. |
| `codes/mirror TBA and wrapping corrections.nb` | Boundary linked | Mirror kinematics and the leading Konishi wrapping calculation are rebuilt in Volume VII Chapter 14 and checked by `calculation-checks/planar_n4_integrability_checks.py`; full excited-state and notebook-wide source-term audit is routed to #624. |
| `codes/special geometry.nb` | Incorporated with boundary | Seiberg--Witten special-coordinate and period material is rebuilt in Volume VII Chapter 7 with `calculation-checks/sw_su2_periods.py`; higher-rank/global special-geometry extensions remain part of the SUSY depth lanes (#626/#701) rather than a stringbook import. |
| `codes/spinfield cocycles.nb` | Contextual | Spin-field cocycles are string-worldsheet convention material.  Only the QFT-side chiral algebra, locality, and spin-structure lessons are used, rebuilt in Volume V rather than imported as NSR worldsheet proof. |
| `codes/string coupling conventions.nb` | Outside pure-QFT scope | String coupling and brane-tension normalization conventions are not pure-QFT material. |
| `codes/su(2|2) spin chain.nb` | Boundary linked | Planar magnon dispersion, S-matrix local checks, crossing rational multiplier, and rank certificates are rebuilt in Volume VII Chapter 13 and `calculation-checks/planar_n4_integrability_checks.py`; global scalar branch, Yang--Baxter, and bound-state matrix-intertwiner work remain routed to #624. |

## Current-Head Prose Section Audit

This table is the section-level audit of pure-QFT prose at the same source
revision.  It is intentionally a routing ledger, not a certificate that every
boundary theorem has been proved in the monograph.  The crosswalk is complete
only in the sense that no pure-QFT source range is left in an unclassified
middle state: each range is incorporated, contextual or outside pure-QFT scope,
or boundary-linked to a live focused issue.

| Source range in `texsource/string notes.tex` | QFT classification | Monograph evidence or focused issue |
| --- | --- | --- |
| Non-extracted worldsheet/string ranges before AdS/CFT: `512--5064`, `5249--6217`, `6409--9684`, `10240--10994`, `11060--11716`, `11735--11803`, and `13111--13276` | Contextual with extracted QFT mechanisms | The pure-QFT mechanisms are routed to the later appendix rows: BRST/BV to Volume IV, 2D CFT/sewing to Volumes III/V, defects and orbifolds to Volume V, supersymmetry to Volume VII, and anomalies to Volume II.  String amplitudes, supermoduli, D-brane dynamics, string field theory, and RR-flux string backgrounds are not imported as pure-QFT claims. |
| `5065--5248`, `6218--6408`, and `11804--13110`: NLSM backgrounds, Calabi--Yau/singular CFT material, worldsheet instantons, cosets, conifold, and Liouville/cigar bridges | Incorporated with boundary | Volume V Chapter 11 covers NLSM beta functions, WZW/cosets, orbifolds, and twist fields; Volume V Chapter 15 covers the \(N=2\) SCA and spectral-flow data; Volume VII Chapter 9 covers the intrinsic \(2D\) \((2,2)\) LG/GLSM mirror lane.  Worldsheet-instanton or Hori--Vafa-style formulas are not treated as authority: determinant normalization, vortex compactness, zero modes, operator maps, and continuum equivalence remain routed to #626 and the Chapter 9 dossier. |
| `9685--10239`, `10995--11059`, `11717--11734`: D-instantons and heterotic/gauge-instanton string-duality material | Contextual; pure-QFT instanton work boundary-linked | These ranges are not imported as QFT instanton derivations.  Volume II Chapters 20--21 develop Yang--Mills instantons from regulated determinant/zero-mode/operator-insertion amplitudes and explicitly prioritize physical observables over moduli-space geometry; remaining singular-instanton and QCD-rigor obligations are owned by #597, #629, and #630. |
| `13277--15616`: AdS/CFT, ABJM, \(6D\) \((0,2)\), D1--D5, and AdS\(_3\) string material | Boundary linked or contextual | Pure gauge-theory and SCFT structures are routed to Volume VII and the focused depth issues #624 and #626.  Holographic supergravity/string derivations are comparison context, not pure-QFT proof sources. |
| `15617--17808`: planar \(\mathcal N=4\) integrability, mirror TBA, and QSC | Boundary linked through dedicated crosswalk | The section-by-section ledger lives in `planning/planar_n4_integrability_stringbook_crosswalk.md`; local algebra and finite checks are incorporated in Volume VII Chapters 12--15, while global BES/crossing, excited-state TBA, QSC gluing, strong Konishi, and analytic reconstruction remain routed to #624 and #728. |
| `17809--18747`: holographic Wilson lines, confinement models, Sakai--Sugimoto, Klebanov--Witten, and holographic cascade | Boundary linked or contextual | Wilson-line/cusp/Bremsstrahlung QFT aspects are part of the supersymmetry and planar-depth lanes #624/#626.  Holographic confinement and brane-engineered gauge dynamics are context for Volume IX/QCD discussions but are not imported as derivations of confinement; QCD rigor boundaries remain with #630. |
| `18748--19215`: Matrix theory and matrix string | Incorporated with conjecture boundary | Volume VII Chapter 3 now develops maximally supersymmetric \(U(N)\) matrix gauge quantum mechanics intrinsically: Hamiltonian, Gauss law, center-of-mass/\(SU(N)\) split, flat branch, continuous spectrum, Witten-index boundary terms, and threshold-bound-state status.  `matrix_quantum_mechanics_checks.py` checks the finite Gauss-law and supercharge-closure mechanism.  BFSS/M-theory scattering, black-zero-brane thermodynamics, matrix-string amplitudes, and JT-gravity matrix-model analogies remain comparison or central-conjecture material rather than foundations.  The symmetric-product orbifold mechanisms remain in Volume V Chapter 11. |
| `19381--19922`: path integrals, tunneling/instantons, supersymmetric quantum mechanics, Borel resummation, and Lefschetz thimbles | Incorporated with boundary | Volume I path-integral chapters cover regulated bosonic and fermionic constructions; Volume II instanton chapters handle field-theoretic instanton amplitudes.  Semiclassical/resurgent technology beyond the regulated instanton-amplitude lanes is routed to #597 when it bears on soliton/instanton physics and otherwise remains contextual rather than silently incorporated. |
| `19949--20065`: Faddeev--Popov and BV quantization of gauge theory | Incorporated | Volume IV develops gauge fixing, BRST, BV, master equations, local observables, and finite BV/localization checks, with companion scripts for signs and regulated identities. |
| `20066--20240`: local QFTs, fields, correlators, conformal symmetry, and OPE | Incorporated with theorem boundary | Volumes I, III, IV, and V rebuild the Wightman/OS/local-net/functorial/QFT-side CFT frameworks.  Quoted OS/AQFT structural proof debt remains tracked by #695. |
| `20241--20882`: general \(2D\) CFT, Virasoro, Weyl anomaly, conformal blocks, and block recursion | Incorporated with boundary | Volumes III and V contain the Virasoro/Ward/BPZ/block development and checks; remaining KZ, Coulomb-gas, Moore--Seiberg, and full sewing depth is routed to #625 and #697. |
| `20882--21100`: Riemann surfaces and modular invariance | Incorporated with boundary | Volumes V Chapters 12--14 cover modular covariance, sewing hypotheses, Cardy data, and BCFT boundaries; theorem-level modular/sewing proof debt remains with #625/#697. |
| `21100--21460`: free bosons and fermions on Riemann surfaces | Incorporated | Volumes III/V rebuild the free-field examples, lattice locality, cocycles, spin structures, and modular checks; string-worldsheet uses are not treated as proof sources. |
| `21460--21764`: symmetries, defects, orbifolds, Ising CFT, and Narain lattices | Incorporated with boundary | Volume V develops the generalized-symmetry/defect/orbifold/Narain material with arithmetic checks.  Full categorical/sewing depth remains coordinated with #625/#697. |
| `21764--22157`: Lagrangian descriptions of \(2D\) CFTs, NLSM Weyl anomaly, Buscher rules, gauged WZW/cosets, and Liouville | Incorporated with boundary | Volume V Chapter 11 includes the covariant NLSM renormalization, torsion/dilaton representative, Buscher/coset geometry checks, and Liouville boundary links.  Exact conformality and completeness inputs remain theorem boundaries under #625/#697. |
| `22157--22461`: \(2D\) superconformal symmetry | Incorporated with boundary | Volume V Chapter 15 now rebuilds the flat \((1,1)\) superspace laboratory, local \(N=1\) distribution-preserving superconformal maps, primary-superfield two-/three-point structures with parity bookkeeping, the \(N=1\), \(N=2\), extended spectral-flow, and small \(N=4\) OPE/BPS layers.  The finite algebra, supergeometry, and \(c=6\) short-character checks live in `superconformal_algebra_checks.py`.  Full spin-CFT sewing, global super-Riemann-surface existence, affine \(N=4\) character modular completion, and supersymmetric RG/model construction remain boundary material coordinated with #625/#697 and the Volume VII supersymmetric-QFT lane. |
| `22461--22749`: \(2D\) RG flows, LG models, GLSMs, Calabi--Yau/LG phases, abelian duality, and cigar/Liouville mirror | Incorporated with boundary | Volume VII Chapter 9 develops LG/GLSM data, Coulomb one-loop determinants, vortex-normalized mirror terms, \(P^{N-1}\) protected observables, and Hori--Vafa scrutiny with `susy_2d_lg_glsm_checks.py`.  Full continuum mirror equivalence, vortex compactness, determinant nonvanishing, and operator-map/gluing are routed to #626 and kept out of the monograph as derived claims until proved. |
| `22750--22972`: spinor conventions | Incorporated | Volume I/II/VII convention material and `gamma_trace_checks.py`/`spinor_convention_checks.py` cover the QFT-side spinor and gamma-matrix conventions. |
| `22972--23299`: super-Poincare symmetry, \(4D\) superspace, nonrenormalization, \(4D\) \(N=2\), and \(3D\) supersymmetric gauge theories | Incorporated with boundary | Volume VII develops supersymmetry, superspace, protected quantities, and Seiberg--Witten-style examples; deeper HLS, localization, Wilson-loop, \(F\)-theorem, duality, and \(6D\) material remains routed to #626. |
| `23300--23652`: supergravity appendices | Outside pure-QFT scope with selected convention use | Supergravity formulae are not pure-QFT source material.  Special-geometry conventions may serve as comparison for Volume VII, but any use must be rebuilt as QFT-side Seiberg--Witten/supersymmetric effective-action data and routed through #626 if not already developed. |
| `23717--24166`: anomalies | Incorporated with boundary | Volume II and Volume XII anomaly chapters rebuild axial/gauge/gravitational anomaly machinery with descent and gamma-trace checks.  Remaining proof-debt and convention-boundary work is tracked by #696 and QCD rigor issue #630. |
| `24166--24414`: boundary CFT | Incorporated with boundary | Volume V Chapter 14 covers conformal boundary conditions, boundary states, Cardy consistency, compact-boson and Ising boundaries, and Liouville boundary bridges with `bcft_cardy_checks.py`; full Cardy--Lewellen sewing depth remains with #625/#697. |
| `24414--24663`: double-scaled matrix quantum mechanics | Incorporated with boundary | Volume I Chapter 4 now develops Hermitian one-matrix quantum mechanics as an intrinsic \(0+1\)-dimensional QFT: matrix Hilbert space, \(U(N)\) action, singlet/Gauss projection, eigenvalue measure, radial Laplacian, Vandermonde fermionization, non-singlet angular inverse-square sectors, large-\(N\) density variables, and the leading collective Hamiltonian.  `matrix_quantum_mechanics_checks.py` checks the radial/Vandermonde and collective-field algebra.  The \(c=1\) string, particle-hole leg factors, ZZ-instanton interpretation, JT-gravity matrix-model analogies, and long-string identifications remain comparison boundaries, not proof sources. |
| `24663--24848`: holographic correlator kinematics | Contextual with extracted CFT kinematics | Boundary CFT correlator kinematics and conformal blocks are covered in Volumes III/V; Witten diagrams and AdS bulk dynamics are holographic comparison context rather than pure-QFT derivations. |

## Relevant Sections

### The Path Integral

Consulted source:

- `texsource/string notes.tex`, section "The path integral", especially the
  subsections "Path integral formulation of quantum mechanics" and "Path
  integral with Grassmann-odd field variables".

Potential use:

- finite-dimensional time slicing;
- phase-space and configuration-space forms;
- measure dependence;
- Grassmann path integrals;
- bosonic trace as periodic Euclidean boundary condition;
- fermionic thermal trace as anti-periodic Euclidean boundary condition and
  supertrace as periodic fermionic boundary condition;
- semiclassical analysis;
- instantons, Borel summation, and Lefschetz thimbles.

Required checks:

- classify every integral by mathematical status;
- state regulators and contours;
- identify formal expansions.

Likely placement:

- Volume I path-integral chapters;
- Volume II perturbation and renormalization;
- advanced semiclassical appendices.

Current absorption:

- Volume I, Chapter 4 now includes the bosonic Euclidean trace and periodic
  boundary condition derivation.
- Volume I, Chapter 16 now includes the coherent-state completeness
  derivation, ordered finite-dimensional Berezin measure, fermionic thermal
  trace, anti-periodic boundary condition, and supertrace/periodic boundary
  condition.

### Path Integral Quantization Of Gauge Theories

Potential use:

- quotient by gauge redundancy;
- Faddeev--Popov procedure;
- BRST and BV;
- Wilsonian effective action with master-equation structure.

Required checks:

- define field space, gauge group, ghosts, antifields, and grading;
- distinguish redundancy from physical symmetry;
- state perturbative or finite-dimensional status.

Likely placement:

- Volume IV gauge fixing, Yang--Mills, QCD, and anomalies;
- a dedicated BV block in the gauge-theory volume, where antifields,
  antibrackets, master equations, and the BV forms of the 1PI and Wilsonian
  effective actions are developed systematically.

Current absorption:

- The issue #583 BV deepening pass expands the gauge-theory BV chapter with
  a finite-regulator infinitesimal exact-RG theorem, a local BV--BRST
  comparison theorem for Yang--Mills with matter, ghost-number-zero
  counterterm representatives, the ghost-number-one anomaly ledger, and the
  regulated local-observable/factorization-algebra boundary.
- The finite-dimensional BV/localization chapter now includes the compact
  \(S^2\) Atiyah--Bott fixed-point model in addition to BV Stokes,
  pushforward, normal Gaussian factors, and the Mathai--Quillen rank-one
  calculation.
- Companion checks now cover BV master-algebra signs, Yang--Mills ghost
  nilpotency, doublet contraction, BV localization algebra, and the
  \(S^2\) fixed-point coefficient identity.

### Local Quantum Field Theories

Potential use:

- local fields and microcausality;
- stress tensor;
- Wightman functions;
- Euclidean continuation;
- conformal symmetry;
- OPE intuition;
- Kontsevich--Segal-type comments.

Required checks:

- separate Hilbert-space, Euclidean, and categorical frameworks;
- treat point fields distributionally;
- state reconstruction or analytic-continuation hypotheses.

Likely placement:

- Volume I opening and correlation chapters;
- Volume IV framework comparison;
- Volume III/V CFT material.

Current absorption:

- Issue #599 added a dedicated Kontsevich--Segal functorial QFT chapter in
  `monograph/tex/volumes/volume_iv/chapter06_kontsevich_segal_functorial_qft.tex`,
  included in the Volume I foundations sequence after OS reconstruction.
- The chapter states Segal sewing, proves the K-S allowability angle
  criterion, defines the functorial bordism datum, relates K-S data to OS,
  Wightman, and local-net frameworks under explicit hypotheses, derives OPE
  from sewing under annular spectral/nuclear assumptions, and records the
  construction-status ledger.
- The finite algebra is checked by
  `calculation-checks/ks_allowability_checks.py`.

### Two-Dimensional CFT

Potential use:

- two-dimensional conventions;
- Virasoro algebra;
- state-operator correspondence;
- OPE and conformal blocks;
- modular considerations.
- bosonic and supersymmetric nonlinear sigma-model CFTs;
- finite orbifolds, discrete torsion, twist sectors, and twist-field
  deformations.

Required checks:

- define chiral versus full CFT data;
- state convergence and sewing assumptions when needed;
- separate local operator statements from categorical structures.

Likely placement:

- Volume III CFT chapters;
- Volume V vertex algebra and modular tensor category chapters.

Special boundary:

- two-dimensional CFT material must be developed from local QFT, radial
  quantization, chiral algebras, stress-tensor Ward identities, and sewing or
  modular hypotheses as needed;
- string worldsheet uses of CFT may suggest examples but cannot replace the
  QFT-side construction of chiral and full CFT data.
- all relevant two-dimensional CFT content in the stringbook appendices is a
  required source-coverage item for the QFT monograph; it must be rewritten
  with the monograph's definitions, hypotheses, and proof boundaries, not
  imported as string-theory background.

Current absorption:

- Volume III/Volume V, Chapter 5 now includes the chiral stress-tensor mode
  construction, Virasoro algebra proof, Schwarzian transformation, and
  plane-cylinder \(c/24\) shift.
- Volume V, Chapter 11 now starts the QFT-side development of bosonic and
  supersymmetric sigma-model CFTs, Narain lattice CFTs and toroidal sigma
  models, WZW/current-algebra/coset CFTs, finite orbifolds, twist sectors,
  cyclic and rotation twist weights, and twist-field deformations.  The
  NLSM renormalization pass now gives the covariant exponential background
  split, the source-coupled mean-zero 1PI effective-action convention, the
  pure-metric second variation and curvature vertex, the background-field
  one-loop Ricci divergence with the local heat-kernel pole and
  Ricci-counterterm normalization derived explicitly, the \(G,B,\Phi\)
  Weyl-anomaly package with full string-frame metric/dilaton variation and
  trace representative, scheme-redefinition geometry, torsionful one-loop
  packaging, the
  pure-metric two-loop representative, the precise RG-time conversion to
  Hamilton Ricci flow, and constant-curvature sphere/hyperbolic radius-flow
  checks.  The Narain pass
  rebuilds the stringbook lattice vertex-operator material with explicit
  locality, spin, cocycle, modular-anomaly, and \(O(d,d;\mathbb Z)\) moduli
  statements, together with a public calculation check for the cocycle and
  pairing algebra.  The WZW pass adds integral level quantization, affine
  current algebra, Sugawara stress tensors, integrable highest weights, coset
  stress tensors, the diagonal \(SU(2)\) minimal-model example, and the
  rank-one solvable cosets \(SU(2)_k/U(1)\) and
  \(SL(2,\mathbb R)_k/U(1)\), with the parafermion branching/field
  identification, fusion/modular data, and cigar momentum/winding and
  spectrum-status conventions stated before the gauged sigma-model
  geometries.  The monograph now also checks the bell and cigar
  one-loop Weyl-anomaly equations directly from the rotational curvature
  formulas.  The orbifold twist-field pass now derives the complex-boson
  rotation twist weight from the fractional oscillator normal-ordering
  constant.  The symmetric-product orbifold pass now includes the
  connected-torus-cover Hermite-normal-form count behind the Hecke transform
  and the constant-seed partition-number normalization test, together with a
  Riemann--Hurwitz monodromy ledger for the first twist-correlator covering
  checks and the beta-normalized local coordinate map for the primitive
  joining cover, plus the Schwarzian/OPE-power ledger and class-normalized
  group factor for the primitive joining channel, together with the normalized
  transposition join/split class-algebra factors.  The twist-deformation layer
  now derives the annular conformal-perturbation beta function and the
  contact-term scheme law instead of leaving exact marginality as a slogan.
  The public arithmetic check covers the central-charge,
  conformal-weight, field-identification, compact fusion, reflection-weight,
  integer-spin, and bell/cigar geometry formulas.
- Volume V, Chapter 12 now adds the algebraic chiral-CFT layer: vertex
  operator algebras, ordinary modules, characters, Zhu algebras and top-level
  module classification, unitary Virasoro minimal-model representation data,
  conformal blocks as Ward identity functionals, higher-genus sewing, modular
  tensor category data, the Verlinde formula, rational full-CFT modular
  invariants, torus one-point trace blocks, Verlinde topological defect lines,
  a leading Cardy high-temperature derivation, and logarithmic CFT
  boundaries.  The torus/defect layer states Zhu modular covariance with
  explicit hypotheses, proves the diagonal Verlinde defect fusion and
  temporal/spatial modular \(S\)-move, and works the Ising spin-flip and
  Kramers--Wannier defect examples.  The unitary minimal-model layer now
  includes the full A-series \(S,T\) modular data, the
  Kac-field-identification quotient normalization, and the finite
  \(SU(2)\)-quotient fusion rule.  The Ising minimal-model
  discussion now includes the level-two Virasoro Gram/null-vector calculation,
  the BPZ equation for the spin four-point function, and the crossing
  calculation fixing
  \(C_{\sigma\sigma\varepsilon}=1/2\), expanding the stringbook appendix
  discussion into a self-contained monograph derivation.  The Ising modular,
  defect-line, Zhu, logarithmic-cell, and unitary-minimal-model data are
  checked by `calculation-checks/cft_voa_modular_checks.py` and
  `calculation-checks/cft_virasoro_minimal_checks.py`.
- Volume V, Chapter 13 develops Liouville CFT from the QFT side: classical
  action and stress tensor, background charge and central charge, Seiberg
  domain, probabilistic construction boundary, reflection relation,
  continuous conformal-block decomposition, DOZZ theorem boundary, BPZ
  equations for both \(V_{-b/2}\) and \(V_{-1/(2b)}\), ordinary and dual
  one-screening coefficients, hypergeometric connection formulas,
  Virasoro block Gram-projector coefficients through level three, the
  elliptic nome interface to Zamolodchikov recursion, and boundary Liouville
  states with FZZT one-point functions and ZZ finite differences.  The finite
  convention algebra is checked by
  `calculation-checks/liouville_bpz_checks.py` and the Liouville boundary
  hyperbolic identities are checked by
  `calculation-checks/bcft_cardy_checks.py`.
- Volume V, Chapter 14 develops the 2D BCFT appendix material as a
  self-contained boundary-state theory: conformal boundary data, Ishibashi
  states, Cardy consistency, Cardy--Lewellen sewing hypotheses,
  compact-boson Neumann/Dirichlet states, Majorana/Ising boundary states,
  boundary-condition-changing OPE constants, direct-sum/Chan--Paton
  boundaries, and the nonrational Liouville FZZT/ZZ bridge.  The finite
  Cardy, Ising, compact-boson, Chan--Paton, and Liouville-boundary algebra is
  checked by `calculation-checks/bcft_cardy_checks.py`.
- Volume V, Chapter 15 now absorbs the chiral-algebra and local superspace
  part of Appendix J: spin-sector data, NS/R mode conventions, the flat
  \((1,1)\) superspace multiplet and component action, local \(N=1\)
  superconformal coordinate changes preserving the odd distribution,
  infinitesimal contact vector fields, primary superfields, invariant
  superdistances, two-/three-point superfield structures with parity
  bookkeeping, \(\mathcal N=1\) and \(\mathcal N=2\) superconformal OPEs and
  mode algebras, the Ramond zero-mode shift, \(\mathcal N=2\) spectral flow,
  chiral-primary bounds, the extended \(\mathcal N=2\) spectral-flow
  operator layer with the charge-lattice/locality hypothesis, \(U(1)_R\)
  bosonization, integer and half-integer flow fields, and \(X^\pm/Y^\pm\)
  charge bookkeeping, elliptic-genus Ramond trace hypotheses, right-moving
  ground-state localization, spectral-flow/Jacobi covariance, protected
  Landau--Ginzburg central-charge and \(\chi_y\) charge-polynomial tests,
  and the supersymmetric rank-one coset interfaces for
  \(SU(2)_k/U(1)\) minimal models and the
  \(SL(2,\mathbb R)_k/U(1)\) cigar, including central charges, weights,
  \(R\)-charges, the compact \(A\)-series chiral ring, spectral-flowed
  labels, field identifications, compact \(\mathbb Z_k\) action, and cigar
  momentum/winding bookkeeping.  The small \(N=4\) repair gives the complete
  auxiliary-\(y\) OPE convention, component mode algebra, inner spectral
  flow, unitary \(h\ge j\) BPS bound, and a \(c=6\) global short-character
  example that coordinates with the symmetric-product marginal operators in
  Chapter 11.
  It explicitly coordinates with the Volume VII supersymmetric-QFT lane for
  the actual LG/GLSM RG-flow, elliptic-genus realization theorem, and
  cigar/Liouville mirror-duality
  constructions.  The finite algebra is checked by
  `calculation-checks/superconformal_algebra_checks.py`.

### Two-Dimensional Supersymmetric Models

Current Appendix K absorption:

- Volume VI, Chapter 06 now absorbs the ordinary scalar Landau-Ginzburg part
  of Appendix K as a perturbed two-dimensional QFT interface: it defines the
  normal-ordered polynomial source-coordinate system, proves the local logarithmic
  collision integrability used by the perturbative expansion, derives the
  normal-ordered equation-of-motion relation, and records the finite
  order-field quotient for the even multicritical family.  The expected
  \(M(m,m+1)\) minimal-model endpoint is stated as an RG construction
  problem, not imported as a theorem from the polynomial algebra.
- Volume VII, Chapter 09 develops the Landau--Ginzburg, sigma-model, GLSM,
  and abelian mirror material as intrinsic two-dimensional QFT.  The current
  GLSM/mirror pass expands the stringbook Appendix K charged-chiral duality
  and cigar/Liouville material with a first-order `B_i` derivation, the
  twisted-linear constraint, Legendre elimination, the
  `-Q_i^a Sigma_a Y_i` integration-by-parts term, the vortex-exponential
  proof boundary, a proper-time derivation of the local Coulomb one-loop
  logarithm and its anomaly-completed holomorphic branch, exact elimination
  of the `Y_i` to recover the Coulomb one-loop twisted superpotential, the
  finite FI-coordinate shift, the logarithmic-torus mirror presentation,
  `P^{N-1}` critical-point simplicity, and the classical cigar quotient
  metric.
- The Appendix K Landau--Ginzburg nonrenormalization footnote is now
  rewritten as an explicit two-dimensional Wilsonian-coordinate argument:
  with chiral Wilsonian regularity, flavor spurion symmetries, and
  `R(W)=1`, regular holomorphic corrections to Fermat superpotentials are
  restricted to the original `g_i (Phi^i)^{d_i}` monomials.  The text states
  the regulator and infrared-existence boundaries rather than treating the
  selection rule as a standalone theorem about the continuum fixed point.
- The hypersurface chamber material from Appendix K is now expanded with
  the adjunction calculation `c1(TY_G)=(N-d)H|_{Y_G}`, the `d=N`
  Calabi-Yau condition, the sigma/LG central-charge matching condition, the
  residual `mu_d` finite-gauge action and untwisted invariant Jacobi-basis
  condition, and the anomaly-free Coulomb-coordinate singular signal.
- The monograph deliberately treats Hori--Vafa/Hori--Kapustin-style formulas
  as mechanisms to reconstruct rather than proof sources.  The remaining
  proof obligations are regulator-level construction of the vortex sectors,
  determinant normalizations, local operator maps, topological sectors, and
  equality of continuum Hilbert spaces/local algebras.  The 2026-06-04
  follow-through adds a residual-controlled bridge from the regulated
  vortex coefficient to the protected `P^{N-1}` A-twisted observable, so the
  Hori--Vafa residue identity is explicitly separated from the physical
  determinant, zero-mode, compactification, gluing, operator-map, and
  continuum inputs it still needs.  The same lane now also records the direct
  A-model stable-map gate for the `P^{N-1}` quantum product, deriving the
  degree-one dimension match and line count behind
  `I_1(H,H^{N-1},H^{N-1})=1` before identifying the mirror coordinate with
  the physical \(q\).
- Companion checks in `calculation-checks/susy_2d_lg_glsm_checks.py` now
  cover the finite algebra in the charged-dual elimination, FI shift,
  `P^{N-1}` critical ledger, cigar metric elimination, hypersurface
  adjunction/central-charge matching, residual finite-gauge invariant
  monomials, the Coulomb-coordinate signal, the vortex-to-observable
  residual telescope, the degree-one stable-map quantum-product gate, and
  the Fermat Wilsonian superpotential
  spurion-selection arithmetic.  The companion is now in the evidence-contract
  manifest because the mirror/vortex checks are load-bearing and
  scope-sensitive.

### Planar Integrability

Current relativistic-integrability absorption:

- Volume VI now contains the algebraic/nested Bethe-ansatz infrastructure that
  the stringbook mostly used in the planar gauge-theory setting:
  RTT relations, transfer-matrix commutativity, the \(XXX_{1/2}\) algebraic
  Bethe ansatz, matrix Bethe--Yang quantization, \(SU(N)\) nested equations,
  an explicit \(SU(3)\) nested-root example, nested TBA, Baxter \(TQ\)
  relations, \(T\)-systems, \(Q\)-operators, and separation variables.  The
  finite algebra is checked by
  `calculation-checks/nested_bethe_ansatz_checks.py`.  The planar
  \(\mathcal N=4\) SYM development remains separate because its dispersion,
  cyclic-trace finite-size effects, and quantum spectral curve are different
  physical structures.

Current planar-integrability absorption:

- Volume VII now contains a dedicated planar \(\mathcal N=4\) SYM
  integrability spine: single-trace operators as cyclic spin chains, the
  one-loop `SU(2)` Heisenberg Hamiltonian and Konishi calculation, the
  centrally extended magnon dispersion relation, the all-loop asymptotic
  Bethe ansatz with scalar dressing phase and proof-boundary statement,
  mirror TBA and the T-hook Y-system, the QSC Pmu system and its
  weak-coupling Baxter limit, and the hexagon form-factor framework for
  three-point functions.  The finite algebra is checked by
  `calculation-checks/planar_n4_integrability_checks.py`.

Potential use:

- planar single-trace spectral problem in \(\mathcal N=4\) SYM;
- spin-chain realization of one-loop and asymptotic dilatation operators;
- centrally extended \(su(2|2)\) magnon representation theory;
- asymptotic Bethe ansatz, dressing phase, BES equation, cusp anomalous
  dimension;
- mirror TBA, wrapping corrections, Konishi, \(Y\)-system, and quantum spectral
  curve.

Required checks:

- define the large-\(N\) limit, operator sector, coupling scheme, and spectral
  problem before introducing spin-chain or worldsheet variables;
- distinguish planar gauge-theory integrability from relativistic
  two-dimensional factorized scattering in Volume VI;
- state which integrability inputs are theorem-level, perturbatively checked,
  symmetry-derived, or conjectural;
- reproduce convention-sensitive calculations with public calculation-check
  scripts, using the stringbook notebooks as source leads.

Likely placement:

- a later large-\(N\), gauge/string, or special-structure volume after the
  gauge-theory, supersymmetric, and CFT foundations are mature.

Special boundary:

- the two planar-integrability chapters in the stringbook are the internal
  source spine for the monograph's eventual planar-integrability treatment;
  the QFT monograph must deepen and expand them into a self-contained
  mathematical-physics development.

### Supersymmetry And Supergravity Appendices

Potential use:

- spinor and gamma-matrix convention checks;
- supersymmetry algebra and representation examples;
- superspace notation;
- component-field transformations;
- nonrenormalization and protected-quantity examples;
- supergravity only as a later comparison point, not as an early foundation for
  supersymmetric QFT.

Required checks:

- define the spacetime dimension, signature, spin group, reality condition, and
  R-symmetry before writing a supersymmetry algebra;
- distinguish algebraic representation theory from field-theoretic existence
  statements;
- derive component and superspace formulas in the QFT monograph's own
  conventions;
- state whether the discussion is off-shell, on-shell, perturbative, or
  nonperturbative;
- distinguish particle supermultiplets as Hilbert-space representations from
  off-shell field-variable multiplets as superfield or component-coordinate
  packages;
- for \(4D\) \(\mathcal N=1\) and \(\mathcal N=2\) gauge dynamics, define the
  supersymmetric Wilsonian scheme before importing holomorphy, exact
  superpotential, quantum-moduli-space, Seiberg-Witten, or duality arguments;
- separate supersymmetric QFT from string compactification or worldsheet
  motivation.

Likely placement:

- Volume VII supersymmetric QFT;
- later topological/cohomological volume for twists;
- advanced special-topic volumes for superconformal theories and protected
  sectors.

### Symmetries, Defects, And Orbifolds

Potential use:

- topological defect lines;
- non-invertible symmetries;
- orbifolds;
- anomaly and discrete torsion data.

Required checks:

- define defects as operators, interfaces, or categorical objects depending on
  framework;
- state codimension and locality properties;
- identify topological versus dynamical assumptions.

Likely placement:

- Volume V generalized symmetries and defects.

### Anomalies

Potential use:

- axial anomalies;
- gauge anomalies;
- contact-term viewpoint;
- anomaly polynomials and descent;
- inflow.

Required checks:

- define background fields and gauging problem;
- distinguish current nonconservation, obstruction to gauging, and anomaly
  inflow;
- state perturbative, topological, or cohomological framework.

Likely placement:

- Volume II anomalies;
- Volume V advanced anomaly structures.
