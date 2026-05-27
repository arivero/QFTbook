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

## Continuation XXV: Integrability-Block Derivation Audit and Closed DHM Coefficients

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Review scope:

- Re-read Volume VII Chapters 12--15 as a connected chain:
  spectral problem and one-loop spin chain, crossing/dressing and ABA,
  mirror TBA/Y-system, and QSC/hexagon status boundary.
- Calibrated the review against issue #562 rather than line count: expand
  convention-sensitive or genuinely nontrivial derivations, while avoiding
  new detail on algebra that is already transparent.
- Confirmed that Chapter 15's hexagon material remains intentionally
  downstream and status-bounded; the spectral chain through QSC remains the
  priority.

Content added:

- Strengthened the Chapter 13 DHM/BES weak-coefficient derivation by replacing
  the compressed "apply Chu--Vandermonde" step with a direct two-variable
  Fourier/Laurent coefficient evaluation.
- The text now derives
  `R^{(N)}_{r,s}=(-1)^{N+a} binom(N,(N+a+b)/2) binom(N,(N+a-b)/2)` for
  `a=r-1`, `b=s-1`, then rewrites it as the closed Gamma-function formula for
  `C^{(N)}_{r,s}`.
- The parity/support restrictions are now tied explicitly to the binomial
  lower-entry bounds, equivalently positivity and integrality of the four
  Gamma-function arguments.

Calculation checks added:

- `check_dhm_weak_dressing_coefficients()` now compares the exact Laurent
  residue prefactor against the closed Gamma/binomial formula on a rectangular
  grid of odd `N` and admissible `r,s`, including vanishing cases.

## Continuation XXVI: BES Large-Spin Scaling Bridge

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Source/standard motivation:

- The stringbook contains a more coherent all-loop cusp/BES derivation than
  the monograph previously recorded.  The monograph had only stated the
  weak scaling function; this pass inserts the large-spin ABA-to-BES bridge
  with assumptions and convention data.

Content added:

- Added a large-spin BES scaling-regime assumption for the `SL(2)` all-loop
  ABA at fixed twist and `log S >> L`.
- Defined the Fourier inner-density fluctuation `hat sigma(t)`, the rational
  kernel `K_0`, the dressing kernel `K_dr`, and the combined `K_BES` in the
  stringbook convention.
- Stated the branch-sensitive Fourier transform of `1/(x^pm)^m` that turns
  the all-loop ABA inner equation into Bessel kernels.
- Derived the BES integral equation and the monograph scaling-function
  formula `f(g)=8g^2-64g^4 int hat sigma(t) J_1(2gt)/(2gt) dt`.
- Proved the weak expansion
  `f(g)=8g^2-8 pi^2 g^4/3+88 pi^4 g^6/45+O(g^8)` directly from the BES
  equation, including the power-counting reason the dressing kernel starts
  affecting `f(g)` at `g^8`.
- Recorded the strong-coupling status `f(g)=4g-3 log(2)/pi+O(1/g)` with an
  explicit warning about the factor-of-two convention relative to some
  Wilson-line `Gamma_cusp` normalizations.

Calculation checks added:

- `check_bes_weak_scaling_function()` verifies the exact rational
  coefficient arithmetic for the `sigma_0`, `sigma_1`, `A_0`, and `A_1`
  terms in the weak BES expansion and checks the dressing-kernel power
  counting.

## Continuation XXVII: Fermionic-Node Large-u QSC Energy Bridge

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- The stringbook derives the QSC `mu_12` energy exponent from the
  excited-state mirror-TBA fermionic product using a large-`u` expansion on a
  small-`x` sheet.  The monograph previously recorded this as a
  T-hook-to-`Pmu` normalization input.  This pass supplies the local
  convention-sensitive calculation so the sign is visible.

Content added:

- Defined the fermionic-node sheet `x_f(u)=g/u+O(u^-3)`.
- Defined the mirror fermionic-node ratio
  `R_Q=((x_f-a)/(x_f-b))*((x_f^-1-b)/(x_f^-1-a))` with
  `a=x_Q^+`, `b=x_Q^-`.
- Proved that
  `log R_Q=-tilde E_Q-tilde p_Q/u+O(u^-2)` using the mirror shortening
  relation and the stringbook mirror momentum convention.
- Recorded the inverse mirror continuation
  `tilde E=-i p`, `tilde p=-i E`, giving the physical-root expansion
  `log R_1^phys=i p+i E/u+O(u^-2)`.
- Refined the fermionic-product energy-normalization assumption: the
  remaining framework input is the global excited-state TBA contour formula,
  not an independent QSC sign convention.

Calculation checks added:

- `check_qsc_fermionic_node_ratio_large_u()` verifies the mirror sheet
  placement, mirror energy logarithm, mirror momentum convention, shortening
  relation, ratio constant term, `u^-1` coefficient, numerical large-`u`
  expansion, and inverse mirror continuation.

## Continuation XXVIII: Excited-State TBA Contour Residue Signs

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Source/standard motivation:

