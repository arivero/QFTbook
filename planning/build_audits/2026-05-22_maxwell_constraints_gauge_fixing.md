# Maxwell Constraints and Gauge-Fixing Audit

Date: 2026-05-22

## Scope

- Rewrote
  `monograph/tex/volumes/volume_i/chapter18_maxwell_theory_constraints_and_gauge_fixing.tex`
  as a source-order development of the 253a Maxwell block.
- Kept Feynman diagrams for representative Green functions within the
  gauge-fixed Green-function framework; no perturbative S-matrix material is
  introduced in this chapter.

## Source Visual Checks

- Handwritten QFT source images:
  `monograph/tex/build/source_visual_trace/253a_trace-197.png` through
  `monograph/tex/build/source_visual_trace/253a_trace-215.png`.
- Source content checked against `transcription/tex/253a/foundations.tex`,
  roughly lines 8366--9110.
- The checked handwritten block covers the Maxwell action, canonical
  constraints, axial gauge, gauge-slice path integral, finite-dimensional
  Faddeev--Popov model, axial propagator, Lorenz/covariant gauges,
  field-strength one-photon matrix elements, polarization completeness, and
  the comparison with the free field-strength Wightman function.

## Manuscript Rendering

- Rendered manuscript pages:
  `monograph/tex/build/visual_audit_maxwell_20260522b/maxwell-306.png`
  through `maxwell-313.png`.
- The gauge-slice figure on the page rendered as `maxwell-309.png` was
  adjusted after visual review to separate the orbit and transformation
  labels and to add white label backgrounds.
- A post-patch single-page render was produced for the repaired figure:
  `monograph/tex/build/visual_audit_maxwell_20260522c/maxwell-309.png`.

## Content Added Or Tightened

- Defined the local representative field \(A_\mu\), its gauge equivalence
  relation, the boundary-condition assumptions used for integrations by parts,
  and the separate treatment of zero modes.
- Derived the Maxwell Euler--Lagrange equation, canonical momenta, primary
  constraint, Gauss-law secondary constraint, canonical Hamiltonian, and
  first-class constraint algebra.
- Built the correct gauge generator
  \(G[\zeta]=\int[(\partial_0\zeta)\Pi^0-\zeta\partial_i\Pi^i]\) and checked
  that it gives \(\delta A_\mu=\partial_\mu\zeta\).
- Developed axial gauge both canonically and in the gauge-fixed Lagrangian,
  including the second-class pair for nonzero \(k_3\) modes and the remaining
  canonical variables \(A_a,\Pi^a\), \(a=1,2\).
- Stated the Faddeev--Popov identity with
  \(M_{\mathcal G}[A]\xi=\frac{d}{ds}\mathcal G(A+s\partial\xi)|_{s=0}\),
  emphasizing that the field-independent determinant is special to abelian
  linear gauges.
- Added the finite-dimensional \((x,y)\) gauge-slice model and showed the
  explicit cancellation of the Faddeev--Popov factor against the slice
  Jacobian in gauge-invariant expectation values.
- Derived the axial-gauge \(3\times3\) quadratic block, its inverse, and the
  singularity at residual \(k_3=0\) modes.
- Derived the gauge-independent field-strength correlator by
  antisymmetrizing momentum factors.
- Derived the Lorenz-gauge Faddeev--Popov operator, Gaussian gauge averaging,
  covariant quadratic operator, its inverse, and the photon representative
  propagator.
- Added the one-photon field-strength spectral form, polarization
  completeness with a null covector \(C_\mu(k)\), and the free normalization
  \(Z_A=1\).

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

The build completed cleanly and produced `monograph/tex/main.pdf`. The strict
monograph text audit run by the build script was clean.
