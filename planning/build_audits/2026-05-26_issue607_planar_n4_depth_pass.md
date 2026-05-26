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
- central-extension dispersion;
- Zhukovsky defining equation, large-`u` expansion, cut reciprocal boundary
  values, `x^pm` relation, and corrected energy formula;
- non-invariance of the stringbook-orientation crossing RHS under a naive
  sheet-free `x -> 1/x` substitution;
- weak-coupling dispersion expansion;
- BMN scaling limit;
- bound-state shortening dispersion;
- mirror double-Wick dispersion;
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
- QSC `Pmu` monodromy-recursion signs and antisymmetry of the shifted
  `mu` matrix.

## Status

This is a substantive partial depth pass.  It does not close #607 because the
handoff asks for all four chapters to be expanded beyond stringbook depth with
more complete self-contained derivations, including more comprehensive
analytic-continuation checks.  The issue should remain open.
