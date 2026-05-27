# Issue #495 checkpoint: primitive Wightman domain theorem

## Scope

This pass responds to the directive that key domain theorems should be proved
inside the monograph, not left as literature imports.

## Manuscript changes

- Added to `monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`:
  - `thm:primitive-wightman-tube-domain`, proving the ordered Wightman
    spectral-support inclusion
    \[
      \operatorname{supp}\widehat w_\sigma\subset(\overline V_+)^{n-1}
    \]
    from intermediate spectral projections and the spectrum condition.
  - The Fourier--Laplace continuation and tempered tube-bound statement for
    ordered Wightman functions, using the finite-order Schwartz seminorm
    control of tempered distributions.
  - `thm:jost-edge-gluing-primitive-tubes`, proving Jost-edge equality from
    graded local commutativity and applying edge-of-the-wedge as the
    complex-analysis tool that generates the primitive BEG envelope.
  - `cor:primitive-domain-output-for-scattering`, explaining exactly what
    this primitive domain theorem supplies for connected four-point LSZ
    scattering amplitudes.
- Updated `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`
  so the Jin--Martin proof stack now records the primitive Wightman and
  Jost-edge steps as proved, while leaving the retarded-commutator/JLD,
  Lehmann--Martin fixed-\(t\), and LSZ-transfer steps as remaining theorem
  work.

## Planning updates

- Updated Volume II Chapter 6 dossier with the new symbols, theorem claims,
  boundaries, and audit note.
- Updated Volume II Chapter 7 dossier so issue #495's remaining work is
  accurately narrowed.

## Status

Issue #495 is not closed by this checkpoint.  The primitive tube-domain and
Jost-edge gluing theorems are now in the monograph.  Remaining closure work:

1. Prove the relevant Jost--Lehmann--Dyson representation for the retarded
   commutator matrix element.
2. Prove the Lehmann--Martin fixed-\(t\) enlargement needed for the cut
   \(s\)-plane at fixed \(t\).
3. Prove the LSZ transfer of that domain and the tempered cut-discontinuity
   bounds to the on-shell amplitude after stable-particle pole separation.

