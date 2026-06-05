# Chapter 07: Four-Dimensional N=2 Gauge Dynamics And Seiberg-Witten Theory

## Source Position

Volume VII proceeds from four-dimensional `N=1` holomorphic dynamics to the
first `N=2` exact low-energy gauge-theory structure.  The chapter is placed
before moduli-space, lower-dimensional supersymmetric examples, and
localization so that special geometry, BPS central charges, and Abelian
Wilsonian dynamics are available for later use.

## Notation Inventory

- `G`, `g`, `r`: compact gauge group, Lie algebra, and rank.
- `T`, `B`, `Delta`, `B^circ`: assumed four-dimensional `N=2` QFT,
  Coulomb branch, discriminant locus, and smooth Abelian locus in the
  Seiberg-Witten Coulomb-branch datum.
- `S_l`, `L_l`: pure `su(2)` microscopic global/line datum and its absolute
  Wilson-'t Hooft line lattice, with `l in {SU(2), SO(3)+, SO(3)-}`.
- `Gamma`, `<-,->`: electromagnetic charge local system and integral Dirac
  pairing in the defining datum.
- `Gamma_part`: root-normalized local BPS-particle lattice with W-boson charge
  `(0,1)` and monopole charge `(1,0)`.
- `phi`, `u_k`: vector-multiplet scalar and gauge-invariant Coulomb
  coordinates.
- `a^I`, `a_{D,I}`, `F(a)`, `tau_IJ`: special coordinates, dual periods,
  prepotential, and Abelian coupling matrix.
- `K_F`, `g_{I bar J}`: rigid special-Kahler potential and scalar metric
  determined by the same prepotential in the local Abelian Wilsonian action.
- `gamma=(n_m^I,n_{e,I})`, `Z_gamma`: electromagnetic charge and central
  charge.
- `Sigma_u`, `lambda_SW`, `A_I`, `B^I`: Seiberg-Witten curve, differential,
  and symplectic cycle basis.
- `QFT-hypothesis`, `symmetry-derived`, `holomorphy-derived`,
  `special-geometry theorem`, `constraint-derived`, `consistency check`,
  `central conjecture`, `status boundary`: argument-status labels used in the
  Seiberg-Witten ledger.
- `<delta,gamma>`: rank-one specialization of the antisymmetric Dirac
  pairing.
- `Omega_C(gamma)`: protected one-particle BPS index in chamber `C`.
- `M_{Lambda^2}`, `M_{-Lambda^2}`, `M_infty`: monodromy matrices in the
  pure gauge-algebra `su(2)` example.
- `M_gamma`: Picard-Lefschetz monodromy associated to a massless
  hypermultiplet of charge `gamma=(n_m,n_e)`.
- `a_D^(m)`: local dual period branch that vanishes at the monopole point.
- `c_-`: nonzero local slope of the dyonic vanishing period at
  `u=-Lambda^2`.
- `k`: instanton number, normalized by the Volume II BPST convention.
- `q`: holomorphic instanton-counting coordinate; for pure `SU(N)`,
  identified with `Lambda^(2N)` after the scheme is fixed.
- `K`, `W`: ADHM vector spaces, with dimensions `k` and `N`.
- `B_1`, `B_2`, `I`, `J`: framed ADHM variables.
- `zeta`: real stability or noncommutative resolution parameter in the ADHM
  real moment map.
- `epsilon_1`, `epsilon_2`: equivariant rotation weights of the
  \(\Omega\)-background on `C^2`.
- `a_alpha`: Coulomb/framing weights for the `U(N)` ADHM torus action.
- `Y_alpha`, `vec Y`: Young diagrams labeling torus fixed points in the
  framed instanton compactification.
- `Z_inst`, `Z_k`: Nekrasov instanton partition function and its
  `k`-instanton coefficient.
- `u`, `v`, `x`, `y`, `lambda_AD`: local Argyres-Douglas cusp parameters,
  curve coordinates, and differential in the rank-one scaling model.

## Claim Ledger

- States the Seiberg-Witten Coulomb-branch datum as an upfront hypothesis:
  assumed `N=2` local QFT, vacuum branch and discriminant, electromagnetic
  charge local system with Dirac pairing, period section, local prepotential,
  Abelian Wilsonian action, singularity data, BPS convention, and optional
  curve realization.
- Defines the pure `su(2)` microscopic global/line datum
  `def:pure-su2-sw-global-line-datum`, separating the local particle lattice
  from the absolute `SU(2)`, `SO(3)+`, and `SO(3)-` Wilson-'t Hooft line
  choices.  Records `theta ~ theta+2pi` for `SU(2)` and `theta ~ theta+4pi`
  for fixed `SO(3)_pm`, with `theta -> theta+2pi` exchanging the two `SO(3)`
  variants.
