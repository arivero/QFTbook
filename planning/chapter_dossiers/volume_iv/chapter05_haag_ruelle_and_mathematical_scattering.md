# Chapter 05: Haag--Ruelle Theory And Mathematical Scattering

## Source Position

This chapter is the theorem-level scattering chapter for local nets.  It
supports the introductory Haag--Ruelle chapter in Volume I and supplies the
precise boundary between ordinary massive scattering and the modified
scattering problems of gauge theories, infraparticles, confinement, and
resonances.

## Notation Inventory

- `R(O)`: local von Neumann algebra of the vacuum net.
- `H`, `Omega`: physical Hilbert space and vacuum vector.
- `U(a,Lambda)`, `P^mu`, `E(Delta)`: Poincare representation, translation
  generators, and joint spectral projections.
- `Sigma_m^+`, `H_1`: positive mass shell and isolated one-particle subspace.
- `B_t(h)`: Haag--Ruelle approximant built from an almost-local regular
  creator and a positive-energy wave packet.
- `Omega_in/out`: Haag--Ruelle wave operators.
- `Q_R`, `Q`: large-sphere Gauss-law charge approximants and limiting charge.
- `H_q`, `U_q`, `Phi_infty(f)`: physical charged representation, its
  translation representation, and angular Gauss-law flux operator in the
  nonconfining charged-sector hypothesis.
- `Psi_{q,gamma}`: gauge-invariant noncompact charged creator with Wilson-line
  or Coulombic dressing.
- `Psi_{q,Gamma;L,epsilon}`, `L_i(t)`, `epsilon_i(t)`: finite-length and
  ultraviolet-regularized representatives of a noncompact charged dressing,
  together with admissible large-time truncation schedules used to define the
  charged asymptotic coordinate.
- `S_{gamma',gamma}`: compact oriented surface swept out by two Wilson-line
  dressings with the same endpoint and asymptotic ray; its boundary is the
  difference of the truncated paths, `gamma'_R-gamma_R`.
- `epsilon_a q_a`: signed boundary charge of a dressed insertion in a
  time-ordered correlator; `epsilon_a=+1` for `Psi_{q_a,gamma_a}` and
  `epsilon_a=-1` for its adjoint.
- `J_{q,u,epsilon}`: regulated asymptotic worldline current for velocity
  `u=p/m`.
- `E_{q,v}(n)`: boosted Coulomb angular flux density on the celestial sphere.
- `mathfrak F`, `mathfrak F'`: angular Gauss-law flux characters used to
  project dressed LSZ residues onto matching charged superselection blocks.
- `F_{q,v,lambda,Lambda}`: finite-cutoff soft coherent profile determined by
  the charged velocity.
- `A(v,w)`: positive angular coefficient controlling the infrared logarithm
  in the norm difference between two charged soft profiles.
- `h_{0,Lambda}`, `W(f)`, `sigma(f,g)`: fixed infrared-sensitive photon
  one-particle space, Weyl operator, and real symplectic form.
- `D_{lambda,Lambda}`: difference between two finite-cutoff charged soft
  profiles with distinct velocities.
- `Delta`: finite Hilbert-space soft-coordinate change between two
  infrared-regulated dressings.
- `Theta_I(t)`, `eta_i`, `kappa_{ij}`, `u_{ij}`: modified charged
  comparison phase, creator/adjoint orientation sign, effective pairwise
  long-range coefficient, and relative velocity in the Dollard/Faddeev-Kulish
  comparison calculation.

## Claim Ledger

- States the vacuum-net Haag--Ruelle theorem under locality, covariance,
  spectrum condition, isolated massive shell, and sufficiently many regular
  creators.
- Defines the Haag--Ruelle estimate package and proves that the Cook estimate,
  recursive contraction estimate, and one-particle contraction estimate imply
  existence of incoming/outgoing limits, independence of interpolating
  creators, and the bosonic Fock inner-product permanent.
- Proves the stationary-phase velocity-localization lemma and the derivation
  of the almost-local commutator estimate from spacelike separation of
  velocity tubes.
