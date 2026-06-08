# Volume X, Chapter 4 Dossier: Spectral Functions, Kubo Formulae, and Transport
Source-File: monograph/tex/volumes/volume_x/chapter04_spectral_functions_kubo_transport.tex

## Logical Role

- Role in the monograph: derive transport coefficients from real-time thermal
  response before hydrodynamics is introduced.
- Immediate predecessor: Schwinger--Keldysh real-time formalism.
- Immediate successor: hydrodynamics from Ward identities and local
  equilibrium.

## Definitions And Results

- Retarded thermal correlator.
- Canonical real-time convention ledger covering Fourier transforms,
  unsigned/signed Wightman functions, \(\rho_{\rm comm}\),
  \(\widehat\rho=\rho_{\rm comm}/(2\pi)\), \(G^{R,\rm comm}\), \(K^R\),
  and the Euclidean continuation sign.
- Spectral density and finite-volume spectral representation.
- Finite-volume Lehmann representation with explicit Boltzmann weights and
  distributional positivity \(\omega\rho_{AA}\ge0\).
- Retarded spectral representation with the chapter's sign convention
  \(\rho=-2\operatorname{Im}G^R\), recorded as boundary-value convention
  rather than theorem-family content.
- KMS fluctuation--dissipation relation.
- Linear response from Schwinger--Keldysh contour difference, with the
  source-response sign separated from the commutator-retarded convention.
- Separation between commutator correlators, local contact terms, and full
  background-source response kernels.
- Single contact-sign convention:
  \(\mathcal K^{\rm full}=-G^{R,\rm comm}+C^{\rm resp}\), while the
  conductivity kernel defined by \(\langle J\rangle=-K^{\rm cond}A\) is
  \(K^{\rm cond}=G^{R,\rm comm}-C^{\rm resp}\).
- Regulated charged-oscillator diamagnetic contact example showing the static
  paramagnetic--diamagnetic cancellation.
- Transport limit datum specifying regulator sequence, operator
  normalization, projection/contact prescription, and order of limits.
- Zero-frequency singular sector and finite-volume Mazur projection for
  conserved current overlap.
- Finite-regulator Kubo--Mori projection, Mori--Zwanzig memory identity, and
  the theorem boundary between exact projected dynamics and Markovian
  hydrodynamic closure.
- Conductivity, shear-viscosity, and bulk-viscosity Kubo formulae with
  explicit order of limits and conserved-density projections.
- Direct warning that extracting the low-frequency Kubo slope from Euclidean
  thermal data is more unstable than reconstructing a broad spectral feature:
  the Euclidean kernel smooths the spectral density, and fixed finite smooth
  sum rules do not stabilize the local slope unless additional real-time input,
  priors, or a controlled model class are supplied; admissible finite sum rules
  are understood in the Chapter 2 sense with real constraints and finite
  reference moments.
- Once-subtracted retarded dispersion relation and its theorem boundary.
- Open theorem boundary from Kubo formulae to hydrodynamics.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\rho_\beta\) | KMS state at inverse temperature \(\beta\) |
| \(G^{R,\mathrm{comm}}_{AB}\), \(G^R_{AB}\) | commutator-retarded correlator; the shorter form is used in the chapter once the convention table is declared |
| \(K^R_{AB}\) | source-response kernel for \(H=H_0-h_BB\), equal to \(-G^{R,\mathrm{comm}}_{AB}\) |
| \(\rho^{\rm comm}_{AB}\), \(\rho_{AB}\) | commutator spectral density with \(\rho=-2\operatorname{Im}G^R\); the shorter form is used after the table |
| \(\widehat\rho_{AB}\) | measure-normalized spectral distribution \(\rho^{\rm comm}_{AB}/(2\pi)\) |
| \(G^{\rm sym}_{AB}\) | symmetrized correlator |
| \(\mathcal K^{\rm full}_{AB}\) | full source derivative \(\delta\langle A\rangle/\delta h_B=-G^{R,\rm comm}_{AB}+C^{\rm resp}_{AB}\) |
| \(K^{\rm cond}_{ij}\) | transverse conductivity kernel defined by \(\langle J_i\rangle=-K^{\rm cond}_{ij}A_j\), equal to \(G^{R,\rm comm}_{J_iJ_j}-C^{\rm resp}_{ij}\) |
| \(C^{\rm resp}_{AB}\) | local contact contribution to the full source-response derivative |
| \(I_i\), \(\bar I_i\) | total current and connected total current in finite volume |
| \(Q_a\), \(C_{ab}\), \(v_{ia}\) | conserved operators, symmetrized covariance, and current-charge overlap |
| \(D_{ij}\) | Drude-weight matrix in \(\operatorname{Re}\sigma_{ij}\) |
| \(\mathcal L\) | finite-regulator Liouville generator \(\mathcal L X=\ii[H_L,X]\) |
| \((\cdot,\cdot)_\beta\) | Kubo--Mori inner product on the finite-regulator operator space |
| \(P,Q\) | Kubo--Mori projection onto chosen slow operators and its complement |
| \(\Omega_a{}^b\) | projected reactive/frequency matrix in the slow-coordinate equation |
| \(M_a{}^b(t)\) | projected memory kernel before the hydrodynamic Markovian limit |
| \(\sigma_{ij}\) | conductivity tensor |
| \(\eta\) | shear viscosity |
| \(\zeta\) | bulk viscosity |
| \(\mathcal P\) | pressure channel with conserved energy-density overlap subtracted |
| \(c_s^2\) | equilibrium speed-of-sound derivative \((\partial p/\partial\varepsilon)_{\rm eq}\) |