- The stringbook states the excited-state mirror-TBA contour deformation as
  the mechanism producing physical-root sources and energy residues.  The
  monograph had recorded the formula, but the sign of the `-log S` driving
  term and the `+i tilde p` energy residue were still implicit.  These signs
  are convention-sensitive and feed directly into the TBA-to-QSC energy
  bridge.

Content added:

- Added a one-species contour-deformation proposition with explicit
  hypotheses on the scattering factor, zero set of `1+Y`, crossed
  singularities, and boundary terms at infinity.
- Proved by integration by parts and residues that a crossed simple zero of
  `1+Y` contributes `-log S(u,u_j)` to the pseudoenergy source.
- Proved, with the same orientation, that the deformed mirror free-energy
  integral contributes `+i tilde p(u_j)` to the energy.
- Derived the exact-root quantization
  `zeta(u_j)=-2 pi i(n_j+1/2)` from `1+exp(-zeta(u_j))=0`.
- Tied the residue result to planar N=4 by using the inverse mirror
  continuation `i tilde p(u_j)=E(u_j)`.

Calculation checks added:

- `check_excited_tba_contour_deformation_residues()` numerically evaluates
  the local residue loops for a rational test scattering factor and verifies
  the source orientation, product orientation, energy residue sign, and
  inverse mirror continuation to physical energy.

## Continuation XXIX: Weak-QSC Pre-Baxter Elimination

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- The stringbook gives an explicit weak-coupling step from the `Pmu` system
  to the Baxter equation by eliminating `mu_24` from the leading `mu_12` and
  `mu_24` recursions.  The monograph previously stated the Baxter
  degeneration but did not expose this intermediate algebra.  The missing
  step is convention-sensitive because it uses the signs in
  `P^1=-P_4`, `P^4=P_1` and the shift convention for `f^[n]`.

Content added:

- Added a weak-QSC proposition deriving
  `mu_24=(mu_12^[+2]-mu_12)/P_1^2-mu_12 P_4/P_1` from the leading `(1,2)`
  component of the Pmu monodromy recursion.
- Used the leading `(2,4)` component to eliminate `mu_24` and derive the
  pre-Baxter equation for `mu_12^[+1]` with coefficients
  `P_4^[+1]/P_1^[+1]-P_4^[-1]/P_1^[-1]+1/(P_1^[+1])^2+1/(P_1^[-1])^2`.
- Rewrote the Baxter-degeneration proposition so the Baxter equation follows
  from this pre-Baxter relation plus the weak asymptotics of `P_1` and the
  regular transfer-polynomial assumption, rather than being assumed directly.
- Corrected the Chapter 15 Baxter-root specialization to the one-loop
  `SL(2)` orientation already used in Chapter 13, without the spurious
  overall minus sign.

Calculation checks added:

- `check_qsc_weak_mu12_mu24_elimination()` verifies the `mu_24`
  reconstruction, the eliminated pre-Baxter difference equation, and sample
  transfer-coefficient finiteness for several twists.
- `check_konishi_baxter_polynomial()` now also verifies that the Konishi
  Baxter polynomial gives the `SL(2)` phase
  `(u_j-u_k-i)/(u_j-u_k+i)` at its roots.

## Continuation XXX: Large-u QSC Characteristic Determinant

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- The stringbook gives the `SL(2)` QSC asymptotic products after a compact
  characteristic-root calculation.  The monograph had recorded the
  characteristic polynomial as part of an assumption.  This pass moves the
  convention-sensitive part into an inline derivation from the Pmu monodromy
  recursion, leaving only the physical root assignment as QSC
  gluing/representation-theory input.

Content added:

- Introduced a trial large-`u` exponent `alpha` for the `mu_ab` sector and
  included the `mu_23` leading power alongside
  `mu_12,mu_13,mu_14,mu_24,mu_34`.
- Derived the six leading coefficient equations obtained from the monodromy
  recursion with `P^1=-P_4`, `P^2=P_3`, `P^3=-P_2`, `P^4=P_1`.
- Expanded the determinant of the resulting coefficient matrix and displayed
  the factorization `det M_alpha = alpha^2 Phi(alpha)`, so the nonzero
  charge-carrying exponents obey the stated characteristic polynomial.
- Reframed the physical roots `alpha=Delta` and `alpha=S-1` as the remaining
  QSC asymptotic/gluing input before solving for `A_1A_4` and `A_2A_3`.

Calculation checks added:

- `check_qsc_large_u_coefficient_constraints()` now also constructs the
  six-by-six leading characteristic matrix for complex sample values and
  verifies numerically that its determinant equals `alpha^2 Phi(alpha)`.

## Continuation XXXI: Rank-One ABA Weak Orientation

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Source/standard motivation:

- The stringbook rank-one ABA formula uses the `SL(2)`-vacuum orientation:
  its weak rational factor is `(u_j-u_k-i)/(u_j-u_k+i)`.  The monograph text
  had described the same displayed all-loop equation as `SU(2)` and then
  claimed reduction to the compact Chapter 12 `SU(2)` one-loop phase, whose
  factor is the reciprocal.  This was a convention conflict across the
  one-loop spin-chain, all-loop ABA, and weak-QSC Baxter discussions.

