# Chapter 11: Lattice Fermions And Chiral Symmetry
Source-File: monograph/tex/volumes/volume_xi/chapter11_lattice_fermions_chiral_symmetry.tex

## Source Position

This chapter follows the constructive, numerical, and lattice-to-continuum
chapters by developing fermionic lattice regulators at the finite Berezin
algebra level.  It incorporates the useful content of
`references/lattice fermion.tex`: the mid-link Wilson construction is the
reflection-positive finite regulator developed here, the earlier site/diagonal
no-go shortcut is not used, and the two-dimensional staggered Thirring
interaction is reflection-positive for \(U\geq0\) after the even crossing block
is typed correctly.

## Notation Inventory

- `Lambda`: finite lattice.
- `psi`, `bar psi`: Grassmann generators.
- `D`: finite lattice Dirac matrix.
- `gamma_mu`, `gamma_5`: Euclidean gamma matrices and chirality matrix.
- `D_naive`, `D_W`, `D_ov`: naive, Wilson, and overlap lattice Dirac
  operators.
- `f_mu(p)`: periodic Brillouin-torus vector field defining a
  translation-invariant massless Dirac symbol.
- `chi(p_*)`: local chirality sign of a doubler zero.
- `epsilon`: Brillouin-zone corner vector in \(\{0,1\}^D\).
- `n_epsilon`: number of nonzero corner components.
- `Theta`: fermionic reflection anti-automorphism.
- `Lambda_+`, `Lambda_-`, `vartheta`: positive/negative half-lattices and
  mid-link reflection.
- `B_times`, `F_j`, `c_j`, `tau_j`: reflection-positive homogeneous-block
  crossing-kernel data and orientation phases.
- `eta(x)`, `bar eta(x)`, `eta_mu(x)`: staggered fermion and staggered
  phase.
- `U`: two-dimensional staggered Thirring coupling.
- `rho`, `A_rho`, `H_W(rho)`, `epsilon_rho`, `V_rho`: overlap/domain-wall
  height, dimensionless massless Wilson kernel, Hermitian Wilson kernel, sign
  function, and overlap unitary.
- `L_s`, `K_rho`, `T_rho`, `epsilon_{L_s}`: fifth-direction extent, transfer
  kernel, transfer matrix, and finite-wall sign-function approximation.

## Claim Ledger

- Defines the finite lattice fermion path integral as a Berezin functional,
  not as a Borel measure on a set of fermion configurations.
- Records the finite Berezin Gaussian determinant, propagator, and Wick
  determinant identities with the fixed Berezin ordering.
- Derives the naive massive propagator symbol and proves that the massless
  zeros at Brillouin-zone corners carry chirality signs whose sum vanishes.
- Proves, in the translation-invariant \(D_f=\ii\gamma\cdot f\) setting, the
  degree-theoretic index cancellation on the Brillouin torus.
- Defines the standard spin-scalar Wilson operator and proves the corner
  expansion that gives mass \(m+2rn_\epsilon/a\) to the doublers.
- Defines fermionic mid-link reflection and proves a finite Grassmann
  reflection-positivity criterion from homogeneous crossing kernels
  \(\prod_j(1+c_j\tau_j\Theta(F_j)F_j)\), \(c_j\geq0\), after explicitly
  recording that the bare Berezin functional is a top-coefficient extractor,
  not an inner product on all positive-time monomials.
- Proves Wilson mid-link reflection positivity at \(r=1\) from the actual
  gauge-covariant cross-plane action, using \(P_\pm=(1\pm\gamma_0)/2\),
  reflection of the time link to its inverse, reflection-invariant boundary
  conditions, and an ordered odd-generator crossing kernel.
- Retracts the unsupported site/diagonal no-go claim: the chapter now states
  that alternative cuts require a complete finite Gram test or a fully
  specified counterexample, because the site-reflection sine numerator cannot
  be discarded at nonzero reflected separation.
- Defines two-dimensional staggered fermions and proves reflection positivity
  of the staggered Thirring interaction for \(U\geq0\) using the even block
  \(F_x=\eta(x)\bar\eta(x)\) in the same homogeneous crossing-kernel cone.
- Proves exact invariance of the Ginsparg-Wilson action under Luescher's
  lattice chiral transformation and computes the finite Berezinian giving
  \(\operatorname{index}(D)=\operatorname{Tr}\gamma_5(1-RD)\), and completes
  the finite spectral proof that this trace equals the chirality difference of
  zero modes, with nonreal paired modes and the \(1/R\) modes separated.
- Chooses the explicit overlap convention
  \(A_\rho=aD_W^{(0)}-\rho\), \(H_W(\rho)=\gamma_5A_\rho\), and
  \(D_{\rm ov}(\rho)=\rho a^{-1}(1+\gamma_5\operatorname{sign}H_W(\rho))\);
  derives the free \(0<\rho<2r\) one-species branch window, unit physical
  slope, doubler lifting, and the double-shift failure mode.
- Separates finite invertibility of \(H_W(\rho)\), locality from an
  admissibility/mobility-gap hypothesis, and the continuum topological-index
  claim.
- Defines the finite-\(L_s\) domain-wall operator, boundary fields,
  Pauli--Villars quotient, transfer matrix, Schur-complement effective
  operator, and residual sign-function bound giving convergence to the overlap
  operator under a spectral-gap hypothesis.
- Records the continuum ledger for lattice fermion regulators and keeps the
  chiral-gauge lattice construction as an open problem.

## Figure Ledger

- Figure `fig:lattice-fermion-midlink-reflection`: mid-link reflection plane
  and the cross-plane hopping links.

## Calculation Checks

- `calculation-checks/lattice_fermion_chiral_checks.py` verifies the
  finite arithmetic for doubler chirality cancellation, Wilson corner-mass
  degeneracies, Ginsparg-Wilson/overlap algebra, Berezinian index
  normalization, equality of the Ginsparg-Wilson trace with zero-mode
  chirality, exhaustive one- and two-link Grassmann crossing-kernel Gram
  matrices, wrong-sign and wrong-phase reflection-positive negative controls,
  Wilson \(r=1\) projector crossing coefficients with a naive \(r=0\) negative
  control, the overlap branch window and double-shift rejection, finite-wall
  domain-wall sign-function convergence, and staggered phase signs.

## Audit Notes

- 2026-05-29 eighth anti-wrapper pass: strengthened the Ginsparg-Wilson
  Berezinian proposition by adding \(\gamma_5\)-Hermiticity to the statement
  and proving integrality from the Hermitian involution
  \(\widehat\gamma_5=\gamma_5(1-aD)\), rather than leaving the trace formula
  as a formal finite calculation.
- 2026-05-29 eighth anti-wrapper pass: demoted the finite Berezin Gaussian
  determinant/propagator/Wick identities from proposition form to algebra
  prose, preserving the source-completion derivation and the ordering
  convention.
- 2026-06-08 fermion reflection/overlap rebuild: replaced the false
  \(\int\Theta(e_A)e_B=\delta_{AB}\) Berezin-pairing step by a homogeneous
  crossing-kernel saturation lemma, corrected the even staggered-Thirring
  block, derived Wilson \(r=1\) positivity from the actual gauge-covariant
  cross-plane action, retracted the unsupported site/diagonal cut no-go,
  fixed the overlap kernel convention to a single \(A_\rho=aD_W^{(0)}-\rho\)
  shift, completed the GW spectral index proof, and added a finite
  domain-wall transfer-matrix/residual-mass derivation.
