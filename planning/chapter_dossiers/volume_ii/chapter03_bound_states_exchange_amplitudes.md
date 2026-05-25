# Volume II, Chapter 3 Dossier: Bound States from Exchange Amplitudes

## Source Placement

- Follows the construction of scattering kernels, connected amplitudes, LSZ,
  and cluster decomposition.
- Begins the source sequence on bound states and resonances by treating stable
  poles below the two-particle threshold.
- Stops before the unstable-particle/resonance self-energy analysis, which
  belongs to the next chapter.
- Source material used:
  - rendered handwritten trace
    `monograph/tex/build/source_visual_trace/253b_trace-013.png` through
    `253b_trace-017.png`;
  - `transcription/tex/253b/scattering_rg_qcd.tex`, roughly lines 430--704;
  - Volume II chapters 1--2 for spectral data, connected kernels, and LSZ.

## Framework

- Four-dimensional massive scalar theory with two real scalar fields
  \(\phi_1,\phi_2\), masses \(m_1,m_2>0\), and cubic interaction
  \(-g\phi_1^2\phi_2/2\).
- The scalar Lagrangian is an exchange-model source of a tree kernel in the
  logical sense fixed by Volume II Chapter 1: finite-cutoff perturbative/EFT
  data unless an exact massive local QFT with the stated spectral properties is
  separately supplied.
- Tree-level perturbation theory is used only for the connected
  \(\phi_1\phi_1\to\phi_1\phi_1\) amplitude after LSZ.
- Bound-state identification is stated as an analytic scattering criterion:
  a pole below a two-particle threshold represents a stable one-particle state
  coupled to that channel. Whether the state is elementary or composite is
  extra microscopic information.
- Existence of a composite below-threshold pole is treated as a dynamical
  spectral input, not as something derived from the Lagrangian by general
  principles.
- The simple-pole criterion assumes an isolated finite-multiplicity spectral
  point with nonzero channel overlap and a nonzero gap from the threshold.
  Near-threshold, unitary-limit, and Efimov-accumulation regimes require a
  separate threshold analysis in the relative momentum variable; the pole may
  collide with the branch point or cease to be isolated.
- When the same question is formulated through a Bethe--Salpeter kernel, the
  later analytic Fredholm theorem supplies the precise operator hypotheses;
  this chapter's below-threshold pole criterion is not a hidden proof that a
  truncated kernel eigenvalue produces an exact Hilbert-space particle.
- The first/second sheet convention is introduced here before first use:
  first sheet means the analytic germ reached from the Feynman physical
  upper-edge boundary value, a below-threshold first-sheet point is reached
  without crossing the threshold cut, and the second sheet relative to a
  channel is the adjacent germ obtained by continuing through that channel cut.
- A short-range one-dimensional Schrödinger problem is used as a controlled
  mathematical model for the pole criterion.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\phi_1,\phi_2\) | scalar fields in the exchange model |
| \(m_1,m_2\) | corresponding mass parameters |
| \(g\) | cubic coupling in \(-g\phi_1^2\phi_2/2\) |
| \(s,t,u\) | mostly-plus Mandelstam invariants \(s=-(k_1+k_2)^2\), \(t=-(k_1-k_3)^2\), \(u=-(k_1-k_4)^2\) for incoming \(k_1,k_2\) and outgoing \(k_3,k_4\) |
| \(E\) | center-of-mass energy |
| \(z=\cos\theta\) | scattering-angle variable |
| \(\mathcal M(s,z)\) | connected invariant amplitude |
| \(a_\ell(s)\) | ordered \(16\pi\) partial-wave amplitude, same convention as Volume I Chapter 14 |
| \(S_\ell(s)\) | elastic partial-wave scattering eigenvalue |
| \(\beta(s)\) | two-body elastic kinematic factor \(\sqrt{1-4m^2/s}\), not a spectral measure |
| first sheet | physical stable-channel analytic germ reached without crossing the relevant threshold cut |
| second sheet | adjacent germ obtained by crossing a specified channel cut; in multichannel problems the crossed cuts must be named |
| \(M_B\) | bound-state mass below threshold |
| \(k\) | nonrelativistic relative momentum |
| \(E_{\mathrm{nr}}\) | nonrelativistic energy |
| \(\mathcal N(E)\) | normalization of delta-normalized two-particle partial-wave states |