Content added:

- Renamed the displayed all-loop rank-one equation as the stringbook
  `SL(2)`-vacuum orientation rather than a compact `SU(2)` scalar equation.
- Added a proposition deriving the weak physical-branch expansion
  `x^pm=(u+-i/2)/g-g/(u+-i/2)+O(g^3)`.
- Derived the weak rational factor
  `(x_j^- - x_k^+)/(x_j^+ - x_k^-)
   * (1-1/(x_j^+ x_k^-))/(1-1/(x_j^- x_k^+))
   = (u_j-u_k-i)/(u_j-u_k+i)+O(g^2)`.
- Stated explicitly that the compact Chapter 12 `SU(2)` one-loop
  Bethe--Yang phase is the reciprocal of this rank-one stringbook factor,
  while the noncompact `SL(2)` equation and Chapter 15 weak-QSC Baxter
  degeneration use the stringbook orientation.
- Derived the weak anomalous-energy normalization
  `H-1=2g^2/(u^2+1/4)+O(g^4)`.

Calculation checks added:

- `check_rank_one_aba_weak_orientation()` verifies the physical-branch
  shifted Zhukovsky expansion, weak momentum ratio, anomalous-energy
  normalization, stringbook `SL(2)` rational factor, reciprocal compact
  `SU(2)` phase, and the fact that the dressingless second rational factor
  starts at one.

## Continuation XXXII: Dual Qomega Transport

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- Chapter 15 had developed the `Pmu` transport algebra, Pfaffian
  preservation, and local `P-Q` bridge in detail, but the dual `Qomega`
  paragraph still only named the mirror system.  Since the QSC cut gauge
  changes from short-cut `P_a` functions to long-cut `Q_i` functions, this is
  a convention-sensitive place where signs can silently drift unless the
  transport rule is derived in the same notation.

Content added:

- Defined the dual raising tensor `eta^{ij}` and the dual Pfaffian
  normalization for `omega_ij`.
- Added a lemma proving that the rank-two update
  `omega -> omega + Q wedge tilde Q` preserves `Pf omega` when
  `Q_i Q^i=0`.
- Derived the dual one-step monodromy recursion
  `omega_ij(u+i)=omega_ij+Q_i omega_jk Q^k-Q_j omega_ik Q^k` from
  pseudo-periodicity, the long-cut discontinuity equation, and
  `tilde Q_i=omega_ij Q^j`.
- Stated explicitly that the lemma is local cut-gauge algebra, not a proof of
  the global `Qomega` Riemann-Hilbert existence/gluing problem.

Calculation checks added:

- `check_qomega_dual_monodromy_transport()` verifies `Q_i Q^i=0`, Pfaffian
  preservation, equality of the dual monodromy recursion with the rank-two
  discontinuity update, antisymmetry of the shifted matrix, and sensitivity
  to the overall transport sign on exact and complex samples.

## Continuation XXXIII: Small-Spin QSC Bessel Slope

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- The stringbook gives the small-spin QSC slope through the Bessel-ratio
  formula after displaying the small-spin `Pmu` germ.  Chapter 15 previously
  stated the formula with only a short coefficient-comparison sentence.  This
  was below the derivation density now used in the weak-QSC and large-`u`
  parts of the chapter.

Content added:

- Added the Laurent identity
  `sinh(2 pi u)=sum_n I_{2n+1}(4 pi g) x^{2n+1}`, derived from the
  modified-Bessel generating function and the Zhukovsky relation
  `u=g(x+x^-1)`.
- Extracted the leading small-spin coefficients
  `A_1=epsilon g^(J/2)`,
  `A_2=-epsilon g^(J/2+1) I_{J+1}`,
  `A_3=-epsilon g^(-J/2)`, and
  `A_4=-epsilon g^(-J/2+1) I_{J-1}` from the regularity split of `P_2,P_4`.
- Proved the small-spin slope proposition by substituting these coefficients
  into the linearized QSC charge equations for `Delta-J` and `S`, then using
  `I_{J-1}(z)-I_{J+1}(z)=2J I_J(z)/z` to eliminate `epsilon^2`.
- Kept the extrapolation from infinitesimal spin to integer-spin Konishi as a
  separate QSC analytic-continuation input rather than promoting it to a
  theorem.

Calculation checks added:

- `check_qsc_small_spin_bessel_slope()` verifies the Bessel recurrence and
  the first two exact rational coefficients of
  `z I_{J+1}(z)/(J I_J(z))` for twists `J=1,...,6`.

## Continuation XXXIV: BES Zhukovsky Fourier Transform

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Source/standard motivation:

- The stringbook BES derivation uses the signed transform
  `J_m(2 g t)/t` in the Fourier image of `1/(x^pm)^m`.  Chapter 13 had
  recorded the identity without proof and had rewritten the Bessel ratio with
  absolute values, which erases the lower-branch parity sign for even `m`.
  Since this transform feeds the large-spin ABA-to-BES bridge, it is exactly
  the sort of analytic-continuation step that needs derivation rather than
  citation.

