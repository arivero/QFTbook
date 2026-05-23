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
  uniformization queue for compiled and future volumes.

Historical build audits and chapter dossiers are preserved in subdirectories.

## Compiled Volumes and On-Disk Directories

The directory names under `monograph/tex/volumes/` are historical storage
locations.  They do not by themselves define the compiled volume order.  The
compiled order is defined by the manifest files
`monograph/tex/volumes/volume_*/*_current.tex`, each of which lists the
chapters included in that compiled volume.

| Compiled volume | Part title | Chapter count | On-disk chapter directories used |
| --- | --- | ---: | --- |
| I | Foundations of Local Quantum Field Theory | 15 | `volume_i/`, `volume_iv/` |
| II | Particles, Scattering, and Analyticity | 13 | `volume_i/`, `volume_ii/`, `volume_iv/` |
| III | Renormalization, Effective Field Theory, and Critical Phenomena | 9 | `volume_ii/` |
| IV | Gauge Theory, Infrared Structure, and Anomalies | 11 | `volume_i/`, `volume_ii/` |
| V | Conformal Field Theory | 9 | `volume_iii/` |
