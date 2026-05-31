# Chapter 10: Nonequilibrium Steady States And Open-System Limits

## Source Position

Volume X follows anomalous transport with nonequilibrium steady-state and
open-system definitions needed for later thermal, hydrodynamic, and curved
real-time topics.  The chapter now treats steady states as invariant
positive functionals, reservoir steady states as local weak limits, finite
fluctuation relations as path-measure Radon--Nikodym identities, and
finite-step Langevin/MSRJD variables as exact Fourier rewritings of finite
Gaussian transition kernels.  Open-system dynamics is then treated as a
weak-coupling limit of larger closed systems.

## Notation Inventory

- `A`, `tau_t`, `omega_ss`: observable algebra, time evolution, and steady
  state.
- `beta_L`, `beta_R`, `mu_L`, `mu_R`: reservoir thermodynamic parameters.
- `J_E`, `J_Q`, `dot S_res`: energy current, charge current, and reservoir
  entropy production.
- `X`, `L`: thermodynamic-force vector and Onsager matrix in linear
  response.
- `gamma`, `Theta gamma`, `P_F`, `P_R`, `Sigma`: finite labelled trajectory,
  time-reversed trajectory, forward/reversed path measures, and trajectory
  entropy production.
- `W_ext`, `Delta F`: protocol work and finite free-energy difference in the
  Jarzynski specialization.
- `x_n`, `Delta x_n`, `F_n`, `eta_n`, `D`, `hat x_n`: finite-regulator
  Langevin variables, increments, drift, Gaussian noise covariance, and
  MSRJD Fourier-dual variables.
- `H_S`, `H_E`, `S_a`, `E_a`: system/environment Hamiltonians and couplings.
- `gamma_ab(omega)`: bath spectral matrix.
- `S_a(omega)`: Bohr-frequency component of a system coupling operator.
- `L`, `L_alpha`: Markov generator and Lindblad jump operators; context
  distinguishes this from the Onsager matrix.
- `Gamma`, `H_eff`, `K_t`, `J`: total jump rate operator,
  non-Hermitian effective Hamiltonian, no-jump map, and jump map in the
  finite-dimensional GKSL proof.
- `S_IF`, `phi_r`, `phi_a`, `D_R`, `N`: influence functional, Keldysh
  variables, retarded kernel, and noise kernel.
- `gamma`, `chi`, `D_n`: relaxation rate, susceptibility, and homogeneous
  Ornstein-Uhlenbeck noise strength.

## Claim Ledger

1. A steady state is a positive normalized functional invariant under the
   real-time automorphism group.
2. Reservoir nonequilibrium steady states are local weak limits of
   long-time evolved observables near the junction.
3. With currents positive from left to right, reservoir entropy production is
   \[
     \dot S_{\rm res}
     =(\beta_R-\beta_L)J_E
     -(\beta_R\mu_R-\beta_L\mu_L)J_Q.
   \]
4. In linear response, \(\dot S_{\rm res}=X^TLX\), so positivity is
   equivalent to positive semidefiniteness of the symmetric Onsager matrix.
5. Finite fluctuation relations are path-measure statements: after specifying
   the labelled trajectory space, reversed protocol, and absolute-continuity
   condition, the trajectory entropy production is a Radon--Nikodym logarithm.
6. The finite path-measure identity gives
   \(\langle e^{-\Sigma}\rangle=1\); with thermal local detailed balance and
   Gibbs endpoint distributions it becomes the Jarzynski identity
   \(\langle e^{-\beta W_{\rm ext}}\rangle=e^{-\beta\Delta F}\).
7. A finite-step Ito Langevin process with covariance
   \(2\Delta t\,D\) has an exactly normalized Gaussian transition density.
   Its MSRJD response-field representation is the Fourier transform of that
   transition density at each time step, with \(\hat x_n\) the Fourier-dual
   variable to \(\Delta x_n-\Delta t F_n\).
8. The generator \(L_t=F^a\partial_a+D^{ab}\partial_a\partial_b\) and the
   Fokker-Planck adjoint equation follow from the finite-step moments before
   a continuum stochastic-field limit is taken.
9. In the weak-coupling Markovian limit, the bath spectral matrix
   \(\gamma_{ab}(\omega)\) is positive by the positive-type/Bochner
   argument and yields the Davies/GKSL generator after the van Hove and
   secular limits.
10. The GKSL form preserves trace, preserves Hermiticity, and generates a
   completely positive semigroup; the proof diagonalizes the positive bath
   spectral matrices and constructs the finite-time map by the
   Dyson-Phillips jump expansion.
11. KMS bath spectral functions obey detailed balance; the chapter verifies
   the sign and index order by spectral resolution and applies the result to
   the Gibbs stationary ratio for a two-level system.
12. The quadratic Schwinger-Keldysh influence action has explicitly defined
   retarded and noise kernels; KMS relates them by fluctuation-dissipation.
13. For a Markovian relaxing hydrodynamic density, the Fokker-Planck
   stationary-current computation with the stationary Gaussian
   equilibrium weight fixes \(D_n=\gamma\chi T\) and hence
   \(\langle\xi\xi\rangle=2\gamma\chi T\,\delta\).
14. Continuum QFT constructions must specify the order of long-time,
    thermodynamic, weak-coupling, Markovian, hydrodynamic, and continuum
    limits.

## Calculation Checks

- `calculation-checks/nonequilibrium_open_system_checks.py` verifies the
  reservoir entropy formula, GKSL trace preservation, KMS detailed balance
  for a two-level system, Ornstein-Uhlenbeck noise normalization, and
  positive noise-kernel algebra.  It also verifies the cancellation of
  waiting-time factors in the finite path-measure entropy-production ratio
  and the driven two-state Jarzynski identity, together with the determinant
  normalization in the finite-step MSRJD Fourier kernel and the Langevin
  generator expansion on a cubic test function.

## Figure Ledger

No figure is included in this pass.  Future figures should include reservoir
joining, Keldysh influence contours, and relaxation/noise flow diagrams.

## Audit Notes

- 2026-05-31 statmech crosswalk/#703 pass: added finite trajectory
  probability measures and fluctuation relations as regulator-level
  Radon--Nikodym identities, before any continuum QFT or Schwinger--Keldysh
  formal path-integral language is invoked.
- 2026-05-31 finite-step MSRJD pass: added the exact finite-dimensional
  Gaussian/Fourier derivation of response-field variables and the
  finite-step generator calculation before continuum stochastic-field
  language is used.