Content added:

- Added a proposition proving the Zhukovsky Fourier transform for the
  physical outside branch `x(z)+x(z)^-1=z/g`, with `x^pm(u)=x(u+-i/2)`.
- Derived the upper-branch support by shifting to `R+i/2`, closing the
  contour according to the sign of `t`, mapping the crossed short-cut loop to
  `|x|=1`, and using the Bessel generating function for
  `exp[-i g t (x+x^-1)]`.
- Used the recurrence `J_{m-1}(z)+J_{m+1}(z)=2m J_m(z)/z` to obtain the
  factor `(-i)^m m J_m(2gt)/t`, then derived the lower-branch transform by
  complex conjugation and `J_m(-z)=(-1)^m J_m(z)`.
- Stated explicitly that the signed `t` ratio is part of the convention and
  must not be replaced by the absolute-value ratio with the same lower-sign
  prefactor.

Calculation checks added:

- `check_bes_zhukovsky_fourier_transform_signs()` verifies the exact Bessel
  recurrence, the upper-contour phase, the lower-branch signed-`t` phase, and
  the even-`m` failure mode of the absolute-value rewrite.

## Continuation XXXV: Displacement Normalization of Bremsstrahlung

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- Chapter 15 stated the Wilson-line relation `C_D=12 B(lambda)` after
  defining the displacement two-point function.  Because this coefficient is
  a convention-sensitive bridge between the defect-CFT normalization and the
  cusp/Bremsstrahlung convention, it needed an explicit derivation rather than
  a displayed assertion.

Content added:

- Defined the cusp logarithmic-divergence convention
  `log <W_cusp>_ren = - Gamma_cusp log(R/epsilon)+O(1)`.
- Added a proposition deriving `C_D=12 B(lambda)` from the straight-line
  defect shape-variation Ward identity.
- The proof uses the finite-part Fourier transform of the displacement
  kernel, `pi C_D |omega|^3/6`, and the small-cusp profile
  `X(t)=varphi t Theta(t)`.  In the logarithmic window
  `R^-1 << |omega| << epsilon^-1`, the profile has
  `Xhat(omega)=-varphi/(omega+i0)^2` modulo endpoint,
  zero-frequency, and contact terms, giving the universal coefficient
  `C_D varphi^2 log(R/epsilon)/12`.
- The localization formula for `B(lambda)` remains a separate exact input;
  this pass only fixes the defect-normalization derivation.

Calculation checks added:

- `check_bremsstrahlung_displacement_cusp_normalization()` verifies the exact
  rational coefficient: the Taylor factor, finite-part Fourier coefficient,
  Fourier measure, and positive/negative frequency half-lines multiply to
  `1/12`, hence `C_D=12 B`.

## Continuation XXXVI: Magic-Sheet One-Row T-Gauge

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- Chapter 15 previously stated the magic-sheet continuation
  `hat T_{1,m}=m+hat G^[m]-hat G^[-m]` and
  `hat T_{2,m}=hat T_{1,1}^[m]hat T_{1,1}^[-m]` after the one-row Hirota
  factorization.  This is a sheet/sign convention, not a harmless notation
  change: the lower Cauchy branch must be continued as `-bar G`.

Content added:

- Added a proposition deriving the magic-sheet formulas from the analytic
  Y-system boundary relation `G_+=-bar G_-` across the mirror cut.
- The proof defines `hat G` as `G` on the upper branch and `-bar G` on the
  lower branch, derives the sign flip in the lower shifted slot of
  `T_{1,m}`, and then factors the two-row expression into the shifted
  `hat T_{1,1}` product.
- The proof states the locality boundary: if a pole or endpoint is crossed,
  an extra source term is part of the analytic data rather than a failure of
  the algebra.

Calculation checks added:

- Strengthened `check_t_gauge_resolvent_hirota_factorization()` with a finite
  Cauchy-transform model that verifies the lower magic branch equals the
  analytic continuation of the upper Cauchy formula, detects the wrong
  lower-sheet sign, and checks the `hat T_{2,m}` row-product formula.