## Claim Ledger

1. The chapter is the canonical owner of the Volume X real-time convention
   package: unsigned Wightman KMS, signed fermion lesser convention,
   \(\rho_{\rm comm}\) versus \(\widehat\rho\), retarded \(z-\omega\)
   denominator, and Euclidean \(G_E=-G^R\) sign at nonzero Matsubara frequency.
2. The Schwinger--Keldysh branch difference gives the causal
   source-response commutator; with the convention \(H=H_0-h_BB\), this
   kernel is the negative of the chapter's commutator-retarded function
   \(G^R=-i\Theta\langle[A,B]\rangle\).
3. In finite volume, inserting energy eigenstates gives the Lehmann
   representation for \(G^>\) and \(\rho\); for Hermitian operators it implies
   \(\omega\rho_{AA}\ge0\).
4. With the chapter's Fourier and retarded-sign conventions,
   \(\rho_{AA}=-2\operatorname{Im}G^R_{AA}\) for the nonlocal part of the
   response; the substantive assumption is the thermodynamic tempered
   boundary value and the separation of real contact polynomials.
5. KMS implies detailed balance and the fluctuation--dissipation relation.
6. Local source contacts are part of the full background response but not of
   the commutator spectral measure at nonzero frequency.  The contact sign is
   fixed in the full response derivative
   \(\mathcal K^{\rm full}=-G^{R,\rm comm}+C^{\rm resp}\); a kernel defined
   with an additional minus sign, such as
   \(\langle J\rangle=-K^{\rm cond}A\), carries the opposite contact
   contribution.
7. A transport coefficient requires a declared thermodynamic and
   zero-frequency order of limits.
8. Conserved charges with nonzero current overlap give a positive
   zero-frequency singular sector bounded by the Mazur projection; this is
   separated from the finite dissipative dc slope.
9. At finite regulator, the Kubo--Mori projection gives an exact
   Mori--Zwanzig block identity for chosen slow coordinates.  This identity
   is algebraic and does not by itself imply transport.
10. A diffusion or viscosity coefficient arises from a further theorem
   boundary: thermodynamic limit, decay of projected kernels, controlled
   \(k\to0\) scaling, and removal of Drude sectors must turn the exact
   memory equation into a local low-frequency closure.
11. Conductivity and viscosity are low-frequency spectral slopes after contact
   terms, Drude weights, order of limits, and conserved-density mixings are
   specified.  In the current channel
   \(K^{\rm cond}=G^{R,\rm comm}-C^{\rm resp}\), so the diamagnetic contact
   that cancels the static paramagnetic response has the sign opposite to its
   full-response-derivative entry.
12. Euclidean data and admissible fixed finite smooth sum rules whose real
   weights have finite reference moments and admit the Chapter 2 away-from-zero
   compensator system constrain smeared spectral integrals; they do not stably
   determine the transport slope without additional real-time input, priors, or
   a controlled model class.
13. Subtracted dispersion relations require large-\(\omega\) control and an
   explicit declaration of contact terms.
