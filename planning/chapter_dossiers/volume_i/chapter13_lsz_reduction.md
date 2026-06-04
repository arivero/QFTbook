# Volume I, Chapter 13 Dossier: LSZ Reduction

## Source Placement

- Follows Haag--Ruelle scattering theory.
- Precedes perturbative scattering amplitudes, cross sections, and unitarity
  formulas.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, lines 5079--5608 as an
    approximate source range;
  - `references/sound_references/buchholz_dybalski_scattering_2023.pdf` and
    text sidecar, Section 3.

## External Reference Boundary

- Buchholz--Dybalski Section 3 is used for the theorem boundary:
  LSZ follows after the Haag--Ruelle construction and is valid under massive
  one-particle and stability assumptions.
- Volume I, Chapter 3, Section
  `sec:haag-theorem-interaction-picture-boundary` is now cross-referenced at
  the opening of this chapter to separate Haag--Ruelle/LSZ asymptotic maps from
  the fixed-time interaction-picture unitary excluded by Haag's theorem.
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
- Scalar local field \(\widehat\phi\) with one-particle residue \(Z_\phi>0\).
- Time-ordered Green functions as Lorentzian distributions.
- All momentum-space kernel statements are distributional after wave-packet
  smearing.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(d\) | spatial dimension, \(D-1\) |
| \(\mathcal F_s(\Hilb_1)\) | bosonic asymptotic Fock space over \(\Hilb_1\) |
| \(\Omega_{\mathrm{in/out}}\) | Haag--Ruelle wave operators |
| \(S\) | scattering operator \(\Omega_{\mathrm{out}}^*\Omega_{\mathrm{in}}\) |
| \(\omega_{\vec p}\) | \(\sqrt{\vec p^{\,2}+m^2}\) |
| \(\dd\mu_m\) | Lorentz-invariant mass-shell measure |
| \(\Sigma_m^+\) | positive-energy mass shell |
| \(Z_\phi\) | one-particle pole residue for \(\widehat\phi\) |
| \(F_{\rm in/out}\) | incoming/outgoing asymptotic Fock wave-packet vectors |
| \(G_N\) | Lorentzian time-ordered \(N\)-point function |
| \(\widetilde G_N\) | Fourier transform of \(G_N\) |
| \(\widetilde G_{N}^{\mathrm{conn}}\) | connected part of the Fourier-space Green function |
| \(Z[J]\) | Lorentzian time-ordered source functional with source term \(i\int J\phi\) |
| \(Z_-[J]\) | alternate Lorentzian source functional with source term \(-i\int J\phi\) |
| \(Z_E[J_E]\) | Euclidean ordered source functional with source term \(+\int J_E\phi_E\) |
| \(\operatorname{bv}_{\Sigma_m}\) | Feynman boundary value on \(\Sigma_m\) after smearing |
| \(p_j\) | incoming positive-energy physical momentum |
| \(q_i\) | outgoing positive-energy physical momentum |
| \(k_a\) | all-incoming Green-function momentum, \(q_i\) or \(-p_j\) |
| \(\operatorname{LSZ}_{\phi,k}\) | single-leg external boundary-value extraction |
| \(\mathcal M\) | invariant scattering amplitude |
| \(M_\delta\) | connected amplitude in a nonrelativistic \(\delta^{(d)}\)-normalized basis |

## Claims Established

- The object computed by LSZ is the Hilbert-space matrix element
  \(\langle F_{\rm out},S F_{\rm in}\rangle_{\mathcal F_s(\Hilb_1)}\), with
  \(S\) supplied by Haag--Ruelle wave operators.
- The Haag--Ruelle wave operators are large-time asymptotic maps and do not
  identify the interacting local field algebra with a free field algebra at a
  fixed time; the opening paragraph now points to the Haag-theorem boundary.
- Definitions `def:massive-scalar-lsz-datum`,
  `def:lsz-relativistic-external-normalization`, and
  `def:lsz-wave-packet-scattering-matrix-element` isolate the hypotheses,
  the distributional external-state normalization, and the wave-packet
  Hilbert-space matrix element before the reduction theorem is stated.
- The wave-packet LSZ theorem identifies the connected component of that
  matrix element with the external one-particle residue of
  \(\widetilde G^{\mathrm{conn}}_{m+n}\), after distributional smearing and
  boundary-value restriction to \(\Sigma_m^+\).
