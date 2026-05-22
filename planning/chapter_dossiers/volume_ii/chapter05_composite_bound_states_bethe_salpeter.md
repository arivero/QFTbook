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
| \(\Phi_B(x_1,x_2;P)\) | Bethe--Salpeter amplitude, a time-ordered matrix element |
| \(\widetilde\Phi_B(p;P)\) | momentum-space Bethe--Salpeter amplitude |
| \(\Psi_B(p;P)\) | amputated Bethe--Salpeter vertex/wavefunction |
| \(\overline{\Psi}_B(p;P)\) | right residue of the four-point pole; scalar conjugate with reversed momenta up to conventions |
| \(\mathcal K_P(p,q)\) | two-particle irreducible kernel in the chosen channel |
| \(\mathcal G_P(q)\) | product of two exact constituent propagators |
| \(\widehat V_P\) | integral operator with kernel \(\mathcal K_P(p,q)\mathcal G_P(q)\) acting on the amputated amplitude |
| \(f(s)\) | \(D=2\) scalar bubble Feynman-parameter integral |
| \(s,t\) | Mandelstam variables \(s=-(k_1+k_2)^2\), \(t=-(k_1-k_3)^2\) in the source convention |

## Assumptions

- Mostly-plus metric and scalar propagator \(-\ii/(k^2+m^2-\ii0)\).
- External particles in scattering amplitudes are stable single-\(\phi\)
  states of mass \(m\).
- A composite bound state is a stable spectral state below the relevant
  two-particle threshold.
- The bubble-chain calculation is an approximation that isolates repeated
  two-particle propagation; it is used only in its domain of weak binding.
- The Bethe--Salpeter kernel is defined to be two-particle irreducible in the
  channel being resummed.
- Plane-wave bound-state kets are distributional and are used with covariant
  normalization; finite states are wavepacket smearings.
- The local attractive quartic example is interpreted inside a stable
  large-field completion, not as a nonperturbative negative-quartic scalar
  potential.

## Claims to Derive

- A stable composite particle of mass \(M_B<2m\) produces a first-sheet pole
  in the \(s\)-channel four-point function and in the corresponding
  scattering amplitude.
- In \(D=2\) \(\phi^4\) theory, the bubble-chain approximation gives
  \[
    \ii\mathcal A_{\mathrm{chain}}
    =
    {-\,\ii g\over 1+g f(s)/(8\pi)}
  \]
  and, for attractive weak coupling \(g<0\),
  \[
    M_B\simeq 2m-{g^2\over 256m^3}.
  \]
- The residue of the four-point pole factorizes into Bethe--Salpeter
  amplitudes.
- The amputated residue obeys the homogeneous Bethe--Salpeter equation
  \[
    \Psi_B(p;P)
    =
    \int { \dd^D q\over (2\pi)^D}\,
    \mathcal K_P(p,q)\mathcal G_P(q)\Psi_B(q;P)
  \]
  at \(P^2=-M_B^2\).
- Equivalently, \((\mathbf 1-\widehat V_P)\Psi_B=0\), and the unamputated
  amplitude obeys
  \[
    \widetilde\Phi_B(p;P)
    =
    \mathcal G_P(p)\int { \dd^D q\over (2\pi)^D}\,
    \mathcal K_P(p,q)\widetilde\Phi_B(q;P).
  \]

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
