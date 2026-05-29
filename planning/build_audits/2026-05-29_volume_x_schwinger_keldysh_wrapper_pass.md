# Volume X Schwinger--Keldysh wrapper pass

Date: 2026-05-29.

This pass continued the issue #691 proof-substance audit in the real-time
Schwinger--Keldysh chapters.  The focus was finite trace algebra and
linear-response sign checks that are important for conventions but do not need
theorem-family wrappers.

Changes made:

- Largest-time cancellation in Volume X Chapter 3 was demoted from
  proposition/proof form to a worked paragraph.  The factorization of the
  common future evolution, trace cyclicity, and unitarity remain explicit.
- The source-response kernel from \(r/a\) differentiation in Volume X Chapter
  3 was demoted from proposition/proof form to a worked paragraph.  The
  source convention, the derivative identity, the kernel formula, and the
  relation to the commutator-retarded convention remain displayed.
- The finite closed-time-path constraints in Volume X Chapter 6 were demoted
  from proposition/proof form to a worked paragraph because the chapter is
  recalling the same finite trace algebra already developed in the microscopic
  Schwinger--Keldysh chapter.
- Chapter dossiers now describe these items as derived trace or
  linear-response identities rather than theorem-family claims.
- `tools/audit_theorem_form.py` now rejects reintroduction of these demoted
  titles, and the shortened hydrodynamic variant, as theorem-family wrappers.

Manual review notes:

- The basic Schwinger--Keldysh constraints proposition in Volume X Chapter 3
  remains theorem-family content in this pass: it is the main finite operator
  statement collecting diagonal normalization, branch-exchange reality,
  positivity, and the \(W=-i\log Z\) branch consequences.  The hydrodynamic
  chapter now recalls this algebra instead of reproving it as a separate
  proposition.
- The two demoted Chapter 3 derivations remain central convention checks; they
  now sit at the level of the finite trace calculus from which the continuum
  regulated identities inherit their sign and support conventions.

Verification run before checkpoint:

- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- stale-label search for the three removed proposition labels
- `git diff --check`
- `tools/build_monograph.sh` (clean build and log scan; resulting PDF has
  2577 pages)
