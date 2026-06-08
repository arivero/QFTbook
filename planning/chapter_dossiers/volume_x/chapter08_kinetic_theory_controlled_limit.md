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
- `P_+`: positive-energy shell projector; in the invariant pole convention it
  multiplies a Wigner-space collision insertion by `2E_a/Z_a`.
- `f_a(X,p)`: species distribution function from a quasiparticle pole.
- `Gamma_a`: damping width controlling the quasiparticle approximation.
- `tau_qp`, `tau_coll`, `tau_mem`, `tau_X`: microscopic oscillation time,
  damping/mean-free time, connected-kernel memory time, and macroscopic
  variation scale.
- `epsilon_width`, `epsilon_grad`, `epsilon_off`, `epsilon_corr`: finite
  width, memory-gradient, off-shell-tail, and closure residual parameters.
- `eta_a`: statistics sign, `+1` for bosons and `-1` for fermions.
- `C_a`, `C_a^(t)`: covariant and coordinate-time collision terms.
- `W_ab;cd`: covariant transition weight including shell-projection,
  symmetry, ordered/quotient measure, spin/color, and regulator data.
- `M_ab_to_cd`: on-shell scattering amplitude in the scattering-volume
  normalization, before finite kinetic-convention factors are assigned to
  `W_ab;cd`.
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
2. The invariant quasiparticle pole expands with a \(1/(2E_a)\) mass-shell
   Jacobian.  The positive-shell projector for the Wigner collision insertion
   is \(2E_a/Z_a\), not \(1/Z_a\).
3. The covariant Boltzmann equation is \(p^\mu\partial_\mu f_a=C_a[f]\);
   the coordinate-time collision term is \(C_a^{(t)}=C_a/E_a\).
4. The \(2\to2\) collision kernel carries the invariant measure,
   transition-weight convention, physical-channel/symmetry-factor data, and
   Bose/Fermi factors displayed in the chapter.
5. In weak scalar \(\lambda\phi^4\), the \(\lambda_R^2\) sunset term in the
   Schwinger--Keldysh 2PI truncation produces the displayed \(2\to2\)
   gain/loss kernel after the full positive/negative-energy real-scalar
   Wightman ansatz is used, one internal cut line is crossed into the incoming
   partner, the \(1/3!\) sunset combinatorics leaves the identical-final
   divisor, and Wigner expansion, quasiparticle projection, Markovization, and
   closure of connected higher correlations are imposed.  In the full-product
   measure convention the scalar covariant kernel carries
   \(\lambda_R^2/4\).
6. The identity \(1+\eta f=e^{\beta(-u_\mu p^\mu-\mu q)}f\), together with
   energy-momentum and charge conservation, proves detailed balance.
   The local-equilibrium collision term vanishes pointwise at fixed \(X\);
   gradients source the streaming term, not the local collision term.
7. The kinetic entropy current has nonnegative divergence for nonnegative,
   channelwise microreversible transition weights because the symmetrized
   \(2\to2\) integrand is \((X-Y)\log(X/Y)\ge0\).  With the chapter's
   \(2d\Pi\) entropy-current normalization and transition-measure convention,
   the symmetrized continuum coefficient is \(1/2\); in the scalar
   full-product convention \(\mathcal W=\lambda_R^2/4\), the ordered
   four-particle coefficient is \(\lambda_R^2/8\).  Nonmicroreversible
   effective networks require a separate KMS/unitarity argument.
8. Stress-tensor and current Ward identities are the collision-invariant
   moments of the Boltzmann equation.
9. The linearized collision operator is positive on the inner product
   weighted by \(f^{(0)}(1+\eta f^{(0)})\), with quadratic form
   \((\chi_1+\chi_2-\chi_3-\chi_4)^2\).
10. The null space of the linearized operator is spanned by conserved
   collision invariants under the stated connectivity hypothesis.
11. The finite reversible collision datum proves the algebraic core of the
   continuum formulas: additive conserved quantities are preserved, entropy
   production is \(\sum_r w_r(L_r-G_r)\log(L_r/G_r)\ge0\), and the
   linearized entropy production is a positive sum of squares.
12. The scalar derivation carries a weighted \(L^1\) residual target for
    gradients, finite width, off-shell spectral tails, memory, and connected
    correlation closure.  The target requires explicit Lipschitz, weighted
    moment, noncancellation, and finite-time hypotheses; the chapter records
    it as a controlled-approximation ledger rather than a proved theorem.
13. The relaxation-time worked example gives
   \(\eta_{\rm RTA}=4p_{\rm therm}\tau_R/5\) for one massless classical
   species in three spatial dimensions, as a controlled model on the shear
   subspace.
14. Gauge-theory kinetic theory requires matching hard quasiparticles,
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
- 2026-06-08 issues #886/#887 pass: repaired the invariant shell
  normalization and scalar collision-measure convention by adding the
  \(1/(2E)\) pole Jacobian, the \(2E/Z\) shell projector, the
  \(\lambda_R^2/2\) scalar self-energy weight, the \(\lambda_R^2/4\)
  covariant full-product collision weight, and an explicit transition measure
  whose channelwise H theorem assumes microreversibility.
- 2026-06-08 issue #925 pass: corrected the symmetrized H-theorem coefficient
  from \(1/4\) to \(1/2\) with the \(2d\Pi\) entropy-current factor retained,
  stated that initial/final pair divisors are already part of the transition
  weight or measure convention, and added the scalar \(\lambda_R^2/8\)
  specialization plus a finite prefactor regression check.

## Calculation Checks

- `calculation-checks/kinetic_theory_checks.py` verifies the corrected scale
  hierarchy, detailed balance, the H-theorem integrand, invariant shell
  Jacobian, \(2E/Z\) projector, transition-measure microreversibility,
  force-free quasiparticle drift projection, local-equilibrium
  collision-versus-streaming separation, the full Wightman energy-sign
  reversal, the crossed scalar cut-sunset gain/loss kernel, the
  positive-frequency-only negative control, the sunset combinatoric
  normalization, full-product versus quotient identical-final measure
  equivalence, exact finite reversible-collision detailed balance, exact
  finite linearized-rate algebra, finite collision-invariant algebra,
  the entropy-current-derived H-theorem prefactor with a rejected \(1/4\)
  negative control, linearized collision positivity and null vectors, dimensionful
  Markov-memory and pinch-enhancement bookkeeping, and the relaxation-time
  shear-viscosity integral.

## Figure Ledger

No figure is included in this pass.  Future figures should show the hierarchy
from spectral peak to Wigner distribution, a `2 to 2` collision, and the
moment map from kinetic theory to hydrodynamics.
