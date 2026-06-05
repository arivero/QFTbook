# Chapter 12: Vertex Operator Algebras, Modular Sewing, and Logarithmic CFT

## Source Position

This chapter is the first dedicated Volume V algebraic two-dimensional CFT
chapter after the sigma-model, WZW, Narain, orbifold, and twist-field chapter.
It absorbs the non-ghost chiral-algebra and modular-sewing material required
by the stringbook crosswalk while excluding bc and beta-gamma systems from the
current QFT scope.

## Notation Inventory

- `V`: vertex operator algebra.
- `Y(a,z)`: state-field map \(\sum_m a_m z^{-m-1}\).
- `1`: vacuum vector.
- `omega`: conformal vector whose modes are \(L_n\).
- `c`: chiral central charge.
- `M_i`: simple ordinary \(V\)-module.
- `chi_M(tau)`: character \(\operatorname{Tr}_M q^{L_0-c/24}\).
- `O(V)`: Zhu subspace spanned by \(a\circ b\).
- `A(V)`: Zhu algebra \(V/O(V)\) with product induced by `*`.
- `Omega(M)`: subspace killed by modes above their zero-mode threshold.
- `g(V)`, `a[m]`: mode Lie algebra used in the induction mechanism behind
  Zhu classification, with degree \(\Delta_a-m-1\).
- `M_ind(U)`: induced graded module generated from a simple Zhu-algebra
  module `U`.
- `C_2(V)`: span of \(a_{-2}b\), used in the explicit cofiniteness
  hypothesis for character modularity.
- `Y[a,z]`, `a[n]`: Zhu square-bracket field and modes.
- `Z_i(v,tau)`: torus trace function
  \(\operatorname{Tr}_{M_i}o(v)q^{L_0-c/24}\).
- `wp(z,tau)`, `G_{2k}(tau)`: Weierstrass kernel and Eisenstein series
  entering the genus-one trace recursion.
- `M(c,h)`: Virasoro Verma module with central charge `c` and highest weight
  `h`.
- `c_m`: unitary minimal-model central charge `1 - 6/(m(m+1))`.
- `h_{r,s}^{(m)}`: Kac-table highest weight for the unitary minimal model
  `M(m,m+1)`.
- `J(r,s)`: Kac-table field-identification involution
  `(r,s) -> (m-r,m+1-s)`.
- `n^{(k)}_{ab}{}^c`: \(SU(2)_k\) fusion coefficient used in the finite
  quotient formula for unitary minimal-model fusion.
- `F_0,F_epsilon`: Ising spin four-point Virasoro block basis in the identity
  and energy channels.
- `mathcal L`, `Gamma`: Coulomb-gas rank-one local system of the multivalued
  screening integrand and a twisted cycle with
  \(\partial_{\mathcal L}\Gamma=0\).
- `CB_{g,n}`: space of chiral conformal blocks.
- `q`: sewing parameter in \(zw=q\).
- `G_tau`, `E_tau`, `C_tau`: genus-one free-boson Green kernel, elliptic curve
  \(\mathbb C/(\mathbb Z+\tau\mathbb Z)\), and normal-ordering constant fixed
  after the scalar zero mode is removed.
- `S,T`: genus-one modular matrices.
- `N_{ij}{}^k`: fusion coefficient.
- `d_i`: quantum dimension \(S_{i0}/S_{00}\).
- `M_{ij}`: full-CFT modular-invariant multiplicity matrix.
- `F_i(v;tau)`: chiral torus one-point block
  `Tr_{M_i} o(v) q^{L_0-c/24}`.
- `D_a`: Verlinde topological defect labelled by a simple chiral object `a`
  in the diagonal rational full CFT.
- `lambda_a(i)`: defect eigenvalue `S_{ai}/S_{0i}` on the diagonal sector
  `M_i otimes overline{M_i^vee}`.
- `N(E)`: cumulative positive spectral counting function used in the Cardy
  Tauberian argument.
- `A`: coefficient of the high-temperature Laplace asymptotic
  `log Z(beta)=A/beta+o(beta^-1)`.
- `B`: candidate coefficient in the cumulative growth
  `log N(E) sim B sqrt(E)`.
