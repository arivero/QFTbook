# Quality And Audit Workflow

## Hard Stop Conditions

Stop drafting and return to source or dossier work if:

- a chapter lacks a framework declaration;
- a definition omits symbol types, domains, codomains, or essential
  assumptions;
- a symbol is used load-bearingly before being defined;
- a theorem-like claim lacks hypotheses or reference;
- a path integral lacks mathematical status;
- a Wick rotation lacks analytic or reconstruction input;
- scattering language uses the S-matrix before asymptotic states have been
  constructed;
- gauge redundancy is described as an ordinary physical symmetry;
- a section is organized by slogan or negative contrast;
- an axiomatic framework is treated as the universal foundation without
  qualification;
- a figure is decorative where mathematical content is required.

## Stage 0: Source Preservation

The faithful transcription remains separate from the monograph. It is a source
layer, not the polished book.

## Stage 1: Source Study

For the chapter under development:

- read the relevant handwritten notes or transcription;
- compare Ben Lou notes only as a cautionary aid;
- identify external references for theorem-level claims;
- record exact source anchors.

## Stage 2: Dossier

Create or update the chapter dossier:

- framework declaration;
- notation inventory;
- definition ledger;
- claim ledger;
- derivation plan;
- figure ledger;
- open questions;
- planned remarks or footnotes.

## Stage 3: Draft

Write reader-facing prose only from the dossier. The draft should introduce
objects positively and state all assumptions before consequences.

## Stage 4: Local Audit

Check:

- undefined symbols;
- incomplete definitions;
- unsupported claims;
- hidden framework changes;
- unclear limits;
- unlabelled formal manipulations;
- misplaced scattering, path-integral, or gauge language;
- figures not tied to definitions or equations;
- prose organized around "what it is not."

Every paragraph should be classifiable as one of:

- framework statement;
- definition;
- convention;
- assumption;
- construction;
- derivation;
- theorem or proposition;
- example;
- domain statement;
- comparison remark;
- transition.

## Stage 5: Build And Visual Audit

Run the audit and build scripts. Inspect the log and the rendered PDF. Figures
must be checked visually against their mathematical intent.

## Stage 6: Cross-Chapter Audit

Check:

- dependency order;
- notation consistency;
- repeated or inconsistent definitions;
- theorem status across chapters;
- use of later ideas before their construction;
- figure conventions across chapters.

## Required Report After Chapter Work

Any chapter-writing pass should report:

- files changed;
- sources used;
- definitions added or corrected;
- claims added or reclassified;
- figures added or corrected;
- build/audit result;
- unresolved issues.
