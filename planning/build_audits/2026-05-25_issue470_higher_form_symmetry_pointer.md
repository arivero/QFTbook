# 2026-05-25 Issue #470: Higher-Form Symmetry Pointer

## Scope

GitHub issue #470 requested at least a definition-level treatment of
generalized global symmetries in the gauge-theory volume, with the electric
center one-form symmetry of pure Yang--Mills included before the detailed
categorical framework is developed in Volume IX.

## Manuscript Changes

- Added Section `Higher-Form Symmetry Data in Gauge Theory` to the classical
  Yang--Mills chapter.
- Defined an invertible \(p\)-form global symmetry operationally by
  topological codimension-\(p+1\) operators
  \(U_a(\Sigma^{D-p-1})\), charged \(p\)-dimensional operators, and the
  linking-number action on charged insertions.
- Specialized the definition to pure \(SU(N)\) Yang--Mills:
  \(Z(SU(N))=\mathbb Z_N\), Wilson lines carry \(N\)-ality \(k_R\), and the
  center one-form surface \(U_m(\Sigma)\) acts by
  \[
    U_m(\Sigma)W_R(C)U_m(\Sigma)^{-1}
    =
    \exp\!\left({2\pi i\,m k_R\over N}\operatorname{Lk}(\Sigma,C)\right)
    W_R(C).
  \]
- Derived the subgroup preserved by dynamical matter:
  \[
    A_{\mathrm{el}}
    =
    \{m\in\mathbb Z_N:
      \exp(2\pi i m k_\alpha/N)=1
      \text{ for every dynamical }R_\alpha\}.
  \]
  Thus adjoint matter preserves the center one-form symmetry and fundamental
  quarks break it completely.
- Added a forward-placement remark for higher groups, background
  \(p+1\)-form gauge fields/Postnikov data, and noninvertible or categorical
  topological defects in Volume IX.
- Updated the classical Yang--Mills chapter dossier.

## Verification

Completed after the edit:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 818 pages.
