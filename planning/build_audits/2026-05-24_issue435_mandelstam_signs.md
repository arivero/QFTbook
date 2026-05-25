# Issue 435: Mostly-Plus Mandelstam Signs

Date: 2026-05-24.

Issue:

- GitHub #435 flagged that the scattering/analyticity chapters used
  Mandelstam variables without a part-wide declaration of the mostly-plus sign
  convention and the physical-region signs of \(t\) and \(u\).

Fix:

- Added Definition `def:mostly-plus-mandelstam-variables` at the opening of
  the scattering-kernel chapter:
  \(s=-(p_1+p_2)^2\),
  \(t=-(p_1-p_3)^2\),
  \(u=-(p_1-p_4)^2\), and
  \(s+t+u=\sum_i m_i^2\).
- Displayed the equal-mass center-of-mass formulas
  \(s=E_{\rm cm}^2\),
  \(t=-2|\vec p_*|^2(1-\cos\theta)\),
  \(u=-2|\vec p_*|^2(1+\cos\theta)\), so the physical \(s\)-channel has
  \(t,u\le0\).
- Stated explicitly that positive real \(t\) or \(u\) in fixed-\(t\),
  crossing, and Lehmann-ellipse discussions is a crossed-channel timelike
  invariant, not a physical \(s\)-channel scattering angle.
- Added cross-references in the bound-state, resonance, composite
  Bethe--Salpeter, analyticity, and high-energy-bound chapters and updated
  the corresponding dossiers.

Verification:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 786 pages.
