# 2026-05-22 253b Renormalized Operators And Minimal Subtraction Source Audit

## Scope

- Source block: `references/253b lecture notes 2023.pdf`, from the bottom of
  page 110 through page 118.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, around the renormalized
  operator and minimal-subtraction block.
- Additional comparison:
  `references/253b transcribed lecture notes.tex`, around the same source
  block.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter12_renormalized_operators_and_minimal_subtraction.tex`.

## Source Content Checked

- Infinitesimal deformation of the action
  \(\delta S=\int\dd^Dx\,\delta g_I O_I\) and the relation between bare and
  running deformation coordinates
  \(\delta g_I=\delta g_J(\mu)N_{JI}(\mu)\).
- Definition of the renormalized operator
  \([O_I]_\mu=N_{IJ}(\mu)O_J\) by rewriting the same deformation in running
  coordinates.
- The full differentiation of the bare deformation at fixed bare data:
  \(0=\dd\delta g_I/\dd\log\mu\), the linearized beta function
  \(\delta\beta_J=(\partial\beta_J/\partial g_K)\delta g_K\), and the
  resulting operator mixing equation
  \(\dd N_{IJ}/\dd\log\mu=-\gamma_{IK}N_{KJ}\) with
  \(\gamma_{IK}=\partial\beta_K/\partial g_I\).
- Diagonal running of renormalized operators and the fixed-point power law
  with anomalous dimension \(\gamma_I\).
- The elementary field-operator example:
  \([\phi]_\mu=Z(\mu)^{-1/2}\phi\) and
  \(\gamma_\phi=\frac12\dd\log Z/\dd\log\mu\).
- Dimensional regularization in \(D=d-\epsilon\), the dimensions
  \([\phi]=(d-\epsilon-2)/2\),
  \([O_I]=d-\epsilon+\delta_I(\epsilon)\), and
  \([g_I^\epsilon]=-\delta_I(\epsilon)\).
- Minimal-subtraction coordinates
  \(g_I^\epsilon=\mu^{-\delta_I(\epsilon)}
  [\lambda_I+\sum_{n\ge1}\epsilon^{-n}K_I^{(n)}]\).
- The \(d=4\) scalar quartic one-loop comparison between a finite momentum
  subtraction definition and MS, including the pole
  \(3/(16\pi^2\epsilon)\).
- The Laurent expansion of \(\beta_I^\epsilon\), the positive-power
  constraints \(\beta_I^{(m)}=0\) for \(m\ge2\) and
  \(\beta_I^{(1)}=\delta_I^{(1)}\lambda_I\), and hence
  \(\beta_I^\epsilon=\beta_I(\lambda)+\epsilon\delta_I^{(1)}\lambda_I\).
- The recursive equations determining pole coefficients from the
  \(\epsilon^0\) beta function, including the homogeneous-sector form
  involving
  \((1-\lambda_J\partial_{\lambda_J})K_I^{(n)}\).

## Manuscript Changes

- Added the explicit displayed calculation of
  \(\dd\delta g_I/\dd\log\mu\), so the operator mixing matrix is derived from
  the linearized coupling flow rather than merely asserted.
- Added the homogeneous-sector minimal-subtraction recursion equations that
  match the handwritten source formulas after the more general
  \(D_\epsilon\)-operator recursion.
- Confirmed that the field-operator \(Z^{-1/2}\) example, the scalar
  quartic one-loop pole, and the positive-power beta-function constraints are
  present in the chapter.
- Updated the chapter dossier and the no-skip coverage register to mark this
  source block as certified.

## Rendered Check

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/253b_110-110.png` and `/tmp/253b_111_118-111.png` through
  `/tmp/253b_111_118-118.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_ops_ms_final-256.png` through `/tmp/qft_ops_ms_final-265.png`.
- Visual checks covered the operator-mixing figure, field-insertion figure,
  minimal-subtraction pole-structure figure, scalar quartic one-loop figure,
  and Laurent/recursive-structure figure.  No cropped equations, overlapping
  labels, or missing figure elements were found in the audited pages.

## Verification

- `tools/build_monograph.sh` completed cleanly after the TeX edits.
- The strict monograph text audit inside the build completed cleanly.
- `tools/audit_monograph_text.sh` completed cleanly.
- `git diff --check` completed cleanly.

This promotes handwritten 253b bottom page 110 through page 118 to certified
coverage after the renormalized-operator and minimal-subtraction source audit.
