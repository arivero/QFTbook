# Twenty-First Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

## Purpose

Continue the end-to-end audit of theorem/proposition/lemma/corollary status
requested in #691.  The operative distinction in this pass is between
load-bearing machinery and direct applications of earlier theorems or
definitions.  Direct applications remain in the manuscript when they clarify a
formula, but they should not pretend to be independent theorem-level results.

## Demoted From Theorem-Family Form

- `Finite-dimensional Schrödinger regulators inherit Trotter--Kato` in Volume I
  Chapter 8 is now a framework paragraph.  The mathematical theorem is the
  finite-dimensional Trotter--Kato/Feynman--Kac theorem in Chapter 4; Chapter 8
  only checks when a field regulator actually reduces to that theorem's
  hypotheses.
- `Locality and Slavnov--Taylor control` in Volume II Chapter 18 is now a
  mechanism paragraph.  The nontrivial input is the quantum action principle
  together with local BRST cohomology, and the all-order theorem immediately
  following carries the explicit hypotheses.
- `Spectral thresholds and first-sheet cuts` in Volume I Chapter 11 is now a
  worked analytic-continuation paragraph.  The branch-cut location follows
  directly from the Källén--Lehmann denominators, so the useful content is the
  threshold bookkeeping and boundary-value convention.
- `Finite-volume Lehmann representation` in Volume X Chapter 4 is now a worked
  spectral-decomposition paragraph.  The Boltzmann weights and positivity
  formula remain fully displayed.
- `Cylinder variation of the reduced eta invariant` in Volume XII Chapter 7 is
  now a cylinder specialization paragraph following the quoted APS index
  theorem.  The modulo-integer eta variation formula remains displayed.

## Retained After Reading

The following short/cue-heavy candidates were read in context and retained in
theorem-family form for now because their proofs carry structural content used
later, rather than merely restating a hypothesis or substituting into one
formula: Fredholm expansion for trace-class kernels, GNS unitary implementation
of an invariant state, transfer-matrix commutativity from RTT, Dijkgraaf--Witten
triangulation independence, McKean--Singer, Lichnerowicz, the K-S positive-energy
cylinder statement, Coulomb-slice atlas, QME observable differential, and
Feshbach--Schur reduction with a resolvent estimate.

The three score-four heuristic candidates remain retained for the reason
recorded in earlier passes: finite Grassmann reflection positivity, the
largest-time identity, and positive-energy supersymmetric pairing are reusable
mechanisms, not trivial substitutions.

## Counts After This Pass

- Theorem/proposition/lemma/corollary environments: 607.
- Proof environments: 602.
- Short/cue-heavy heuristic queue: 122 candidates, split as 3 score-four,
  10 score-three, and 109 score-two items.

## Verification

- Stale-label scan for the five removed labels: clean.
- `python3 tools/audit_theorem_form.py`: clean.
- `tools/audit_negative_scope_prose.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2581`.
