# Volume X, Chapter 2 Dossier: Finite-Temperature Path Integrals

## Source Position

This chapter sits between the algebraic KMS formulation and the real-time
Schwinger--Keldysh construction.  Its role is to derive the Euclidean thermal
circle, spin structures, Matsubara modes, spectral continuation problem, and
chemical-potential twists directly from the Gibbs trace at finite regulator.
It keeps the field-theory path integral subordinate to the regulated operator
or constructive definition.

## Notation Inventory

- `H`: self-adjoint Hamiltonian bounded below.
- `beta`: inverse temperature.
- `Z(beta)`: finite-volume Gibbs partition function.
- `omega_beta`: Gibbs state.
- `A_E(tau)`: Euclidean-time translate of an operator.
- `K_epsilon(qprime,q)`: short Euclidean-time coordinate kernel.
- `S^1_beta`: Euclidean thermal circle of circumference `beta`.
- `eta`, `bareta`: fermionic coherent-state Grassmann variables.
- `s`: thermal boundary sign, `+1` for bosons and `-1` for thermal fermions.
- `omega_n^B`, `omega_n^F`: bosonic and fermionic Matsubara frequencies.
- `rho_AB(omega)`: finite-volume thermal spectral distribution.
- `Q`, `mu`, `q`: conserved global charge, chemical potential, and charge of
  an operator or field.
- `P(x)`: thermal gauge holonomy/Polyakov loop.

## Claim Ledger

1. Defines Euclidean thermal correlators as trace insertions of
   \(A_E(\tau)=e^{\tau H}Ae^{-\tau H}\) under trace-class finite-volume
   hypotheses.
2. Proves that trace cyclicity identifies the two KMS strip boundary values
   and produces the Euclidean thermal circle.
3. Derives bosonic periodic boundary conditions from time slicing of the
   coordinate trace.
4. States and proves the finite-dimensional fermionic coherent-state trace
   identity, including the minus sign responsible for antiperiodic thermal
   fermions.
5. Derives bosonic and fermionic Matsubara frequencies as eigenvalues on
   \(S^1_\beta\) with specified spin structure.
6. Proves the free scalar thermal Green function by Fourier inversion of
   \(-\partial_\tau^2-\Delta+m^2\) on the thermal circle.
7. Derives the finite-volume bosonic thermal spectral representation,
   including the separate zero-frequency degenerate contribution, and the
   Matsubara Cauchy-transform formula.
8. States the analytic-continuation problem precisely: retarded functions
   require a spectral distribution and growth hypotheses, not only discrete
   Matsubara values.
9. Derives chemical potential as either \(D_\tau\mapsto D_\tau-\mu q\) or a
   twisted boundary condition.
10. Separates fixed global background holonomies from dynamical gauge
    holonomy integration on the thermal circle.

## Calculation Checks

- `calculation-checks/finite_temperature_path_integral_checks.py` verifies
  Matsubara boundary phases, the finite-volume spectral representation,
  the separate Euclidean zero mode, the Matsubara Cauchy transform, and
  chemical-potential twist bookkeeping.

## Figure Ledger

No figure is included in this pass.  A later figure may show trace gluing
around \(S^1_\beta\), with separate bosonic periodic and fermionic
antiperiodic spin structures.
