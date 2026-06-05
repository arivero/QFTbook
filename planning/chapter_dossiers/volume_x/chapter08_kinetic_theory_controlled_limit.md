# Chapter 08: Kinetic Theory As A Controlled Limit

## Source Position

Volume X develops kinetic theory as the controlled quasiparticle bridge
between real-time thermal QFT and hydrodynamics.  This chapter now defines
the on-shell measure and collision kernel precisely, derives detailed
balance and the entropy inequality, identifies hydrodynamic Ward identities
as collision-invariant moments, derives one weak-scalar collision kernel from
a declared Schwinger--Keldysh/2PI sunset truncation, and explains how
transport coefficients arise from the inverse linearized collision operator.

## Notation Inventory

- `D=d+1`: spacetime and spatial dimensions.
- `p^mu=(E_a,p)`, `E_a(p)`: on-shell momentum and energy.
- `dPi_a`: Lorentz-invariant on-shell measure
  \(d^d p/((2\pi)^d2E_a)\).
- `f_a(X,p)`: species distribution function from a quasiparticle pole.
- `Gamma_a`: damping width controlling the quasiparticle approximation.
- `tau_qp`, `tau_coll`, `tau_mem`, `tau_X`: microscopic oscillation time,
  damping/mean-free time, connected-kernel memory time, and macroscopic
  variation scale.
- `epsilon_width`, `epsilon_grad`, `epsilon_off`, `epsilon_corr`: finite
  width, memory-gradient, off-shell-tail, and closure residual parameters.
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
- `Phi_2`, `Sigma^<`, `Sigma^>`: weak-scalar 2PI sunset functional and
  lesser/greater cut self-energies.
- `mathcal G^<`, `mathcal G^>`: real cut Wightman functions \(iG^{<,>}\)
  with both positive- and negative-energy branches.
- `Delta_K`: Markov-memory difference between the nonlocal memory integral
  and its local zeroth-moment approximation.

## Claim Ledger

1. A phase-space density is the coefficient of a positive-energy
   quasiparticle pole in a Wigner-transformed two-point function, under the
   narrow-width and slow-variation hypotheses.  The scale assumptions are
   separated: \(\Gamma/E\ll1\) for the spectral peak,
   \(\tau_{\rm mem}/\tau_X\ll1\) for Markov gradients, and regime-specific
   relations between \(\tau_X\) and \(\tau_{\rm coll}\).
2. The covariant Boltzmann equation is \(p^\mu\partial_\mu f_a=C_a[f]\);
   the coordinate-time collision term is \(C_a^{(t)}=C_a/E_a\).
3. The \(2\to2\) collision kernel carries the invariant measure,
   physical-channel/symmetry-factor convention, and Bose/Fermi factors
   displayed in the chapter.
4. In weak scalar \(\lambda\phi^4\), the \(\lambda_R^2\) sunset term in the
   Schwinger--Keldysh 2PI truncation produces the displayed \(2\to2\)
   gain/loss kernel after the full positive/negative-energy real-scalar
   Wightman ansatz is used, one internal cut line is crossed into the incoming
   partner, the \(1/3!\) sunset combinatorics is reduced to the physical
   channel, and Wigner expansion, quasiparticle projection, Markovization, and
   closure of connected higher correlations are imposed.
5. The identity \(1+\eta f=e^{\beta(-u_\mu p^\mu-\mu q)}f\), together with
   energy-momentum and charge conservation, proves detailed balance.
   The local-equilibrium collision term vanishes pointwise at fixed \(X\);
   gradients source the streaming term, not the local collision term.
6. The kinetic entropy current has nonnegative divergence because the
   symmetrized \(2\to2\) integrand is
   \((X-Y)\log(X/Y)\ge0\).
7. Stress-tensor and current Ward identities are the collision-invariant
   moments of the Boltzmann equation.
8. The linearized collision operator is positive on the inner product
   weighted by \(f^{(0)}(1+\eta f^{(0)})\), with quadratic form
   \((\chi_1+\chi_2-\chi_3-\chi_4)^2\).
9. The null space of the linearized operator is spanned by conserved
   collision invariants under the stated connectivity hypothesis.
10. The finite reversible collision datum proves the algebraic core of the
   continuum formulas: additive conserved quantities are preserved, entropy
   production is \(\sum_r w_r(L_r-G_r)\log(L_r/G_r)\ge0\), and the
   linearized entropy production is a positive sum of squares.
11. The scalar derivation carries a weighted \(L^1\) residual target for
    gradients, finite width, off-shell spectral tails, memory, and connected
    correlation closure.  The target requires explicit Lipschitz, weighted
    moment, noncancellation, and finite-time hypotheses; the chapter records
    it as a controlled-approximation ledger rather than a proved theorem.
12. The relaxation-time worked example gives
   \(\eta_{\rm RTA}=4p_{\rm therm}\tau_R/5\) for one massless classical
   species in three spatial dimensions, as a controlled model on the shear
   subspace.
13. Gauge-theory kinetic theory requires matching hard quasiparticles,
    soft collective gauge fields, and ultrasoft hydrodynamic modes in a
    common regulator and source convention.

## Anti-Wrapper Audit

- 2026-05-29 ninth pass: retained the finite collision H-theorem and
  linearized collision propositions as substantive finite models, but expanded
  the proofs to state the open-domain hypothesis for logarithms, the
  Bose/Fermi/classical derivative convention, the reactionwise positivity
  argument, and the exact identification of the linearized null space with
  collision invariants.
- 2026-06-04 issue #787 pass: corrected the collapsed
  \(\Gamma\ell_{\rm variation}\) hierarchy into distinct quasiparticle,
  damping, memory, kinetic-relaxation, and hydrodynamic scales; added the
  weak scalar Schwinger--Keldysh/2PI sunset derivation of the \(2\to2\)
  collision kernel; fixed the local-equilibrium collision-versus-streaming
  wording; and promoted `kinetic_theory_checks.py` to a high-risk evidence
  contract with scalar-kernel, Markov, pinch, and residual negative controls.
- 2026-06-05 issue #815 pass: repaired the scalar 2PI-to-Boltzmann derivation
  by replacing the positive-frequency-only cut ansatz with the full
  positive/negative-energy real-scalar Wightman ansatz, deriving the crossed
  \(p_1+p_2=p_3+p_4\) assignment from the negative-energy internal line,
  spelling out the \(1/3!\) sunset combinatorics and physical-channel
  normalization, adding the local mass/field-strength/coupling/2PI
  renormalization datum, correcting the Markov-memory estimate to a
  dimensionful absolute bound plus a conditional relative bound, and demoting
  the weighted residual inequality to a controlled-approximation target.

## Calculation Checks

- `calculation-checks/kinetic_theory_checks.py` verifies the corrected scale
  hierarchy, detailed balance, the H-theorem integrand, force-free
  quasiparticle drift projection, local-equilibrium collision-versus-streaming
  separation, the full Wightman energy-sign reversal, the crossed scalar
  cut-sunset gain/loss kernel, the positive-frequency-only negative control,
  the sunset combinatoric normalization, exact finite reversible-collision
  detailed balance, exact finite linearized-rate algebra, finite
  collision-invariant algebra, linearized collision positivity and null
  vectors, dimensionful Markov-memory and pinch-enhancement bookkeeping, and
  the relaxation-time shear-viscosity integral.

## Figure Ledger

No figure is included in this pass.  Future figures should show the hierarchy
from spectral peak to Wigner distribution, a `2 to 2` collision, and the
moment map from kinetic theory to hydrodynamics.