- Definition `def:lsz-external-boundary-value-extraction` states the
  single-leg LSZ operation as a distributional boundary-value coefficient
  rather than a formal pointwise operation.
- Theorem `thm:lsz-wave-packet` now includes a proof block tracing the
  argument from Haag--Ruelle approximants, through locality/time-ordering, to
  the large-time external pole selector and the on-shell wave-packet pairing.
- The two-point pole coefficient \(Z_\phi\) supplies the external wavefunction
  factor.  In the Feynman two-point function, \(-iZ_\phi\) is the coefficient of
  \(k^2+m^2-i0\), whereas the complex \(k^0\)-plane residues at fixed
  \(\vec k\) are \(iZ_\phi/(2\omega_{\vec k})\) and
  \(-iZ_\phi/(2\omega_{\vec k})\).
- Definition `def:lsz-interpolating-field-pole-datum` packages the
  Kallen--Lehmann atom, the invariant-denominator coefficient, and the
  external multiplier \(Z_\phi^{-1/2}i(k^2+m^2)\) before the residue
  propositions.
- Paragraph "Invariant denominator coefficient and linear pole residues"
  records the mostly-plus partial-fraction calculation relating the
  invariant-denominator coefficient to the two linear \(k^0\)-pole residues.
- Proposition `prop:lsz-pole-spectral-projection` proves that the external
  pole is the one-particle spectral projection \(P_1\) multiplied by the
  field-state overlap factors.
- LSZ is a distributional theorem for wave-packet matrix elements.
- Incoming physical momenta enter the Green function as \(-p_j\) in the
  all-momenta-incoming Fourier convention.
- Connected scattering kernels are obtained by applying
  \(Z_\phi^{-1/2}i(k^2+m^2)\) to every external leg and taking the on-shell
  boundary value.
