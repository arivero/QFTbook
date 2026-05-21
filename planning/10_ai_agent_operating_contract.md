# AI Agent Operating Contract

AI agents working on this project must treat the planning layer as binding.
The goal is not to produce plausible QFT prose. The goal is to produce a
source-grounded, logically ordered, symbol-complete monograph.

## Core Rules

- Follow the logical order of Xi Yin's QFT notes.
- Do not draft from generic memory.
- Do not treat student transcriptions as authoritative.
- Do not treat any axiomatic framework as the universal foundation.
- Do not import the organization of standard textbooks.
- Define all symbols before load-bearing use.
- Use proper definitions in the stated framework.
- State assumptions before consequences.
- Classify every major claim.
- Use external references for theorem-level claims not proved in the chapter.
- Keep the transcription layer separate from the monograph.
- Include only audited chapters in the compiled TeX.

## Prose Rules

Reader-facing prose should be organized by:

- framework;
- data;
- definition;
- construction;
- theorem or proposition;
- derivation;
- example;
- domain statement;
- comparison remark.

Avoid organizing the main text around wrong pictures, slogans, or textbook
correction. When a misconception must be named, place it after the correct
formulation and keep it local.

## Framework Rules

For each framework, state its data and domain:

- Hilbert-space local QFT;
- Wightman fields;
- local observable nets;
- Euclidean Schwinger functions;
- regulated path integrals;
- formal perturbative expansions;
- BRST/BV complexes;
- asymptotic scattering spaces;
- Wilsonian effective actions;
- conformal data.

Never move formulas among these frameworks without a theorem, derivation, or
explicit formal-status label.

## Required Outputs For Chapter Work

After drafting or revising a chapter, report:

- files changed;
- source anchors used;
- external references used;
- definitions introduced or corrected;
- symbols added to the notation inventory;
- claims added, proved, quoted, or reclassified;
- figures added or changed;
- build and audit result;
- unresolved issues.

## Good Work Units

- create a chapter dossier;
- type-check all symbols in a chapter;
- verify a figure against the handwritten source;
- classify all path-integral expressions;
- locate all theorem-level claims needing references;
- rewrite a slogan paragraph into definitions and propositions;
- compare one external framework with the local construction.

## Failed Work Patterns

- drafting a chapter before its dossier;
- writing formulas with undefined symbols;
- using "standard QFT says" as evidence;
- adding a theorem without hypotheses;
- using an axiom system as a universal foundation;
- discussing S-matrix perturbatively before the nonperturbative construction;
- treating gauge redundancy as a physical symmetry;
- adding decorative figures;
- moving unrevised scaffold chapters into the compiled manuscript.

## Machine-Readable Structure To Add Later

The project may eventually add:

- YAML chapter dossiers;
- notation ledgers;
- claim ledgers;
- figure ledgers;
- dependency graphs;
- citation-support checks;
- automated TeX audits;
- visual PDF audits.

These tools should support the book; they should not replace mathematical
judgment.