## Continuation XXXVII: Crossing Scalar Convention Algebra

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`

Source/standard motivation:

- The stringbook convention ledger fixes a definite Janik crossing RHS, while
  the literature often prints the reciprocal because the scalar/rational split
  or the `S_{12}`/`S_{21}` orientation has been chosen differently.  The
  monograph should not leave that as a reader-facing assertion, especially
  because the crossed bar is path data rather than a sheet-free substitution.

Content added:

- Added a proposition isolating the rational scalar convention algebra.  It
  defines the stringbook multiplier `Xi_12`, defines the reciprocal multiplier
  used in the opposite convention, and proves `Xi_12^rec=Xi_12^{-1}` by
  factor cancellation.
- Added an explicit algebraic counterexample showing that substituting
  `x_1^pm -> 1/x_1^pm` in the same rational expression does not leave the RHS
  invariant.  The text then restates that Janik crossing itself is the
  scalar-factor monodromy input, not a finite algebraic identity.

Calculation checks added:

- Strengthened `check_crossing_rhs_is_sheet_sensitive()` so it checks the
  exact reciprocal relation on several physical-branch samples and verifies
  the algebraic counterexample used in the text.

## Continuation XXXVIII: Interior T-Hook Y-System Algebra

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Source/standard motivation:

- Chapter 14 already derived the auxiliary-wing Y-system from TBA kernels, but
  the passage from local Hirota T-functions to the full interior T-hook
  Y-system was still compressed into "direct substitution."  Since QSC uses
  exactly this T-gauge redundancy and T-hook boundary data, the monograph
  should spell out the local algebra and identify where boundary modifications
  enter.

Content added:

- Defined the planar `N=4` bulk T-hook domain used by the interior functional
  relation, with `T_{0,s}` adjoined as a gauge boundary and zero T-functions
  outside that hook-plus-boundary domain.
- Added a proposition proving that Hirota plus
  `Y_{a,s}=T_{a,s+1}T_{a,s-1}/(T_{a+1,s}T_{a-1,s})` gives the interior
  Y-system relation.  The proof derives the local `1+Y` and `1+1/Y`
  identities, applies them to the four neighboring Hirota squares, and
  cancels the common T-product.
- Proved that the four-function Hirota gauge
  `T_{a,s}->g_1^[a+s]g_2^[a-s]g_3^[-a-s]g_4^[-a+s]T_{a,s}` cancels in
  `Y_{a,s}`, while analytic QSC gauge data still must fix cuts, asymptotics,
  and gluing.

Calculation checks added:

- Strengthened `check_t_system_to_y_system_identity()` with exact rational
  checks of the full interior T-hook product relation, Hirota gauge
  covariance, and cancellation of the T-gauge labels in `Y_{a,s}`.

## Continuation XXXIX: Planar Chiral-Primary Wick Normalization

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.tex`
- `calculation-checks/susy_n4_scft_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.md`

Source/standard motivation:

- Chapter 12 displayed the normalized planar chiral-primary two-point function
  and extremal three-point/OPE coefficient before entering the spin-chain
  spectral problem.  Since this is the field-theoretic normalization that
  anchors the single-trace Hilbert space, the color/cyclic Wick-counting
  factor should be derived explicitly rather than recorded as a convention.

Content added:

- Added a proposition proving the planar normalization of
  `mathcal Z_J=(2 pi)^J/(g_YM^J sqrt(J N^J)) tr(Z^J)`.
- The proof counts the `J` cyclic planar contractions and `N^J` color loops in
  the two-point function, then counts the `J J1 J2` planar embeddings and
  `N^(J-1)` color loops in the extremal three-point pair-of-pants graph.
- The finite-`N` warning remains explicit: trace relations and multi-trace
  mixing are not part of the single-trace planar spin-chain approximation.

Calculation checks added:

- Strengthened `check_planar_chiral_primary_ope_coefficients()` so it checks
  the unit two-point normalization, the raw extremal color/cyclic factor, and
  the normalized coefficient squared exactly for several `J_1,J_2,N` samples.

## Continuation XL: Hexagon Scalar Watson Orientation

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- Chapter 15 displayed the scalar hexagon factor `h(u,v)` with the correct
  crossing-path caveat, but it did not yet prove the local Watson ratio that
  fixes the scalar-factor orientation.  This is convention-sensitive because
  the weak hexagon exchange phase is compact-`SU(2)` oriented, while the
  stringbook rank-one ABA equation earlier in Chapter 13 is written in the
  `SL(2)` vacuum orientation.

Content added:

- Added a proposition proving
  `h(u_1,u_2)/h(u_2,u_1)=S_hex^scal(1,2)` by explicit rational cancellation
  and dressing unitarity `sigma_12 sigma_21=1`.
- Derived the weak physical-branch limit
  `S_hex^scal=(u_1-u_2+i)/(u_1-u_2-i)+O(g^2)`.
- Kept the global hexagon derivation behind the existing open-problem
  boundary: the new result is local scalar-factor algebra, not a derivation
  of the full pair-of-pants expansion from four-dimensional QFT.

Calculation checks added:

- Added `check_hexagon_scalar_watson_factor()`, which verifies the Watson
  identity exactly on rational samples and checks that the weak limit matches
  the compact one-loop phase rather than the reciprocal `SL(2)` ABA phase.

## Continuation XLI: Hexagon Bridge Kinematics

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- Chapter 15 used the standard bridge lengths and partition phase in the
  asymptotic hexagon formula.  These are elementary but load-bearing
  kinematic data, and the monograph should state the planar length-balance
  hypotheses rather than leaving the formula as an unexplained convention.

Content added:

- Added a proposition deriving
  `ell_12=(L_1+L_2-L_3)/2`, `ell_23=(L_2+L_3-L_1)/2`, and
  `ell_31=(L_3+L_1-L_2)/2` from the three planar pair-of-pants length-balance
  equations.
- Recorded the exact existence criterion for a nonnegative integer planar
  skeleton: even total length plus the three triangle inequalities.
