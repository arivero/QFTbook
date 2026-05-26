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
  \(\rho=-2\operatorname{Im}G^R\).
- KMS fluctuation--dissipation relation.
- Linear response from Schwinger--Keldysh contour difference, with the
  source-response sign separated from the commutator-retarded convention.
- Separation between commutator correlators, local contact terms, and full
  background-source response kernels.
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
   response.
4. KMS implies detailed balance and the fluctuation--dissipation relation.
5. Local source contacts are part of the full background response but not of
   the commutator spectral measure at nonzero frequency.
6. Conductivity and viscosity are low-frequency spectral slopes after contact
   terms, Drude weights, order of limits, and conserved-density mixings are
   specified.
7. Subtracted dispersion relations require large-\(\omega\) control and an
   explicit declaration of contact terms.
8. Hydrodynamic control requires additional analyticity, clustering,
   equilibration, and limit-exchange hypotheses.

## Calculation Checks

- `calculation-checks/thermal_kubo_checks.py` verifies the two-level
  detailed-balance and fluctuation--dissipation weights, the retarded sign
  \(\rho=-2\operatorname{Im}G^R\), the shear-viscosity spectral slope, and
  invariance of dissipative spectral slopes under real contact terms.

## Figures

- None in this chapter.
