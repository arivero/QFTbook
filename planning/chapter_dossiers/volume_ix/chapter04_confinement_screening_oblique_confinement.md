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
- Adds a Wilson-loop string-breaking spectral extraction test: the single
  Wilson-loop channel may stay flux-tube dominated over a finite Euclidean-time
  window even when the screened broken-string state is the static ground state,
  so resolving string breaking requires a full-rank correlator basis, spectral
  tails, and entry-error margins.
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
- Adds the continuum line-confinement criterion from renormalized Wilson,
  't Hooft, and dyonic lines: UV line renormalization, thermodynamic limit, and
  large-loop/static limits are ordered explicitly; the surface-cost hypothesis
  converts screening, clustering, endpoint, and condensate data into positive
  area rates for charges outside \(K^\perp\), while isolating the remaining
  four-dimensional Yang--Mills theorem boundary.

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
| \(O_{\rm F}(L)\), \(O_{\rm B}(L)\) | flux-tube and broken-string trial operators in a static-source sector |
| \(C_{ij}(L,T)\), \(Z_{in}(L)\) | static-source correlator matrix and spectral overlap matrix |
| \(\varphi,\zeta_{\rm M},\kappa_{\rm d},m_\gamma,\sigma_{\rm P}\) | Polyakov dual photon, monopole fugacity, dual kinetic coefficient, dual-photon mass, and wall/string tension in the controlled 3D monopole-gas mechanism |
| \(K\) | isotropic condensed charge subgroup |
| \(K^\perp\) | finite charges with trivial braiding against \(K\) |
| \(d_K(\overline\gamma)\) | maximal finite pairing distance from a line class to the condensate |
| \(\sigma_\gamma^\pm\), \(\mu_\gamma\) | continuum surface-cost and perimeter constants in the line criterion |

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
6. In a theory with dynamical screening fields, a single finite-time Wilson
   loop is not a confinement order parameter: the flux-tube overlap can hide the
   broken-string ground state unless a full-rank flux/broken-string correlator
   matrix and GEVP extraction resolve both states.
7. Strong-coupling lattice area behavior follows from Haar projection forcing
   plaquette surfaces ending on the loop, plus convergence of the polymer
   expansion.
8. In the controlled three-dimensional compact-Abelian semiclassical window,
   primitive monopoles generate a dual-photon sine-Gordon potential, a mass
   gap, and a calculable Wilson-loop area coefficient
   \(\sigma_{\rm P}=8\kappa_{\rm d}m_\gamma\).  This is not a derivation of
   four-dimensional Yang--Mills confinement.
9. Oblique confinement is the finite Dirac-pairing criterion for a dyonic
   condensate \(K=\langle(p,1)\rangle\), with unconfined finite charges
   obeying \(e\equiv pm\pmod N\).
10. The continuum line-confinement criterion is now formulated as a conditional
    implication from renormalized-line existence, infrared clustering/static
    spectral control, endpoint data, and surface-cost bounds to positive area
    rates.  The remaining open theorem-level target is proving those
    surface-cost bounds from four-dimensional continuum Yang--Mills.

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
  Polyakov monopole-gas area law.  It also checks the finite string-breaking
  spectral model behind the Wilson-loop extraction test: finite-time flux
  dominance despite a screened ground state, exact two-channel GEVP roots,
  rank-one basis failure, and an omitted-tail entry bound.  The same companion
  verifies the continuum criterion's finite line-charge arithmetic, pairing
  distance, local perimeter/cusp subtraction, positive area-rate extraction,
  rectangular static-limit ordering, endpoint-screening negative control, and
  strong-coupling surface-window calibration.

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
- 2026-06-04 QCD confinement-diagnostics pass: added the string-breaking
  spectral extraction test to separate finite-time Wilson-loop area signals from
  the asymptotic screened static energy, with an exact finite companion check.
- 2026-06-04 continuum line-criterion pass: replaced the single open-problem
  status with a renormalized-line criterion and surface-cost theorem boundary,
  connecting the chapter to the QCD rigor track (#630) and the generalized
  symmetry/defect proof-debt track (#698) without treating finite charge
  arithmetic or cochain laboratories as continuum confinement proofs.
