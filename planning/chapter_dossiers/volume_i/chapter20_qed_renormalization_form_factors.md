# Volume I, Chapter 20 Dossier: QED Renormalization and Electromagnetic Form Factors

Status: revised, source-audited, and formalized on 2026-05-27.

## Source Placement

- Follows QED as a gauge-fixed representative perturbation theory with LSZ
  external factors.
- Develops photon vacuum polarization, photon field-strength normalization,
  the electron current matrix element, and the one-loop anomalous magnetic
  moment.
- Precedes the systematic treatment of infrared divergences and inclusive or
  dressed charged scattering.
- Source material used:
  - handwritten `references/253a lectures 2022.pdf`, trace pp. 224--244;
  - `references/253a_notes.tex`, roughly lines 4579--4855, used only as
    secondary text after checking against the handwritten pages;
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
  \(g=-e\), \(e>0\), and regulator-dependent representative variables labelled
  by the superscript \(B\).
- Renormalized representative fields are fixed by pole-residue conditions for
  photon field strength and electron spinor fields.
- Dimensional regularization is used for one-loop integrals, with
  \(D=4-\epsilon\), \(\eta^{\mu\nu}\eta_{\mu\nu}=D\), and
  \(\operatorname{Tr}\mathbf 1=4\).
- Charge normalization is imposed through the zero-momentum current matrix
  element.
- The handwritten source, not the student transcription, fixes the charge
  convention: \(e=e^B Z_A^{1/2}\).  The factor \(Z_\psi\) multiplies the
  spinor covariant derivative and is not part of the gauge-representative
  charge.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(A_\mu^B,\psi^B,m^B,e^B\) | regulator-dependent vector representative, spinor, mass, and charge |
| \(A_\mu,\psi,m,e\) | renormalized representatives, physical mass parameter, charge parameter |
| \(Z_A,Z_\psi,Z_1\) | photon, spinor, and vertex renormalization constants |
| \(\delta m\) | mass counterterm |
| \(\Pi^{\mu\nu}\) | photon one-particle-irreducible self-energy |
| \(\pi(k^2)\) | scalar vacuum-polarization function |
| \(j^\mu\) | electromagnetic current normalized by \(\partial_\nu F^{\mu\nu}=j^\mu\) |
| \(M^{\mu\nu}(k)\) | noncontact current-current two-point coefficient |
| \(M_x^2\) | \(m^2+x(1-x)k^2\) in the vacuum-polarization integral |
| \(F(k^2),G(k^2)\) | electron electromagnetic form factors in the chapter's gamma convention |
| \(F_{1,2}^{\rm DP}\) | Dirac--Pauli form factors; \(F_1^{\rm DP}=F+G\), \(F_2^{\rm DP}=-G\) |
| \(g_{\mathrm{mag}}\) | electron magnetic \(g\)-factor |
| \(\alpha\) | fine-structure parameter \(e^2/(4\pi)\) |
| \(\mathcal W_\alpha\) | Abelian Ward--Takahashi generator on the QED 1PI functional |

## Claims Established

- `def:qed-regulated-explicit-coupling-coordinates` fixes the regulated QED
  representative variables, the explicit-coupling normalization, and the
  distinction between field-residue constants and the electric charge
  coordinate.
- `prop:qed-ward-organization-current` proves that gauge-covariant local
  counterterms organize the electron kinetic and QED vertex counterterms
  through the Abelian Ward identity \(Z_1=Z_\psi\).
- The current entering form factors is consequently
  \(j^\mu=-iZ_A^{-1}eZ_\psi\bar\psi\gamma^\mu\psi\), as follows from the
  renormalized Maxwell equation.
- `prop:qed-photon-self-energy-transversality` proves that current
  conservation forces the photon self-energy to be transverse:
  \(k_\mu\Pi^{\mu\nu}=0\).
