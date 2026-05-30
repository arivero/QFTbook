# Chapter 09: Boundaries, Defects, And Categories In Topological QFT

## Source Position

Volume VIII follows the Donaldson/Seiberg-Witten comparison with the boundary,
defect, and categorical layer required for extended topological theories and
gauge-theoretic boundary constructions.

## Notation Inventory

- `Z`: topological theory or functorial assignment.
- `B`, `H(B_0,B_1)`: boundary labels and interval state spaces.
- `G`, `H`, `K`: finite groups in finite-gauge examples.
- `Z(C[G])`, `e_rho`, `M_rho`: closed circle algebra of finite `BF_2`,
  primitive central idempotents, and elementary boundary modules.
- `D_ij`: codimension-one defects between theories.
- `X otimes_H Y`: balanced product of finite biset defects.
- `C`: monoidal or modular line-defect category in three-dimensional TQFT.
- `I`, `N_ab^c`, `S_ab`, `theta_a`: modular tensor category labels, fusion,
  modular matrix, and twists.
- `W_R(gamma)`: Chern-Simons Wilson line labelled by representation `R`.
- `K`, `A_K`, `b`, `q`, `L`: abelian Chern-Simons matrix, finite line group,
  braiding form, spin quadratic form, and Lagrangian subgroup.
- `omega_BV`, `alpha_partial`, `omega_partial`: BV symplectic form and BFV
  boundary forms.
- `L_partial`: boundary Lagrangian condition in BFV phase space.
- `A`, `q`, `b`, `Rad(A,b)`: pointed braided finite abelian input, spin
  quadratic function, polarized braiding form, and radical/Mueger-center
  subgroup in the pointed Walker--Wang mechanism.
- `Z_2(C)`, `M_{a,x}`: Mueger center of a finite semisimple braided category
  and categorical monodromy \(c_{x,a}c_{a,x}\) used in the non-pointed
  Walker--Wang plaquette criterion.

## Claim Ledger

- Derives categorical composition from gluing intervals with boundary labels.
- Displays finite `BF_2` boundary states as primitive central idempotents
  `e_rho` in `Z(C[G])`, with proof from Schur orthogonality.
- Defines topological defect fusion through collision limits.
- Gives finite-gauge codimension-one defects as bisets and proves
  associativity of balanced-product fusion.
- Relates line defects in three-dimensional TQFT to braided monoidal
  categories and records explicit modular tensor category data.
- Reuses the `SU(2)_k` modular data from the Chern-Simons chapter as the
  line-defect input for boundary and condensable-algebra questions.
- Defines Lagrangian subgroups in abelian Chern-Simons theory and proves how
  they give commutative separable boundary algebra objects.
- Works out the two toric-code Lagrangian boundary subgroups.
- Replaces the Crane-Yetter / Walker-Wang quoted boundary principle by a
  local pointed theorem: in a finite abelian pointed input, bulk deconfined
  lines are precisely the radical of the braiding form, while a nondegenerate
  input leaves its nontrivial line category on the boundary.
- Works out the toric-code pointed input as a modular boundary order with
  trivial bulk radical.
- Adds the non-pointed algebraic plaquette criterion: under the hypothesis
  that the local plaquette-loop crossing with a transverse line is categorical
  monodromy, the algebraic candidates for deconfined bulk lines are exactly
  the simple objects in the Mueger center.
- Uses the Ising modular category as a non-pointed example whose \(S\)-matrix
  row-factorization test leaves only the tensor unit transparent.
- Defines the BV-BFV boundary mechanism and the extended assignment problem.

## Figure Ledger

No figure is included in this pass.  Future figures should include interval
composition, defect fusion, braided line exchange, and BV-BFV boundary
restriction diagrams.

## Calculation Checks

- `calculation-checks/walker_wang_boundary_checks.py` verifies the pointed
  Walker--Wang radical criterion, including toric-code, symmetric
  nonmodular, and cyclic nondegenerate examples, and the non-pointed Ising
  M\"uger-center row-factorization test.

## Anti-Wrapper Audit

- 2026-05-30 pass: removed the Crane--Yetter / Walker--Wang `quotedtheorem`
  wrapper.  The fully general categorical construction remains an external
  mathematical boundary, but the monograph now proves the finite pointed
  mechanism actually used in the chapter.
- 2026-05-30 non-pointed mechanism pass: added the finite semisimple braided
  M\"uger-center definition and a local plaquette-algebra proposition, so the
  non-pointed Walker--Wang statement now has a precise algebraic mechanism
  rather than only an external-theorem remark.
