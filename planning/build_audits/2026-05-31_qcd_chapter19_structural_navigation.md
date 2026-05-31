# 2026-05-31 QCD Chapter 19 Structural Navigation Pass

Scope: GitHub issue #706, `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`.

What changed:
- Added substance-aligned subsections to the long background-field,
  large-\(N_c\), spectroscopy, integrated-PDF/DIS, and exclusive-pion blocks.
- Added labels for the new anchors so later issue work can cite precise
  locations rather than a several-thousand-line QCD chapter.
- Left physics formulae, normalization conventions, determinant coefficients,
  splitting kernels, Roy/Roy--Steiner formulae, and form-factor formulae
  unchanged.

Structural audit:
- A source-line scan of `chapter19` after the pass shows every section longer
  than 500 lines now has at least three `\subsection` anchors.
- The largest spectroscopy block is now divided into finite-volume spectral
  sources, elastic reconstruction, pole coordinates, effective-range charts,
  Roy coordinates, light-meson poles, unequal-mass/baryon-meson channels,
  quarkonium/baryon/hybrid source charts, and current-matrix-element data.

Verification:
- `git diff --check` clean.
- `python3 tools/audit_unnumbered_display_labels.py` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `python3 tools/audit_theorem_form.py` clean.
- `tools/build_monograph.sh` clean, producing
  `monograph/tex/main.pdf` at 2765 pages with a clean final log scan.
