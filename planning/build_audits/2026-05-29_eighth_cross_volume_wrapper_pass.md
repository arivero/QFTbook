# Eighth Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: continued the active #691 audit after reviewing `claude_review.md` and
the live open GitHub issue list.  This pass focused on theorem-family
statements whose proofs were elementary finite algebra, direct bookkeeping, or
canonical convention checks, while strengthening short proofs that carry real
structural content.

## Demotions

Demoted eight theorem-family wrappers to prose calculations or ledgers:

- `Primary constraint, Gauss constraint, and canonical Hamiltonian`.
- `First-class constraints generate Maxwell gauge transformations`.
- `Translation from the origin and descendant fields`.
- `Parabolic Taylor-subtraction gain`.
- `First law as the derivative of relative entropy`.
- `Finite Berezin Gaussian identities`.
- `Riemann--Hurwitz ledger for twist correlators`.
- `Spectral meaning of a finite residual`.

All removed labels were checked for stale references across `monograph/tex`,
`planning`, and `tools`.

## Strengthened Retained Statements

- Expanded `Variational derivation of TBA` to include the admissible density
  variations, hole-density variation, kernel-transpose convention, and the
  cancellation that gives the stationary free-energy formula.
- Expanded `Linking phase in finite BF theory` to identify the cohomological
  reason the linking integer is well defined on \(S^D\) and to state the
  result as an exact finite-sum ratio.
- Strengthened `Exact lattice chiral symmetry and the finite Berezinian` by
  adding \(\gamma_5\)-Hermiticity to the hypotheses and proving integrality
  using the Hermitian involution
  \(\widehat\gamma_5=\gamma_5(1-aD)\).

## Guardrails

`tools/audit_theorem_form.py` now rejects recurrence of the eight demoted
titles as theorem-family wrappers.

## Verification

Commands run:

- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py`
- stale-label `rg` scan for all removed labels
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`

The first full build caught one small overfull line in the Riemann--Hurwitz
paragraph; the prose was reflowed and the build rerun.  Final result:

- Full monograph build and log scan clean.
- Built PDF: `monograph/tex/main.pdf`, 2584 pages.

## Remaining Queue

Using the current `<=105`-word immediate-proof heuristic, the queue is now 30
items.  This is a reading queue rather than a defect count: it contains some
compact but genuine structural proofs, some corollaries of deep quoted input,
and likely further elementary wrappers that still require manual reading.