- `E_beta`: Laplace-saddle energy `B^2/(4 beta^2)`, equal to
  `A/beta^2` after matching.
- `X_{BA}, mu_{BA}, K_x`: nonrational direct-integral spectral label space,
  Plancherel measure, and multiplicity/descendant fiber for a radial product.
- `F_st`: measurable fusing transform between direct-integral channel
  decompositions.
- `V_f`: noncompact free-boson exponential smeared over the real momentum
  shift label.
- `Z_R^dens`: noncompact free-boson torus partition density per unit target
  volume, proportional to `tau_2^{-1/2}|eta|^{-2}`.
- `A(I)`: von Neumann algebra assigned by a conformal net to an interval
  `I subset S^1`.
- `Omega`: conformal-net vacuum vector.
- `mu_A`: complete-rational conformal-net `mu`-index.
- `rho,sigma`: DHR localized endomorphisms representing finite-index chiral
  net sectors.
- `Hom(rho,sigma)`: DHR intertwiner space.
- `epsilon_{rho,sigma}`: charge-transporter braiding intertwiner from
  `rho sigma` to `sigma rho`.
- `d_rho`: DHR statistical dimension, the square root of the Jones index of
  `rho(A(I)) subset A(I)`.
- `mathcal D`: square root of the categorical global dimension
  `sum_lambda d_lambda^2`.
- `H^infty`: common smooth domain `cap_k Dom(1+L_0)^k` for smeared VOA
  fields.
- `Y(a,f)`: smooth smearing of a VOA field, defined by the Fourier-mode
  series `sum_n hat f_n a_n`.
- `C,D`: states forming a rank-two logarithmic Virasoro pair of weight `h`.
- `mathcal C, mathcal D`: corresponding chiral fields.
- `N`: nilpotent operator on the logarithmic pair, with `ND=C` and `NC=0`.
- `b,d`: constants in logarithmic two-point functions; `b` is invariant under
  `D -> D + lambda C`, while `d` is basis-dependent.
- `A`: finite-dimensional associative algebra used in the logarithmic
  pseudo-trace model.
- `P`: finitely generated projective left `A`-module.
- `phi`: symmetric linear functional on `A`, used to pair the
  Hattori-Stallings trace with a complex number.
- `ptr_P^phi`: finite projective pseudo-trace
  `sum_r phi(f^r(T p_r))`.

## Claim Ledger

- Adds a chapter-level theorem-boundary ladder separating formal VOA and
  finite-level algebra, fixed-channel analytic block estimates, global sewing
  across moduli space, and operator-algebraic conformal-net locality.  The
  ladder also distinguishes rational semisimple, nonrational direct-integral,
  and logarithmic/nonsemisimple mechanisms so later local calculations are
  read as proof-boundary exposure rather than as a completed all-surface CFT
  construction.
- Gives a self-contained VOA definition with grading, vacuum, state-field
  map, conformal vector, translation, and locality axioms.
- Derives the chiral OPE expansion from VOA locality and lower truncation.
- Defines ordinary modules, characters, and chiral conformal blocks as Ward
  identity functionals on pointed Riemann surfaces.
- Defines Zhu's products \(a*b\), \(a\circ b\), the quotient algebra
  \(A(V)=V/O(V)\), and the zero-mode top-level action on ordinary modules.
- Records the component Jacobi identity used in the Zhu top-level calculation,
  proves that \(O(V)\) acts trivially on lowest-energy spaces and that
  \(o_M(a*b)=o_M(a)o_M(b)\) there, and states the classification theorem with
  explicit CFT-type, ordinary-module, rationality, and \(C_2\)-cofiniteness
  hypotheses.
- Spells out the induction mechanism behind Zhu classification: the mode Lie
  algebra, triangular degree, top-level positive-mode annihilation, induced
  module from an \(A(V)\)-module, Jacobi-relation quotient, and irreducible
  ordinary quotient boundary.
- Works the Ising Zhu algebra as
  \(\mathbb C[x]/(x(x-1/16)(x-1/2))\), matching the vacuum, spin, and energy
  top weights.
