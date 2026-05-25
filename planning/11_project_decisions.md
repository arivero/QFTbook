# Project Decisions

This file records explicit project-level decisions. Later drafts should treat
these as settled unless Xi changes them.

## Decisions From Xi

Date: 2026-05-20

- The project should be multi-volume.
- The readers are advanced PhD students, researchers, mathematically competent
  humans, and AI agents.
- Human readability and minimized cognitive burden are required, but not by
  lowering mathematical or conceptual standards.
- Misconceptions in standard textbooks may be pointed out in footnotes or
  remarks when this benefits the reader.
- The main exposition should be constructive, not polemical.
- The monograph should be based in logical order on Xi Yin's QFT notes.
- The finished monograph should not explicitly refer to course numbering or
  source-note labels.
- The only previous textbook-level source serving as a model is Xi Yin's own
  QFT lecture notes.
- External references are required for rigor, but they do not set the order or
  conceptual framing.
- Existing axiomatic frameworks are incomplete as strict foundations of the
  whole subject. They must be discussed and kept in view, but not treated as the
  master foundation.
- Kallen--Lehmann spectral representation must appear early.
- Perturbation theory for Green functions may appear before scattering.
- The S-matrix must first be defined nonperturbatively in the spirit of
  Haag--Ruelle/asymptotic-state construction.
- LSZ comes after the nonperturbative S-matrix.
- Feynman diagrams for S-matrix elements come after LSZ.
- All assumptions must be clearly stated.
- All claims must be derived, quoted with hypotheses, or clearly classified.
- All symbols must be defined.
- Definitions must be proper, not simplified or informal placeholders.
- The book should explain what each object is. Negative clarification belongs
  only in remarks, footnotes, or appendices when needed.
- The author line is "GPT 5.5 under the supervision of Xi Yin".

Date: 2026-05-21

- The compiled monograph should keep only material essential to the core QFT
  development at this stage.
- Premature treatments of AdS/CFT, holography, defects, localization,
  large-\(N\) bootstrap, projective-lightcone bootstrap machinery, and rushed
  supersymmetric/superconformal material should be moved out of the compiled
  manuscript and preserved only as deprecated draft material.
- Supersymmetric field theory and gauge theory should be developed later from
  their own foundations rather than introduced through popular advanced
  topics.
- The current compiled CFT material should stop at fixed points, conformal
  symmetry, stress tensor and Ward identities, primaries, unitarity bounds,
  correlator kinematics, and the OPE as local operator algebra.
- Volume divisions should be by subject matter, not by semester sequence.
- The first four subject volumes are:
  1. Foundations of Local Quantum Field Theory;
  2. Particles, Scattering, and Analyticity;
  3. Renormalization, Effective Field Theory, and Critical Phenomena;
  4. Gauge Theory, Infrared Structure, and Anomalies.
- Nonperturbative frameworks must be introduced from the beginning of the
  monograph.  Wightman, Osterwalder--Schrader, AQFT, and related frameworks
  are not a final appendix volume; they are part of the foundational
  understanding of QFT, with technical material developed as needed.
- Detailed studies of QFTs with special properties should be organized in
  dedicated later volumes: CFT, integrable QFT, supersymmetric QFT,
  topological and cohomological QFT, global structure and extended operators,
  thermal and nonequilibrium QFT, constructive/lattice/numerical QFT, and QFT
  in curved spacetime.

Date: 2026-05-22

- Xi's stringbook appendices may be used as internal source material,
  convention checks, examples, and source leads wherever the content is
  relevant to QFT.
- The QFT monograph must develop such material in its own framework: no
  adapted appendix, inherited string-theory context, or unproved physics claim
  enters without independent definitions, hypotheses, and derivation or an
  explicit theorem boundary.
- Any stringbook use must be recorded in the relevant dossier as an internal
  source, cross-check, or seed, with independent QFT-side definitions,
  hypotheses, derivations, and external references supplied as needed.

Date: 2026-05-23

- The current compiled manuscript has no formal BibTeX or biblatex layer and
  no reader-facing `\cite{...}` commands.  Named theorems and named mechanisms
  in the text are attribution labels and theorem-boundary markers, not imported
  claims.  The exposition must remain self-contained: every nontrivial physics
  or mathematical claim used in the logical development is either derived,
  stated with hypotheses, or explicitly bounded as an assumption, conjecture,
  open problem, controlled approximation, or formal calculation.
- External sources remain essential for rigor checks, convention checks, and
  source leads, but for the current compiled manuscript they are recorded in
  `references/`, planning files, and chapter dossiers rather than promoted to a
  reader-facing bibliography.  A future bibliography apparatus may be added
  only as a deliberate project-level change with a single style decision and a
  complete audit of all promoted citations.
