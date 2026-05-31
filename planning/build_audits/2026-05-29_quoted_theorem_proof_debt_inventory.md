# Quoted-theorem proof-debt inventory

This inventory answers the current audit question: yes, the manuscript still
contains essential `quotedtheorem` blocks whose proofs are not reproduced in
the monograph.  This is not automatically a defect.  Pure mathematical
theorems used as analytic infrastructure may remain quoted when the hypotheses,
conclusion, attribution, and local role are stated precisely.  The remaining
problem is narrower: a theorem whose conclusion is specifically a QFT object,
QFT construction, QFT phase statement, or QFT observable should ultimately be
proved self-containedly in the relevant chapter or demoted to a status
statement, hypothesis, controlled approximation, or open proof obligation.

Current scan: 82 `quotedtheorem` environments.

Directive update, 2026-05-30: every `quotedtheorem` in the compiled
monograph must be expanded in place.  The required local text is not a
bibliographic note; it must state the primitive objects, give the proof
mechanism in the monograph's notation, verify the hypotheses used locally,
and identify exactly which analytic or algebraic step remains imported.  The
correct end state is not necessarily zero quoted theorems.  The correct end
state is that no quoted theorem is a black box at its point of use.

GitHub tracking:

- #695: foundational reconstruction and AQFT structural theorem proof debt.
- #581, #582, #608: constructive QFT and stochastic quantization proof debt.
- #505: rigorous Wilsonian RG proof debt.
- #519, #527, #528: scattering, infrared structure, Wilson-line LSZ, and
  light-ray/energy-correlator proof debt.
- #696: anomaly-conclusion proof debt in the monograph's conventions.
- #697, with #625: 2D CFT, Liouville, VOA/modularity, and sewing proof debt.
- #626, #596: supersymmetric dynamics and three-dimensional Chern-Simons-matter
  proof debt.
- #624, #694: planar and nested-integrability proof debt.
- #698, with #629: TQFT, Donaldson-Seiberg-Witten, higher-symmetry, and
  singular-instanton/localization proof debt.

High-priority proof-debt classes:

1. Foundational reconstruction and local-QFT structure.
   `qthm:polynomial-tube-bounds-boundary-values` is an analytic input to OS
   reconstruction.  It is a complex-analysis/distribution theorem, not itself a
   QFT theorem, but the OS chapter should eventually include enough proof
   infrastructure that the linear-growth correction and boundary-value passage
   are transparent.  The OS boundary-value theorem now has a local proof
   sketch detailed enough for the reconstruction use.  The DHR/DR
   reconstruction block now separates the QFT-specific DHR input from the
   categorical compact-group output and contains finite pointed, nonabelian
   representation, crossed-product, and regular charged-coordinate diagnostics;
   the full analytic DHR/DR theorem remains a theorem-boundary input.  AQFT
   structural inputs such as
   Bisognano-Wichmann, nuclearity-to-split consequences, and
   Borchers-Wiesbrock half-sided inclusions are currently quoted and should be
   triaged into proof appendices versus explicit theorem-boundary status.

2. Constructive QFT and stochastic quantization.
   `qthm:p-phi-two-stability`, `qthm:p-phi-two-cluster-os-output`,
   `thm:phi-four-three-constructive-output`, the Da Prato-Debussche mechanism,
   and the renormalized dynamic `Phi^4_3` package are genuine QFT proof debts.
   Recent chapters narrowed several sub-proofs, but the quoted blocks still
   mark missing analytic estimates and construction proofs.

3. Rigorous Wilsonian RG.
   The long-range fermionic fixed-point theorem and the hierarchical scalar
   fixed-point theorem are examples of nonperturbative RG, but their proofs are
   not yet reproduced.  They must remain theorem-boundary examples until a
   self-contained multiscale proof is developed or their role is demoted.

4. Scattering, infrared structure, and light-ray observables.
   Buchholz's infraparticle obstruction, ANEC, and the Lorentzian light-ray OPE
   theorem are quoted.  They are essential for a rigorous treatment of charged
   scattering, infrared-safe observables, and energy correlators; these should
   become proof-appendix targets rather than permanent citations.

5. Anomalies and index-theoretic inputs.
   Mathematical index theorems may be quoted as differential-geometric
   infrastructure.  QFT anomaly conclusions such as the finite `SU(2)` anomaly,
   the cubic gauge obstruction, and WZW level matching should be derived in the
   monograph's conventions or downgraded to explicit theorem-boundary status
   until the derivations are complete.

6. Two-dimensional CFT, Liouville theory, and VOA/modular structure.
   Zhu theory, modularity of rational chiral characters, completely rational
   nets, probabilistic Liouville theory, the DOZZ formula, FZZT one-point
   functions, and boundary sewing statements are currently quoted.  These are
   not all equally central, but those used to define the mathematical content
   of the CFT volumes need either proof appendices or honest status labels.

7. Supersymmetry, planar integrability, and three-dimensional examples.
   Haag-Lopuszanski-Sohnius, half-BPS protection, Seiberg-duality inputs,
   phase-table statements, `F`-theorem statements, ABJM Fermi-gas identities,
   BES strong-coupling data, and QSC spectral-problem statements are quoted.
   Several of these are better understood as conditional physics status
   statements unless and until the monograph supplies a precise construction
   and proof.

8. TQFT, Donaldson-Seiberg-Witten comparison, and higher symmetry.
   The cobordism hypothesis, Crane-Yetter/Walker-Wang boundary principle,
   Donaldson wall crossing, Bauer-Furuta, and finite higher-gauging statements
   are quoted.  Purely mathematical classification statements may remain
   quoted, but any claimed QFT mechanism connecting RG flow, twists, and
   invariants requires local development.

Operational consequence:

- Do not remove `quotedtheorem` merely to make the count smaller.
- For each quoted block, decide one of three actions: prove locally, keep as an
  external mathematical infrastructure theorem with hypotheses and local role,
  or demote to status/hypothesis/open problem when the advertised conclusion is
  not currently established in the monograph.
- The anti-wrapper audit and the quoted-theorem audit are related but distinct:
  demoting trivial local propositions is almost finished for the current pass,
  while proving or triaging all essential quoted theorem blocks is a much
  larger remaining project.
