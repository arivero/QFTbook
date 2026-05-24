# Issue 378: LSZ Mass-Shell Boundary Value

GitHub issue #378 noted that Volume I, Chapter 13 wrote
\(\operatorname{Res}_{k^2=-m^2}\widetilde G_2(k)=-iZ\).  That notation was
too coarse: the Feynman two-point function is a boundary value of a meromorphic
function of \(k^0\) at fixed \(\vec k\), while \(k^2+m^2\) is the invariant
denominator whose coefficient is extracted by LSZ.

Edits made:

- Added a warning immediately after the LSZ wave-packet distribution:
  "residue" means coefficient of the isolated Feynman denominator after the
  boundary value, not a complex residue in \(k^2\).
- Expanded the one-particle pole section by factoring
  \(k^2+m^2-i0=-(k^0-\omega_{\vec k}+i0)(k^0+\omega_{\vec k}-i0)\).
- Displayed the partial-fraction decomposition
  \[
    \frac{-iZ}{k^2+m^2-i0}
    =
    \frac{iZ}{2\omega_{\vec k}}
    \left(
      \frac{1}{k^0-\omega_{\vec k}+i0}
      -
      \frac{1}{k^0+\omega_{\vec k}-i0}
    \right),
  \]
  so that the \(k^0\)-plane residues are distinguished from the invariant
  denominator coefficient.
- Replaced the misleading \(\operatorname{Res}_{k^2=-m^2}\) display by
  \[
    \operatorname{bv}_{\Sigma_m}
    \left[(k^2+m^2)\widetilde G_2(k)\right]
    =
    -iZ,
  \]
  and defined \(\operatorname{bv}_{\Sigma_m}\) as the Feynman mass-shell
  boundary value selected after wave-packet smearing.
- Updated the chapter dossier symbols, claims, and audit notes accordingly.

This keeps the LSZ normalization tied to the Haag--Ruelle mass-shell measure
and prevents the invariant denominator coefficient \(-iZ\) from being confused
with the one-variable residues \( \pm iZ/(2\omega_{\vec k}) \).
