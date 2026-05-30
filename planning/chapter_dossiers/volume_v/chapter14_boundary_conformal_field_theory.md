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
- Fixes the relation among boundary-state coefficients, disk one-point
  coefficients, and the identity term in the bulk-boundary OPE:
  `R^a_{i0}=U^a_i=D_{ij}U_a^j` after the bulk two-point metric and identity
  normalization are declared.
- Develops finite direct sums of boundary conditions as Chan--Paton
  multiplicity spaces, with
  `H_{a^n b^m}=H_ab tensor Mat_{n x m}(C)`, matrix-unit OPE
  multiplication, annulus multiplicity `nm`, and boundary entropy
  `g_{a^n}=n g_a`.
- Works out compact free-boson Neumann and Dirichlet boundary states,
  including oscillator gluing, zero-mode restrictions, Wilson-line/position
  phases, and T-duality exchange.
- Works out the Majorana/Ising example: fermion NS/R gluing, Ising modular
  `S` matrix, fixed/free Cardy states, and annulus spectra.
- Derives the Ising boundary-condition-changing OPE constants in the
  Cardy/F-symbol basis, including the nontrivial
  `F^{sigma sigma sigma}_sigma` matrix, the free-boundary identity/energy
  channels, and the normalization-dependence of raw constants.
- Adds Liouville as the nonrational boundary-state test case: continuous
  direct-integral closed spectrum, FZZT wavefunctions, ZZ finite differences,
  and the hyperbolic kernels replacing finite modular `S`-matrix entries.
- States Cardy-Lewellen sewing status as a `quotedtheorem`, records the
  boundary `g`-theorem as a quoted monotonicity theorem, and adds an
  `openproblem` for nonrational/continuous-spectrum BCFT sewing.
- Expands the algebraic core of the rational boundary construction:
  symmetric special Frobenius algebra object \(A\) in the chiral tensor
  category, left \(A\)-module boundary conditions, open multiplicities
  `dim Hom_A(M tensor U_i,N)`, boundary OPE composition by \(A\)-linear
  morphisms, the \(A=1\) reduction to diagonal Cardy boundary spectra, and
  the bimodule formula for closed bulk multiplicities.

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
8. The coefficient `R^a_{i0}` in the bulk-boundary OPE equals the lowered
   disk one-point coefficient; raising the bulk label inserts the two-point
   metric `D_{ij}`.
9. Direct-sum boundary conditions compose by matrix units, so annulus
   multiplicities scale by `nm` and boundary entropy is additive under finite
   sums.
10. Compact-boson Neumann gluing forces `m=0`, while Dirichlet gluing forces
   `w=0`; T-duality exchanges these constraints.
11. The Ising Cardy states reproduce the open spectra of fixed/free boundary
   conditions.
12. The Ising boundary-changing OPE constants are the chiral fusing symbols
   in the Cardy basis; raw constants rescale with boundary two-point
   normalizations, while the `sigma sigma sigma` fusing matrix and relative
   fixed-boundary sign are invariant sewing data.
13. Liouville FZZT/ZZ boundary states are distributional wavefunctions on a
   continuous spectrum; their finite-difference and degenerate-annulus
   simplifications are hyperbolic algebra, not a substitute for an analytic
   sewing theorem.
14. Cardy-Lewellen sewing and the boundary `g`-theorem are theorem inputs, not
   rederived in full here.
15. The Frobenius-algebra object formalism turns rational Cardy-Lewellen
   boundary sewing into module associativity and chiral associator pentagon
   identities; analytic all-surface sewing remains the external theorem
   boundary.

## Figures

- No figure added.  Future figures should show annulus open/closed channel
  exchange, boundary-state propagation, and topological defect endpoints on
  boundary segments.

## Checks

- `calculation-checks/bcft_cardy_checks.py` verifies the Ising modular
  `S`-matrix arithmetic, Cardy annulus spectra, fusion associativity,
  fusion-ring characters, boundary entropy squares, Ising
  boundary-changing fusing constants and OPE powers, the \(A=1\)
  Frobenius-algebra module multiplicity formula, Chan--Paton direct-sum
  multiplicities and matrix-unit multiplication, compact-boson zero-mode
  exchange under T-duality, and the Liouville FZZT/ZZ hyperbolic identities.

## Remaining Obligations

- Develop the full analytic nonrational sewing framework: direct-integral
  topology, boundary-condition-changing operators for Liouville, annulus
  spectral-density positivity, pole prescriptions for contour motion, and
  compatibility with anomaly lines.

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
- Liouville boundary-state sources consulted:
  `references/02_2d_cft/boundary_liouville_fzz_hep-th-0001012/blio.tex` and
  `references/02_2d_cft/liouville_pseudosphere_zz_hep-th-0101152/look.tex`.
  Used to check FZZT wavefunction normalization, imaginary-parameter ZZ
  finite differences, and degenerate annulus shift-sum identities.  The BCFT
  chapter states only the algebraic and structural consequences; the full
  nonrational sewing problem remains open.

## Audit Notes

- 2026-05-26 Ising boundary-changing pass: added the
  boundary-condition-changing OPE constants for fixed/free Ising boundaries
  in the Cardy/F-symbol basis, with calculation checks for the
  `F^{sigma sigma sigma}_sigma` matrix, relative signs, and OPE exponents.
- 2026-05-26 Liouville boundary bridge: added the nonrational BCFT
  interpretation of FZZT and ZZ states, displayed the direct-integral
  replacement for rational Cardy sums, and added exact hyperbolic checks for
  the boundary-state kernels.
- 2026-05-30 rational Frobenius-core pass: expanded the Cardy-Lewellen
  theorem boundary by deriving the open-sector and boundary-OPE algebraic
  mechanism from symmetric special Frobenius algebra objects and their
  modules, with an exact Ising \(A=1\) module-multiplicity check.
