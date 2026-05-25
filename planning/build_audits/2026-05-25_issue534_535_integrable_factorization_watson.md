# Build Audit: Issues 534 and 535 Integrable Factorization and Watson Exchange

Date: 2026-05-25

## Scope

Development pass on
`monograph/tex/volumes/volume_vi/chapter01_factorized_scattering_and_integrability.tex`
and
`monograph/tex/volumes/volume_vi/chapter04_form_factor_bootstrap_local_operators.tex`,
addressing the higher-spin factorization and Watson-exchange rigor gaps.

## Mathematical Changes

- Added a definition of a separating higher-spin charge family as injectivity
  of a species-resolved moment map on \(N\)-particle rapidity multisets,
  outside coincident-rapidity, threshold, and bound-state singular loci.
- Recorded a concrete sufficient condition for separation using
  species-resolved power sums and Newton identities.
- Rewrote the higher-spin factorization proposition as a support theorem for
  scattering distribution kernels, with the relevant topology stated through
  compact wave-packet smearing and distributional boundary values.
- Replaced the vague continuity argument by the distribution support fact
  that \(fT=0\) with \(f\neq0\) on an open set forces \(T\) to vanish there.
- Removed the phrase that locality directly gives Watson equations.  Chapter
  1 now states Watson exchange as a rapidity-boundary-value statement about
  ordered scattering bases.
- Expanded the Chapter 4 Watson proof with the two adjacent rapidity chambers,
  the two \(i0\)-boundary values, the ordered-state exchange relation, and
  the final pairing with the local-operator covector.
- Updated the Volume VI Chapter 1 and Chapter 4 dossiers.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` was rebuilt
  without log-scan failures.
- `pdfinfo monograph/tex/main.pdf` reports 1271 pages.
