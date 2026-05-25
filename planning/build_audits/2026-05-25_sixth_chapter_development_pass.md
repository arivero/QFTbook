# Sixth-Chapter Development Pass Build Audit

Date: 2026-05-25.

Scope:
- Added sixth compiled chapters for Volumes VI-XII: integrable RG flows and
  perturbed two-dimensional CFT, four-dimensional N=1 gauge dynamics,
  topological sigma models, anomaly inflow and invertible field theories,
  Schwinger-Keldysh hydrodynamic effective actions, Monte Carlo methods and
  sign problems, and background gauge fields and index theory.
- Updated the corresponding volume manifests, master architecture,
  systematic development matrix, and chapter dossiers.
- Widened the chapter-number box in the table of contents so three-digit
  chapter numbers do not produce overfull boxes.

Verification:
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed. The final log scan reported no
  unresolved references, hyperref warnings, or overfull boxes.
- `pdfinfo monograph/tex/main.pdf`: final PDF has 1024 pages.

Rendered spot-check pages:
- `/tmp/qft_ch67_integrable_rg_title-0906.png`: Chapter 67, printed page 875.
- `/tmp/qft_ch73_n1_dynamics_title-0929.png`: Chapter 73, printed page 898.
- `/tmp/qft_ch79_top_sigma_title-0948.png`: Chapter 79, printed page 917.
- `/tmp/qft_ch85_inflow_title-0965.png`: Chapter 85, printed page 934.
- `/tmp/qft_ch91_sk_hydro_title-0984.png`: Chapter 91, printed page 953.
- `/tmp/qft_ch97_monte_carlo_title-1005.png`: Chapter 97, printed page 974.
- `/tmp/qft_ch103_index_title-1022.png`: Chapter 103, printed page 991.

Notes:
- The first build exposed PDF bookmark warnings from math in headings and TOC
  overfulls after the manuscript reached three-digit chapter numbers.  The
  headings were converted to plain text and the TOC chapter-number width was
  increased in the preamble.
- The chapter openings render cleanly after the final build.
