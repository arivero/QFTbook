# Build Audit: Issue #607 Planar N=4 Integrability Depth Pass

## Scope

- Branch: `codex/planar-n4-integrability`.
- Issue: #607, with cross-cutting relevance to #606.
- Files edited:
  - `monograph/tex/volumes/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.tex`
  - `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
  - `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
  - `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
  - `planning/chapter_dossiers/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.md`
  - `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`
  - `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`
  - `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`
  - `calculation-checks/planar_n4_integrability_checks.py`

## Source Spine Checked

- `planning/agent_handoffs/00_common_agent_contract.md`
- `planning/agent_handoffs/README.md`
- `planning/agent_handoffs/01_planar_n4_integrability_depth_pass.md`
- `planning/12_strict_writing_harness.md`
- `claude_review.md`
- GitHub issues #607, #606, and #608 for scope exclusion.
- Stringbook source:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, especially
  `integrabilitychapter`, mirror TBA/QSC, Konishi wrapping, and
  Maldacena-Wilson/cusp/Bremsstrahlung sections.
- Stringbook calculation notebooks located:
  - `/Users/xiyin/ResearchIdeas/stringbook/codes/su(2|2) spin chain.nb`
  - `/Users/xiyin/ResearchIdeas/stringbook/codes/BES equation.nb`
  - `/Users/xiyin/ResearchIdeas/stringbook/codes/mirror TBA and wrapping corrections.nb`

## Full-Draft Orientation

- Reviewed the compiled monograph table of contents and volume include map
  after the forced build.
- Reviewed `frontmatter_volume_dependency_guide.tex` to keep the lane aligned
  with the monograph's dependency order.
- Reviewed the relevant cross-volume support chapters:
  - Vol VI algebraic Bethe ansatz and nested Bethe-Yang chapters, used here
    only as algebraic background;
  - Vol VI mirror-channel TBA chapter, used to keep the mirror/TBA language
    distinct from planar N=4 mirror kinematics;
  - Vol VII supersymmetric localization chapter, used for the status boundary
    of the Bremsstrahlung/localization formula;
  - Vol IX line-operator chapter, used for the general defect/Wilson-line
    definition discipline.

## Mathematical Additions

- Added planar single-trace inner product and spectral-datum definition.
- Added two-site scalar mixing proposition for the one-loop `SU(2)` sector.
- Added BMN scaling check, `su(2|2)_c` matrix-amplitude structure, dressing
  phase status ledger, nested-root first step, bound-state dispersion, and
  large-spin cusp scaling data.
- Added mirror-sheet status, Hirota-to-Y-system derivation, and Konishi
  four-loop wrapping coefficient assembly.
- Added QSC asymptotic coefficient constraints, small-spin Bessel-ratio
  expansion, and Maldacena-Wilson/cusp/Bremsstrahlung interface.

## Continuation Pass

- Added the full one-loop `SO(6)` scalar density `K+2I-2P` and its
  holomorphic `SU(2)` reduction.
- Added an explicit convention ledger aligning the monograph with the
  stringbook integrability convention `h=g=sqrt(lambda)/(4 pi)` and warning
  about reciprocal scalar-factor conventions in the literature.
- Corrected the Zhukovsky energy formula to
  `H=-1-2ig(x^+-x^-)=1+2ig(1/x^+-1/x^-)` and added a proof from the
  physical branch.
- Added physical-branch Zhukovsky map data, large-`u` expansion, cut
  reciprocal boundary values, shifted branch-point crossing paths, Janik
  scalar crossing, and the BES `chi(x,y)` contour-integral representation
  with sheet caveats.
- Derived the mirror bound-state dispersion from double Wick rotation and
  recorded the mirror-kernel datum and mirror Bethe-string node inventory.
- Added analytic Y-system data: shifted strips, meromorphy domains,
  discontinuities, and exact-root regularity conditions.
- Added QSC Pfaffian normalization, a rank-two discontinuity consistency
  lemma, the dual `Qomega` system, an explicit Konishi Baxter polynomial, and
  the scalar hexagon factor with crossing-path caveat.

## Comprehensive Development Continuation

- Downloaded local study copies of key planar-integrability TeX sources under
  `references/planar_n4_integrability/` for convention checking:
  Bajnok--Janik `0807.0399`, Arutyunov--Frolov `0901.1417` and `0903.0141`,
  and Arutyunov--Frolov--Suzuki `1002.1711`.  These are local study cache
  files and should not be staged.
- Tightened Chapter 13 by adding an explicit asymptotic Bethe--Yang regime
  assumption: ABA is a long-chain quantization rule, applicable to fixed or
  controlled high-density root configurations as `L -> infinity`, with
  wrapping/mirror winding suppressed; it is not thermodynamic Bethe ansatz.
- Rebuilt the leading Konishi wrapping derivation in Chapter 14 from the
  stringbook spine:
  weak mirror branch, leading `Y_Q^{(0)}(u)`, mirror momentum measure
  `d tilde p_Q/du=2+O(g^2)`, `q=2u` rational integral, residue summand,
  telescoping rational tail, and the final
  `324 + 864 zeta(3) - 1440 zeta(5)` coefficient.
- Made the conceptual assumptions explicit: one-loop physical roots,
  antisymmetric mirror `SL(2)` bound-state sector, weak mirror branch,
  leading dressing-phase status, and absence of a weak-coupling Konishi
  `mu`-term.

## Comprehensive Development Continuation II

- Strengthened Chapter 12's coordinate Bethe ansatz derivation.  The text now
  derives the two-magnon contact equation for the one-loop `XXX_{1/2}` chain,
  solves for the ordered-chamber exchange coefficient
  `(u_1-u_2-i)/(u_1-u_2+i)`, and explains why the Bethe-Yang phase in the
  closed-chain equation is the inverse coefficient in this chamber convention.
- Derived the two-magnon cyclic quantization directly from
  `Psi(n_1,n_2)=Psi(n_2,n_1+L)` before stating the factorized `M`-magnon
  equations.  This keeps the one-loop finite-chain statement separate from
  the all-loop asymptotic long-range Bethe ansatz.

## Comprehensive Development Continuation III

- Downloaded a local study copy of the foundational QSC source
  `1305.1939` under `references/planar_n4_integrability/qsc/` for convention
  and weak-coupling-argument checking.  This is reference cache and should not
  be staged.
- Expanded Chapter 15's weak-coupling QSC derivation.  Added a precise
  `SL(2)` weak-degeneration regularity assumption for the `Pmu` system:
  leading `P_1`, suppression of `P_2 P_3`, polynomial `P_4/P_1`, polynomial
  `Q`, and the allowed singularities in the `g^2` correction to `mu_12` from
  collapsed short cuts.
- Proved the one-loop dimension extraction formula from the weak QSC by
  writing the singular correction to `mu_12` in digamma form, matching its
  large-`u` logarithm to `mu_12 ~ u^(Delta-J)`, and reducing the result to
  the Bethe-root energy sum.
- Added a twist-two Baxter family example
  `Q_S(u)=3F2(-S,S+1,1/2-iu;1,1;1)`, including its finite-difference
  equation, endpoint/cyclicity signs, harmonic-number energy identity, and
  `Delta_{J=2,S}=2+S+8g^2 H_S+O(g^4)` for physical even spin.

## Comprehensive Development Continuation IV

- Further expanded Chapter 15's QSC foundations before the weak limit.
  Added a QSC Riemann-Hilbert datum definition that states the spectral
  plane, single-short-cut `P_a` functions, antisymmetric `mu_ab`, fixed
  `chi`, tilde continuation, regularity, large-`u` asymptotics, gluing data,
  and cyclic single-trace constraints.
- Proved the one-step monodromy recursion
  `mu_ab(u+i)=mu_ab(u)+P_a mu_bc P^c-P_b mu_ac P^c` from
  pseudo-periodicity, the discontinuity equation, and
  `tilde P_a=mu_ab P^b`.  The text explicitly separates this algebraic
  continuation mechanism from the unproved physical existence/uniqueness
  input.
- Added a QSC status boundary after the quoted theorem, listing what the
  chapter derives locally and what remains framework input: existence of
  single-short-cut functions, the normalized discontinuity coefficient,
  physical gluing, and equivalence to the exact planar gauge-theory spectrum.

## Comprehensive Development Continuation V

- Added the T-hook-to-`Pmu` charge bridge in Chapter 15.  The text now states
  the framework input identifying the fermionic-node product
  `Y_{1,1}Y_{2,2}` with
  `1+(P_1 tilde P_2-P_2 tilde P_1)/mu_12`, together with the mirror-TBA
  large-`u` energy normalization.
- Proved the local algebraic part of the bridge:
  `Y_{1,1}Y_{2,2}=tilde mu_12/mu_12=mu_12(u+i)/mu_12(u)` follows from the
  `Pmu` discontinuity and pseudo-periodicity equations.
- Derived the exponent `mu_12(u) ~ u^(Delta-J)` by comparing
  `log(mu_12(u+i)/mu_12(u))` with the energy normalization.  This makes the
  dimension-carrying asymptotic of `mu_12` a checked consequence of the
  bridge assumptions rather than an unexplained proclamation.

## Comprehensive Development Continuation VI

- Expanded the T-hook-to-`Pmu` bridge from an assumed formula into a local
  reconstruction derivation in Chapter 15.  The text now states the two-row
  physical/magic-gauge datum: shifted Wronskians for `T_{1,m}`,
  `T_{0,1}=mu_12^2`, `T_{3,2}=T_{2,3} mu_12`, central-node regularity, and
  nondegeneracy of the shifted Wronskian determinant.
- Proved the Pluecker/Hirota algebra behind the bridge.  Regularity of
  `T_{2,1}` across the central cut forces
  `tilde mu_12-mu_12=P_1 tilde P_2-P_2 tilde P_1`; the central `(1,1)`
  Hirota square then gives `T_{1,0}=mu_12 tilde mu_12`, hence
  `Y_{1,1}Y_{2,2}=tilde mu_12/mu_12`.
- Narrowed the later fermionic-product assumption to the genuine remaining
  framework input: the mirror-TBA large-`u` energy normalization.  This keeps
  the monograph closer to the stringbook convention while making the local
  algebra self-contained.

## Comprehensive Development Continuation VII

- Expanded the Chapter 15 large-`u` QSC asymptotics.  The text now derives
  the remaining `mu_ab` powers from the `Pmu` sheet equation and the
  `SL(2)` `P_a` powers, with an explicit no-accidental-cancellation
  qualification.
- Added the large-`u` characteristic-root input for the five independent
  `mu_ab` components:
  `Phi(alpha)=0` with physical root `alpha=Delta` and spin-shadow root
  `alpha=S-1`.  The representation-theory status of this second root is now
  stated instead of being hidden inside the final coefficient products.
- Proved the displayed `A_1A_4` and `A_2A_3` formulae by solving
  `Phi(Delta)=Phi(S-1)=0`.  The derivation exposes the intermediate linear
  combination
  `U=-i(J+1)A_2A_3+i(J-1)A_1A_4` and the elementary factorization that fixes
  the convention-sensitive signs.

## Comprehensive Development Continuation VIII

- Expanded the weak-QSC analytic-continuation step in Chapter 15.  The
  digamma singular correction to `mu_12(u+i/2)` is now packaged as a lemma
  with its pole locations, residues, endpoint signs, and large-`u`
  logarithmic coefficient proved explicitly.
- The one-loop dimension proof now invokes this collapsed-cut lemma instead
  of simply asserting the digamma expression.  This makes the branch-point
  residue data and the `2 log u` coefficient auditable inside the monograph.
- Added companion checks for the collapsed-cut digamma package on the
  twist-two Baxter family.  The check uses a local recurrence/Stirling
  implementation of `psi=Gamma'/Gamma` and verifies residues at `u=+-i/2`
  and the large-`u` logarithmic coefficient.

