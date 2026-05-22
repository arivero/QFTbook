# 2026-05-22 253c CFT Opening Fixed-Point and Ising Pass

## Scope

Checked handwritten 253c pp. 1--6 against the compiled CFT opening.  The source
visual trace was rendered to:

- `monograph/tex/build/source_visual_trace/253c_trace-001.png`
- `monograph/tex/build/source_visual_trace/253c_trace-002.png`
- `monograph/tex/build/source_visual_trace/253c_trace-003.png`
- `monograph/tex/build/source_visual_trace/253c_trace-004.png`
- `monograph/tex/build/source_visual_trace/253c_trace-005.png`
- `monograph/tex/build/source_visual_trace/253c_trace-006.png`

## Manuscript Changes

Rewrote `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`.

The chapter now includes:

- local Lorentzian QFT data: Hilbert space, Poincare representation,
  \(P_\mu,J_{\mu\nu}\), invariant vacuum, local operator-valued
  distributions, covariance, and microcausality;
- stress-tensor assumptions, distributional conservation, symmetry, charge
  formulas for \(P^\mu\) and \(J^{\mu\nu}\), Lorentz tensor covariance, and
  scalar transformation of the trace;
- the bare-to-renormalized insertion definition
  \(\delta\mathcal L_{\rm int}^{\rm bare}
    =\sum_I\delta g_I(\mu)[O_I]_\mu\);
- the beta-function vector field and the trace identity
  \(T^\mu{}_\mu=\sum_I\beta_I[O_I]_\mu+\partial_\mu V^\mu\), with
  contact-term, curvature, virial, and improvement qualifications stated;
- the distinction between an RG fixed point and a conformal fixed point with
  an improved flat-space traceless stress tensor;
- the finite Ising trace space \(\widetilde{\mathcal H}_\Lambda\), diagonal
  spin operators, thermal trace, inverse temperature, magnetization curve,
  two-point correlation regimes, quoted \(D=2,3\) exponents, scalar cutoff
  representation, and the dictionary
  \(\phi\mapsto\sigma\), \([\phi^2]\mapsto\varepsilon\),
  \(\Delta_\varepsilon=D-1/\nu\).

## Visual Audit

Rendered manuscript physical PDF pages 416--421 to
`/tmp/qft_cft_opening_phys-416.png`--`/tmp/qft_cft_opening_phys-421.png`.
The two new figures are legible:

- Figure 48.1: lattice spins, magnetization as a function of
  \(\beta_{\rm T}\), and the three correlation regimes.
- Figure 48.2: scalar double-well cutoff model, Brillouin zone, mass tuning,
  and infrared Ising operator data.

No handwritten PDF page is embedded in the manuscript.

## Verification

Ran:

```bash
tools/build_monograph.sh
tools/audit_monograph_text.sh
git diff --check
```

The monograph build completed cleanly and the strict reader-facing text audit
passed.
