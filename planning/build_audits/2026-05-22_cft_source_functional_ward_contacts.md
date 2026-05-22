# CFT Source Functional Ward Contacts Audit

Date: 2026-05-22

This pass carries the source-dependent observable framework into the opening
CFT/fixed-point chapter.  The purpose is to make CFT correlators and Ward
identities source-defined distributions before later chapters derive
conformal charges and primary transformations.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`.
- Added "Source Functionals and Ward-Identity Contact Terms."
- Defined the Euclidean fixed-point source functional \(W_\ast[g,\eta]\).
- Fixed stress-tensor and local-operator derivative conventions with respect
  to \(g_{\mu\nu}\) and \(\eta^A\).
- Related contact-term freedom to the source-coordinate freedom developed in
  the renormalized-operators chapter.
- Derived the source diffeomorphism Ward identity and gave the smeared
  translation Ward identity for scalar insertions.
- Added the Weyl source convention for scalar primaries and the corresponding
  smeared trace Ward identity with local anomaly/contact term.

## Planning Updates

- Added a Volume III chapter dossier for fixed points and conformal data.
- Updated the master architecture and dependency map so the next target is
  using these Ward-contact conventions in the conformal-current, charge, and
  primary-transformation chapters.

## Verification

- `git diff --check` passed.
- Strict phrase scan on the edited manuscript and planning files found no
  manuscript-policy issue; the remaining hits were `stress-lorentz` in a
  label and planning-only guardrail text.
- `tools/build_monograph.sh` passed; the strict text audit, LaTeX build, and
  log scan were clean.
- Rendered and inspected PDF pages 456--458, corresponding to printed pages
  438--440.  The new source-functional section and the following Ising page
  typeset cleanly, including the source derivative conventions, the
  diffeomorphism Ward identity, the smeared translation Ward identity, and the
  smeared trace Ward identity.