- Adds central conjecture `conj:pure-su2-sw-low-energy-solution`: for a fixed
  global/line datum, the pure `su(2)` continuum theory has Coulomb branch
  `C_u`, discriminant `{Lambda^2,-Lambda^2}`, two-derivative Abelian
  Wilsonian action encoded by the displayed SW curve and differential, and
  protected prepotential data matching after scheme choice.
- Defines Coulomb-branch coordinates and repeats the monograph gauge-coupling
  convention at the first use of `N=2` gauge dynamics.
- Defines special coordinates, the prepotential, electric-magnetic duality,
  and the BPS central charge.
- Derives the rigid special-Kahler metric identity
  `g_{I bar J}=(2 pi)^(-1) Im tau_IJ` from
  `K_F=(2 pi)^(-1) Im(bar a^I F_I)`, and records how linear and real
  quadratic prepotential shifts affect only Kahler transformations or
  theta-angle coordinates.
- Proves local existence of the prepotential from symmetry of the period
  coupling.
- Defines the argument-status labels used for Seiberg-Witten reasoning and
  classifies the pure `su(2)` construction by QFT hypotheses,
  symmetry-derived input, holomorphy-derived input, special-geometry
  theorems, constraint-derived ansatz choices, consistency checks, and status
  boundaries, with the exact SW-to-QFT identification now labeled as the
  central conjecture.
- Defines the rank-one local BPS-particle electromagnetic pairing in the
  root-normalized W-boson convention and distinguishes it from the absolute
  `SU(2)`/`SO(3)` line lattice.
- Proves the
  Picard-Lefschetz hypermultiplet monodromy formula from the local
  \(\mathcal N=2\) hypermultiplet threshold
  `tau_sing=-(i/pi) log z`, including the origin of the factor two, its
  central-charge action, symplecticity, and unipotence.
- Derives the weak-coupling monodromy at infinity from the one-loop
  prepotential and the Weyl action `a -> -a`.
- Derives the residual `u -> -u` action from the anomalous `U(1)_R -> Z_8`
  symmetry, including the one-instanton zero-mode count
  `2 gauginos * 2 C_2(SU(2)) = 8`, the `R`-charge of the vector-multiplet
  scalar, and the generic `Z_4` stabilizer of a nonzero Coulomb-branch point;
  explains that the minimal two-singularity set is `{s,-s}` and that the
  chapter's strong-scale normalization chooses `s=Lambda^2`.
- Derives the finite monodromies from Picard-Lefschetz transformations for
  charges `(1,0)` and `(1,-1)`, and checks their product gives
  `M_infty`.
- Derives the pure `su(2)` curve
  `y^2=(x^2-Lambda^4)(x-u)` from the two finite singularities, the residual
  `u -> -u` action, nodal-fiber monodromy, and the weak-coupling cusp.
- Proves uniqueness of the displayed curve inside the stated minimal
  two-singularity hyperelliptic ansatz and displays the branch-point
  discriminant `4 Lambda^4 (u^2-Lambda^4)^2`.
- Displays hypergeometric representatives for the electric period and the
  monopole-vanishing dual period, and states the Picard-Fuchs equation
  `(u^2-Lambda^4) Pi'' + Pi/4 = 0`.
- Computes the monopole mass near `u=Lambda^2`:
  `M_(1,0)=|u-Lambda^2|/(sqrt(2)|Lambda|)+O(|u-Lambda^2|^2)`.
- Identifies the dyonic vanishing central charge `a_D-a` at `u=-Lambda^2`
  and records its linear mass behavior.
- Defines framed `U(N)` ADHM data, the complex and real moment-map equations,
  the role of the stability parameter, and the framing at infinity.
- Proves the ADHM dimension count:
  complex dimension `2kN`, real dimension `4kN`, and centered real dimension
  `4kN-4`.
- Separates the `U(N)` ADHM compactification from the `SU(N)` specialization
  `sum a_alpha=0`, and records the `U(1)` point-instanton caveat.
- States the equivariant fixed-point theorem for framed ADHM compactification
  with generic `a_alpha, epsilon_1, epsilon_2`, using `N`-tuples of Young
  diagrams as fixed-point labels.
- Defines the pure vector Nekrasov instanton function and displays the
  one-instanton `U(N)` fixed-point formula.
- Derives the pure `SU(2)` one-instanton fixed-point sum
  `Z_1=2/(epsilon_1 epsilon_2 (4a^2-(epsilon_1+epsilon_2)^2))`.
- Takes the Nekrasov prepotential limit and obtains the first pure
  `SU(2)` instanton coefficient `q/(2a^2)`, with `q=Lambda^4`.
- Records the instanton action/transseries ledger: the same `k`, action, and
  theta phase grade ADHM integrals, the \(\Omega\)-background partition
  function, and instanton sectors in a weak-coupling transseries.
- Defines the protected one-particle BPS index as a second helicity
  supertrace, with hypermultiplet index `+1` and vector index `-2`.
