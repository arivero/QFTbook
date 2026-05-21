# Volume I, Chapter 20 Dossier: QED Renormalization and Electromagnetic Form Factors

## Source Placement

- Follows QED as a gauge-fixed representative perturbation theory with LSZ
  external factors.
- Develops photon vacuum polarization, photon field-strength normalization,
  the electron current matrix element, and the one-loop anomalous magnetic
  moment.
- Precedes the systematic treatment of infrared divergences and inclusive or
  dressed charged scattering.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 9490--10515;
  - `references/sound_references/fredenhagen_rejzner_paqft_1208.1428.pdf`
    for the interpretation of renormalization as local counterterm freedom;
  - `references/sound_references/rosten_exact_rg_1003.1366.pdf` for
    Wilsonian/ERG perspective on field-strength renormalization and
    gauge-invariant formulations.

## External Reference Boundary

- The chapter performs the one-loop QED calculations in the local Feynman-rule
  framework established earlier.
- It uses external references only to orient the meaning of counterterms and
  renormalization conditions; no external axiomatic framework is adopted as the
  foundation.
- The Ward identity is used in its local Abelian form: spinor wavefunction and
  vertex counterterms combine gauge-covariantly.

## Framework

- Four-dimensional QED in covariant gauge, with electron convention
  \(g=-e\), \(e>0\).
- Renormalized representative fields are fixed by pole-residue conditions for
  photon field strength and electron spinor fields.
- Dimensional regularization is used for one-loop integrals, with
  \(D=4-\epsilon\), \(\eta^{\mu\nu}\eta_{\mu\nu}=D\), and
  \(\operatorname{Tr}\mathbf 1=4\).
- Charge normalization is imposed through the zero-momentum current matrix
  element.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(A_\mu^B,\psi^B,m^B,e^B\) | bare vector representative, spinor, mass, and charge |
| \(A_\mu,\psi,m,e\) | renormalized representatives, physical mass parameter, charge parameter |
| \(Z_A,Z_\psi,Z_1\) | photon, spinor, and vertex renormalization constants |
| \(\delta m\) | mass counterterm |
| \(\Pi^{\mu\nu}\) | photon one-particle-irreducible self-energy |
| \(\pi(k^2)\) | scalar vacuum-polarization function |
| \(j^\mu\) | electromagnetic current |
| \(F(k^2),G(k^2)\) | electron electromagnetic form factors in the chapter's gamma convention |
| \(g_{\mathrm{mag}}\) | electron magnetic \(g\)-factor |
| \(\alpha\) | fine-structure parameter \(e^2/(4\pi)\) |

## Claims Established

- Gauge-covariant local counterterms organize the electron kinetic and QED
  vertex counterterms through the Abelian Ward identity \(Z_1=Z_\psi\).
- Current conservation forces the photon self-energy to be transverse:
  \(k_\mu\Pi^{\mu\nu}=0\).
- Lorentz covariance then gives
  \(\Pi^{\mu\nu}=(\eta^{\mu\nu}k^2-k^\mu k^\nu)\pi(k^2)\).
- The photon pole normalization condition is \(\pi(0)=0\), fixing \(Z_A\) at
  one loop.
- The one-loop finite vacuum-polarization function is the standard
  Feynman-parameter integral after subtraction at \(k^2=0\).
- The electron current matrix element has two form factors in the stated
  parity-preserving theory, and charge normalization gives \(F(0)+G(0)=1\).
- In a weak magnetic background, \(g_{\mathrm{mag}}=2F(0)\).
- The one-loop vertex correction gives \(G(0)=-\alpha/(2\pi)\), hence
  \(g_{\mathrm{mag}}=2+\alpha/\pi+O(\alpha^2)\).

## Figure Requirements

- Compact diagrammatic Dyson series for the photon propagator.
- One-loop photon vacuum-polarization diagram plus photon counterterm.
- Current insertion/form-factor diagram.
- One-loop vertex-correction diagram with clear momentum labels.

## Exclusions

- No full proof of perturbative renormalizability.
- No beta function or running coupling beyond the one-loop vacuum-polarization
  subtraction.
- No all-order Ward--Takahashi proof.
- No infrared cancellation or soft-photon exponentiation.
- No nonabelian generalization.
