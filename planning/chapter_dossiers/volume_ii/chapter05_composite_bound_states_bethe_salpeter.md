# Volume II, Chapter 5 Dossier: Composite Bound States and Bethe--Salpeter Amplitudes

## Scope

- Continues after the resonance chapter by returning to first-sheet
  below-threshold poles.
- Treats stable composite particles as spectral states and as poles of
  four-point functions.
- Gives the \(D=2\) \(\phi^4\) bubble-chain example of a weak bound state.
- Defines the Bethe--Salpeter amplitude as a time-ordered matrix element and
  derives the homogeneous Bethe--Salpeter equation from four-point
  factorization.
- Certifies handwritten 253b pp. 27--33 after checking the rendered source
  trace and the manuscript figures on 2026-05-22.

## Source Spine

- `transcription/tex/253b/scattering_rg_qcd.tex`, subsection "Bound States as
  Composite Particles" through "Bethe--Salpeter Amplitudes".
- `references/253b transcribed lecture notes.tex`, corresponding bubble-chain
  and Bethe--Salpeter sections, used cautiously for cross-checking signs,
  diagrams, and threshold estimates.
- Volume I spectral representation and LSZ chapters.
- Volume II Chapter 3 for first-sheet pole criteria and Chapter 4 for the
  resonance/second-sheet contrast.

## Definitions and Symbols

| Symbol | Meaning |
| --- | --- |
| \(P\) | total momentum in the two-particle channel |
| \(p,q\) | relative momenta in Bethe--Salpeter kernels |
| \(M_B\) | mass of a stable composite particle |
| \(X,Y\) | center coordinates of the two field pairs in the \((12)\)-channel spectral decomposition |
| \(\xi,\eta\) | relative coordinates inside the two field pairs |
| \(\mathcal O_f(X)\) | relative-coordinate-smeared time-ordered pair operator |
| \(\Phi_B(x_1,x_2;P)\) | Bethe--Salpeter amplitude, a time-ordered matrix element |
| \(\widetilde\Phi_B(p;P)\) | momentum-space Bethe--Salpeter amplitude |
| \(\Psi_B(p;P)\) | amputated Bethe--Salpeter vertex/wavefunction |
| \(\overline{\Psi}_B(p;P)\) | right residue of the four-point pole; scalar conjugate with reversed momenta up to conventions |
| \(\mathcal K_P(p,q)\) | two-particle irreducible kernel in the chosen channel |
| \(\mathcal G_P(q)\) | product of two exact constituent propagators |
| \(\widehat V_P\) | integral operator with kernel \(\mathcal K_P(p,q)\mathcal G_P(q)\) acting on the amputated amplitude |
| \(\mathcal X\) | chosen test-function, Sobolev, or Hilbert space on which the amputated Bethe--Salpeter operator is realized |
| \(f(s)\) | \(D=2\) scalar bubble Feynman-parameter integral |
| \(s,t\) | Mandelstam variables \(s=-(k_1+k_2)^2\), \(t=-(k_1-k_3)^2\) in the source convention |

## Assumptions

- Mostly-plus metric and scalar propagator \(-\ii/(k^2+m^2-\ii0)\).
- External particles in scattering amplitudes are stable single-\(\phi\)
  states of mass \(m\).
- A composite bound state is a stable spectral state below the relevant
  two-particle threshold.
- The existence of that state is an explicit spectral assumption; the chapter
  derives pole and residue consequences rather than proving bound-state
  existence from the Lagrangian.
- The bubble-chain calculation is an approximation that isolates repeated
  two-particle propagation; it is used only in its domain of weak binding.
- A zero of the bubble-chain denominator is a pole of the approximate kernel;
  identifying it with an exact particle requires additional nonperturbative
  control.
- The Bethe--Salpeter kernel is defined to be two-particle irreducible in the
  channel being resummed.
- The exact Bethe--Salpeter kernel is an operator-level object only after a
  topology has been chosen: \(\mathcal K_P\) must act from the selected
  relative-momentum space \(\mathcal X\) to its dual, or
  \(\mathcal K_P\mathcal G_P\) must define a densely defined/compact operator
  on \(\mathcal X\).
- A converse from a homogeneous Bethe--Salpeter eigenvector to a genuine bound
  state requires analytic Fredholm hypotheses, nonzero overlap with the
  interpolating two-field channel, and absence of competing threshold
  singularities near the pole; \(\mathbf 1-\widehat V(z)\) must also be
  invertible somewhere in the analytic neighborhood.
- The Fredholm criterion is now a theorem, not an informal converse: the exact
  kernel must be an analytic compact-operator family on the chosen Banach
  space, the represented four-point block must factor through analytic
  external-channel maps, and spectral positivity below threshold is an extra
  Hilbert-space input beyond analytic Fredholm theory.
- Ladder sums converge as Neumann series only in regions where the selected
  \(\widehat V_P^{(0)}\) has operator norm below one; bound-state poles are
  described by meromorphic resolvent continuation rather than convergence of
  the raw series at the pole.
