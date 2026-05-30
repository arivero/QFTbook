# 2026-05-30 Finite Liouville Theorem Dequoted

## Scope

- `monograph/tex/volumes/volume_iii/chapter02_conformal_killing_vectors_and_the_conformal_group.tex`
- `planning/chapter_dossiers/volume_iii/chapter02_conformal_killing_vectors_conformal_group.md`

## Substance

The former quoted Liouville theorem in Volume III, Chapter 2 has been replaced
by a local theorem and proof.  The proof no longer imports the finite rigidity
of conformal maps as a black box.  It starts from
\[
  f^*\delta=\Omega_f^2\delta
\]
for a smooth conformal diffeomorphism between connected open subsets of
\(\mathbb R^D\), \(D\ge3\), writes \(\Omega_f=e^\varphi\), and uses the
preservation of the Levi-Civita connection to obtain the second-derivative
equation for \(f\).  Flatness of the pullback metric gives the displayed
conformal curvature equation and hence
\[
  \partial_i\partial_j\varphi
  =
  \partial_i\varphi\,\partial_j\varphi
  -\frac12|\nabla\varphi|^2\delta_{ij}.
\]
For \(q=\Omega_f^{-1}\), this implies \(\partial_i\partial_jq=\rho\delta_{ij}\)
with constant \(\rho\), so \(q=\alpha |x|^2+\beta\cdot x+\gamma\).  Substitution
back gives the null-quadratic condition \(4\alpha\gamma=|\beta|^2\).  The proof
then treats the constant-denominator case and the inversion case separately,
showing that the finite map is affine conformal or affine conformal after one
inversion.

## Remaining Boundary

The theorem is intentionally a smooth local Euclidean theorem.  The later
Lorentzian section still separately defines the projective Lorentzian group
and its Hilbert-space cover.  Spin covers and projective-null-cone
representation theory remain representation-theoretic material rather than
part of this analytic Liouville proof.