## Comprehensive Development Continuation IX

- Replaced the compressed weak-QSC phrase "same Baxter equation up to regular
  terms" by a local half-integer digamma-primitive lemma.  The lemma proves
  the one-step shift defects of `psi(1/2-iu)+psi(1/2+iu)`, the central
  second-difference identity, and the exact `i`-periodic ambiguity statement.
- The one-loop QSC proof now says precisely what is fixed by the collapsed
  square-root cuts: after division by the leading Baxter polynomial, the
  singular quotient `R_sing/Q` has rational one-step defects.  The remaining
  entire `i`-periodic ambiguity is explicitly assigned to the regular
  polynomial/asymptotic-power part and cannot change the `log u` coefficient.
- Added companion checks for the shift primitive and for the induced
  `R_sing/Q` shift defects on the twist-two Baxter family.

## Comprehensive Development Continuation X

- Upgraded the twist-two Baxter family in Chapter 15 from a stated example to
  a proved proposition.  The proof rewrites the hypergeometric polynomial in
  the variable `z=1/2-iu` and proves the finite-difference equation by an
  explicit summand-level telescoping certificate.
- The endpoint values and energy identity are now derived rather than merely
  recorded.  The proof uses the finite Chu--Vandermonde identity for
  `Qhat_S(1)`, an integral form for `Qhat'_S(0)`, the endpoint
  Christoffel--Darboux identity for Legendre polynomials, and a differentiated
  Chu--Vandermonde identity for `Qhat'_S(1)`.
