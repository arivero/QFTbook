# 2026-05-21 Volume III OPE-Blocks-Lightcone Block

## Scope

Extended Volume III with the next CFT sequence:

- the operator product expansion as a radial-quantization expansion on a
  separating sphere;
- scalar-scalar OPE structure and conformally fixed descendant coefficients;
- conformal blocks as projections onto a primary multiplet;
- radial variables, reflection positivity, crossing equations, and bootstrap
  linear functionals;
- projective lightcone formalism and conformal Casimir equations.

## Reader-Facing Inclusion

Added three chapters to `monograph/tex/volumes/volume_iii/volume_iii_current.tex`:

- `chapter09_operator_product_expansion.tex`
- `chapter10_conformal_blocks_crossing_and_bootstrap.tex`
- `chapter11_projective_lightcone_and_casimir_equations.tex`

## Visual Audit

Rendered the new pages from `monograph/tex/main.pdf` to PNG pages in
`/tmp/qft_cft_ope_visual_audit`.  Reviewed the contact sheet
`/tmp/qft_cft_ope_visual_audit/contact_sheet.png` and inspected the OPE,
conformal-block, crossing, and projective-lightcone figure pages.

The pass found one layout collision in Figure 9.1: the outside-insertion
annotation overlapped the separating sphere.  The label was moved below the
left diagram and re-rendered at `/tmp/qft_cft_ope_visual_audit/fixed-279.png`.
The final figure is legible and unclipped.

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

Continue Volume III with the survey of conformal field theories, then the
two-dimensional CFT sequence: stress tensor, Virasoro algebra, Ward identities,
radial quantization on the circle, and modular structure.
