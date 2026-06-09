# Volume VI, Chapter 1 Dossier: Factorized Scattering And Integrability
Source-File: monograph/tex/volumes/volume_vi/chapter01_factorized_scattering_and_integrability.tex

## Logical Role

- Role in the monograph: open the integrable-QFT volume after the general
  scattering and analyticity volumes have defined the S-matrix.
- Immediate predecessor: Volume II scattering and analytic structure.
- Immediate successor: detailed two-dimensional integrable models, form
  factors, and thermodynamic Bethe ansatz.
- Cross-volume role: supplies the Volume VI reconstruction-status map that
  separates on-shell exact data, Hilbert-space construction, local observables,
  TBA/mirror thermodynamics, and hydrodynamic limits.

## Definitions And Results

- Massive two-dimensional one-particle rapidity variables.
- Ordered rapidity chambers and the mostly-plus invariant
  \(s_{ab}=-(p_a+p_b)^2\).
- Elastic factorized scattering datum on \(V\otimes V\).
- Unitarity, Hermitian analyticity, crossing, and Yang--Baxter compatibility.
- Separating higher-spin charge family, formulated as injectivity of a
  species-resolved moment map outside threshold and bound-state singular
  loci, with a concrete Newton-identity sufficient condition.
- Higher-spin conserved-charge argument proving elastic permutation support and
  excluding generic particle production as a distribution-kernel support
  statement under stated asymptotic-state and regularity hypotheses.
- No-diffraction pairwise-collision gate: asymptotic wave-packet separation,
  macrocausality/cluster decomposition, reduction to isolated ordered pair
  collisions, simultaneous-collision control, threshold and bound-state channel
  treatment, and regularity needed to identify two-body operators.
- Conditional pairwise-factorization proposition: under the no-diffraction
  gate, an allowed ordered collision history gives an ordered product of
  two-body maps, and Yang--Baxter follows by comparing the two three-particle
  histories.
- Chamber groupoid representation by adjacent two-body scattering maps,
  with unitarity and Yang--Baxter proven equivalent to path-independent
  chamber continuation.
- Zamolodchikov--Faddeev algebra as the operator algebraic encoding of
  factorized scattering, with associativity proven equivalent to
  Yang--Baxter.
- \(S\)-symmetric finite-particle wavefunctions and well-defined extension
  from a fundamental chamber.
- Watson exchange previewed as a rapidity-boundary-value statement about
  ordered scattering bases, now stated as a proposition with proof from the
  ZF exchange relation; locality is reserved for cyclicity and reconstruction
  conditions.
- Boundary between on-shell scattering data and reconstruction of local
  fields through form factors.
- Volume-level reconstruction map from local QFT with higher-spin charges to
  factorized scattering, \(S\)-Fock/ZF data, wedge-local fields, local
  algebras, local fields/Wightman functions, TBA, mirror finite-size data, and
  GHD.
- Status labels for integrable-QFT bridges: theorem, conditional theorem,
  formal construction, numerical or finite-regulator evidence, and open
  problem.
- Bridge-status map for the main Volume VI arrows, including the exact
  load-bearing assumptions needed to upgrade finite algebra or formal
  functional equations to local-QFT statements.
- Reference model discipline: massive Ising as a free-field theorem-level
  calibration; regular scalar factorizing models such as sinh-Gordon as
  conditional wedge-local/local-algebra constructions whose point-field
  form-factor completeness remains separate.
- Wedge-local reconstruction proof-obligation map: defines the double-cone candidate
  `A_S(O)=A_S(W_R+x) cap A_S(W_L+y)`, the modular-nuclearity map coordinate,
  and the residual split separating wedge-generator, nuclearity,
  local-intersection, form-factor, domain/positivity, and completeness
  inputs before a local observable is claimed.
- End-to-end observable reconstruction map for Volume VI reference paths:
  Ising energy, sinh-Gordon wedge/local-net reconstruction, Lee--Yang TBA, and
  GHD Euler cells.  The map names the on-shell, Hilbert-space, wedge,
  local-algebra, form-factor/domain, thermodynamic/state, microscopic-operator,
  and physical-projection checkpoints that must close before an exact formula is
  quoted as a local, thermodynamic, hydrodynamic, or real-time transport QFT
  observable.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\theta\) | rapidity |