- The external-pole stability paragraph records that contact terms and
  zero-overlap field components do not contribute to external LSZ poles, and
  that nonzero interpolating-field coordinate changes cancel against the
  corresponding \(Z_{\phi'}^{-1/2}\) factors.  This is boundary-value and
  field-coordinate bookkeeping, not a theorem-level result.
- With \(x^0=-i\tau\), the Lorentzian source term
  \(i\int dx^0\,J_L\phi\) becomes \(+\int d\tau\,J_E\phi_E\) for
  \(J_E(\tau,\vec x)=J_L(-i\tau,\vec x)\); the factor \(i^{-N}\) in the
  connected cumulant formula compensates the \(i^N\) produced by differentiating
  the Lorentzian source exponential before contour rotation.
- The source-derivative prefactor is convention-dependent: with the alternate
  \(-i\int J\phi\) source coupling, the connected cumulant uses
  \((-i)^{-N}=i^N\) rather than \(i^{-N}\).
- Definitions `def:lsz-connected-lorentzian-source-convention` and
  `def:lsz-external-amputation-map` separate connected cumulant extraction
  from external one-particle amputation.
- The large-time Haag--Ruelle matrix element becomes an oscillatory integral
  whose nonzero limit is precisely the external one-particle pole residue.
- The large-time pole-selector paragraph records the contour calculation that
  selects the incoming negative-energy and outgoing positive-energy Feynman
  poles in the large-time limit.
- Disconnected two-point factors reproduce the identity part of the
  S-operator.
- The identity kernel for identical scalar particles is the symmetric
  permutation sum; the fermionic analogue carries the antisymmetric Koszul
  signs.
- The relation between \(\mathcal M\) and \(M_\delta\) is fixed by the external
  relativistic normalization factors.
- Definition `def:lsz-invariant-scalar-amplitude-convention` records the
  invariant-amplitude convention and its conversion to a
  \(\delta^{(d)}\)-normalized basis before cross-section conventions appear in
  the next chapter.
- The full scattering kernel decomposes into products of connected kernels
  over compatible partitions of incoming and outgoing labels.
- Paragraph "Partition formula for connected scattering kernels" gives this
  scattering-kernel analogue of moment-cumulant inversion and explains its
  relation to cluster factorization.
- Perturbative \(\phi^4\) Green functions yield
  \(\mathcal M=-g+O(g^2)\) for tree-level \(2\to2\) scattering after LSZ;
  the four external scalar propagator numerators \((-\ii)^4\) and four LSZ
  multipliers \(\ii^4\) multiply to one before the vertex factor is converted
  to the invariant amplitude.
- Paragraph `par:lsz-tree-phi-four-after-reduction` records this perturbative
  example as a worked calculation after the nonperturbative
  Haag--Ruelle/LSZ construction, not as a separate theorem.
- The closing scope remark records the exact boundary of the scalar formula:
  it applies only to stable massive isolated local-field poles; massless
  gauge, infraparticle, confinement, resonance, and conformal cases require
  their own asymptotic data and reduction theorems.
- The longitudinal-vector/Goldstone equivalence relation in the broken
  Yang--Mills chapter may use this LSZ machinery only after supplying an
  isolated massive-vector pole and residue convention.  For physical \(W,Z\)
  bosons, literal stable-particle LSZ is replaced by a stable deformation,
  complex-pole scheme, or narrow-width idealization.
- 2026-05-24 issue #393 pass: standardized the one-particle residue in the
  LSZ chapter as \(Z_\phi\).  The unsubscripted source-functional notation
  \(Z[J]\), \(Z_-[J]\), and \(Z_E[J_E]\) remains separate.
- 2026-05-24 issue #433 pass: later renormalization chapters reserve the
  explicit notation \(Z_\phi^{\rm pole}\) for this LSZ/Kallen--Lehmann
  residue when several \(Z\)-factors are compared.  Within this chapter
  \(Z_\phi\) remains the same object, not a Callan--Symanzik or MS
  field-renormalization factor.

## Figure Requirements

- A compact diagram showing external Green-function legs being amputated by
  LSZ into an invariant amplitude.
- A connected-kernel decomposition diagram showing the full \(S\)-kernel as a
  sum over connected components.

## Exclusions

- No cross-section formulas; those belong in the next chapter.
- No unitarity/optical theorem development beyond the amplitude convention.
- No LSZ formula for massless gauge particles or infraparticles.
- No literal stable-particle LSZ formula for unstable electroweak \(W,Z\)
  bosons; those require pole-scheme or narrow-width data before external
  longitudinal amplitudes are interpreted.
- Companion checks are finite convention checks only; they do not replace the
  distributional boundary-value theorem.

## Audit Notes

- 2026-05-24 issue #377 pass: labelled the connected cumulant equation and
  displayed the source-functional Wick-rotation identity in the
  \(x^0=-i\tau\) convention, separating the Euclidean \(+\int J_E\phi_E\)
  source from the Lorentzian \(i^{-N}\) source-derivative compensation.
- 2026-05-24 issue #378 pass: replaced the misleading
  \(\operatorname{Res}_{k^2=-m^2}\) notation by the invariant-denominator
  boundary-value coefficient and displayed the two linear \(k^0\)-pole residues
  explicitly.
- 2026-05-24 issue #381 pass: displayed the tree-level \(2\to2\) external-leg
  phase bookkeeping \((-\ii)^4=1\) and \(\ii^4(-\ii)^4=1\) before reading off
  \(\mathcal M=-g+O(g^2)\).
- 2026-05-24 issue #384 pass: flagged the source-coupling-sign dependence of
  the connected-cumulant prefactor, adding the alternate
  \(Z_-[J]\) convention with \((-i)^{-N}=i^N\).
- 2026-05-27 #615 pass: added the LSZ boundary-value definition, proof block
  for the wave-packet theorem, propositions for invariant-denominator
  residues, spectral projection, contact/interpolating-field stability, and
  the large-time pole selector; added
  `calculation-checks/lsz_residue_checks.py`.
- 2026-05-27 #615 follow-up: formalized the LSZ assumptions, external-state
  normalization, wave-packet matrix element, interpolating-field pole datum,
  connected-source convention, external-amputation map, invariant-amplitude
  convention, partition formula, tree \(\phi^4\) post-reduction example, and
  scalar-LSZ scope boundary.
- 2026-06-04 issue #780 cross-reference pass: recorded the stable-pole
  boundary needed when the broken Yang--Mills chapter invokes LSZ-style
  external-pole extraction for longitudinal massive vectors.
