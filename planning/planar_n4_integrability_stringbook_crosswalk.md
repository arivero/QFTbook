# Planar N=4 Integrability Stringbook Crosswalk

## Purpose

This file is the working ledger for the floor requirement: every pure-QFT
integrability detail in the two stringbook integrability chapters must either
appear in the monograph in a defined, hypothesis-stated, derivation-grade form
with calculation checks where conventions or algebra are delicate, or be
routed to a focused issue with an explicit theorem/construction boundary.

This ledger records the current classification at the audited source head.
Every row is either expanded in the monograph, contextual, or boundary-linked
to a focused issue with an explicit construction or theorem boundary.

## Source Scope

- Stringbook source repository: `xiyin137/stringbook`.
- Audited source revision: `9fbd771d17945ce502ee030fdb7936061cef01d6`
  (`main`; reachable at
  `https://github.com/xiyin137/stringbook/commit/9fbd771d17945ce502ee030fdb7936061cef01d6`).
- QFT monograph repository baseline reviewed against this source snapshot:
  `259a2005c84b64e5f23a12e065cf5ff69ce956f6`.
- Primary TeX source anchor: `texsource/string notes.tex`.
- Reproducibility verification on 2026-06-04: a fresh clone of
  `https://github.com/xiyin137/stringbook.git` resolved the audited revision as
  `HEAD`, `git cat-file -t <sha>^{commit}` returned `commit`, and the three
  relevant notebook paths below are present under `codes/`.  The formerly pinned
  local-only source commit `4262f9c821859ace1b6ee43b31afa72fc1542ecd` has
  identical tree objects for `texsource/string notes.tex` and `codes/` to this
  reachable revision, so this ledger is repinned without changing its source
  content.
- Chapter I source range:
  `Strings from N=4 SYM I: planar integrability and the asymptotic Bethe
  ansatz`, approximately lines 15617--16748.
- Chapter II source range:
  `Strings from N=4 SYM II: mirror TBA and the quantum spectral curve`,
  approximately lines 16749--17808.
- Stringbook calculation notebooks directly relevant to this lane:
  `codes/su(2|2) spin chain.nb`,
  `codes/BES equation.nb`,
  and
  `codes/mirror TBA and wrapping corrections.nb`.
- Monograph target files:
  `monograph/tex/volumes/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.tex`,
  `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`,
  `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`,
  and
  `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`.

## Status Vocabulary

- `Expanded`: the monograph defines the symbols, states hypotheses, gives a
  local derivation or proof, and has companion checks when the calculation is
  convention-sensitive.
- `Boundary`: the monograph contains the material with an explicit theorem,
  assumption, or issue-linked development boundary.  This is acceptable only
  when the omitted part is genuinely a global framework theorem or conjectural
  integrability input, not when it is merely tedious algebra.
- `Context`: the stringbook material is primarily holographic string-worldsheet
  context rather than a pure QFT integrability input.  The monograph may use it
  for normalization or orientation, but it is not counted as a pure-QFT floor
  item unless explicitly imported into the gauge-theory derivation.
- `Issue-routed`: the material is a pure-QFT floor item whose missing part is
  owned by a focused issue.  For this ledger the relevant issue is usually
  #624, with analytic-infrastructure overlaps to #728 when the missing object
  is a general TBA/Q-system reconstruction theorem rather than a planar
  \(\mathcal N=4\) specialization.

## Crosswalk

