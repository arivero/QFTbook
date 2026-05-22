# 253b pp. 41--55 Lehmann/Dispersion/Froissart Source Pass

Date: 2026-05-22

## Scope

- Source block: handwritten 253b pp. 41--55.
- Monograph target:
  `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`.
- Control dossier:
  `planning/chapter_dossiers/volume_ii/chapter07_partial_waves_dispersion_froissart.md`.

## Source Items Checked

- Angular variable \(x=1+2t/(s-4m^2)\), physical interval \([-1,1]\), and
  crossed-channel cuts beginning at \(x=\pm (s+4m^2)/(s-4m^2)\).
- Possible crossed-channel bound-state poles and the elementary
  \(t_0=\min\{4m^2,M_B^2\}\) nearest-singularity convention.
- Cauchy representation on the angular contour and the
  \(P_\ell(x)Q_\ell(z)\) kernel expansion.
- Both representations of \(Q_\ell\): the \([-1,1]\) integral and the
  \(\zeta\)-integral used for the large-\(\ell\) estimate.
- Lehmann ellipses as level sets of \(z+\sqrt{z^2-1}\), with foci at
  \(\pm1\), and convergence of the partial-wave expansion for unphysical
  \(x\) inside the ellipse.
- Identical-scalar partial-wave normalization, positive weights
  \(1-\operatorname{Re}S_\ell\), elastic/inelastic/total cross sections, and
  the optical theorem in the chapter normalization.
- Box-profile comparison, Legendre lower bound for \(x>1\), and the
  Froissart-Martin logarithmic bound at \(0<t<t_0\).
- Causal motivation for polynomial boundedness in a retarded one-dimensional
  kernel.
- Fixed-\(t\) \(s\)-plane contour, subtraction points, right and left cuts, and
  the \(N\)-subtracted dispersion relation.
- Explicit crossed-channel \(u'\)-integral form of the dispersion relation.
- Elastic unitarity integral used in the subtraction-count argument, including
  the \(x\)-to-\(t\) change of variables.
- Two-subtraction conclusion, positivity of \(t\)-derivatives of the absorptive
  part, \(D\)-dimensional logarithmic scaling, and the scope caveats for
  massless particles and gravity.

## Fixes Applied

- Added a conditional-hypothesis paragraph so the chapter does not overstate
  what current axiomatic frameworks prove.
- Added the elementary \(t_0\) formula for a crossed bound-state pole.
- Added the missing \(\zeta\)-integral representation of \(Q_\ell\).
- Added the explicit \(s'\)- and crossed \(u'\)-channel form of the
  subtracted dispersion relation.
- Expanded the subtraction-count argument to display the positive elastic
  unitarity integral and to distinguish fixed-\(t\) from fixed-angle
  uniformity.
- Added an effective-radius schematic for
  \(\sigma_{\rm tot}\asymp R_{\rm eff}^{D-2}\) and
  \(R_{\rm eff}=O(\log s)\) under the massive hypotheses.
- Updated the no-skip source inventory and chapter dossier.

## Verification Results

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/build_monograph.sh`: clean; produced
  `monograph/tex/main.pdf`.
- Rendered and inspected PDF pages 185--195 of the chapter.  The opening
  angular-analyticity figure, the \(Q_\ell\) representation, the crossed
  dispersion relation, the elastic unitarity chain, and the effective-radius
  figure render without overlap or truncation.
