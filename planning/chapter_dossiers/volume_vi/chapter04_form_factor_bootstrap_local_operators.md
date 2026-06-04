# Volume VI, Chapter 4 Dossier: Form-Factor Bootstrap and Local Operators

## Logical Role

- Role in the monograph: move from on-shell factorized scattering data to
  local-operator matrix elements.
- Immediate predecessor: nested Bethe ansatz and matrix Bethe--Yang equations.
- Immediate successor: thermodynamic Bethe ansatz and finite-volume spectra.

## Definitions And Results

- Local-operator form-factor datum
  \(\mathfrak F_{\mathcal O}\) over a regular factorized scattering datum,
  including the operator domain, meromorphic covectors, semi-locality
  monodromies, kinematic and bound-state residue data, and explicit growth
  bounds before the bootstrap equations are used.
- Finite-particle form factors as vacuum-to-in-state matrix elements.
- Watson exchange equation derived from the two distributional rapidity
  boundary values and the ordered-state basis relation supplied by
  factorized scattering.
- Cyclicity and semi-locality monodromy, derived from spectrum-condition
  tube analyticity, one-particle crossing, and locality at the boundary of
  the analytic continuation domain.
- Kinematic annihilation pole equation with the direct and scattered Cauchy
  kernels displayed; the direct coefficient is matched to the rapidity delta
  contraction through the Sokhotski boundary-value identity, and the relative
  minus sign is traced to the reversed local coordinate \(z_{\rm rev}=-z\)
  around the annihilation pole.
- Bound-state pole equations.
- Free Majorana examples: the energy-density two-particle form factor, its
  explicit two-particle Wightman spectral density and Euclidean Bessel-kernel
  reconstruction, the even semi-local Ising spin-field family, its crossed
  mixed bra/ket product formula, the odd Ising order/twist form-factor
  family, and separated Euclidean convergence estimates for the infinite
  spin/twist spectral series.
- Status checkpoint from form-factor equations to local fields: Hilbert-space
  domain/closability, Wightman-distribution convergence including collision
  diagonals, positivity/covariance/spectrum condition, spacelike
  local-commutativity or semi-locality, and sector completeness.
- Reconstruction boundary for Wightman distributions from spectral series.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(F_n^{\mathcal O}\) | \(n\)-particle form factor of \(\mathcal O\) |
| \(\mathfrak F_{\mathcal O}\) | local-operator form-factor datum over a regular factorized scattering datum |
| \(\mathcal P_{\rm kin}\) | annihilation-pole residue data in \(\mathfrak F_{\mathcal O}\) |
| \(\mathcal P_{\rm bs}\) | bound-state residue data in \(\mathfrak F_{\mathcal O}\) |
| \(\mathcal G_{\mathcal O}\) | growth and boundary-value bounds in \(\mathfrak F_{\mathcal O}\) |
| \(a_i\) | particle species labels |
| \(\theta_i\) | rapidities |
| \(S_{ab}(\theta)\) | two-body scattering map |
| \(\omega_{\mathcal O,a}\) | semi-locality monodromy datum |
| \(\Gamma_{ab}^c\) | bound-state residue tensor |
| \(F_n^\varepsilon\) | free-Majorana energy-density form factor |
| \(s=-P^2\) | positive invariant mass squared in the mostly-plus convention |
| \(K_0\) | modified Bessel function defined by \(K_0(z)=\int_0^\infty e^{-z\cosh u}\,du\) |
| \(P_N\) | Ising product \(\prod_{i<j}\tanh((\theta_i-\theta_j)/2)\) |
| \(\bar\sigma\) | spin-field vacuum expectation value in the ordered massive-Ising convention |
| \(F_n^{\sigma_+}\) | even semi-local spin-field form-factor family |
| \(F_n^\Sigma\) | odd Ising order/twist form-factor family |
| \(I_m(r)\) | one-particle Euclidean majorant \(K_0(mr)/\pi\) for the free Majorana mass \(m\) |

## Claim Ledger

1. A local-operator form-factor datum is not merely a list of meromorphic
   functions.  It includes the operator domain, the species-space covector
   interpretation, semi-locality monodromies, pole-residue tensors inherited
   from the scattering datum, and growth hypotheses strong enough for whatever
   distributional reconstruction is claimed.
2. Exchange of adjacent rapidities gives Watson's equation when the two
   \(i0\)-boundary values of ordered finite-particle states are related by
   the adjacent factorized \(S\)-matrix; locality enters upstream in
   scattering-state construction and downstream in cyclicity, not as a
   substitute for this boundary-value statement.
3. Cyclicity is a crossing-locality theorem under explicit boundary-value
   hypotheses; semi-locality is an additional monodromy datum.
