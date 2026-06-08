# Chapter Blueprint Template

Every mature chapter requires a dossier before reader-facing drafting.

## Pre-Draft Gate

The dossier must contain:

- working title and volume;
- exact compiled source key, recorded as
  `Source-File: monograph/tex/volumes/.../chapter....tex` immediately after
  the dossier title;
- logical role in the source spine;
- primary source anchors;
- comparison sources;
- external references for theorem-level claims;
- framework declarations;
- notation inventory;
- definitions to be introduced;
- primitive data versus constructed objects;
- claim ledger;
- derivation plan;
- figure ledger;
- open questions;
- forbidden framings for this chapter.

If any item is absent, the chapter is not ready for drafting.

## Framework Declaration

State every framework used in the chapter. For each framework, record:

- ambient space or category;
- objects;
- morphisms or maps when relevant;
- topology, smoothness, measure, distributional, algebraic, or operator-domain
  assumptions;
- positivity, locality, spectral, covariance, grading, or reflection-positivity
  conditions;
- relation to previous frameworks in the monograph.

## Notation Inventory

For every symbol introduced, record:

- symbol;
- type;
- domain and codomain if it is a map or operator;
- first planned use;
- framework;
- possible conflicts with existing notation.

No symbol may be introduced only by context if it becomes load-bearing.

## Definition Ledger

For every definition, record:

- name;
- purpose;
- precise statement;
- ambient framework;
- all data and their types;
- all required conditions;
- examples;
- non-examples or failure modes, only as dossier material unless needed in a
  remark;
- downstream use.

## Claim Ledger

For every major claim, record:

- claim statement;
- status;
- assumptions;
- proof or argument in chapter, theorem reference with hypotheses and proof
  status, or formal status;
- framework of validity;
- failure mode or changed-domain case;
- downstream dependency.

Claims without certification cannot enter polished prose.
For nontrivial physics claims, a reference is not enough: the ledger must
point to the self-contained derivation or argument planned for the chapter, or
state that the claim is conditional on an external theorem whose hypotheses
are explicitly listed.

## Derivation Plan

For each derivation, record:

- starting definitions and assumptions;
- algebraic or analytic steps;
- regulated objects and limit order if any;
- topology or sense of equality;
- conclusion;
- what is deferred to a theorem or reference.

## Figure Ledger

For every figure, record:

- mathematical purpose;
- source or original design;
- whether schematic or exact;
- coordinate conventions;
- labels;
- visual checks;
- relation to equations or definitions.

Figures are content. A figure that cannot be stated mathematically is not ready
for the monograph.

## Misconception Handling

Record common misleading presentations only when they affect the chapter. For
each one, decide:

- no mention in final prose;
- footnote;
- remark;
- appendix;
- source for the misconception ledger.

The main chapter spine should remain positive: definitions, assumptions,
constructions, and consequences.

## Chapter Readiness Questions

- Are all symbols typed?
- Are all definitions proper for their framework?
- Are all assumptions visible?
- Are exact, regulated, perturbative, formal, heuristic, conjectural, and open
  statements separated?
- Are theorem-level claims proved, sketched, or quoted with hypotheses and
  proof status?
- Does every nontrivial physics claim have a self-contained argument in the
  chapter or a clearly conditional theorem dependency?
- Does every load-bearing theorem, proposition, construction, approximation,
  or formal calculation have enough proof detail in the main chapter for the
  reader to see why it applies in the stated framework?
- If a proof is deferred to an appendix, does the main chapter still state the
  exact result, all hypotheses, the sense of equality or convergence, and the
  specific role of the deferred argument?
- Is any "sketch" explicitly non-load-bearing, or else upgraded to a complete
  derivation, a precise theorem boundary, or a marked open problem?
- Are figures accurate?
- Does the chapter preserve the source order?
- Does the chapter avoid textbook ordering habits?
- Does any paragraph make a universal QFT claim without a framework?
