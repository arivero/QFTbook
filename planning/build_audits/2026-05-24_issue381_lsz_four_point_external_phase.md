# Issue 381: LSZ Four-Point External Phase Bookkeeping

GitHub issue #381 noted that the tree-level \(\phi^4\) LSZ calculation left
the four external propagator numerators in product form and did not display
that \((-\ii)^4=1\).

Edits made:

- Inserted the explicit identity
  \[
    \prod_{a=1}^4(-\ii)=(-\ii)^4=1 .
  \]
- Displayed the per-leg LSZ cancellation
  \[
    \ii(k_a^2+m^2)\frac{-\ii}{k_a^2+m^2-\ii0}\longrightarrow 1
  \]
  after the mass-shell boundary value.
- Displayed the four-leg product
  \[
    \prod_{a=1}^4
    \left[
      \ii(k_a^2+m^2)
      \frac{-\ii}{k_a^2+m^2-\ii0}
    \right]
    \longrightarrow
    (\ii(-\ii))^4=1 .
  \]
- Added the general \(N\)-external-scalar bookkeeping
  \(\ii^N(-\ii)^N=1\), so the remaining factor is the connected amputated
  kernel.
- Updated the chapter dossier claim and audit notes.

The resulting tree-level connected scattering kernel remains
\(-\ii g\,(2\pi)^D\delta^{(D)}(\sum q-\sum p)\), hence with the chapter's
amplitude convention \(i\mathcal M\) one obtains \(\mathcal M=-g+O(g^2)\).
