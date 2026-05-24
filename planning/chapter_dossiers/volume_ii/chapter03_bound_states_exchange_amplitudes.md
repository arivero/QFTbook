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
- Tree-level perturbation theory is used only for the connected
  \(\phi_1\phi_1\to\phi_1\phi_1\) amplitude after LSZ.
- Bound-state identification is stated as an analytic scattering criterion:
  a pole below a two-particle threshold represents a stable one-particle state
  coupled to that channel. Whether the state is elementary or composite is
  extra microscopic information.
- Existence of a composite below-threshold pole is treated as a dynamical
  spectral input, not as something derived from the Lagrangian by general
  principles.
- A short-range one-dimensional Schrödinger problem is used as a controlled
  mathematical model for the pole criterion.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\phi_1,\phi_2\) | scalar fields in the exchange model |
| \(m_1,m_2\) | corresponding mass parameters |
| \(g\) | cubic coupling in \(-g\phi_1^2\phi_2/2\) |
| \(s,t,u\) | Mandelstam invariants |
| \(E\) | center-of-mass energy |
| \(z=\cos\theta\) | scattering-angle variable |
| \(\mathcal M(s,z)\) | connected invariant amplitude |
| \(\mathcal M_\ell(s)\) | partial-wave amplitude |
| \(S_\ell(s)\) | elastic partial-wave scattering eigenvalue |
| \(M_B\) | bound-state mass below threshold |
| \(k\) | nonrelativistic relative momentum |
| \(E_{\mathrm{nr}}\) | nonrelativistic energy |
| \(\mathcal N(E)\) | normalization of delta-normalized two-particle partial-wave states |

## Claims Established

- The tree-level exchange model has \(s\)-, \(t\)-, and \(u\)-channel poles
  with positions fixed by \(m_2\).
- For \(m_2<2m_1\), the \(s\)-channel pole lies below the
  \(\phi_1\phi_1\) threshold and has the scattering signature of a stable
  state coupled to the two-\(\phi_1\) channel.
- In short-range nonrelativistic scattering, bound states correspond to poles
  of the analytically continued scattering function at \(k=\ii\alpha\),
  \(\alpha>0\).
- In relativistic partial waves, a stable spin-\(\ell\) state below threshold
  gives a pole in \(\mathcal M_\ell(s)\) or \(S_\ell(s)\) at
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
