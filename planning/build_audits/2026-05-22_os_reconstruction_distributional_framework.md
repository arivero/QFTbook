# OS Reconstruction Distributional Framework Pass

Date: 2026-05-22

## Scope

This pass strengthened `monograph/tex/volumes/volume_iv/chapter02_osterwalder_schrader_reconstruction.tex` as part of the early nonperturbative framework layer of the monograph.

## Improvements

- Replaced the informal Euclidean-data discussion by a distributional Schwinger hierarchy:
  - Euclidean space \(E=\mathbb R^D\) with \(x=(\tau,\mathbf x)\).
  - A complex field-label space \(V\).
  - Test insertions in \(\mathcal S(E^n;V^{\otimes n})\), or \(C_c^\infty(E^n;V^{\otimes n})\) when compact support is the selected test class.
  - Schwinger functions as distributions \(S_n\in\mathcal S'(E^n;(V^*)^{\otimes n})\), with kernel notation explicitly subordinated to distributional pairing.
- Defined the Euclidean group action, time reflection, and an antilinear label reflection \(J:V\to V\) that records adjunction and tensor/spinor reflection data.
- Defined the positive-time ordered region, the reflected adjoint test function \(\Theta f_n\), the finite-sequence space \(\mathcal E_+\), and the OS sesquilinear form.
- Added an explicit definition of OS-admissible Euclidean field data, including normalization, Euclidean covariance, permutation symmetry, Hermiticity, reflection positivity, and regularity/growth assumptions.
- Clarified the graded/fermionic replacement of permutation symmetry and the role of clustering when uniqueness of the vacuum is required.
- Expanded the Hilbert-space reconstruction:
  - Null quotient and completion.
  - Cauchy--Schwarz on the positive semidefinite form.
  - Positive-time translations as a strongly continuous contraction semigroup \(T_E(s)=e^{-sH}\), with \(H\ge0\).
  - Spatial Euclidean symmetries and analytic continuation as the input for the Lorentzian Poincare representation and spectrum condition.
- Strengthened the field-domain discussion:
  - \(\mathcal D_{\rm OS}\) is the image of \(\mathcal E_+\) before closure.
  - Euclidean field insertion acts by adding ordered test insertions.
  - Lorentzian fields are obtained from boundary values of continued matrix elements.
  - Reconstructed fields are distinguished from represented local observable algebras, whose construction requires closure, affiliation, bounded functional calculus, or an independently built local net.
- Sharpened the reconstruction theorem boundary into three pieces: positive Hilbert space/Hamiltonian, Lorentzian symmetry/spectrum, and distributional boundary values.
- Added a two-point spectral positivity section linking reflection positivity, the Euclidean time semigroup, and the spectral theorem to the Kallen--Lehmann representation introduced in the next chapter.
- Clarified Euclidean-measure reflection positivity, including the distinction between ordinary measure positivity and OS reflected positivity as a remark.
- Updated figure captions and checked OS figures for readability and correct conceptual flow.

## Verification

- Built the monograph with `tools/build_monograph.sh`; the build and log scan were clean.
- Rendered the affected OS chapter pages from `monograph/tex/main.pdf` using `pdftoppm`.
- Visually inspected the rendered pages containing:
  - Schwinger hierarchy and OS-admissible data.
  - Figure 12.1 on reflection positivity.
  - Figure 12.2 on OS reconstruction flow.
  - The reconstruction theorem and two-point spectral positivity.
  - Figure 12.3 on Euclidean measures and verified OS data.

## Next Dependency

The OS chapter now aligns more tightly with the surrounding Wightman, AQFT, path-integral, and Kallen--Lehmann chapters. The next natural foundation pass is to continue uniformizing the comparison between Euclidean boundary values, Lorentzian Wightman functions, and Green functions so that every later use of Wick rotation has an explicit hypothesis boundary.
