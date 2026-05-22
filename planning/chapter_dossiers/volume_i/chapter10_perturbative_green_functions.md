# Volume I, Chapter 10 Dossier: Perturbative Green Functions

## Source Placement

- Follows the Kallen-Lehmann spectral representation and its particle-content
  interpretation.
- Covers the perturbative computation of Green functions in scalar
  \(\phi^4\) theory, before any definition of scattering states or the
  S-matrix.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 3905--4383;
  - `references/253a_notes.tex`, corresponding non-authoritative comparison
    around the scalar perturbation chapter.
- Source/figure certification:
  - handwritten pp. 100--109 were checked against the compiled manuscript on
    2026-05-22;
  - audit file:
    `planning/build_audits/2026-05-22_perturbative_green_functions_source_figures.md`.

## External Reference Boundary

- Fredenhagen--Rejzner, "Perturbative algebraic quantum field theory",
  arXiv:1208.1428:
  - used as a rigor lens for formal power series, time-ordered products, local
    functionals, and renormalization as extension/ambiguity of products of
    distributions;
  - not used as the foundation or ordering principle of the chapter.
- Rosten, "Fundamentals of the Exact Renormalization Group", arXiv:1003.1366:
  - used only to check terminology around bare actions, cutoffs, Wilsonian
    effective actions, and scale dependence;
  - full Wilsonian RG is reserved for a later volume.

## Framework

- Euclidean scalar field with an explicit regulator or formal perturbative
  status.
- The formal field variable \(\phi\) is integrated with a regulated Gaussian
  measure or treated as a perturbative symbol.
- Correlation functions are normalized Schwinger functions, not scattering
  amplitudes.
- Connected functions are obtained either by cancellation of vacuum components
  in normalized correlators or by the logarithm of the source functional.
- The chapter may also state Lorentzian time-ordered Green-function rules as
  analytic continuations of Green functions, still before scattering.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(D\) | Euclidean spacetime dimension |
| \(x\in\mathbb R^D\) | Euclidean point |
| \(k\in\mathbb R^D\) | Euclidean momentum |
| \(\phi\) | real scalar field variable |
| \(m\) | mass parameter in the quadratic part of the regulated action |
| \(g\) | quartic coupling |
| \(\mathcal L\) | Lorentzian scalar \(\phi^4\) density used only to identify the model |
| \(\mathcal L_E\) | Euclidean scalar \(\phi^4\) density used for Schwinger functions |
| \(S_E=S_{0,E}+S_{\mathrm{int},E}\) | Euclidean action |
| \([\dd\phi]_\Lambda\) | regulated finite-mode integration symbol |
| \(C_\Lambda(k)\) | regulated free propagator |
| \(Z_\Lambda[J]\) | regulated source functional |
| \(W_\Lambda[J]\) | logarithm of \(Z_\Lambda[J]\) |
| \(G_{E,n}\) | normalized Euclidean \(n\)-point function |
| \(G^{\mathrm{conn}}_{E,n}\) | connected Euclidean \(n\)-point function |
| \(\Gamma\) | graph with labelled external legs |
| \(\operatorname{Aut}\Gamma\) | automorphism group fixing external labels |
| \(\Sigma_E(k)\) | Euclidean self-energy defined by \(G_E(k)=(k^2+m^2-\Sigma_E(k))^{-1}\) |
| \(C_1(\Lambda,m)\) | cutoff tadpole integral including the factor \(1/2\) |
| \(m_*\) | spectral pole mass identified from the two-point function |
| \(m_R\) | renormalized mass parameter chosen by a prescription |
| \(\delta m^2\) | mass counterterm |

## Claims To Establish

- Expanding a regulated normalized Euclidean path integral gives a formal
  power series in \(g\).
- Wick's theorem converts Gaussian moments into sums over pairings.
- Vacuum components cancel in normalized correlators, leaving components
  attached to external fields.
- The logarithm of the source functional generates connected functions.
- For \(\phi^4\), each vertex has valence four; the graph weight can be stated
  using vertex factor \(-g\), propagators, loop integrations, momentum
  conservation, and a symmetry factor.
- The unlabelled action-expansion vertex \(-g/4!\) and the labelled-leg rule
  \(-g\) are the same convention after Wick-contraction multiplicities are
  counted.
- The tadpole and sunset coefficients are explicitly
  \(4\cdot3!/2(-g/4!)=-g/2\) and
  \(\frac1{2!}(2\cdot4^2\cdot3!)(-g/4!)^2=g^2/6\).
- The two-point function admits a Dyson form once the self-energy is defined as
  the sum of amputated 1PI two-point insertions.
- At order \(g\), the tadpole contribution is
  \[
    \Sigma_E^{(1)}(k)
    =
    -{g\over2}
    \int {d^Dq\over(2\pi)^D}{1\over q^2+m^2}
  \]
  before regularization.
- With a momentum cutoff \(\Lambda\), the tadpole integral diverges as
  \(\log(\Lambda/m)\) in \(D=2\) and as a power \(\Lambda^{D-2}\) in \(D\ge3\).
- A mass counterterm reorganizes perturbation theory so that the pole mass can
  be fixed order by order.
- The leading connected four-point Green function is
  \[
    (2\pi)^D\delta^D\!\left(\sum_i k_i\right)
    \left[-g\prod_i{1\over k_i^2+m^2}+O(g^2)\right].
  \]

## Figure Requirements

- Diagram of normalized correlator components attached to external fields.
- Diagrammatic two-point expansion with bare propagator, tadpole, sunset, and
  higher terms.
- 1PI self-energy diagram row.
- Euclidean Feynman rules for propagator and quartic vertex.
- Tadpole and sunset diagrams with loop momenta.
- Four-point connected decomposition.

## Exclusions

- No S-matrix graph interpretation.
- No LSZ formula.
- No on-shell external particle amplitudes.
- No statement that the formal path integral is an actual measure without a
  regulator or constructive theorem.
- No broad Wilsonian RG treatment beyond the local counterterm bookkeeping
  needed for the pole-mass discussion.
