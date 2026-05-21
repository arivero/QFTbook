# 2026-05-21 Volume III Ward-Primary-Correlator Block

## Scope

Extended Volume III with the next conformal-field-theory block:

- conformal charges as stress-tensor surface operators and their Ward
  identities;
- primary operators at arbitrary points and finite conformal transformation
  laws;
- radial-quantization positivity, scalar and spin unitarity bounds, and short
  multiplets;
- one-, two-, three-, and four-point functions, inversion tensor structures,
  and conformal frames.

## Reader-Facing Inclusion

Added four chapters to `monograph/tex/volumes/volume_iii/volume_iii_current.tex`:

- `chapter05_conformal_charges_and_ward_identities.tex`
- `chapter06_primary_operators_and_finite_transformations.tex`
- `chapter07_unitarity_bounds_and_short_multiplets.tex`
- `chapter08_correlation_functions_and_conformal_frames.tex`

## Visual Audit

Rendered the new block from `monograph/tex/main.pdf` to PNG pages in
`/tmp/qft_cft_visual_audit`.  Reviewed the contact sheet
`/tmp/qft_cft_visual_audit/newblock_contact_sheet.png` and then inspected the
new figure pages individually.

The pass found one layout issue in the two-point/cylinder figure: the
cylinder-time arrow was too close to the radial-quantization label.  The
annotation was moved to the right side of the cylinder and the page was
re-rendered at `/tmp/qft_cft_visual_audit/fixed-275.png`.  The final figure
is legible and unclipped.

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

Continue Volume III with the operator product expansion, convergence in radial
quantization, conformal blocks, crossing symmetry, and the projective
lightcone formalism.
