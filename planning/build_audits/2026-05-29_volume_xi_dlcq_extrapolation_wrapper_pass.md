# Volume XI DLCQ/extrapolation wrapper pass

Date: 2026-05-29.

This pass continued the issue #691 proof-substance audit in the Hamiltonian
truncation and DLCQ benchmark chapter.  The focus was finite-regulator algebra
that is useful for scripts and diagnostics but should not be presented as
theorem-family content.

Changes made:

- The finite principal-value matrix positivity statement was demoted from
  proposition/proof form to a worked paragraph.  The quadratic form remains
  displayed and labelled.  The text now states that this is positivity of the
  displayed finite matrix; positivity and self-adjointness of the continuum
  principal-value operator require a separate continuum-domain construction.
- The integer-power extrapolation weight statement was demoted from
  proposition/proof form to a worked paragraph.  The Vandermonde equations and
  remainder bound remain explicit.  The text now emphasizes that the exact
  finite algebra cancels declared powers, while the QFT problem must supply
  evidence that those powers are the correct cutoff expansion.
- The later large-\(K\) diagnostic now points to the finite matrix through the
  labelled quadratic-form equation instead of citing a proposition wrapper.
- The chapter dossier now records these as regulator-level identities and
  diagnostics rather than theorem-level continuum claims.
- `tools/audit_theorem_form.py` now rejects reintroduction of the two demoted
  titles as theorem-family wrappers.

Manual review notes:

- The finite quadratic form remains central because the companion DLCQ script
  checks exactly this algebraic identity at finite \(K\).
- The extrapolation calculation remains central because it makes the
  finite-data ambiguity and remainder-amplification logic explicit for
  numerical readers.  Its theorem status is deliberately withheld from the
  algebraic cancellation step and assigned only to the separate controlled
  cutoff-expansion hypothesis.

Verification run before checkpoint:

- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh` (clean build and log scan; resulting PDF has
  2577 pages)
