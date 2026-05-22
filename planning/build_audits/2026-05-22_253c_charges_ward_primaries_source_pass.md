# 253c Charges, Ward Identities, Primaries Source Pass

Date: 2026-05-22

Source block checked: `references/253c 2023.pdf`, pp. 29--48, rendered as
`monograph/tex/build/source_visual_trace/253c_trace-029.png` through
`monograph/tex/build/source_visual_trace/253c_trace-048.png`.

Manuscript files revised:

- `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
- `monograph/tex/volumes/volume_iii/chapter05_conformal_charges_and_ward_identities.tex`
- `monograph/tex/volumes/volume_iii/chapter06_primary_operators_and_finite_transformations.tex`
- `monograph/tex/volumes/volume_iii/chapter07_unitarity_bounds_and_short_multiplets.tex`
- `planning/source_inventory/253a_253b_no_skip_coverage_register.md`

Content certified in this pass:

- Lorentzian charge commutator represented by slices immediately before and
  after an insertion, with a redrawn TeX figure showing the Euclidean closed
  surface after continuation.
- Euclidean Ward-identity derivation by deforming a large enclosing surface to
  small enclosing spheres around insertions, with an explicit surface
  decomposition formula.
- Conformal charge on the cylinder, including explicit vector fields for
  \(D_{\rm rad}\), \(P_\mu\), and \(K_\mu\), inversion exchanging \(P_\mu\)
  and \(K_\mu\), and the stress-tensor expression for the cylinder Hamiltonian.
- Hermitian spin-matrix convention for primary operators, the primary state
  conditions, the construction of descendants, and the stated assumptions under
  which the local operator space decomposes into primary modules.
- Source-faithful infinitesimal transformations of primary operators, including
  the \(\ii\)-weighted spin terms and the finite tensor transformation formulae
  for covariant and contravariant rank-\(s\) primaries.
- Opening unitarity consequence from \(P_\mu^\dagger=K_\mu\): the
  first-descendant Gram matrix is positive semidefinite.

Verification:

- `tools/build_monograph.sh` completed successfully and reported a clean strict
  text audit.
- `git diff --check` passed.
- Rendered `main.pdf` pages 441--449 at 160 dpi and visually checked the new
  Ward-surface figures and the affected formula pages.
