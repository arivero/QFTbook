# Distributional Edge-Of-The-Wedge Dequotation Pass

Date: 2026-05-30

Scope:
- Volume I, Chapter 11, `thm:distributional-edge-of-the-wedge`.
- Issue context: quoted-theorem proof-debt audit, especially the foundational
  boundary-value infrastructure in #695.

Edits:
- Replaced the `quotedtheorem` wrapper by a local `theorem`.
- Moved the existing analytic mechanism into a proof environment, so the
  chapter no longer presents the distributional edge-of-the-wedge statement as
  a black-box imported theorem.
- Kept the proof boundary explicit: the theorem uses analytic infrastructure
  from several complex variables and distribution theory, while the QFT-specific
  work remains the verification of spectral tube growth and equality of
  distributional boundary values from microcausality.
- Updated the Volume I Chapter 11 dossier to record the new theorem/proof
  status.

Verification:
- `git diff --check`.
- `python3 tools/audit_theorem_form.py`.
- `python3 tools/audit_unnumbered_display_labels.py`.
- `tools/audit_negative_scope_prose.py`.
- `tools/audit_monograph_text.sh`.
- `tools/audit_chapter_dossiers.sh`.
- `tools/build_monograph.sh`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2622 pages.
