# Volume XI Phi-Four-Three Local Coordinates Audit

## Scope

This pass deepens the \(\Phi^4_3\) part of Volume XI, Chapter 2.  The
previous text correctly stated that Wick ordering leaves a logarithmic
two-loop local two-point coordinate, but it did not derive the coefficient
or make the normal-ordered coordinate chart explicit.

## Edits

- Updated
  `monograph/tex/volumes/volume_xi/chapter02_constructive_scalar_models_os_data.tex`.
- Introduced normal-ordered \(\Phi^4_3\) coordinates
  \(\lambda:\phi^4:+\alpha_\varepsilon:\phi^2:+\beta_\varepsilon\) and
  derived their conversion to the un-Wick-ordered coordinates
  \(a_\varepsilon,b_\varepsilon\).
- Added the universal short-distance sunset estimate
  \(J_\varepsilon(R)=\int_{|x|\le R}C_\varepsilon(x)^3\,d^3x
  =(16\pi^2)^{-1}\log(1/\varepsilon)+O(1)\).
- Derived the two-loop local mass coordinate in the chapter's normalization:
  the Wick-product coefficient is \(\binom{4}{3}^2 3!=96\), the two external
  pairings give the local two-point coefficient \(96\lambda^2J_\varepsilon\),
  and the \(\alpha_\varepsilon:\phi^2:\) insertion contributes
  \(-2\alpha_\varepsilon\), so
  \(\alpha_\varepsilon=48\lambda^2J_\varepsilon+\alpha_{\rm fin}
  +O(\lambda^3)\).
- Extended `calculation-checks/constructive_scalar_spde_checks.py` to verify
  the finite combinatorics and the coefficient \(48/(16\pi^2)=3/\pi^2\).
- Updated the calculation-check README and the Volume XI Chapter 2 dossier.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed after replacing TeX primitive binomial
  notation by `\binom`; the generated `monograph/tex/main.pdf` has 1332
  pages.
