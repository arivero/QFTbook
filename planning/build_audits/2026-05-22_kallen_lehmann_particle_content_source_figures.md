# 2026-05-22 Kallen-Lehmann and Particle-Content Source Audit

## Source Scope

- Handwritten source: `references/253a lectures 2022.pdf`, pp. 80--99.
- Source visual trace:
  `monograph/tex/build/source_visual_trace/253a_trace-080.png` through
  `253a_trace-099.png`.
- Operational transcript: `transcription/tex/253a/foundations.tex`, the
  spectral-representation and particle-content block.
- Manuscript home:
  `monograph/tex/volumes/volume_i/chapter09_kallen_lehmann_spectral_representation_and_particle_content.tex`.

## Coverage Added

- Recovered the generalized spectral insertion notation for the Wightman
  two-point function while keeping the spectral measure \(d\nu_\phi\) as the
  rigorous object.
- Made the Lorentz-invariant mass decomposition explicit, including the density
  shorthand \(\theta(p^0)\rho(-p^2)/(2\pi)^{D-1}\) when an ordinary density
  exists.
- Added the spacelike equality
  \(\Delta_+(x;\mu^2)=\Delta_+(-x;\mu^2)\) and stated why it is not a timelike
  equality.
- Added the \(k^0\)-contour derivation of the Feynman prescription, including
  the displaced poles \(+\omega-\ii0\) and \(-\omega+\ii0\), the lower closure
  for \(x^0>0\), and the upper closure for \(x^0<0\).
- Added the Euclidean continuation domain
  \(\operatorname{Im}(x^0-y^0)<0\) and the two Euclidean time orderings.
- Added the scalar one-particle standard-boost construction, Wigner little
  group, delta-normalized states, \(N(\vec k)=\sqrt{m/\omega_{\vec k}}\),
  invariant normalization, and the field-overlap definition of \(Z\).
- Rewrote the one-particle atom calculation as a momentum-space measure first,
  then compared it with the invariant-mass decomposition to obtain
  \(d\rho_1=Z\delta_{m^2}\).

## Figure Audit

- Replaced the source \(k^0\)-plane contour with a TikZ contour figure whose
  axes, pole displacements, and upper/lower closures are visible at page scale.
- Added a TikZ positive mass-shell diagram showing the rest momentum \(k_R\),
  the standard boost \(L(\vec k)\), and the target momentum \(k\).
- Preserved and rechecked the spectral projection diagram for
  \(\widehat\phi(f)\Omega\) into vacuum, one-particle, and continuum spectral
  parts.
- Rechecked the spectral-measure graph with one-particle atom at \(m^2\) and
  continuum support beginning at \(4m^2\) under the stated threshold
  assumptions.

## Verification

- Ran `tools/build_monograph.sh`; build and strict text audit completed cleanly.
- Rendered manuscript pages
  `monograph/tex/build/source_visual_trace/kallen_render-090.png` through
  `kallen_render-098.png` and inspected the new and existing figures.
- The chapter keeps scattering and the S-matrix out of this block except for a
  final statement that their construction comes later.