| \(p^\mu(\theta)\) | massive two-dimensional momentum |
| \(s_{ab}(\theta)\) | positive invariant mass squared, \(-\bigl(p_a+p_b\bigr)^2\) |
| \(V\) | finite-dimensional species space |
| \(S_{12}(\theta)\) | two-body scattering operator on \(V\otimes V\) |
| \(C\) | charge-conjugation matrix used in crossing |
| \(Z_a^\dagger(\theta)\) | Zamolodchikov--Faddeev creation operator |
| \(Q_{s,\lambda}\) | conserved charge of Lorentz spin \(s\) |
| \(\Phi_N\) | higher-spin charge moment map on \(N\)-particle multisets |
| \(\mathsf T_i\) | adjacent chamber-transition map induced by two-body scattering |
| \(\mathsf S_N(\sigma;\theta)\) | conditional \(N\)-body scattering map attached to a permutation graph after the no-diffraction gate |
| \(S\)-Fock space | Hilbert space of \(S\)-symmetric finite-particle wavefunctions |
| ZF algebra | Zamolodchikov--Faddeev exchange algebra encoding ordered scattering bases |
| TBA | thermodynamic Bethe ansatz; conditional thermodynamic/mirror functional equation |
| GHD | generalized hydrodynamics; conditional Euler-scale limit of locally equilibrated integrable states |
| \(\mathfrak A_S(W_R)\) | right-wedge algebra produced by the \(S\)-Fock/wedge-local construction |
| \(\mathfrak A_S(\mathcal O)\) | double-cone local-algebra candidate, defined as an opposite-wedge intersection |
| \(\Xi_{x,y}\) | modular nuclearity map used to test local-intersection phase space |
| \(R_{\rm pfg},R_{\rm nuc},R_{\rm int},R_{\rm ff},R_{\rm dom},R_{\rm comp}\) | reconstruction residuals from wedge data to local observables |
| \(\mathsf R=(\mathsf S,\mathsf H,\mathsf W,\mathsf O,\mathsf F,\mathsf T,\mathsf P)\) | end-to-end observable reconstruction checkpoints: scattering/Bethe datum, Hilbert space, wedge locality, local algebra, form-factor/domain package, thermodynamic or mirror state, and physical projection |
| \(\varepsilon_{\mathsf S},\ldots,\varepsilon_{\mathsf P}\) | route-level residual slots or bounds in the observable reconstruction map; summable only after a common observable norm or topology and estimates have been supplied |

## Claim Ledger

1. Factorization is a property of the scattering theory after asymptotic
   states exist and the no-diffraction/pairwise-collision gate has been
   supplied.
2. Yang--Baxter consistency follows from equality of different pairwise
   scattering orderings.
2a. More precisely, unitarity and Yang--Baxter are the local relations that
    make adjacent chamber-crossing maps path independent.
3. Higher-spin charge conservation constrains the support of scattering
   distribution kernels to the common zero locus of charge differences.
4. Under the separating moment-map hypothesis, that common zero locus is the
   elastic permutation graph away from threshold and bound-state singular
   loci.
4a. Elastic support and absence of generic production do not by themselves
    determine the coefficient on an elastic permutation graph; joint
    three-body diffractive phases can preserve every additive higher-spin charge
    while failing pairwise factorization.
4b. Under asymptotic wave-packet separation, macrocausality/cluster
    decomposition, isolated two-body collision reduction, simultaneous-collision
    control, threshold/bound-state channel treatment, and two-body regularity,
    the coefficient on an allowed permutation graph is the ordered product of
    the corresponding two-body maps.  Yang--Baxter is then the comparison of
    the two admissible three-particle collision histories.
5. Watson exchange is a boundary-value identity for ordered scattering
   bases; it should not be compressed into the phrase "locality gives".
6. Local QFT reconstruction from factorized \(S\)-matrices requires separate
   form-factor and locality analysis.
7. Exact finite identities, TBA equations, and form-factor functional
   equations occupy different locations in the reconstruction map; finite
   calculation checks verify algebraic cells but do not prove local algebras,
   point-field domains, spectral convergence, or thermodynamic limits.
