# Chapter 08: Kinetic Theory As A Controlled Limit

## Source Position

Volume X develops kinetic theory as the controlled quasiparticle bridge
between real-time thermal QFT and hydrodynamics.  This chapter now defines
the on-shell measure and collision kernel precisely, derives detailed
balance and the entropy inequality, identifies hydrodynamic Ward identities
as collision-invariant moments, and explains how transport coefficients
arise from the inverse linearized collision operator.

## Notation Inventory

- `D=d+1`: spacetime and spatial dimensions.
- `p^mu=(E_a,p)`, `E_a(p)`: on-shell momentum and energy.
- `dPi_a`: Lorentz-invariant on-shell measure
  \(d^d p/((2\pi)^d2E_a)\).
- `f_a(X,p)`: species distribution function from a quasiparticle pole.
- `Gamma_a`: damping width controlling the quasiparticle approximation.
- `eta_a`: statistics sign, `+1` for bosons and `-1` for fermions.
- `C_a`, `C_a^(t)`: covariant and coordinate-time collision terms.
- `M_ab_to_cd`: on-shell scattering amplitude in the scattering-volume
  normalization.
- `S_kin^mu`: kinetic entropy current.
- `T^{mu nu}`, `J_A^mu`: kinetic stress tensor and conserved current.
- `L_ab`: linearized collision operator.
- `tau_R`: relaxation time in the explicitly marked controlled
  approximation.
- `I`, `R`, `nu_r`: finite one-particle cell set, reversible reaction set,
  and stoichiometric vector in the finite collision algebra.
- `L_r`, `G_r`, `M_r`: loss product, gain product, and equilibrium reaction
  weight for a finite reversible collision.

## Claim Ledger

1. A phase-space density is the coefficient of a positive-energy
   quasiparticle pole in a Wigner-transformed two-point function, under the
   narrow-width and slow-variation hypotheses.
2. The covariant Boltzmann equation is \(p^\mu\partial_\mu f_a=C_a[f]\);
   the coordinate-time collision term is \(C_a^{(t)}=C_a/E_a\).
3. The \(2\to2\) collision kernel carries the invariant measure and
   Bose/Fermi factors displayed in the chapter.
4. The identity \(1+\eta f=e^{\beta(-u_\mu p^\mu-\mu q)}f\), together with
   energy-momentum and charge conservation, proves detailed balance.
5. The kinetic entropy current has nonnegative divergence because the
   symmetrized \(2\to2\) integrand is
   \((X-Y)\log(X/Y)\ge0\).
6. Stress-tensor and current Ward identities are the collision-invariant
   moments of the Boltzmann equation.
7. The linearized collision operator is positive on the inner product
   weighted by \(f^{(0)}(1+\eta f^{(0)})\), with quadratic form
   \((\chi_1+\chi_2-\chi_3-\chi_4)^2\).
8. The null space of the linearized operator is spanned by conserved
   collision invariants under the stated connectivity hypothesis.
9. The finite reversible collision datum proves the algebraic core of the
   continuum formulas: additive conserved quantities are preserved, entropy
   production is \(\sum_r w_r(L_r-G_r)\log(L_r/G_r)\ge0\), and the
   linearized entropy production is a positive sum of squares.
10. The relaxation-time worked example gives
   \(\eta_{\rm RTA}=4p_{\rm therm}\tau_R/5\) for one massless classical
   species in three spatial dimensions, as a controlled model on the shear
   subspace.
11. Gauge-theory kinetic theory requires matching hard quasiparticles,
    soft collective gauge fields, and ultrasoft hydrodynamic modes in a
    common regulator and source convention.

## Anti-Wrapper Audit

- 2026-05-29 ninth pass: retained the finite collision H-theorem and
  linearized collision propositions as substantive finite models, but expanded
  the proofs to state the open-domain hypothesis for logarithms, the
  Bose/Fermi/classical derivative convention, the reactionwise positivity
  argument, and the exact identification of the linearized null space with
  collision invariants.

## Calculation Checks

- `calculation-checks/kinetic_theory_checks.py` verifies detailed balance,
  the H-theorem integrand, exact finite reversible-collision detailed
  balance, exact finite linearized-rate algebra, finite collision-invariant
  algebra, linearized collision positivity and null vectors, and the
  relaxation-time shear-viscosity integral.

## Figure Ledger

No figure is included in this pass.  Future figures should show the hierarchy
from spectral peak to Wigner distribution, a `2 to 2` collision, and the
moment map from kinetic theory to hydrodynamics.
