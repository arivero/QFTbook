# Issue 410: Radial Conformal-Algebra Sign

Date: 2026-05-24.

Issue:

- GitHub #410 flagged that the radial unitarity-bounds chapter uses
  \[
    [K_\mu,P_\nu]=2\delta_{\mu\nu}D_{\rm rad}-2J_{\nu\mu},
  \]
  while the conformal-Killing-vector chapter writes the Hermitian charge
  relation
  \[
    [P^{\rm L}_\mu,K^{\rm L}_\nu]
    =
    2\ii(\delta_{\mu\nu}D_{\rm L}-J^{\rm L}_{\mu\nu}).
  \]
  A slogan that radial notation is obtained by simply deleting the visible
  factor of \(\ii\) gives the wrong sign for descendant positivity.

Fix:

- Added the explicit complexified real-form map in the radial-quantization
  chapter:
  \[
    D_{\rm rad}=-\ii D_{\rm L},\qquad
    J_{\rm rad}=-\ii J_{\rm L},\qquad
    P_{\rm rad}=\ii P_{\rm L},\qquad
    K_{\rm rad}=-\ii K_{\rm L}.
  \]
- Derived
  \[
    [P^{\rm rad}_\mu,K^{\rm rad}_\nu]
    =
    -2(\delta_{\mu\nu}D_{\rm rad}-J^{\rm rad}_{\mu\nu}),
    \qquad
    [K^{\rm rad}_\mu,P^{\rm rad}_\nu]
    =
    2\delta_{\mu\nu}D_{\rm rad}-2J^{\rm rad}_{\nu\mu}.
  \]
- Cross-referenced this derivation from the unitarity-bounds chapter.
- Updated the radial-quantization and unitarity-bounds dossiers.

Verification:

- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean.
- `pdfinfo monograph/tex/main.pdf` reports 780 pages.