- The main chapters carry the logical proof burden.  Every result used in the
  main development must have its definitions, assumptions, and derivation or
  theorem boundary visible at the point of use.  Appendices may contain long
  estimates, background machinery, repeated algebra, classification details, or
  technical proofs whose length would obscure the main line, but an appendix
  reference never licenses a gap in the main chapter: the main text must state
  the precise result, hypotheses, dependency, and role in the argument.
- Machine-readable planning metadata remains Markdown-first for now.  The
  required near-term structure is an auditable heading contract for chapter
  dossiers, enforced by `tools/audit_chapter_dossiers.sh`.  YAML dossiers,
  separate notation/claim/figure ledger files, generated dependency graphs,
  citation-support checks, and visual PDF audits are deferred until the chapter
  architecture stabilizes enough for those artifacts to reduce errors rather
  than create bookkeeping churn.
- The common literature framing "QFT is defined by perturbing a UV CFT" is
  rejected as a general definition.  Conformal perturbation theory is a
  controlled method for deformations of an already supplied fixed point, with
  explicit operator, contact-term, regulator, and reconstruction hypotheses.
  It is not the foundation for asymptotically free gauge theories,
  constructive QFTs, lattice scaling limits, stochastic-quantization
  constructions, or effective presentations of the Standard Model.
- Counterterms are regulator-dependent local coordinates in the single
  regulated action used in the path integral, relative to a chosen finite
  renormalized chart.  The monograph should not treat the legacy
  two-Lagrangian split as conceptually primary.
  Regularization of the action or measure, regularization of composite
  insertions, and renormalization of finite action/source/operator coordinates
  are distinct data and must be named separately.
- The Standard Model is treated as a hybrid object: a lattice/nonperturbative
  QCD sector, an electroweak finite-cutoff EFT, low-energy weak EFTs, and
  matching maps.  The compiled Standard Model chapter derives the electroweak
  mass coordinates, verifies local and finite anomaly cancellation, and states
  the constructive Standard Model problem.
- Effective field theories without Poincare-invariant UV completion are
  treated by their regulator, observable class, matching map, and error
  bounds.  Critical lattice scaling limits that satisfy reconstruction
  hypotheses are separated from finite-cutoff condensed-matter EFTs that only
  borrow relativistic QFT technology after a validation map is supplied.
- A reader-facing volume dependency guide is part of the frontmatter.  Its
  role is only navigational: it locates where deferred machinery is developed
  and requires local chapters to state theorem status at the point of use.

Date: 2026-05-24

- Energy correlators are core QFT observables for the monograph, not optional
  phenomenology.  The gauge-theory volume treats them as stress-tensor-defined
  color-singlet detector observables in the physical Hilbert space before
  introducing partonic approximations.  The CFT volume treats the same
  observables as light-ray operators and conformal-collider distributions,
  with null-integral hypotheses, contact terms, positivity, and theorem
  boundaries stated explicitly.
- Jets and hadronization belong in the gauge-theory volume as a careful
  treatment of final-state observables.  Jet definitions must be formulated as
  measurement functions on physical final states and tested for infrared and
  collinear safety before perturbative partonic representatives are used.
  Hadronization, fragmentation functions, and parton showers enter only with
  their operator definitions, controlled-approximation status, or
  nonperturbative-input status explicitly stated.

Date: 2026-05-25

- Open GitHub issues should now be reviewed as a global development map rather
  than as a strict old-to-new queue.  Issue closure still requires a compiled
  manuscript change, local verification, a pushed commit, and a GitHub comment
  explaining what was addressed.
- Volumes VI--XII are launched as compiled subject volumes.  Their first
  chapters establish the local mathematical objects for integrable QFT,
  supersymmetric QFT, topological/cohomological QFT, global structure and
  higher-form symmetry, thermal QFT and hydrodynamics, constructive/lattice/
  numerical QFT, and QFT on curved backgrounds.
- Thermal field theory and the bridge from QFT to hydrodynamics form their own
  subject volume.  The volume begins from KMS states and retarded correlators,
  then develops finite-temperature path integrals, Schwinger--Keldysh theory,
  Kubo formulae, hydrodynamic constitutive relations, entropy-current and
  effective-action constraints, thermal gauge theory, kinetic theory, and
  anomalous transport.

## Current Implementation Decisions

- Keep `transcription/` as the faithful source layer.
- Use `monograph/tex/` for the polished manuscript.
- Compile only audited chapters through volume include files.
- Keep planning metadata out of reader-facing TeX.
- Use `tools/audit_monograph_text.sh` and `tools/build_monograph.sh` as the
  first automated gate.
- Add stricter audits as failure patterns become clear.

## Open Decisions

- Final TeX class and volume compilation strategy.
- Exact chapter allocation inside future special-topic volumes.
