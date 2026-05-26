# Volume XI, Chapter 3 Dossier: Lattice Reflection Positivity

## Logical Role

- Role in the monograph: give a finite-regulator positivity mechanism for
  OS-type reconstruction.
- Immediate predecessor: constructive scalar models and OS data.
- Immediate successor: continuum limits and scaling windows.

## Definitions And Results

- Reflection-invariant lattice and positive-time algebra.
- Antilinear reflection operation \(\Theta\).
- Lattice reflection positivity condition.
- Nearest-neighbor scalar lattice measure.
- Proof of reflection positivity by positive power-series expansion of
  cross-plane kernels.
- Free lattice fermion reflection positivity for the mid-link reflection.
- Failure of site and diagonal fermion reflections by two-point tests.
- Staggered fermion reflection and Thirring interaction positivity for
  \(U\geq0\).
- Transfer-matrix interpretation.
- Osterwalder-Seiler character-expansion criterion for compact lattice
  gauge fields.
- Wilson plaquette reflection positivity for \(SU(N)\), \(U(N)\), and the
  \(U(1)\) Bessel/Fourier expansion.
- Explicit \(SU(2)\) Wilson character coefficients
  \(a_\ell=I_\ell-I_{\ell+2}=2(\ell+1)I_{\ell+1}/\beta>0\), derived from
  Haar class-function orthogonality.
- Improved-action caveat: negative rectangle coefficients fall outside the
  positive-character proof and require a separate positivity theorem.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Lambda\) | finite lattice |
| \(\vartheta\) | reflection of the lattice |
| \(\mathcal A_+\) | algebra of positive-time functions |
| \(\Theta\) | antilinear reflected action on functions |
| \(d\mu\) | lattice probability measure |
| \(S(\phi)\) | lattice scalar action |
| \(C_\mu\) | Euclidean Clifford matrices for lattice fermions |
| \(\psi_A,\bar\psi^A\) | independent lattice Grassmann variables |
| \(R\) | mid-link lattice reflection |
| \(\eta,\bar\eta\) | one-component staggered fermion variables |
| \(U_\ell\) | compact-group variable on an oriented gauge link |
| \(U_p\) | plaquette holonomy |
| \(w(g)\) | one-plaquette class-function weight |
| \(\chi_\lambda\) | irreducible character of the compact gauge group |
| \(c_\lambda\) | character-expansion coefficient of \(w\) |
| \(I_n(\beta)\) | modified Bessel coefficient in the \(U(1)\) and \(SU(2)\) Wilson-weight expansions |
| \(a_\ell(\beta)\) | \(SU(2)\) Wilson character coefficient for spin \(\ell/2\) |

## Claim Ledger

1. Reflection positivity is a measure property relative to a reflection and a
   positive algebra.
2. Nearest-neighbor scalar lattice actions with positive couplings are
   reflection positive by explicit kernel expansion.
3. The transfer-matrix Hilbert space is the quotient of \(\mathcal A_+\) by
   the null space of the reflection-positive form.
4. Free nearest-neighbor lattice fermions require the mid-link reflection
   \(v=e_1,c=1/2\); site and diagonal reflections fail elementary two-point
   positivity tests.
5. A staggered Thirring interaction preserves the same positivity mechanism
   for \(U\geq0\).
6. Compact gauge measures with nonnegative plaquette character expansion
   are reflection positive by Peter-Weyl decomposition of every crossing
   plaquette into a sum of reflected squares.
7. The Wilson plaquette weight has nonnegative character coefficients
   because its exponential expansion decomposes tensor products of defining
   and conjugate defining representations with nonnegative multiplicities.
8. In \(SU(2)\), the coefficient positivity is checked explicitly by Haar
   orthogonality and the Bessel recurrence
   \(I_\ell-I_{\ell+2}=2(\ell+1)I_{\ell+1}/\beta\).
9. Improved actions with negative crossing-loop coefficients, including
   standard tree-level Symanzik/Luscher-Weisz and Iwasaki rectangle terms,
   are not covered by the Wilson proof and require separate positivity
   control.

## Calculation Checks

- `calculation-checks/lattice_reflection_positivity_checks.py` verifies the
  \(U(1)\) Fourier/Bessel positivity, the \(SU(2)\) Wilson coefficient
  identity, reconstruction of sample Wilson weights from truncated positive
  character expansions, and finite \(SU(2)\) tensor-product character
  identities.

## Figures

- Reflected lattice halves and cross-plane links.
- Transfer-matrix construction diagram.
