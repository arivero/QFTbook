# Volume II, Chapter 4 Dossier: Resonances and Dressed Propagators

## Scope

- Continues the two-scalar exchange model after the below-threshold
  bound-state analysis.
- Treats the above-threshold regime \(m_2>2m_1\), where the exchange
  channel couples to an open two-particle continuum.
- Develops resonances as analytic features of amplitudes with stable external
  states: complex poles of analytically continued partial waves or invariant
  amplitudes.
- Derives the one-loop \(\phi_2\) self-energy, its threshold branch cut, its
  imaginary part, the resulting finite-width resonant form, and the
  second-sheet pole.

## Source Spine

- `transcription/tex/253b/scattering_rg_qcd.tex`, from the subsection
  "Unstable Particles and Resonances" through "The Complex \(s\)-Plane and
  the Second Sheet".
- `references/253b transcribed lecture notes.tex`, corresponding resonance,
  self-energy, and second-sheet material, used cautiously for cross-checking
  diagrams and formulas but not as authoritative text.
- Volume I chapters on spectral measures, Lorentzian Green functions, LSZ, and
  cross sections.
- Volume II Chapters 1--3 for the local notation, scattering kernel
  convention, and below-threshold pole discussion.
- External resonance references used as controls: rigged-Hilbert/Gamow-vector
  treatments of S-matrix resonance poles, Stuart/Sirlin pole-scheme
  gauge-invariance work, and Denner--Dittmaier/Denner--Lang complex-mass
  scheme and unitarity analyses.  These are controls for terminology and
  theorem boundaries; the chapter defines the local pole-residue construction
  directly from stable-channel amplitudes.
- Rendered handwritten trace
  `monograph/tex/build/source_visual_trace/253b_trace-017.png` and
  `253b_trace-018.png` for the above-threshold tree pole, unitarity
  obstruction, resonance interpretation, and one-dimensional outgoing-wave
  setup.
- Rendered handwritten trace
  `monograph/tex/build/source_visual_trace/253b_trace-019.png` through
  `253b_trace-026.png` for the resonance \(k\)- and \(E\)-plane pictures,
  dressed \(\phi_2\) propagator, one-loop self-energy, Wick rotation,
  cutoff subtraction, threshold cut, phase motion, and second-sheet pole.

## Definitions and Symbols

| Symbol | Meaning |
| --- | --- |
| \(K\) | total momentum carried by the \(s\)-channel line, \(K=k_1+k_2\) |
| \(s\) | invariant energy, \(s=-K^2\) |
| \(D_2(k)\) | exact time-ordered two-point function of \(\phi_2\) in momentum space |
| \(\Sigma(k)\) | amputated one-particle-irreducible two-point insertion for \(\phi_2\) |
| \(\Sigma^R(k)\) | renormalized self-energy after subtracting the mass counterterm |
| \(\rho_1(s)\) | two-\(\phi_1\) phase-space square root, \(\sqrt{1-4m_1^2/s}\) |
| \(a_\ell(s)\) | identical-boson partial-wave coordinate in the \(32\pi\), even-\(\ell\) convention |
| \(S_\ell(s)\) | elastic partial-wave \(S\)-matrix element on the symmetric two-\(\phi_1\) channel |
| \(F(s)\) | dressed inverse denominator of the \(s\)-channel exchange amplitude |
| \(s_\ast\) | complex pole of the second-sheet continuation |
| \(M_R,\Gamma_R\) | real resonance mass parameter and narrow-width decay rate |
| \(\mathfrak s\) | sheet of an analytically continued stable-channel amplitude |
| \(R_{ab}\) | pole-residue kernel between stable channels \(a,b\) |
| \(r_a,r_b\) | production and decay residue functionals, defined up to reciprocal rescaling |
| \(\Phi_\pm\) | rigged-Hilbert test spaces for incoming/outgoing analytic continuations |
| \(\ket{G_\ast}\) | Gamow functional representing the decaying pole term when a rigging is supplied |

## Assumptions

- Mostly-plus Lorentzian signature and scalar propagator
  \(-\ii/(k^2+m^2-\ii0)\).
- The external scattering states are stable \(\phi_1\) particles.
- The coupling \(g\) is weak enough that one-loop self-energy and narrow-width
  approximations are meaningful when explicitly invoked.
- The physical boundary value is obtained from the Feynman prescription:
  Euclidean momenta are analytically continued to positive real energy from
  above.
- After loop Wick rotation, no residual \(-i0\) is attached to the Euclidean
  loop variable \(\ell_E\).  Any later \(-i0\) in
  \(k^2x(1-x)+m_1^2-i0\) or
  \(1-sx(1-x)/m_1^2-i0\) is the boundary-value prescription for the external
  invariant \(k^2=-s\).
- The partial-wave normalization for the \(\phi_1\phi_1\) resonance channel is
  the unordered identical-boson convention
  \[
    \mathcal M(s,z)
    =
    32\pi\sum_{\ell\ {\rm even}}(2\ell+1)a_\ell(s)P_\ell(z),
    \qquad
    S_\ell=1+2i\rho_1a_\ell .
  \]
  Ordered \(16\pi\) amplitudes may be used only as labelled-leg
  bookkeeping before Bose symmetrization.
- The cut width uses the two-point specialization of the exact unitarity
  discontinuity; the displayed inclusive line-replacement expression is its
  weak-coupling perturbative expansion.
- Statements about the resonance pole use the analytic continuation of the
  amplitude, not a Hilbert-space eigenvector with real energy.

## Claims to Derive

- A real-axis tree pole in the open two-particle region is replaced, in the
  dressed amplitude, by a branch cut plus a complex pole on the adjacent sheet.
