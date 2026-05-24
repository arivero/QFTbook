# Issue #330 Wick-Rotation Function-Space Pass

Date: 2026-05-24

## Files Touched

- `monograph/tex/volumes/volume_i/chapter11_lorentzian_green_functions_and_analytic_continuation.tex`
- `planning/chapter_dossiers/volume_i/chapter11_lorentzian_green_functions_analytic_continuation.md`

## Mathematical Point

The Wick-rotation chapter now fixes its analytic-continuation category:

- Lorentzian \(r\)-point kernels are tempered distributions in
  \(\mathcal S'(M^r)\);
- after translation invariance, tube boundary values are limits in
  \(\mathcal S'(M^{r-1})\);
- the relative Wightman distribution \(w_n\) and its Fourier transform
  \(\widetilde w_n\) are named, with
  \(\operatorname{supp}\widetilde w_n\subset\overline V_+^{\,n-1}\);
- the Fourier-Laplace transform is displayed as the holomorphic function in
  the tube;
- boundary values are explicitly paired with
  \(f\in\mathcal S(M^{n-1})\).

## Edge-of-the-Wedge Hypotheses

The previous bare invocation was replaced by a theorem statement listing the
hypotheses used in the chapter:

- holomorphy on two tubes over an open real set;
- polynomial growth near the real edge, sufficient for distributional
  boundary values;
- equality of those boundary values on a nonempty open real set;
- conclusion: a common holomorphic continuation in a complex neighborhood of
  the real edge.

The text then identifies the Wightman inputs: tempered spectral
Fourier-Laplace bounds and local-commutativity equality on spacelike real
regions.