- Extended the companion checks so the twist-two finite-sum derivation is
  audited exactly over rational arithmetic: endpoint values, endpoint
  derivatives, and the telescoping certificate behind the Baxter equation.

## Comprehensive Development Continuation XI

- Strengthened the Chapter 13 nested-ABA discussion by replacing the displayed
  single level-II factor with a proved local nesting proposition.  In the
  stringbook spin-chain orientation, the proof records the four mixed
  `su(2|2)_c` amplitude ratios needed for one fermionic defect, writes the
  two adjacent-transposition coefficient equations, and reduces them to
  explicit polynomial identities in the auxiliary spectral parameter `y`.
- Added the corresponding level-III/level-II scattering factor next to the
  level-III rational self-scattering factor, with the convention-dependent
  string-basis square-root factors isolated from the matrix-ratio algebra.

## Comprehensive Development Continuation XII

- Extended the Chapter 13 nesting discussion from the one-defect problem to
  the two-defect level-II datum.  The text now records the `SU(2)`-invariant
  `M,N` matrix amplitudes, the ungraded `M+N=-1` identical-fermion sign, the
  rational `M-N` eigenvalue, and the same-site `phi_2 Z^+` contact
  coefficient in the stringbook spin-chain convention.
- Added a proved single level-III nesting proposition.  The proof keeps the
  graded sign explicit, showing that the fermionic exchange sign converts the
  ungraded level-II vacuum eigenvalue into trivial vacuum scattering, and
  derives the displayed `S^{III,II}` factor by two cleared polynomial
  identities.