- The transversality statement is now identified as the two-photon consequence
  of a linear Abelian Ward--Takahashi identity
  \(\mathcal W_\alpha\Gamma_{\rm inv}=0\).  The chapter contrasts this with
  the nonabelian Slavnov--Taylor identity, which is quadratic in the 1PI
  functional because BRST variations of \(A_\mu\) and \(c\) are composite
  insertions represented by external BRST sources.
- Lorentz covariance then gives
  \(\Pi^{\mu\nu}=(\eta^{\mu\nu}k^2-k^\mu k^\nu)\pi(k^2)\).
- The photon pole normalization condition is \(\pi(0)=0\), fixing \(Z_A\) at
  one loop.
- `prop:qed-one-loop-vacuum-polarization` gives the one-loop pole
  \(Z_A=1-e^2/(6\pi^2\epsilon)+\cdots\) and the finite Feynman-parameter
  integral after subtraction at \(k^2=0\).
- The dimensional-regularization algebra is displayed through the shifted
  numerator, \(p_\mu p_\nu\mapsto D^{-1}\eta_{\mu\nu}p^2\), and the two scalar
  integrals analytically continued in \(D\).
- `def:qed-electron-electromagnetic-form-factors` defines the electron current
  matrix element in a parity-preserving theory.  The chapter's \((F,G)\) basis
  is related to the Dirac--Pauli basis by \(F_1^{\rm DP}=F+G\) and
  \(F_2^{\rm DP}=-G\).
- Charge normalization is now written as a distributional plane-wave
  normalization calculation in prose: \(\widehat Q|\vec p,\sigma\rangle=q|\vec
  p,\sigma\rangle\) is equivalent to \(F(0)+G(0)=1\).
- `prop:qed-magnetic-factor-from-form-factor` proves that, in a weak magnetic
  background, \(g_{\mathrm{mag}}=2F(0)=2(1-G(0))\).
- The tree current vertex plus photon self-energy chain contributes only to
  \(F(k^2)\); the order-\(e^2\) contribution to \(G(k^2)\) comes from the
  proper vertex correction.
- `prop:qed-one-loop-vertex-schwinger` records the one-loop vertex correction
  \(G(0)=-\alpha/(2\pi)\), hence
  \(g_{\mathrm{mag}}=2+\alpha/\pi+O(\alpha^2)\).

## Calculation Checks

- `calculation-checks/qed_form_factor_checks.py` checks the exact rational
  factors in the vacuum-polarization pole, the Ward organization of \(Z_1\),
  the \((F,G)\) versus Dirac--Pauli basis conversion, the zero-transfer
  Feynman-parameter integral for \(G(0)\), and
  \(g_{\mathrm{mag}}-2=\alpha/\pi\).

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
- No derivation of the nonabelian Slavnov--Taylor identity in this QED
  chapter; the chapter only cross-references the BRST chapter to mark the
  linear-versus-quadratic distinction.

## Audit Notes

- 2026-05-24 issue #248 pass: added the linear Ward--Takahashi functional
  identity behind photon self-energy transversality and cross-referenced the
  BRST chapter's quadratic Slavnov--Taylor identity.
- 2026-05-24 issue #398 pass: made the Gordon-identity comparison to the
  Dirac--Pauli basis explicit in the mostly-plus convention.  The manuscript
  now displays \(m^{-1}S^{\mu\nu}k_\nu=\gamma^\mu+\ii(p+p')^\mu/(2m)\) on
  external spinors and records that \(F_2^{\rm DP}=-G\), so
  \(G(0)=-\alpha/(2\pi)\) is equivalent to the standard positive
  \(F_2^{\rm DP}(0)=+\alpha/(2\pi)\).
- 2026-05-27 issue #615 pass: converted the chapter's definitions,
  Ward-identity argument, photon transversality, vacuum-polarization
  calculation, charge normalization, magnetic-moment extraction, and one-loop
  vertex correction into labeled formal environments; added the companion
  rational calculation check listed above.
