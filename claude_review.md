# QFT Monograph — Active Review

Tracks **unresolved / actionable** items only. The GitHub issue tracker on `xiyin137/QFT` is the primary backlog. **Current state (2026-05-29)**: **22 open issues after the #693 cross-reference repair**. End-to-end per-figure audit complete (114 figures across all 12 volumes; 43 issues filed #649–#690, all closed). Audit-meta issue #579 is closed after the proof-substance ledgers and the #691 trivial-wrapper cleanup. Depth-pass-B work on previously-closed lanes and substantive chapter additions remain. Issue #693 is resolved by converting every genuinely labelled `\[...\]` display to a numbered equation environment and adding a build-gate audit against recurrence.

This document holds items that are either (a) not well-captured in individual issues, (b) cross-cutting in a way the tracker can't surface, or (c) strategic decisions / planning recommendations / standing directives. For completed work and per-issue history, see `git log` and the GitHub issue threads.

---

## DOMINANT FRAMING — the monograph is a foundational rebuild

**Xi 2026-05-26**: "the monograph isn't merely a collection of results/derivations from the literature, but a revisitation and rebuild of foundation at a higher level of rigor and depth than in typical theoretical physics literature."

Not a literature survey / textbook reproduction / curated collection / lecture-notes compendium. IS an **authoritative foundational rebuild** with its own definitions, conventions, hypotheses, derivations, and theorem-level statements — at **higher rigor and depth than typical physics literature**, **self-contained** so reading does not require external recourse for foundational logic. Citations support but do not replace inline derivation. Every claim has a precise mathematical referent, a stated regulator/scheme, an honest scope label, and a checkable derivation or `\quotedtheorem` with full hypotheses + attribution.

---

## Standing directives (active)

0. **UNPRECEDENTED DEPTH (Xi 2026-05-27)** — DOMINANT bar: "the monograph must develop every topic at unprecedented depth and rigor far beyond existing books and reviews in the literature." Closure of a baseline-development issue does NOT mean a topic is done. **Every closed lane has a depth-pass-B follow-on**. Operational test: "is this chapter actually deeper than the best existing review/book on this topic?" — not "is this chapter substantial?"

1. **End-to-end audit (Xi 2026-05-27)**: every chapter, every section, every sentence, every formula, every figure must be audited. All concepts and symbols properly defined. No hand-waving. Every calculation/derivation checked. Proofs sound. Examples nontrivial and illuminating; no trivial manipulations or "demonstration by plugging in numbers." **Issues flagged as audit proceeds.**

2. **New-volumes depth (Xi 2026-05-25)**: Vols VI–XII chapters must be deepened — derivations end-to-end, worked examples carried to results, modern-literature engagement, paired calc-check companions, cross-volume references.

3. **Stringbook QFT absorption (Xi 2026-05-25)**: all purely-QFT material in stringbook must be vastly expanded with derivations more rigorous than the stringbook source.

4. **Kontsevich-Segal axioms (Xi 2026-05-26)**: K-S is the **most promising** framework for capturing path-integral structure and OPE. Vol IV ch06 hosts the systematic chapter + 8-entry openproblem ledger for the K-S construction gap.

5. **bc / βγ scope exclusion (Xi 2026-05-26)**: bc and βγ ghost systems excluded from monograph scope; BRST formalism for gauge theories (Vol II ch18) unaffected.

6. **Modernity / rigor (Xi 2026-05-26)**: default treatment is the modern rigorous one, with textbook treatment as backdrop.

7. **Must exceed stringbook depth (Xi 2026-05-26)**: monograph goes MUCH FURTHER than stringbook on every shared topic.

8. **Best approach by systematic framework-fit (Xi 2026-05-26)**: citation count / popularity is NOT a quality proxy. Classical-and-deeply-established is preferred default. **Out-of-scope**: black hole entropy; HKS; SSS / JT-gravity matrix model; BTZ-CFT entropy matching.

9. **Superstring out of scope; QFT focus (Xi 2026-05-26)**: NO worldsheet or quantum-gravitational frameworks. IN: intrinsic QFT content; QCD strings; strings as solitons; emergent strings in planar gauge-theory integrability. OUT: fundamental worldsheet quantization; D-brane effective actions; string compactification ansatz; mirror symmetry as string-theory duality.

