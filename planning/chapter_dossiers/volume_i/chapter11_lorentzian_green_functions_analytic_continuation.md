# Volume I, Chapter 11 Dossier: Lorentzian Green Functions and Analytic Continuation

## Source Placement

- Follows perturbative Euclidean Green functions and their self-energy
  expansion.
- Precedes the construction of asymptotic states and the S-matrix.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 4380--4558;
  - `references/253a_notes.tex`, corresponding Lorentzian Feynman-rule block,
    used only as a non-authoritative comparison.

## External Reference Boundary

- Schmidt, "Euclidean Reconstruction in Quantum Field Theory",
  arXiv:math-ph/9811002:
  - used as a reminder that Euclidean-Schwinger to Lorentzian-Wightman
    reconstruction requires positivity, covariance, regularity, and growth
    hypotheses;
  - no reconstruction theorem is proved in this chapter.
- Fredenhagen--Rejzner, "Perturbative algebraic quantum field theory",
  arXiv:1208.1428:
  - used as a rigor lens for time-ordered products and renormalized
    distributional products;
  - no pAQFT foundation is imposed on the monograph.

## Framework

- Lorentzian spacetime \(\mathbb R^{1,D-1}\) with mostly-plus metric
  \(\eta=\operatorname{diag}(-,+,\ldots,+)\).
- A scalar local field \(\widehat\phi\), vacuum vector \(\Omega\), and
  time-ordered Green functions \(G_n\).
- Perturbative Lorentzian rules are boundary-value prescriptions for
  time-ordered Green functions, obtained from Euclidean rules by specified
  contour continuation.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(x^\mu\) | Lorentzian coordinate |
| \(k^\mu=(k^0,\vec k)\) | Lorentzian momentum |
| \(k^2=\eta_{\mu\nu}k^\mu k^\nu\) | mostly-plus square |
| \(\omega_{\vec k}\) | \(\sqrt{\vec k^{\,2}+m^2}\) |
| \(G_n\) | time-ordered Lorentzian \(n\)-point function |
| \(\widetilde G(k)\) | Fourier transform of the two-point function |
| \(\epsilon\) | positive infinitesimal defining Feynman boundary value |
| \(\Sigma(k)\) | Lorentzian self-energy, first-sheet continuation of Euclidean \(\Sigma_E\) |
| \(M\) | lightest invariant mass in the continuum channel under discussion |
| \(E_M(\vec k)\) | \(\sqrt{\vec k^{\,2}+M^2}\) |

## Claims To Establish

- The Lorentzian time-ordered two-point free propagator has denominator
  \(k^2+m^2-i\epsilon\) and poles at
  \(-\omega_{\vec k}+i0\) and \(+\omega_{\vec k}-i0\).
- For labelled quartic vertices the Lorentzian vertex rule is
  \(-ig(2\pi)^D\delta^D(\sum k_i)\).
- The one-loop tadpole contour rotation gives \(i\) times the Euclidean
  self-energy contribution with the sign convention of Chapter 10.
- The full perturbative two-point function has the form
  \[
    \widetilde G(k)=
    {-i\over k^2+m^2-i\epsilon-\Sigma(k)}
  \]
  once \(\Sigma(k)\) is defined by the same Dyson convention.
- Multiparticle spectral support gives branch cuts in \(k^0\) beginning at
  \(\pm E_M(\vec k)\).
- The first-sheet boundary value on the positive-energy cut is obtained by
  continuation from the Euclidean axis to the real axis from above; the
  negative-energy cut has the conjugate Feynman prescription.

## Figure Requirements

- Lorentzian Feynman rule display for propagator and labelled vertex.
- Complex \(\ell^0\)-plane for loop Wick rotation with displaced poles.
- Complex \(k^0\)-plane with two threshold cuts and first-sheet approach
  arrows.

## Exclusions

- No definition of the S-matrix.
- No LSZ formula.
- No interpretation of external legs as asymptotic particles.
- No claim that Euclidean data reconstruct Lorentzian QFT without stating
  reconstruction hypotheses.
