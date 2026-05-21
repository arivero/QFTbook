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

- Xi's stringbook appendices may be used as inspiration, convention checks, and
  source leads for CFT and supersymmetric field theory.
- The CFT and supersymmetric QFT volumes must be developed as new,
  comprehensive QFT monograph treatments, not adapted appendices or a string
  theory support text.
- Any stringbook use in CFT or supersymmetry must be recorded in the relevant
  dossier as a cross-check or seed, with independent definitions, hypotheses,
  derivations, and external references supplied for the QFT monograph.

## Current Implementation Decisions

- Keep `transcription/` as the faithful source layer.
- Use `monograph/tex/` for the polished manuscript.
- Compile only audited chapters through volume include files.
- Keep planning metadata out of reader-facing TeX.
- Use `tools/audit_monograph_text.sh` and `tools/build_monograph.sh` as the
  first automated gate.
- Add stricter audits as failure patterns become clear.

## Open Decisions

- Final bibliography style.
- Final TeX class and volume compilation strategy.
- How much theorem-proof detail belongs in main chapters versus appendices.
- How much machine-readable source metadata to maintain.
- Exact chapter allocation inside future special-topic volumes.
