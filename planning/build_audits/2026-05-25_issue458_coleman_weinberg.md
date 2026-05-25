# 2026-05-25 Issue #458: Coleman--Weinberg Effective Potential

## Scope

GitHub issue #458 flagged that the monograph only mentioned
Coleman--Weinberg in passing and did not derive the one-loop effective
potential, radiative scale generation, or dimensional transmutation.

## Manuscript Changes

- Added `One-Loop Effective Potential and Dimensional Transmutation` to the
  1PI effective-action chapter, immediately after the derivative expansion.
- Defined the effective potential as the zero-derivative part of the local
  formal 1PI action, distinct from the exact convex Legendre--Fenchel
  effective action.
- For massless \(\lambda\phi^4\), expanded around a constant background and
  derived the quadratic fluctuation operator
  \(-\partial^2+M^2(\varphi)\), \(M^2(\varphi)=\lambda\varphi^2/2\).
- Evaluated the one-loop determinant by differentiating with respect to
  \(M^2\), integrating back, and applying the \(\overline{\rm MS}\)
  subtraction:
  \[
    V_1=M^4(\varphi)(\log(M^2(\varphi)/\mu^2)-3/2)/(64\pi^2).
  \]
- Displayed the massless scalar one-loop potential
  \[
    V_{\rm eff}^{\overline{\rm MS}}
    =
    \lambda\varphi^4/24
    +
    \lambda^2\varphi^4
    (\log(\lambda\varphi^2/(2\mu^2))-3/2)/(256\pi^2)
    +O(\lambda^3).
  \]
- Checked the one-loop RG equation explicitly using
  \(\beta_\lambda=3\lambda^2/(16\pi^2)+O(\lambda^3)\).
- Derived the Coleman--Weinberg finite-subtraction form
  \(V_{\rm CW}^{(4)}(M)=\lambda_{\rm CW}\), including the \(-25/6\) constant.
- Solved for the formal nonzero stationary scale and the induced curvature
  \(V''(v)=\lambda_{\rm CW}^2v^2/(32\pi^2)+\cdots\).
- Stated the perturbative-control limitation: pure massless scalar
  \(\lambda\phi^4\) does not by itself give a controlled weak-coupling
  radiatively generated minimum.
- Added the general RG definition of dimensional transmutation by the scale
  \(\Lambda_{g_*}\) at which a running dimensionless coupling reaches a
  reference value, and contrasted the positive scalar beta function with the
  asymptotically free gauge-theory case.
- Included the controlled multi-coupling scalar-electrodynamics variant as the
  weak-coupling Coleman--Weinberg mechanism.
- Updated the chapter dossier with the new construction requirements and
  claim ledger entries.

## Verification

Completed after the edit:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 828 pages.
