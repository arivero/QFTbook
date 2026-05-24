# 2026-05-24 Issue #354 Symmetric Point Identity Audit

## Issue

GitHub issue #354 flagged that the symmetric Euclidean four-point subtraction
point used
\[
  k_i^2=\mu^2,\qquad s=t=u=-\frac43\mu^2
\]
without displaying the kinematic identity fixing the common channel value.

## Edits

- Replaced the terse identity statement by an expanded derivation:
  \[
    s+t+u
    =
    -\sum_{j=2}^4(k_1+k_j)^2
    =
    -\left(
      3k_1^2+\sum_{j=2}^4k_j^2
      +2k_1\cdot\sum_{j=2}^4k_j
    \right)
    =
    -\sum_{i=1}^4k_i^2 .
  \]
- Stated explicitly that \(k_1+k_2+k_3+k_4=0\) is the step used in the last
  equality.
- Stated explicitly that \(k_i^2=\mu^2\) gives \(s+t+u=-4\mu^2\), and imposing
  the symmetric subtraction condition \(s=t=u\) gives
  \(s=t=u=-4\mu^2/3\).
- Updated the chapter dossier to record the kinematic derivation as a claim of
  the 1PI renormalization-group chapter.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 757 pages.