- Clarified the one-excited-operator status of the displayed asymptotic
  partition formula and derived the bridge phase
  `prod exp(i p_j ell)=exp(i p(bar alpha) ell)`.

Calculation checks added:

- Added `check_hexagon_bridge_lengths_and_phase()`, checking the bridge
  length-balance equations, parity/triangle criterion, bridge partition phase,
  and full-state cyclic translation phase.

## Continuation XLII: QSC Large-u Power Balance

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`

Source/standard motivation:

- Chapter 15 already displayed the trial large-`u` powers of the six
  `mu_ab` entries used in the QSC characteristic determinant.  The row
  balance was stated in prose, but this is a convention-sensitive step
  because it uses the `chi`-raising convention
  `(P^1,P^2,P^3,P^4)=(-P_4,P_3,-P_2,P_1)` and fixes which monodromy terms
  survive at the leading power.

Content added:

- Added a proposition proving the six trial powers
  `(alpha-J, alpha+1, alpha, alpha, alpha-1, alpha+J)` from the `SL(2)`
  `P_a` powers, the common sheet exponent shift of `tilde P_a`, and the
  `mu_12` exponent.
- Proved that these powers make every retained term in the leading
  monodromy-recursion system homogeneous with
  `mu_ab(u+i)-mu_ab(u)`, explaining why the six-coordinate characteristic
  determinant is a well-defined leading system.

Calculation checks added:

- Added `check_qsc_large_u_mu_power_balance()`, an exact rational check of
  row homogeneity in `tilde P_a=mu_ab P^b`, the universal monodromy exponent
  identity `p_a+p_b+alpha=e_ab-1`, and term-by-term homogeneity of the
  retained monodromy-recursion terms.

## Continuation XLIII: Konishi Weak-Density Rationalization

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Source/standard motivation:

- The stringbook notes and notebook explicitly checked the weak Konishi
  wrapping density, but Chapter 14 still jumped quickly from the
  stringbook-style `Y_Q^(0)(u)` expression to the rational `q=2u` integrand
  used for residues.  This is one of the places where a compact Mathematica
  check should become a transparent monograph derivation.

Content added:

- Added a proposition proving the exact rationalization of
  `Y_Q^(0)(q/2)`: the numerator factor, the `(q^2+Q^2)^4` mirror denominator,
  and the two quartics `B_Q^-`, `B_Q^+` obtained by pairing the
  `u_*=1/(2 sqrt 3)` physical-root factors.
- Updated the leading wrapping-integral proof to cite this rationalization
  before the contour-residue step, so the residue integrand is no longer
  introduced as an unexplained algebraic jump.

Calculation checks added:

- Strengthened `check_konishi_wrapping_residue_sum()` with exact rational
  checks of the `q=2u` weak-density rationalization for several mirror charges
  and rational rapidities, in addition to the existing numerical integrand and
  residue/telescoping checks.

## Continuation XLIV: Konishi Rational Pole Structure

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Source/standard motivation:

- The leading Konishi wrapping proof already used the upper-half-plane residue
  contour, but the absence of real contour poles and the `Q=1` cancellation
  were compressed into prose.  Since this step fixes which singularities are
  included in the residue sum, it belongs in the derivation rather than in an
  implicit Mathematica notebook convention.

Content added:

- Added a lemma factoring `B_Q^-` and `B_Q^+` as paired physical-root
  quadratics, listing the resulting upper-half-plane poles, proving that the
  `Q=1` points `q=+-1/sqrt(3)` are removable because `B_1^-=(3q^2-1)^2`
  cancels against the numerator, and proving the `q^{-12}` decay needed to
  discard the closing semicircle.
- Updated the wrapping-integral proof to cite this lemma before the residue
  computation, so the contour prescription now rests on a stated pole
  inventory.

Calculation checks added:

- Strengthened `check_konishi_wrapping_residue_sum()` with exact coefficient
  checks of the paired-root factorizations of `B_Q^-` and `B_Q^+`, the `Q=1`
  removable-factor identity and reduced density, and the large-`q` leading
  coefficient consistent with `q^{-12}` decay.

## Continuation XLV: Konishi Exact Residue Reduction

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`

Source/standard motivation:

- After the pole inventory was made explicit, the proof still compressed the
  next algebraic step into "the residue sum gives."  This is precisely the
  sort of convention-sensitive Mathematica-style reduction that should be
  reproducible from stated residue formulas in the monograph.

Content added:

- Added a residue-reduction lemma for the per-charge Konishi summand.  It
  writes the `q=iQ` contribution as a third derivative of the regular part of
  the fourth-order pole, writes the simple-pole contributions using
  `N(q_0)/(D'(q_0))`, and evaluates the derivative of the vanishing quartic
  factor as `24 i a_eta (1 + sigma i sqrt(3) a_eta)`.
- The lemma records that the calculation takes place in
  `Q(sqrt(3), i)`, that the `sigma=+-1` pair cancels the radical-odd pieces,
  and that the reduced result is the displayed
  `R_Q + 864/Q^3 - 1440/Q^5` summand.
