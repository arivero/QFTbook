# Volume I, Chapter 19 Dossier: Quantum Electrodynamics and External States

Status: revised and source-audited on 2026-05-22; formalized and
calculation-check companion added on 2026-05-27.

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
  - handwritten 253a trace pages
    `monograph/tex/build/source_visual_trace/253a_trace-216.png` through
    `253a_trace-223.png`;
  - `transcription/tex/253a/foundations.tex`, roughly lines 9114--9545;
  - `references/sound_references/buchholz_dybalski_scattering_2023.pdf`
    for the boundary between ordinary particle scattering and infraparticles;
  - `references/sound_references/rosten_exact_rg_1003.1366.pdf` for the
    distinction between manifestly gauge-invariant formulations and
    gauge-fixed representative correlators.

## External Reference Boundary

- The chapter derives the classical gauge covariance of the QED Lagrangian and
  the tree-level Ward cancellation directly.
- The 2026-05-27 formalization pass promotes the representative datum,
  local-neutrality criterion, Wilson-line dressing endpoint cancellation,
  gauge-fixed source functional, representative Feynman rules, LSZ external
  residue factors, tree Compton hard kernel, tree Ward identity, and infrared
  boundary of charged scattering into labeled definitions/propositions or a
  theorem with proof blocks.
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
- The covariant QED Faddeev--Popov determinant is treated as the Abelian
  specialization of the general local orbit-slice construction, with the
  nonabelian ghost and Gribov-local-chart issues deferred to the BRST chapter.
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
| \(F_\varphi[A]\) | covariant gauge condition \(\partial_\mu A^\mu-\varphi\) used for the QED Faddeev--Popov operator |
| \(\Delta_{\rm FP}^{U(1)}\) | Abelian Faddeev--Popov determinant after residual zero modes are removed |
| \(C_x,C_{y\to x}\) | dressing paths for charged Wilson-line insertions |
| \(Z_\psi,Z_A\) | pole residues for spinor and photon representative fields |
| \(u^\sigma,v^\sigma\) | massive spinor intertwiners fixed in Chapter 16 |
| \(e_\mu^h\) | massless helicity-one polarization representative |
| \(\not e^{\,h}\) | \(e_\mu^h\gamma^\mu\) |
| \(\mathcal M\) | reduced scattering amplitude after removing the momentum-conservation delta function |
| \(N(q),D(q)\) | tree-Compton shorthand \(N(q)=-\ii\not q+m\), \(D(q)=q^2+m^2-\ii\epsilon\) |

## Claims Established

- The QED interaction is the unique dimension-four local Abelian coupling of a
  charged Dirac representative to a Maxwell representative through the
  covariant derivative, under the stated field content and charge assignment.
- The gauge-fixed Abelian path integral has the photon and spinor propagators
  already derived in Chapters 18 and 16, together with a single cubic vertex
  \(-g\gamma^\mu\) in the present conventions.
- The QED Faddeev--Popov operator for
  \(F_\varphi[A]=\partial_\mu A^\mu-\varphi\) is
  \(\Box_x\delta^{(4)}(x-y)\), hence the determinant is a field-independent
  normalization constant after zero modes are separated; representing it by
  ghosts gives only a free decoupled ghost action.  The dossier explicitly
  cross-references the nonabelian construction in the BRST chapter.
- Local gauge-invariant observables have zero net local charge; charged
  representative fields are used in gauge-fixed Green functions, and charged
  insertions require dressing data such as Wilson lines with specified paths.
- External electron, positron, and photon factors are pole residues supplied by
  LSZ only in an infrared-regulated hard theory with isolated charged
  one-particle poles; in massless QED the charged spinor rows are hard-kernel
  data to be completed by inclusive probabilities or soft dressings.
- In a hard tree-level process such as Compton scattering, replacing a photon
  polarization by a longitudinal representative gives zero after summing the
  two diagrams and using the external Dirac equations and momentum
  conservation.
- Ordinary fixed-photon-number charged S-matrix elements are a formal
  perturbative object in QED; the physical long-range theory requires
  infrared-inclusive observables or dressed asymptotic charged states.
- Tree-level Compton scattering is presented as a Born hard kernel.  It is not
  claimed to be an exact fixed-photon-number electron \(S\)-matrix element of
  massless QED after removal of the infrared regulator.
- The companion script `calculation-checks/qed_external_state_checks.py`
  verifies the finite sign bookkeeping for charge neutrality, Abelian
  Wilson-line endpoint phases, Abelian Faddeev--Popov field independence, the
  tree-Compton longitudinal Ward cancellation, and the fixed-incoming-label
  cross-section summation convention.

## Figure Requirements

- A compact Feynman-rule display for the spinor propagator, photon propagator,
  and QED vertex.
- A compact external-factor diagram showing LSZ residues attached to
  amputated kernels.
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

## Audit Notes

- 2026-05-29 anti-wrapper pass: demoted the Abelian Faddeev--Popov
  specialization from proposition form to derivation prose.  The general
  orbit-measure construction remains the theorem-level input; the QED
  specialization is the direct calculation \(\mathcal M=\Box\) and field
  independence of \(\det{}'\Box\).