- Adds the unitary Virasoro minimal-model layer: derives the level-one and
  level-two Gram matrices, states the unitary highest-weight classification as
  a quoted theorem boundary, exposes the Kac-determinant/positivity mechanism
  behind that boundary, records the Kac-table identification and triangular
  representative set, proves the full unitary minimal-model \(S,T\) modular
  data as a proposition conditional on the Rocha--Caridi character formula,
  derives the \(S\)-matrix by Poisson summation and cosine-to-sine reduction,
  proves the finite \(SU(2)\)-quotient fusion rule from Verlinde, derives the
  Ising spin level-two null vector, and proves the Ising spin four-point
  BPZ/crossing calculation fixing
  \(C_{\sigma\sigma\varepsilon}=1/2\).
- Makes the Coulomb-gas screening construction more precise by defining the
  rank-one local system of the multivalued screening integrand, the twisted
  cycle condition, and the twisted-Stokes proof that integrated screenings
  commute with the Virasoro modes under the neutrality condition.
- Adds the two-screening Dotsenko--Fateev Selberg chamber, displaying the
  \(n=2\) gamma-function formula, the ordered-chamber finite polynomial
  expansion, and the screening--screening Vandermonde exponent as the first
  genuinely multi-screening datum.
- Adds a screening-to-BPZ construction budget that separates raw
  Dotsenko--Fateev integrals, Virasoro Ward/intertwiner checks, closed
  twisted-cycle projection, BPZ solution-basis comparison, analytic
  continuation, and nonchiral sewing pairing into five residuals rather than
  treating a screening integral as a full correlator.
- Defines sewing of blocks through dual bases of a module and its dual, with
  the annulus propagation factor \(q^{h_a+n-c/24}\).
- Adds a concrete torus free-boson period-kernel example: the scalar Green
  function solves the Laplacian equation only after constant-mode subtraction,
  neutral normal-ordered vertex correlators are built from pairwise Green
  kernels, non-neutral products vanish by zero-mode integration, and the
  higher-genus prime-form/Szego-kernel objects are identified as the next
  analytic inputs rather than consequences of graph-genus bookkeeping.
- Expands the finite sewing-graph estimate: after finite-level truncation,
  continuity of each vertex block gives a pointwise operator-norm bound,
  absolute values separate the internal edge labels, the cutoff contraction is
  bounded by
  \(\prod_v\|\mathcal F_v\|\prod_e\|P_{a_e}(q_e)\|_1\), and basis
  independence follows from trace-norm convergence of the tensor product of
  edge propagators.
- States explicit rationality/sewing hypotheses before invoking modular
  tensor category language.
- States character modularity as a quoted theorem, separating the theorem
  input from the linear-algebraic Verlinde derivation.
- Adds the finite trace-recursion mechanism behind character modularity:
  square-bracket fields, the Weierstrass kernel, the genus-one Ward recursion
  for \(Z_i(a[-2]b,\tau)\), and the role of \(C_2\)-cofiniteness in producing
  finite modular differential systems before the analytic theorem boundary.
- Proves the Verlinde formula from simultaneous diagonalization by the
  modular \(S\)-matrix.
- Works the Ising chiral theory explicitly: \(c=1/2\), three simple modules,
  \(S_{\rm Ising}\), \(T_{\rm Ising}\), quantum dimensions, fusion rules, and
  the finite genus-one proof that the diagonal full-CFT modular invariant is
  the unique nonnegative invariant with one vacuum on the Ising label set.
- Defines chiral conformal nets on `S^1`: interval algebras, isotony,
  locality, Moebius/diffeomorphism covariance, positive energy, vacuum
  cyclicity, irreducibility, split property, strong additivity, `mu`-index,
  and complete rationality.
- States the complete-rational conformal-net representation-category theorem
  as a quoted theorem and records `mu_A=sum d_rho^2`.
- Expands the local DHR mechanism behind the complete-rationality theorem:
  localized endomorphisms, intertwiner spaces, tensor product by composition,
  statistical dimensions from Jones index, conjugate equations,
  charge-transporter braiding, the two-interval index, categorical trace
  formula for the modular \(S\)-matrix, and the transparent-sector
  nondegeneracy criterion.