| Stringbook topic | Source anchor | Monograph status | Remaining floor work |
| --- | --- | --- | --- |
| Single-trace operators as cyclic spin chains; `SU(3)` and `SU(2)` sectors; one-loop scalar Hamiltonian | `sec:spinchainfirst` | `Expanded` in Chapter 12: cyclic quotient, planar inner product, `SO(6)` scalar density, `SU(2)` reduction, one-loop Hamiltonian | Keep only if future edits change normalization; current checks cover projector, Wick factors, one-magnon spectrum, two-magnon contact equation, and Konishi roots. |
| Coordinate Bethe ansatz for the one-loop `SU(2)` chain | stringbook equations around `twomagwvfn`, `bethasimp`, `abaheisen` | `Expanded` in Chapter 12 with chamber exchange coefficient and closed-chain inverse Bethe-Yang orientation | No major gap; preserve the distinction between ordered-wavefunction exchange coefficient and Bethe-Yang phase. |
| BMN/pp-wave normalization and lightcone string context | `sec:ppwave` and following GS/pp-wave subsubsections | `Context`: monograph Chapter 13 uses BMN scaling as a gauge-theory normalization check | The Green-Schwarz pp-wave action and string spectrum derivation are not pure-QFT floor items for this lane.  If the monograph later wants the holographic string derivation, it needs a separate string-background pass. |
| All-order magnon dispersion from central extension | `The all-order magnon dispersion relation` | `Expanded` in Chapter 13 with shortening, Zhukovsky variables, physical branch, and energy checks | No major gap, but all later uses must keep `g=sqrt(lambda)/(4 pi)` and the stringbook energy sign. |
| `su(2|2)_c` magnon S-matrix, amplitudes, length-changing markers, and scalar split | `The magnon S-matrix` | `Expanded/Boundary`: Chapter 13 now defines the dynamic frame, displays the ten one-copy amplitude formulas, proves a highest-weight `Q` identity, adds a generic rank-nine row-reduction certificate showing one scalar freedom in the one-copy intertwiner, records the scalar split, ports local matrix-unitarity checks, and internalizes the notebook's finite crossed-channel `L_{\bar1 2}/G_{21}` scalar-multiplier check from `su(2|2) spin chain.nb`; the global symmetry-fixed S-matrix remains framework input | Remaining boundaries are Yang--Baxter factorization, special reducible/pole loci and bound-state projections, and the global scalar monodromy; the generic local one-copy rank chart is now internalized and checked. |
| Crossing equation and crossing-symmetric dressing factor | `The crossing-symmetric dressing factor` | `Expanded/Boundary`: Chapter 13 now explicitly separates magnon crossing from ordinary four-dimensional Wightman-LSZ crossing, identifies the strong-coupling relativistic string worldsheet as the physical source of the crossing/mirror intuition, then derives scalar unitarity, shifted-cut crossing-path monodromy for `x^pm`, DHM weak coefficients, the local DHM residue-continuation rules from the stringbook notebook convention, the induced crossed-first-particle BES-phase residue package, the DHM Gamma-kernel pole lattice and admissibility conditions, reciprocal convention algebra, the finite matrix-channel origin of the Janik rational multiplier, the scalar crossing monodromy cocycle, the explicit double-crossing branch displacement, and the CDD quotient equations with zero/pole propagation; it states BES/crossing as a theorem | Still needs the genuinely global scalar-branch construction: minimal BES branch uniqueness and analyticity, global `chi` continuation, and a systematic comparison with any remaining stringbook notebook crossing experiments not yet ported. |
| Asymptotic Bethe ansatz and finite-density ABA assumption | `Asymptotic Bethe ansatz and the cusp anomalous dimension` | `Expanded/Boundary`: Chapter 13 states the long-chain ABA regime, distinguishes it from TBA, derives the finite-density counting equation, and gives weak/large-spin BES checks | Need keep the status precise: ABA is a long-chain quantization rule assumed to remain valid for controlled finite-density states, not thermodynamic Bethe ansatz. |
| One-loop `SL(2)` sector and large-spin cusp | stringbook `SL(2)` subsection | `Expanded`: Chapter 13 derives the one-loop noncompact resolvent and `8 g^2 log S` coefficient | No major gap except maintaining normalization against the BES scaling-function convention. |
| BES equation and weak scaling function | stringbook all-order cusp subsection and `BES equation.nb` | `Boundary` linked to #624: Chapter 13 derives the BES bridge and weak coefficients through `g^6`; checks cover signed Zhukovsky Fourier transform and weak integrals | Owed work: direct notebook-to-Python crosswalk for every remaining BES experiment and a sharper strong-coupling/global BES branch boundary. |
| Nested Bethe ansatz: level-II one-defect step | `Level II excitations` | `Expanded`: Chapter 13 derives `f(y,p)` and `S^{II,I}` from adjacent-transposition coefficient equations; checks clear the local identities | No major gap for one-defect step. |
| Nested Bethe ansatz: two level-II excitations and level-III step | `Level II scattering`, `Level III` | `Expanded` with #624/#728 boundary: Chapter 13 records `M,N`, contact coefficient, level-III scattering, and checks local identities | The many-excitation ZF construction should be kept explicit if the text is later expanded; current derivation covers the local algebra but not every combinatorial many-body induction detail. |
| Bethe-Yang equations and string-basis frame | `Bethe-Yang equations` | `Expanded`: Chapter 13 proves single-copy transport equations, records nesting numbers, and states full `su(2|2)^2` frame factors | Need ensure every future formula identifies whether it is spin-chain basis, string basis, `SU(2)` vacuum, or `SL(2)` vacuum. |
| Physical bound states and fused Bethe-Yang equations | `Bound States` subsection | `Expanded/Boundary`: Chapter 13 now constructs the `Q`-string endpoints, proves momentum and energy telescoping, derives the bound-state shortening dispersion, proves the level-II auxiliary-factor telescoping, and defines the fused `SL(2)` scalar product used in bound-state Bethe-Yang equations; Chapter 14 uses the same `Q|bullet` charges on the mirror side | Remaining boundary is the full bound-state matrix intertwiner projection and scalar-branch residue normalization at the pole.  The endpoint fusion and scalar product are now checked by `check_bound_state_fusion_telescoping()`. |
| Mirror double Wick rotation and mirror dispersion | `Mirror model and thermodynamic Bethe ansatz` | `Expanded`: Chapter 14 separates mirror magnons from ordinary four-dimensional asymptotic particles, explains their origin as the mirror channel of the relativistic string worldsheet before gauge fixing, and derives mirror dispersion, mirror sheet placement, and weak Boltzmann scaling | No major gap; maintain stringbook convention `E=i tilde p`, `p=i tilde E`. |
| One-particle TBA, density equation, entropy, pseudoenergy, ground-state energy | `The case of one particle type` | `Expanded`: Chapter 14 gives the density derivation, Fermi level-statistics entropy, constrained variation, and source/target kernel convention bridge | No major gap; current checks cover the variation and sign conversion. |
| Excited-state one-particle TBA and contour deformation | `Excited states` | `Expanded`: Chapter 14 derives defect source signs, zero condition, and energy residue orientation | No major gap; keep the contour hypotheses explicit. |
| Multi-species mirror Bethe-Yang to TBA | `TBA from Bethe-Yang equations` | `Expanded/Boundary`: Chapter 14 now proves the target-first/source-kernel convention bridge, maps `oplus`, `ominus`, `M|yw`, and `M|w` to the monograph nodes, states the left/right fermion chemical potentials, and records the node-by-node source inventory including reversed-root denominator signs | Remaining boundary is the global mirror string hypothesis and scalar-kernel analytic input; the explicit closed formulas for every fused scattering kernel are tracked in the full mirror-TBA row. |
| Mirror Bethe strings: `y`, `v|M`, `w|M`, and `bullet_Q` support | `Bethe strings of the mirror model` | `Expanded`: Chapter 14 derives the support and pole-cancellation arrays, with string-hypothesis status for real centers | Need verify every stringbook array and naming convention against the companion checks and the mirror TBA notation table. |
| Full mirror TBA equations | `Mirror TBA` | `Expanded/Boundary`: Chapter 14 contains the TBA framework, node/source inventory, fused `bullet bullet`, `y bullet`, `(v|M) bullet`, and auxiliary `K_mn` formula crosswalk, and enough structure for Y-system and Konishi | Remaining boundary is global dressing-phase analytic continuation for `chi`, possible extra crossed singularities, and the excited-state source crosswalk beyond the one-species residue theorem. |
| Y-system from TBA/Hirota and analytic Y-system data | `The Y-system` | `Expanded/Boundary`: Chapter 14 proves local Hirota-to-Y-system algebra, T-gauge cancellation, the regular-domain `s`-inverse, explicit `s`-zero-mode data loss, shifted zero-pole source factors, and now records the stringbook node map, strip assumptions, branch-point lattice, central fermionic cut inversion, and source-factor bookkeeping as explicit analytic data with companion checks | The finite algebra and bookkeeping are internalized; the remaining boundary is the global analytic-continuation proof selecting the physical sheet, dressing branch, and excited-state source positions. |
| Excited finite-volume states and asymptotic conditions | `Excited states in finite volume and asymptotic conditions` | `Issue-routed` to #624: Chapter 14 and Chapter 15 derive several local bridges and mark remaining QSC/TBA framework inputs | Owed work: tighter bridge from excited-state TBA source terms to QSC asymptotics, including all assumptions on roots, contours, and physical gluing. |
| Konishi wrapping | `The Konishi operator and wrapping corrections`; `mirror TBA and wrapping corrections.nb` | `Expanded/Boundary` linked to #624: Chapter 14 now derives weak-density rationalization, pole structure, exact residue reduction, telescoping, and final coefficient; the leading mirror input remains an explicit assumption | Owed work: audit the whole notebook, not just the rational density/residue path, and decide whether the leading mirror input can be derived further from the preceding ABA/mirror data. |
| T-gauge, `T`-gauge, `mathbb T`-gauge, and `Pmu` system | QSC subsections through `The Pmu-system` | `Expanded/Boundary`: Chapter 15 now derives the one-row analytic gauge, magic-sheet Cauchy continuation, fermionic `mathbf T`/`mathbb T` gauge bridge, central-row discontinuity telescope, two-row local Wronskian algebra, central-cut `Pmu` bridge, Pfaffian, and recursion; global analytic reconstruction remains assumption/theorem input | Remaining boundary is the global Riemann-Hilbert existence/gluing problem and the mirror-TBA discontinuity relation itself, rather than the finite T-gauge algebra. |
| QSC asymptotic conditions and coefficient products | `Asymptotic conditions for the Pmu-system` | `Expanded/Boundary`: Chapter 15 derives `mu_12` power, `mu_ab` powers, characteristic determinant, and coefficient products; physical root assignment is an explicit input | Need ensure every use of large-`u`, sheet exponent, and no-cancellation hypothesis is stated uniformly. |
| QSC weak-coupling limit and Baxter equation | `Weak coupling limit` | `Expanded/Boundary`: Chapter 15 derives the pre-Baxter equation, Baxter limit, digamma package, and twist-two family under explicit weak-regularity assumptions | Need continue replacing weak-QSC regularity assumptions with derivations when feasible; otherwise keep them as honest QSC framework boundaries. |
| Small-spin QSC slope | `Small spin expansion` | `Expanded/Boundary`: Chapter 15 now states the small-spin QSC germ as the analytic input and derives the Bessel slope formula as a coefficient extraction from that germ | Need derive or clearly boundary-label the analytic continuation from small spin to integer spin and any higher-order `K` terms. |
| Konishi at strong coupling | `Konishi at strong coupling` | `Issue-routed` to #624: Chapter 15 records benchmark status but does not yet derive the `K^2` small-spin input or strong Konishi expansion self-containedly | Owed work: dedicated QSC strong-coupling pass; until then, do not present strong Konishi coefficients as derived monograph results. |
| Hexagon form factors | Not part of the two stringbook integrability chapters; added in monograph Chapter 15 | `Boundary`: current text defines the hexagon framework, proves bridge kinematics and local scalar Watson identity, and marks derivation of the full expansion as open | Keep hexagon downstream of the spectral chain.  Do not let it displace unresolved crossing/dressing, ABA, mirror TBA, Y-system, and QSC foundations. |