## Claims Established

- The tree-level exchange model has \(s\)-, \(t\)-, and \(u\)-channel poles
  with positions fixed by \(m_2\).
- The equal-mass physical \(s\)-channel kinematics are
  \(s=E^2\), \(t=-(E^2-4m_1^2)(1-z)/2\), and
  \(u=-(E^2-4m_1^2)(1+z)/2\), so \(t,u\le0\) on the physical angular
  interval.
- For \(m_2<2m_1\), the \(s\)-channel pole lies below the
  \(\phi_1\phi_1\) threshold and has the scattering signature of a stable
  state coupled to the two-\(\phi_1\) channel.
- In short-range nonrelativistic scattering, bound states correspond to poles
  of the analytically continued scattering function at \(k=\ii\alpha\),
  \(\alpha>0\).
- In relativistic partial waves, a stable spin-\(\ell\) state below threshold
  gives a pole in \(a_\ell(s)\) or \(S_\ell(s)\) at
  \(s=M_B^2<4m^2\).
- The partial-wave state normalization is explicitly recorded in the
  chapter: for identical scalar bosons
  \(\mathcal N(E)=(2E/(k\omega_1\omega_2))^{1/2}\), only even \(\ell\)
  occur, and open inelastic channels imply \(|S_\ell(E)|\le1\) for the
  elastic component.
- The chapter distinguishes this unordered identical-boson normalization from
  the ordered \(16\pi\) invariant-amplitude expansion and from
  distinguishable equal-mass channels, where odd partial waves are present.
- A scalar-QED photon exchange supplies a channel check for spin assignment:
  the scalar-antiscalar numerator is proportional to
  \(4k^2P_1(\cos\theta)\), so the massless pole has \(\ell=1\) residue in
  that channel.
- The residue of a bound-state pole factorizes into couplings of the
  bound-state one-particle vector to the external two-particle channel.
- The chapter computes consequences of an isolated stable pole; it does not
  prove that an arbitrary interacting QFT contains such a pole.
- The chapter now separates \(M_B<2m\) as a physical location statement from
  the stronger mathematical simple-pole hypothesis; shallow molecular states,
  zero-energy/unitary-limit states, virtual states, and Efimov accumulation
  are outside the isolated-pole theorem unless additional threshold
  hypotheses are supplied.
- The cross-reference to the later Bethe--Salpeter Fredholm theorem now makes
  explicit that pole existence, operator compactness, channel overlap, and
  spectral positivity are separate assumptions or results, not consequences of
  the elementary exchange diagram.
- 2026-05-24 issue #425 pass: renamed the elastic kinematic factor to
  \(\beta(s)\) in the partial-wave \(S_\ell\) convention, reserving
  \(\rho\) for spectral measures.
- 2026-05-24 issue #434 pass: renamed the bound-state chapter's ordered
  partial-wave coefficient from \(\mathcal M_\ell(s)\) to \(a_\ell(s)\) and
  added the explicit cross-reference to the Volume I ordered \(16\pi\)
  convention.
- 2026-05-24 issue #435 pass: matched the chapter's \(s,t,u\) notation to the
  part-wide mostly-plus Mandelstam convention and recorded the physical
  \(s\)-channel signs \(t,u\le0\).
- 2026-05-25 issue #443 pass: introduced the stable-channel sheet convention
  before first use and redirected later references away from the later
  analyticity chapter.

## Figure Requirements

- Tree exchange diagrams for \(s\), \(t\), and \(u\) channels with all species
  indicated.
- Complex \(s\)-plane picture of a below-threshold pole and the two-particle
  cut.
- Nonrelativistic \(k\)-plane picture showing bound-state poles on the upper
  imaginary axis.
- Source-matched short-range potential sketch with incoming/outgoing waves
  and a decaying bound-state profile.
- Partial-wave pole diagram relating a two-particle channel to a stable
  one-particle state.

## Exclusions

- No resonance pole on the second sheet.
- No self-energy resummation or decay width.
- No Bethe--Salpeter equation.
- No claim that every below-threshold pole is generated dynamically by a
  composite operator; the microscopic origin is separated from the scattering
  criterion.
