# 253b Analyticity, Crossing, and Landau Source Pass

## Source Block

- Handwritten source: `references/253b lecture notes 2023.pdf`, pp. 34--40.
- Operational transcription: `transcription/tex/253b/scattering_rg_qcd.tex`,
  analyticity/crossing/Landau section.
- Student transcription comparison: `references/253b transcribed lecture notes.tex`,
  corresponding section, used only as a cautionary comparison.

## Manuscript Changes

- Certified `volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
  against the source block.
- Corrected the real \((s,t)\)-plane crossing-region figure so that the
  \(s\)-channel wedge lies between \(t=0\) and \(u=0\), the \(t\)-channel wedge
  lies between \(s=0\) and \(u=0\), and the \(u\)-channel region is the
  lower-left physical quadrant.
- Added the source partial-wave unitarity formula on the physical
  \(s\)-channel cut, including the definition of \(S_\ell(s)\), the angular
  relation \(\cos\theta=1+2t/(s-4m^2)\), the bound \(|S_\ell(s)|\le1\), and the
  elastic equality below \(M_{\mathrm{inel}}\).
- Strengthened the anomalous-threshold discussion as a first-sheet
  contour-pinch mechanism with positive Feynman parameters, separate from the
  physical-region notion.
- Expanded the triangle example to include the equal-internal-mass
  \(M_1,M_2<\sqrt2m\) versus \(M_1,M_2>\sqrt2m\) criterion and added a
  two-panel vector-closure figure showing origin-outside-convex-hull and
  origin-inside-convex-hull cases.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- Rendered and visually inspected affected PDF pages 192--201 at 170 dpi,
  including the first-sheet \(s\)-plane figure, crossing-region figure,
  unitarity formula page, pinch figure, Landau-equation page, bubble-threshold
  figure, and triangle/vector-closure figures.

## Coverage Result

The 253b pp. 34--40 block is now marked certified in the no-skip coverage
register.  Remaining analytic consequences, including Lehmann ellipses,
dispersion relations, and Froissart--Martin bounds, remain assigned to the
following source block pp. 41--55.
