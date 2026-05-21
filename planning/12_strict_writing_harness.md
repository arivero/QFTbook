# Strict Writing Harness

This file is the immediate hard gate for all reader-facing monograph drafting.

## Source-First Rule

For each chapter, work in this order:

1. locate the chapter in the source-note logical spine;
2. read the corresponding handwritten or transcribed source section;
3. compare student transcriptions only as non-authoritative aids;
4. identify rigorous external references for theorem-level claims;
5. write or update the chapter dossier;
6. draft the chapter;
7. audit before inclusion in compiled TeX.

No step may be skipped because the topic is familiar.

## Modular Foundation Rule

No existing framework is the universal foundation of the monograph. For every
construction, state the local framework and its data. Use Wightman, OS, AQFT,
perturbative AQFT, constructive, factorization, functorial, and
Kontsevich--Segal-type frameworks as theorem sources and comparison lenses,
with their domains stated.

## Definition Integrity Rule

Every definition must state:

- ambient setting;
- input data and types;
- domains and codomains;
- support, topology, continuity, distributional, or operator-domain conditions;
- covariance, locality, positivity, spectral, grading, or functoriality
  conditions when relevant;
- whether the object is primitive or constructed.

Forbidden in reader-facing definitions:

- undefined symbols;
- pointwise operator fields without smearing;
- path-integral notation without status;
- gauge symmetry as ordinary physical symmetry without physical-observable
  definition;
- S-matrix formulas before asymptotic states and wave operators;
- slogan or analogy as definition.

## Symbol Rule

Every symbol must be introduced with its type before load-bearing use. If a
symbol changes meaning across frameworks, rename it or explicitly declare the
change.

## Claim Certification Rule

Every load-bearing claim must be one of:

- definition or convention;
- assumption;
- construction;
- derivation in the chapter;
- theorem with hypotheses and reference;
- controlled approximation;
- formal calculation with formal status;
- conjecture or open problem.

Uncertified claims cannot appear in polished TeX.

## Positive Formulation Rule

The main text explains objects by their data, definitions, assumptions, and
consequences. It should not be organized around:

- slogans;
- generic textbook correction;
- wrong pictures used as foils;
- "what it is not" framing;
- surprise or exception language where a clean domain statement is available.

Negative clarification is allowed only in a remark, footnote, or appendix after
the positive construction has been given and only to prevent a specific
misreading.

## QFT Ordering Rule

- Kallen--Lehmann spectral representation appears early.
- Perturbation theory for Green functions may precede scattering.
- The S-matrix is nonperturbative first.
- LSZ follows the nonperturbative scattering construction.
- Perturbative S-matrix diagrams follow LSZ.

## Compilation Gate

Only chapters that pass this harness may be included in the compiled
manuscript. Draft files may remain on disk but must stay out of volume include
files.

## Audit Questions

- What is the framework?
- What are the primitive data?
- What is constructed?
- Are all symbols defined?
- Are all definitions proper?
- What is the first nontrivial claim?
- Where is that claim proved, sourced, or classified?
- Are all limits and approximations stated?
- Are all figures mathematical content?
- Does the chapter preserve the source-order spine?
