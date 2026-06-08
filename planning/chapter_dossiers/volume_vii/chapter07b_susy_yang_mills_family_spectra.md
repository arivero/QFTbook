# Chapter 07b: Spectral Bridges Among Supersymmetric Yang--Mills Cousins
Source-File: monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex

## Source Position

Volume VII places this compiled Chapter 7b immediately after the
four-dimensional `N=2` Seiberg-Witten chapter and before the general
supersymmetric moduli-space chapter.  Its role is to compare spectral
questions across `N=4`, `N=2`, `N=1`, and bosonic Yang-Mills relatives without
identifying protected holomorphic data with nonchiral masses or string
tensions.

The chapter depends on:

- Volume VII Chapter 3 for supersymmetric gauge-theory conventions.
- Volume VII Chapter 4 for Wilsonian holomorphic schemes.
- Volume VII Chapter 6 for pure `N=1` SYM branch, wall, and spectral
  conjecture status.
- Volume VII Chapter 7 for Seiberg-Witten periods, BPS charges, local
  Abelian patches, and monopole condensation.
- Volume VII Chapters 12--15 for the planar `N=4` spectral row.
- Volumes II, IX, and XI for bosonic Yang-Mills, line sectors, confinement
  status, and lattice transfer-matrix language.

## Notation Inventory

- `G`, `N_c`: gauge group, usually `SU(N_c)`.
- `V`, `Phi_i`: `N=1` vector and adjoint chiral multiplets used to present
  `N=4` Yang-Mills.
- `tau`, `q`: holomorphic coupling and instanton coordinate
  `q=exp(2 pi i tau)`.
- `m_h`, `m_i`, `mu`, `m_lambda`: hypermultiplet mass, adjoint chiral masses,
  `N=2 -> N=1` soft superpotential mass, and soft gaugino-mass spurion.
- `Lambda_{N=2}`, `Lambda_{N=1}`, `Lambda_h`: holomorphic low-energy scale
  coordinates.
- `S`, `u`, `a_D`, `a`, `Z_gamma`: pure `N=1` glueball coordinate,
  Seiberg-Witten Coulomb coordinate, periods, and BPS central charge.
- `W_R(C)`, `H_m(C)`: Wilson and magnetic line operators with declared line
  lattice.
- `T_k`, `E_k(L)`, `R_k`: `k`-string tension, finite-length center-flux
  energy, and normalized tension ratio.
- `Gamma_k(t)`: logarithmic response controlling transport of normalized
  string-tension ratios along a deformation path.
- `R_k^sine`, `R_k^Casimir`: finite comparison functions for center-string
  tension ratios.
- `K_ij`, `xi_i`, `s_i`: `A_{N_c-1}` Cartan matrix, Abelian FI coordinates,
  and sine eigenvector in the Abelianized Seiberg-Witten string example.
- `C_+`, `C_-`, `C_F`, `delta_SUSY`: pure-SYM scalar, pseudoscalar,
  fermionic correlator matrices and the supersymmetry-restoration spectral
  diagnostic.
- `H_{a,L}(m)`, `V_{a,L}(m)`, `P_n(m)`: common regulated soft-mass
  Hamiltonian path, perturbing Hamiltonian derivative, and Riesz projection
  for an isolated finite-volume spectral cluster.

## Claim Ledger

- Defines a Yang-Mills cousin comparison problem as a package of global form,
  line lattice, deformation parameters, observable class, and theorem-status
  label.
- Derives holomorphic threshold matching for `N=4 -> N=2` and
  `N=4 -> N=1` scale coordinates.  This is chiral Wilsonian bookkeeping, not
  a nonchiral spectrum computation.
- Records the `N=1*` critical equations and fuzzy-sphere algebra as chiral
  vacuum data, with the massive spectrum left to nonchiral dynamics.
- Separates chiral local, massive local spectral, center-line, and defect
  spectral observables in a family comparison table.
- States a controlled threshold comparison for low-momentum nonchiral
  correlators: massive fields produce local Wilsonian operators under stated
  regulator and gap hypotheses, while numerical masses and string tensions
  remain spectral problems.
- Defines `k`-string tension extraction through transfer-matrix or Wilson-loop
  data and distinguishes finite sine/Casimir comparison identities from
  QFT-derived string tensions.
