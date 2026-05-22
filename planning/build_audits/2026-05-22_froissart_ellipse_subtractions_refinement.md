# Froissart Ellipse and Subtractions Refinement

Date: 2026-05-22

Scope:
- Refined the Lehmann-ellipse parametrization with \(R=\ee^\eta\), \(x_R=\cosh\eta\), and the large-energy relation \(\eta_*(s)=2\sqrt{t_*/s}+O(s^{-3/2})\).
- Added the explicit ellipse coordinate \(z=(R\ee^{i\varphi}+R^{-1}\ee^{-i\varphi})/2\), identifying the semimajor and semiminor axes.
- Tightened the Legendre-kernel convergence statement and the exponential partial-wave coefficient bound inside smaller ellipses.
- Replaced the compressed Legendre lower-bound step with a hyperbolic variable derivation from the integral representation of \(P_\ell(\cosh\eta)\), including the nontrivial case \(L(y-1)\ge1\).
- Reframed the two-subtraction conclusion as a conditional consequence of the real-axis absorptive bound and finite-subtraction hypothesis.
- Added the explicit positivity formula for derivatives of Legendre polynomials at \(x=1\), used in the complex-\(t\) extension.
- Reworded the scope paragraph so massless and gravitational cases are described by their applicable observables and hypotheses.

Verification:
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- Rendered and visually inspected PDF pages 174--183 at 150 dpi, covering the chapter opening, Lehmann ellipse figure, partial-wave normalization, Froissart profile figure, dispersion contour region, two-subtraction refinement, and scope page.

Follow-up:
- A later analytic-S-matrix pass should state more precisely which nonperturbative analyticity domains are assumed, which are proven in existing frameworks, and which are perturbative diagnostics.
