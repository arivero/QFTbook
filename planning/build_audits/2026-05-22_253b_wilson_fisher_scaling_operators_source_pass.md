# 2026-05-22 253b Wilson-Fisher Scaling Operators Source Audit

## Scope

- Source block: `references/253b lecture notes 2023.pdf`, pages 124--135.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, around the Wilson-Fisher
  and scaling-operator block.
- Additional comparison:
  `references/253b transcribed lecture notes.tex`, around the same source
  block.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`.

## Source Content Checked

- The \(D=4-\epsilon\) scalar quartic Euclidean action and the mass tuning
  needed to ask for a massless infrared limit.
- The renormalized 1PI quartic coordinate
  \(\lambda(\mu)=-\mu^{-\epsilon}Z(\mu)^2\Gamma^{(4)}\) at the symmetric
  Euclidean subtraction point.
- The one-loop finite-\(\epsilon\) formula for \(\lambda(\mu)\), the
  intermediate \(\dd\lambda/\dd\log\mu\) expression at fixed bare coupling,
  the beta function
  \(\beta(\lambda)=-\epsilon\lambda+
  (3/(16\pi^2)+O(\epsilon))\lambda^2+O(\lambda^3)\), and the fixed point
  \(\lambda_*=16\pi^2\epsilon/3+O(\epsilon^2)\).
- The distinction between the divergent dimensionless bare coordinate
  \(\mu^{-\epsilon}g_0\) and the finite renormalized 1PI coordinate along the
  massless critical trajectory.
- The \(O_1=\phi\) anomalous dimension statement
  \(\gamma_\phi=O(\epsilon^2)\).
- The failure of the zero-momentum \(\phi^2\) subtraction because of the
  infrared integral \(\int\dd^D\ell/(\ell^2)^2\), and the replacement by a
  spacetime-dependent source with nonzero momentum.
- The one-loop \(O_2=\phi^2\) source relation, anomalous dimension
  \(\gamma_2(\mu)=\lambda_4(\mu)/(16\pi^2)+\cdots\), fixed-point value
  \(\gamma_{2*}=\epsilon/3+O(\epsilon^2)\), and
  \(\Delta_{\phi^2}=2-2\epsilon/3+O(\epsilon^2)\).
- The momentum-space and position-space scaling of
  \(\langle O_2O_2\rangle\), including the fact that the modewise Fourier
  integral with \((|p|/\mu_0)^{-\gamma_{2*}}\) is not a local operator
  definition.
- The point-splitting local definition of the fixed-point \(\phi^2\) scaling
  operator.
- The \(\mathbb Z_2\)-even critical surface, the mass/thermal eigenvalue
  \(y_t=D-\Delta_{\phi^2}\), the correlation-length exponent
  \(\nu=1/y_t\), and the odd source \(h[\phi]\) caveat in the full local
  coupling chart.
- The equation-of-motion descendant relation
  \(O_3=\phi^3\propto\Box\phi\) and
  \(\Delta_{\phi^3}=\Delta_\phi+2\).
- The \(O_4=\phi^4\) source deformation, why source momentum can be set to
  zero in this case, and the linearized relation
  \(\gamma_{4*}=\beta'(\lambda_*)=\epsilon+O(\epsilon^2)\), making
  \(\Delta_{\phi^4}=4+O(\epsilon^2)>D\).
- The dimension table for \(d=4-\epsilon\), \(d=3\), and \(d=2\), with the
  latter two rows treated as data about the corresponding fixed points rather
  than substitutions into the first-order epsilon series.

## Manuscript Changes

- Added the intermediate one-loop derivative and inversion steps connecting
  the finite-\(\epsilon\) 1PI coupling formula to
  \(\beta(\lambda)\).
- Added the explicit nonlocality caveat for the modewise
  \([O_2(x)]_{\rm mode}\) construction before the local point-splitting
  definition.
- Added the spacetime-dependent \(\phi^4\) source paragraph, the absence of
  the \(\phi^2\)-type infrared obstruction at \(p=0\), and the intermediate
  \(-\epsilon+3\lambda_4/(8\pi^2)\) step in the derivation of
  \(\gamma_{4*}\).
- Confirmed that the chapter keeps the fixed-point existence statements for
  \(d=3\) and \(d=2\) separate from the first-order epsilon expansion.
- Updated the chapter dossier and the no-skip coverage register to mark this
  source block as certified.

## Rendered Check

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/253b_124_135-124.png` through `/tmp/253b_124_135-135.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_wf_final3-283.png` through `/tmp/qft_wf_final3-291.png`.
- Visual checks covered the symmetric-coupling figure, bare-vs-renormalized
  coupling figure, \(\phi^2\) source/one-loop figure, critical-surface
  figure, momentum-to-position scaling figure, and
  descendant/irrelevant-operator figure.  No cropped equations, overlapping
  labels, or missing figure elements were found in the audited pages.

## Verification

- `tools/build_monograph.sh` completed cleanly after the TeX edits.
- The strict monograph text audit inside the build completed cleanly.
- `tools/audit_monograph_text.sh` completed cleanly.
- `git diff --check` completed cleanly.

This promotes handwritten 253b pages 124--135 to certified coverage after the
Wilson-Fisher fixed-point and scaling-operator source audit.
