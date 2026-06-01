# Six-Dimensional Defect Group: Circle Finite-Flux Decomposition

This pass continues the Volume VII Chapter 11 six-dimensional depth lane.  The
finite \(H^3(Y;A_{\mathfrak g})\) Heisenberg system was already present; the
new text specializes it to \(Y=S^1\times X_5\), where it becomes the finite
global-form datum of the five-dimensional compactification.

Added manuscript content:
- product splitting
  \(H^3(S^1\times X_5;A_{\mathfrak g})
  \simeq H^3(X_5;A_{\mathfrak g})\oplus\eta H^2(X_5;A_{\mathfrak g})\);
- cup-product sign derivation
  \(\langle u+\eta v,u'+\eta v'\rangle
  =\int_{X_5}\{b(v\smile u')-b(u\smile v')\}\);
- interpretation of \(H^3(X_5;A_{\mathfrak g})\) as the unwrapped
  five-dimensional surface-defect finite charge and
  \(\eta H^2(X_5;A_{\mathfrak g})\) as the circle-wrapped surface-defect
  sector, hence five-dimensional line-defect finite charge;
- statement that a polarization is a finite topological supplement to the
  local gauge algebra, not a datum determined by the local Yang--Mills density.

The calculation check `susy_abjm_6d_checks.py` now verifies the cyclic
one-cell model for the circle-pairing sign, alternating/skew symmetry,
nondegeneracy, and the two natural isotropic polarizations.