- States the Cook derivative estimates as strong finite-energy estimates
  for smooth spectrally smeared Haag--Ruelle creators, avoiding any hidden
  assumption that unsmeared bounded local operators are norm differentiable.
- Separates the existence of an isolated shell from perturbative pole
  language and from global asymptotic completeness.
- Proves the Gauss-law obstruction: bounded local gauge-invariant observables
  cannot create charged vectors from a neutral vacuum.
- Derives the stronger almost-local obstruction: an operator almost local with
  respect to the gauge-invariant observable net still creates a neutral vector
  from the vacuum, provided the Gauss-law charge is closed on the local
  domain.  Thus a nonzero charged creator cannot be hidden inside the
  ordinary Haag--Ruelle almost-local hypothesis.
- States the nonconfining charged sector as an explicit hypothesis
  before dressed LSZ is formulated: a physical charged representation,
  boundary charge and angular flux operators, flux preservation by compact
  observables, finite-energy asymptotic content through an isolated charged
  shell or an infraparticle threshold structure, noncompact charged creators with
  nonzero asymptotic projection or coefficient, and spectral tightness of
  normalized truncated dressings on the admissible large-time schedules.
  Uniform first-moment control is recorded only as a sufficient estimate for
  this spectral tightness.  A spectral string-energy lower bound
  \(E_{\rm vac}+\sigma L-o(L)\) with \(\sigma>0\) is recorded as absence of
  the finite-energy charged asymptotic sector.
- Defines the dressed charged LSZ problem for noncompact gauge-invariant
  charged creators and records the data that must replace local
  Haag--Ruelle creators.
- States the truncation topology required before a noncompact Wilson-line
  charged creator can be used in a Haag--Ruelle theorem: finite dressings
  \(\Psi_{q,\Gamma;L,\varepsilon}\) must have a renormalized matrix-element
  limit, and same-flux admissible schedules \(L_i(t)\to\infty\),
  \(\varepsilon_i(t)\downarrow0\) must give uniformly equivalent modified
  comparison vectors with vanishing norm tails and \(L^1\) Cook tails.  This
  separates genuine large-time control from fixed-time convergence of formal
  infinite Wilson lines.
- Defines the finite dressed-residue coordinate algebra for an
  infrared-regulated charged isolated shell: the pole matrix is the Gram
  matrix of charged one-particle overlaps, a left inverse of the overlap map
  extracts normalized external charged amplitudes, and finite invertible
  dressing-coordinate changes preserve the extracted residue.  The text
  explicitly separates this coordinate statement from changes of asymptotic
  Gauss-law flux.
- Derives the abelian Wilson-line boundary-charge transformation and the
  nonabelian parallel-transporter transformation law.
- Adds the boundary-charge Ward selection rule for dressed correlators:
  vacuum matrix elements of abelian dressed insertions vanish unless the
  signed endpoint charges sum to zero, while nonabelian endpoint labels must
  be projected to invariant tensors in the boundary representation tensor
  product.  The text separates this exact algebraic constraint from the
  dynamical existence of finite-energy charged asymptotic particles.
- Adds the flux-sector projection that refines boundary-charge selection
  before dressed LSZ residues are extracted: the simultaneous external-shell
  residue is block diagonal in angular Gauss-law flux characters, so a
  vacuum-to-vacuum residue requires equality of the full angular flux profile
  rather than only the charge zero mode.  Finite same-flux coordinate changes
  act inside a single block; matrices mixing different angular flux characters
  are sector changes, not harmless dressing-coordinate changes.
- Gives the finite-ray abelian calculation that a Wilson-line dressed charged
  coordinate is the ordinary charged coordinate on the axial gauge slice
  \(u^\mu A_\mu=0\), under explicit endpoint and decay assumptions, and
  derives the associated \((k\cdot u-\ii0)^{-1}\) line denominator from the
  regulated half-line Fourier transform.
- Refines the missing large-time estimate for noncompact charged dressings
  into a charged Haag--Ruelle replacement package: dressed creators with
  charge, dressing geometry, limiting flux and multiplicity labels; a
  velocity-separated exchange estimate with possible Dollard/Faddeev--Kulish
  phase; a modified Cook estimate after subtracting the comparison phase; and
  scalar-product limits in the correct asymptotic representation.
