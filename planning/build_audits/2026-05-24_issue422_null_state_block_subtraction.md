# Issue 422: Null-State Subtraction in Conformal Blocks

Date: 2026-05-24.

Issue:

- GitHub #422 flagged that the conformal-block construction referred to a
  reduced basis when null descendants are present, without connecting the nulls
  to Chapter 7 shortening equations or explaining that subtraction is
  level-by-level.

Fix:

- Labeled the Chapter 7 discussion as
  `sec:short-multiplets-operator-equations`.
- Added a bridge paragraph before the local OPE-block existence theorem:
  saturated unitarity bounds create singular null descendants at definite
  levels, such as \(\widehat P^2|\phi\rangle\) at level \(2\), divergence
  nulls at level \(1\), and gamma-trace nulls at level \(1\).
- Explained that all translation descendants of a singular null are null at
  higher levels, so the level-\(n\) block construction uses the raw descendant
  space modulo the span of null descendants at total level \(n\).
- Rewrote the proof to define the raw level space
  \(W_n\simeq\operatorname{Sym}^n(\mathbb C^D)\otimes V_{\Delta,\ell}\), the
  null radical \(\mathcal N_n\), the quotient \(Q_n=W_n/\mathcal N_n\), and the
  quotient Gram matrix before inversion.
- Updated the Chapter 7 and Chapter 9 dossiers.

Verification:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 783 pages.