- Updated the leading wrapping proof to cite the residue-reduction lemma
  before the telescoping step.

Calculation checks added:

- Added `check_konishi_wrapping_exact_residue_reduction()`, an exact SymPy
  check that extracts the fourth-order Laurent coefficient, checks the
  simple-pole derivative formula, verifies cancellation of radicals in the
  contour sum, and compares the result with the displayed per-charge summand
  for the first four mirror charges.

## Continuation XLVI: Stringbook Integrability Crosswalk

Substantive files edited:

- `planning/planar_n4_integrability_stringbook_crosswalk.md`

Source/standard motivation:

- The user identified incorporation and expansion of the two stringbook
  integrability chapters as the floor requirement for the monograph's planar
  integrability component.  A precise crosswalk is needed before any honest
  claim of completion can be made.

Content added:

- Added a working ledger mapping the two stringbook integrability chapters and
  the relevant stringbook notebooks to Chapters 12--15 of the monograph.
- Introduced explicit status categories: `Expanded`, `Boundary`, `Partial`,
  `Context`, and `Open`.
- Recorded which topics are already derivation-grade and checked, and which
  topics still block certification: global `su(2|2)` S-matrix derivation,
  dressing/crossing analytic continuation, full mirror-TBA kernel/source
  inventory, global QSC reconstruction assumptions, notebook-to-companion-code
  migration, and strong-coupling/small-spin QSC development.

Calculation checks added:

- No new calculation check was added in this bookkeeping pass.  The crosswalk
  identifies the next calculation-check migrations required from the
  stringbook notebooks.

## Continuation XLVII: `su(2|2)_c` Matrix Amplitude Derivation Pass

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`
- `planning/planar_n4_integrability_stringbook_crosswalk.md`

Source/standard motivation:

- The crosswalk identified the one-copy centrally extended `su(2|2)` matrix
  part as a remaining floor blocker.  The chapter previously named the ten
  amplitudes but did not display the stringbook formulas or reproduce the
  local notebook checks that certify the frame and scalar split.

Content added:

- Expanded Chapter 13's two-body S-matrix section with the dynamic spin-chain
  frame, unnormalized symmetrization convention, marker placement for the
  `C_{12}` and `F_{12}` channels, and the representation-ratio definitions
  `x^+=i d/b`, `x^-=-i a/c`.
- Added the full stringbook ten-amplitude formula block for
  `A_{12},...,L_{12}` in terms of `x_i^pm`, `a_i`, `g`, and the one-copy
  scalar `mathcal S_{12}`.
- Proved the highest-weight `Q` relation
  `A=(a_1/a_2)K+G=L+(a_2/a_1)H`, defined the finite `R^{BB}` and `R^{BF}`
  matrix blocks, and separated local matrix unitarity from scalar unitarity,
  Yang-Baxter factorization, and crossing.
- Added the stringbook scalar split for `mathcal S_{12}` and the resulting
  compact `SU(2)` rational factor multiplying `sigma_{12}^2`.
- Updated the crosswalk status for this row to `Expanded/Boundary`: the local
  amplitude and unitarity algebra is now internalized, while the generic
  row-rank proof of one-dimensionality and the notebook's crossing experiments
  remain floor work.

Calculation checks added:

- Added `check_su2c_matrix_amplitudes_and_unitarity()`, porting finite checks
  from `su(2|2) spin chain.nb`: the ten amplitudes satisfy the displayed
  `Q` relation, the boson-boson/fermion-fermion and mixed blocks obey
  `R_12 R_21=1` on physical-branch samples after removing the common scalar,
  and the scalar split reproduces the compact `SU(2)` rational factor.

## Continuation XLVIII: Local DHM/BES Analytic Continuation

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`
- `planning/planar_n4_integrability_stringbook_crosswalk.md`

Content added:

- Inserted a local DHM residue-continuation proposition between the BES
  `chi(x,y)` contour and the weak-coefficient extraction.
- The text defines the Gamma-kernel logarithm `mathcal L_g`, radial raw
  chambers `chi_raw^{epsilon_x,epsilon_y}`, one-residue corrections
  `Psi_x`, `Psi_y`, and the double-residue contact term
  `mathcal C_g=i mathcal L_g(x,y)`.
- This internalizes the sign pattern from the stringbook
  `su(2|2) spin chain.nb` analytic-continuation code:
  inward `x` continuation subtracts the `z=x` residue, inward `y`
  continuation adds the corresponding `w=y` residue in the stringbook
  convention, and simultaneous continuation subtracts the contact correction,
  giving the notebook's final `-i mathcal L_g(x,y)` term.
- The text explicitly keeps this local contour-deformation result separate
  from the global Janik crossing equation, which still requires a path on the
  \(u\)-surface and control of shifted Zhukovsky branch-point windings.

Calculation checks added:

- `check_dhm_local_residue_continuation()` verifies the local continuation
  algebra on a finite Laurent model of the DHM kernel expansion.  It checks
  the one-residue signs, proves the double-residue contact has the displayed
  sign, verifies restoration of the outside branch, and confirms that the
  double crossing fails if the contact term is omitted.