- Identifies the geometric replacement for ordinary spacelike separation in
  charged sectors: the compact velocity cores can separate linearly, but the
  noncompact Gauss-law tails attached to the dressing cones/rays remain and
  must be decomposed into tail--tail flux pairing plus an \(L^1\) remainder.
  This prevents the charged estimate from being misread as ordinary almost
  locality in disguise.
- Works out the finite-dimensional Coulomb-tail model behind the comparison
  phase: for \(V(t)=\kappa/\sqrt{a^2+|b+ut|^2}\), the pair phase is
  \((\kappa/|u|)\log t+O(1)\).  This identifies exactly why a \(t^{-1}\)
  long-range charged pair term must be subtracted rather than treated as a
  Cook-integrable error.
- Specifies the finite many-body Dollard bookkeeping required by the charged
  theorem target: after short-range terms are separated, nonintegrable tails
  must be exhausted by oriented velocity-separated pair fluxes with signs
  \(\eta_i\eta_j\), while the residual derivative enters the Cook estimate
  only through an \(L^1\) remainder.  Equal-velocity charged pairs are
  explicitly excluded from this datum and must be treated as charged clusters
  or separate infraparticle/bound-state sectors.
- Adds the scalar-product Cauchy criterion for charged modified comparison
  vectors: uniform norm bounds and \(L^1\) modified-Cook derivative bounds
  imply Cauchy scalar products in the charged asymptotic representation,
  whereas a wrong logarithmic Dollard coefficient leaves the nonconvergent
  factor \(\exp(i\delta\log t)\).
- Adds the finite null-quotient ledger behind the charged Dollard--Cook
  wave-map construction: an overcomplete asymptotic symbol frame with Gram
  matrix
  \(\begin{psmallmatrix}1&0&1\\0&1&1\\1&1&2\end{psmallmatrix}\) has null
  relation \(e_1+e_2-e_3=0\), so packet-refinement and same-flux coordinate
  redundancies are removed by the Hilbert-space quotient before the wave map
  becomes isometric.
- Proves the same-flux schedule-invariance bridge for the charged
  Dollard--Cook package: if two admissible truncation schedules have vanishing
  modified-comparison-vector tails up to a finite phase, then their physical
  charged wave maps and asymptotic Gram forms agree after the corresponding
  finite coordinate identification.  The same proposition records how a
  same-flux coordinate matrix in the dressed-correlator interface cancels
  against the transformed left inverses, so the external-shell residue
  coefficient is not schedule-dependent.
- Proves a finite-regulator dressed LSZ theorem under explicit Hilbert-space,
  pole, and dressed-wave-operator hypotheses.  The theorem now distinguishes
  the general rectangular dressed-coordinate case, handled by a left inverse
  of the one-particle overlap map, from the displayed square-frame
  \(Z^{-1/2}\) formula, which requires an invertible Gram matrix after
  choosing a full-rank coordinate frame.
- States the dressed-correlator reduction interface that a Wilson-line LSZ
  theorem must prove before correlator residues can be identified with
  charged wave-map matrix elements.  The interface requires boundary-value
  distributions for renormalized finite-truncation dressed coordinates,
  uniformity over same-flux truncation schedules, a finite-rank simultaneous
  external-shell singular expansion, control or absorption of endpoint,
  cusp, and collision contact terms, and covariance under finite same-flux
  coordinate changes.  It is explicitly a hypothesis naming the analytic
  burden, not a theorem about noncompact charged sectors.
- Shows that compact abelian Wilson-line dressing changes with fixed
  asymptotic flux are field-strength surface insertions:
  \(\int_{\gamma'_R}A-\int_{\gamma_R}A=\int_{S_{\gamma',\gamma}}F\).
  The resulting neutral compact factor changes the LSZ overlap coordinates
  but not the boundary charge or flux sector.  The nonabelian analogue is
  recorded as the covariantly transported curvature-insertion formula for the
  first variation of a parallel transporter.  Changes of the asymptotic ray
  are kept separate because they change the charged infrared sector.
