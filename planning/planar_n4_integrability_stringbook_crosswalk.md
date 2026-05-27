# Planar N=4 Integrability Stringbook Crosswalk

## Purpose

This file is the working ledger for the floor requirement: every purely-QFT
integrability detail in the two stringbook integrability chapters must appear
in the monograph in a defined, hypothesis-stated, derivation-grade form, with
calculation checks where conventions or algebra are delicate.

This ledger is not a certificate of completion.  It records what is already
expanded, what is present only with honest proof-boundary status, and what
still needs development.

## Source Scope

- Stringbook source:
  `/Users/xiyin/PhysicsLogic/references/stringbook/string notes.tex`.
- Chapter I source range:
  `Strings from N=4 SYM I: planar integrability and the asymptotic Bethe
  ansatz`, approximately lines 15617--16748.
- Chapter II source range:
  `Strings from N=4 SYM II: mirror TBA and the quantum spectral curve`,
  approximately lines 16749--17808.
- Stringbook calculation notebooks directly relevant to this lane:
  `/Users/xiyin/PhysicsLogic/references/stringbook/Code repository/su(2|2) spin chain.nb`,
  `/Users/xiyin/PhysicsLogic/references/stringbook/Code repository/BES equation.nb`,
  and
  `/Users/xiyin/PhysicsLogic/references/stringbook/Code repository/mirror TBA and wrapping corrections.nb`.
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
  assumption, or open-problem boundary.  This is acceptable only when the
  omitted part is genuinely a global framework theorem or conjectural
  integrability input, not when it is merely tedious algebra.
- `Partial`: the monograph has the topic, but some stringbook detail or
  calculation is still not crosswalked or is not yet at uniform depth.
- `Context`: the stringbook material is primarily holographic string-worldsheet
  context rather than a pure QFT integrability input.  The monograph may use it
  for normalization or orientation, but it is not counted as a pure-QFT floor
  item unless explicitly imported into the gauge-theory derivation.
- `Open`: not yet incorporated at the required standard.

## Crosswalk

