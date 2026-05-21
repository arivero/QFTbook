# 2026-05-21 Volume III Virasoro-Modular Block

## Scope

Extended Volume III with the next conformal-field-theory sequence:

- a working landscape of conformal field theories by spacetime dimension;
- two-dimensional conformal symmetry in complex coordinates;
- chiral and antichiral stress tensors, Virasoro modes, and the Virasoro
  algebra from stress-tensor OPEs;
- plane-cylinder transformation and the central-charge shift of the cylinder
  Hamiltonian;
- highest-weight Virasoro modules, null vectors, unitary minimal models, and
  BPZ differential equations;
- torus partition functions, modular transformations, chiral characters, and
  the two-dimensional Weyl anomaly.

## Reader-Facing Inclusion

Added four chapters to `monograph/tex/volumes/volume_iii/volume_iii_current.tex`:

- `chapter12_landscape_of_conformal_field_theories.tex`
- `chapter13_two_dimensional_conformal_symmetry_and_virasoro.tex`
- `chapter14_virasoro_representations_minimal_models_and_bpz.tex`
- `chapter15_modular_invariance_and_weyl_anomaly.tex`

## Visual Audit

Rendered the updated PDF pages 287--303 to PNG pages in
`/tmp/qft_cft_2d_visual_audit_final` and reviewed the contact sheet
`/tmp/qft_cft_2d_visual_audit_final/contact.png`.  Inspected the figure pages
for the Virasoro contour deformation, stress-tensor double contour, unitary
Virasoro representation branches, BPZ contour motion, torus modular cycles, and
local Weyl-chart reduction.

The figures are legible, unclipped, and correctly placed in the final PDF.  A
conceptual prose pass also replaced a negative formulation of the classification
status of higher-dimensional CFTs with a direct statement of the open
classification problem.

## Verification

Ran:

```bash
tools/build_monograph.sh
```

Result:

- strict monograph text audit clean;
- cross-references resolved by latexmk;
- final LaTeX log scan clean;
- compiled PDF produced at `monograph/tex/main.pdf`.

## Next Local Target

Continue Volume III with supersymmetric conformal field theories and the
four-dimensional \(\mathcal N=4\) super-Yang--Mills block, while keeping the
two-dimensional Virasoro and modular material available as the comparison
point for local versus global conformal data.