- States the Carpi--Kawahigashi--Longo--Weiner strongly-local-VOA-to-net
  theorem and the Fredenhagen--Joerss converse under polynomial-energy-bound
  and FJ-field hypotheses.
- Expands the local mechanism behind the strongly-local VOA/net theorem:
  polynomial energy bounds, convergence of smooth smeared fields, closability
  from the unitary adjoint formula, the distinction between common-domain
  field locality and von Neumann locality, covariance of smeared fields,
  and the Fredenhagen--Joerss reconstruction route from finite-energy vectors
  to affiliated fields and a VOA state-field map.
- Proves the Ising conformal-net `mu`-index `4` from the displayed quantum
  dimensions and records the open problem for unqualified VOA/net
  equivalence.
- Defines rational full-CFT torus partition functions and the modular
  invariance constraints \(MS=SM\), \(MT=TM\).
- Defines chiral torus one-point trace blocks, states Zhu modular covariance
  with the primary weight factor and explicit rationality/\(C_2\)-cofiniteness
  hypotheses, expands the one-point modular mechanism through coordinate
  transport on the once-punctured torus, primary versus descendant mixing,
  finite \(C_2\)-cofinite trace systems, and explains why full-CFT torus
  one-point functions constrain OPE tensors beyond the scalar partition
  function.
- Defines diagonal Verlinde topological defects \(D_a\), proves their fusion
  from the simultaneous diagonalization form of the Verlinde formula, proves
  the temporal-defect to spatial-defect modular \(S\)-move, and works the
  Ising spin-flip and Kramers--Wannier defect lines including the spin-field
  one-point selection rule.
- Derives the leading Cardy high-temperature partition-function asymptotic
  from modular invariance and a unique vacuum hypothesis, states the
  exponential Tauberian theorem needed to pass from the partition function to
  cumulative state growth, proves the elementary Laplace upper bound, explains
  the nontrivial Tauberian lower-bound input, checks the Legendre saddle
  coefficient, and proves the CFT-internal Cardy density formula under
  compact/discrete-spectrum/positivity hypotheses.
- Defines nonrational radial products by direct-integral spectral data and
  states the Plancherel form of four-point OPE/crossing identities.
- Works the noncompact free boson as the basic continuous-spectrum example:
  Hilbert space as a direct integral over real momentum, smeared exponential
  fields as momentum-shift distributions, weighted-convolution OPE, the
  charge-associativity exponent identity, the modular invariant partition
  density per unit target volume, and the compact-circle decompactification
  limit.
- Defines logarithmic CFT by nonsemisimple \(L_0\) action, introduces a
  rank-two logarithmic Virasoro pair, derives finite state and field scaling,
  proves the logarithmic two-point functions from the \(L_0\) and \(L_1\)
  Ward identities, records the basis dependence of the constant term, and
  explains why ordinary characters miss the nilpotent extension data.
- Defines the finite projective pseudo-trace mechanism: a symmetric functional
  on a finite algebra paired with the Hattori-Stallings trace on a projective
  module, with cyclicity following from symmetry.  The dual-number regular
  module example shows explicitly that ordinary trace gives only the
  generalized eigenspace dimension while the pseudo-trace detects the
  nilpotent \(\tau\)-coefficient in \(q^{L_0-c/24}\).
- Identifies generalized characters, pseudo-traces, projective modules,
  modified traces, and braided finite tensor category data as the honest
  replacement for semisimple modular data in logarithmic CFT, with the full
  logarithmic modular-closure theorem kept at theorem-boundary status.

## Figure Ledger

- No figures in the initial chapter pass.  Sewing and modular moves are
  currently carried by equations and categorical data.

## Calculation Checks

