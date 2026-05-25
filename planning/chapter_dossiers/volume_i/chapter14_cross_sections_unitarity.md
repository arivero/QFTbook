# Volume I, Chapter 14 Dossier: Cross Sections, Phase Space, and Unitarity

## Source Placement

- Follows LSZ reduction.
- Uses the invariant amplitude \(\mathcal M\) only after the S-operator and
  LSZ have been constructed.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 5608--6075;
  - `references/253a_notes.tex`, corresponding cross-section and partial-wave
    blocks, used only as a comparison.

## Framework

- Relativistically normalized asymptotic momentum states.
- Mostly-plus metric, with \(p^2=-m^2\) for a physical particle.
- Amplitude convention:
  \[
    \langle f|T|i\rangle=(2\pi)^D\delta^D(P_f-P_i)\mathcal M(f|i).
  \]
- Cross sections are derived from wave-packet transition probabilities and
  expressed through sharp-momentum kernels.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(T\) | transition operator defined by \(S=\mathbf 1+iT\) |
| \(\mathcal M\) | invariant amplitude |
| \(M_\delta\) | connected amplitude in the \(\delta^{(d)}\)-normalized sharp-momentum basis |
| \(a_\ell(s)\) | partial-wave coefficient of the invariant amplitude; not the same object as \(M_\delta\) |
| \(\dd\Phi_m\) | invariant \(m\)-body final-state phase space |
| \(\mathcal F\) | invariant two-particle flux factor |
| \(v_{\mathrm{rel}}\) | invariant relative speed |
| \(s\) | positive center-of-mass energy squared, \(-(p_1+p_2)^2\) |
| \(\vec p_*\) | incoming COM three-momentum |
| \(\vec q_*\) | outgoing COM three-momentum |
| \(S_\ell(s)\) | partial-wave S-matrix eigenvalue |
| \(\beta(s)\) | two-body elastic phase-space factor \(2|\vec p_*|/\sqrt s\); \(\rho\) is reserved for spectral measures |
| \(\mathcal N(E)\) | normalization of the COM partial-wave generalized state |
| \(\delta_\ell(s)\) | elastic phase shift |

## Claims Established

- Cross sections are transition probabilities divided by invariant flux.
- The sharp-momentum delta-square derivation is included as a regulated check:
  \((2\pi)^D\delta^D(0)=V\mathcal T\) and
  \(\delta^{(d)}(0)=V/(2\pi)^d\).
- The notation table now separates \(M_\delta\), the
  \(\delta^{(d)}\)-normalized connected sharp-momentum kernel, from
  \(\mathcal M\), the invariant amplitude, and \(a_\ell(s)\), the
  partial-wave coefficient.
- The \(m\)-body phase-space measure and flux factor are fixed in the chosen
  normalization.
- Identical-particle factors are derived from the resolution of the identity
  on symmetric or antisymmetric asymptotic Fock sectors:
  \(\mathbf 1_{\Hilb_1^{\odot r}}\) carries
  \(r!^{-1}\int\prod_j\dd\mu(q_j)|q_1,\ldots,q_r\rangle
  \langle q_1,\ldots,q_r|\).
- For \(2\to2\) scattering in \(D=4\),
  \[
    \frac{\dd\sigma}{\dd\Omega}
    =
    \frac{1}{64\pi^2s}
    \frac{|\vec q_*|}{|\vec p_*|}|\mathcal M|^2
  \]
  before specializing the outgoing identity resolution to identical-particle
  sectors.
- Unitarity gives the amplitude-level cutting relation and the optical
  theorem.
- 2026-05-24 issue #391 pass: the unitarity identity now explicitly
  distinguishes Hilbert-space adjunction from reversed-process reciprocity.
  The factor in the exact relation is
  \(\mathcal M(X|f)^*\), because
  \(\langle f|T^\dagger|X\rangle=\langle X|T|f\rangle^*\).  The forward
  optical theorem therefore gives
  \(\sum_X\int d\Phi_X |\mathcal M(X|i)|^2\) from unitarity alone; no
  time-reversal invariance is being assumed.
- The optical theorem is stated as a complete outgoing-state sum.  Finite
  detector resolution is represented by a positive outgoing effect
  \(E_{\mathcal C}\), with the full forward imaginary part corresponding to
  \(E_{\mathcal C}=\mathbf 1\).  In massless theories the inclusive sum over
  detector-degenerate soft states is taken before removing the infrared
  regulator.
- Partial waves diagonalize scalar \(2\to2\) scattering in the COM frame.
- The COM partial-wave state normalization is derived from the radial
  energy-conservation delta function, including the identical-particle factor
  from the symmetric two-particle identity resolution.
- The sharp-momentum partial-wave kernel is reconstructed explicitly from
  \(S_\ell(E)-1\), before converting to the invariant amplitude convention.
- Elastic unitarity gives \(S_\ell=e^{2i\delta_\ell}\) and
  \(\operatorname{Im}a_\ell=\beta|a_\ell|^2\).
- 2026-05-24 issue #425 pass: renamed the two-body kinematic factor from
  \(\rho(s)\) to \(\beta(s)\) so \(d\rho\) remains reserved for
  Kallen--Lehmann spectral measures.
- 2026-05-24 issue #434 pass: recorded \(a_\ell(s)\) as the ordered
  \(16\pi\) partial-wave amplitude and matched the later bound-state chapter
  to this same symbol and normalization.

## Figure Requirements

- Invariant flux/cross-section schematic.

## Exclusions

- No spin/helicity partial waves; spin begins in the later particle
  classification chapters.
- No detailed analytic continuation of resonance poles; only the organizing
  statement is recorded.
