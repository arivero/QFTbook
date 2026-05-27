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
  - `thm:dyson-causal-commutator-representation`, proving the
    Dyson/Jost--Lehmann representation for a causal commutator distribution
    whose Fourier transform vanishes in a coincidence slab.
  - `cor:jld-input-for-lsz-retarded-commutator`, applying the representation
    to LSZ source-current commutators and separating finite contact
    polynomials.
- Updated `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`
  so the Jin--Martin proof stack now records the primitive Wightman,
  Jost-edge, and causal-commutator/JLD steps as proved, while leaving the
  Bros--Epstein--Glaser Lehmann--Martin fixed-\(t\) completion and
  LSZ-transfer steps as remaining theorem work.

## Planning updates

- Updated Volume II Chapter 6 dossier with the new symbols, theorem claims,
  boundaries, and audit note.
- Updated Volume II Chapter 7 dossier so issue #495's remaining work is
  accurately narrowed.

## Status

Issue #495 is not closed by this checkpoint.  The primitive tube-domain,
Jost-edge gluing, and causal-commutator Dyson/JLD theorems are now in the
monograph.  Remaining closure work:

1. Prove the Bros--Epstein--Glaser/Lehmann--Martin fixed-\(t\) enlargement
   needed for the cut
   \(s\)-plane at fixed \(t\).
2. Prove the LSZ transfer of that domain and the tempered cut-discontinuity
   bounds to the on-shell amplitude after stable-particle pole separation.
