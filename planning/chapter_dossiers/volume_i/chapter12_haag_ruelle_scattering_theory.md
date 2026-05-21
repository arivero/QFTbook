# Volume I, Chapter 12 Dossier: Haag--Ruelle Scattering Theory

## Source Placement

- Follows Lorentzian Green functions and analytic continuation.
- Precedes LSZ reduction and every perturbative interpretation of Feynman
  graphs as scattering amplitudes.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 4550--5078;
  - `references/sound_references/buchholz_dybalski_scattering_2023.pdf` and
    text sidecar, especially Sections 1--2.

## External Reference Boundary

- Buchholz--Dybalski, "Scattering in relativistic quantum field theory: basic
  concepts, tools, and results":
  - used for the theorem boundary of Haag--Ruelle scattering in the
    Haag--Kastler/local-operator formulation;
  - records standing assumptions: locality, spectrum condition, vacuum,
    one-particle subspace, stability/mass gap or Herbst-type condition,
    Poincare covariance;
  - no claim of general asymptotic completeness is imported.

## Framework

- Mostly-plus Minkowski signature in \(D\) spacetime dimensions.
- Physical Hilbert space \(\Hilb\) with strongly continuous Poincare
  representation \(U(a,\Lambda)\), vacuum \(\Omega\), and spectrum condition.
- Local or almost-local bounded operators are used to state the theorem
  without domain distractions from unbounded point fields.
- A massive one-particle subspace \(\Hilb_1\) of mass \(m>0\) is assumed to be
  isolated from the remaining spectrum.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(d\) | spatial dimension, \(d=D-1\) |
| \(P^\mu\) | energy-momentum generators |
| \(M^2\) | invariant mass operator \(-P_\mu P^\mu\) |
| \(\Hilb_1\) | one-particle Hilbert space of mass \(m\) |
| \(P_1\) | orthogonal projection onto \(\Hilb_1\) |
| \(\Sigma_m^+\) | positive-energy mass shell |
| \(\omega_{\vec p}\) | \(\sqrt{\vec p^{\,2}+m^2}\) |
| \(A,B\) | local or almost-local interpolating operators |
| \(h\) | compactly supported momentum wave packet |
| \(h_t\) | positive-energy Klein--Gordon wave packet |
| \(B_t(h)\) | Haag--Ruelle creation approximant |
| \(V(h)\) | velocity support of \(h\) |
| \(\mathcal F_s(\Hilb_1)\) | bosonic Fock space over \(\Hilb_1\) |
| \(\Omega_{\mathrm{in/out}}\) | Haag--Ruelle wave operators |
| \(\Hilb_{\mathrm{in/out}}\) | incoming/outgoing scattering subspaces |
| \(S\) | scattering operator \(\Omega_{\mathrm{out}}^*\Omega_{\mathrm{in}}\) |

## Claims Established

- The massive scattering construction requires Hilbert-space data and
  explicit spectral/locality hypotheses.
- A local operator with nonzero one-particle overlap can be energy-momentum
  filtered and smeared with a positive-energy Klein--Gordon wave packet.
- Disjoint velocity supports imply asymptotic spacelike separation of the
  corresponding wave packets.
- Haag--Ruelle limits exist in norm under the stated hypotheses and depend
  only on the one-particle vectors.
- The limits carry the bosonic Fock inner product and define isometric wave
  operators from free Fock space into the physical Hilbert space.
- The S-operator is \(\Omega_{\mathrm{out}}^*\Omega_{\mathrm{in}}\) when the
  incoming and outgoing ranges coincide.
- LSZ is positioned as the next theorem relating these nonperturbative matrix
  elements to time-ordered Green functions.

## Figure Requirements

- Mass-spectrum schematic showing vacuum, isolated one-particle mass shell,
  continuum threshold, and spectral gap.
- Spacetime wave-packet schematic showing disjoint velocity supports becoming
  spacelike separated.
- Wave-operator diagram relating Fock space, incoming/outgoing subspaces, and
  the S-operator.

## Exclusions

- No LSZ formula in this chapter.
- No Feynman graphs for scattering amplitudes.
- No assumption of full asymptotic completeness unless stated as a separate
  hypothesis.
- No treatment of massless/infraparticle scattering beyond defining the scope
  boundary for later chapters.
