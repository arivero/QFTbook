# Volume I, Chapter 16 Dossier: Spinor Fields, Fermionic Statistics, and Grassmann Path Integrals

## Source Placement

- Follows the massive-particle spin and spinor-intertwiner chapter.
- Develops the Dirac field operator, the CAR local algebra, Weyl and Majorana
  projections, finite-dimensional Berezin calculus, the Grassmann path
  integral, and the spinorial pole structure needed for external fermions.
- Precedes massless helicity, gauge redundancy, Maxwell theory, and QED.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 6773--7825;
  - `references/sound_references/straumann_poincare_representations_0809.4942.pdf`
    and text sidecar for free-field representation and spin-statistics
    context;
  - `references/sound_references/fredenhagen_rejzner_paqft_1208.1428.pdf`
    and text sidecar for the CAR and functional-integral setting.

## External Reference Boundary

- The chapter verifies locality for the free Dirac field built from the
  spinor one-particle data of Chapter 15.
- The full spin-statistics theorem is cited only as a theorem-level statement
  under Wightman-type assumptions; its proof is not reproduced.
- The Berezin path integral is constructed first in finite dimension and then
  used as the regulated model for the continuum notation.

## Framework

- Four-dimensional Minkowski spacetime with mostly-plus metric.
- Gamma matrices obey \(\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\).
- Spinor fields are operator-valued distributions on a common dense domain,
  with a fermion-parity grading.
- Functional integrals over spinor fields are formal continuum limits of
  finite-dimensional Grassmann Gaussian integrals.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\psi_\alpha,\bar\psi^\alpha\) | Dirac spinor field and Dirac adjoint |
| \(\beta\) | \(\ii\gamma^0\), used in \(\bar\psi=\psi^\dagger\beta\) |
| \(b_\sigma^\dagger,d_\sigma^\dagger\) | creation operators for charged spin-\(\frac12\) particle and antiparticle |
| \(\Delta_+\) | positive-frequency scalar two-point distribution |
| \(P_\pm\) | chiral projectors \((1\pm\gamma_5)/2\) |
| \(B\) | matrix implementing complex conjugation on gamma matrices |
| \(\Lambda_N\) | Grassmann algebra on \(N\) generators |
| \(\eta_a,\bar\eta_a\) | finite-dimensional Grassmann generators |
| \(A\) | invertible matrix in a Berezin Gaussian integral |
| \(J,\bar J\) | Grassmann sources |
| \(S_F\) | free Dirac Feynman two-point function |
| \(Z_\psi\) | spinor one-particle pole residue |

## Claims Established

- The free Dirac field built from spin-\(\frac12\) one-particle data is local
  when its creation and annihilation operators obey CAR.
- Its anticommutator is a Dirac differential operator applied to the
  Pauli--Jordan distribution, hence has causal support.
- Chiral and Majorana spinor fields are Lorentz-covariant reductions of the
  Dirac representation under stated algebraic conditions.
- Berezin integration is the finite-dimensional algebraic operation whose
  Gaussian integral produces determinants and fermionic Wick signs.
- The Grassmann path integral is obtained from coherent-state resolutions of
  identity for a two-state fermionic system.
- The Dirac propagator is the inverse of \(\not\partial+m\) with the Feynman
  boundary value.
- In an interacting theory with an isolated charged massive spin-\(\frac12\)
  pole, the spinor two-point function has a pole residue determined by the
  spinor intertwiners; spinorial LSZ external factors are those residues.

## Figure Requirements

- Two-state fermionic oscillator figure showing the creation and annihilation
  maps.
- Optional time-slicing figure for the coherent-state path integral.

## Exclusions

- No massless helicity representations.
- No Maxwell gauge constraints.
- No QED vertices or radiative corrections.
- No proof of the general spin-statistics theorem.
- No use of fermionic diagrams before the spinorial LSZ pole has been stated.
