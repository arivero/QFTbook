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

External references are study tools and theorem-boundary checks. They do not
license the manuscript to import a nontrivial physics claim as an unexplained
fact. If a claim is used in the logical development, the chapter must carry
its assumptions and argument, or else mark it as an external theorem with a
precise statement and state that the proof is outside the present scope.

## No-Skip Source Coverage Rule

The 253a and 253b source notes are a coverage obligation for the core
monograph.  The 253c source notes are a coverage obligation for the CFT and
later special-topic volumes, with only the core CFT portion currently included
in the compiled manuscript.  A chapter may deepen, reorganize, correct, or
generalize the source material, but it may not silently omit a source
derivation, example, figure, definition, or conceptual distinction.  Each
source block must be accounted for in a dossier, audit note, or coverage
register as one of:

- incorporated in the compiled monograph;
- incorporated after a corrected derivation or notation change;
- deferred to a specified later core chapter;
- moved to a specified non-core or deprecated file because the topic is
  outside the current core scope.

Compression is not coverage.  A result stated without the source calculation
is a gap when the source calculation carries conceptual content.

## Modular Foundation Rule

No existing framework is the universal foundation of the monograph, and no
framework is valuable merely because it is axiomatic.  For every construction,
state the local framework and its data. Use Wightman, OS, AQFT, perturbative
AQFT, constructive, factorization, functorial, and Kontsevich--Segal-type
frameworks as theorem sources, comparison lenses, and example-building tools,
with their domains stated.  A framework discussion passes the harness only if
it produces nontrivial information: a theorem with hypotheses, a construction,
an example, a comparison map, a limitation, or a precise open problem.

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
- theorem with hypotheses, reference, and a statement of whether the proof is
  included, sketched, or deliberately deferred;
- controlled approximation;
- formal calculation with formal status;
- conjecture or open problem.

Uncertified claims cannot appear in polished TeX.

A citation alone is not a certificate for a nontrivial physics claim. For
central physics claims, the monograph should give a self-contained derivation
or argument from the chapter's stated data. External theorem citations are
permitted only when the theorem is a mathematical input whose hypotheses,
domain, conclusion, and role in the local argument have been made explicit.
If those hypotheses are not verified in the chapter, the conclusion must be
phrased conditionally.

Proofs must not use structural prose as a substitute for construction.  When
a statement asserts a coordinate change, a matching map, a quotient, a contact
term, a limiting object, a topology, a measure, or an equivalence of
functionals, the proof must construct the object or cite an earlier theorem in
the monograph that constructs it.  In particular:

- a phrase such as "absorbed into local coordinates" must be accompanied by
  the displayed coordinate map or by a recursive construction of that map;
- a phrase such as "suppressed by powers" must give the norm or seminorm, the
  exponent, the constants' dependencies, and the scale regime;
- a phrase such as "Legendre transformation gives" must identify the source
  space, the classical-field space, the convexity or Hessian hypothesis, and
  whether the object is a low-mode Legendre transform or a restriction of a
  larger functional;
- a phrase such as "same continuum limit" must state the object that
  converges and the topology or correlation-function sense of convergence.

Known proofs should be developed when they are part of the monograph's
logical spine.  Highly technical proofs may be placed in chapter appendices or
technical subsections, but the main text must point to the proof and state the
precise theorem being proved.  Do not omit a key argument because it is long.

Do not promote an expected large-class statement to a theorem because the
physics literature uses that name.  In CFT, RG flow, bootstrap, anomaly,
duality, large-\(N\), or continuum-limit contexts, theorem labels require a
specified framework, hypotheses, conclusion, and proof status.  Otherwise the
claim must be stated as a conditional argument, conjecture, criterion, formal
calculation, or open problem.

For invariance, anomaly, duality, matching, universality, or reconstruction
claims, the text must identify the object being compared and the equivalence
relation.  Examples: equality of generating functionals, equality of cocycle
classes modulo local counterterms, convergence of correlation functions in a
stated limit, equivalence of local nets, or isomorphism of representation
data.  A named principle without this object-level statement is not certified.

Every example used in the main text must do at least one of the following:

- verify a definition in a nontrivial case;
- show that a hypothesis is necessary;
- compute an invariant introduced in the chapter;
- mark the boundary of a theorem.

Examples that only decorate the prose fail the harness.

## Soft Phrase Audit Rule

Reader-facing prose must not use community habit as a substitute for data.
During every audit pass, search for soft phrases such as "usual",
"standard", "well-known", "schematic", "formal", "one can show", and "it is
known".  Each occurrence must be classified as one of:

- a harmless fixed name or convention already defined in the text;
- a displayed shorthand whose regulated or distributional meaning is stated
  immediately nearby;
- a theorem-level input with hypotheses and proof status;
- a phrase to be rewritten into explicit assumptions, definitions, or a
  conditional statement.

The words themselves are not banned, since terms such as standard boost or
standard representation can be mathematically precise after definition.  What
is forbidden is using them to hide hypotheses, domains, convergence,
normalization, or proof obligations.

## Positive Formulation Rule

The main text explains objects by their data, definitions, assumptions, and
consequences. It should not be organized around:

- slogans;
- lore or folklore;
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

## Gauge And RG Separation Rule

- Spectral representations are statements about operators acting on the
  relevant positive Hilbert space, or about explicitly stated indefinite
  gauge-fixed spaces.  Gauge-variant propagators must not be treated as
  physical spectral measures.
- The 1PI renormalization group is a comparison of scale-dependent
  coordinates on the 1PI effective action.
- The Wilsonian renormalization group is a cutoff-dependent action flow
  defined by integrating out modes while preserving low-momentum observables.
- Physical scaling limits are statements about correlation functions,
  operator dimensions, spectra, or other specified observables.  These three
  RG notions may be related only after the map between their data is stated.

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
- Where is that claim proved, argued, or classified?
- If an external theorem is cited, are its hypotheses, conclusion, and local
  role stated, and is the proof status clear?
- Are all limits and approximations stated?
- Are all figures mathematical content?
- Does the chapter preserve the source-order spine?
