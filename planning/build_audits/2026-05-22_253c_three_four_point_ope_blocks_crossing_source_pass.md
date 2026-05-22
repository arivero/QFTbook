# 253c Three-/Four-Point, OPE, Blocks, Crossing Source Pass

Date: 2026-05-22

Source checked:

- `references/253c 2023.pdf`, selected handwritten pages 62--89.
- Rendered source trace:
  `monograph/tex/build/source_visual_trace/253c_trace-062.png` through
  `monograph/tex/build/source_visual_trace/253c_trace-089.png`.

Manuscript files revised:

- `monograph/tex/volumes/volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`
- `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`

Coverage added or tightened:

- Scalar three-point function and non-scalar three-point tensor-structure
  decomposition with explicit finite structure label.
- Stress-tensor three-point discussion: parity-even \(D\ge4\) three-structure
  statement, Ward-fixed linear combination in terms of \(C_T\), and a redrawn
  small-sphere stress-tensor-flux figure.
- Scalar-scalar-stress-tensor three-point coefficient from the small-sphere
  dilatation Ward identity:
  \[
    C_{12T}= -\frac{D\Delta}{(D-1)A_{D-1}}\,N_{12}.
  \]
- Four-point conformal frame: two-plane reduction, residual fractional-linear
  map, complex cross ratio \(z=z_{12}z_{34}/(z_{13}z_{24})\), and
  \(u=z\bar z,\ v=(1-z)(1-\bar z)\).
- OPE as a cylinder Hilbert-space/state expansion, including the local-operator
  limit at the origin and the identical-scalar first descendant coefficient.
- Representation-theoretic OPE data and multiplicity: tensor structures as
  multiplicities, scalar-scalar exchange restricted to symmetric traceless
  tensors with multiplicity one.
- General scalar conformal-block decomposition with the inverse two-point
  pairing on degeneracy spaces.
- Redrawn OPE-channel tree figure and radial-cylinder figure for
  \(x_1=\rho,\ x_2=-\rho,\ x_3=-1,\ x_4=1\), with
  \(z=4\rho/(1+\rho)^2\).
- Descendant Gram matrix construction, reduced basis in the presence of nulls,
  radial block expansion, and Gegenbauer leading term.
- Identical-scalar crossing equation and the source's first approximate
  crossing/positivity consequence bounding the possible gap above the identity,
  stated explicitly as a controlled approximation rather than a theorem.

Verification:

- `tools/build_monograph.sh` completed successfully after the edits.
- The affected pages were rendered from `monograph/tex/main.pdf` and visually
  checked, including the new Ward-sphere, OPE-tree, and radial-cylinder
  figures.

Residual notes:

- The source pages 90--112 continue into projective-lightcone and more
  detailed bootstrap machinery.  Those remain deferred to the later dedicated
  CFT volume by the current architecture decision, rather than being expanded
  further in the core monograph.
