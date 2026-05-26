# Volume VI, Chapter 4 Dossier: Form-Factor Bootstrap and Local Operators

## Logical Role

- Role in the monograph: move from on-shell factorized scattering data to
  local-operator matrix elements.
- Immediate predecessor: Yang--Baxter consistency and internal symmetry.
- Immediate successor: thermodynamic Bethe ansatz and finite-volume spectra.

## Definitions And Results

- Finite-particle form factors as vacuum-to-in-state matrix elements.
- Watson exchange equation derived from the two distributional rapidity
  boundary values and the ordered-state basis relation supplied by
  factorized scattering.
- Cyclicity and semi-locality monodromy, derived from spectrum-condition
  tube analyticity, one-particle crossing, and locality at the boundary of
  the analytic continuation domain.
- Kinematic annihilation pole equation with the direct and scattered Cauchy
  kernels displayed; the relative minus sign is traced to the reversed local
  coordinate \(z_{\rm rev}=-z\) around the annihilation pole.
- Bound-state pole equations.
- Free Majorana examples: the energy-density two-particle form factor, its
  explicit two-particle Wightman spectral density and Euclidean Bessel-kernel
  reconstruction, and the odd Ising order/twist form-factor family.
- Form-factor datum for a scalar local operator.
- Reconstruction boundary for Wightman distributions from spectral series.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(F_n^{\mathcal O}\) | \(n\)-particle form factor of \(\mathcal O\) |
| \(a_i\) | particle species labels |
| \(\theta_i\) | rapidities |
| \(S_{ab}(\theta)\) | two-body scattering map |
| \(\omega_{\mathcal O,a}\) | semi-locality monodromy datum |
| \(\Gamma_{ab}^c\) | bound-state residue tensor |
| \(F_n^\varepsilon\) | free-Majorana energy-density form factor |
| \(s=-P^2\) | positive invariant mass squared in the mostly-plus convention |
| \(K_0\) | modified Bessel function defined by \(K_0(z)=\int_0^\infty e^{-z\cosh u}\,du\) |
| \(F_n^\Sigma\) | odd Ising order/twist form-factor family |

## Claim Ledger

1. Exchange of adjacent rapidities gives Watson's equation when the two
   \(i0\)-boundary values of ordered finite-particle states are related by
   the adjacent factorized \(S\)-matrix; locality enters upstream in
   scattering-state construction and downstream in cyclicity, not as a
   substitute for this boundary-value statement.
2. Cyclicity is a crossing-locality theorem under explicit boundary-value
   hypotheses; semi-locality is an additional monodromy datum.
3. Kinematic-pole residues are differences between direct annihilation and
   annihilation after scattering through spectator particles, with the minus
   sign fixed by the reversed orientation of the annihilation-pole coordinate.
4. Bound-state form-factor poles use the same residue tensors as scattering.
5. In the free Majorana example with \(S=-1\), the energy-density form factor
   checks exchange and cyclicity with a finite two-particle local scalar
   datum.
6. The same energy-density form factor reconstructs the separated-point
   two-point function explicitly:
   \(\widetilde W_\varepsilon(P)=\theta(P^0)\theta(s-4m^2)
   |\kappa_\varepsilon|^2(2m^2)^{-1}\sqrt{1-4m^2/s}\) in the chapter's
   Fourier convention, and the Euclidean correlator is the displayed
   \(K_0\)-kernel integral.  The derivation constructs the delta-function
   Jacobian and the identical-particle factor instead of importing a
   phase-space formula.
7. The odd Ising product formula
   \(F_{2k+1}^{\Sigma}=v i^k\prod_{i<j}\tanh((\theta_i-\theta_j)/2)\)
   satisfies Watson exchange, cyclicity, and the kinematic annihilation
   recursion; the \(i^k\) factor is fixed by the residue equation.
8. Form-factor axioms do not by themselves complete local reconstruction;
   convergence, locality, clustering, and Wightman domains remain theorem
   obligations.

## Calculation Checks

- `calculation-checks/ising_form_factor_checks.py` verifies the free-Majorana
  energy-density exchange/cyclicity identities and the Ising odd-family
  Watson, cyclicity, and kinematic-pole residue signs.  It also checks the
  two-particle invariant-mass identity, the spectral-density normalization
  after the identical-particle cancellation, and the Euclidean
  Bessel-reduction prefactor.

## Figures

- None in this chapter.