## Comprehensive Development Continuation XIII

- Assembled the local Chapter 13 nesting factors into the single-copy
  closed-chain nested Bethe-Yang equations.  The proof now explicitly
  transports level-I, level-II, and level-III excitations around the
  corresponding ZF chains and distinguishes this asymptotic quantization from
  thermodynamic Bethe ansatz.
- Added the nesting-number bookkeeping for a state with
  `(N_1,N_2,N_3,N_4)` excitations and a string-basis frame ledger for
  `S^{I,I}`, `S^{II,I}`, `S^{III,II}`, and `S^{III,III}`.
- Recorded the reciprocal auxiliary insertion for the alternative `SL(2)`
  vacuum nesting while keeping the BES dressing phase separate from the
  nesting-frame choice.

## Comprehensive Development Continuation XIV

- Expanded Chapter 14's mirror Bethe-string section from a node inventory
  into a pole-cancellation derivation in the stringbook mirror orientation.
  The text now displays the one-wing auxiliary mirror Bethe-Yang subsystem,
  including the mirror fermion boundary-condition sign.
- Proved the mirror-sheet modulus lemma for the level-II/level-I factor:
  for `x^+=r xi`, `x^-=r^{-1} xi`, the factor has modulus below, equal to,
  or above one according as `|y|<1`, `|y|=1`, or `|y|>1`.  This explains why
  elementary `y` roots live on the unit circle in the thermodynamic mirror
  string hypothesis.