- Derives the half-line worldline-current Fourier transform and the eikonal
  denominator \(p\cdot k\) in the Faddeev--Kulish soft profile.
- Proves that the boosted Coulomb flux integrates to the charge and that, for
  nonzero charge, the angular flux density determines the charged velocity.
- Separates total boundary-charge neutrality from equality of angular
  Gauss-law flux sectors: a neutral dressed correlator obeys only the
  zero-mode Ward condition, while opposite charges at distinct asymptotic
  velocities can still carry a nonzero limiting angular flux profile.
- Proves that finite-cutoff soft coherent profiles with distinct charged
  velocities have a norm difference proportional to
  \(\log(\Lambda/\lambda)\mathcal A(v,w)\), with
  \(\mathcal A(v,w)>0\) off the diagonal; this gives the explicit
  finite-Fock calculation behind velocity-labelled charged sectors.
- Defines the finite-cutoff Weyl algebra, derives the coherent-state
  characteristic functional, and proves that the Weyl implementers changing
  between distinct charged velocities have no strong operator limit and no
  nonzero weak operator limit as the infrared cutoff is removed.
- Defines Hilbert-equivalent soft dressings and proves that such finite soft
  changes are inner Weyl coordinate changes with strongly convergent
  implementers; this separates harmless soft reparametrizations from genuine
  changes of charged infrared sector.
- Constructs the velocity-fibered soft representation
  \(\int^\oplus \mathcal H_{\mathbf v}\,d\nu(\mathbf v)\) for infrared-regular
  Weyl tests and proves that the soft photon Weyl algebra preserves velocity
  fibers, so momentum-changing charged scattering dynamics cannot be an
  operator of the soft photon algebra alone.
- Restricts the dressed charged Haag--Ruelle/LSZ open problem explicitly to
  nonconfining charged sectors with finite-energy physical charged asymptotic
  data; in a confining phase the relevant asymptotic particles are neutral
  hadrons or glueballs, and ordinary Haag--Ruelle theory is the starting
  point when isolated shells exist.

## Figure Ledger

- No new figure was added in this pass. Future figures should display the
  noncompact Wilson-line dressing to infinity, the boosted Coulomb flux density
  on the celestial sphere, and the separation between local Haag--Ruelle
  creators and charged noncompact dressings.

## Calculation Checks

- `calculation-checks/charged_flux_dressing_checks.py` verifies the boosted
  Coulomb flux integral, the velocity read from flux extrema, the regulated
  half-line Fourier transform, the equality of worldline-current and
  momentum-space eikonal denominators, the Coulomb-tail logarithmic Dollard
  phase coefficient, the oriented pairwise many-body Dollard logarithm,
  decay of the log-subtracted Coulomb pair remainder on large dyadic time
  intervals, and sample positivity plus logarithmic normalization for the
  soft coherent velocity-separation coefficient.  It also checks the
  finite-dimensional Weyl/coherent characteristic functional and the monotone
  decay of the coherent overlap as the infrared cutoff is removed.  The same
  script now checks the finite Hilbert soft-coordinate transformation law and
  strong-continuity behavior on coherent vectors, as well as the
  finite-dimensional left-inverse algebra for dressed charged LSZ residues
  and its invariance under finite dressing-coordinate changes.  It now also
  checks the boundary-charge selection rule for abelian dressed correlators
  and elementary \(SU(2)\) endpoint singlet channels.  It now also verifies
  that boundary-charge neutrality is weaker than flux-sector triviality:
  opposite charges at the same velocity cancel the angular profile pointwise,
  whereas opposite charges at different velocities have vanishing total
  charge but a nonzero angular flux profile.  It now also verifies
  the finite abelian Stokes bookkeeping for compact Wilson-line path
  deformations: the change of line integral is a curvature surface flux, and
  the associated surface factor carries no endpoint gauge charge.  It now
  also checks the finite tail arithmetic behind the truncation topology:
  an unscheduled \(1/t\) noncompact tail is not a Cook error, whereas an
  admissible same-flux polynomial schedule produces decreasing norm tails
  and an \(L^1\) derivative tail.  It also checks the finite spectral-measure
  arithmetic behind the nonconfining-sector boundary: common finite-energy
  windows, Markov's first-moment sufficient bound, and linear string-energy
  escape beyond every fixed cutoff.  It now also checks the finite algebra of
  the dressed-correlator reduction interface: simultaneous simple
  external-shell poles survive the multi-leg residue extraction, partial
  external poles and contact terms are less singular, higher poles are
  outside the interface, and finite same-flux coordinate changes on each
  external leg leave the extracted wave-map coefficient invariant.  It now
  also checks the scalar-product Cauchy criterion after Dollard subtraction:
  summable derivative tails give decreasing dyadic inner-product bounds,
  while a wrong logarithmic phase leaves a persistent dyadic obstruction.
  It now also checks same-flux schedule invariance for charged wave maps and
  residues: rational schedule tails shrink to a common Hilbert limit and a
  cutoff-dependent finite coordinate transform leaves the left-inverse LSZ
  extraction exact.