8. Massive Ising and regular scalar factorizing models provide two calibration
   paths: the former is theorem-level through free-field construction, while
   the latter is conditional on analytic/nuclearity estimates for local
   algebras and separate form-factor convergence for point fields.
9. The first genuinely local object in the \(S\)-matrix reconstruction chain
   is the double-cone intersection of opposite wedge algebras.  Exact
   Yang--Baxter/ZF algebra controls the \(S\)-Fock coordinate, but modular
   nuclearity, nontrivial local intersections, form-factor convergence,
   domains/positivity, and completeness remain separate inputs.
10. End-to-end reconstruction has route-dependent observable checkpoints.  The
    Ising energy route is theorem-level because the free Majorana CAR
    construction already supplies the Hilbert space, local net, domains,
    positivity, and completeness; the sinh-Gordon route remains conditional
    until nuclearity, local intersections, point-field domains, and completeness
    are supplied; Lee--Yang TBA and GHD certify thermodynamic, Euler-scale, or
    Drude coordinates only under their own finite-volume, state-limit,
    microscopic-observable, Kubo, and projection hypotheses.  A named residual
    slot is not a numerical estimate until a common observable norm/topology and
    bound are supplied.

## Figures

- Rapidity-space two-body scattering diagram.
- Three-particle Yang--Baxter braid diagram.
- Factorized scattering line ordering diagram.

## Audit Notes

- 2026-05-28 formalization pass: promoted the rapidity convention, chamber
  groupoid consistency, ZF associativity, \(S\)-symmetric wavefunction
  extension, and Watson exchange to definitions/propositions with proofs.
  Added `calculation-checks/factorized_scattering_algebra_checks.py` for the
  rapidity-sign convention, Newton identities, braid relations, rational
  Yang--Baxter identity, scalar unitarity, and Watson coefficient bookkeeping.
- 2026-06-03 reconstruction-map pass: added a reader-facing status map for
  the whole Volume VI exact-data-to-local-QFT chain.  The pass deliberately
  demotes finite checks and formal bootstrap/TBA equations to their proper
  evidence class unless the missing Hilbert-space, convergence, nuclearity,
  mirror-continuation, or hydrodynamic-limit assumptions are supplied.
- 2026-06-04 wedge-local reconstruction pass: added the operational residual
  split from \(S\)-Fock/ZF data to double-cone local observables and
  registered `factorized_scattering_algebra_checks.py` as an evidence-contract
  companion.  The finite check verifies that exact scattering algebra does not
  erase modular-nuclearity or local-intersection residuals, and includes
  negative controls for empty local intersections and failed nuclearity
  proxies.
- 2026-06-05 issue #728 route-map pass: added the end-to-end observable
  reconstruction map, turning the Volume VI reconstruction map into explicit
  model routes for Ising,
  sinh-Gordon, Lee--Yang TBA, and GHD.  The companion check verifies the route
  checkpoint logic and negative controls against treating exact scattering, exact TBA
  endpoints, or exact GHD dressing as local-observable or microscopic-current
  reconstruction.
- 2026-06-05 GHD transport coherence hook: clarified in the route map that
  Drude/transport claims require a real-time KMS/Kubo checkpoint in addition to the
  Euler GHD current coordinate.
- 2026-06-06 issue #844 observable-map pass: renamed the end-to-end route
  ledger as an observable reconstruction map, clarified that residual slots are
  not summable estimates until common-norm bounds are supplied, and extended
  `factorized_scattering_algebra_checks.py` with a negative control against
  hiding nonzero projection residuals as irrelevant.
- 2026-06-06 issue #844 status-surface pass: demoted the wedge-local
  reconstruction and end-to-end observable maps from controlled-approximation
  surfaces to remarks.  The formulas are retained as proof-obligation and
  conditional propagation maps: they classify where local-algebra,
  nuclearity, form-factor, state-limit, and projection estimates enter a
  physical observable, but they are not controlled estimates until those
  estimates are supplied in a common topology.
- 2026-06-09 issue #966 repair: renamed the higher-spin proposition so it
  claims only elastic permutation support and absence of generic production;
  inserted the no-diffraction pairwise-collision gate and a conditional
  factorization proposition before the chamber-groupoid construction; updated
  `factorized_scattering_algebra_checks.py` with a finite three-body phase
  negative control showing that additive charges alone do not imply pairwise
  factorization.
