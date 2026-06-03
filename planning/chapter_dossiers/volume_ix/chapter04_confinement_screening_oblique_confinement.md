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
- Records the variational endpoint-screening bound: finite-mass screened
  endpoint trial states bound the large-separation static energy and rule out
  a positive asymptotic linear potential for the screened charge.
- Proves the strong-coupling lattice area mechanism from character expansion,
  Haar projection, surface selection, and the convergent-polymer hypothesis.
- Adds the controlled three-dimensional Polyakov monopole-gas mechanism:
  monopole fugacity generates a dual-photon sine-Gordon potential, the dual
  photon mass is \(m_\gamma^2=2\zeta_{\rm M}/\kappa_{\rm d}\), and the
  primitive Wilson loop becomes a sine-Gordon wall with
  \(\sigma_{\rm P}=8\sqrt{2\kappa_{\rm d}\zeta_{\rm M}}\).  The chapter
  explicitly distinguishes this controlled 3D mechanism from a
  four-dimensional instanton-liquid explanation of Yang--Mills confinement.
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
| \(\varphi,\zeta_{\rm M},\kappa_{\rm d},m_\gamma,\sigma_{\rm P}\) | Polyakov dual photon, monopole fugacity, dual kinetic coefficient, dual-photon mass, and wall/string tension in the controlled 3D monopole-gas mechanism |
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
7. In the controlled three-dimensional compact-Abelian semiclassical window,
   primitive monopoles generate a dual-photon sine-Gordon potential, a mass
   gap, and a calculable Wilson-loop area coefficient
   \(\sigma_{\rm P}=8\kappa_{\rm d}m_\gamma\).  This is not a derivation of
   four-dimensional Yang--Mills confinement.
8. Oblique confinement is the finite Dirac-pairing criterion for a dyonic
   condensate \(K=\langle(p,1)\rangle\), with unconfined finite charges
   obeying \(e\equiv pm\pmod N\).
9. The continuum confinement criterion remains an open theorem-level target,
   not a definition.

## Figures

- `fig:oblique-confinement-finite-lattice`: finite
  \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\) charge-lattice picture of
  the dyonic unconfined direction.

## Calculation Checks

- `calculation-checks/oblique_confinement_checks.py` verifies the finite
  charge arithmetic used in the chapter: screened-pairing descent,
  orthogonal complements, maximal isotropic dyonic condensates, the oblique
  condition \(e\equiv pm\pmod N\), non-mutual-locality of simultaneous
  electric/magnetic generators, and the normalization algebra of the 3D
  Polyakov monopole-gas area law.

## Audit Notes

- 2026-05-26 confinement depth pass: expanded the chapter from a short
  sketch into a theorem-led treatment of line-charge systems, renormalized
  line laws, screening, strong-coupling lattice area law, and oblique
  confinement; added the calculation-check companion.
- 2026-06-03 issue #597 physics-consequence pass: added the controlled 3D
  Polyakov monopole-gas area-law mechanism.  The text derives the dual-photon
  mass, the sine-Gordon wall tension, and the Wilson-loop area coefficient
  from monopole fugacity data, while explicitly distinguishing this mechanism
  from any uncontrolled four-dimensional instanton-liquid confinement claim.