| Stringbook topic | Source anchor | Monograph status | Remaining floor work |
| --- | --- | --- | --- |
| Single-trace operators as cyclic spin chains; `SU(3)` and `SU(2)` sectors; one-loop scalar Hamiltonian | `sec:spinchainfirst` | `Expanded` in Chapter 12: cyclic quotient, planar inner product, `SO(6)` scalar density, `SU(2)` reduction, one-loop Hamiltonian | Keep only if future edits change normalization; current checks cover projector, Wick factors, one-magnon spectrum, two-magnon contact equation, and Konishi roots. |
| Coordinate Bethe ansatz for the one-loop `SU(2)` chain | stringbook equations around `twomagwvfn`, `bethasimp`, `abaheisen` | `Expanded` in Chapter 12 with chamber exchange coefficient and closed-chain inverse Bethe-Yang orientation | No major gap; preserve the distinction between ordered-wavefunction exchange coefficient and Bethe-Yang phase. |
| BMN/pp-wave normalization and lightcone string context | `sec:ppwave` and following GS/pp-wave subsubsections | `Context`: monograph Chapter 13 uses BMN scaling as a gauge-theory normalization check | The Green-Schwarz pp-wave action and string spectrum derivation are not pure-QFT floor items for this lane.  If the monograph later wants the holographic string derivation, it needs a separate string-background pass. |
| All-order magnon dispersion from central extension | `The all-order magnon dispersion relation` | `Expanded` in Chapter 13 with shortening, Zhukovsky variables, physical branch, and energy checks | No major gap, but all later uses must keep `g=sqrt(lambda)/(4 pi)` and the stringbook energy sign. |
| `su(2|2)_c` magnon S-matrix, amplitudes, length-changing markers, and scalar split | `The magnon S-matrix` | `Expanded/Boundary`: Chapter 13 now defines the dynamic frame, displays the ten one-copy amplitude formulas, proves a highest-weight `Q` identity, records the scalar split, and ports local matrix-unitarity checks from `su(2|2) spin chain.nb`; the global symmetry-fixed S-matrix remains framework input | Still needs the full row-reduction proof of generic one-dimensionality of the intertwined tensor product and a complete audit of the notebook's crossing/analytic-continuation experiments.  Yang--Baxter factorization and the global scalar monodromy remain boundary data rather than finite local algebra. |
| Crossing equation and crossing-symmetric dressing factor | `The crossing-symmetric dressing factor` | `Partial/Boundary`: Chapter 13 derives scalar unitarity, DHM weak coefficients, reciprocal convention algebra, and states BES/crossing as a theorem | Needs deeper analytic-continuation development: crossing path, branch point winding, DHM/BES contour deformation hypotheses, and a systematic comparison with stringbook notebook conventions. |
| Asymptotic Bethe ansatz and finite-density ABA assumption | `Asymptotic Bethe ansatz and the cusp anomalous dimension` | `Expanded/Boundary`: Chapter 13 states the long-chain ABA regime, distinguishes it from TBA, derives the finite-density counting equation, and gives weak/large-spin BES checks | Need keep the status precise: ABA is a long-chain quantization rule assumed to remain valid for controlled finite-density states, not thermodynamic Bethe ansatz. |
| One-loop `SL(2)` sector and large-spin cusp | stringbook `SL(2)` subsection | `Expanded`: Chapter 13 derives the one-loop noncompact resolvent and `8 g^2 log S` coefficient | No major gap except maintaining normalization against the BES scaling-function convention. |
| BES equation and weak scaling function | stringbook all-order cusp subsection and `BES equation.nb` | `Partial/Expanded`: Chapter 13 derives the BES bridge and weak coefficients through `g^6`; checks cover signed Zhukovsky Fourier transform and weak integrals | Needs a direct notebook-to-Python crosswalk for all stringbook BES experimental calculations and a clearer boundary for strong-coupling BES results. |
| Nested Bethe ansatz: level-II one-defect step | `Level II excitations` | `Expanded`: Chapter 13 derives `f(y,p)` and `S^{II,I}` from adjacent-transposition coefficient equations; checks clear the local identities | No major gap for one-defect step. |
| Nested Bethe ansatz: two level-II excitations and level-III step | `Level II scattering`, `Level III` | `Expanded/Partial`: Chapter 13 records `M,N`, contact coefficient, level-III scattering, and checks local identities | The many-excitation ZF construction should be kept explicit if the text is later expanded; current derivation covers the local algebra but not every combinatorial many-body induction detail. |
| Bethe-Yang equations and string-basis frame | `Bethe-Yang equations` | `Expanded`: Chapter 13 proves single-copy transport equations, records nesting numbers, and states full `su(2|2)^2` frame factors | Need ensure every future formula identifies whether it is spin-chain basis, string basis, `SU(2)` vacuum, or `SL(2)` vacuum. |
| Physical bound states and fused Bethe-Yang equations | `Bound states` | `Partial`: Chapter 13 defines bound-state dispersion and the fused product form; Chapter 14 uses mirror bound states | Needs a more detailed derivation of the fused scalar factor and pole-residue interpretation, beyond dispersion and telescoping of auxiliary factors. |
| Mirror double Wick rotation and mirror dispersion | `Mirror model and thermodynamic Bethe ansatz` | `Expanded`: Chapter 14 derives mirror dispersion, mirror sheet placement, and weak Boltzmann scaling | No major gap; maintain stringbook convention `E=i tilde p`, `p=i tilde E`. |
| One-particle TBA, density equation, entropy, pseudoenergy, ground-state energy | `The case of one particle type` | `Expanded`: Chapter 14 gives the density derivation, Fermi level-statistics entropy, constrained variation, and source/target kernel convention bridge | No major gap; current checks cover the variation and sign conversion. |
| Excited-state one-particle TBA and contour deformation | `Excited states` | `Expanded`: Chapter 14 derives defect source signs, zero condition, and energy residue orientation | No major gap; keep the contour hypotheses explicit. |
| Multi-species mirror Bethe-Yang to TBA | `TBA from Bethe-Yang equations` | `Partial`: Chapter 14 states the node-family framework and mirror-kernel datum | Needs a complete node-by-node kernel/source inventory against the stringbook formulas, especially boundary-condition signs and source-derivative orientations. |
| Mirror Bethe strings: `y`, `v|M`, `w|M`, and `bullet_Q` support | `Bethe strings of the mirror model` | `Expanded`: Chapter 14 derives the support and pole-cancellation arrays, with string-hypothesis status for real centers | Need verify every stringbook array and naming convention against the companion checks and the mirror TBA notation table. |
| Full mirror TBA equations | `Mirror TBA` | `Partial`: Chapter 14 contains the TBA framework and enough structure for Y-system and Konishi | Needs a systematic formula-by-formula comparison with the stringbook full mirror TBA block and the Arutyunov-Frolov convention sources. |
| Y-system from TBA/Hirota and analytic Y-system data | `The Y-system` | `Expanded/Partial`: Chapter 14 proves local Hirota-to-Y-system algebra, T-gauge cancellation, shifted zero-pole source factors, and records analytic data | Needs the complete discontinuity/source-condition crosswalk from the stringbook analytic continuation discussion. |
| Excited finite-volume states and asymptotic conditions | `Excited states in finite volume and asymptotic conditions` | `Partial`: Chapter 14 and Chapter 15 derive several local bridges and mark remaining QSC/TBA framework inputs | Needs a tighter bridge from excited-state TBA source terms to QSC asymptotics, including all assumptions on roots, contours, and physical gluing. |
| Konishi wrapping | `The Konishi operator and wrapping corrections`; `mirror TBA and wrapping corrections.nb` | `Expanded/Boundary`: Chapter 14 now derives weak-density rationalization, pole structure, exact residue reduction, telescoping, and final coefficient; the leading mirror input remains an explicit assumption | Need audit the whole notebook, not just the rational density/residue path, and decide whether the leading mirror input can be derived further from the preceding ABA/mirror data. |
| T-gauge, `T`-gauge, `mathbb T`-gauge, and `Pmu` system | QSC subsections through `The Pmu-system` | `Partial/Boundary`: Chapter 15 derives one-row and two-row local algebra, central-cut bridge, `Pmu` discontinuity, Pfaffian, and recursion; global analytic reconstruction remains assumption/theorem input | Needs fuller self-contained development of the gauge transformations and global Riemann-Hilbert assumptions, or sharper theorem statements for exactly what is imported. |
| QSC asymptotic conditions and coefficient products | `Asymptotic conditions for the Pmu-system` | `Expanded/Boundary`: Chapter 15 derives `mu_12` power, `mu_ab` powers, characteristic determinant, and coefficient products; physical root assignment is an explicit input | Need ensure every use of large-`u`, sheet exponent, and no-cancellation hypothesis is stated uniformly. |
| QSC weak-coupling limit and Baxter equation | `Weak coupling limit` | `Expanded/Boundary`: Chapter 15 derives the pre-Baxter equation, Baxter limit, digamma package, and twist-two family under explicit weak-regularity assumptions | Need continue replacing weak-QSC regularity assumptions with derivations when feasible; otherwise keep them as honest QSC framework boundaries. |
| Small-spin QSC slope | `Small spin expansion` | `Expanded/Boundary`: Chapter 15 proves the Bessel slope formula under small-spin analytic assumptions | Need derive or clearly boundary-label the analytic continuation from small spin to integer spin and any higher-order `K` terms. |
| Konishi at strong coupling | `Konishi at strong coupling` | `Open/Boundary`: Chapter 15 records benchmark status but does not yet derive the `K^2` small-spin input or strong Konishi expansion self-containedly | Needs a dedicated QSC strong-coupling pass; until then, do not present strong Konishi coefficients as derived monograph results. |
| Hexagon form factors | Not part of the two stringbook integrability chapters; added in monograph Chapter 15 | `Boundary`: current text defines the hexagon framework, proves bridge kinematics and local scalar Watson identity, and marks derivation of the full expansion as open | Keep hexagon downstream of the spectral chain.  Do not let it displace unresolved crossing/dressing, ABA, mirror TBA, Y-system, and QSC foundations. |