- `calculation-checks/cft_voa_modular_checks.py` verifies the Ising modular
  \(S\)-matrix, Verlinde fusion coefficients, quantum dimensions, the
  conformal-net `mu`-index/global-dimension relation, the DHR categorical
  \(S\)-matrix vacuum row and trivial Ising transparent sector, character
  exponent shifts in \(\mathbb Q(\sqrt2)\), smooth-smearing convergence from
  a polynomial energy bound and rapidly decaying Fourier coefficients, the
  \(T\)-phase spin-selection rule,
  uniqueness of the diagonal Ising genus-one modular invariant with one
  vacuum, the finite multi-edge sewing trace-norm bound and paired
  internal-edge relabelling invariance, Verlinde defect eigencharacters,
  exact temporal-to-spatial defect
  \(S\)-move multiplicities, the Ising spin-field one-point selection rule,
  the Cardy Tauberian Laplace-bound and Legendre-saddle coefficients, and the
  Ising Zhu
  polynomial/idempotent decomposition over \(\mathbb Q\), as well as the
  rank-two logarithmic Jordan-cell Ward identities, basis shift, and ordinary
  trace invisibility of the nilpotent part.  It also verifies the dual-number
  projective pseudo-trace model: \(\varphi_{\rm res}(a+b\epsilon)=b\) is
  cyclic, ordinary vector-space trace kills the nilpotent coefficient, and
  the projective pseudo-trace extracts the \(\tau\)-coefficient in the Jordan
  cell.
- `calculation-checks/cft_virasoro_minimal_checks.py` verifies the unitary
  minimal-model Kac-table arithmetic, Ising and tricritical-Ising weights,
  the Rocha--Caridi theta-character Poisson coefficient identities for the
  A-series minimal-model \(S\)-matrix, \(S^2\), Verlinde integrality and
  agreement with the exact \(SU(2)\)-quotient fusion rule, level-two Ising
  Gram determinant/null vector, the level-two Kac determinant roots
  \(h_{1,2}\) and \(h_{2,1}\), the one-screening beta integral and
  two-screening Selberg finite-sum/factorial identity, the finite
  screening-to-BPZ residual telescope and norm bound, Ising BPZ block
  differential equation, and the crossing matrix fixing
  \(C_{\sigma\sigma\varepsilon}=1/2\).

## Reference Intake

- Local source consulted:
  `references/02_2d_cft/conformal_nets_cklw_1503_01260/VOAtoNets_CKLW_2018.tex`.
  Used to check the precise hypotheses in the strongly-local VOA to
  conformal-net theorem, the Fredenhagen--Joerss reconstruction boundary,
  and the definitions of split property, strong additivity, and `mu`-index.
  The monograph text defines the net objects locally and quotes only the
  external theorem boundary.
- Internal source consulted for the unitary Virasoro pass:
  `transcription/tex/253c/conformal_field_theory.tex`, pp. 116--135 source
  block, and `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`
  around the Ising minimal-model four-point and torus discussion.  The
  monograph gives local Gram/BPZ/crossing derivations and treats the full
  unitary classification as a quoted theorem boundary.

## Audit Notes

- 2026-06-03 VOA/modular architecture pass: inserted a front-of-chapter
  architecture ladder that organizes the existing Zhu, modularity, conformal
  net, sewing, nonrational, and logarithmic inserts into four layers:
  formal chiral algebra, fixed-channel analytic estimates, global sewing, and
  operator-algebraic locality.  This is a coherence/depth pass for #697/#625;
  it does not claim to prove rational sewing, conformal-net complete
  rationality, strong-locality correspondence, nonrational sewing, or
  logarithmic modular closure.
- 2026-05-26 issue #584 pass: added the VOA/modular-sewing/logarithmic-CFT
  chapter, included it in Volume V, and added the Ising modular-data
  calculation check.
- 2026-05-26 conformal-net pass: added the operator-algebraic conformal-net
  framework, complete-rationality and strongly-local-VOA theorem boundaries,
  the Ising `mu`-index check, and the open problem for unqualified VOA/net
  equivalence.
- 2026-05-26 Zhu-algebra pass: inserted the Zhu algebra/top-level module
  section, made the theorem hypotheses explicit, and added exact Ising
  Zhu-polynomial/idempotent checks.
- 2026-05-27 Ising full-CFT modular-invariant pass: added the Ising
  \(T\)-matrix, proved that the genus-one modular-invariance equations force
  the diagonal invariant under the one-vacuum/nonnegative-integral
  hypothesis, and extended the exact modular-data check.
