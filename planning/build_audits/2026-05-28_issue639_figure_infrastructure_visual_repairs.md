# Issue #639 Figure Infrastructure And Named Visual Repairs

Date: 2026-05-28.

Scope of this checkpoint:

- Added `\listoffigures` to the monograph front matter.
- Added the project-wide figure policy in `planning/figure_style_guide.md`.
- Added the Figure Rule to `planning/12_strict_writing_harness.md`.
- Added `tools/audit_figures.py`, a local audit command for figure labels,
  body references, placement specifiers, and inline TikZ counts.
- Repaired the five named visual defects from GitHub issue #639:
  - Figure 12.1 OS reconstruction: moved the stray positivity sentence into
    the caption and added the Euclidean-axis convention in the surrounding
    text.
  - Figure 47.1 gauge fixing: put \(\phi\) and \(\phi^\xi\) on the same
    highlighted gauge orbit; added grayscale-readable dashed orbit encoding
    and marker-shape distinction.
  - Figure 46.3 lattice fermion doubling: distinguished the inequivalent
    Brillouin-torus doubler classes by marker shape and added local continuum
    cone glyphs.
  - Figure 49.1 QCD rules: replaced the cramped four-gluon label with a
    stable line break and explicit interaction label.
  - Figure 49.3 QCD constant-background extraction: split the infrared
    position-space box from the ultraviolet momentum tail and removed the
    previously undefined inward arrows.
- Added local `Figure~\ref{...}` callouts for the repaired named figures.
- Added a short List-of-Figures caption for the minimal-subtraction coordinate
  figure that otherwise caused an overfull List-of-Figures entry.

Verification performed:

```bash
tools/audit_figures.py
git diff --check
tools/audit_negative_scope_prose.py
tools/audit_theorem_form.py
tools/build_monograph.sh
```

The build completed with a clean final log scan:

```text
Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf
```

Targeted PDF visual inspection:

- Rendered PDF pages 231, 847, 852, 904, and 906 with `pdftoppm`.
- Inspected the rendered PNGs with the local image viewer.
- Rebuilt and re-rendered pages 847 and 906 after tightening residual label
  crowding.

Open remainder for issue #639:

```text
tools/audit_figures.py
  figure environments: 164
  figure labels: 164
  figure labels referenced from body text: 9
  unreferenced labeled figures: 155
  TikZ inside figures: 164
  TikZ outside figures: 85
```

Therefore issue #639 is not close-eligible after this checkpoint.  The next
stage is the monograph-wide body-callout pass, followed by a second visual
audit for color-only semantic encodings and axis-convention departures beyond
the named figures.
