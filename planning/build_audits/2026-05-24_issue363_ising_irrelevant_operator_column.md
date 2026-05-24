# 2026-05-24 Issue #363 Ising Irrelevant-Operator Column

GitHub issue #363 flagged that the low-lying scalar-dimension comparison table
used the header \(\Delta_{\phi^4}\) for a column whose lower-dimensional entries
are not literally powers of a spin field.

Changes made:

- Renamed the table's third column to \(\Delta_{O_{\rm irr}}\).
- Defined \(O_{\rm irr}\) as the leading nonredundant
  \(\mathbb Z_2\)-even scalar irrelevant deformation after removing the identity
  and the energy operator.
- Stated that \(\phi^4\) is the representative only in the \(4-\epsilon\)
  perturbative Landau chart.
- Reworded the \(d=3\) text so the third column is identified with
  \(\varepsilon'\), not with an unrenormalized power.
- Reworded the \(d=2\) text so the dimension-\(4\) entry is explicitly
  \(T\bar T\), not an unrenormalized \(\sigma^4\) operator.
- Updated the Wilson--Fisher chapter dossier accordingly.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
