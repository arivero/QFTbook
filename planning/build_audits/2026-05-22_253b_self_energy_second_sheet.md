# 2026-05-22 253b Self-Energy and Second-Sheet Audit

## Source Block

- Handwritten source: `references/253b lecture notes 2023.pdf`, pp. 19--26.
- Rendered trace checked:
  - `monograph/tex/build/source_visual_trace/253b_trace-019.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-020.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-021.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-022.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-023.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-024.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-025.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-026.png`
- Monograph home:
  - `monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex`

## Verification Notes

- The resonance continuation from the one-dimensional model now includes both
  the \(k\)-plane picture and an explicit \(E\)-plane sheet picture.
- The dressed propagator section matches the source convention
  \(D_2(k)=-i/(k^2+m_{2,\mathrm{bare}}^2-i0-\Sigma(k))\) and includes the
  1PI Dyson series.
- The one-loop \(\phi_1\) bubble records the symmetry factor, Feynman
  parameter, shifted loop momentum, and loop-energy Wick-rotation contour.
- The Euclidean cutoff computation and mass counterterm subtraction reproduce
  the source formula
  \[
    \Sigma_1^R(k)
    =
    -{g^2\over32\pi^2}\int_0^1 dx\,
    \log{ k^2x(1-x)+m_1^2-i0 \over m_1^2}.
  \]
- The threshold cut analysis follows the source branch prescription:
  for \(s>4m_1^2\), the interval \(x\in[x_-,x_+]\) gives
  \(\log(-|a|-i0)=\log |a|-i\pi\).
- The imaginary part is
  \[
    \operatorname{Im}\Sigma_1^R(K)=
    {g^2\over32\pi}\sqrt{1-{4m_1^2\over s}}
  \]
  on the physical upper boundary.
- The chapter includes the narrow-width denominator, the \(S_0\) unit-circle
  phase motion, and the first-sheet sign argument showing that the resonance
  denominator has no first-sheet zero in either half-plane.
- The second-sheet statement is recorded as
  \(F_{\mathrm{II}}(s_\ast)=0\), with
  \(s_\ast=M_R^2-iM_R\Gamma_R+O(g^4)\).

## Checks

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/build_monograph.sh`: passed; compiled
  `monograph/tex/main.pdf` at 426 pages with clean log scan.
- Targeted render passed for the changed resonance and self-energy pages:
  `pdftoppm -png -f 179 -l 186 -r 170 monograph/tex/main.pdf
  /tmp/qft_253b_second_sheet_render`, followed by a rerender of page 182
  after cleaning the loop-contour labels.