14. Hydrodynamic control requires additional analyticity, clustering,
   equilibration, and limit-exchange hypotheses.

## Calculation Checks

- `calculation-checks/thermal_kubo_checks.py` verifies the two-level
  detailed-balance and fluctuation--dissipation weights, the retarded sign
  \(\rho=-2\operatorname{Im}G^R\), the shear-viscosity spectral slope, and
  invariance of dissipative spectral slopes under real contact terms.  It
  also checks a minimally coupled charged oscillator with nonzero diamagnetic
  response contact, verifying the static full-response cancellation, the
  opposite contact sign in \(K^{\rm cond}\), and the unchanged spectral part;
  the finite Mazur projection/Drude-weight normalization; and a
  two-dimensional finite-regulator Mori--Zwanzig identity with its
  Laplace-space Schur complement.
- The #882 canonical convention ledger is also guarded by
  `calculation-checks/kms_foundation_checks.py` and
  `calculation-checks/finite_temperature_path_integral_checks.py`, which test
  the fermionic lesser sign, \(H-hB\) source-response sign, \(2\pi\)
  normalization, and retarded denominator.

## Figures

- Figure `fig:kubo-order-of-limits`: thermodynamic limit, zero-frequency
  limit, and prior separation of Drude/conserved singular sectors.

## Audit Notes

- 2026-05-30 figure semantic audit: added the missing body callout for
  `fig:kubo-order-of-limits` and rewrote the caption/body text to state the
  positive distributional decomposition into a singular Drude sector and a
  locally integrable regular part.
- 2026-05-31 statmech crosswalk/#703 pass: added the Kubo--Mori projection
  and memory-kernel bridge from exact finite-regulator dynamics to
  hydrodynamic closure, with the additional thermodynamic and decay
  hypotheses stated at the point where they enter.
- 2026-05-31 projected-current closure pass: expanded the theorem boundary
  behind the Mori-Zwanzig bridge into an explicit hydrodynamic closure datum:
  thermodynamic convergence of projected kernels, Laplace-transform
  regularity after singular-sector subtraction, initial-force decoupling,
  nonsingular charge susceptibility, derivation of the diffusive pole from
  the closed Laplace-space memory equation, and the Einstein relation
  \(\Sigma=D\chi\) as a coordinate comparison between current and density
  response.
- 2026-05-31 issue #691 continuation: demoted the finite-regulator
  Mori--Zwanzig projection identity from proposition/proof form to
  paragraph-level block-Duhamel derivation.  The exact identity and all slow
  coordinate formulae remain; theorem-family weight is reserved for the
  hydrodynamic closure hypotheses and estimates needed after the
  thermodynamic limit.
- 2026-06-04 transport-reconstruction pass: connected the conductivity Kubo
  slope to the Chapter 2 Euclidean reconstruction instability, emphasizing that
  positivity, admissible fixed finite smooth sum rules, and finite Euclidean
  samples do not stably determine \(\rho(\omega)/(2\omega)\) as
  \(\omega\downarrow0\).
- 2026-06-04 issue #822 re-audit: narrowed the transport-reconstruction
  warning to positivity plus admissible fixed finite smooth sum rules, matching
  the Chapter 2 compensator construction and avoiding any claim about complete
  infinite moment data.
- 2026-06-04 issue #830 re-audit: qualified the finite-sum-rule warning by the
  Chapter 2 restricted-weight compensator hypothesis, so smooth weights whose
  restrictions become dependent on the allowed compensator region are not
  silently included.
- 2026-06-04 issue #831 re-audit: synchronized the transport warning with the
  Chapter 2 admissibility definition: complex constraints must be split into a
  finite real family, finite reference moments are part of the datum, and
  restricted compensator independence alone does not certify finite sum-rule
  values.
- 2026-06-08 issue #882 convention-owner pass: added the compact real-time
  convention ledger and synchronized it with Chapters 1, 2, and 12.  The pass
  is a convention and architecture repair supporting later transport physics,
  not an additional lemma-density expansion.
- 2026-06-08 issue #926 contact-sign pass: replaced the ambiguous current
  response contact \(C\) by \(C^{\rm resp}\) in the full source derivative,
  defined \(K^{\rm cond}=-\mathcal K^{\rm full}\) for conductivity, and added
  a charged-oscillator diamagnetic contact example and check so the static
  response, conductivity kernel, and spectral part use one sign ledger.