- 2026-05-27 Cardy Tauberian pass: made the analytic Tauberian hypothesis
  explicit, proved the CFT-internal cumulative Cardy growth statement from
  modular invariance plus positivity/discreteness assumptions, and added the
  saddle coefficient check.
- 2026-05-27 logarithmic Jordan-cell pass: expanded logarithmic CFT from a
  status paragraph into a self-contained rank-two local derivation, including
  finite logarithmic scaling, \(L_0/L_1\) Ward-identity two-point functions,
  basis-dependence bookkeeping, the ordinary-character failure mode, and exact
  formal calculation checks.
- 2026-06-01 issue #697 logarithmic pseudo-trace pass: added the finite
  projective Hattori-Stallings pseudo-trace construction and the dual-number
  regular-module model showing how pseudo-traces detect nilpotent extension
  data invisible to ordinary characters.
- 2026-05-27 unitary Virasoro minimal-model pass: incorporated the 253c and
  stringbook Ising/minimal-model material into Chapter 12 by deriving the
  low-level Virasoro Gram/null-vector algebra, stating the unitary
  minimal-model classification boundary, proving the Ising BPZ block/crossing
  calculation fixing \(C_{\sigma\sigma\varepsilon}=1/2\), and adding a
  dedicated conformal-block calculation check script.
- 2026-05-27 unitary minimal-model modular-data pass: added the full A-series
  \(S,T\) data for \(\mathcal M(m,m+1)\), made the Kac-field-identification
  quotient normalization explicit, proved the finite \(SU(2)\)-quotient
  fusion rule, and extended the minimal-model calculation companion to check
  modular orthogonality and Verlinde fusion for \(m=3,\ldots,7\).
- 2026-05-27 torus one-point/defect-line pass: added Zhu torus one-point
  trace blocks, the modular-covariance theorem boundary with explicit
  hypotheses, diagonal Verlinde defect operators, the temporal/spatial defect
  modular \(S\)-move, Ising spin-flip and Kramers--Wannier examples, and exact
  defect-line arithmetic checks.
- 2026-05-29 anti-wrapper pass: strengthened the proof that VOA locality gives
  the chiral OPE by spelling out lower truncation, formal residue extraction
  of the singular coefficients, regularity after multiplication by
  \((z-w)^N\), and matrix-element equality in the \(|z|>|w|\) expansion.
- 2026-05-30 quoted-theorem proof-debt pass: expanded the local mechanisms
  behind Zhu classification and rational-character modularity.  The chapter
  now displays the mode Lie algebra/induction construction and the
  genus-one trace recursion that make the quoted analytic theorem boundaries
  concrete.
- 2026-05-30 conformal-net DHR proof-debt pass: expanded the
  complete-rational-net theorem boundary by defining DHR localized
  endomorphisms, intertwiners, finite-index dimensions, conjugates,
  charge-transporter braiding, categorical \(S\)-matrix normalization, and
  the transparent-sector criterion; added an exact Ising DHR
  nondegeneracy check.
- 2026-05-30 strongly-local VOA/net mechanism pass: expanded the CKLW/FJ
  theorem boundary by deriving the smooth-field smearing estimate from
  polynomial energy bounds, isolating the strong-locality upgrade from
  common-domain commutators to von Neumann locality, and spelling out the
  finite-energy vector-to-field reconstruction mechanism; added an exact
  smooth-smearing tail check.
- 2026-05-30 torus one-point modular mechanism pass: expanded the
  Zhu one-point modular covariance theorem boundary by spelling out
  zero-mode trace finiteness, primary coordinate weight, descendant
  quasimodular mixing, the finite marked-state trace system from
  \(C_2\)-cofiniteness, and the remaining analytic modular-closure input.
- 2026-06-01 Moore--Seiberg defect-junction pass: expanded the
  Moore--Seiberg system from a named pentagon/hexagon reference into the
  physical topological-line and junction-space datum used in the defect
  category chapters.  The text now defines the fusion spaces \(V_{ij}^{k}\),
  the \(F\)-move between the two four-point pants bases, the \(R\)-move,
  associator pentagon, braiding hexagon, and balancing identity, while
  keeping the analytic QFT construction of Hilbert space, positive pairing,
  correlation functions, and sewing maps as the real theorem boundary.
