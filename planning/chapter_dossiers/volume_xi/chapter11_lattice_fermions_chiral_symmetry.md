# Chapter 11: Lattice Fermions And Chiral Symmetry

## Source Position

This chapter follows the constructive, numerical, and lattice-to-continuum
chapters by developing fermionic lattice regulators at the finite Berezin
algebra level.  It incorporates the useful content of
`references/lattice fermion.tex`: mid-link reflection is the viable free
fermion reflection, site and diagonal reflections fail elementary two-point
tests, and the two-dimensional staggered Thirring interaction is
reflection-positive for \(U\geq0\).

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
- `B_times`, `F_j`, `c_j`: reflection-positive crossing factor data.
- `eta(x)`, `bar eta(x)`, `eta_mu(x)`: staggered fermion and staggered
  phase.
- `U`: two-dimensional staggered Thirring coupling.
- `H_W`, `epsilon(H_W)`, `V`: Hermitian Wilson kernel, sign function, and
  overlap unitary.

## Claim Ledger

- Defines the finite lattice fermion path integral as a Berezin functional,
  not as a Borel measure on a set of fermion configurations.
- Proves the finite Berezin Gaussian determinant, propagator, and Wick
  determinant identities.
- Derives the naive massive propagator symbol and proves that the massless
  zeros at Brillouin-zone corners carry chirality signs whose sum vanishes.
- Proves, in the translation-invariant \(D_f=\ii\gamma\cdot f\) setting, the
  degree-theoretic index cancellation on the Brillouin torus.
- Defines the standard spin-scalar Wilson operator and proves the corner
  expansion that gives mass \(m+2rn_\epsilon/a\) to the doublers.
- Defines fermionic mid-link reflection and proves a finite Grassmann
  reflection-positivity criterion from crossing factors
  \(\prod_j(1+c_j\Theta(F_j)F_j)\), \(c_j\geq0\).
- Applies the criterion to the free nearest-neighbor mid-link cut and records
  the one-fermion two-point obstruction for site and diagonal reflections.
- Proves Wilson mid-link reflection positivity at \(r=1\) by decomposing the
  crossing term with \(P_\pm=(1\pm\gamma_0)/2\).
- Defines two-dimensional staggered fermions and proves reflection positivity
  of the staggered Thirring interaction for \(U\geq0\).
- Proves exact invariance of the Ginsparg-Wilson action under Luescher's
  lattice chiral transformation and computes the finite Berezinian giving
  \(\operatorname{index}(D)=\operatorname{Tr}\gamma_5(1-aD/2)\).
- Proves that the overlap operator satisfies the Ginsparg-Wilson relation and
  derives the overlap index as
  \(-\frac12\operatorname{Tr}\operatorname{sign}(H_W)\).
- States the domain-wall/overlap relationship and the locality hypothesis
  needed for the overlap operator in gauge backgrounds.
- Records the continuum ledger for lattice fermion regulators and keeps the
  chiral-gauge lattice construction as an open problem.

## Figure Ledger

- Figure `fig:lattice-fermion-midlink-reflection`: mid-link reflection plane
  and the cross-plane hopping links.

## Calculation Checks

- `calculation-checks/lattice_fermion_chiral_checks.py` verifies the
  finite arithmetic for doubler chirality cancellation, Wilson corner-mass
  degeneracies, Ginsparg-Wilson/overlap algebra, Berezinian index
  normalization, reflection-positive crossing coefficients, and staggered
  phase signs.
