# Volume IX, Chapter 4 Dossier: Confinement, Screening, and Oblique Confinement

## Logical Role

- Role in the monograph: give a precise line-operator formulation of
  confinement, screening, and oblique confinement before the more general
  phase-invariant discussion of Chapter 7.
- Immediate predecessor: line, surface, and domain-wall operators.
- Immediate successor: discrete theta terms and anomaly inflow.

## Definitions And Results

- Defines the full electric/magnetic line-charge lattices
  \(\Gamma_{\rm e}\oplus\Gamma_{\rm m}\) and the finite center-sensitive
  charge group \(\mathcal C\).
- Defines the external charge system \((\mathcal C,B,S)\), distinguishing
  external charges modulo screening \(\mathcal C/S\) from residual
  topological charges \(S^\perp/S\).
- Proves that an isotropic screened subgroup \(S\) gives a well-defined
  nondegenerate alternating pairing on \(S^\perp/S\).
- Defines renormalized line operators and area, perimeter, zero-tension, and
  rectangular static-potential laws with the line renormalization scheme
  explicit.
- Proves transfer-matrix extraction of the static potential from a positive
  spectral measure.
- Proves that endpoint screening by finite-mass dynamical particles bounds
  the large-separation static energy and rules out a positive asymptotic
  linear potential for the screened charge.
- Proves the strong-coupling lattice area mechanism from character expansion,
  Haar projection, surface selection, and the convergent-polymer hypothesis.
- Defines the finite condensate diagnostic \(K^\perp\), proves the finite
  condensate criterion, and works out magnetic, electric, and oblique
  confinement in \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\).
- Adds a finite charge-lattice figure for the oblique unconfined direction.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Gamma_{\rm e}\), \(\Gamma_{\rm m}\) | full electric and magnetic charge lattices |
| \(\mathcal C\) | finite center-sensitive line-charge group |
| \(B\) | finite alternating Dirac pairing |
| \(S\) | screened subgroup of finite charges |
| \(\mathcal C_{\rm ext}\) | static external charges modulo screening, \(\mathcal C/S\) |
| \(\mathcal C_{\rm top}\) | residual topological charges, \(S^\perp/S\) |
| \(L_\gamma^{\rm ren}(C)\) | renormalized line operator on contour \(C\) |
| \(V_\gamma(L)\) | rectangular-loop static potential |
| \(K\) | isotropic condensed charge subgroup |
| \(K^\perp\) | finite charges with trivial braiding against \(K\) |

## Claim Ledger

1. Line labels depend on the global form of the gauge group and on the
   distinction between full charge lattices and finite center-sensitive data.
2. Screening is an endpoint relation; it identifies external charges but
   leaves a separate topological quotient only on \(S^\perp/S\).
3. Area and perimeter laws are asymptotic statements about renormalized line
   operators with a specified order of limits.
4. A reflection-positive transfer matrix identifies the rectangular-loop
   static potential with the bottom of the static-source spectrum.
5. Endpoint screening by finite-energy dynamical particles bounds the static
   potential at large separation.
6. Strong-coupling lattice area behavior follows from Haar projection forcing
   plaquette surfaces ending on the loop, plus convergence of the polymer
   expansion.
7. Oblique confinement is the finite Dirac-pairing criterion for a dyonic
   condensate \(K=\langle(p,1)\rangle\), with unconfined finite charges
   obeying \(e\equiv pm\pmod N\).
8. The continuum confinement criterion remains an open theorem-level target,
   not a definition.

## Figures

- `fig:oblique-confinement-finite-lattice`: finite
  \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\) charge-lattice picture of
  the dyonic unconfined direction.

## Calculation Checks

- `calculation-checks/oblique_confinement_checks.py` verifies the finite
  charge arithmetic used in the chapter: screened-pairing descent,
  orthogonal complements, maximal isotropic dyonic condensates, the oblique
  condition \(e\equiv pm\pmod N\), and non-mutual-locality of simultaneous
  electric/magnetic generators.

## Audit Notes

- 2026-05-26 confinement depth pass: expanded the chapter from a short
  sketch into a theorem-led treatment of line-charge systems, renormalized
  line laws, screening, strong-coupling lattice area law, and oblique
  confinement; added the calculation-check companion.