- Derived the `M|yw` and pure `w|M` auxiliary string arrays from the
  nearest pole/zero cancellations, while labeling the real-center condition
  as thermodynamic string-hypothesis input rather than a theorem of the
  four-dimensional gauge theory.

## Calculation Checks

`calculation-checks/planar_n4_integrability_checks.py` now checks:

- `SO(6)` trace-operator reduction to the holomorphic `SU(2)` sector;
- one-magnon XXX finite-difference normalization;
- two-magnon coordinate-Bethe matching: contact equation, chamber exchange
  coefficient, inverse Bethe-Yang phase, and the length-four cyclic Konishi
  eigenvector;
- Konishi one-loop cyclic roots;
- explicit Konishi Baxter polynomial identity;
- twist-two QSC Baxter-family identities for spins `S=1,...,8`, including
  the finite-difference equation, endpoint sign/cyclicity pattern, and
  logarithmic-derivative energy `4 H_S`;
- exact twist-two QSC Baxter-family finite-sum identities: endpoint values,
  endpoint derivatives, and the summand-level telescoping certificate over
  rational `z` test points;
- central-extension dispersion;
- Zhukovsky defining equation, large-`u` expansion, cut reciprocal boundary
  values, `x^pm` relation, and corrected energy formula;
- non-invariance of the stringbook-orientation crossing RHS under a naive
  sheet-free `x -> 1/x` substitution;
- single level-II nesting in the stringbook spin-chain orientation: the two
  adjacent-transposition equations and their cleared polynomial identities;
- two-defect level-II scattering and level-III nesting: `M,N` eigenvalues,
  matrix unitarity, graded vacuum-sign conversion, the two level-III local
  equations, their cleared polynomial identities, and level-III self-scattering
  unitarity;
- closed-chain nested Bethe-Yang frame conventions: string-basis level-I and
  level-II frame ratios, reciprocal `SU(2)`/`SL(2)` auxiliary nesting factors,
  level-III inverse orientation, and nesting-number bookkeeping;
- weak-coupling dispersion expansion;
- BMN scaling limit;
- bound-state shortening dispersion;
- mirror double-Wick dispersion;
- mirror auxiliary Bethe-string derivation: level-II/level-I modulus
  identity and support signs, `M|yw` pole/zero positions, and pure `w|M`
  spacings;
- Konishi four-loop wrapping arithmetic;
- Konishi leading wrapping rational-integral checks: stringbook `u`-integrand
  versus `q=2u` rational integrand, numerical real-line integrals for
  `Q=1,...,4`, and exact telescoping of the non-zeta rational tail;
- planar Bremsstrahlung weak-series Bessel-ratio coefficients through four
  displayed orders;
- local Hirota-to-Y-system algebra.
- QSC `Pmu` Pfaffian preservation under the rank-two discontinuity update.
- QSC `Y_{1,1}Y_{2,2}` bridge algebra and large-`u` exponent extraction for
  `mu_12(u+i)/mu_12(u)`.
- QSC two-row T-hook Wronskian bridge algebra: the Pluecker factorization,
  central-cut regularity of `T_{2,1}`, the `mu_12` discontinuity sign, and
  `T_{1,0}=mu_12 tilde mu_12`.