- The exact physical-axis partial wave remains bounded by unitarity:
  \(|S_\ell|=1\) in a one-channel elastic interval and \(|S_\ell|\le1\) for
  the elastic component of a larger unitary matrix. The tree-level divergence
  is therefore a perturbative expansion signal, not an exact physical-axis
  singularity.
- A one-dimensional outgoing resonance pole is represented by a purely
  outgoing analytically continued solution. Its time decay and spatial growth
  are linked by probability conservation; the object is a singular outgoing
  functional rather than a normalizable eigenvector of the self-adjoint
  Hamiltonian.
- The nonrelativistic energy-plane figure records that resonance poles lie on
  the sheet reached through the positive-energy cut.
- The one-loop self-energy derivation now includes the shifted loop-energy
  Wick-rotation contour and the Euclidean cutoff evaluation used in the
  handwritten notes.
- The one-loop \(\phi_1\) bubble gives
  \[
    \Sigma^R(k)
    =
    -{g^2\over 32\pi^2}
    \int_0^1\dd x\,
    \log {k^2x(1-x)+m_1^2-\ii0\over m_1^2}.
  \]
- For \(s>4m_1^2\),
  \[
    \operatorname{Im}\Sigma^R(K)\big|_{K^2=-s+\ii0}
    =
    {g^2\over 32\pi}\sqrt{1-{4m_1^2\over s}} .
  \]
- In the narrow-width approximation,
  \[
    M_R\Gamma_R
    =
    {g^2\over 32\pi}\sqrt{1-{4m_1^2\over M_R^2}}
    +O(g^4)
  \]
  up to the stated normalization convention for the cubic interaction.
- Elastic partial-wave unitarity is represented by phase motion of \(S_0(s)\),
  not by a physical-axis divergence.
- 2026-05-24 issue #392 pass: the Breit--Wigner elastic factor is now defined
  as \(S_0^{\rm BW}\).  The approximation lies in the single-channel resonant
  truncation and the chosen width function \(W(s)\); after this truncation,
  \[
    S_0^{\rm BW}(s)=
    {M_R^2-s+iW(s)\over M_R^2-s-iW(s)}
  \]
  is exactly elastic-unitary on the real elastic interval because the numerator
  is the complex conjugate of the denominator.
- For the angle-independent resonant \(s\)-channel exchange,
  \(a_0^{(s)}=\mathcal M_s/(32\pi)\), hence
  \[
    \mathcal M_s=-16\pi i\,\rho_1^{-1}(S_0-1),
  \]
  which is the normalization used in the phase-motion derivation.
- The first-sheet sign argument is recorded: in the upper half \(s\)-plane
  both \(\operatorname{Im}(-s)\) and the imaginary part of the logarithmic
  term have the same negative sign, while the lower half-plane has the
  conjugate positive sign. Hence the resonance zero of the denominator is not
  on the first sheet.
- The first-sheet amplitude has the threshold cut; the resonance pole is on
  the continuation through that cut.
- A pole-factorized resonance object is defined as the residue kernel of a
  stable-channel amplitude in a local pole neighborhood, with rank-one
  factorization recorded only after the sheet, channel variables, and
  normalization equivalence have been specified.
- Multiple external resonance slots are represented by nested residues only in
  a polydisc where the only singular divisors are isolated simple pole
  hyperplanes.
- Field-redefinition invariance, covariance, unitarity constraints, and
  gauge-representative independence are inherited by applying residue
  functionals to stable-channel amplitudes.
- Gamow functionals live in duals of chosen test spaces and represent pole
  residues as semigroup-evolving generalized vectors; they are not additional
  Hilbert-space particles.
- Threshold collisions, coupled channels, overlapping poles, real-axis
  line-shape conventions, and massless long-range sectors are explicit
  obstructions to naive external-resonance amplitudes.

## Figures

- Above-threshold exchange and open continuum diagram.
- Nonrelativistic outgoing resonance pole and its \(k\)-plane/\(E\)-plane
  geometry.
- Dyson series and one-loop bubble for the \(\phi_2\) self-energy.
- Wick/threshold analytic-continuation diagram.
- Argand and second-sheet diagrams for the resonant partial wave.

## Boundaries

- No composite bound-state Bethe--Salpeter analysis; that begins in the next
  chapter.
- No general analyticity/crossing/Landau singularity development; only the
  local analytic structure needed for this resonance construction.
- No perturbative S-matrix introduction before the nonperturbative scattering
  and LSZ framework already established in Volume I.
- The external-resonance section is an isolated-pole construction and open
  problem statement.  It is not an LSZ theorem for unstable particles.

## Audit Notes

- 2026-05-24 issue #386 pass: corrected the opening partial-wave convention
  from the ordered \(16\pi\) expansion to the unordered identical-boson
  \(32\pi\), even-\(\ell\) convention, replaced \(\mathcal M_\ell\) by
  \(a_\ell\), and displayed the inversion
  \(a_0^{(s)}=\mathcal M_s/(32\pi)\Rightarrow
  \mathcal M_s=-16\pi i\rho_1^{-1}(S_0-1)\).
- 2026-05-24 issue #387 pass: corrected the nonrelativistic \(E\)-plane
  resonance figure so the first-sheet trajectory remains on the upper lip of
  the positive-real-energy cut, while the second-sheet path starts only after
  a separate continuation through the cut and then runs on the lower lip to
  the resonance pole.
- 2026-05-24 issue #388 pass: clarified that the Wick-rotated loop integral
  has an ordinary Euclidean denominator and that any later \(-i0\) belongs to
  the external invariant boundary value, not to the loop integration variable.