- The direct-integral velocity-fiber proposition is purely algebraic and has
  no numerical companion: it is a decomposability statement for the
  representation of the Weyl algebra.
- `calculation-checks/haag_ruelle_fock_inner_product_checks.py` verifies the
  bosonic Fock inner-product recursion using exact rational permanent
  computations and particle-number orthogonality.

## Open Problems

- Complete the nonperturbative charged-sector Haag--Ruelle theorem for
  nonconfining sectors with noncompact gauge-invariant charged dressings,
  including the replacement for the almost-local commutator estimate and the
  representation theory of asymptotic flux sectors.
- Combine that theorem with the infraparticle analysis of massless QED and
  with detector-inclusive probabilities.

## Reference Intake Notes

- 2026-05-26 arXiv:2605.26077 intake: inspected the new paper
  \emph{On Perturbatively Dressed Observables}.  Only the independently
  checked finite-ray dressing/gauge-slice mechanism was absorbed.  The
  paper's loop-level singularity claims, perturbative-gravity claims, and
  finite-reference-system discussion were not imported as monograph results;
  they remain possible prompts for future derivations if needed.

## Anti-Wrapper Audit

- 2026-05-29: demoted the worldline-dressing eikonal denominator from
  proposition/proof to a worked Fourier-transform paragraph.  The calculation
  remains because it fixes the charged-dressing endpoint prescription, but its
  proof is a regulated half-line integral.
- 2026-05-29: strengthened the Gauss-law obstruction proof by spelling out
  the smeared large-sphere charge limit and domain pairing, and demoted the
  ray-dressing/axial-gauge and compact-dressing/LSZ-coordinate calculations
  from proposition/proof form to worked prose.
- 2026-05-30: retained `prop:almost-locality-gives-hr-commutator` as
  theorem-level Haag--Ruelle proof infrastructure and expanded its proof.  The
  proof now performs the near/tail split, derives the \(L^1\) wave-packet tail
  bound from stationary phase, chooses local approximants with radius
  \(R=\delta |t|/8\), checks spacelike separation of the translated double
  cones by comparing \(\delta |t|-2R\) with \(2R\), and absorbs the polynomial
  near-packet \(L^1\)-growth by the arbitrary-power almost-local approximation
  estimate.
- 2026-05-31: added the no-almost-local-observable-coordinate consequence for
  nonzero Gauss charge and rewrote the charged-sector missing-estimate
  discussion so the open theorem is localized in the exchange and modified
  Cook estimates, not in vague claims about Wilson-line nonlocality.
- 2026-05-31 issue #691 continuation: demoted that almost-local Gauss-law
  consequence from proposition/proof form to paragraph-level closed-operator
  prose.  The local Gauss-law obstruction theorem remains the substantive
  theorem-level result; the almost-local extension is the graph-closedness
  passage needed to identify the exact failure of the ordinary Haag--Ruelle
  localization hypothesis for unscreened charges.
