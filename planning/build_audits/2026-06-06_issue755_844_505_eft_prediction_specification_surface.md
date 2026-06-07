# 2026-06-06 Issue #755/#844/#505 EFT Prediction Specification Surface

## Scope

- Target: `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`.
- Planning companion: `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md`.
- Issue connection: #755 reader-facing clarity and coherence, #844 formal machinery connected to physical observables, and #505 Wilsonian/EFT depth surface.

## Quality Rationale

This pass is a coherence repair rather than a new calculation annex.  The
chapter already contained the needed finite-regulator EFT machinery,
evanescent projection example, conditional positivity derivation, and
finite-density setup.  The remaining risk was that visible terms such as
"datum", "ledger", and generic "status" made the argument read like internal
bookkeeping rather than a physics prediction workflow.

The TeX now presents the same equations and labels through reader-facing
language organized as:

1. choose an observable problem and domain;
2. state regulator, projection, matching, and RG inputs;
3. identify the retained expression and the meaning of the omitted remainder;
4. apply conditional positivity only after the observable amplitude has been
   specified.

No formula, label, or calculation companion was changed.

## Re-Audit Requirements

- Focused style-density audit for Chapter 16.
- Focused theorem-form, display-label, and negative-scope audits for Chapter 16.
- Process scan confirming no GitHub, review, directive, monitoring, or planning
  language entered the TeX.
- Dossier and monograph text audits.
- Full monograph build.
