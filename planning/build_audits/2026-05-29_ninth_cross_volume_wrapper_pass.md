# Ninth Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: continued the active #691 audit after refreshing `claude_review.md` and
the live open GitHub issue list.  This pass read another compact-proof cluster
in context and separated convention-level calculations from substantive
finite-structure statements.

## Demotions

Demoted four theorem-family wrappers to prose calculations:

- `Purely odd Berezinian transformation`.
- `Crossing of the invariant tensors`.
- `Off-shell closure`.
- `Mass and chemical-potential contribution to mismatch`.

All removed labels were checked for stale references across `monograph/tex`,
`planning`, and `tools`.

## Strengthened Retained Statements

- Retained `Finite collision conservation and entropy production` and
  `Finite linearized collision operator` as substantive finite kinetic
  models, but expanded the proofs to state the open-domain/logarithm
  condition, the classical/Bose/Fermi entropy derivative convention, the
  reactionwise positivity argument, and the exact identification of the
  linearized null space with collision invariants.
- Retained `State-space duality from caps and cylinders` as a structural
  Atiyah-Segal consequence, but expanded the proof from a reference to
  triangular identities into explicit finite-dimensional maps, injectivity,
  dimension comparison, and inverse-tensor conclusion.

## Guardrails

`tools/audit_theorem_form.py` now rejects recurrence of the four demoted
titles as theorem-family wrappers.

## Verification

Commands run:

- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- stale-label `rg` scan for all removed labels

Additional checkpoint verification completed:

- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` (`Pages: 2583`)

The first full build attempt caught a paragraph-heading overfull hbox introduced
by demoting the dense-matter mismatch calculation; the heading was shortened and
the final full build/log scan is clean.

## Remaining Queue

The `<=105`-word immediate-proof heuristic queue is now 23 items.  The queue
is still a manual reading queue: some entries are compact proofs of real
machinery or corollaries of quoted global-analysis input, while others may
still need demotion or expansion.