## Focused Issue Work Queue

1. Audit the three relevant stringbook notebooks against
   `calculation-checks/planar_n4_integrability_checks.py`; every Mathematica
   experiment that supports a monograph formula should either be ported to
   clear Python/SymPy code or explicitly declared obsolete.  A first
   reader-facing companion pair,
   `calculation-checks/planar_n4_reader_companion_checks.py` and
   `calculation-checks/planar_n4_reader_companion_checks.wl`, now gives
   compact spin-chain, Bethe-Yang, local Y-system, and mirror-TBA checks; the
   remaining notebook audit is still broader than this pedagogical layer.
2. Finish the remaining global `su(2|2)_c` S-matrix boundaries: the
   representation, length-changing frame, ten amplitude formulas, scalar
   split, local matrix-unitarity checks, finite crossed-channel
   scalar-multiplier experiment, and generic one-copy row-rank certificate
   are now in Chapter 13.  The remaining work is Yang--Baxter factorization,
   special reducible/pole loci, and bound-state matrix projections.
3. Expand the global dressing/crossing analytic continuation beyond the
   shifted-cut `x^pm` monodromy, crossed BES-phase residue package, local DHM
   residue chamber rules, DHM Gamma-pole lattice, finite matrix-channel
   origin of the Janik multiplier, and scalar double-crossing cocycle now in
   Chapter 13, plus the local CDD quotient and zero/pole propagation law:
   construct or sharply axiomatize the minimal BES scalar branch, make the
   global analyticity assumptions on allowed CDD factors precise, and port
   any remaining stringbook notebook crossing experiments.
4. Complete the global mirror-TBA analytic-continuation crosswalk from the
   stringbook: the node families, fermion signs, reversed-root ratios,
   source/target derivative conventions, fused rational kernels, endpoint
   dressing package, Y-system strip/cut lattice, and central fermion inversion
   are now internalized; the remaining work is the global `chi` continuation
   and excited-state source positions.
5. Tighten the remaining global QSC framework inputs: the local T-gauge,
   `mathbb T`, central-row telescope, and `Pmu` algebra are now internalized;
   the remaining work is the global Riemann-Hilbert existence/gluing problem,
   the mirror-TBA discontinuity relation as analytic input, and sharper
   theorem statements for physical solution selection.
6. Expand the strong-coupling/small-spin QSC block before claiming any
   self-contained strong-Konishi derivation.

## Completion Criterion

The integrability floor is met only after every row above is either
`Expanded` or explicitly classified as `Context`/`Boundary` for a reason that
is mathematical rather than editorial, with any remaining pure-QFT work linked
to #624 or #728 as appropriate.  A boundary without a focused issue and
acceptance criteria blocks any statement that all stringbook integrability
details have been incorporated in depth.
