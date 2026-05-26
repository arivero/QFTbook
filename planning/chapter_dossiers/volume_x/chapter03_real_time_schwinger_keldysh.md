# Volume X, Chapter 3 Dossier: Real-Time Schwinger--Keldysh Formalism

## Source Position

This chapter follows the Euclidean thermal path-integral derivation and
precedes spectral/Kubo and hydrodynamic effective-action chapters.  Its role
is to derive the real-time closed-time-path formalism as a finite operator
identity before introducing any coordinate path integral.  It supplies the
normalization, reality, positivity, retarded-response, and KMS constraints
used later in transport and hydrodynamic effective actions.

## Notation Inventory

- `Hilb`: finite or regulated Hilbert space.
- `H`: self-adjoint Hamiltonian.
- `rho_0`: positive trace-class initial density operator.
- `O_alpha`: Hermitian operators coupled to sources, with Greek labels used
  to avoid collision with the SK difference branch.
- `J_+`, `J_-`: forward and backward branch sources.
- `H_J(t)`: source-dependent Hamiltonian `H - J^alpha O_alpha`.
- `U_J(t_f,t_i)`: source-dependent time-evolution operator.
- `Z[J_+,J_-]`: closed-time-path generating functional.
- `W[J_r,J_a]`: connected Schwinger--Keldysh functional `-i log Z`.
- `J_r`, `J_a`: average and difference sources; the monograph writes these
  as roman subscripts `J_{\mathrm r}` and `J_{\mathrm a}` in formulas.
- `G^>`, `G^<`: greater and lesser two-point functions.
- `K^R`: physical source-response kernel for the convention
  `H-J^alpha O_alpha`.
- `G^{R,comm}`, `G^{A,comm}`, `G^K`: commutator-retarded, commutator-advanced,
  and Keldysh fluctuation functions.
- `Phi_+`, `Phi_-`, `Phi_+^*`, `Phi_-^*`: doubled BV fields and antifields.

## Claim Ledger

1. Defines the closed-time-path generating functional
   \(Z[J_+,J_-]=\operatorname{Tr}(U_{J_+}\rho_0U_{J_-}^\dagger)\) for a
   finite or regulated system.
2. Derives one- and two-point contour derivative formulae, including the
   signs from forward versus backward source insertions.
3. Proves \(Z[J,J]=1\), branch-exchange reality
   \(Z[J_+,J_-]^*=Z[J_-,J_+]\), and the positivity bound \(|Z|\le1\).
4. Converts these constraints to \(W=-i\log Z\), including
   \(\operatorname{Im}W\ge0\) near the origin.
5. Defines \(r/a\) sources and proves that
   \(\delta W/\delta J_{\mathrm a}\) gives the physical one-point function.
6. Proves that differentiating the one-point function with respect to the
   physical source \(J_r\) gives the causal source-response kernel
   \(K^R=i\Theta\langle[O(t),O(t')]\rangle\), which is the negative of the
   commutator-retarded convention \(G^{R,\mathrm{comm}}\).
7. Writes the two-point matrix in terms of \(G^>\), \(G^<\), \(G^R\), \(G^A\),
   and \(G^K\), and records \(G^{\mathrm{aa}}=0\) as a consequence of
   diagonal unitarity.
8. Derives the thermal KMS/detailed-balance relation and its
   fluctuation-dissipation form in the SK basis.
9. Derives the regulated coordinate path-integral representation with final
   gluing and initial density-matrix kernel.
10. States the gauge-theory/BV status of SK doubling and the continuum
    construction problem.

## Calculation Checks

- `calculation-checks/schwinger_keldysh_operator_checks.py` verifies diagonal
  unitarity, branch-exchange reality, \(|Z|\le1\), impulse retarded response,
  and KMS detailed balance in two-level finite systems.

## Figure Ledger

No figure is included in this pass.  A later figure may show the closed time
path with the final gluing point and optional Euclidean thermal segment.
