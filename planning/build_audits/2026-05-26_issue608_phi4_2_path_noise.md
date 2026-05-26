# Issue 608: Phi4_2 Path-Space Enhanced Noise

## Scope

This pass addresses the concrete path-space enhanced-noise gap in
`volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.

## Mathematical Change

- Added Proposition
  `prop:spde-two-dimensional-enhanced-noise-path-convergence`.
- Proved the exact Ornstein--Uhlenbeck time cross-covariance
  \(E[X_k(t)\overline{X_\ell(s)}]=\delta_{k\ell}e^{-a_k|t-s|}/a_k\).
- Derived the Fourier increment variance for \(:X_N^n:\), \(n=1,2,3\).
- Used \(1-e^{-r}\le r^\vartheta\) to replace one covariance propagator by
  a weakened propagator \(g_\vartheta(k)=(1+|k|^2)^{-1+\vartheta}\).
- Proved the corresponding two-dimensional convolution bound and the
  \(H^{-s}\) summability condition \(\vartheta<s\).
- Used finite-Wiener-chaos moment bounds and the Kolmogorov/grid argument to
  obtain convergence in probability in \(C([0,T];H^{-s})^3\).
- Updated the \(\Phi^4_2\) stochastic-quantization assembly theorem so
  path-space enhanced-noise convergence is no longer listed as an assumed
  analytic fact.
- Added Proposition
  `prop:spde-os-positivity-closed-under-weak-convergence`, proving that OS
  reflection positivity on bounded positive-time cylinder observables is
  closed under weak convergence of measures.  The finite-cutoff
  reflection-positivity input remains explicit, and the only extra condition
  for unbounded Wick-polynomial observables is the stated uniform
  integrability needed for truncation.
- Added Remark `rem:spde-fourier-cutoff-os-regulator-separation`, making
  explicit that the Fourier-Galerkin cutoff used for stochastic estimates is
  not being assumed to be OS-positive.  OS positivity is a separate property
  of the Euclidean regulator, or else one owes a regulator-independence
  comparison theorem.
- Added Proposition
  `prop:spde-lattice-cutoff-os-positive-regulator`, proving that finite
  nearest-neighbor lattice scalar cutoffs with positive kinetic coefficients
  and reflection-invariant real on-site potential are OS reflection positive.
  The proof uses the explicit cross-plane expansion
  \(\exp(c\phi_x\phi_{\vartheta x})=\sum_n c^n\phi_x^n\phi_{\vartheta x}^n/n!\)
  and expresses the reflection quadratic form as a sum of half-lattice
  absolute squares.
- Clarified that this lattice theorem supplies a concrete OS-positive
  Euclidean regulator but does not, by itself, identify the lattice
  Schwinger functions with the Fourier-Galerkin stochastic-quantization
  family.  The remaining comparison is now stated as a regulator-comparison
  theorem: after matching local coordinates, prove convergence of the
  relevant Schwinger functions or construct one regulator supporting both
  the Langevin estimates and OS positivity.

## Remaining Issue-608 Boundary

This pass does not yet close issue #608.  The remaining hard parts are the
global rough Besov/Hölder energy-continuity estimates, tightness and
uniform moment bounds for the invariant cutoff laws, comparison between the
OS-positive lattice regulator and the Fourier-Galerkin stochastic regulator
or construction of a common regulator, the concrete \(\Phi^4_3\)
modelled-distribution estimates, and the full SPDE-to-Wightman closure.