- QSC large-`u` characteristic-root coefficient products: the dimension root,
  the spin-shadow root `S-1`, the intermediate linear relation, and failure
  of an overall sign flip.
- QSC collapsed-cut digamma singular package: endpoint residues and large-`u`
  logarithmic coefficient for twist-two spins `S=2,4,6`.
- QSC half-integer digamma primitive: upward/downward one-step defects,
  central second difference, and induced singular-quotient shift defects for
  twist-two spins `S=2,4,6`.
- QSC `Pmu` monodromy-recursion signs and antisymmetry of the shifted
  `mu` matrix.

## Status

This is a substantive partial depth pass.  It does not close #607 because the
handoff asks for all four chapters to be expanded beyond stringbook depth with
more complete self-contained derivations, including more comprehensive
analytic-continuation checks.  The issue should remain open.

## Continuation XV: DHM/BES Weak Dressing Coefficients

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Content added:

- Returned upstream from the hexagon material to the crossing/dressing phase
  part of the planar integrability chain, in accordance with the required
  order: crossing/dressing phase, ABA, Bethe-Yang, mirror TBA, Y-system, QSC,
  and only then hexagon form factors.
- Expanded the DHM/BES weak-coupling derivation in Chapter 13.  The text now
  derives the coefficient extraction directly from the contour integral by
  expanding the gamma-function logarithm and taking the Laurent coefficient of
  `(z+z^{-1}-w-w^{-1})^N`.
- Corrected the convention-sensitive order statement: in the stringbook/DHM
  convention the coefficient begins as
  `c_{2,3}(g)=4 zeta(3) g^3-40 zeta(5) g^5+O(g^7)`, while the first weak
  dressing contribution to anomalous dimensions is order `g^6` because the
  physical charges contribute `q_2 q_3=O(g^3)`.

Calculation checks added:

- `check_dhm_weak_dressing_coefficients()` in
  `calculation-checks/planar_n4_integrability_checks.py` now checks the
  Laurent-residue prefactors for several DHM weak coefficients, compares them
  against the closed weak formula, verifies parity and minimal-order
  selection, and confirms that the first charge-dressed term scales as `g^6`.

## Continuation XVI: One-Loop `SL(2)` Large-Spin Cusp Resolvent

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Content added:

- Expanded the pure spectral/QFT content of the stringbook's one-loop
  `SL(2)` large-spin cusp derivation inside Chapter 13.
- Stated the noncompact one-loop `SL(2)` Bethe equations for twist-`L`,
  spin-`S` operators, introduced the scaled root density and resolvent, fixed
  the one-cut square-root branch, derived the discontinuity density, and
  extracted
  `Delta-S-L=8g^2 log S+O(S^0 g^2,g^4)` from the resolvent value at
  `z=i/(2S)`.

Calculation checks added:

- `check_sl2_large_spin_cusp_resolvent()` now checks the physical square-root
  branch of the one-loop cusp resolvent, the derivative formula, the
  discontinuity/density sign, and the large-spin extraction of the
  `8g^2 log S` term including the constant `4g^2 log 4`.

## Continuation XVII: One-Species Mirror-TBA Variational Derivation

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Content added:

- Returned to the pure mirror-QFT/statistical-mechanical foundation of the
  stringbook mirror TBA before further Y-system/QSC development.
- Added a self-contained one-species derivation of mirror TBA from logarithmic
  Bethe-Yang quantization: density equation, Fermi level-statistics entropy,
  constrained free-energy variation, pseudoenergy equation, log-partition
  function, and ground-state energy after the mirror space-time exchange.
- Made the convention bridge explicit.  The density equation differentiates
  `log S(v,u)` in the target rapidity, whereas the chapter's multi-species
  formula uses source-derivative kernels.  Diagonal unitarity gives the minus
  sign in the displayed source-kernel TBA equation, so the monograph convention
  remains aligned with the stringbook rather than silently switching signs.