- Records the weak-chamber BPS-index seed as conjectural/semiclassical input:
  `Omega_wk(+/-(0,1))=-2`, `Omega_wk(+/-(1,n))=+1`, and no other primitive
  charges.  Monodromy transport is explicitly not used as a proof of
  existence or completeness.
- Records the strong-chamber BPS-index seed as conjectural input:
  only `+/-(1,0)` and `+/-(1,-1)` have primitive hypermultiplet index `+1`.
- States the rank-one KS wall-crossing automorphism and the elementary
  pentagon identity, while leaving the complete weak/strong spectrum-generator
  equality as a theorem-level obligation rather than inferred from monodromy.
- Defines a local rank-one Argyres-Douglas cusp model
  `y^2=x^3+v x+u` with `lambda_AD=u dx/y`, proves the scaling dimensions
  `[x]=2/5`, `[y]=3/5`, `[u]=6/5`, `[v]=4/5`, and records the status boundary
  separating local special-geometry scaling from a full QFT construction.
- Explains, in prose, the rank-two symplectic-lattice obstruction to putting
  mutually nonlocal light charges into a single electric polarization.
- Records the theorem boundary for turning Seiberg-Witten dynamics into a
  nonperturbative construction of four-dimensional supersymmetric QFT.

## Calculation Checks

- `calculation-checks/sw_su2_periods.py` verifies the monodromy matrices, the
  finite-monodromy product, Picard-Lefschetz central-charge action and
  symplecticity, the local hypermultiplet threshold shift that produces the
  factor two, the pure `su(2)` global-form line-lattice choices and
  Witten-effect theta shift, the root-normalized particle-charge convention,
  chamber BPS-index seed bookkeeping, the rigid special-Kahler metric identity
  and real
  theta-shift invariance, the one-instanton \(R\)-anomaly zero-mode count,
  the residual \(R\)-symmetry quotient action \(u\mapsto -u\), the
  two-singularity scale ledger, the exclusion of a single nodal finite
  singularity by the trace of \(M_\infty\), the minimal-curve discriminant,
  the Picard-Fuchs equation for the displayed hypergeometric periods, the
  large-\(u\) asymptotic of \(a(u)\), logarithmic growth of \(a_D(u)\), linear
  vanishing of \(a_D\) at the monopole point, and the rank-one Argyres-Douglas
  cusp scaling dimensions.
- `calculation-checks/susy_instanton_nekr_checks.py` verifies the ADHM
  dimension count, trace-delta to half-trace instanton-action conversion,
  the pure `SU(2)` one-instanton Nekrasov fixed-point sum, the first
  Nekrasov prepotential coefficient, and the Young-diagram count for
  one-box fixed points.

## Source Notes

- `references/susy_gauge_dynamics_localization/issue588_sw_rigor/` stores
  local arXiv source payloads for the original Seiberg-Witten and
  Argyres-Douglas/Argyres-Plesser-Seiberg-Witten papers.  They are source
  leads and convention checks only; the chapter supplies its own definitions,
  hypotheses, derivations, and status boundaries.
- String compactification and superstring constructions are out of scope for
  this chapter and this monograph.

## Figure Ledger

No figure is included in this pass.  Future figures should include the
two-singularity \(u\)-plane with monodromy loops and a branch-cut picture of
the elliptic curve cycle degeneration.

## Anti-Wrapper Audit

- 2026-05-29: demoted the cusp discriminant calculation to a worked paragraph.
  The discriminant formula is still shown because it identifies the collision
  of two nodal fibers, but the proof is elementary cubic algebra rather than a
  theorem-level QFT or special-geometry result.
- 2026-05-29: demoted the mutually nonlocal electric-frame obstruction from
  proposition/proof form to conceptual linear-algebra prose.  The obstruction
  remains explicit because it is the local reason an Argyres-Douglas collision
  is not described by a single weakly coupled electric Abelian frame.
- 2026-06-02 residual-\(R\) pass: expanded the compressed sentence placing the
  two pure `su(2)` finite singularities into a derivation from the anomalous
  `U(1)_R -> Z_8` symmetry, including the instanton zero-mode count, the
  charge-four action on `u`, the generic `Z_4` stabilizer, the resulting
  quotient action `u -> -u`, the trace obstruction to representing
  \(M_\infty\) by one nodal hypermultiplet monodromy, and the dimension-two
  scale normalization \(s=\Lambda^2\).  Added the corresponding finite
  arithmetic to `sw_su2_periods.py`.
- 2026-06-05 issue #801 SW foundation split: added the pure `su(2)`
  global/line datum and central low-energy SW conjecture, separated the local
  BPS-particle lattice from `SU(2)`/`SO(3)` absolute line choices, replaced the
  monodromy-derived spectrum phrasing by protected-index weak/strong chamber
  conjectural seeds, and recorded the KS wall-crossing product obligation.
