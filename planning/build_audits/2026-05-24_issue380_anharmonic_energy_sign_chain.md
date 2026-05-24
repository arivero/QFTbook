# Issue 380: Anharmonic Ground-State Energy Sign Chain

GitHub issue #380 flagged that the anharmonic-oscillator chapter displayed the
negative first-order vacuum graph in \(Z_g/Z_0\) and later the positive
first-order ground-state energy shift, but did not show explicitly how
\(E_0=-T^{-1}\log Z\) reverses the sign.

Edits made:

- Labeled the first-order vacuum correction as
  `eq:anharmonic-leading-correction`.
- Wrote the correction as
  \[
    (Z_g/Z_0-1)_{O(g)}
    =
    -\frac{g}{4!}\int\dd\tau\,\langle q(\tau)^4\rangle_0
    =
    -\frac{g}{8}\int\dd\tau\,G_0(\tau,\tau)^2 .
  \]
- Inserted the spectral extraction of the energy difference:
  \[
    E_0(g)-E_0(0)
    =
    -\lim_{T_{\rm tot}\to\infty}
    T_{\rm tot}^{-1}\log(Z_g/Z_0).
  \]
- Displayed the first-order logarithm per unit Euclidean time,
  \[
    T_{\rm tot}^{-1}\log(Z_g/Z_0)
    =
    -\frac{g}{8}G_0(0)^2+O(g^2),
  \]
  and then derived
  \(\Delta E_0=+(g/8)G_0(0)^2+O(g^2)=g/32+O(g^2)\).
- Stated explicitly that the sign comes from the energy extraction formula
  together with the per-vertex factor \(-g/4!\).
- Updated the chapter dossier claim ledger and certification notes.

This keeps the sign convention tied to the Euclidean transition kernel and the
linked-cluster logarithm, rather than leaving the reconciliation implicit.
