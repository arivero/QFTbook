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
- Adds an explicit sewing-architecture guide that organizes the chapter into
  Virasoro/annulus kinematics, genus-zero diagonal sewing, rational
  Frobenius-module mechanisms, nonrational direct-integral/contour data, and
  the remaining all-surface analytic theorem boundary.
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
- Expands the diagonal Cardy disk two-bulk sewing mechanism: after normalizing
  the raw disk coefficient to the classifying coordinate
  `Bhat_a(i)=sqrt(S_0i) B_a^i/S_0a`, the disk one-point functional is a
  character of the fusion/classifying algebra and obeys
  `chi_a(e_i e_j)=chi_a(e_i) chi_a(e_j)`.
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
- Adds the finite Ising four-boundary sewing cell: for fixed boundary labels
  `r,s in {+,-}`, the free-boundary channel vectors
  `v_+=2^{-1/2}(1,1)` and `v_-=2^{-1/2}(1,-1)` obey
  `sum_p v_r(p)v_s(p)=delta_rs`, identifying the Cardy--Lewellen sewing
  equation with the orthogonality of the nontrivial Ising fusing matrix in
  this diagonal cell.
- Adds Liouville as the nonrational boundary-state test case: continuous
  direct-integral closed spectrum, FZZT wavefunctions, ZZ finite differences,
  and the hyperbolic kernels replacing finite modular `S`-matrix entries.
- Adds the stripped continuous annulus Plancherel cell for the even FZZT
  wave `C_s(P)=2 cos(2 pi sP)`: the heat-regulated closed momentum pairing
  is `G_t(s-s')+G_t(s+s')`, tending to `delta(s-s')+delta(s+s')`, so the
  second term records the boundary-label quotient `s ~ -s` rather than an
  additional open multiplicity.  Also records the exact odd finite-cyclic
  regulator `(2N)^(-1) sum_p c_s(p)c_s'(p)=delta_ss'` on nonzero
  reflection orbits.
- Adds the local pole-crossing residue cell for nonrational sewing: when a
  simple pole crosses the closed-channel contour, Cauchy's theorem adds the
  rank-one evaluation functional `2 pi i phi(alpha) rho(alpha)`, which is the
  finite local model for a discrete open-channel spectral summand.
- Adds the analytic sewing datum that the Liouville boundary formulas would
  have to satisfy to become a BCFT construction: a dense nuclear closed
  test space and distributional boundary states, open-channel Hilbert spaces
  with positive spectral measures, boundary-condition-changing fields as
  operator-valued distributions on common domains, contour/residue
  prescriptions for FZZT-to-ZZ continuation, and continuous multilinear
  sewing maps for closed and open gluing.
- States the rational Cardy-Lewellen construction boundary as a
  `quotedtheorem` with a narrowed role: special symmetric Frobenius algebra
  objects and module categories supply local finite-categorical sewing data
  for rational examples, while converse/classification and all-surface
  analytic sewing remain external.  The chapter replaces the vague boundary
  `g`-theorem statement by the boundary entropy gradient formula with explicit
  trace, entropy, metric, and positivity hypotheses, derives
  \(g_{\rm UV}\ge g_{\rm IR}\) from it, and adds an `openproblem` for
  nonrational/continuous-spectrum BCFT sewing.
- Expands the finite spectral mechanism behind the boundary entropy gradient
  metric: after subtracting the one-point function, a finite half-cylinder
  KMS spectral representation gives positive gap weights
  `2 kappa^2/(Delta(Delta^2+kappa^2))` for the kernel
  `1 - cos(kappa tau)`, separating finite spectral positivity from the
  continuum renormalization and contact-term theorem boundary.
- Expands the algebraic core of the rational boundary construction:
  symmetric special Frobenius algebra object \(A\) in the chiral tensor
  category, left \(A\)-module boundary conditions, open multiplicities
  `dim Hom_A(M tensor U_i,N)`, boundary OPE composition by \(A\)-linear
  morphisms, the \(A=1\) reduction to diagonal Cardy boundary spectra, and
  the bimodule formula for closed bulk multiplicities.
