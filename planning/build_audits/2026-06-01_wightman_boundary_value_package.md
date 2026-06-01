# Wightman Boundary-Value Package Pass

Date: 2026-06-01

Scope:
- `monograph/tex/volumes/volume_iv/chapter01_wightman_fields_and_reconstruction.tex`
- `planning/chapter_dossiers/volume_iv/chapter01_wightman_fields_and_reconstruction.md`

Purpose:
- Tighten the foundational Wightman reconstruction lane by replacing the
  compressed tube-analyticity paragraph with a precise proposition and proof.
- Address the cross-reference/proof-boundary concern in the comprehensive
  audit: the chapter now proves the QFT-specific ingredients for Wightman
  boundary values in place and points only the pure analytic
  edge-of-the-wedge step to the detailed theorem already stated in the
  Lorentzian Green-functions chapter.

Mathematical content:
- The new proposition fixes the Fourier convention in relative variables,
  derives the support inclusion
  `supp \widetilde w_n \subset \overline V_+^{n-1}` from the translation
  spectral condition, constructs the Fourier--Laplace tube function for
  `z=\xi-i\eta`, proves distributional boundary convergence, records the
  polynomial normal-growth estimate needed by the distributional
  edge-of-the-wedge theorem, explains the complex Lorentz extension, and
  verifies that microcausality gives equality of permuted boundary values on
  Jost real edges.

Verification commands:
- `git diff --check` completed cleanly.
- `python3 tools/audit_theorem_form.py` reported
  `Theorem-form audit clean.`
- `python3 tools/audit_unnumbered_display_labels.py` reported
  `No labels inside unnumbered display math.`
- `tools/audit_monograph_text.sh` reported
  `Strict monograph text audit clean.`
- `tools/audit_negative_scope_prose.py` reported
  `Negative-scope prose audit clean.`
- `tools/audit_chapter_dossiers.sh` reported
  `Chapter dossier metadata audit clean.`
- `tools/build_monograph.sh` completed with clean TeX log scan.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported
  `Pages:           2796`.
