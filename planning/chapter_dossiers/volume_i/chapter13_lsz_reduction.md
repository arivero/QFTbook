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
- Haag--Ruelle wave operators
  \(\Omega_{\mathrm{in/out}}:\mathcal F_s(\Hilb_1)\to\Hilb\) already
  constructed in the preceding chapter.
- The symmetric Fock space and plus permutation signs are scalar-boson data.
  Fermionic external particles use the graded asymptotic Fock space with signs
  fixed by spin-statistics.
- Scattering operator \(S=\Omega_{\mathrm{out}}^*\Omega_{\mathrm{in}}\) on
  the asymptotic Fock space when the incoming and outgoing ranges coincide.
- Relativistically normalized generalized momentum states.
- Scalar local field \(\widehat\phi\) with one-particle residue \(Z>0\).
- Time-ordered Green functions as Lorentzian distributions.
- All momentum-space kernel statements are distributional after wave-packet
  smearing.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(d\) | spatial dimension, \(D-1\) |
| \(\mathcal F_s(\Hilb_1)\) | bosonic asymptotic Fock space over the isolated one-particle subspace |
| \(\Omega_{\mathrm{in/out}}\) | Haag--Ruelle wave operators |
| \(S\) | scattering operator \(\Omega_{\mathrm{out}}^*\Omega_{\mathrm{in}}\) |
| \(\omega_{\vec p}\) | \(\sqrt{\vec p^{\,2}+m^2}\) |
| \(\dd\mu_m\) | Lorentz-invariant mass-shell measure |
| \(\Sigma_m^+\) | positive-energy mass shell |
| \(Z\) | one-particle pole residue for \(\widehat\phi\) |
| \(F_{\rm in/out}\) | incoming/outgoing asymptotic Fock wave-packet vectors |
| \(G_N\) | Lorentzian time-ordered \(N\)-point function |
| \(\widetilde G_N\) | Fourier transform of \(G_N\) |
| \(\widetilde G_{N}^{\mathrm{conn}}\) | connected part of the Fourier-space Green function |
| \(Z[J]\) | Lorentzian time-ordered source functional with source term \(i\int J\phi\) |
| \(Z_E[J_E]\) | Euclidean ordered source functional with source term \(+\int J_E\phi_E\) |
| \(\operatorname{bv}_{\Sigma_m}\) | Feynman boundary value at the isolated mass shell after wave-packet smearing |
| \(p_j\) | incoming positive-energy physical momentum |
| \(q_i\) | outgoing positive-energy physical momentum |
| \(k_a\) | all-incoming Green-function momentum, \(q_i\) or \(-p_j\) |
| \(\mathcal M\) | invariant scattering amplitude |
| \(M_\delta\) | connected amplitude in a nonrelativistic \(\delta^{(d)}\)-normalized basis |

## Claims Established

- The object computed by LSZ is the Hilbert-space matrix element
  \(\langle F_{\rm out},S F_{\rm in}\rangle_{\mathcal F_s(\Hilb_1)}\), with
  \(S\) supplied by Haag--Ruelle wave operators.
- The wave-packet LSZ theorem identifies the connected component of that
  matrix element with the external one-particle residue of
  \(\widetilde G^{\mathrm{conn}}_{m+n}\), after distributional smearing and
  boundary-value restriction to \(\Sigma_m^+\).
- The two-point pole coefficient \(Z\) supplies the external wavefunction
  factor.  In the Feynman two-point function, \(-iZ\) is the coefficient of
  \(k^2+m^2-i0\), whereas the complex \(k^0\)-plane residues at fixed
  \(\vec k\) are \(iZ/(2\omega_{\vec k})\) and
  \(-iZ/(2\omega_{\vec k})\).
- LSZ is a distributional theorem for wave-packet matrix elements.
- Incoming physical momenta enter the Green function as \(-p_j\) in the
  all-momenta-incoming Fourier convention.
- Connected scattering kernels are obtained by applying
  \(Z^{-1/2}i(k^2+m^2)\) to every external leg and taking the on-shell
  boundary value.
- With \(x^0=-i\tau\), the Lorentzian source term
  \(i\int dx^0\,J_L\phi\) becomes \(+\int d\tau\,J_E\phi_E\) for
  \(J_E(\tau,\vec x)=J_L(-i\tau,\vec x)\); the factor \(i^{-N}\) in the
  connected cumulant formula compensates the \(i^N\) produced by differentiating
  the Lorentzian source exponential before contour rotation.
- The large-time Haag--Ruelle matrix element becomes an oscillatory integral
  whose nonzero limit is precisely the external one-particle pole residue.
- Disconnected two-point factors reproduce the identity part of the
  S-operator.
- The identity kernel for identical scalar particles is the symmetric
  permutation sum; the fermionic analogue carries the antisymmetric Koszul
  signs.
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

## Audit Notes

- 2026-05-24 issue #377 pass: labelled the connected cumulant equation and
  displayed the source-functional Wick-rotation identity in the
  \(x^0=-i\tau\) convention, separating the Euclidean \(+\int J_E\phi_E\)
  source from the Lorentzian \(i^{-N}\) source-derivative compensation.
- 2026-05-24 issue #378 pass: replaced the misleading
  \(\operatorname{Res}_{k^2=-m^2}\) notation by the invariant-denominator
  boundary-value coefficient and displayed the two linear \(k^0\)-pole residues
  explicitly.