4. Kinematic-pole residues are differences between direct annihilation and
   annihilation after scattering through spectator particles, with the minus
   sign fixed by the reversed orientation of the annihilation-pole coordinate.
5. Bound-state form-factor poles use the same residue tensors as scattering.
6. In the free Majorana example with \(S=-1\), the energy-density form factor
   checks exchange and cyclicity with a finite two-particle local scalar
   datum.
7. The same energy-density form factor reconstructs the separated-point
   two-point function explicitly:
   \(\widetilde W_\varepsilon(P)=\theta(P^0)\theta(s-4m^2)
   |\kappa_\varepsilon|^2(2m^2)^{-1}\sqrt{1-4m^2/s}\) in the chapter's
   Fourier convention, and the Euclidean correlator is the displayed
   \(K_0\)-kernel integral.  The derivation constructs the delta-function
   Jacobian and the identical-particle factor instead of importing a
   phase-space formula.
8. The even spin-field family
   \(F_{2k}^{\sigma_+}=\bar\sigma i^kP_{2k}\) satisfies Watson exchange,
   semi-local cyclicity with phase \(-1\), and the semi-local kinematic-pole
   equation \( -i\,\mathrm{Res}\,F_{n+2}^{\sigma_+}=(1+(-1)^n)F_n^{\sigma_+}\).
9. Crossing the even spin-field family gives the connected mixed bra/ket
   formula with \(\tanh\)-factors within each side and \(\coth\)-factors
   between crossed and uncrossed rapidities, including the
   \(i^{(K+N)/2}\bar\sigma\) phase in this chapter's convention.
10. The odd Ising product formula
   \(F_{2k+1}^{\Sigma}=v i^k\prod_{i<j}\tanh((\theta_i-\theta_j)/2)\)
   satisfies Watson exchange, cyclicity, and the kinematic annihilation
   recursion; the \(i^k\) factor is fixed by the residue equation.
11. The infinite even and odd Ising product families reconstruct separated
   Euclidean two-point functions on the temporal ray by absolutely convergent
   finite-particle spectral series.  The proof uses the explicit bound
   \(|\tanh((\theta_i-\theta_j)/2)|\le1\), the one-particle integral
   \(I_m(r)=K_0(mr)/\pi\), and the even/odd exponential majorants
   \(\cosh I_m(r)\) and \(\sinh I_m(r)\), with uniform convergence of
   \(r\)-derivatives on compact subsets of \(r>0\).
12. The reconstruction checkpoint separates theorem-level Ising/free-fermion
   control from the interacting factorizing-model program: Watson, cyclicity,
   and residue equations are matrix-element identities, while local-field
   reconstruction additionally requires common domains, closability,
   distributional convergence, contact-term extension, positivity,
   covariance, spacelike locality or semi-locality, and sector completeness.
13. Form-factor axioms do not by themselves complete local reconstruction;
   convergence, locality, clustering, and Wightman domains remain theorem
   obligations.

## Calculation Checks

- `calculation-checks/ising_form_factor_checks.py` verifies the free-Majorana
  energy-density exchange/cyclicity identities, the Cauchy-kernel orientation
  behind the annihilation-pole sign, and the Ising odd-family Watson,
  cyclicity, and kinematic-pole residue signs.  It also checks the
  two-particle invariant-mass identity, the spectral-density normalization
  after the identical-particle cancellation, the Euclidean Bessel-reduction
  prefactor, the even spin-field semi-local cyclicity phase, the crossed
  \(\coth\) matrix element, the semi-local kinematic residue, and the
  even/odd spectral-series majorants.

## Audit Notes

- 2026-05-31 anti-wrapper pass: demoted the odd Ising product-family
  Watson/cyclicity/kinematic-residue check from proposition/proof form to a
  convention-sensitive verification paragraph.  The formulas and residue
  calculation remain in the chapter; theorem-family status is reserved for the
  separated Euclidean spectral-series convergence statement.
- 2026-05-31 issue #691 continuation: demoted the even Ising spin-field
  product-family statement from proposition/proof form to a worked derivation
  paragraph.  The \(F_{2k}^{\sigma_+}=\bar\sigma i^kP_{2k}\) formula,
  semi-local cyclicity, annihilation-pole residue, crossed connected
  \(\coth\)-matrix element, and Fonseca--Zamolodchikov comparison remain
  explicit; theorem-family rank remains with the separated Euclidean
  spectral-series convergence result.
- 2026-06-03 reconstruction-spine point-of-use pass: added the chapter-level
  status checkpoint preventing form-factor equations from being read as a
  local-field construction without Hilbert-space, convergence, positivity,
  locality, and completeness input.

## Figures

- None in this chapter.