- Added the one-species excited-state defect source and zero condition
  `zeta(u_j)=-2 pi i(n_j+1/2)`, identifying this as the one-species ancestor of
  the exact Bethe-root regularity condition.

Calculation checks added:

- `check_one_species_tba_variation()` now verifies the finite-dimensional
  constrained-entropy variation, stationarity of the grand functional, the
  free-energy identity after using the density equation, the source-kernel
  sign convention implied by unitarity, and the excited-state zero
  quantization condition.

## Continuation XVIII: Auxiliary-Wing TBA to Y-System Kernel Inversion

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Content added:

- Added a self-contained derivation of the rational auxiliary-string kernel
  inverse used in the stringbook mirror-TBA-to-Y-system passage.  The text now
  defines `K_n`, the fused `K_mn`, the `A_mn=delta+K_mn` kernel, and the
  `s(u)=1/(2 cosh pi u)` kernel with its Fourier symbols.
- Proved in Fourier variables that
  `A^{-1}_{mn}=delta_{mn}-s(delta_{m+1,n}+delta_{m-1,n})`, including the
  boundary condition at `m=1`, and recorded the two consequences
  `A^{-1}K_mn` and `A^{-1}K_n` needed for the wing Y-system.
- Derived the one-wing `n|w` Y-system relation from the mirror TBA equation,
  explicitly stating the strip analyticity and no-crossed-pole hypotheses
  needed to replace `s^{-1}` by the shifts `u -> u +/- i/2`.

Calculation checks added:

- `check_mirror_wing_kernel_inverse()` now checks the fused `A_mn` Fourier
  symbol against the finite fusion sum, verifies the tridiagonal inverse,
  verifies the `A^{-1}K_mn` and `A^{-1}K_n` identities, checks the
  `s^{-1}` shift symbol, and checks the boundary-source algebra in the
  auxiliary-wing Y-system.

## Continuation XIX: Analytic T-Hook Gauge Before the `Pmu` System

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Content added:

- Added the missing analytic T-hook gauge layer from the stringbook QSC
  derivation before the `Pmu` system is introduced.
- Stated the one-row `T`-gauge assumptions explicitly: strip analyticity,
  `T_{0,m}=1`, large-`u` normalization `T_{1,m}->m`, Cauchy transforms
  `G,bar G`, and the ansatz `T_{1,m}=m+G^[m]+bar G^[-m]`.
- Proved directly from Hirota that
  `T_{2,m}=(1+G^[m+1]-G^[m-1])(1+bar G^[-m-1]-bar G^[-m+1])`.
- Recorded the magic-sheet continuation forced by the fermionic-node
  discontinuity: `hat G` equals `G` in the upper half-plane and `-bar G` in
  the lower half-plane, giving
  `hat T_{1,m}=m+hat G^[m]-hat G^[-m]` and
  `hat T_{2,m}=hat T_{1,1}^[m] hat T_{1,1}^[-m]`.

Calculation checks added:

- `check_t_gauge_resolvent_hirota_factorization()` verifies the one-row Hirota
  factorization algebra and the magic-sheet Cauchy-continuation sign.

## Continuation XX: Local `P-Q` Bridge for the QSC Gauge Change

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Content added:

- Expanded the `Qomega` section with the local auxiliary `Q_{a|i}` bridge
  between the `Pmu` and `Qomega` gauges.
- Stated the rank-one finite-difference relation
  `Q_{a|i}^+ - Q_{a|i}^- = P_a Q_i`, the contraction formulae
  `Q_i=-P^a Q_{a|i}^-`, `P_a=-Q^i Q_{a|i}^-`, and the null contractions
  `P_a P^a=Q_i Q^i=0`.
- Proved that the contraction formulae are independent of the `+/-` shift
  and that the rank-one update preserves `det Q_{a|i}`, giving the local
  algebraic reason for the unimodular Q-system gauge.
- Stated the proof boundary explicitly: this local algebra does not prove
  global cut structure, physical gluing, or existence/uniqueness of QSC
  solutions.

Calculation checks added:

