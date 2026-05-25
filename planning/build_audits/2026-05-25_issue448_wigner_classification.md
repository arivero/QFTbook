# Issue #448 Wigner Classification Table

## Scope

- GitHub issue #448 requested a single location in Volume I where the full
  four-dimensional Wigner orbit classification is visible, rather than only
  the massive-spin and massless-helicity special cases used later.

## Resolution

- Added Table~\ref{tab:wigner-classification-four-dimensional} to
  Volume I Chapter 2, immediately after the first one-particle representation
  discussion.
- The table lists:
  - the zero-momentum vacuum orbit;
  - the massive positive-energy tower \(j=0,\frac12,1,\frac32,\ldots\);
  - massless finite-helicity representations \(h\in\frac12\mathbb Z\);
  - massless continuous-spin representations with nonzero little-group
    translation orbit \(N_1^2+N_2^2=\rho^2>0\);
  - spacelike/tachyonic orbits with little group \(SO^+(1,2)\).
- The text distinguishes:
  - exclusion by the spectrum condition for spacelike/tachyonic orbits;
  - representation-theoretic admissibility but point-localization obstruction
    for continuous-spin sectors;
  - the isolated-shell hypothesis used for stable massive particles.
- Added cross-references from the massive-spin and massless-helicity chapters
  back to the classification table.
- Updated the Volume I Chapter 2 dossier.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 789 pages.

The first build exposed an incorrect Maxwell chapter label and an overfull
classification table; both were corrected before this audit entry.
