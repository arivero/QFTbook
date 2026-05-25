# Issue 418: OPE Convergence Uses the Chapter 4 Radial Reconstruction Hypothesis

Date: 2026-05-24.

Issue:

- GitHub #418 flagged that the OPE convergence theorem repeated the
  reflection positivity, radial Hamiltonian, discreteness, finite
  multiplicity, and local-completeness assumptions from the radial
  quantization chapter without making the dependence on the Chapter 4
  hypothesis explicit enough.

Fix:

- Retitled `def:radial-ope-convergence-hypotheses` as "Radial OPE inputs from
  radial reconstruction".
- Added an explicit sentence that the enumerated items are not an independent
  assumption package, but the clauses of
  `hyp:radial-reconstruction-data` used in the Euclidean convergence proof.
- Updated the Chapter 9 dossier to record this dependency and prevent future
  drift into duplicated assumptions.

Verification:

- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean.
- `pdfinfo monograph/tex/main.pdf` reports 781 pages.
