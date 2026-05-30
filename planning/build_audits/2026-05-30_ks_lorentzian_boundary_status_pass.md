# K-S Lorentzian Boundary Status Pass

Date: 2026-05-30

Scope:
- Volume IV, Chapter 6, the former `thm:ks-lorentzian-boundary` block.
- Issue context: foundational quoted-theorem proof debt in #695 and the
  standing rule that theorem-like statements must not hide their substance in
  undeveloped hypotheses.

Edits:
- Replaced the `quotedtheorem` wrapper by
  `Construction~\ref{cons:ks-lorentzian-boundary}`.
- Listed the actual Lorentzian-boundary construction data: admissible
  approach metrics, reflection-positive Hilbert completions, amplitude
  boundary limits, approach independence, sewing, reflection/unitarity, and
  insertion limits.
- Added the algebraic consequence once the analytic boundary data exist:
  reflection plus sewing gives unitarity, and exchange of spacelike-separated
  insertion germs in admissible configuration space gives graded
  commutativity.
- Updated the chapter dossier so the K-S boundary passage is no longer
  recorded as an imported theorem.

Verification:
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reports 2624 pages.
