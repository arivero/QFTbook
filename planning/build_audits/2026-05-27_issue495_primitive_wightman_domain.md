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
  - `def:dyson-regular-causal-commutator`, separating the six-dimensional
    Dyson lift from the invalid shorthand of multiplying an arbitrary
    Wightman distribution by a light-cone delta.
  - `thm:dyson-causal-commutator-representation`, proving the
    Dyson/Jost--Lehmann representation for a Dyson-regular causal commutator
    distribution whose Fourier transform vanishes in a coincidence slab.
  - `prop:source-current-commutator-coincidence-region`, deriving the
    coincidence regions for LSZ source-current commutator matrix elements
    directly from translation covariance and the joint spectral theorem.  The
    wave-packet theorem uses spectral matrix distributions on
    \(B_f\times\operatorname{Spec}(P)\times B_i\), with the generalized
    sharp-momentum shorthand giving the familiar supports
    \(\Sigma_{bc}^{fi}-K\) and \(K-\Sigma_{cb}^{fi}\).
  - `prop:dyson-light-cone-lift-microlocal-criterion`, isolating the
    microlocal status of Dyson's light-cone lift.  It proves that the ordinary
    product \(\pi^*C\delta(x_D^2-|y|^2)\) is defined away from the vertex
    under the explicit transversality condition
    \(\operatorname{WF}(C)\cap\mathcal N_{\rm lc}=\varnothing\), and proves
    that different extensions differ by finite contact polynomials after
    Fourier transform.
  - `def:dyson-regular-modulo-contact` and
    `thm:punctured-dyson-lift-finite-scaling-degree`, proving the local
    finite-scaling-degree extension mechanism for the punctured Dyson lift.
    The theorem explicitly requires the cone equation
    \((x_D^2-|y|^2)U=0\), \(O(2)\)-invariance, temperedness, and
    \(y\)-pushforward normalization modulo \(x=0\) contact terms; it proves
    that the Fourier transform solves the six-dimensional wave equation and
    that all extension ambiguity restricts to a polynomial in \(q\).
  - `def:local-scaling-degree` and
    `prop:source-current-differentials-preserve-punctured-input`, proving
    that replacing interpolating fields by LSZ source currents is a
    finite-order relative-coordinate differential operation
    \(\mathcal K_b(2\partial_x)\mathcal K_c(-2\partial_x)\).  The proposition
    proves preservation of causal support, punctured light-cone wavefront
    avoidance, finite scaling degree, and finite scaling degree of the
    punctured six-dimensional Dyson product.
  - `cor:jld-input-for-lsz-retarded-commutator`, applying the representation
    to LSZ source-current commutators and separating finite contact
    polynomials.
- Updated `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`
  so the Jin--Martin proof stack now records the primitive Wightman and
  Jost-edge steps as proved, and records the causal-commutator/JLD theorem as
  proved under the explicit Dyson-regularity hypothesis.  The
  Dyson-regularity verification for the relevant LSZ source-current matrix
  coefficients, the Bros--Epstein--Glaser Lehmann--Martin fixed-\(t\)
  completion, and the verification of the off-shell normal-coordinate
  hypotheses needed for LSZ transfer remain theorem work.
  - `thm:lsz-transfer-fixed-t-domain`, proving the analytic LSZ transfer
    itself: if the BEG/JLD construction supplies an off-shell fixed-\(t\)
    holomorphic domain with normal-crossing external one-particle poles and
    uniform polynomial boundary growth, then the LSZ-amputated on-shell
    amplitude is holomorphic on the fixed-\(t\) domain and inherits tempered
    cut discontinuities.
  - `thm:fixed-t-finite-subtraction-cauchy`, proving the one-variable
    finite-subtraction Cauchy formula in a fixed-\(t\) cut plane from a
    meromorphic first-sheet domain, explicit stable-particle poles, tempered
    discontinuities on the two cuts, and a polynomial large-contour bound.
  - `def:admissible-fixed-t-two-cut-exhaustion`, defining the contour
    exhaustions used in the finite-subtraction theorem.  The definition now
    specifies the large circular part, right and left lips, endpoint and
    large-end connector arcs, orientations, exhaustion property, and length
    estimates needed to justify dropping the large arcs while keeping
    threshold endpoint contributions inside the cut distributions.

## Planning updates

- Updated Volume II Chapter 6 dossier with the new symbols, theorem claims,
  boundaries, and audit note.
- Updated Volume II Chapter 7 dossier so issue #495's remaining work is
  accurately narrowed.

## Status

Issue #495 is not closed by this checkpoint.  The primitive tube-domain and
Jost-edge gluing theorems are now in the monograph.  The
source-current coincidence-region support statement is now proved from the
spectral theorem.  The causal-commutator Dyson/JLD theorem is now proved for
the mathematically defined class of Dyson-regular causal commutators, with the
light-cone lift regularity no longer hidden in notation.  The microlocal
criterion now explains exactly where the naive light-cone product is valid
and where renormalized lift data must be supplied.  The finite-scaling-degree
extension theorem now makes the local extension/contact-polynomial mechanism
explicit, including the cone equation and pushforward normalization that a
physical source-current kernel must satisfy.  The source-current differential
pass proves that the LSZ replacement \(J=\mathcal K\Phi\) itself preserves the
punctured wavefront and scaling inputs; the remaining regularity issue is
therefore not a hidden derivative problem.  The fixed-\(t\) Cauchy theorem
now also has an explicit admissible two-cut contour class, so its
large-contour and threshold-endpoint limits are no longer hidden in the
word ``admissible.''  Remaining closure work:

1. Prove Dyson regularity for the LSZ source-current matrix coefficients used
   in the massive scattering application.  The new microlocal proposition
   supplies a sufficient wavefront transversality criterion and the contact
   ambiguity analysis, and the extension theorem supplies the local
   finite-scaling-degree mechanism.  The source-current differential
   proposition proves stability under the LSZ differential operators.  The
   actual source-current kernels still require a theorem proving the needed
   wavefront/scaling behavior for the underlying field commutators together
   with the cone equation, pushforward normalization, temperedness, and
   Cauchy-data trace hypotheses for the six-dimensional lift, or a different
   construction of that lift.
2. Prove the Bros--Epstein--Glaser/Lehmann--Martin fixed-\(t\) enlargement
   needed for the cut
   \(s\)-plane at fixed \(t\), including the off-shell normal-coordinate
   control needed to apply `thm:lsz-transfer-fixed-t-domain`, and the
   pointwise large-contour polynomial estimate needed to apply
   `thm:fixed-t-finite-subtraction-cauchy`.