- 2026-06-01 #527/#528 continuation: added the finite-dimensional Coulomb-tail
  comparison calculation that produces the logarithmic Dollard phase, so the
  missing charged Haag--Ruelle estimate now states not only that a comparison
  phase is needed but the exact asymptotic mechanism behind its \(t^{-1}\)
  derivative.
- 2026-06-01 #691 follow-up: demoted that Coulomb-tail comparison from
  proposition/proof form to paragraph-level worked calculation.  The formulae
  and calculation-check companion remain; the theorem-family burden stays on
  the charged Haag--Ruelle estimate, not on completed-square algebra.
- 2026-06-01 #527 continuation: added a non-theorem residue-coordinate
  synthesis before the Wilson-line covariance subsection.  The new text
  defines the overlap map from physical charged one-particle multiplicity
  space to dressed operator coordinates, identifies the two-point pole
  residue as its Gram matrix, and states the left-inverse extraction of a
  normalized external charged amplitude.  This clarifies the exact finite
  sense in which same-flux dressing changes are coordinate changes while
  preserving the open theorem debt for changes of asymptotic Gauss-law flux.
- 2026-06-01 #527 continuation: inserted the boundary-charge Ward selection
  rule immediately after Wilson-line covariance.  The pass keeps it as a
  structural paragraph rather than a proposition/proof: the point is the
  charge bookkeeping every dressed correlator must satisfy, not a new theorem
  family.  The paired check now covers abelian signed-charge neutrality and
  finite \(SU(2)\) singlet-channel bookkeeping.
- 2026-06-01 #527 continuation: expanded the compact path-deformation
  paragraph into explicit abelian Stokes bookkeeping and the nonabelian
  curvature-insertion formula for path-ordered transport.  This removes a
  vague "neutral Wilson loop" assertion and makes clear exactly which
  same-flux dressing changes are finite LSZ-coordinate changes, while leaving
  the asymptotic-ray problem as genuine charged-sector proof debt.
- 2026-06-02 #527 continuation: inserted a cone/flux decomposition paragraph
  in the missing-estimate subsection.  The text now states that velocity-core
  separation handles only the compact part of a dressed charged creator; the
  noncompact Gauss-law tail must be isolated as a flux-pairing comparison
  phase with an \(L^1\) residual, not treated as an almost-local commutator
  error.
- 2026-06-02 #527 continuation: added a non-theorem synthesis distinguishing
  signed boundary-charge neutrality from equality of the limiting angular
  Gauss-law flux profile.  The passage prevents a false path-independence
  inference: vanishing total charge is a necessary zero-mode Ward identity,
  not a statement that the charged asymptotic flux sector is trivial.
