# Volume V, Chapter 14 Dossier: Boundary Conformal Field Theory

## Logical Role

- Address issue #602 / Block S by adding the dedicated two-dimensional BCFT
  machinery missing from the monograph: conformal boundary conditions,
  boundary states, Ishibashi states, Cardy consistency, free-field examples,
  and sewing status.
- Complements Volume IX boundary/defect material by developing the
  Virasoro/modular-sewing technology special to two-dimensional CFT.
- Depends on the Volume V VOA/modular tensor category chapter and on the
  general CFT Ward-identity chapters.

## Definitions And Results

- Defines an oriented bosonic BCFT datum with boundary-condition labels,
  interval Hilbert spaces, boundary operators, bulk-to-boundary OPE maps, and
  bordered-surface sewing.
- States the conformal boundary condition `T = Tbar` on the upper half-plane.
- Proves that stress-tensor gluing preserves one Virasoro algebra and yields
  the closed-channel condition `(L_n - Lbar_{-n})|B> = 0`.
- Defines the open/closed annulus equality with open-channel Hilbert spaces
  and closed-channel boundary states.
- Constructs Ishibashi states from an orthonormal basis and an antiunitary
  orientation-reversal map; proves the Virasoro gluing equation.
- Derives the diagonal-rational Cardy solution
  `|a> = sum_i S_ai / sqrt(S_0i) |i>>` and proves that the open spectrum is
  the fusion coefficient `N_ab^k` by the Verlinde formula.
- Works out compact free-boson Neumann and Dirichlet boundary states,
  including oscillator gluing, zero-mode restrictions, Wilson-line/position
  phases, and T-duality exchange.
- Works out the Majorana/Ising example: fermion NS/R gluing, Ising modular
  `S` matrix, fixed/free Cardy states, and annulus spectra.
- States Cardy-Lewellen sewing status as a `quotedtheorem`, records the
  boundary `g`-theorem as a quoted monotonicity theorem, and adds an
  `openproblem` for nonrational/continuous-spectrum BCFT sewing.

## Claims To Verify

1. Boundary stress-tensor gluing cancels the boundary term in the conformal
   Ward identity.
2. The closed-channel sign in `(L_n - Lbar_{-n})|B> = 0` comes from reversing
   the antiholomorphic contour orientation.
3. Ishibashi states are distributional states; their regulated overlaps are
   characters.
4. Cardy's diagonal solution converts the annulus coefficients into Verlinde
   fusion coefficients.
5. Compact-boson Neumann gluing forces `m=0`, while Dirichlet gluing forces
   `w=0`; T-duality exchanges these constraints.
6. The Ising Cardy states reproduce the open spectra of fixed/free boundary
   conditions.
7. Cardy-Lewellen sewing and the boundary `g`-theorem are theorem inputs, not
   rederived in full here.

## Figures

- No figure added.  Future figures should show annulus open/closed channel
  exchange, boundary-state propagation, and topological defect endpoints on
  boundary segments.

## Checks

- `calculation-checks/bcft_cardy_checks.py` verifies the Ising modular
  `S`-matrix arithmetic, Cardy annulus spectra, boundary entropy squares, and
  compact-boson zero-mode exchange under T-duality.

## Remaining Obligations

- Add explicit Cardy-Lewellen coefficient equations for a nontrivial rational
  model beyond the annulus.
- Add boundary-condition-changing three-point constants in the Ising model.
- Develop Liouville boundary states only in a later pass coordinated with the
  nonrational Liouville sewing open problem.
