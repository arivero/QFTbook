# Figure Style Guide

Figures in the monograph are mathematical content.  A figure is retained only
when it carries information used by the surrounding argument, construction, or
example.

## Textual Anchoring

Every floated figure must be referenced from the surrounding text with a
`Figure~\ref{fig:...}` callout.  The callout should state the mathematical role
of the figure: the construction it fixes, the comparison it displays, the
convention it records, or the calculation it organizes.  A figure whose only
role is decorative should be removed.

Inline `tikzpicture` diagrams are allowed only when they function as notation:
small Feynman-rule glyphs, local operator-product schematics, or one-line
commutative diagrams placed next to the formula they abbreviate.  A nontrivial
diagram with a caption-worthy claim belongs in a `figure` environment with a
label and a textual callout.

## Grayscale-Readable Encoding

Color may emphasize information but must not be the only carrier of a semantic
distinction.  Distinct mathematical objects in a figure should also differ by
one of:

- line style: solid, dashed, dotted, densely dashed;
- line weight;
- marker shape: filled circle, open circle, square, triangle, cross;
- direct labels placed next to the relevant object.

Recurring conventions:

- matter or scalar propagation: solid line;
- gauge-field propagation: wavy line;
- ghost propagation: dashed line with ghost-number arrow;
- gauge orbits: dashed or solid blue-toned curves, with textual labels;
- gauge slices or constraints: heavier solid curves, with textual labels;
- auxiliary or reference structures: dotted or faint lines;
- excluded or absent vertices: crossed out with a line and an explanatory
  local label.

## Axis Conventions

The default Lorentzian spacetime drawing convention is time vertical and space
horizontal.  A chapter may use another convention when the construction makes
that more natural: for example OS reflection may draw Euclidean reflection
time \(\tau\) horizontally, and finite-temperature Euclidean figures may draw
the thermal circle horizontally.  Any departure from the default must be
announced in the local text or conventions block before the figure is used.

All axis labels must state the coordinate actually drawn.  Avoid unlabeled
spacetime axes, and avoid changing conventions within a chapter without an
explicit local reason.

## Placement

Use `[!htbp]` or `[!tbp]` for ordinary floated figures.  Use `[H]` only when
exact placement is mathematically part of the local reading order, such as a
figure sitting between a definition and the formula it explains.  If a chapter
uses many `[H]` figures, the author should re-check whether the figures are
serving local derivations or whether ordinary float placement would improve
typography.

## Audit Command

The repository audit command

```bash
tools/audit_figures.py
```

reports figure labels, body references, unreferenced figures, placement
specifiers, and inline TikZ counts.  The strict mode

```bash
tools/audit_figures.py --strict
```

fails when a floated figure label has no body reference.