- Plane-wave bound-state kets are distributional and are used with covariant
  normalization; finite states are wavepacket smearings.
- The local attractive quartic example is interpreted inside a stable
  large-field completion, not as a nonperturbative negative-quartic scalar
  potential.
- Time-ordered functions, residues, and bubble integrals use the status
  convention declared in
  `def:scattering-time-ordered-correlator-status`: exact pole statements are
  spectral/LSZ statements, while the bubble-chain integral is a formal
  regulated graph calculation of a time-ordered kernel.

## Claims to Derive

- A stable composite particle of mass \(M_B<2m\) produces a first-sheet pole
  in the \(s\)-channel four-point function and in the corresponding
  scattering amplitude.
- In \(D=2\) \(\phi^4\) theory, the bubble-chain approximation gives
  \[
    \ii\mathcal A_{\mathrm{chain}}
    =
    \frac{-\,\ii g}{1+g f(s)/(8\pi)}
  \]
  and, for attractive weak coupling \(g<0\),
  \[
    M_B\simeq 2m-\frac{g^2}{256m^3}.
  \]
- The residue of the four-point pole factorizes into Bethe--Salpeter
  amplitudes.  The proof now smears relative coordinates, inserts the
  bound-state spectral projection between pair operators, and derives the
  \(-\ii/(P^2+M_B^2-\ii0)\) pole from the explicit
  \(\theta(t)\)-Fourier identity.
- The amputated residue obeys the homogeneous Bethe--Salpeter equation
  \[
    \Psi_B(p;P)
    =
    \int \frac{\dd^D q}{(2\pi)^D}\,
    \mathcal K_P(p,q)\mathcal G_P(q)\Psi_B(q;P)
  \]
  at \(P^2=-M_B^2\).
- Equivalently, \((\mathbf 1-\widehat V_P)\Psi_B=0\), and the unamputated
  amplitude obeys
  \[
    \widetilde\Phi_B(p;P)
    =
    \mathcal G_P(p)\int \frac{\dd^D q}{(2\pi)^D}\,
    \mathcal K_P(p,q)\widetilde\Phi_B(q;P).
  \]
- The Bethe--Salpeter equation is a necessary residue equation for an existing
  exact pole.  In a truncated kernel it is a self-consistency condition inside
  the approximation, not an existence theorem for the underlying QFT.
- Under analytic compact-operator Fredholm hypotheses on
  \(\widehat V(z)=\mathcal K_z\mathcal G_z\), a pole of the represented
  four-point block is equivalent, with nonzero external-channel overlap, to
  a nonzero vector in \(\ker(\mathbf 1-\widehat V(z_B))\).
- In the simple-root case, if the analytic eigenvalue \(\lambda(z)\) of
  \(\widehat V(z)\) satisfies \(\lambda(z_B)=1\) and
  \(\lambda'(z_B)\ne0\), the pole residue is explicitly
  \[
    -\frac{(\mathcal F_{z_B}\psi)\otimes(\chi\mathcal E_{z_B})}
      {\lambda'(z_B)(z-z_B)}
  \]
  up to terms holomorphic at \(z_B\); the pole is absent from a chosen channel
  exactly when the channel maps kill this rank-one residue.
- A ladder approximation is a controlled approximation only after a norm or
  compact-operator topology is supplied and the omitted two-particle
  irreducible kernels are bounded in that topology.

## Figures

- First-sheet composite pole and bubble-chain resummation.
- Four-point Green function factorization through a bound-state propagator.
- Kernel recursion, excluded two-particle cuts, and homogeneous
  Bethe--Salpeter equation.
- Amputated versus unamputated Bethe--Salpeter amplitude.

## Boundaries

- No resonance/second-sheet derivation; that belongs to Chapter 4.
- No general analyticity, crossing, Landau equations, or Lehmann ellipse; those
  begin in the next chapter.
- No nonrelativistic potential reduction beyond a controlled limiting
  statement.

## Audit Notes

- 2026-05-24 issue pass: addressed #216 by adding the missing
  function-space status of \(\mathcal K_P\), the conditional Fredholm converse
  between poles and homogeneous Bethe--Salpeter eigenvectors, and the
  operator-norm/meromorphic-continuation status of ladder sums.
- 2026-05-24 issue #509 pass: expanded the pole-factorization proof to show
  which channel spectral resolution is inserted and how time ordering plus
  the spectrum condition produce the Feynman \(i0\) prescription.
- 2026-05-24 issue #319 pass: added a chapter-opening reminder that the
  Bethe--Salpeter and bubble-chain objects inherit the scattering
  time-ordered-correlator status convention rather than an implicit continuum
  path-integral definition.
- 2026-05-24 issue #324 pass: upgraded the Bethe--Salpeter pole criterion
  from an informal Fredholm converse to a labeled theorem with compactness,
  analyticity, invertibility-somewhere, channel-overlap, and spectral
  positivity hypotheses, including the simple-eigenvalue residue formula.
