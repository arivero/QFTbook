# 2026-05-22 Perturbative Green Functions Source/Figure Audit

## Source Block

- Primary source: `references/253a lectures 2022.pdf`, pp. 100--112.
- Operational transcription: `transcription/tex/253a/foundations.tex`,
  approximately lines 3905--4558.
- Comparison aid only: `references/253a_notes.tex`.

## Manuscript Homes

- `monograph/tex/volumes/volume_i/chapter10_perturbative_green_functions_and_feynman_graphs.tex`
- `monograph/tex/volumes/volume_i/chapter11_lorentzian_green_functions_and_analytic_continuation.tex`

## Source Trace And Render Trace

- Handwritten trace rendered as
  `monograph/tex/build/source_visual_trace/253a_trace-100.png` through
  `253a_trace-112.png`.
- Compiled manuscript trace rendered as
  `monograph/tex/build/source_visual_trace/pert_green_render_phys-099.png`
  through `pert_green_render_phys-109.png`, corresponding to manuscript page
  labels 83--93.

## Repairs Made

- Added the Lorentzian and Euclidean scalar \(\phi^4\) densities before the
  Euclidean perturbative construction, while keeping the chapter explicitly
  about Green functions rather than scattering.
- Made the finite-mode path-integral regulator explicit:
  \(\int[\dd\phi]_\Lambda\leadsto
  \int\prod_{|k|\le\Lambda}\dd\widetilde\phi(k)\), with the real-field
  reality condition.
- Separated the unlabelled action-expansion vertex \(-g/4!\) from the
  labelled-leg rule \(-g\).
- Restored the source Wick-contraction counts:
  \(4\cdot3!/2\) for the tadpole and
  \(\frac1{2!}(2\cdot4^2\cdot3!)=4\cdot4!\) for the sunset.
- Stated that the tadpole insertion is independent of external momentum and
  divergent for \(D\ge2\), then displayed the cutoff integral \(C_1\) and its
  logarithmic/power asymptotics with the dimensionless \(\log(\Lambda/m)\).
- Tightened the spectral pole-mass discussion: \(m_*\) is read from the nearest
  isolated two-point singularity at \(k^2=-m_*^2\), equivalently
  \(k_D=\pm i\sqrt{\vec k^{\,2}+m_*^2}\) at fixed spatial momentum.
- Clarified that \(gC_1(\Lambda,m)\) is not uniformly small as the cutoff is
  removed, so the bare quadratic parameter \(m\) and the spectral pole mass are
  distinct data until a prescription is specified.
- Strengthened the counterterm discussion as a prescription-dependent
  reorganization that cancels local cutoff-dependent terms order by order, with
  the on-shell choice \(m_R=m_*\) stated as a possible prescription.
- In the Lorentzian chapter, wrote the unlabelled vertex rule with the full
  \((2\pi)^D\delta^D(\sum k_i)\), and made the first-sheet continuation path
  \(k^0=i k_E^D\) explicit.
- Rechecked the Wick-rotation diagram and the \(k^0\)-branch-cut diagram against
  source pp. 111--112: the positive-energy boundary value is approached from
  \(\operatorname{Im}k^0>0\) on the first sheet, with the conjugate placement
  on the negative-energy cut.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

The build completed cleanly. The only visible LaTeX warning is the pre-existing
hyperref PDF-string warning in the pion chapter, unrelated to this source block.

## Logical Boundary

This block remains strictly before the construction of asymptotic states. It
contains perturbative Euclidean and Lorentzian Green-function rules, self-energy
insertions, and analytic continuation data. It does not assign any scattering
interpretation to amputated external legs and does not introduce LSZ or the
S-matrix.
