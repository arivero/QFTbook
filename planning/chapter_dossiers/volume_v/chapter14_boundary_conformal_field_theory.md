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
- States explicit rational sewing hypotheses for boundary OPE equations:
  finite semisimple unitary chiral data, convergent genus-zero blocks,
  nondegenerate boundary two-point pairings, and Moore--Seiberg fusing
  isomorphisms satisfying the pentagon identity.
- Defines boundary-condition-changing fields, writes the boundary OPE
  coefficient tensor, and displays the Cardy--Lewellen four-boundary-field
  sewing equation.
- Proves that in the diagonal Cardy case boundary-field multiplicities are
  fusion coefficients and that normalized fusing matrices reduce boundary
  sewing to the pentagon identity.
- Corrects the disk one-point/fusion-character normalization: the fusion
  character is `lambda_a(i)=S_ia/S_0a`, while the Cardy disk coefficient is
  `B_a^i = S_0a lambda_a(i)/sqrt(S_0i)`.
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
5. Boundary OPE coefficients depend on two-point normalization and block
   bases, while the Cardy--Lewellen sewing equation is invariant under basis
   changes.
6. In the diagonal Cardy case, boundary-changing field multiplicities obey
   `dim psi_i^{ab}=N_ia^b`, and associativity of boundary OPEs is the
   Moore--Seiberg pentagon identity in boundary-field language.
7. The Verlinde eigenvalue `S_ia/S_0a` is the fusion-ring character; the
   Cardy disk one-point coefficient differs by the two-point normalization
   factor `S_0a/sqrt(S_0i)`.
8. Compact-boson Neumann gluing forces `m=0`, while Dirichlet gluing forces
   `w=0`; T-duality exchanges these constraints.
9. The Ising Cardy states reproduce the open spectra of fixed/free boundary
   conditions.
10. Cardy-Lewellen sewing and the boundary `g`-theorem are theorem inputs, not
   rederived in full here.

## Figures

- No figure added.  Future figures should show annulus open/closed channel
  exchange, boundary-state propagation, and topological defect endpoints on
  boundary segments.

## Checks

- `calculation-checks/bcft_cardy_checks.py` verifies the Ising modular
  `S`-matrix arithmetic, Cardy annulus spectra, fusion associativity,
  fusion-ring characters, boundary entropy squares, and compact-boson
  zero-mode exchange under T-duality.

## Remaining Obligations

- Add boundary-condition-changing three-point constants in the Ising model.
- Develop Liouville boundary states only in a later pass coordinated with the
  nonrational Liouville sewing open problem.

## Reference Intake

- Local sources consulted:
  `references/02_2d_cft/frs_tft1_hep-th-0204148/hep.tex` and
  `references/02_2d_cft/frs_tft4_hep-th-0412290/IV.tex`.
  Used to verify the rational-BCFT status boundary: symmetric special
  Frobenius algebras and module categories solve rational sewing under
  analytic RCFT hypotheses.  The chapter reproduces the annulus, boundary
  OPE, fusion-character, and pentagon-reduction arguments locally; it quotes
  the full all-surface Frobenius-algebra construction rather than treating it
  as folklore.
