# 253c Unitarity, BPZ, and Two-Point Source Pass

Date: 2026-05-22

Source block checked: `references/253c 2023.pdf`, pp. 48--61, rendered as
`monograph/tex/build/source_visual_trace/253c_trace-048.png` through
`monograph/tex/build/source_visual_trace/253c_trace-061.png`.

Manuscript files revised:

- `monograph/tex/volumes/volume_iii/chapter07_unitarity_bounds_and_short_multiplets.tex`
- `monograph/tex/volumes/volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`
- `planning/source_inventory/253a_253b_no_skip_coverage_register.md`

Content certified in this pass:

- Scalar unitarity-bound derivation now includes the explicit level-one
  \(\Delta_\phi=0\) branch, its null first descendants, and the assumptions
  under which this branch is the identity representation.
- Level-two scalar Gram matrix is followed by the explicit
  \(\delta^{\alpha\beta}\delta^{\mu\nu}\) contraction, matching the handwritten
  derivation of the \(\Delta_\phi=0\) or
  \(\Delta_\phi\ge (D-2)/2\) alternatives.
- Saturation of the scalar bound is stated as the null descendant
  \(\partial^2\phi=0\), i.e. the free massless scalar conformal multiplet.
- Rank-\(\ell\) symmetric-traceless primaries now explicitly record the
  divergence-channel origin of the spin bound
  \(\Delta\ge\ell+D-2\) and the conservation equation at saturation.
- Correlator constraints now begin with the precise global Ward-identity
  assumptions: separated Euclidean points, conformally invariant vacuum, and
  contact terms confined to coincident-point diagonals.
- The scalar two-point function derivation now includes the conformal map that
  fixes \(0\) and \(e_1\) while producing local scale factors
  \(\lambda\) and \(\lambda^{-1}\), forcing equality of dimensions for a
  nonzero coefficient.
- The radial/BPZ inner product is derived from the cylinder limits, and the
  two-point coefficient is identified with the BPZ/Hilbert inner product in a
  reflection-positive theory.
- General vector and rank-\(s\) symmetric-traceless two-point functions are
  included with the inversion tensor and the STT projector, followed by the
  stress-tensor two-point function and its \(C_T\) normalization statement.
- The flat-space-to-cylinder two-point figure was moved to the BPZ section and
  relabeled to show the BPZ-conjugate bra rather than an ordinary unexplained
  bra.

Verification:

- `tools/build_monograph.sh` completed successfully and reported a clean strict
  text audit.
- `git diff --check` passed.
- Rendered `main.pdf` physical pages 447--456 at 160 dpi and visually checked
  the affected unitarity-bound pages, BPZ/cylinder figure, spin-structure
  formulae, and stress-tensor two-point page.
