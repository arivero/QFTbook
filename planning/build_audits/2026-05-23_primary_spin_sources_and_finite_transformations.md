# Primary Spin Sources And Finite Transformations Audit

Date: 2026-05-23

This pass connects the source-derived conformal current Ward identity in the
charge chapter to the primary-operator transformation chapter.  The purpose is
to make spin contact terms and finite transformation laws part of the same
source convention as the earlier CFT Ward identities.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_iii/chapter06_primary_operators_and_finite_transformations.tex`.
- Added "Spin Sources and Contact Terms."
- Introduced spin sources \(\eta^a\in V_\rho^\vee\) and their conformal
  source transformation.
- Defined the primary contact operator \(\mathcal D_\epsilon\mathcal O_a\).
- Added the spinful local conformal-current Ward identity.
- Identified the small-sphere charge action with the contact operator.
- Added cocycle identities for \(\Omega_f\) and \(R_f\).
- Clarified tensor determinant powers in finite primary transformations.
- Clarified that inversion for spinning primaries requires a specified
  extension of the spin action beyond \(SO(D)\).

## Planning Updates

- Added a Volume III chapter dossier for primary operators and finite
  conformal transformations.
- Updated the master architecture and dependency map so the next CFT target is
  radial-positivity derivation of unitarity bounds and short multiplets.

## Verification

- `git diff --check` passed.
- Strict phrase scan on the edited manuscript found no manuscript-policy hits.
- `tools/build_monograph.sh` passed; the strict text audit, LaTeX build, and
  log scan were clean after replacing unsupported `\mathscr` notation with
  `\mathcal D`.
- Rendered and inspected PDF pages 484--486, corresponding to printed pages
  466--468.  The new spin-source section and finite-transformation revisions
  typeset cleanly.
