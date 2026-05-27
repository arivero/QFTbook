# Chapter 07: Eta Invariants and Global Anomalies

## Source Position

Volume XII has introduced background gauge fields, index theory, anomaly
polynomials, and determinant lines.  This chapter now develops the holonomy
side of the same structure: eta invariants, APS boundary terms, determinant
and Pfaffian-line transport, Dai--Freed inflow, and the Witten \(SU(2)\)
global anomaly as an explicit mod-two-index example.

## Notation Inventory

- `Y`: closed odd-dimensional spin manifold; `X`: compact even-dimensional
  spin manifold with boundary.
- `B_Y`: self-adjoint odd-dimensional Dirac operator.
- `eta_B(s)`, `h(B)`, `xi(B)`: eta function, kernel dimension, and reduced
  eta invariant.
- `D_X^{+,APS}`: chiral Dirac operator with APS spectral boundary condition.
- `P_{\geq0}`: APS projection onto nonnegative boundary spectrum.
- `Det D`, `Pf D`: determinant and Pfaffian lines over background-field space.
- `gamma`, `Y_gamma`: closed loop of backgrounds and its mapping torus.
- `Ind_2(B_Y)`: mod-two index of the real/pseudoreal Dirac operator.
- `R_j`, `n=2j`, `T_Delta(R_j)`: \(SU(2)\) isospin representation, doubled
  isospin, and trace-delta Dynkin index.

## Claim Ledger

- Defines the eta function and reduced eta invariant for self-adjoint
  Dirac-type operators, including the integer jump at zero crossings.
- States the APS formula as an external global-analysis theorem with explicit
  product-collar and boundary-projection conventions.
- Proves the cylinder variation formula for \(\xi\) modulo integers from the
  APS theorem, including the orientation-reversal bookkeeping
  \(\xi(-B)=-\xi(B)+h(B)\).
- Defines determinant-line fibers and states the Bismut--Freed holonomy
  theorem for mapping tori.
- Derives finite gauge-transformation phases as determinant-line holonomies.
- Defines the Pfaffian mod-two index and proves its deformation invariance in
  the real skew setting.
- States the mod-two index theorem for the Witten \(SU(2)\) mapping torus and
  derives the parity criterion \(2j\equiv1\pmod4\) using exact binomial parity.
- Explains Dai--Freed inflow as a boundary-line trivialization and proves the
  descent limit for contractible loops.
- Records the interacting-QFT anomaly-line construction as an open problem.

## Calculation Ledger

- `calculation-checks/eta_global_anomaly_checks.py` checks the APS
  orientation bookkeeping, the first \(SU(2)\) trace-delta Dynkin indices,
  Witten parity criterion, Pfaffian-sign multiplicativity, cubic-weight-sum
  cancellation, and cylinder congruence arithmetic.
- Related scripts: `calculation-checks/background_index_theory_checks.py`,
  `calculation-checks/anomaly_polynomial_descent_checks.py`, and
  `calculation-checks/inflow_anomaly_line_checks.py`.

## Figure Ledger

- `fig:eta-cylinder-mapping-torus` shows the APS cylinder and the mapping
  torus used to pass from local eta variation to determinant-line holonomy.

## Residual Work

- The quoted APS, Bismut--Freed, and mod-two-index theorems are mathematical
  inputs.  A later appendix could develop their proofs in the level of
  global analysis and KO-theory needed by the monograph.
- A later interacting-anomaly chapter should replace the free-fermion
  determinant-line model by a general construction of anomaly lines for
  interacting QFTs.
