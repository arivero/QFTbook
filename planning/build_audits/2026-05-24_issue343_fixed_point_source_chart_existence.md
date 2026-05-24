# 2026-05-24 Issue #343 Fixed-Point Source Chart Existence Audit

## Issue

GitHub issue #343 flagged that Volume V, Chapter 1 differentiated the
fixed-point source functional \(W_\ast[g,J]\) without first stating a precise
existence condition for that functional.  The concern was convergence of the
source-coupled construction, the role of a regulator, and regulator
independence of the continuum limit.

## Edits

- Added `hyp:cft-fixed-point-source-chart-existence` to the fixed-points and
  conformal-data chapter.
- The hypothesis defines the source domain as an open neighborhood of
  \((\delta,0)\) in the Frechet space of smooth compactly supported source
  data.
- It requires all Gateaux derivatives of \(W_\ast[g,J]\) to exist as
  distributions and to be continuous in the test-function topology.
- In a regulator presentation, it requires convergence of the renormalized
  derivatives of \(-\log Z_\Lambda[g,J]+P_\Lambda[g,J]\) in \(\mathcal D'\).
- It states that regulator or subtraction changes are tracked by local source
  counterterms, hence by contact-term changes, not by separated-point
  correlator changes.
- It states that diffeomorphism and Weyl Ward identities, including anomalies,
  are additional properties of the source chart rather than consequences of
  flat separated correlators alone.
- Updated the chapter dossier to record the issue #343 pass.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 752 pages.
