# Volume I, Chapter 11 Dossier: Lorentzian Green Functions and Analytic Continuation

## Source Placement

- Follows perturbative Euclidean Green functions and their self-energy
  expansion.
- Precedes the construction of asymptotic states and the S-matrix.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 4380--4558;
  - `references/253a_notes.tex`, corresponding Lorentzian Feynman-rule block,
    used only as a non-authoritative comparison.
- Source/figure certification:
  - handwritten pp. 110--112 were checked against the compiled manuscript on
    2026-05-22;
  - audit file:
    `planning/build_audits/2026-05-22_perturbative_green_functions_source_figures.md`.

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
- A scalar Wightman field presentation in a vacuum sector, including
  \(\Hilb\), \(\Omega\), translation generators \(P^\mu\) with spectrum in
  \(\overline V_+\), and a scalar operator-valued distribution
  \(\widehat\phi\).
- The analytic-continuation category is the tempered Schwartz pairing:
  Lorentzian kernels live in \(\mathcal S'(M^r)\), and relative-coordinate
  boundary values live in \(\mathcal S'(M^{r-1})\).
- Time-ordered Green functions \(G_n\) are distributions extending the
  noncoincident ordered Wightman restrictions across partial diagonals.
- Perturbative Lorentzian rules are boundary-value prescriptions for
  time-ordered Green functions, obtained from Euclidean rules by specified
  contour continuation.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(x^\mu\) | Lorentzian coordinate |
| \(k^\mu=(k^0,\vec k)\) | Lorentzian momentum |
| \(k^2=\eta_{\mu\nu}k^\mu k^\nu\) | mostly-plus square |
| \(M\) | Lorentzian spacetime \(\mathbb R^{1,D-1}\) |
| \(\overline V_+\) | closed forward spectrum cone \(\{p:p^0\ge0,\ p^2\le0\}\) |
| \(W_n\) | Wightman \(n\)-point distribution |
| \(w_n\) | relative-coordinate Wightman distribution in \(\mathcal S'(M^{n-1})\) |
| \(\widetilde w_n\) | Fourier transform of \(w_n\), supported in \(\overline V_+^{\,n-1}\) |
| \(\omega_{\vec k}\) | \(\sqrt{\vec k^{\,2}+m^2}\) |
| \(G_n\) | time-ordered Lorentzian \(n\)-point function |
| \(M_\pi^n\) | strict time-ordering region for permutation \(\pi\) |
| \(\mathcal W_{n,\pi}\) | holomorphic continuation of the Wightman ordering \(\pi\) |
| \(F_\pm\) | holomorphic tube functions in the distributional edge-of-the-wedge theorem |
| \(S_n\) | Euclidean Schwinger \(n\)-point distribution |
| \(\widetilde G(k)\) | Fourier transform of the two-point function |
| \(\epsilon\) | positive infinitesimal defining Feynman boundary value |
| \(\Sigma(k)\) | Lorentzian self-energy, first-sheet continuation of Euclidean \(\Sigma_E\) |
| \(k_E^D\) | Euclidean external energy related by \(k^0=i k_E^D\) |
| \(M\) | lightest invariant mass in the continuum channel under discussion |
| \(E_M(\vec k)\) | \(\sqrt{\vec k^{\,2}+M^2}\) |

## Claims To Establish

- A vacuum time-ordered Green function is a distribution whose restriction
  to each strict time-ordering region agrees with the corresponding Wightman
  ordering.
- Local commutativity gives compatibility across spacelike equal-time
  boundaries; extension across partial diagonals is local time-ordered product
  data.
- The spectrum condition gives tube analyticity in relative variables, with
  boundary values obtained after pairing with test functions.
- Boundary values in this chapter are \(\mathcal S'\)-limits in relative
  variables; compactly supported local-field smearing is compatible because
  \(C_c^\infty\) test functions are Schwartz.
- The edge-of-the-wedge step uses holomorphic tube functions with polynomial
  growth near the real edge and equal distributional boundary values on an
  open spacelike real set.
- Ordered imaginary shifts
  \(\epsilon_1>\cdots>\epsilon_n>0\) give the time-ordered boundary value of
  the holomorphic Wightman function.
- Ordered Euclidean times give Schwinger functions as imaginary-time
  restrictions of the same holomorphic functions under Wightman tube
  analyticity, while OS-admissible Schwinger data reconstructs Wightman
  boundary values by the reconstruction theorem.
- The Lorentzian time-ordered two-point free propagator has denominator
  \(k^2+m^2-i\epsilon\) and poles at
  \(-\omega_{\vec k}+i0\) and \(+\omega_{\vec k}-i0\).
- For labelled quartic vertices the Lorentzian vertex rule is
  \(-ig(2\pi)^D\delta^D(\sum k_i)\).
- For unlabelled four-field insertions direct expansion gives
  \(-ig(2\pi)^D\delta^D(\sum k_i)/4!\), and the labelled rule follows by
  contraction counting.
- The one-loop tadpole contour rotation gives \(i\) times the Euclidean
  self-energy contribution with the sign convention of Chapter 10.
- In the same regulator and local two-point subtraction convention,
  \[
    \Sigma(k^0=i k_E^D,\vec k_E)=\Sigma_E(k_E),
    \qquad
    \widetilde G(i k_E^D,\vec k_E)=-i\widetilde G_E(k_E),
  \]
  so the factor \(i\) in the Lorentzian insertion is not an additional sign in
  the denominator self-energy.
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
- The continuation path is stated as \(k^0=i k_E^D\) from the imaginary
  \(k^0\)-axis to the real boundary value without crossing first-sheet cuts.

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

## Audit Notes

- 2026-05-24 issue #330 pass: fixed the function-space drift by declaring
  \(\mathcal S/\mathcal S'\) as the chapter's analytic-continuation category,
  writing the relative Wightman distribution, Fourier support condition,
  Fourier-Laplace transform, and \(\mathcal S'\) boundary-value limit
  explicitly, and adding the distributional edge-of-the-wedge theorem with
  growth and boundary-agreement hypotheses.
- 2026-05-24 issue #372 pass: displayed the equality of Euclidean and
  Lorentzian denominator self-energies under \(k^0=i k_E^D\), with the
  corresponding \(\widetilde G(i k_E^D,\vec k_E)=-i\widetilde G_E(k_E)\)
  identity.
