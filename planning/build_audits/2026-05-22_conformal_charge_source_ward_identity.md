# Conformal Charge Source Ward Identity Audit

Date: 2026-05-22

This pass propagates the source-functional Ward-contact conventions from the
opening fixed-point chapter into the conformal charge chapter.  The purpose is
to make conformal charges act through local source-defined current Ward
identities before the following chapter derives primary transformations.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_iii/chapter05_conformal_charges_and_ward_identities.tex`.
- Replaced the local Ward identity section with "Source-Derived Local Ward
  Identities."
- Defined \(X=\mathcal O_1(x_1)\cdots\mathcal O_n(x_n)\) for noncoincident
  insertions and gave the local translation Ward identity in the same contact
  convention as the opening CFT chapter.
- Recast the trace Ward identity as the local derivative of
  \(\mathcal A_\sigma[X]\).
- Combined translation and trace identities into the local conformal-current
  Ward identity for \(J^\mu_\epsilon=T^\mu{}_\nu\epsilon^\nu\).
- Removed an unnecessary negative framing in the Lorentzian commutator
  paragraph.

## Planning Updates

- Added a Volume III chapter dossier for conformal charges and Ward
  identities.
- Updated the master architecture and dependency map so the next CFT target is
  the link from source-derived current Ward identities to primary finite
  transformations.

## Verification

- `git diff --check` passed.
- Strict phrase scan on the edited manuscript and planning files found no
  manuscript-policy issue; remaining hits were labels or planning-only
  guardrail text.
- `tools/build_monograph.sh` passed; the strict text audit, LaTeX build, and
  log scan were clean after latexmk resolved the expected cross-reference
  rerun.
- Rendered and inspected PDF pages 481--483, corresponding to printed pages
  463--465.  The revised local Ward section and the transition into the
  primary-operator chapter typeset cleanly.
