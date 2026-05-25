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

## Claim Ledger

- States the vacuum-net Haag--Ruelle theorem under locality, covariance,
  spectrum condition, isolated massive shell, and sufficiently many regular
  creators.
- Separates the existence of an isolated shell from perturbative pole
  language and from global asymptotic completeness.
- Proves the Gauss-law obstruction: bounded local gauge-invariant observables
  cannot create charged vectors from a neutral vacuum.
- Defines the dressed charged LSZ problem for noncompact gauge-invariant
  charged creators and records the data that must replace local
  Haag--Ruelle creators.
- Derives the abelian Wilson-line boundary-charge transformation and the
  nonabelian parallel-transporter transformation law.
- States the missing large-time commutator estimate for noncompact charged
  dressings as the core unsolved Haag--Ruelle replacement.
- Proves a finite-regulator dressed LSZ theorem under explicit Hilbert-space,
  pole, and dressed-wave-operator hypotheses.
- Shows that compact dressing changes with fixed asymptotic flux are
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
  normalization for the soft coherent velocity-separation coefficient.

## Open Problems

- Complete the nonperturbative charged-sector Haag--Ruelle theorem for
  noncompact gauge-invariant charged dressings, including the replacement for
  the almost-local commutator estimate and the representation theory of
  asymptotic flux sectors.
- Combine that theorem with the infraparticle analysis of massless QED and
  with detector-inclusive probabilities.
