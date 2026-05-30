# 2026-05-30 Figure Semantic Audit, Round 2

## Scope

- Audited the full floated-figure ledger of the compiled monograph:
  172 `figure` environments.
- Built a label/page ledger from the LaTeX sources and the compiled auxiliary
  data, then inspected rendered contact sheets using the printed-page to PDF
  page offset.  The generated temporary ledger and contact sheets live under
  `tmp/figure_audit_2026-05-30/` and are not repository artifacts.
- Source inspection was used as the decisive check whenever a rendered contact
  sheet could not isolate the figure from surrounding text.

## Repairs Made

1. `fig:aqft-local-net` now displays the actual isotone local-net assignment:
   nested regions, the morphism
   \(\iota_{\mathcal O_1\mathcal O_2}:\Obs(\mathcal O_1)\to
   \Obs(\mathcal O_2)\), and the commutation relation for spacelike separated
   algebras.  The previous arrow from the larger region directly to
   \(\Obs(\mathcal O_1)\) was not faithful to the construction.
2. `fig:gns-representation` now shows the null left ideal
   \(\mathcal N_\omega\), quotient pre-Hilbert space, inner product,
   completion, cyclic vector, left-multiplication representation, and
   represented local von Neumann algebras.  The previous state-to-GNS box hid
   the actual construction.
3. `fig:qcd-dis-ope-light-ray-factorization` now labels the gauge transporter
   as the open Wilson segment \(W[\lambda n,0]\), not \(W_\square\).  The
   caption explicitly says that the segment connects the colored fields in
   the bilocal PDF operator.
4. `fig:extended-defect-basic-operations` now marks a defect-local insertion
   \(\widehat{\mathcal O}_\alpha(y)\) on the support \(\Sigma\), matching the
   surrounding text and caption.
5. `fig:kubo-order-of-limits` now has a body callout tied to the
   distributional decomposition
   \(\operatorname{Re}\sigma=\pi D\delta+\sigma^{\rm reg}\).  The caption and
   preceding paragraph now state the positive content: the Drude sector is a
   singular summand and the finite dc coefficient is extracted from the
   locally integrable regular part.

## Figures Rechecked In This Pass

- Foundational construction diagrams: Wightman reconstruction, Wightman tube
  analyticity, OS reflection positivity, AQFT local nets, GNS, Reeh--Schlieder,
  DHR localization, split inclusions, wedge modular flow, and Haag--Ruelle
  spectral transfer.
- Perturbative and renormalization diagrams: Wick topologies, Feynman rules,
  counterterm and forest diagrams, Wilsonian shell integration, Polchinski
  flow, BPHZ/Wilsonian low-1PI bridge, stress-trace diagrams, and
  Wilson--Fisher/Ising RG figures.
- Gauge and QCD diagrams: Yang--Mills index/curvature data, BEH and monopole
  figures, lattice gauge and fermion figures, Faddeev--Popov/Gribov/BV
  diagrams, QCD background-field, Wilson-line, large-\(N\), QCD-string,
  baryonic-junction, DIS, jets, and anomaly figures.
- CFT diagrams: conformal Killing charge geometry, inversion, Weyl
  improvement, radial quantization, local-operator density, Ward surfaces,
  conformal frames, OPE trees, and \(\rho\)-coordinate convergence.
- Later-volume diagrams: bordism gluing, Frobenius generators, finite-gauge
  gluing spans, line-charge lattices, defect operations, anomaly inflow,
  thermal/KMS figures, Schwinger--Keldysh and Kubo figures, lattice-fermion
  reflection, and eta-invariant mapping-torus geometry.

## Pass Criteria

A figure passes this audit only if its drawn objects encode the mathematical
objects named in the surrounding callout and caption, the semantic
distinctions are not carried by color alone, and the diagram adds information
that the surrounding derivation actually uses.
