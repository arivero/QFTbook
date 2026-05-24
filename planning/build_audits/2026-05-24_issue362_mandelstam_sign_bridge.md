# 2026-05-24 Issue #362 Mandelstam Sign Bridge

GitHub issue #362 flagged a possible sign clash between the Euclidean
momentum-subtraction variables and Lorentzian Mandelstam variables.

Resolution:

- The manuscript uses mostly-plus Lorentzian signature in the scattering
  chapters, so the physical Mandelstam variable is
  \(s_{\rm L}=-(p_1+p_2)^2_{\rm L}\).
- The Euclidean subtraction chapter defines
  \(s_{\rm E}=-(k_1+k_2)^2_{\rm E}\).
- Under the Wick continuation \(k_i=(\ii p_i^0,\vec p_i)\),
  \((k_i+k_j)^2_{\rm E}=(p_i+p_j)^2_{\rm L}\), hence
  \(s_{\rm E}=s_{\rm L}\).
- The apparent sign flip is only between \(s_{\rm E}\) and the bare mostly-plus
  Lorentzian quadratic form \((p_1+p_2)^2_{\rm L}\), not between the Euclidean
  subtraction variable and the Mandelstam variable used in the scattering
  chapters.

Changes made:

- Added the explicit Wick-rotation formula in the 1PI RG chapter immediately
  after the symmetric Euclidean subtraction-point identity.
- Updated the 1PI RG chapter dossier with the same convention bridge.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
