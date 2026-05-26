# Issue #548 SU(2) Seiberg-Witten Periods And BPS Spectrum

## Scope

- GitHub issue: `#548`.
- Manuscript locus:
  `monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`.
- Calculation-check locus:
  `calculation-checks/sw_su2_periods.py`.

## Content Added

- Replaced the asserted pure \(SU(2)\) curve with the constraint derivation:
  one-loop prepotential gives the infinity monodromy, residual \(R\)-symmetry
  gives paired finite singularities, Picard-Lefschetz transformations give the
  monopole and dyon monodromies, and the minimal genus-one curve with finite
  discriminant \(u^2-\Lambda^4\) is
  \(y^2=(x^2-\Lambda^4)(x-u)\).
- Added the explicit charge-monodromy formula
  \[
    M_\gamma =
    \begin{pmatrix}
      1+2n_mn_e & 2n_e^2\\
      -2n_m^2 & 1-2n_mn_e
    \end{pmatrix}.
  \]
- Added hypergeometric period representatives for \(a(u)\) and the local
  monopole-vanishing period \(a_D^{(m)}(u)\), together with the Picard-Fuchs
  equation.
- Computed the monopole mass near \(u=\Lambda^2\) and recorded the dyonic
  vanishing central charge \(a_D-a\) near \(u=-\Lambda^2\).
- Added the weak-coupling BPS tower, the strong-coupling chamber, and the
  marginal-stability wall condition.
- Updated the calculation-check index and chapter dossier.

## Verification

- `python3 calculation-checks/sw_su2_periods.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed.
- Independent log scan passed:
  `rg -n "LaTeX Warning: Reference|LaTeX Warning: Citation|Latex failed to resolve|Undefined control sequence|Overfull|Underfull|Fatal error|Emergency stop|Missing .* inserted|Token not allowed" monograph/tex/main.log monograph/tex/build/latexmk.out`
  returned no matches.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1442`.
