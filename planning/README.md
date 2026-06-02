# Planning Layer

This directory is the operating constitution for the QFT monograph. Its purpose
is to keep the manuscript faithful to the logical order of Xi Yin's QFT notes
while raising the exposition to a substantially higher level of precision,
scope, and mathematical care.

The planning layer is not reader-facing prose. It may mention source notes,
student transcriptions, audits, and workflow rules that must not appear in the
finished monograph.

## Active Principles

- The monograph is multi-volume.
- The author line is: "GPT 5.5 under the supervision of Xi Yin".
- The logical order follows Xi Yin's QFT notes.
- Volume divisions are by subject matter, not by semester sequence.
- The main text explains objects by their definitions, data, assumptions, and
  consequences.
- Existing nonperturbative frameworks are introduced from the beginning as
  framework-specific theorem sources and comparison structures, not as a
  single final foundation and not as a detached appendix.
- Every reader-facing definition must define all symbols, domains, codomains,
  support conditions, topology or continuity assumptions when relevant, and
  framework of validity.
- Only audited chapters enter the compiled manuscript.

## Document Map

- `00_project_manifesto.md`: project constitution and non-negotiable aims.
- `01_audience_and_expository_contract.md`: human and AI reader contract.
- `02_epistemic_and_rigor_standards.md`: claim, definition, symbol, and proof
  standards.
- `03_source_hierarchy_and_crosswalk.md`: source priority and local source map.
- `04_master_architecture.md`: multi-volume logical architecture.
- `05_axiomatic_frameworks_and_foundations.md`: status of Wightman, OS, AQFT,
  perturbative AQFT, factorization, and related frameworks.
- `06_chapter_blueprint_template.md`: required dossier before chapter drafting.
- `07_quality_and_audit_workflow.md`: audit and build workflow.
- `08_first_milestones.md`: immediate work sequence.
- `09_misconception_ledger.md`: controlled record of remarks and footnotes.
- `10_ai_agent_operating_contract.md`: rules for AI collaborators.
- `11_project_decisions.md`: explicit decisions from Xi.
- `12_strict_writing_harness.md`: immediate hard gate for drafting.
- `13_development_dependency_map.md`: dependency order, promotion gates, and
  uniformization queue for the compiled volumes.
- `14_code_policy.md`: reproducibility and public-facing calculation companion
  policy.
- `15_convention_dictionary.md`: global convention defaults, chapter-header
  macros, and chapter-local deviations.
- `16_primary_definitions.md`: canonical homes of load-bearing definitions and
  theorem families.
- `agent_handoffs/`: detailed parallel-work packets for agents developing
  independent topics simultaneously.

Chapter dossiers are preserved in this public planning layer. Historical
build-audit logs are local process records under the ignored
`planning/build_audits/` directory and are not part of the public repository
distribution.

## Full Volume Program

The public monograph program currently has twenty numbered volumes.  Volumes
I-XII are active compiled volumes.  Volumes XIII-XX are roadmap volumes whose
subject scope is part of the public architecture but whose source assemblies
are not yet active compiled volumes.

| Volume | Status | Title |
| --- | --- | --- |
| I | Compiled | Foundations of Local Quantum Field Theory |
| II | Compiled | Particles, Scattering, and Analyticity |
| III | Compiled | Renormalization, Effective Field Theory, and Critical Phenomena |
| IV | Compiled | Gauge Theory, Infrared Structure, and Anomalies |
| V | Compiled | Conformal Field Theory |
| VI | Compiled | Integrable Quantum Field Theory |
| VII | Compiled | Supersymmetric Quantum Field Theory |
| VIII | Compiled | Topological and Cohomological Quantum Field Theory |
| IX | Compiled | Global Structure, Phases, and Extended Operators |
| X | Compiled | Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics |
| XI | Compiled | Constructive, Lattice, and Numerical Quantum Field Theory |
| XII | Compiled | Quantum Field Theory in Curved Spacetime and Background Fields |
| XIII | Roadmap | Large-N Gauge Theory, QCD Strings, Flux Tubes, Baryons, and Gauge-String Expansions |
| XIV | Roadmap | Advanced Local-Algebraic QFT and Modular Structure |
| XV | Roadmap | Advanced Scattering, Amplitudes, Resonances, and Infrared-Safe Observables |
| XVI | Roadmap | Advanced Supersymmetric Theories and Protected Sectors |
| XVII | Roadmap | Advanced Two-Dimensional CFT and Exact Two-Dimensional QFT |
| XVIII | Roadmap | Advanced Constructive, Stochastic, and Rigorous Wilsonian QFT |
| XIX | Roadmap | Advanced Phases, Defects, Categorical Symmetry, and Extended-Operator Theory |
| XX | Roadmap | Advanced Curved-Background, Locally Covariant, and Semiclassical QFT |

## Compiled Volumes and On-Disk Directories

The directory names under `monograph/tex/volumes/` are historical storage
locations.  They do not by themselves define the compiled volume order.  The
compiled order is defined by the manifest files
`monograph/tex/volumes/volume_*/*_current.tex`, each of which lists the
chapters included in that compiled volume.
Chapter counts below are printed `\chapter` counts, not raw input counts.
For example, Volume IV currently has one extra section-level input for the
spinor-convention material inside its first printed chapter.

| Compiled volume | Part title | Chapter count | On-disk chapter directories used |
| --- | --- | ---: | --- |
| I | Foundations of Local Quantum Field Theory | 16 | `volume_i/`, `volume_iv/` |
| II | Particles, Scattering, and Analyticity | 13 | `volume_i/`, `volume_ii/`, `volume_iv/` |
| III | Renormalization, Effective Field Theory, and Critical Phenomena | 10 | `volume_ii/` |
| IV | Gauge Theory, Infrared Structure, and Anomalies | 16 | `volume_i/`, `volume_ii/` |
| V | Conformal Field Theory | 15 | `volume_iii/`, `volume_v/` |
| VI | Integrable Quantum Field Theory | 14 | `volume_vi/` |
| VII | Supersymmetric Quantum Field Theory | 17 | `volume_vii/` |
| VIII | Topological and Cohomological Quantum Field Theory | 11 | `volume_viii/` |
| IX | Global Structure, Phases, and Extended Operators | 11 | `volume_ix/` |
| X | Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics | 12 | `volume_x/` |
| XI | Constructive, Lattice, and Numerical Quantum Field Theory | 11 | `volume_xi/` |
| XII | Quantum Field Theory in Curved Spacetime and Background Fields | 11 | `volume_xii/` |
