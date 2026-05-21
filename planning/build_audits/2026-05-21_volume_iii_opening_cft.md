# 2026-05-21 Volume III Opening CFT Block

## Scope

Created the compiled opening block of Volume III:

- fixed points, conformal local data, Ising universality, and the trace
  equation at a fixed point;
- conformal Killing vectors, finite conformal transformations, inversion,
  special conformal transformations, the conformal algebra, and the
  two-dimensional local enhancement;
- stress tensor from background metric variation, Weyl transformations,
  improvement, the conformally coupled free scalar, and stress-tensor Ward
  identities;
- radial quantization, the Weyl map to the cylinder, state-operator
  correspondence, primary/descendant states, reflection positivity, and the
  free scalar spectrum check.

## Reader-Facing Inclusion

Added `volume_iii_current.tex` and included it from `main.tex` after Volume II.

## Visual Audit

Rendered the new Volume III opening pages to PNG and reviewed the contact
sheet at:

`monograph/tex/build/visual_audit_vol3_opening/contact-vol3.png`

The newly introduced figures render legibly without clipping or layout
collisions.

## Verification

Ran:

```bash
tools/build_monograph.sh
```

Result:

- strict monograph text audit clean;
- cross-references resolved after the latexmk rerun;
- final LaTeX log scan clean;
- compiled PDF produced at `monograph/tex/main.pdf`.

## Next Local Target

Continue Volume III with conformal charges acting on local operators,
primary transformation laws at arbitrary points, two- and three-point
functions, unitarity bounds, and the operator product expansion.