10. **Rigor uplift is the QCD value-add, not topic-import** (Xi 2026-05-27) — particle-physics literature is generally sloppy on both conceptual and mathematical rigor. The monograph's distinguishing contribution on QCD subjects is to **bring rigor** the literature has not delivered. **Per-topic action is `develop with rigor that the literature lacks`**, NOT `import standard textbook treatment`. See [#630](https://github.com/xiyin137/QFT/issues/630).

11. **All-loop cusp via BES, with QCD/DIS cross-link** (Xi 2026-05-27) — full BES-equation development + weak/strong expansions + Bremsstrahlung function. Vol II ch19 now defines the QCD cusped-Wilson-line datum, derives the one-loop angular integral and lightlike coefficient, and cross-links the DIS large-spin relation \(P_{{\rm ns},N}=-\Gamma_{\rm cusp}^q\log N+O(N^0)\) to the planar N=4 BES discussion. Remaining work is the deeper planar N=4 side of [#624](https://github.com/xiyin137/QFT/issues/624).

12. **Singular instantons in SUSY localization must be treated rigorously** (Xi 2026-05-27) — literature is sloppy. Required: small/point-instanton singular stratum; Uhlenbeck vs Gieseker vs Donaldson-Uhlenbeck compactifications; honest status of the Nekrasov ↔ field-theoretic-localization identification (construction-level equivalence not rigorous). See [#629](https://github.com/xiyin137/QFT/issues/629).

13. **Forward references** (Xi 2026-05-27) — every concept/symbol defined at first use. Forward reference allowed *only* for significant technical development deferred to later chapters, *and* must clearly indicate where the construction is given.

14. **Naturalness / fine-tuning / hierarchy problem EXCLUDED** (Xi 2026-05-28) — "naturalness and finetuning are unjustified and sometimes misguided principles and cannot be part of any serious foundational discussion of QFT." The monograph does not use *naturalness*, *fine-tuning*, *hierarchy problem*, or anthropic/multiverse/landscape framings as principles or motivations anywhere. Precise RG-flow statements about Wilson coefficients + SMEFT operators ARE the substance; the editorializing language ABOUT them is out. Parameter values are inputs to the hybrid datum with experimental uncertainties — the smallness of `\bar\theta < 10^{−10}` or `m_h / M_{Pl}` is stated as a precise empirical fact, not editorialized as "unnatural." Applies wherever these temptations arise (SM chapters, EFT chapters, Higgs/scalar discussions, strong CP, neutrino mass, etc.).

15. **Particle-phenomenology content treated as suspicious by default** (Xi 2026-05-28) — "everything from particle pheno must be treated as suspicious and likely wrong and needs to be re-examined thoroughly, if to be incorporated at all." The monograph's epistemic stance on particle-pheno literature is **adversarial by default**: any claim, statement, slogan, or result originating in the particle-phenomenology literature is held to the rigorous hybrid-QFT bar before it is incorporated. The presumption is *likely wrong / likely imprecise / likely sloppy* — not "standard textbook content that can be imported." This applies to (non-exhaustive):
   - All BSM-motivation arguments (SUSY-as-hierarchy-solution, axion-as-strong-CP-solution, see-saw-as-neutrino-mass-explanation, etc.) — re-examined as mathematical hypotheses on the hybrid datum, not as principles
   - All "EFT-power-counting" claims used to constrain BSM — required to specify matching scale + scheme + UV completion or be excluded
   - All "asymptotic-freedom" / "confinement-mechanism" slogans (dual superconductor, center vortex, instanton liquid) — required to specify the precise observable being computed + the regulator
   - All renormalon-cancellation, factorization, parton-distribution, jet-observable claims — required to specify the operator definition, OPE expansion, matching to lattice or dispersive data
   - All SCET / HQET / NRQCD claims — re-examined per [#630](https://github.com/xiyin137/QFT/issues/630) (literature is sloppy; monograph builds rigor)
   - All particle-data-group "fits" and "constraints" used loosely — required to specify scheme + matching + correlation matrix or be excluded
   - All cosmology-particle-pheno claims (sphaleron baryogenesis, dark-matter freeze-out, BBN constraints) — required to be derived from precise Boltzmann or nonperturbative equations, not asserted from review-article folklore
   - All "naturalness" / "fine-tuning" / "hierarchy" / anthropic arguments — already EXCLUDED per #14
   - All BSM "scans" (pMSSM, NMSSM landscape) — out unless reframed as precise SMEFT-coefficient parameter studies

   **Operational rule**: when a chapter touches a pheno-originated subject, the author must (i) state the precise observable + regulator + scheme, (ii) derive or quote-with-attribution any input matrix element, (iii) avoid review-article folklore phrasing, (iv) flag honest scope-limits via `\begin{controlledapproximation}` or `\begin{openproblem}`. Default presumption: re-examine before incorporating. **Many pheno claims will not survive this scrutiny and should be excluded outright.**

16. **EST scope strictly YM-only** (Xi 2026-05-28) — when EST (effective string theory for confining flux tubes) is developed in the monograph, scope is **strictly** the noncritical EST expansion (Polchinski-Strominger / Nambu-Goto / Aharony-Komargodski) around the long-string saddle in YM. Stringbook material on worldsheet formalism may be drawn on *only* for the EST expansion technology, never as a fundamental theory of gravity. **Out**: critical-string worldsheet quantization, BRST conformal anomaly cancellation at `D=26/10`, GSO projection, modular invariance, string compactifications, Polyakov target-spacetime path integral as a theory of gravity. **In**: Lüscher term derivation as worldsheet `Z_2` fluctuation, Polchinski-Strominger universality, Nambu-Goto systematic expansion as EFT for the flux-tube transverse modes.

---

## Methodological principles (cross-cutting)

1. **No uncontrolled approximations** — every approximation derived/flagged/marked.
2. **Axioms as expected properties, not defining conditions** — Wightman/AQFT axioms are expected properties; K-S functorial formulation is most promising for path-integral / OPE.
3. **Reject "QFT defined by perturbing a UV CFT"** — common literature framing the monograph must not propagate.
4. **Moore-Seiberg paper has loopholes** (Xi 2026-05-27) — not a trusted rigorous source. Rational-CFT classification, if developed, belongs to the **MTC + fusion-category framework in Vol VIII (TQFT) or Vol IX (categorical symmetry)**, not Vol V; if developed, alongside fusion categories.
5. **Moore-Seiberg AND Verlinde reframed via defect operators on topological lines** (Xi 2026-05-27) — re-explain from defect operators on topological lines (Verlinde lines = topological defect lines; fusion → Verlinde algebra; modular S = defect-link pairing). **Develop only if Vol IX dives deep into QFT defects.** If no defect-depth commitment, Vol V ch12's existing Verlinde treatment is the floor.
6. **Yangian apparatus questionable** (Xi 2026-05-27) — only include in planar N=4 SYM if needed for a key integrability proof leading to QSC; if centrally-extended psu(2|2)_c shortening / direct crossing suffice, omit Yangian. See [#624](https://github.com/xiyin137/QFT/issues/624).
7. **Hexagon stitching requires extra scrutiny** (Xi 2026-05-27) — if developed in Vol VII ch15, every BKV-style claim must be (a) derived from independent inputs, OR (b) status-labeled conjecture with **explicit nontrivial cross-checks** (4–5-loop weak-coupling matching, mirror-TBA wrapping match, calc-check companion per identity).
8. **pp-wave GS-action quantization OUT; free magnons IN** (Xi 2026-05-27) — GS quantization on pp-wave is string-theory, excluded. Free-magnon spectrum + BMN operators ARE in scope as the spin-chain starting point.

---

## Open backlog (21 GitHub issues)

### Substantial chapter-additions still owed

| Issue | Remaining work | Vol |
|---|---|---|
| [#494](https://github.com/xiyin137/QFT/issues/494) | Vol XI chapter-level integration of the `qft_scripts/` demos (cluster-scale codes scoped under #631) | XI |
| [#519](https://github.com/xiyin137/QFT/issues/519) | Energy-correlator section — partial: nonperturbative detector definition, EEC contact/moment sum rules, tree-level collinear EEC coefficient, and leading back-to-back Sudakov factor added (Vol II ch19, calc-checks pass). Remaining: full modern program (Moult/Zhiboedov/Korchemsky/Kravchuk/Simmons-Duffin); renormalized light-ray-OPE/mixing theorem; complete endpoint matching; analytic high-loop frontier | IV |
| [#526](https://github.com/xiyin137/QFT/issues/526) | Modern jet substructure (soft-drop, N-subjettiness, SCET, track functions) — conditional on rigor standard | IV |
| [#527](https://github.com/xiyin137/QFT/issues/527) / [#528](https://github.com/xiyin137/QFT/issues/528) | Haag-Ruelle for charged particles + Wilson-line LSZ; partial in Vol IV ch05 | IV |
| [#594](https://github.com/xiyin137/QFT/issues/594) | Conformal manifolds + exactly marginal deformations | III/V |
| [#596](https://github.com/xiyin137/QFT/issues/596) | **Block M** — partial: **new chapter Vol II ch20c "Large-N 2D QCD light-front" (462L)** delivered (regulated theory + light-front coords, Gauss-law reduction, planar 't Hooft equation in subtracted positive form, DLCQ benchmark, endpoint exponents, honest scope); Vol VII ch10 now has light-cone CS reduction, bilocal large-\(N\) closure, and planar self-energy equation. Remaining: exact CS-matter solution layer in specific boson/fermion conformal charts; broader light-front-quantization chapter | I/II/VII |
| [#597](https://github.com/xiyin137/QFT/issues/597) | **Block N**: monopole + instanton chapters still owed. Partial: soliton collective-coordinate measure, monopole phase-coordinate dyon/Witten-effect derivation, universal one-loop BPST density scale/RG factors, and the \(k=1\) ADHM orientation-cone/small-instanton boundary derivation added | II |
| [#505](https://github.com/xiyin137/QFT/issues/505) | Wilsonian RG — partial: hierarchical scalar RG benchmark, theorem-level fixed-point definition, stable critical-surface/tuning map, finite-depth linear tuning estimate, Newton validation, universality datum, RG-map taxonomy/comparison datum, gauge-compatible BV/lattice RG datum, distributional reconstruction estimates, and source-extended RG/contact-term theorem added in Vol XI ch07. Remaining: ordinary short-range scalar reconstruction theorem; deeper gauge-specific constructive examples; stronger model-by-model state-of-the-art synthesis | II |

### Vol XI constructive depth

| Issue | Remaining work |
|---|---|
| [#581](https://github.com/xiyin137/QFT/issues/581) | Vol XI ch02 self-contained Φ⁴_3 constructive proof |
| [#582](https://github.com/xiyin137/QFT/issues/582) | Vol XI ch09 singular-SPDE proof stack: BPHZ Φ⁴_3 model + Schauder/product/local-counterterm + invariant-law + SPDE-to-OS (3D) |
| [#608](https://github.com/xiyin137/QFT/issues/608) | Φ⁴_3 concrete model bounds (Schauder + product for BPHZ); local-counterterm derivation; invariant-law comparison |

### Depth-pass-B (unprecedented-depth bar on previously-closed lanes)

| Issue | Remaining work |
|---|---|
| [#624](https://github.com/xiyin137/QFT/issues/624) | Planar N=4: remaining core gaps are full classical finite-gap/algebraic-curve development beyond the first finite-density Bethe-root curve, Pohlmeyer, TBA↔QSC equivalence, and possible future replacement of the quoted strong-BES Riemann-Hilbert theorem by a fully self-contained derivation. Delivered on this lane: QCD/DIS cusp cross-link in Vol II ch19 + Vol VII ch13; free-magnon/BMN spin-chain entry in Vol VII ch12 with finite-chain `p=2 pi n/(L-1)` derivation and calc-check; weak BES scaling function through the first dressing-sensitive `g^8` term in Vol VII ch13; shifted strong-BES expansion and monograph-normalization conversion in Vol VII ch13; finite-density Bethe-root spectral-curve definition, Cauchy jump/quasimomentum gluing, and one-cut cusp curve in Vol VII ch13; Bremsstrahlung weak/strong expansion from the exact Wilson-loop Bessel ratio in Vol VII ch15; Konishi four-loop wrapping residue/telescoper derivation in Vol VII ch14 with exact checks. Yangian removed; hexagon kept with scrutiny-bar |
| [#625](https://github.com/xiyin137/QFT/issues/625) | Vol V CFT — remaining: full Cardy-Lewellen sewing beyond rational diagonal; NLSM higher-loop. (KZ/Sugawara/Ishibashi, Coulomb-gas, nonrational direct-integral, higher-genus sewing delivered + verified) |
| [#626](https://github.com/xiyin137/QFT/issues/626) | Vol VII SUSY — **partial**: HLS classification now a section in ch01 ✓; circular Wilson loop in N=4 (Bessel `(2/√λ)I₁(√λ)` derivation, ch16) ✓; ABJM Bose-Fermi (ch10, 62 hits) ✓; F-theorem present in Vol VII ch10 §10 ✓. **Remaining**: Pestun deep; 6D (2,0) deep (ch11 still 371/4 unchanged) |
| [#629](https://github.com/xiyin137/QFT/issues/629) | Singular instantons — partial: BV boundary obstruction for singular localization strata added (Vol VIII ch10 +171L, calc-check passes). **Remaining**: Uhlenbeck/Gieseker/Donaldson-Uhlenbeck compactifications; ADHM stability + singular stratum; honest Nekrasov ↔ localization status |
| [#630](https://github.com/xiyin137/QFT/issues/630) | QCD rigor uplift — partial: SCET, HQET/NRQCD, Drell-Yan/Glauber, BFKL, GPD/TMD, lattice quasi-/pseudo-PDF matching, QCD current sum rules, Eguchi--Kawai volume-reduction hypotheses/center-selection, and Gribov--Zwanziger horizon-functional/BRST-status treatment now have operator-level rigorous starts with calculation checks. Remaining subclusters: refined jet factorization, CGC/JIMWLK, stronger SCET/Glauber proofs, exact CS-matter solution layer, hydrodynamics-from-QCD. (θ/WV/CFL/HTL/NFL done in Vol X ch12 + Vol II ch20/21) |
| [#631](https://github.com/xiyin137/QFT/issues/631) | Lattice — remaining: dynamical-fermion HMC/RHMC production module; MPI scaling wrappers; SDPB bootstrap workflow; stronger continuum-control examples. Glueball GEVP now has finite transfer-matrix theory, residual criterion, and a theorem-anchored correlator-matrix analysis script; cluster job-array parameter sweep now has deterministic grid resolver, SLURM template, manifest discipline, and calc-check. (Axis A theory + SU(3) pure-gauge pipeline with HDF5/checkpoint/theorem-anchor/calc-check delivered + verified.) Higher-standard mandate: teaching-repo as inspiration only |
| [#694](https://github.com/xiyin137/QFT/issues/694) | Vol VI nested Bethe ansatz / TQ-relations / separation-of-variables depth gap — partial: ch04b/ch05b rewritten with RTT/Yangian component algebra, recursive nested monodromy, Cartan-matrix rational and trigonometric nested Bethe equations, explicit dressed-vacuum transfer eigenvalue and pole-cancellation derivation, string-hypothesis scope, finite-chain generic completeness theorem, SU(3) nested density example, QQ-system, Pluecker/Hirota derivation, exact-sequence \(Q\)-operator proof, q-oscillator trace datum, SoV Baxter reduction, finite-chain SoV measure, finite-chain ABA--Q--SoV comparison, and `nested_integrability_checks.py`. Remaining before closure: fully explicit q-oscillator \(L\)-operator verification for the trigonometric rank-one/U_q case; more worked model-specific nested TBA/string examples for PCM/Gross--Neveu families |

### Cross-cutting + audit-meta

| Issue | Remaining work |
|---|---|
| [#561](https://github.com/xiyin137/QFT/issues/561) | Per-chapter calc-check companions: 153 scripts, ≈85%+ coverage; close remaining gaps |
| [#562](https://github.com/xiyin137/QFT/issues/562) | Assertion-passing-as-derivation pattern — continued reduction by Vol VI ch04 Ising spin/twist separated Euclidean spectral-series proof |
| [#564](https://github.com/xiyin137/QFT/issues/564) | Promised examples / computations never delivered — partial: Vol VI ch04 now carries the infinite Ising spin/twist form-factor families through separated Euclidean spectral convergence with paired calc-checks |
---

## Strategic items not captured as individual issues

- **`tools/audit_approximations.sh`** (proposed; not yet implemented) — flag approximation language outside `controlledapproximation` / `hypothesis` environments; useful as ongoing-CI infrastructure (Session-4 audit already found essentially zero uncontrolled-approximation language).

---

## Non-binding recommendations — CFT chapter additions (open)

- **Embedding-space + closed-form conformal blocks** (Dolan-Osborn + Hogervorst-Rychkov + Casimir recursion). `conformal_block_companion.py` provides the calc-check; standalone chapter optional.
- **Wilson-Fisher / O(N) at d=3 as CFT** (Vol III).
- **QED_3 + 3D fermion CFTs** (Vol III or new Vol VII section).
- **N=4 SYM as 4D CFT** (operator spectrum, OPE, 4-pt bootstrap — distinct from the Vol VII chs 12–15 integrability angle).

---

## Audit status

**Figure audit**: COMPLETE. 114 figures across all 12 volumes / 2514 PDF pages examined per-figure against Xi's criterion ("each figure must contain information not in or easily missed from the text"). 43 issues filed (#649–#690), all closed by codex with substantive figure replacements (function plots, complex-plane pole diagrams, spectral pictures, Drude-vs-regular decompositions, etc.) backed by new propositions + calc-checks. Pattern of failure (labeled-box-with-named-arrows flowchart restating prose) eradicated.

**Proof-level / slogan / definition-locality audit**: COMPLETE across all 12 volumes / ~156 chapters. Zero substantive proof-level errors found; uniform symbol-definition + no-slogan discipline; forward references are overwhelmingly the allowed deferred-development type.

**Substance audit** (Xi 2026-05-28: "quality and depth are essential"): COMPLETE. Methodology: actually read each chapter for substance content (not env-count). Findings: substance is **uniformly at unprecedented depth across the entire monograph**. No additional substance-gap GH issues warranted beyond the existing depth-pass-B + literature-sloppy backlog above. Representative anti-slogan / unprecedented-depth markers documented in `git log` and individual issue threads.

**Substance verdict by axis**:

| Axis | Status |
|---|---|
| Foundational rigor (axiomatic Wightman/OS/AQFT/K-S, rigged Hilbert, microlocal, distributional) | At bar across Vols I/III/IV/XII |
| Perturbative apparatus (BPHZ, MS, RG, BS, Källén-Lehmann, LSZ, Haag-Ruelle) | At bar across Vol I/II |
| CFT machinery (radial, OPE, Ward, unitarity, bootstrap, stress tensor) | At bar across Vol III |
| 2D CFT (VOA, Liouville, BCFT, sigma models, superconformal) | At bar across Vol V |
| Integrable QFT (factorized S, BA, TBA, form factors, sine-Gordon) | At bar across Vol VI |
| SUSY (superspace, N=1 dynamics, N=2 SW, planar N=4, localization, 6D) | At bar across Vol VII |
| TQFT (cohomological FT, BV, Chern-Simons, BF, sigma models, state-sum) | At bar across Vol VIII |
| Generalized symmetry (higher-form, anomaly inflow, defects, categorical) | At bar across Vol IX |
| Thermal/real-time (KMS, SK, hydro, kinetic, NESS, QCD phases) | At bar across Vol X |
| Constructive/lattice (P(φ)_2, φ⁴_3, lattice gauge, MC, rigorous RG, SPDE) | At bar across Vol XI |
| Curved-space (Hadamard, microlocal, AS index, eta, Hawking, paqft) | At bar across Vol XII |

---

## Recommended next steps (prioritized)

1. **Depth-pass-B**: [#624](https://github.com/xiyin137/QFT/issues/624) (planar N=4 BES + spin-chain start), [#626](https://github.com/xiyin137/QFT/issues/626) (SUSY Pestun + 6D (2,0) deep), [#629](https://github.com/xiyin137/QFT/issues/629) (singular instantons), [#630](https://github.com/xiyin137/QFT/issues/630) remaining QCD-rigor subclusters (SCET/HQET/NRQCD/BFKL/GPD-TMD/…), [#625](https://github.com/xiyin137/QFT/issues/625) remaining (Cardy-Lewellen beyond rational diagonal; NLSM higher-loop).
2. **Active development**: [#597](https://github.com/xiyin137/QFT/issues/597) (monopole + instanton chapters), [#596](https://github.com/xiyin137/QFT/issues/596) (light-front + 't Hooft + CS-matter), [#608](https://github.com/xiyin137/QFT/issues/608)/[#582](https://github.com/xiyin137/QFT/issues/582)/[#581](https://github.com/xiyin137/QFT/issues/581) (SPDE Φ⁴_3), [#631](https://github.com/xiyin137/QFT/issues/631) remaining (dynamical-fermion HMC/RHMC + MPI scaling wrappers + SDPB bootstrap + continuum-control examples), [#494](https://github.com/xiyin137/QFT/issues/494) (Vol XI numerical-methods integration), [#505](https://github.com/xiyin137/QFT/issues/505) (rigorous RG).
3. **Cross-cutting**: [#561](https://github.com/xiyin137/QFT/issues/561) calc-check coverage to ~100%; [#562](https://github.com/xiyin137/QFT/issues/562)/[#564](https://github.com/xiyin137/QFT/issues/564) pattern fixes.

---

## What this document tracks vs the GitHub issue tracker

`claude_review.md` is reserved for items either (a) not well-captured in individual GitHub issues, (b) cross-cutting in a way the issue tracker can't surface, or (c) strategic / planning recommendations / standing directives. For per-issue history and completed work, see `git log` and the GitHub issue threads.