- 2026-05-30 unitary Virasoro classification boundary pass: expanded the
  minimal-model classification theorem boundary with the Kac determinant
  formula, the \(b^2=m/(m+1)\) interlacing mechanism, the all-level positivity
  and exhaustion roles of the quoted theorem, and an exact level-two Kac-root
  calculation check.
- 2026-06-02 minimal-model modular-data dequote pass: converted the unitary
  minimal-model \(S,T\) matrix formula from quoted-theorem form into a local
  proposition conditional on the Rocha--Caridi character formula.  The true
  external representation-theory boundary is now the singular-vector
  resolution/character formula, while the modular matrix is proved by
  Poisson summation, Kac-orbit quotient normalization, and the existing exact
  minimal-model calculation check.
- 2026-05-31 Coulomb-gas screening proof pass: strengthened the screening
  intertwiner lemma by defining the local system and twisted boundary
  condition, proving the Virasoro commutator as a twisted exact derivative,
  and deriving the neutrality condition from the background charge at
  infinity before invoking meromorphic continuation.
- 2026-06-03 two-screening Selberg pass: extended the Coulomb-gas
  Dotsenko--Fateev section beyond the one-screening beta integral by adding
  the \(n=2\) Selberg chamber, its finite ordered-chamber polynomial
  expansion, and exact rational checks comparing that expansion with the
  factorial Selberg formula.
- 2026-06-03 screening-to-BPZ budget pass: added a finite construction
  budget from Dotsenko--Fateev screening coordinates through twisted cycles,
  BPZ basis comparison, analytic continuation, and nonchiral sewing pairing;
  the paired calculation check verifies the residual telescope and norm
  bound.
- 2026-05-31 Cardy Tauberian mechanism pass: expanded the quoted
  exponential-Tauberian boundary by proving the elementary positive-measure
  Laplace upper bound, isolating the nontrivial Tauberian lower-bound input,
  deriving the Legendre coefficient relation \(B^2=4A\), and strengthening
  the exact calculation check to match this logic.
- 2026-06-01 noncompact free-boson direct-integral pass: added a worked
  continuous-spectrum example in which labelled exponential fields are
  momentum-shift distributions, Hilbert vectors are smeared wave packets, the
  leading OPE is weighted convolution over the Plancherel label, and the
  torus zero-point function is a modular invariant trace density rather than
  a finite trace.  Extended `nonrational_cft_direct_integral_checks.py` with
  the exact charge-associativity and modular-weight cancellations.
- 2026-06-01 rational sewing trace-bound pass: replaced the compressed
  finite-graph sewing estimate by explicit cutoff, pointwise vertex-norm,
  edge trace-norm, and trace-class tensor-product bookkeeping, and extended
  `cft_voa_modular_checks.py` with an exact triangle-graph sewing bound plus
  paired internal-edge relabelling invariance check.
- 2026-06-02 issue #705 bibliography-population pass: attached source-trace
  citations to the chapter's main quoted-theorem boundaries for Zhu
  classification, unitary Virasoro minimal-model classification, minimal-model
  modular data, rational-character modularity, complete-rational conformal
  nets, strongly local VOAs/conformal nets, Zhu torus one-point modular
  covariance, and the exponential Tauberian input used in Cardy asymptotics.
  Added the missing bibliographic-guide entries for FQS, GKO,
  Kawahigashi--Longo--Muger, CKLW, and regular variation.
- 2026-06-05 issue #625 torus free-boson kernel pass: added
  `ex:torus-free-boson-green-kernel`, giving an explicit genus-one scalar
  Green-function and vertex-correlator computation with zero-mode subtraction,
  normal-ordering convention, neutrality, and prime-form/Szego higher-genus
  boundary.  Extended `cft_higher_genus_sewing_checks.py` with a finite
  discrete-torus Laplacian/Green-kernel check and negative controls for
  non-neutral sources, diagonal self-contractions, and untransported Green
  constants.
