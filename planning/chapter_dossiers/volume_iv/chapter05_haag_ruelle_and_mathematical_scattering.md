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
- `Psi_{q,gamma}`: gauge-invariant noncompact charged creator with Wilson-line
  or Coulombic dressing.
- `J_{q,u,epsilon}`: regulated asymptotic worldline current for velocity
  `u=p/m`.
- `E_{q,v}(n)`: boosted Coulomb angular flux density on the celestial sphere.
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
- Defines the dressed charged LSZ problem for noncompact gauge-invariant
  charged creators and records the data that must replace local
  Haag--Ruelle creators.
- Derives the abelian Wilson-line boundary-charge transformation and the
  nonabelian parallel-transporter transformation law.
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
- Proves a finite-regulator dressed LSZ theorem under explicit Hilbert-space,
  pole, and dressed-wave-operator hypotheses.
- Shows in prose that compact dressing changes with fixed asymptotic flux are
  coordinate changes at the level of LSZ residues, while changes of the
  asymptotic flux change the charged sector.
- Derives the half-line worldline-current Fourier transform and the eikonal
  denominator \(p\cdot k\) in the Faddeev--Kulish soft profile.
- Proves that the boosted Coulomb flux integrates to the charge and that, for
  nonzero charge, the angular flux density determines the charged velocity.
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
  momentum-space eikonal denominators, and sample positivity plus logarithmic
  normalization for the soft coherent velocity-separation coefficient.  It
  also checks the finite-dimensional Weyl/coherent characteristic functional
  and the monotone decay of the coherent overlap as the infrared cutoff is
  removed.  The same script now checks the finite Hilbert soft-coordinate
  transformation law and strong-continuity behavior on coherent vectors.
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
