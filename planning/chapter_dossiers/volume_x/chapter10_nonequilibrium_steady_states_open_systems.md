# Chapter 10: Nonequilibrium Steady States And Open-System Limits

## Source Position

Volume X follows anomalous transport with nonequilibrium steady-state and
open-system definitions needed for later thermal, hydrodynamic, and curved
real-time topics.  The chapter now treats steady states as invariant
positive functionals, reservoir steady states as local weak limits, and
open-system dynamics as weak-coupling limits of larger closed systems.

## Notation Inventory

- `A`, `tau_t`, `omega_ss`: observable algebra, time evolution, and steady
  state.
- `beta_L`, `beta_R`, `mu_L`, `mu_R`: reservoir thermodynamic parameters.
- `J_E`, `J_Q`, `dot S_res`: energy current, charge current, and reservoir
  entropy production.
- `X`, `L`: thermodynamic-force vector and Onsager matrix in linear
  response.
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
5. In the weak-coupling Markovian limit, the bath spectral matrix
   \(\gamma_{ab}(\omega)\) is positive by the positive-type/Bochner
   argument and yields the Davies/GKSL generator after the van Hove and
   secular limits.
6. The GKSL form preserves trace, preserves Hermiticity, and generates a
   completely positive semigroup; the proof diagonalizes the positive bath
   spectral matrices and constructs the finite-time map by the
   Dyson-Phillips jump expansion.
7. KMS bath spectral functions obey detailed balance; the chapter verifies
   the sign and index order by spectral resolution and applies the result to
   the Gibbs stationary ratio for a two-level system.
8. The quadratic Schwinger-Keldysh influence action has explicitly defined
   retarded and noise kernels; KMS relates them by fluctuation-dissipation.
9. For a Markovian relaxing hydrodynamic density, the Fokker-Planck
   stationary-current computation with the stationary Gaussian
   equilibrium weight fixes \(D_n=\gamma\chi T\) and hence
   \(\langle\xi\xi\rangle=2\gamma\chi T\,\delta\).
10. Continuum QFT constructions must specify the order of long-time,
    thermodynamic, weak-coupling, Markovian, hydrodynamic, and continuum
    limits.

## Calculation Checks

- `calculation-checks/nonequilibrium_open_system_checks.py` verifies the
  reservoir entropy formula, GKSL trace preservation, KMS detailed balance
  for a two-level system, Ornstein-Uhlenbeck noise normalization, and
  positive noise-kernel algebra.

## Figure Ledger

No figure is included in this pass.  Future figures should include reservoir
joining, Keldysh influence contours, and relaxation/noise flow diagrams.
