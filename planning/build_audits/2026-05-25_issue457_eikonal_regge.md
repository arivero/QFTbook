# 2026-05-25 Issue #457: Eikonal and Regge High-Energy Scattering

## Scope

GitHub issue #457 flagged that Volume II, Chapter 7 derived the
Froissart--Martin bound but did not include the standard small-angle
high-energy physics: the eikonal exponentiation of ladder exchange and the
Regge-pole organization of partial waves.

## Manuscript Changes

- Added `Eikonal Small-Angle Scattering and Regge Singularities` to
  Volume II, Chapter 7.
- Derived the impact-parameter representation from the ordered partial-wave
  expansion in the limit \(s\to\infty\), fixed \(q=\sqrt{-t}\), and
  \(b=(\ell+\frac12)/p\) fixed.
- Recorded the impact-parameter unitarity identities for
  \(\Gamma=1-S\):
  \(2\operatorname{Re}\Gamma=|\Gamma|^2+1-|S|^2\),
  \(\sigma_{\rm tot}=2\int d^2b\,\operatorname{Re}\Gamma\),
  \(\sigma_{\rm el}=\int d^2b\,|\Gamma|^2\), and
  \(\sigma_{\rm inel}=\int d^2b(1-|S|^2)\).
- Defined the eikonal phase \(S=e^{i\chi}\), the condition
  \(\operatorname{Im}\chi\ge0\), and the Born transform
  \[
    \chi_1(s,b)=\frac1{2s}\int\frac{d^2Q}{(2\pi)^2}
    e^{-iQ\cdot b}\mathcal M_{\rm Born}(s,-Q^2).
  \]
- Proved leading eikonal exponentiation of ladder and crossed-ladder graphs
  under explicit eikonal-propagator and integrable-remainder hypotheses,
  using the Wilson-line/eikonal-propagator derivation rather than a slogan.
- Added a Sommerfeld--Watson representation for signature-projected
  \(t\)-channel partial waves, checked the integer-spin residues, and derived
  the fixed-\(t\) Regge-pole asymptotic
  \[
    \mathcal M_\tau^{\rm pole}(s,t)
    =
    \eta_\tau(\alpha(t))\mathfrak r_\tau(t)
    (s/s_0(t))^{\alpha(t)}(1+O(s^{-1})).
  \]
- Explained recovery of ordinary exchanged-particle poles when
  \(\alpha(M_n^2)=n\) with the correct signature.
- Added a careful Pomeron paragraph: an uncompensated simple pole with
  \(\alpha_P(0)>1\) is incompatible with the complete massive
  Froissart--Martin asymptotics, while eikonal saturation of a phase
  \(s^\Delta e^{-\mu b}\) gives \(R(s)\sim(\Delta/\mu)\log s\).
- Added two TikZ figures: one for eikonal impact-parameter exponentiation and
  one for the complex-\(J\) Regge contour.
- Updated the chapter dossier with the new symbol inventory, claim ledger,
  figure requirements, and issue certification note.

## Verification

Completed after the edit:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 825 pages.
- Rendered affected PDF pages 329--336 with `pdftoppm`; inspected pages 331
  and 334 containing the new eikonal and Regge figures.  Both figures are
  legible, correctly placed, and captioned.
