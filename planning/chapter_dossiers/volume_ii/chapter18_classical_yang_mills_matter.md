# Volume II, Chapter 18 Dossier: Classical Yang-Mills Theory And Matter

## Source Position

- Primary local source: second-sequence handwritten material, pages 157--168.
- Immediate predecessor: Wilsonian effective actions and exact cutoff flow.
- Immediate successor in the source order: gauge fixing, ghosts, and BRST.
- Role in the monograph: introduce nonabelian gauge fields as
  Lie-algebra-valued connections, construct their curvature and invariant
  action, state the trace and compactness assumptions needed for unitary
  Lorentzian gauge theory, and add matter fields in representations with QCD
  notation.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 157--168;
  checked against rendered page images in
  `monograph/tex/build/source_visual_trace/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  corresponding classical Yang-Mills section, used only as a comparison layer.
- `SRC-EXTERNAL`: standard Lie-algebra and principal-connection conventions
  used as guardrails only; the chapter follows the local source order and
  conventions.

## Construction Task

The chapter must define and derive:

- gauge potentials \(A_{a\mu}\) carrying spacetime and internal indices;
- the distinction between the anti-Hermitian mathematical Lie algebra
  \(\mathfrak g_{\mathrm{ah}}=\operatorname{Lie}(G)\) and the Hermitian
  generator coordinate space \(\mathfrak g=i\,\mathfrak g_{\mathrm{ah}}\);
- the anti-Hermitian connection one-form
  \(\mathsf A_{\mathrm{ah}}=-iA\) corresponding to the Hermitian local
  representative \(A\);
- the Hermitian-coordinate bracket
  \([X,Y]_{\mathrm H}=-i[X,Y]_{\mathrm{mat}}\), so explicit factors of \(i\)
  in transformation laws keep \(A_\mu,\zeta,F_{\mu\nu}\) Hermitian;
- Hermitian Lie-algebra generators \(t^a\) with output-first structure
  constants \([t^a,t^b]=i f^c{}_{ab} t^c\);
- infinitesimal gauge transformation
  \(\delta A_\mu=\partial_\mu\zeta-i[A_\mu,\zeta]\);
- finite gauge transformation
  \(A_\mu'=gA_\mu g^{-1}+i g\partial_\mu g^{-1}\) with
  \(g(x)=\exp(i\zeta^a(x)t^a)\);
- the overlap transformation law for local connection representatives on
  nontrivial principal bundles and the covariant gluing of curvature;
- BCH closure and the adjoint action \(e^X Y e^{-X}\);
- covariant derivative \(\nabla_\mu=\partial_\mu-iA_\mu\);
- field strength \(F_{\mu\nu}=i[\nabla_\mu,\nabla_\nu]\);
- covariant transformation \(F'_{\mu\nu}=gF_{\mu\nu}g^{-1}\);
- invariant trace \(\operatorname{tr}(t^a t^b)=\kappa^{ab}\), cyclicity,
  trace-lowered structure constants
  \(f_{abc}=\kappa^{ad}f^d{}_{bc}\), and the raising relation
  \(f^a{}_{bc}=\kappa_{ad}f_{dbc}\);
- Yang-Mills Lagrangian
  \(-\frac1{4g_{\mathrm{YM}}^2}\operatorname{tr}F_{\mu\nu}F^{\mu\nu}\);
- positive definite invariant form and compact reductive Lie algebras;
- the status distinction between the classical local Yang--Mills action and
  the open four-dimensional continuum quantum Yang--Mills existence/mass-gap
  problem;
- \(SU(2)\) and \(SU(N)\) examples with the default monograph/stringbook
  normalization \(\operatorname{tr}(t^a t^b)=\delta^{ab}\), while recording
  how the common half-trace convention changes component formulas;
- the four-dimensional \(\theta\)-term and its perturbative/topological roles;
- invertible \(p\)-form global symmetry in operational topological-operator
  form, including codimension-\(p+1\) symmetry operators, charged
  \(p\)-dimensional operators, and linking-number actions;
- the electric center one-form symmetry of pure \(SU(N)\) Yang--Mills,
  Wilson-line \(N\)-ality, and the surface-operator action
  \(U_m(\Sigma)W_R(C)U_m(\Sigma)^{-1}\);
- the subgroup of center one-form symmetry preserved by dynamical matter
  representations, including adjoint matter preserving and fundamental matter
  breaking the \(SU(N)\) center symmetry;
- the placement of higher groups and noninvertible/categorical symmetries in
  the later global-structure volume, with only the definitions needed for
  gauge-theory Wilson lines and confinement diagnostics used here;
- matter representations \(\rho_R:G\to GL(V_R)\), Lie-algebra generators
  \(t_R^a\), and the matter covariant derivative;
- invariant Hermitian pairings on compact-group representations and the
  resulting gauge-invariant contractions for scalar and Dirac matter;
- the Brout--Englert--Higgs mechanism as a local gauge-theory construction,
  not as literal breaking of a local gauge redundancy: Abelian Higgs quadratic
  expansion, unitary-gauge gauge-invariant vector coordinate,
  \(R_\xi\) gauge fixing, ghost/Goldstone gauge-dependent masses, and physical
  BRST/gauge-invariant mode counting;
- the nonabelian BEH mass matrix
  \(K_{ab}=\operatorname{Re}(t_R^a v,t_R^b v)_R\), its kernel
  \(\mathfrak h=\{X:t_R(X)v=0\}\), the count \(\dim G-\dim H\) of massive
  gauge bosons, and the \(SU(2)\to U(1)\) adjoint pattern;
- the orbit differential \(q_v(X)=i\,t_R(X)v\), the identity
  \(D_\mu(v+\eta)=\partial_\mu\eta-q_v(A_\mu)+O(A_\mu\eta)\), and the local
  BEH mode-count proposition relating \(\operatorname{rank}q_v\), scalar
  gauge-orbit coordinates, and massive vector polarizations;
- the nonabelian \(R_\xi\) gauge-fixing functional
  \(\mathcal F_\xi=\partial^\mu A_\mu+\xi g_{\rm YM}^2q_v^\dagger\eta\) in a
  local linear chart, with \(q_v^\dagger q_v\) controlling the broken-sector
  unphysical scalar and ghost masses;
- the perturbative renormalizability role of \(R_\xi\) gauges: local
  dimension-four shifted action, \(p^{-2}\) vector propagators, and BRST
  identities controlling counterterms, while unitary gauge is kept as a
  classical spectrum coordinate chart rather than the manifest proof gauge;
- the longitudinal-vector/Goldstone equivalence relation as a perturbative
  amplitude statement: broken-gauge datum, contracted Slavnov--Taylor identity,
  vector/Goldstone pole-residue conversion matrix, \(O(m/E)\) longitudinal
  polarization expansion, Abelian Higgs tree convention, electroweak
  \(W_LW_L\) scalar representative, Higgs cancellation of \(s/v^2\) growth,
  and the unstable-\(W/Z\) pole-scheme or narrow-width caveat;
- finite-energy gauge-Higgs sectors for adjoint scalar fields, including the
  vacuum orbit \(\mathcal O_v\), stabilizer \(H\), and the boundary map
  \(S^2_\infty\to G/H\);
- the homotopy classification \(\pi_2(G/H)\simeq\pi_1(H)\) when \(G\) is
  simply connected, with \(SU(2)\to U(1)\) as the basic monopole sector;
- the trace-form Bogomolny completion, the magnetic central charge
  \(\Gamma_{\mathrm m}=(4\pi)^{-1}\int_{S^2_\infty}\operatorname{tr}(\Phi B)\),
  and the \(SU(2)\) BPS lower bound after fixing a primitive magnetic
  cocharacter;
- the hedgehog ansatz for the unit 't Hooft--Polyakov/Prasad--Sommerfield
  monopole, the radial BPS ODEs, and the explicit
  \(K(\rho)=\rho/\sinh\rho\), \(H(\rho)=\coth\rho-\rho^{-1}\) solution;
- the framed BPS monopole moduli datum, including the based gauge quotient,
  the residual \(U(1)_\infty\) phase, the linearized Bogomolny equation, the
  background-gauge horizontal condition, the kinetic \(L^2\) metric, the
  \(4n\) dimension bookkeeping, and the low-velocity geodesic Lagrangian;
- the monopole \(S^1\) phase coordinate, its primitive periodicity, the
  theta-angle total-derivative term on the phase path, quantization of
  \(-i\partial_\chi\), the dyonic tower Hamiltonian, and the Witten-effect
  shifted electric coordinate \(n_{\mathrm e}+\theta n_{\mathrm m}/2\pi\);
- the distinction between topologically stable monopoles and vortices versus
  unstable sphaleron saddle points;
- the Abelian-Higgs Nielsen--Olesen vortex energy, BPS flux bound, and
  first-order vortex equations;
- the Jackiw-Rebbi kink zero-mode example: the sign-changing fermion mass
  profile, normalizable zero-mode wavefunction, spectral pairing, and
  soliton-sector half-charge operator;
- the spatial Chern--Simons functional used to locate the electroweak
  sphaleron between neighboring vacua;
- fundamental, anti-fundamental, and complexified adjoint representations of
  \(SU(N)\);
- QCD quark indices \(i,I,\alpha\), fermion kinetic term, Hermitian mass
  matrices \(m,\widetilde m\), and equivalent chiral complex mass matrix \(M\).

## Claim Ledger

1. The local Yang-Mills field is a connection one-form on a local
   trivialization of a principal \(G\)-bundle.
2. With Hermitian generators, the compact real Lie bracket is represented by
   \([X,Y]_{\mathrm H}=-i[X,Y]_{\mathrm{mat}}\), while formulas use ordinary
   matrix commutators with explicit \(i\)'s.
3. Closure of the local infinitesimal transformations is encoded by the Lie
   bracket of \(\mathfrak g\).
4. The finite transformation law is characterized by covariance of
   \(\partial_\mu-iA_\mu\).
5. Local connection representatives on overlapping trivializations obey the
   same transformation law as local gauge changes; curvature glues by
   conjugation.
6. Curvature transforms by conjugation, and invariant actions are built using
   invariant tensors on \(\mathfrak g\).
7. A positive invariant quadratic form gives the kinetic energy sign needed
   for unitary Lorentzian gauge fields.
8. The four-dimensional pure Yang--Mills continuum existence and positive
   mass-gap problem is the Clay Millennium problem; the local classical action,
   perturbative gauge-fixed expansions, and finite-cutoff lattice systems are
   not by themselves a completed continuum quantum Yang--Mills construction.
9. In \(D=4\), the \(\theta\)-density is local and gauge invariant; as a total
   derivative it enters perturbatively only through global/topological sectors.
10. Matter fields carry representations of \(G\), and their covariant
    derivative transforms in the same representation.
11. Pure \(SU(N)\) Yang--Mills has an electric \(\mathbb Z_N\) one-form
    symmetry acting on Wilson lines by their \(N\)-ality and by the linking
    number with the symmetry surface.
12. Dynamical matter preserves exactly the subgroup of the center that acts
    trivially on every dynamical representation; fundamental quarks break the
    pure Yang--Mills center one-form symmetry completely.
13. Higher groups and noninvertible/categorical symmetries are extended-operator
    and background-coupling data deferred to the global-structure volume, while
    the gauge-theory volume uses the one-form definition needed for Wilson
    loops, screening, and confinement diagnostics.
14. The BEH mechanism is a statement about the spectrum and local coordinates
    of gauge theories with scalar matter.  Gauge-orbit scalar coordinates are
    would-be Goldstone fields; in \(R_\xi\) gauges they are unphysical
    gauge-dependent fields paired with ghosts by BRST, while the physical
    spectrum contains massive vector particles and gauge-invariant scalar
    excitations.  The high-energy equivalence between external longitudinal
    massive vectors and would-be Goldstone amplitudes is a separate
    perturbative external-pole statement controlled by Slavnov--Taylor
    identities, residue/mixing conventions, and the \(m/E\) expansion; it is
    not a nonperturbative theorem and it does not make gauge-dependent
    Goldstone fields physical asymptotic particles.
15. In a nonabelian scalar vacuum \(v\), the gauge-boson mass matrix is
    determined by \(K_{ab}=\operatorname{Re}(t_R^a v,t_R^b v)_R\); its kernel
    is the stabilizer Lie algebra \(\mathfrak h\), so the massive-vector count
    is \(\dim G-\dim H\).  Equivalently, \(K=q_v^\dagger q_v\) for the orbit
    differential \(q_v(X)=i\,t_R(X)v\), which also constructs the local
    nonabelian \(R_\xi\) gauge-fixing term.
16. Finite-energy gauge-Higgs boundary conditions turn spatial infinity into
    a sphere mapped to the vacuum orbit \(G/H\); the resulting homotopy class
    labels classical magnetic sectors before quantization.
17. In the BPS limit of an adjoint \(SU(2)\) gauge-Higgs theory, completing the
    square gives a trace-form energy bound by the surface charge
    \(\Gamma_{\mathrm m}\); the integer formula requires fixing the primitive
    magnetic cocharacter and is not a generator-normalization-free statement.
18. The Prasad--Sommerfield profile solves the radial Bogomolny ODEs and
    provides a smooth nonabelian core for the unit 't Hooft--Polyakov
    monopole.
19. Quantizing the primitive \(S^1\) phase coordinate of a BPS monopole gives
    integer electric labels; the theta-angle term shifts the electric-field
    coordinate to \(n_{\mathrm e}+\theta n_{\mathrm m}/2\pi\), with
    \(\theta\mapsto\theta+2\pi\) compensated by
    \(n_{\mathrm e}\mapsto n_{\mathrm e}-n_{\mathrm m}\).
20. Nielsen--Olesen vortices arise from the same finite-energy logic in
    codimension two, with flux quantization and a first-order BPS system at
    critical coupling.
21. A sign-changing kink mass profile in the Jackiw-Rebbi model carries one
    normalizable fermion zero mode.  Chiral spectral pairing cancels the
    nonzero modes in the charge-conjugation symmetric sea, so the two
    zero-mode occupations carry charges \(-1/2\) and \(+1/2\).
22. The sphaleron is an unstable finite-energy saddle classified by its
    position relative to Chern--Simons number and by its negative fluctuation
    mode.
23. QCD uses the fundamental and anti-fundamental representations for quarks
    and antiquarks; the complexified adjoint representation describes
    adjoint-valued fields, with real adjoint fields selected by a reality
    condition.
24. Chiral mass notation repackages scalar and pseudoscalar Hermitian mass
    matrices into a complex flavor matrix.
25. Framed BPS monopole moduli spaces are quotients by based gauge
    transformations.  Their tangent coordinates satisfy the linearized
    Bogomolny equation together with the background-gauge horizontal
    condition, and the low-velocity kinetic energy restricts to the \(L^2\)
    metric on this horizontal zero-mode space.

## Calculation Checks

- `calculation-checks/soliton_collective_coordinate_checks.py`: verifies the
  Bogomolny and vortex square completions, Prasad-Sommerfield profile ODEs,
  monopole phase-coordinate Legendre transform and theta relabelling, framed
  monopole moduli dimension bookkeeping, zero-mode-density coordinate
  invariance, the one-instanton orientation dimension count, and the
  Jackiw-Rebbi kink zero-mode profile/normalization/half-charge algebra with
  integer-charge and unpaired-spectrum negative controls.
- `calculation-checks/longitudinal_goldstone_equivalence_checks.py`: verifies
  the longitudinal-polarization \(O(m/E)\) remainder, the external-pole
  residue/analytic-term separation, the electroweak Higgs-sector cancellation,
  and the ordered \(16\pi\) partial-wave normalization used by the new
  equivalence-relation section.

## Figure Requirements

- Index and Lie-algebra data for \(A_{a\mu}\), \(A_\mu=A_{a\mu}t^a\), and
  the infinitesimal transformation.
- Connection-curvature diagram showing covariance of \(\nabla_\mu\), curvature,
  invariant trace, and the Yang-Mills action.
- \(SU(N)\) representation diagram/table: fundamental, anti-fundamental,
  adjoint, and QCD quark indices.
- BEH mode-accounting figure for the Abelian model, showing scalar radial and
  gauge-orbit coordinates, the massive vector, and the \(R_\xi\)/BRST
  treatment of unphysical fields.
- Finite-energy boundary map diagram \(S^2_\infty\to G/H\), showing the
  relation between asymptotic Higgs data, transition functions, and magnetic
  sectors.
- Bogomolny square-completion diagram showing the nonnegative square, surface
  flux, and trace-form BPS energy bound.
- Chiral mass decomposition diagram relating \(m,\widetilde m\) to \(M\).

## Audit Notes

- 2026-05-22 source pass: compared handwritten pages 157--168, the local
  transcription, and Ben Lou's transcription against
  `volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`.
- Tightened the invariant trace discussion by adding the source-level cyclicity
  identity
  \(\operatorname{tr}([t^a,t^b]t^c)=\operatorname{tr}(t^a[t^b,t^c])\).
- Made explicit the positive-form classification as abelian \(\mathbb R\)
  factors plus compact simple Cartan types \(A,B,C,D,E,F,G\), with
  \(\operatorname{tr}(t^a t^b)=\delta^{ab}\) as the default
  normalization, matching the stringbook convention and the trace-form
  coupling \(-\frac1{4g_{\mathrm{YM}}^2}\operatorname{tr}F^2\).
- Added a rendered \(SU(N)\) representation/QCD-index figure, including the
  source convention
  \(\rho_{\overline{\square}}(g)=g^*\) without transposition and
  \(t_{\overline{\square}}^a=-(t^a)^*\).
- Rechecked the \(\theta\)-term statement: total derivative locally, no local
  perturbative vertex around the trivial sector, but nonzero action on
  finite-action topological sectors.
- Stop before Faddeev-Popov gauge fixing and BRST.
- State conventions for Hermitian generators and \(\gamma_5\) projectors.
- Do not let Hermitian-generator notation obscure the anti-Hermitian
  mathematical connection convention used in Chern-Weil and descent formulas.
- Avoid saying gauge symmetry is a physical symmetry; formulate it as local
  covariance/redundancy of field coordinates.
- No reader-facing source-page references or course labels.
- 2026-05-24 issue #261 pass: added a status remark naming the
  four-dimensional pure Yang--Mills existence and mass-gap problem as the Clay
  Millennium problem and separating that open continuum construction from the
  classical local action, perturbative BRST expansions, and finite-cutoff
  lattice regularizations.
- 2026-05-24 issue #263 pass: linked the status remark to the new lattice
  Yang--Mills chapter, where the finite-cutoff compact Haar formulation and
  continuum-limit hypothesis are developed before covariant gauge fixing.
- 2026-05-25 issue #471 pass: added finite-energy gauge-Higgs solitons to the
  classical Yang--Mills chapter rather than the current axiomatic Volume IV,
  because the repository's volume map has moved since the issue was opened.
  The new section treats the 't Hooft--Polyakov monopole through the
  finite-energy boundary map, the \(\pi_2(G/H)\) classification, the
  trace-form Bogomolny bound, the explicit Prasad--Sommerfield solution,
  Nielsen--Olesen vortices, sphalerons, and the quantization caveat for
  collective coordinates and semiclassical sectors.
- 2026-05-25 issue #470 pass: added a higher-form symmetry section before
  matter representations.  The section defines invertible \(p\)-form symmetry
  by topological codimension-\(p+1\) operators and linking action, then
  specializes to the electric center one-form symmetry of pure \(SU(N)\)
  Yang--Mills and its breaking by dynamical matter.  The full higher-group and
  noninvertible/categorical framework remains assigned to Volume IX.
- 2026-05-25 issue #464 pass: added a dedicated BEH mechanism section after
  matter representations and before finite-energy solitons.  The section
  derives the Abelian Higgs quadratic mixing, unitary-gauge
  gauge-invariant vector coordinate, \(R_\xi\) gauge fixing and propagator,
  ghost/Goldstone gauge-dependent masses, the nonabelian mass matrix and
  \(SU(2)\to U(1)\) pattern, and the BRST/power-counting role of \(R_\xi\)
  gauges.  The Goldstone-theorem chapter now cross-references this section.
- 2026-05-29 issue #597 pass: expanded the monopole collective-coordinate
  discussion by deriving the phase-coordinate dyon tower and Witten-effect
  charge-lattice shift from a finite-dimensional \(S^1\) quantum mechanics
  with the theta-angle total derivative fixed by the Chern--Weil boundary
  pairing.
- 2026-06-04 issue #597 Jackiw-Rebbi pass: added an explicit soliton
  quantization consequence rather than further moduli-space structure.  The
  chapter now solves the kink Dirac zero-mode equation, normalizes the
  \(\operatorname{sech}(mx)\) wavefunction, records the anti-kink chirality
  flip, and derives the \(\pm1/2\) soliton-sector fermion numbers from
  spectral pairing and the zero-mode operator.  The companion rejects integer
  zero-mode bookkeeping and unpaired nonzero spectra.
- 2026-06-01 issue #701 warning-scope pass: promoted the trace-form
  Yang--Mills coupling convention to a scannable warning block.  The warning
  states that the invariant datum is
  \(-\frac1{4g_{\mathrm{YM}}^2}\operatorname{tr}F^2\) for the
  matrix-valued curvature and that changing the generator trace normalization
  necessarily changes component coordinates and the component coordinate
  called \(g_{\mathrm{YM}}\).
- 2026-06-04 issue #780 pass: added a longitudinal-vector/Goldstone
  equivalence section after the BEH construction.  The pass keeps hypotheses
  before conclusions: \(R_\xi\) datum, restored Slavnov--Taylor identity,
  vector/Goldstone pole residues, high-energy \(m/E\) expansion, stable-pole
  LSZ versus unstable \(W/Z\) caveat, Abelian Higgs tree convention,
  electroweak \(W_LW_L\) scalar representative, and Higgs cancellation of the
  apparent \(s/v^2\) growth.
