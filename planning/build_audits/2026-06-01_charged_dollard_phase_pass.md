# Charged Haag--Ruelle Dollard Phase Pass

This pass continues GitHub issues #527 and #528.  Earlier work localized the
missing charged Haag--Ruelle theorem in the replacement exchange and modified
Cook estimates.  The new text supplies the finite-dimensional asymptotic
calculation behind the comparison phase required by those estimates.

Added manuscript content in Volume IV Chapter 5:
- a proposition for
  \(V(t)=\kappa/\sqrt{a^2+|b+ut|^2}\) with \(u\ne0\), proving
  \[
    \int_{T_0}^T V(t)\,dt
    =(\kappa/|u|)\log T+C+O(T^{-1});
  \]
- the completed-square variables
  \(\sigma=(b\cdot u)/|u|^2\), \(b_\perp=b-\sigma u\), and
  \(\rho^2=a^2+|b_\perp|^2\);
- the exact primitive by an \(\operatorname{arsinh}\) expression;
- the interpretation that a charged QFT pair term with the same \(t^{-1}\)
  asymptotic must be absorbed into \(\Theta_I(t)\), while the open theorem is
  to derive the coefficient and the \(L^1\) remainder from Wilson-line or
  Coulomb-dressed charged creators.

The paired calculation check now verifies the exact \(\operatorname{arsinh}\)
primitive and the logarithmic coefficient for sample finite-dimensional
Coulomb tails.