## Open Floor Work Queue

1. Audit the three relevant stringbook notebooks against
   `calculation-checks/planar_n4_integrability_checks.py`; every Mathematica
   experiment that supports a monograph formula should either be ported to
   clear Python/SymPy code or explicitly declared obsolete.
2. Finish the `su(2|2)_c` S-matrix derivation: the representation,
   length-changing frame, ten amplitude formulas, scalar split, and local
   matrix-unitarity checks are now in Chapter 13, but the generic row-rank
   proof of uniqueness of the intertwiner and the notebook's crossing
   experiments still need to be fully internalized.
3. Expand the global dressing/crossing analytic continuation: state the
   crossing contour, branch cuts, monodromy, BES/DHM kernel hypotheses, and
   convention transformations.
4. Complete the full mirror-TBA kernel/source crosswalk from the stringbook:
   all node families, signs, source/target derivative conventions, and
   excited-state sources.
5. Tighten the QSC derivation from T-system/TBA to `Pmu`: every global
   analytic assumption should either be proved locally, quoted as a theorem
   with hypotheses, or listed as a framework input.
6. Expand the strong-coupling/small-spin QSC block before claiming any
   self-contained strong-Konishi derivation.

## Completion Criterion

The integrability floor is met only after every row above is either
`Expanded` or explicitly classified as `Context`/`Boundary` for a reason that
is mathematical rather than editorial.  A row marked `Partial` or `Open`
blocks any statement that all stringbook integrability details have been
incorporated in depth.