- Adds the finite matrix-algebra model of the Frobenius cutting move:
  for \(A=\operatorname{Mat}_d(\mathbb C)\),
  \(\Delta(E_{ij})=\sum_r E_{ir}\otimes E_{rj}\), the two Frobenius sliding
  maps and \(\Delta m\) agree on \(E_{ij}\otimes E_{k\ell}\), and
  \(m\Delta=d\,\operatorname{id}\).  This is the exact algebraic content of
  the local topological line move used in rational boundary sewing.
- Adds the finite classifying-center model for non-diagonal rational sewing:
  for \(A_{\rm fin}=\oplus_r \operatorname{Mat}_{d_r}(\mathbb C)\), central
  primitive idempotents \(e_r\) act by scalar characters on simple boundary
  modules \(M_r\), giving the disk identity-channel sewing equation
  `chi_r(zz')=chi_r(z) chi_r(z')`; noncentral elements give
  endomorphism-valued boundary insertions, and finite direct sums replace the
  elementary character by Chan--Paton matrix data or by nonmultiplicative
  trace choices.
- Adds the annulus nimrep constraint for non-diagonal rational boundaries:
  the open-channel matrices
  `(n_i)_M^N = dim Hom_A(M tensor U_i,N)` satisfy
  `n_i n_j = sum_k N_ij^k n_k` by module associativity, with a finite
  pointed \(G=\mathbb Z_2\times\mathbb Z_2\), \(G/H\) coset example where a
  nontrivial stabilizer object acts trivially and the other coset swaps the
  two boundary labels.
- Adds the Fourier diagonalization of that pointed annulus nimrep:
  \(P_\eta=|G/H|^{-1}\sum_{\bar g}\eta(\bar g)^{-1}n_{\bar g}\) are
  orthogonal projectors and \(n_g=\sum_\eta\eta(g+H)P_\eta\).  The same
  formula in boundary Fourier coefficients shows that annulus spectra see
  only the quotient \(G/H\), so stabilizer chiral labels require the later
  boundary-endomorphism and mixed-projector data.
- Adds the boundary-OPE composition law in the same pointed \(G/H\) module
  example: the generator \(\psi_{x,g}\) from \(xH\) to \((x+g)H\) obeys
  \(\psi_{x+g,h}\psi_{x,g}=\psi_{x,g+h}\), so the finite
  Cardy-Lewellen associativity cell is just group associativity, while the
  stabilizer labels remain distinct chiral boundary endomorphisms.
- Adds the mixed bulk-boundary sewing shadow in the pointed \(G/H\) cell:
  stabilizer character idempotents
  `e_{x,chi}=|H|^{-1} sum_h chi(h)^{-1} psi_{x,h}` obey orthogonal
  idempotent algebra and slide through boundary-changing fields by
  `psi_{x,g} e_{x,chi}=e_{x+g,chi} psi_{x,g}`.  The text identifies this as
  a finite classifying-projector compatibility, not a full analytic
  bulk-boundary sewing construction.
