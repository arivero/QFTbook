# Volume I, Chapter 13 Dossier: LSZ Reduction

## Source Placement

- Follows Haag--Ruelle scattering theory.
- Precedes perturbative scattering amplitudes, cross sections, and unitarity
  formulas.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 5079--5608;
  - `references/sound_references/buchholz_dybalski_scattering_2023.pdf` and
    text sidecar, Section 3.

## External Reference Boundary

- Buchholz--Dybalski Section 3 is used for the theorem boundary:
  LSZ follows after the Haag--Ruelle construction and is valid under massive
  one-particle and stability assumptions.
- The chapter reproduces the scalar momentum-space reduction formula in the
  monograph's mostly-plus and \(-i/(k^2+m^2-i0)\) propagator convention.
- No LSZ statement is made for massless/infraparticle sectors in this chapter.

## Framework

- Massive scalar particle of mass \(m>0\), isolated one-particle subspace.
- Relativistically normalized generalized momentum states.
- Scalar local field \(\widehat\phi\) with one-particle residue \(Z>0\).
- Time-ordered Green functions as Lorentzian distributions.
- All momentum-space kernel statements are distributional after wave-packet
  smearing.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(d\) | spatial dimension, \(D-1\) |
| \(\omega_{\vec p}\) | \(\sqrt{\vec p^{\,2}+m^2}\) |
| \(\dd\mu_m\) | Lorentz-invariant mass-shell measure |
| \(Z\) | one-particle pole residue for \(\widehat\phi\) |
| \(G_N\) | Lorentzian time-ordered \(N\)-point function |
| \(\widetilde G_N\) | Fourier transform of \(G_N\) |
| \(\widetilde G_{N}^{\mathrm{conn}}\) | connected part of the Fourier-space Green function |
| \(p_j\) | incoming positive-energy physical momentum |
| \(q_i\) | outgoing positive-energy physical momentum |
| \(k_a\) | all-incoming Green-function momentum, \(q_i\) or \(-p_j\) |
| \(\mathcal M\) | invariant scattering amplitude |
| \(M_\delta\) | connected amplitude in a nonrelativistic \(\delta^{(d)}\)-normalized basis |

## Claims Established

- The two-point pole residue \(Z\) supplies the external wavefunction factor.
- LSZ is a distributional theorem for wave-packet matrix elements.
- Incoming physical momenta enter the Green function as \(-p_j\) in the
  all-momenta-incoming Fourier convention.
- Connected scattering kernels are obtained by applying
  \(Z^{-1/2}i(k^2+m^2)\) to every external leg and taking the on-shell
  boundary value.
- The large-time Haag--Ruelle matrix element becomes an oscillatory integral
  whose nonzero limit is precisely the external one-particle pole residue.
- Disconnected two-point factors reproduce the identity part of the
  S-operator.
- The relation between \(\mathcal M\) and \(M_\delta\) is fixed by the external
  relativistic normalization factors.
- The full scattering kernel decomposes into products of connected kernels
  over compatible partitions of incoming and outgoing labels.
- Perturbative \(\phi^4\) Green functions yield
  \(\mathcal M=-g+O(g^2)\) for tree-level \(2\to2\) scattering after LSZ.

## Figure Requirements

- A compact diagram showing external Green-function legs being amputated by
  LSZ into an invariant amplitude.
- A connected-kernel decomposition diagram showing the full \(S\)-kernel as a
  sum over connected components.

## Exclusions

- No cross-section formulas; those belong in the next chapter.
- No unitarity/optical theorem development beyond the amplitude convention.
- No LSZ formula for massless gauge particles or infraparticles.
