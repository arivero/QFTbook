# Common Agent Contract For Parallel Development

## Mission

The monograph is a foundational rebuild of quantum field theory.  It is not a
survey, not a textbook rewrite, and not a compilation of named results.  Each
agent must produce theorem-quality mathematical physics text: definitions
with ambient data, statements with hypotheses, derivations with objects
constructed rather than asserted, and honest status labels when a proof is
not currently supplied.

## Non-Negotiable Standards

- Do not draft from generic memory.
- Do not import a nontrivial physics claim solely by citation.
- Do not use slogans as definitions or section content.
- Do not write "it is well known" unless the result is then stated and
  derived, proved, or status-labeled.
- Do not label a physics-literature expectation as a theorem unless the
  hypotheses and proof are present in the monograph.
- Every symbol in a load-bearing formula must have a type and domain.
- Every regulator-dependent statement must name the regulator and the
  topology, norm, formal-power-series sense, or observable class in which it
  is asserted.
- Every gauge-theory Wilsonian or 1PI statement must be formulated in a
  consistent framework: BV, lattice, or another explicitly specified
  replacement with a stated master identity.
- Use `quotedtheorem` only as an honesty boundary, not as final depth for a
  central QFT result.

## Source And Reference Discipline

1. Read the relevant current chapter and dossier before editing.
2. Review `claude_review.md` and the relevant open GitHub issue.
3. Search the repo for existing treatment before adding new material.
4. Use the stringbook only as an internal source spine and convention guide;
   the monograph must go beyond it.
5. If outside references are needed, download them into `references/` or a
   suitable ignored subfolder, make a text sidecar when useful, and record
   their role in the dossier or build audit.
6. References are not authority.  Re-derive the argument or state the exact
   theorem boundary.

## Parallel Git Discipline

- Work on a branch with prefix `codex/` unless instructed otherwise.
- Before editing, inspect `git status --short`.
- Never revert unrelated user or agent changes.
- Avoid touching files outside the lane unless necessary.
- Do not stage `.claude/` or `claude_review.md`.
- If a GitHub issue is fully addressed, comment on the issue with:
  - commit hash;
  - files changed;
  - theorem/proof content added;
  - verification commands;
  - reason the issue is closed.
- Do not close an issue unless every stated concern has been satisfactorily
  addressed at the monograph standard.

## Required Chapter-Work Artifacts

For every substantive chapter edit, update or create:

- the chapter TeX file;
- the chapter dossier under `planning/chapter_dossiers/...`;
- a build audit note under `planning/build_audits/`;
- a calculation check under `calculation-checks/` when signs, combinatorics,
  special-function identities, beta functions, or finite algebra are involved.

The calculation check does not replace the derivation; it verifies fragile
arithmetic or conventions.

## Verification Commands

Run the smallest relevant checks first.  For a normal TeX-only lane:

```sh
tools/audit_monograph_text.sh
tools/audit_chapter_dossiers.sh
git diff --check
tools/build_monograph.sh
rg -n "LaTeX Warning: Reference|LaTeX Warning: Citation|Undefined control sequence|Overfull|Underfull|Fatal error|Emergency stop|Missing .* inserted|Token not allowed|Foreign command" monograph/tex/main.log
pdfinfo monograph/tex/main.pdf
```

If calculation checks were edited:

```sh
python3 calculation-checks/<script>.py
tools/run_calculation_checks.sh
```

Do not rerun heavyweight global calculation checks merely for unrelated TeX
edits.  If a script is edited, verify that script directly.  If a Wolfram
Language script is edited, verify the actual Wolfram backend and record the
success marker.

## Final Report Format

The final report should include:

- branch and commit hash;
- GitHub issue numbers touched;
- files changed;
- new definitions, theorems, propositions, examples, or open problems;
- calculation checks added or run;
- full build status and PDF page count;
- remaining proof obligations.

## Style Of Mathematical Writing

Each section should change the reader's mathematical state.  A good section
contains:

- primitive data and framework;
- definition or construction;
- theorem/proposition/lemma with hypotheses;
- derivation or proof;
- substantial example or comparison;
- precise limitation or open problem when needed.

Avoid wrappers, bureaucratic summaries, and motivational filler.  Develop the
physics and mathematics.