- Adds the stabilizer-sector two-point ledger in the same finite cell:
  with Frobenius trace \(\varepsilon_x(\psi_{x,h})=\delta_{h,0}\),
  \(\varepsilon_x(e_{x,\chi}e_{x,\chi'})=\delta_{\chi,\chi'}/|H|\), and the
  projected inverse boundary-changing fields obey
  \(\psi_{x+g,g;\chi'}\psi_{x,g;\chi}=\delta_{\chi,\chi'}e_{x,\chi}\).
  This shows that stabilizer characters are invisible to the annulus quotient
  \(G/H\) but visible to boundary two-point sewing.
- Adds the pointed-laboratory dependency ledger: annulus entries equal the
  graded dimensions of the same boundary-changing sectors
  \((n_g)_{xH,yH}=\dim\operatorname{span}\{\psi_{x,g}\mid(x+g)H=yH\}\),
  the stabilizer fields are recovered from classifying idempotents by Fourier
  inversion \(\psi_{x,h}=\sum_{\chi\in\widehat H}\chi(h)e_{x,\chi}\), and the
  annulus, boundary OPE, classifying idempotents, and two-point pairings are
  explicitly presented as projections of one finite module-category datum.

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
   normalizations, while the `sigma sigma sigma` fusing matrix, relative
   fixed-boundary sign, and four-boundary orthogonality sewing cell are
   invariant sewing data.
13. Liouville FZZT/ZZ boundary states are distributional wavefunctions on a
   continuous spectrum; their finite-difference and degenerate-annulus
   simplifications are hyperbolic algebra, not a substitute for an analytic
   sewing theorem.  The stripped FZZT annulus has a continuous Plancherel
   reflection kernel, `delta(s-s')+delta(s+s')`, so open boundary labels live
   on the quotient `s ~ -s` and the annulus coefficient is a spectral measure,
   not an integer Cardy matrix.  A nonrational BCFT construction must also
   produce test spaces, open spectral measures, operator domains, contour
   prescriptions, and continuous sewing maps with determinant-line
   bookkeeping.  A simple pole crossing adds a residue/evaluation functional;
   omitting that discrete term in one sewing channel changes the amplitude.
14. Rational Cardy-Lewellen construction and the boundary entropy gradient
   formula are theorem-boundary inputs; monotonicity of \(g\) is derived from
   the positive gradient formula, not quoted as an independent
   endpoint-classification statement.  The positivity mechanism of the
   gradient metric is spectral: in a finite regulator each positive boundary
   gap contributes the weight `2 kappa^2/(Delta(Delta^2+kappa^2))`.
15. The Frobenius-algebra object formalism turns rational Cardy-Lewellen
   boundary sewing into module associativity and chiral associator pentagon
   identities; analytic all-surface sewing remains the external theorem
   boundary.
16. In a finite semisimple algebra shadow of a non-diagonal rational BCFT,
   disk identity-channel one-point coordinates are central characters on
   elementary boundary modules, not arbitrary traces on reducible modules and
   not actions of noncentral boundary endomorphisms.
17. The non-diagonal annulus multiplicity matrices form a nonnegative-integer
    representation of the chiral fusion algebra because interval sewing with
    two successive chiral labels can be evaluated either through an
    intermediate boundary module or by fusing the two chiral labels first.
18. In the pointed \(G/H\) module cell, the annulus matrices are
    simultaneously diagonalized by quotient Fourier projectors; stabilizer
    labels have the vacuum annulus spectrum but do not collapse as boundary
    endomorphism labels.
19. In the pointed \(G/H\) module cell, boundary-field OPE associativity
    keeps both endpoint data and chiral labels: stabilizer objects preserve a
    boundary endpoint but do not collapse to the vacuum boundary field.
20. The stabilizer classifying idempotents in the pointed \(G/H\) module cell
    are orthogonal projectors and are compatible with boundary-changing fields
    by the slide identity
    \(\psi_{x,g}e_{x,\chi}=e_{x+g,\chi}\psi_{x,g}\).
21. The same stabilizer sectors have orthogonal Frobenius two-point pairings
    \(\varepsilon_x(e_{x,\chi}e_{x,\chi'})=\delta_{\chi,\chi'}/|H|\), and
    projected inverse boundary-changing fields compose back to the matching
    stabilizer idempotent rather than collapsing all stabilizer labels.
22. The pointed finite laboratory is coherent end-to-end: the annulus matrix
    entry is the dimension of the corresponding boundary-changing field space,
    boundary-OPE composition has the same endpoint as annulus multiplication,
    and stabilizer Fourier inversion recovers endpoint-preserving fields from
    the classifying idempotents.

## Figures

- No figure added.  Future figures should show annulus open/closed channel
  exchange, boundary-state propagation, and topological defect endpoints on
  boundary segments.

## Checks

- `calculation-checks/bcft_cardy_checks.py` verifies the Ising modular
  `S`-matrix arithmetic, Cardy annulus spectra, fusion associativity,
  fusion-ring characters, normalized Cardy two-bulk classifying sewing,
  the finite classifying-center model for non-diagonal rational sewing,
  the pointed module-category annulus nimrep identity,
  the pointed annulus Fourier diagonalization and stabilizer degeneracy check,
  the pointed module-category boundary-OPE associativity cell,
  the pointed stabilizer classifying-idempotent slide identity,
  the unified pointed-laboratory dependency check tying annulus entries to
  boundary-field counts, OPE endpoints, and stabilizer Fourier inversion,
  boundary entropy squares, Ising
  boundary-changing fusing constants and OPE powers, the finite Ising
  four-boundary Cardy--Lewellen sewing cell, the \(A=1\)
  Frobenius-algebra module multiplicity formula, the matrix-unit Frobenius
  cutting move and specialness scalar, the positive spectral weight in the
  boundary entropy gradient metric, Chan--Paton direct-sum
  multiplicities and matrix-unit multiplication, compact-boson zero-mode
  exchange under T-duality, the Liouville FZZT/ZZ hyperbolic identities, and
  the finite cyclic cosine-Plancherel regulator for the continuous annulus
  quotient \(s\sim -s\), and the exact simple-pole residue/evaluation algebra
  for nonrational contour-crossing prescriptions.

## Remaining Obligations

- Prove or construct the full analytic nonrational sewing framework now
  specified in the chapter: direct-integral nuclear test spaces, distributional
  FZZT/ZZ boundary functionals, positive open spectral measures, domains for
  boundary-condition-changing operator-valued distributions, compatible
  contour/pole prescriptions, continuous closed/open gluing maps, and anomaly
  determinant-line compatibility.

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
- 2026-05-30 boundary entropy pass: replaced the vague boundary \(g\)-theorem
  block by the precise boundary entropy gradient formula.  The chapter now
  defines the boundary trace equation, the finite-temperature entropy
  \(s=(1-L\partial_L)\log z\), the positive susceptibility metric \(G_{ab}\),
  and derives \(d s/d\log L=-B^aG_{ab}B^b\le0\).
- 2026-05-30 quoted-theorem proof-boundary pass: expanded the mechanism of the
  boundary entropy gradient formula.  The text now displays the boundary
  deformation convention, the coupling derivative of \(\log z\), the integrated
  trace insertion, the finite Ward susceptibility with kernel \(K_L\), and the
  precise analytic inputs hidden in the quoted theorem: contact-term
  prescription, quotient by redundant derivatives, and reflection positivity.
- 2026-06-01 finite Ising sewing-cell pass: added the explicit
  four-boundary-field Cardy--Lewellen cell whose equality is
  \(F_{\sigma}^{\sigma\sigma\sigma}(F_{\sigma}^{\sigma\sigma\sigma})^T=1\),
  together with an exact calculation check of the fixed-boundary
  orthogonality relation.
- 2026-06-01 boundary entropy spectral-metric pass: expanded the gradient
  formula proof boundary by deriving the finite KMS spectral representation
  of the boundary two-point function and the positive kernel weight
  \(2\kappa^2/(\Delta(\Delta^2+\kappa^2))\); extended
  `bcft_cardy_checks.py` to verify the rational algebra of this weight.
- 2026-06-01 finite classifying-center pass: added the finite semisimple
  algebra shadow of non-diagonal rational disk sewing, distinguishing
  central elementary boundary characters from noncentral endomorphism-valued
  insertions and from trace choices on finite direct sums; extended
  `bcft_cardy_checks.py` with exact center-character and reducible-trace
  diagnostics.
- 2026-06-02 nonrational analytic-sewing datum pass: replaced the vague
  warning after the Liouville hyperbolic identities by a precise construction
  target for nonrational BCFT sewing.  The manuscript now separates exact
  FZZT/ZZ finite-difference algebra from the still-open analytic tasks:
  closed test-space topology, distributional boundary states, open spectral
  positivity, boundary-field domains, pole prescriptions, continuous gluing,
  and anomaly-line compatibility.
- 2026-06-02 rational Frobenius-boundary tightening pass: narrowed the
  Cardy-Lewellen quoted theorem from broad classification language to the
  construction theorem-boundary actually used in the chapter, and added the
  finite matrix-unit Frobenius cutting move
  \((m\otimes1)(1\otimes\Delta)=\Delta m=(1\otimes m)(\Delta\otimes1)\)
  plus \(m\Delta=d\,1\), with a paired exact calculation check.
- 2026-06-02 anti-wrapper pass: demoted the Ising boundary-changing OPE
  constants from a proposition/proof shell to a worked normalization and
  sewing cell.  The formulas remain because they are useful explicit data; the
  derivation is a Cardy-basis fusing-symbol evaluation after the general
  boundary-field framework has already been constructed, so it should not be
  presented as theorem-level mathematics.
- 2026-06-02 annulus nimrep pass: added the open-channel matrix
  representation identity for non-diagonal rational boundaries and the finite
  pointed \(G/H\) coset module example; extended `bcft_cardy_checks.py` with
  exact integer checks of \(n_g n_h=n_{g+h}\), stabilizer collapse, and the
  boundary-label swap matrix.
- 2026-06-03 pointed annulus Fourier pass: added the simultaneous
  diagonalization of the pointed \(G/H\) annulus nimrep by quotient character
  projectors, the boundary Fourier coefficient formula, and the warning that
  stabilizer labels have the vacuum annulus spectrum while remaining visible
  in boundary endomorphism data.  Extended `bcft_cardy_checks.py` to verify
  projector orthogonality, spectral resolution, Fourier matrix entries, and
  stabilizer-spectrum degeneracy.
- 2026-06-02 pointed boundary-OPE pass: added the finite boundary-field
  composition law \(\psi_{x+g,h}\psi_{x,g}=\psi_{x,g+h}\) in the same
  \(G/H\) module example; extended `bcft_cardy_checks.py` to verify endpoint
  matching, associativity, and the fact that stabilizer chiral labels preserve
  endpoints without collapsing to the vacuum field.
- 2026-06-03 continuous annulus Plancherel pass: added the stripped FZZT
  annulus heat-kernel identity
  \(K_t(s,s')=G_t(s-s')+G_t(s+s')\), isolating the continuous spectral
  quotient \(s\sim -s\) from the full Liouville sewing theorem.  Extended
  `bcft_cardy_checks.py` with the exact odd finite-cyclic regulator verifying
  cosine-Plancherel orthogonality on nonzero reflection orbits and the
  off-diagonal overlap between unquotiented reflected labels.
- 2026-06-03 pointed mixed sewing pass: added the stabilizer-character
  classifying idempotents in the finite \(G/H\) module cell and the slide
  identity through boundary-changing fields, with exact checks of idempotent
  algebra and mixed bulk-boundary compatibility.
- 2026-06-03 pointed stabilizer two-point pass: added the finite Frobenius
  trace pairing for stabilizer idempotents and the inverse projected
  boundary-changing sector composition.  Extended `bcft_cardy_checks.py` to
  verify orthogonal two-point pairings and the fact that inverse fields return
  to \(e_{x,\chi}\) only in matching stabilizer-character sectors.
- 2026-06-03 nonrational pole-crossing pass: added the Cauchy residue
  accounting cell showing that a crossed pole contributes a rank-one
  evaluation functional, plus exact rational checks that multiple residue
  additions commute and that omitting one residue changes the sewing channel.
- 2026-06-03 architecture/coherence pass: added a chapter-level sewing guide,
  moved the bulk/classifying-algebra block before the pointed \(G/H\)
  example, and consolidated the pointed formulas as one finite sewing
  laboratory.  The annulus, Fourier, boundary-OPE, stabilizer-idempotent, and
  two-point-pairing cells now read as a single rational module mechanism
  rather than as detached local ledgers.
- 2026-06-03 pointed-laboratory dependency pass: added the end-to-end ledger
  inside that finite sewing laboratory.  The text now identifies annulus
  entries with boundary-field counts, recovers stabilizer endomorphism fields
  from classifying idempotents by Fourier inversion, and states that these are
  compatible projections of one module-category datum rather than independent
  evidence for full analytic sewing.
