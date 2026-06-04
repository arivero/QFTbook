# Quality And Audit Workflow

## Hard Stop Conditions

Stop drafting and return to source or dossier work if:

- a chapter lacks a framework declaration;
- a definition omits symbol types, domains, codomains, or essential
  assumptions;
- a symbol is used load-bearingly before being defined;
- a theorem-like claim lacks hypotheses or reference;
- a principle is stated without specifying the object whose equality,
  invariance, convergence, or obstruction is being asserted;
- an example is used only as illustration and does not test a definition,
  hypothesis, or theorem boundary;
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
- download any necessary public external reference into `references/` or
  `references/sound_references/`;
- create a readable text sidecar before using the reference for drafting;
- record exact source anchors.

## Stage 1A: External Reference Intake

When a new external source is needed:

- prefer stable public sources such as arXiv, journal-author copies, lecture-note
  PDFs from the author, or official institutional repositories;
- save the PDF with a descriptive filename in `references/sound_references/`;
- generate a `.txt` sidecar with `pdftotext -layout` or a better extraction
  method available for that source;
- update `references/sound_references/README.md` with its bibliographic role;
- inspect the sidecar for extraction failures before relying on it;
- record in the chapter dossier which sections or theorem statements are used;
- do not import the reference's order of presentation into the monograph unless
  the monograph's own logical spine independently requires it.
- when the literature contains a genuine gap, record the gap as a precise
  construction, comparison, or theorem problem rather than as a vague
  bibliographic absence.

## Stage 2: Dossier

Create or update the chapter dossier:

- framework declaration;
- notation inventory;
- definition ledger;
- claim ledger;
- derivation plan;
- frontier-gap ledger when the chapter touches undeveloped or incomplete
  mathematical physics;
- figure ledger;
- open questions;
- planned remarks or footnotes.

The claim ledger must separate:

- assumptions;
- definitions and conventions;
- constructions;
- derivations performed in the chapter;
- theorem-level inputs quoted with hypotheses and references;
- examples, with the definition or theorem they test.

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
- terms such as "lore", "slogan", "miracle", "surprise", "roughly speaking",
  or "modern language" in reader-facing prose unless they occur in a quoted
  bibliographic title.

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

For a full rendered figure pass after building the monograph, run

```bash
tools/render_figure_pages.py --force
```

The command requires `qpdf`, Poppler's `pdftoppm`, and Pillow by default.  It
records render provenance under
`monograph/tex/build/figure_audit_current/render_provenance.json`; a non-forced
rerun may reuse cached page PNGs only when the PDF digest, DPI, renderer
identity/version, render options, and stored page digest still match.  Use the
generated contact sheets in
`monograph/tex/build/figure_audit_current/contact/` as overview/triage images,
then inspect the rendered page PNGs at 100 percent scale for print-size labels,
line weights, grayscale distinctions, and caption separation against the figure
style guide.

For convention-sensitive derivations, run the public calculation checks.  The
default entry point is

```bash
tools/run_calculation_checks.sh
```

This script runs the Python checks and then, when `.wl` files exist, requires
a working Wolfram batch backend.  On the author's macOS installation, agents
should prefer
`/Applications/Wolfram.app/Contents/MacOS/WolframKernel -script`; the runner
falls back to `wolframscript -file` only when the kernel entrypoint is not
available.  The runner probes the exact selected backend, rejects known
Wolfram line-continuation parse hazards, runs every committed `.wl` check, and
fails unless each check prints its Wolfram success marker.  Plain `.wl` files
in `calculation-checks/` are preferred over `.nb` notebooks for committed
checks, since `.wl` files are directly diffable and agent-readable.
Computationally heavy or numerical checks should be written in Python; Wolfram
Language is for lightweight symbolic convention checks and reader-facing
algebra.  Use `QFT_SKIP_WOLFRAM=1 tools/run_calculation_checks.sh` only for an
explicitly Python-only pass, never as verification of a touched `.wl` file.

For release candidates, do not confuse a clean build with a release signoff.
Run the aggregate local gate

```bash
tools/verify_release.sh
```

after the working tree is clean.  It records the Git revision, dirty-state
check, tool versions, selected verification Python, dossier and figure-structure
audits, evidence-contract audit, full calculation-check runner, monograph build,
PDF integrity, PDF page count/hash, figure count, and command logs in
timestamped JSON and Markdown manifests under
`monograph/tex/build/release_verification/`.  Add
`--rendered-figures` for a full rendered figure-page regeneration and
`--qft-scripts-smoke` for the public numerical smoke suite; skipped optional
passes are recorded explicitly in the manifest.

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
