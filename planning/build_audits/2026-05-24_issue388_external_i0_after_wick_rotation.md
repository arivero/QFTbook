# Issue #388 External \(-i0\) After Wick Rotation Audit

GitHub issue #388 asked for the self-energy Wick-rotation paragraph in
Volume II, Chapter 4 to distinguish two different uses of the Feynman
prescription.

## Clarification

After the shifted loop energy is Wick rotated, the Euclidean loop integral is
an integral over real \(\ell_E\) with an ordinary Euclidean denominator.  There
is no residual pole prescription attached to \(\ell_E\).

The \(-i0\) that appears later in expressions such as
\[
  k^2x(1-x)+m_1^2-i0
\]
or
\[
  1-\frac{s\,x(1-x)}{m_1^2}-i0,\qquad k^2=-s,
\]
is the Lorentzian boundary-value prescription for the external invariant
\(k^2\).  It specifies which edge of the external timelike cut is taken after
the Euclidean integral has defined the analytic function.

## Files Changed

- `monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex`
- `planning/chapter_dossiers/volume_ii/chapter04_resonances_dressed_propagators.md`
