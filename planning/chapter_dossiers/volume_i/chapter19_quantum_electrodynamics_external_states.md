# Volume I, Chapter 19 Dossier: Quantum Electrodynamics and External States

## Source Placement

- Follows the construction of spinor fields, massless helicity
  representatives, Maxwell constraints, and covariant gauge fixing.
- Introduces the Abelian coupling between a charged Dirac representative
  field and the Maxwell representative field.
- Uses the already constructed Haag--Ruelle and LSZ framework before assigning
  scattering meaning to QED diagrams.
- Precedes QED renormalization, vacuum polarization, vertex corrections,
  anomalous magnetic moments, and infrared-inclusive scattering.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 9114--9545;
  - `references/sound_references/buchholz_dybalski_scattering_2023.pdf`
    for the boundary between ordinary particle scattering and infraparticles;
  - `references/sound_references/rosten_exact_rg_1003.1366.pdf` for the
    distinction between manifestly gauge-invariant formulations and
    gauge-fixed representative correlators.

## External Reference Boundary

- The chapter derives the classical gauge covariance of the QED Lagrangian and
  the tree-level Ward cancellation directly.
- It uses the Buchholz--Dybalski review only to justify the stated limitation
  that charged sectors of long-range Abelian gauge theories need infrared-aware
  asymptotic constructions beyond ordinary massive Haag--Ruelle hypotheses.
- It uses Rosten only as framework orientation: gauge-fixed correlators of
  representative fields are computational devices, while gauge-invariant
  operator correlators are the natural objects in manifestly gauge-invariant
  formulations.

## Framework

- Four-dimensional Minkowski spacetime with mostly-plus metric.
- A charged Dirac representative field \(\psi_\alpha\) of charge \(g\), its
  Dirac adjoint \(\bar\psi^\alpha\), and an Abelian vector-potential
  representative \(A_\mu\).
- Gauge transformations are local \(U(1)\) representative changes
  \(A_\mu\mapsto A_\mu+\partial_\mu\xi\),
  \(\psi\mapsto\exp(\ii g\xi)\psi\).
- Perturbative QED is treated as a formal expansion of gauge-fixed Green
  functions around the free Maxwell and free Dirac theories.
- External electron, positron, and photon factors are LSZ pole residues, with
  infrared qualifications stated explicitly.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(g\) | charge of the Dirac field; \(g=-e\) for the electron convention |
| \(D_\mu\psi\) | Abelian gauge-covariant derivative \(\partial_\mu\psi-\ii gA_\mu\psi\) |
| \(j^\mu\) | electromagnetic current represented, in these gamma conventions, by \(\ii g\bar\psi\gamma^\mu\psi\) |
| \(\xi_{\mathrm g}\) | covariant gauge-fixing parameter |
| \(J^\mu,\eta,\bar\eta\) | sources for \(A_\mu,\bar\psi,\psi\) in the generating functional |
| \(Z_\psi,Z_A\) | pole residues for spinor and photon representative fields |
| \(u^\sigma,v^\sigma\) | massive spinor intertwiners fixed in Chapter 16 |
| \(e_\mu^h\) | massless helicity-one polarization representative |
| \(\mathcal M\) | reduced scattering amplitude after removing the momentum-conservation delta function |

## Claims Established

- The QED interaction is the unique dimension-four local Abelian coupling of a
  charged Dirac representative to a Maxwell representative through the
  covariant derivative, under the stated field content and charge assignment.
- The gauge-fixed Abelian path integral has the photon and spinor propagators
  already derived in Chapters 18 and 16, together with a single cubic vertex
  \(-g\gamma^\mu\) in the present conventions.
- Local gauge-invariant observables have zero net local charge; charged
  representative fields are used in gauge-fixed Green functions, and genuinely
  charged insertions require dressing data.
- External electron, positron, and photon factors are pole residues supplied by
  LSZ, not independent diagrammatic definitions.
- In a hard tree-level process such as Compton scattering, replacing a photon
  polarization by a longitudinal representative gives zero after summing the
  two diagrams and using the external Dirac equations and momentum
  conservation.
- Ordinary fixed-photon-number charged S-matrix elements are a formal
  perturbative object in QED; the physical long-range theory requires
  infrared-inclusive observables or dressed asymptotic charged states.

## Figure Requirements

- A compact Feynman-rule display for the spinor propagator, photon propagator,
  and QED vertex.
- A Compton-scattering diagram with both tree-level channels, with momentum
  labels that match the analytic expression.
- A small conceptual diagram showing representative Green functions being
  projected by LSZ onto hard external data, with an infrared boundary marked.

## Exclusions

- No vacuum polarization calculation.
- No counterterm algebra or charge renormalization.
- No anomalous magnetic moment.
- No soft-photon exponentiation or Bloch--Nordsieck/Kulish--Faddeev
  construction beyond naming the boundary.
- No nonabelian ghosts or BRST cohomology.
