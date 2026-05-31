# Volume X, Chapter 4 Dossier: Spectral Functions, Kubo Formulae, and Transport

## Logical Role

- Role in the monograph: derive transport coefficients from real-time thermal
  response before hydrodynamics is introduced.
- Immediate predecessor: Schwinger--Keldysh real-time formalism.
- Immediate successor: hydrodynamics from Ward identities and local
  equilibrium.

## Definitions And Results

- Retarded thermal correlator.
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
- Transport limit datum specifying regulator sequence, operator
  normalization, projection/contact prescription, and order of limits.
- Zero-frequency singular sector and finite-volume Mazur projection for
  conserved current overlap.
- Finite-regulator Kubo--Mori projection, Mori--Zwanzig memory identity, and
  the theorem boundary between exact projected dynamics and Markovian
  hydrodynamic closure.
- Conductivity, shear-viscosity, and bulk-viscosity Kubo formulae with
  explicit order of limits and conserved-density projections.
- Once-subtracted retarded dispersion relation and its theorem boundary.
- Open theorem boundary from Kubo formulae to hydrodynamics.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\rho_\beta\) | KMS state at inverse temperature \(\beta\) |
| \(G^R_{AB}\) | retarded correlator |
| \(\rho_{AB}\) | spectral density |
| \(G^{\rm sym}_{AB}\) | symmetrized correlator |
| \(K_{ij}\) | full transverse current response kernel, including contact terms, defined by \(\langle J_i\rangle=-K_{ij}A_j\) |
| \(K^R_{AB}\) | source-response kernel for \(H=H_0-h_BB\), equal to \(-G^R_{AB}\) in the chapter's commutator-retarded convention |
| \(C_{AB}\) | local source-contact contribution to a response kernel |
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

1. The Schwinger--Keldysh branch difference gives the causal
   source-response commutator; with the convention \(H=H_0-h_BB\), this
   kernel is the negative of the chapter's commutator-retarded function
   \(G^R=-i\Theta\langle[A,B]\rangle\).
2. In finite volume, inserting energy eigenstates gives the Lehmann
   representation for \(G^>\) and \(\rho\); for Hermitian operators it implies
   \(\omega\rho_{AA}\ge0\).
3. With the chapter's Fourier and retarded-sign conventions,
   \(\rho_{AA}=-2\operatorname{Im}G^R_{AA}\) for the nonlocal part of the
   response; the substantive assumption is the thermodynamic tempered
   boundary value and the separation of real contact polynomials.
4. KMS implies detailed balance and the fluctuation--dissipation relation.
5. Local source contacts are part of the full background response but not of
   the commutator spectral measure at nonzero frequency.
6. A transport coefficient requires a declared thermodynamic and
   zero-frequency order of limits.
7. Conserved charges with nonzero current overlap give a positive
   zero-frequency singular sector bounded by the Mazur projection; this is
   separated from the finite dissipative dc slope.
8. At finite regulator, the Kubo--Mori projection gives an exact
   Mori--Zwanzig block identity for chosen slow coordinates.  This identity
   is algebraic and does not by itself imply transport.
9. A diffusion or viscosity coefficient arises from a further theorem
   boundary: thermodynamic limit, decay of projected kernels, controlled
   \(k\to0\) scaling, and removal of Drude sectors must turn the exact
   memory equation into a local low-frequency closure.
10. Conductivity and viscosity are low-frequency spectral slopes after contact
   terms, Drude weights, order of limits, and conserved-density mixings are
   specified.
11. Subtracted dispersion relations require large-\(\omega\) control and an
   explicit declaration of contact terms.
12. Hydrodynamic control requires additional analyticity, clustering,
   equilibration, and limit-exchange hypotheses.

## Calculation Checks

- `calculation-checks/thermal_kubo_checks.py` verifies the two-level
  detailed-balance and fluctuation--dissipation weights, the retarded sign
  \(\rho=-2\operatorname{Im}G^R\), the shear-viscosity spectral slope, and
  invariance of dissipative spectral slopes under real contact terms, and
  the finite Mazur projection/Drude-weight normalization.  It also checks a
  two-dimensional finite-regulator Mori--Zwanzig identity and its
  Laplace-space Schur complement.

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