- 2026-06-06 #527 flux-sector LSZ projection pass: connected the angular
  flux distinction back to the dressed-correlator residue algebra.  The new
  prose block states the flux-character selection rule
  \(P_{\mathfrak F'}{\rm Res}^{\rm LSZ}_I(G)P_{\mathfrak F}=0\) unless the
  sector difference equals the full signed angular flux profile of the
  external list, and records the corresponding block form of the left-inverse
  overlap maps.  The companion check includes a negative control where a
  charge-only selector would accept a flux-nonzero neutral pair in the
  vacuum block.
- 2026-06-01 #527 continuation: added finite many-body Dollard bookkeeping
  after the one-pair Coulomb-tail calculation.  The new paragraph defines the
  creator/adjoint signs, the pairwise derivative of the comparison phase, the
  logarithmic coefficient \(\sum_{i<j}\eta_i\eta_j\kappa_{ij}/|u_{ij}|\), and
  the velocity-separation boundary.  It remains prose and equations rather
  than theorem/proof form because the substantive theorem is the QFT estimate
  deriving the pair coefficients and the \(L^1\) remainder.
- 2026-06-01 #527 continuation: formalized the abstract charged
  Dollard--Cook estimate package as a hypothesis and added the Hilbert-space
  construction of charged wave maps from it.  The construction proves the
  Cauchy/null-vector/isometry part once the \(L^1\) modified-Cook and
  scalar-product estimates are known, while explicitly leaving the
  nonperturbative Wilson-line/Coulomb-dressed QFT estimates as the open
  load-bearing problem.  The paired charged-flux calculation check now
  includes a discrete Cook-tail model distinguishing an unsubtracted \(1/t\)
  Dollard derivative from an \(L^1\) residual.
- 2026-06-02 #527 continuation: inserted the nonconfining charged-sector
  datum before the dressed LSZ definition.  The pass makes explicit that a
  charged Haag--Ruelle/LSZ problem needs positive spectral and
  representation-theoretic input: a physical charged representation with
  angular Gauss-law flux, compact-observable flux preservation, an isolated
  charged shell or infraparticle threshold datum, noncompact charged creators
  with nonzero asymptotic projection/coefficient, and tight finite-energy
  truncated dressings.  A positive string-tension law for charged truncations
  is recorded as absence of this datum, so confinement is separated from an
  infrared regulator issue.
- 2026-06-02 #527 coordinate-rank refinement: tightened the finite-regulator
  dressed LSZ theorem so the square-root normalization is used only after a
  full-rank square dressed-coordinate frame has been chosen.  Overcomplete or
  rank-deficient operator families remain governed by the earlier
  left-inverse residue extraction formula; the theorem no longer hides this
  coordinate choice inside \(Z^{-1/2}\).
- 2026-06-02 #527 spectral-tightness refinement: replaced the expectation-only
  finite-energy condition in the nonconfining charged-sector hypothesis by
  spectral tightness of the Hamiltonian measures for normalized truncated
  dressings on admissible schedules.  The text now treats a uniform
  first-moment bound as a sufficient route via Markov's inequality, and states
  the confining alternative as a spectral string-energy lower bound rather
  than as a vague high-energy trial-state expectation.  The companion
  charged-flux check verifies the finite arithmetic behind this boundary.
- 2026-06-02 #527 coefficient-residual refinement: inserted an explicit
  non-theorem paragraph identifying the QFT estimate that remains to be
  proved.  For velocity-separated charged packet data, the theorem must
  construct the flux-pairing coefficient
  \(\kappa(\Gamma_i,\Gamma_j)\), a scalar pair kernel
  \(K_{ij}^{\#\#}(t)\), and an operator residual
  \(\mathcal R_{ij}^{\#\#}(t)\) satisfying an \(L^1\) scattering-domain
  bound after the \(1/t\) Dollard term has been subtracted.  The text now
  states that a wrong coefficient leaves a nonintegrable
  \(\delta\kappa/(|u_{ij}|t)\) Cook tail, while compact same-flux dressing
  changes contribute only \(L^1\) derivatives and finite comparison phases.
  The charged-flux companion check now verifies this finite dyadic arithmetic
  and the equal-velocity boundary.
- 2026-06-02 #527 scalar-product Cauchy pass: added the functional-analytic
  estimate that turns uniform bounds plus \(L^1\) modified-Cook derivative
  tails into Cauchy scalar products of charged comparison vectors.  The
  manuscript now records that an incorrect logarithmic Dollard coefficient
  leaves \(\exp(i\delta\log t)\), hence no scalar-product limit.  The
  companion check verifies the dyadic Cauchy bound, the wrong-phase
  obstruction, and finite same-flux phase changes.
- 2026-06-03 #527 null-quotient pass: added the finite asymptotic
  Gram/null-quotient cell after the charged Dollard--Cook wave-map
  construction.  The worked ledger shows explicitly how the null relation
  \(e_1+e_2-e_3=0\) makes an overcomplete same-flux/refinement frame descend
  to a genuine asymptotic Hilbert vector and isometric wave map.  The
  charged-flux companion check verifies the Gram matrix, null relation, and
  refinement equivalence by exact rational arithmetic.
- 2026-06-03 #527 schedule-invariance pass: added the same-flux
  schedule-invariance proposition after the abstract charged wave-map
  construction.  This remains theorem-level because it proves how the
  already-declared truncation topology propagates through the charged wave map,
  the asymptotic Gram form, and the finite-coordinate LSZ extraction; the
  nonperturbative exchange and modified-Cook estimates remain the open analytic
  burden.