- Records the pure bosonic Yang-Mills row as a central-conjecture and
  spectral-extraction target rather than a theorem.
- Records the pure `N=1` SYM row: chiral branch phases and BPS walls are
  protected or conjectural as stated in Chapter 6, while glueball,
  gluinoball, and flux-string masses are spectral data.
- Defines regulated pure-SYM source matrices and the
  `delta_SUSY` multiplet-restoration diagnostic for continuum,
  thermodynamic, and massless-gluino limits.
- Derives the local Seiberg-Witten Abelian vortex equations, flux, and BPS
  tension near a monopole point.
- Defines the Abelianized `A_{N_c-1}` string construction and proves the
  finite sine-profile identities inside that low-energy Abelian chart.
- Replaces the tautological Seiberg-Witten-to-pure-Yang-Mills transfer claim
  by a derivative criterion:
  `log(R_k(t1)/R_k(t0)) = integral Gamma_k dt`.  The Abelian sine ratio is an
  initial datum unless a common-regulator bound on `Gamma_k` is supplied.
- States the soft gaugino-mass branch-selection response at small
  `m_lambda`.
- Constructs a finite-volume controlled soft-mass spectral bridge segment:
  common regulator and tuning path, renormalized perturbing Hamiltonian
  derivative, Riesz projection transport for isolated local and flux-sector
  windows, Feynman-Hellmann formulas for mass and tension responses, and
  phase-boundary diagnostics.  Large soft-mass decoupling to bosonic
  Yang-Mills remains an open endpoint problem.

## Calculation Checks

- `calculation-checks/susy_yang_mills_family_checks.py` verifies finite
  algebra for pure-SYM root-of-unity wall tensions, one-coordinate chiral
  mass normalization, the Seiberg-Witten monopole-condensate `F`-term
  equation, and Abelian vortex square completion.
- `calculation-checks/susy_yang_mills_deformation_ladder_checks.py` verifies
  holomorphic scale dimensions, the `N=1*` fuzzy-sphere ansatz, sine/Casimir
  `k`-string comparison identities, local vortex flux and small-radius
  normalization, the Abelianized `A`-type sine eigenvector and subadditivity
  algebra, pure-SYM channel-pole diagnostic bookkeeping, finite soft-mass
  Riesz-projection and Feynman-Hellmann transport, and a negative control
  rejecting constant ratio transfer when the logarithmic tension response is
  nonzero.

These checks are finite normalization and algebra companions.  They do not
prove the nonperturbative existence of the pure-YM endpoint, spectral
continuity along a full soft-breaking path, or equality of Abelianized and
bosonic string tension ratios.  The deformation-ladder check now carries an
extended evidence contract.

## Source Notes

The chapter uses the monograph's own earlier definitions and theorem
boundaries rather than importing a claimed universality of supersymmetric
string ratios.  Seiberg-Witten local Abelian calculations are treated as
effective-theory outputs inside their patch.  Their transport to bosonic
Yang-Mills requires an additional regulator-level spectral argument.

## Figure Ledger

No figure is included in the current chapter.  Useful future figures would be
a deformation-ladder diagram with status labels, a center-flux transfer-matrix
extraction schematic, and an Abelianized Seiberg-Witten patch diagram showing
which data are local and which require a global deformation argument.

## Anti-Wrapper And Depth Audit

- 2026-06-08 issue #928 dossier pass: added the missing Chapter 7b dossier as
  a planning record tied to the compiled source key.  The dossier records the
  current chapter as a comparison map plus finite Abelian checks, not as a
  completed nonperturbative spectral bridge.
- Physics-depth warning: adding this dossier is infrastructure for #927.  The
  depth frontier remains the construction of one controlled bridge, preferably
  a soft-gaugino-mass spectral projection transport or an explicitly
  bounded Seiberg-Witten Abelian string approximation with regulator-level
  deformation diagnostics.
- 2026-06-08 issue #927 pass: replaced the constant-ratio transfer paragraph
  by a logarithmic-response criterion and added a controlled small-soft-mass
  spectral bridge segment with finite-volume Riesz projections,
  Feynman-Hellmann mass/tension responses, and explicit failure diagnostics.
  The pass improves the physics architecture while preserving the theorem
  boundary: it does not claim the path reaches bosonic Yang-Mills.
