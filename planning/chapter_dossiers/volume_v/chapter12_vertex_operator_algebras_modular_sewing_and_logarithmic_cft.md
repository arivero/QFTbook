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
- `C_2(V)`: span of \(a_{-2}b\), used in the explicit cofiniteness
  hypothesis for character modularity.
- `CB_{g,n}`: space of chiral conformal blocks.
- `q`: sewing parameter in \(zw=q\).
- `S,T`: genus-one modular matrices.
- `N_{ij}{}^k`: fusion coefficient.
- `d_i`: quantum dimension \(S_{i0}/S_{00}\).
- `M_{ij}`: full-CFT modular-invariant multiplicity matrix.
- `A(I)`: von Neumann algebra assigned by a conformal net to an interval
  `I subset S^1`.
- `Omega`: conformal-net vacuum vector.
- `mu_A`: complete-rational conformal-net `mu`-index.

## Claim Ledger

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
- Works the Ising Zhu algebra as
  \(\mathbb C[x]/(x(x-1/16)(x-1/2))\), matching the vacuum, spin, and energy
  top weights.
- Defines sewing of blocks through dual bases of a module and its dual, with
  the annulus propagation factor \(q^{h_a+n-c/24}\).
- States explicit rationality/sewing hypotheses before invoking modular
  tensor category language.
- States character modularity as a quoted theorem, separating the theorem
  input from the linear-algebraic Verlinde derivation.
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
- States the Carpi--Kawahigashi--Longo--Weiner strongly-local-VOA-to-net
  theorem and the Fredenhagen--Joerss converse under polynomial-energy-bound
  and FJ-field hypotheses.
- Proves the Ising conformal-net `mu`-index `4` from the displayed quantum
  dimensions and records the open problem for unqualified VOA/net
  equivalence.
- Defines rational full-CFT torus partition functions and the modular
  invariance constraints \(MS=SM\), \(MT=TM\).
- Derives the leading Cardy high-temperature partition-function asymptotic
  from modular invariance and a unique vacuum hypothesis.
- Defines logarithmic CFT by nonsemisimple \(L_0\) action, explains the
  appearance of logarithms, and identifies pseudo-traces and finite tensor
  category data as the replacement for semisimple modular data.

## Figure Ledger

- No figures in the initial chapter pass.  Sewing and modular moves are
  currently carried by equations and categorical data.

## Calculation Checks

- `calculation-checks/cft_voa_modular_checks.py` verifies the Ising modular
  \(S\)-matrix, Verlinde fusion coefficients, quantum dimensions, the
  conformal-net `mu`-index/global-dimension relation, character exponent
  shifts in \(\mathbb Q(\sqrt2)\), the \(T\)-phase spin-selection rule,
  uniqueness of the diagonal Ising genus-one modular invariant with one
  vacuum, and the Ising Zhu polynomial/idempotent decomposition over
  \(\mathbb Q\).

## Reference Intake

- Local source consulted:
  `references/02_2d_cft/conformal_nets_cklw_1503_01260/VOAtoNets_CKLW_2018.tex`.
  Used to check the precise hypotheses in the strongly-local VOA to
  conformal-net theorem, the Fredenhagen--Joerss reconstruction boundary,
  and the definitions of split property, strong additivity, and `mu`-index.
  The monograph text defines the net objects locally and quotes only the
  external theorem boundary.

## Audit Notes

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
