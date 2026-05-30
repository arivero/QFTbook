# Shale--Stinespring Diagonal Criterion Dequotation Pass

Date: 2026-05-30

Scope:
- Volume XII, Chapter 8, the diagonal Shale--Stinespring block.
- Issue context: quoted-theorem proof-debt inventory and the standing
  distinction between finite-volume Fock equivalence and infinite-volume
  particle-density diagnostics.

Edits:
- Replaced the `quotedtheorem` wrapper by a local theorem for a countable
  mode basis.
- Added the proof from two-mode squeezed vacua: block CCR preservation,
  squeezed-vacuum normalization, von Neumann incomplete tensor-product
  criterion, and equivalence of \(\sum|\gamma_n|^2\) with
  \(\sum|\beta_n|^2\).
- Corrected the continuum wording.  On a noncompact homogeneous slice,
  \(\int |\beta_{\mathbf k}|^2\,d\mathbf k\) is a finite-density or
  box-normalized diagnostic; exact continuum-diagonal multiplication is not
  Hilbert--Schmidt on the global \(L^2\) one-particle space unless it vanishes
  almost everywhere.
- Updated the chapter dossier accordingly.

Verification:
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reports 2625 pages.
