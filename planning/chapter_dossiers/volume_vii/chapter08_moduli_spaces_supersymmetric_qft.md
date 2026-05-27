# Chapter 08: Moduli Spaces In Supersymmetric Quantum Field Theory

## Source Position

Volume VII now separates supersymmetric vacuum spaces from the earlier exact
Wilsonian dynamics.  The chapter supplies moduli-space definitions before the
later lower-dimensional examples, protected sectors, and localization.

## Notation Inventory

- `Phi^i`, `W`, `F_i`, `mu`: chiral fields, superpotential, F-term equations,
  and moment map.
- `V`, `G_C`, `Z_F`, `I_F`: scalar representation, complexified reductive
  gauge group, F-flat locus, and F-term ideal.
- `M_cl`: classical Kahler or holomorphic quotient vacuum space.
- `M_ch,cl`, `M_mu,cl`: affine chiral quotient and symplectic vacuum
  quotient.
- `M`, `H_p`, `A_p`, `G_p`: quantum moduli space, Hilbert space, local
  operator algebra, and background response in vacuum `p`.
- `R_ch`, `ev_p`: chiral ring and evaluation homomorphism at a vacuum.
- `M_H`, `mu_R`, `mu_C`: hyperkahler quotient and real/complex moment maps.
- `g_{i bar j}`: branch metric in the low-energy effective action.
- `q_i`, `tilde q_i`: rank-one \(U(1)\) hypermultiplet coordinates with
  charges \(+1\) and \(-1\).
- `z_i^(a)`, `p_i^(a)`: local base and cotangent coordinates on the
  \(q_a\neq0\) patch of the rank-one hyperkahler quotient.
- `zeta`: positive real FI parameter in the rank-one hypermultiplet model.
- `Theta`: holomorphic cotangent one-form \(\sum_i\tilde q_i\,dq_i\).
- `prop:n2-rank-one-hyperkahler-quotient`: explicit construction of the
  rank-one \(U(1)\) hypermultiplet Higgs branch as
  \(T^\ast\mathbb P^{N-1}\), including dimension, local coordinates, moment
  map solving, and one-form descent.

## Claim Ledger

- Defines classical supersymmetric vacuum equations and quotient data.
- States the precise affine chiral quotient and symplectic quotient data and
  proves their coordinate-ring comparison under explicit Kempf-Ness
  hypotheses.
- Works out the rank-one abelian quotient
  `C[x,y]^{C^*}=C[xy]` and its moment-map quotient, fixing the quotient
  convention used later in rank-one gauge-theory examples.
- Defines quantum moduli spaces as vacuum families together with low-energy
  Hilbert, operator, metric, and background-response data.
- Relates chiral rings to holomorphic functions under explicit separation and
  reducedness hypotheses.
- Records `N=1` SQCD branch behavior and `N=2` Coulomb/Higgs/mixed branch
  structures.
- Proves the rank-one \(\mathcal N=2\) hypermultiplet quotient
  \(\{\mu_C=0,\mu_R=\zeta\}/U(1)\simeq T^\ast\mathbb P^{N-1}\) for
  \(\zeta>0\), including the elementary real-moment representative,
  local cotangent coordinates, and preservation of the canonical holomorphic
  one-form on overlaps.
- Identifies singularities as loci where the low-energy theory changes and
  records the domain of validity of branch effective actions.

## Calculation Checks

- `calculation-checks/susy_moduli_space_checks.py` verifies the rank-one
  abelian invariant-ring calculation, the matching real/complex quotient
  dimension count, F-term ideal equivariance for an invariant
  superpotential, and the rank-one hyperkahler quotient dimension, one-form
  descent, and cotangent transition algebra for \(T^\ast\mathbb P^{N-1}\).

## Figure Ledger

No figure is included in this pass.  Later figures should show the quotient
construction, SQCD branch cases, and the `N=2` Coulomb branch with singular
local models.
