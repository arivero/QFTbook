# OS Polynomial Tube Boundary-Value Dequotation Pass

Date: 2026-05-30

Scope:
- Volume IV, Chapter 2, `qthm:polynomial-tube-bounds-boundary-values`.
- Issue context: foundational quoted-theorem proof debt in #695.

Edits:
- Replaced the `quotedtheorem` wrapper by a local `theorem`.
- Added a proof of the tempered boundary-value mechanism:
  finite-order Schwartz dual bounds, Cauchy estimates in proper subtubes,
  radial Cauchy convergence in `S'`, independence of the approach cone by
  convexity, and uniqueness of the boundary distribution.
- Kept the existing Fourier--Laplace cone-support lemma and made it the
  final step in the theorem proof when the holomorphic tube function comes
  from a distribution supported in the dual cone.
- Updated the OS reconstruction chapter dossier so the polynomial-growth
  boundary-value theorem is no longer listed as an imported black box.

Verification:
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reports 2624 pages.
