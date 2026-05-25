# Issue #462 Audit: Dangerously Irrelevant Operators

## Scope

- GitHub issue: #462, "[Vol III] Dangerously irrelevant operators not
  mentioned."
- Manuscript loci:
  - `monograph/tex/volumes/volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`
  - `monograph/tex/volumes/volume_ii/chapter15_the_statistical_ising_model_and_universality.tex`
- Dossier loci:
  - `planning/chapter_dossiers/volume_ii/chapter15_wilson_fisher_fixed_point_scaling_operators.md`
  - `planning/chapter_dossiers/volume_ii/chapter16_statistical_ising_model_universality.md`

## Content Added

- Defined a dangerously irrelevant coordinate as an irrelevant RG coordinate
  together with an observable and a scaling sector whose observable scaling
  function is singular as the irrelevant scaling variable tends to zero.
- Derived the scalar/Ising \(D>4\) equation-of-state example:
  \(y_t=2\), \(y_h=(D+2)/2\), \(y_g=4-D<0\),
  \(h=tM+gM^3/6\), \(M^2=-6t/g\), and
  \({\mathcal M}(-1,0,w)\sim(6/w)^{1/2}\), giving
  \(\beta_{\rm mag}=1/2\), \(\delta=3\), and the failure of naive
  hyperscaling.
- Derived the \(D=4\) leading logarithms from the marginally irrelevant
  quartic flow:
  \(\dd x/\dd L=-3x^2+\cdots\) and
  \(\dd t/\dd L=(2-x+\cdots)t\), giving
  \[
    \xi\asymp |t|^{-1/2}(\log(1/|t|))^{1/6},
    \qquad
    M\asymp |t|^{1/2}(\log(1/|t|))^{1/3}.
  \]
- Added an Ising-chapter cross-reference separating Gaussian critical
  separated-point scaling limits in \(D\ge4\) from the quartic-dependent
  ordered equation of state.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 841 pages.
- Rendered and inspected affected manuscript pages:
  - Chapter 36 dangerous-irrelevance section, printed pages 473--475.
  - Chapter 37 Ising cross-reference, printed pages 483--484.
- No calculation-check scripts were edited for this issue, so no calculation
  scripts were rerun.
