# Twenty-Second Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

## Purpose

Continue #691 by reading the next low-score proof candidates as complete
statement-proof units.  This pass focuses on direct consequences of powerful
inputs: Tauberian theorems, residue theorem, KMS strip analyticity, inverse
function theorem bookkeeping, and a duplicate superselection argument.

## Demoted From Theorem-Family Form

- `CFT-internal Cardy growth` is now a Tauberian-consequence paragraph.  The
  analytic theorem is the quoted exponential Tauberian theorem; the CFT step is
  the identification of the positive counting measure and the modular
  high-temperature coefficient.
- `BCFW recursion with boundary term` is now a BCFW residue-formula paragraph.
  The proof is residue theorem bookkeeping for \(A_n(z)\,dz/z\) once the
  factorization poles and boundary term have been assumed.
- `Detailed balance from the KMS boundary relation` is now a contour-shift
  paragraph with the switching-function hypothesis kept explicit.
- `Universal late-time ray tracing` is now a ray-tracing paragraph.  The content
  is the smooth last-ray expansion, the Kruskal exponential, and the
  inverse-function/log expansion.
- `Local operators preserve pure vacuum sectors` was folded into the surrounding
  superselection prose.  The proof duplicated the preceding locality plus
  clustering argument; the character-decomposition nuance is preserved in the
  main text.

## Strengthened

- `Goldstone spectral pole from a broken current` remains a proposition, but its
  hypotheses and proof were tightened.  The text now separates local contact
  polynomial freedom from the nonlocal scalar spectral channel and explains why
  a local vector polynomial contribution \(p_\mu P^\mu(p)\) cannot provide the
  nonzero constant in the broken Ward identity.  The massless pole is identified
  as an atom at \(\mu^2=0\) in the scalar spectral measure.

## Retained After Reading

The following candidates were read and retained in theorem-family form for now:
QME preservation by BV pushforward, Rindler normal form, mass gap from Euclidean
clustering, Wick graph expansion and connected cumulants, the adjoint
\(SU(2)\) Bogomolny lower bound, the charge-one ADHM cone/small-instanton
boundary, contact-term support for time-ordered extensions, and the score-three
infrastructure statements retained in the previous pass.

## Counts After This Pass

- Theorem/proposition/lemma/corollary environments: 602.
- Proof environments: 597.
- Short/cue-heavy heuristic queue: 116 candidates, split as 3 score-four,
  10 score-three, and 103 score-two items.

## Verification

- Stale-label scan for the five removed labels: clean.
- `python3 tools/audit_theorem_form.py`: clean.
- `tools/audit_negative_scope_prose.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 2580 pages.