## Continuation XLIX: Shifted-Cut Crossing Path

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`
- `planning/planar_n4_integrability_stringbook_crosswalk.md`

Content added:

- Promoted the earlier warning about sheet data in crossing into an explicit
  right-endpoint crossing-path definition on the shifted Zhukovsky
  \(u\)-surface.
- The path data now states the mod-two winding around `2g-i/2`, which flips
  `x^+`, and around `2g+i/2`, which flips `x^-`, while requiring the DHM
  contour singularities to be avoided except for the controlled residue
  crossings already described.
- Added a proved Zhukovsky monodromy proposition: along such a crossing path,
  `x^pm -> 1/x^pm`, the momentum ratio is inverted, and the meromorphically
  continued stringbook energy changes sign.
- Updated the crosswalk to narrow the remaining crossing floor work to the
  scalar-factor monodromy, pole-avoidance hypotheses, and remaining
  stringbook notebook crossing experiments.

Calculation checks added:

- `check_zhukovsky_crossing_path_monodromy()` numerically tracks the
  continuous square-root branch of `x(u+i/2)` and `x(u-i/2)` around the
  shifted right endpoints.  It verifies that the lower endpoint flips only
  `x^+`, the upper endpoint flips only `x^-`, and the combined path flips
  both variables while preserving shortening, inverting momentum, and flipping
  the continued energy.

## Continuation L: Crossed BES Phase Residue Package

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`
- `planning/planar_n4_integrability_stringbook_crosswalk.md`

Content added:

- Added a local crossed-first-particle BES-phase proposition after the DHM
  residue-continuation rule.
- The text defines `theta_raw^{-,+}` for the four raw DHM kernels with the
  first magnon in the inside chamber and the second in the outside chamber.
- It derives the residue package
  `-Psi(x1+,x2+)+Psi(x1+,x2-)+Psi(x1-,x2+)-Psi(x1-,x2-)`, exposing the
  signs inherited from the BES combination `+,-,-,+` and the single-kernel
  `x`-crossing correction.
- It explicitly states that this is still local contour algebra: the global
  Janik scalar crossing equation additionally needs the scalar branch,
  homotopy class, and treatment of additional crossed singularities.

Calculation checks added:

- Extended `check_dhm_local_residue_continuation()` so the finite Laurent
  DHM model also checks the crossed-first-particle four-kernel BES phase.
  The check verifies the displayed residue package, confirms restoration of
  the outside branch termwise, and fails if the four residue signs are
  reversed.

## Continuation LI: Matrix Channel Origin of Janik Multiplier

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`
- `planning/planar_n4_integrability_stringbook_crosswalk.md`

Content added:

- Ported the finite crossing experiment from the stringbook
  `su(2|2) spin chain.nb` notebook into Chapter 13.
- Defined the crossed-amplitude ratio
  `mathcal R_cr=L_bar1 2/G_21`, where the first magnon is continued to
  `bar x_1^pm=1/x_1^pm` and `S_21=S_12^{-1}` is used for the exchanged
  amplitude.
- Proved that substituting the stringbook scalar split into this finite
  channel gives the Janik scalar product
  `sigma_bar1 2 sigma_12=Xi_12` in the positive square-root chamber.
- The text explicitly separates this finite matrix-channel origin of the
  rational multiplier from the still-global analytic problem of constructing
  the crossed scalar branch.

Calculation checks added:

- Added `check_matrix_crossing_channel_scalar_multiplier()`, an exact
  rational check of the squared `L_bar1 2/G_21` ratio.  It verifies that the
  stringbook multiplier `Xi_12` makes the channel ratio one, that the
  reciprocal multiplier fails, and that the positive real chamber fixes the
  unsquared square-root branch.

## Continuation LII: DHM Gamma-Pole Admissibility

Substantive files edited:

- `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `calculation-checks/planar_n4_integrability_checks.py`
- `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`
- `planning/planar_n4_integrability_stringbook_crosswalk.md`

Content added:

- Added a DHM pole-lattice proposition immediately after the local
  residue-continuation rule.
- The text defines `Delta(z,w)=z+z^{-1}-w-w^{-1}` and derives the
  Gamma-kernel singular divisors `Delta=+/- i n/g`, `n>=1`, from the poles
  of the numerator and denominator Gamma functions.
- It states admissibility conditions for one-residue corrections, the
  double-residue contact term, and the four-kernel crossed-BES phase: the
  crossing path may cross the named Cauchy poles, but the Gamma-pole divisors
  must be avoided unless an additional residue contribution is being
  explicitly tracked.
- The crosswalk now records the Gamma-pole lattice and local admissibility
  hypotheses as incorporated, leaving the genuinely global scalar-branch
  monodromy and homotopy dependence as remaining work.

Calculation checks added:

- Added `check_dhm_gamma_pole_lattice_and_admissibility()`.  The check
  verifies the numerator and denominator pole signs, realizes endpoint pole
  divisors by solving `x+1/x`, checks representative admissible samples, and
  confirms that clearance vanishes on the constructed pole lattice.
