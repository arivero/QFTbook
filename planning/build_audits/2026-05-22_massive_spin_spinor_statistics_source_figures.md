# 2026-05-22 Massive Spin and Spinor-Statistics Source/Figure Audit

## Source Block

- Primary handwritten source: `references/253a lectures 2022.pdf`, pp. 146--165.
- Operational transcription: `transcription/tex/253a/foundations.tex`, roughly
  lines 6024--6909.
- Source visual trace rendered to
  `monograph/tex/build/source_visual_trace/253a_trace-146.png` through
  `monograph/tex/build/source_visual_trace/253a_trace-165.png`.

## Manuscript Homes

- `monograph/tex/volumes/volume_i/chapter15_massive_particles_with_spin.tex`
- `monograph/tex/volumes/volume_i/chapter16_spinor_fields_fermionic_statistics_and_grassmann_path_integrals.tex`

## Source Content Checked

- Massive rest momentum \(p_R=(m,\vec0)\), standard boosts \(L(p)\), and the
  delta-normalized state factor \(N(\vec p)=(m/\omega_{\vec p})^{1/2}\).
- Wigner rotation \(W(\Lambda,p)=L(\Lambda p)^{-1}\Lambda L(p)\), including
  the \(((\Lambda p)^0/p^0)^{1/2}\) factor in the delta-normalized state
  transformation.
- Projective rotation representations by path lifting, endpoint-fixed homotopy,
  noncontractible \(2\pi\) loop, contractible \(4\pi\) loop, and the lift
  \(\widetilde{SO(3)}\simeq SU(2)\).
- Decomposition into \(SU(2)\) spin-\(j\) irreducibles and the source
  row-index convention for matrix multiplication.
- Spin-\(\frac12\) Pauli rotation
  \(\exp(-\ii\theta\sigma_3/2)\), including the \(2\pi\mapsto -1\) check.
- Mostly-plus gamma matrix basis, spinor Lorentz generators, covariance of
  gamma matrices, and momentum-space Dirac equations for \(u\) and \(v\).
- \(\beta=\ii\gamma^0\), \(R(\Lambda)^\dagger=\beta R(\Lambda^{-1})\beta\),
  delta-normalized \(\mathcal U,\mathcal V\), \(\beta\)-inner products, spin
  sums, rest spinors, \(\gamma_5\), and
  \(\mathcal V_R^\sigma=\gamma_5\mathcal U_R^\sigma\).
- Free spinor locality sign check: the ordinary commutator gives a nonzero
  spacelike scalar part, while the CAR gives the Pauli--Jordan difference.

## Figure/Rendering Check

- Manuscript pages rendered:
  - `massive_spin_render_phys-141.png` through
    `massive_spin_render_phys-147.png`;
  - `spinor_statistics_render-287.png` through
    `spinor_statistics_render-293.png`.
- Checked visually:
  - the \(SO(3)\to SU(2)\) lift diagram is legible and labels \(1\), \(2\pi\),
    \(-1\), \(2\pi\), and \(4\pi\) correctly;
  - the path-homotopy diagram distinguishes homotopic paths from the
    noncontractible \(2\pi\) loop and states that its square is contractible;
  - the explicit spinor matrices, rest spinors, and spin sums fit inside the
    text block;
  - the spinor-statistics derivation fits on a single page without equation
    overrun.

## Verification

- `git diff --check`
- `tools/build_monograph.sh`

The monograph build and strict text audit were clean after the patch. The only
LaTeX warning reported during the build was an existing hyperref PDF-string
warning in a different chapter.
