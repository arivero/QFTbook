# 253c Radial Quantization and State-Operator Source Pass

Date: 2026-05-22

## Source Scope

- Handwritten source: `references/253c 2023.pdf`, pages 19--28.
- Rendered source trace:
  - `monograph/tex/build/source_visual_trace/253c_trace-019.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-020.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-021.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-022.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-023.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-024.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-025.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-026.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-027.png`
  - `monograph/tex/build/source_visual_trace/253c_trace-028.png`

## Manuscript Changes

Updated:

- `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
- `monograph/tex/volumes/volume_iii/chapter06_primary_operators_and_finite_transformations.tex`

The revised radial-quantization chapter now includes:

- Lorentzian local operators as operator-valued distributions and the graded
  microcausality condition;
- Wightman, time-ordered, and Euclidean Schwinger functions with the
  imaginary-time ordering used in analytic continuation;
- a path-integral contour representation of Wightman, time-ordered, and
  Euclidean correlators;
- a remark recording the conformal fixed-point observable data and the
  quantum Yang--Mills scale/trace-anomaly distinction;
- the Weyl map from punctured \(\R^D\) to \(\R\times S^{D-1}\) with explicit
  assumptions about background metrics and renormalized operator bases;
- the primary scalar cylinder-operator map
  \(\widetilde{\mathcal O}(\tau,n)=e^{\Delta\tau}\mathcal O(e^\tau n)\);
- the correlation-function form of the state-operator map with an origin
  insertion preparing a cylinder state;
- a radial-generator convention in which
  \(\widehat H_{\rm cyl}=\widehat D_{\rm rad}\), so scaling dimensions are
  cylinder energies without an extra Euclidean factor of \(\ii\);
- the conformally coupled free scalar action on the cylinder, including the
  conformal mass \(m_{\rm cyl}^2=(D-2)^2/4\);
- the free scalar letter character
  \(f_\phi(q)=q^{(D-2)/2}(1-q^2)/(1-q)^D\);
- the bosonic symmetric-algebra operator partition function
  \(Z_{\rm op}^\phi(q)=\exp\{\sum_{m\ge1}f_\phi(q^m)/m\}\);
- the \(D=3\) one-particle check
  \(\sum_{\ell\ge0}(2\ell+1)e^{-\beta(\ell+1/2)}\).

The primary-operator chapter was aligned with the same radial-generator
convention:

- primary states now satisfy
  \(\widehat D_{\rm rad}\ket{\mathcal O_a}=\Delta\ket{\mathcal O_a}\);
- descendants correspond to derivatives without stray factors of \(\ii\);
- the special conformal parameter convention was made consistent with the
  finite transformation convention used earlier,
  \(\epsilon^\mu=c^\mu x^2-2(c\cdot x)x^\mu\).

## Figures Checked

- Figure 51.1: Wightman, time-ordered, and Euclidean complex-time contours.
  The first render had crowded headings; the title and vertical-axis label
  positions were separated and re-rendered.
- Figure 51.2: the Weyl map from radial slices to the Euclidean cylinder.
- Figure 51.3: local insertion at the origin mapped to a cylinder state.  The
  external-operator label was moved inside the flat-space panel.
- Figure 51.4: primary/descendant conformal multiplet figure remains legible
  after the generator-convention update.

## Verification

Ran:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
tools/audit_monograph_text.sh
git diff --check
tools/build_monograph.sh
pdftoppm -png -f 434 -l 436 -r 160 monograph/tex/main.pdf /tmp/qft_radial_polished
```

Results:

- strict monograph text audit clean;
- pdfLaTeX compile clean;
- XeLaTeX monograph harness clean:
  `Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf`;
- rendered visual spot-check clean for the new contour and state-operator
  figures;
- no handwritten PDF pages are embedded in the manuscript.
