# 2026-05-26 Issue #582 Coordinate-To-Model Convergence

## Scope

- Volume XI, Chapter 9 now includes a finite-coordinate theorem that converts
  coordinate supremum estimates into the model-seminorm and model-distance
  hypotheses of the random-model Cauchy criterion.
- This theorem sits between the dyadic-net supremum upgrade and the concrete
  dynamic \(\Phi^4_3\) BPHZ discussion.

## Mathematical Content

- A finite coordinate index set \(I\) labels the real coordinate fields that
  enter the finite-sector model seminorm and model distance.
- Each coordinate is defined on a compact parameter space equipped with
  finite dyadic nets and entropy bounds.
- Uniform coordinate moment estimates give a uniform \(L^p\) bound for
  \(N_n=1+\|\Pi^{(n)}\|+\|\Gamma^{(n)}\|\).
- Cutoff-increment coordinate estimates give the dyadic Cauchy bound for
  \(d_{K;\gamma}(Z_{n+1},Z_n)\).
- The theorem displays the resulting constants \(C_N\) and \(C_D\) entering
  the random-model convergence theorem.

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies a
  two-coordinate exact rational sample for the theorem: the uniform
  coordinate constants, the model-seminorm \(L^2\) bound, the Cauchy
  prefactor, \(C_N\), \(C_D\), and the dyadic \(n=3\) distance bound.

## Remaining Issue #582 Obligations

- Prove the tree-by-tree BPHZ coordinate estimates that provide the
  hypotheses of the finite-coordinate theorem for the dynamic \(\Phi^4_3\)
  negative sector.
- Specify the coordinate charts for every \(\Pi\)- and \(\Gamma\)-component
  entering the finite-sector seminorms.
- Combine the finite-coordinate theorem with the fixed-point and invariant
  law steps to remove the remaining quoted status of the dynamic
  \(\Phi^4_3\) convergence theorem.