- `check_qsc_pq_bridge_unimodular_rank_one_update()` verifies the local
  `P-Q` bridge over exact rational samples: antisymmetric null contractions,
  plus/minus shift independence for both contraction formulae, and determinant
  preservation under the rank-one update.

## Continuation XXI: Stringbook Mirror-Sheet Sign Convention

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Content added:

- Corrected the mirror double-Wick sign convention in Chapter 14 to match the
  stringbook convention `E=i tilde p`, `p=i tilde E`.
- Added an explicit real-mirror-momentum Zhukovsky parametrization
  `x_Q^+=r_Q xi_Q`, `x_Q^-=r_Q^{-1} xi_Q`, with
  `xi_Q=(tilde p-i Q)/sqrt(Q^2+tilde p^2)`.
- Proved the bound-state shortening relation, the mirror energy relation
  `log(x_Q^-/x_Q^+)=tilde E_Q`, the stringbook mirror-momentum relation
  `i tilde p=-Q-2 i g(x_Q^+-x_Q^-)`, and the weak wrapping scaling
  `exp(-L tilde E_Q)=O(g^{2L})`.

Calculation checks added:

- `check_mirror_zhukovsky_sheet_parametrization()` verifies the inside/outside
  sheet assignment, shortening, mirror momentum sign, and weak Boltzmann
  leading order for several charges, momenta, and couplings.

## Continuation XXII: Finite-Density ABA Counting Assumption

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Content added:

- Added a self-contained finite-density ABA counting proposition immediately
  after the asymptotic Bethe-Yang regime assumption.
- Stated the branch, regularity, empirical-measure, and hole-density
  hypotheses needed to pass from
  `L p(u_j)+sum_{k neq j} Theta(u_j,u_k)=2 pi I_j` to the macroscopic
  counting equation.
- Proved
  `rho+rho_h=Z'(u)/(2 pi)=p'(u)/(2 pi)+int K(u,v)rho(v)dv`, with
  `K=(2 pi)^{-1} partial_u Theta`, using the `1/L` empirical measure.
- Explicitly separated this large-`L` finite-density ABA limit from mirror
  TBA: it uses no mirror energy, entropy functional, pseudoenergy, or thermal
  variational principle.

Calculation checks added:

- `check_finite_density_aba_counting_normalization()` verifies the `1/L`
  empirical-measure normalization and `Z'(u)/(2 pi)` level-density
  normalization on a finite-density diagonal Bethe-Yang toy model.

## Continuation XXIII: Analytic Y-System Source Factors

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Content added:

- Added a local proposition deriving the analytic Y-system source factor
  contributed by a shifted zero-pole pair
  `B_alpha(u)=(u-alpha+i/2)/(u-alpha-i/2)`.
- Proved the convention-sensitive identity
  `B_a^+(u) B_a^-(u)=(u-a+i)/(u-a-i)` and its finite-product extension.
- Explained that the homogeneous Y-system only applies after the
  `s^{-1}` shift inverse is used in a singularity-free strip; positions,
  orientations, and sheets of the source factors are separate contour and
  exact-root data.

Calculation checks added:

- `check_y_system_shift_source_factor()` verifies the shifted source factor,
  inverse orientation, and finite source products on complex samples.

## Continuation XXIV: Dressing Scalar Unitarity

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Content added:

- Added a proposition proving dressing scalar unitarity directly from the
  antisymmetric charge expansion of the BES/DHM phase.
- Stated the local convergence/truncation and same-branch hypotheses needed
  for the derivation.
- Proved `theta_21=-theta_12`, hence `sigma_12 sigma_21=1` and
  `sigma_12^2 sigma_21^2=1`, while keeping crossing as separate monodromy data
  on the Zhukovsky surface.

Calculation checks added:

- `check_dressing_charge_antisymmetry_unitarity()` evaluates finite charge
  expansions on physical-branch `x^pm` samples and verifies phase
  antisymmetry, scalar unitarity, and squared-factor unitarity.
