# Issue #253 Descent Bicomplex Pass

## Scope

- Oldest active GitHub issue: `#253`, on the descent equations in
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Required repair: state the bigraded local-form complex, display the
  \((s,d)\) cocycle and coboundary conditions, and connect
  \(H^{1,4}(s\mid d)\) to consistent gauge anomalies rather than asserting the
  relation.

## Content Added

- Defined \(\Omega_{\mathrm{loc}}^{p,q}\), local \(p\)-forms of ghost number
  \(q\), and the two anticommuting differentials
  \[
    d:\Omega_{\mathrm{loc}}^{p,q}\to\Omega_{\mathrm{loc}}^{p+1,q},
    \qquad
    s:\Omega_{\mathrm{loc}}^{p,q}\to\Omega_{\mathrm{loc}}^{p,q+1},
    \qquad
    d^2=s^2=sd+ds=0.
  \]
- Displayed the relative cocycle and coboundary relations for a
  four-dimensional local anomaly:
  \[
    s a_4^{(1)}-d a_3^{(2)}=0,
    \qquad
    a_4^{(1)}\sim a_4^{(1)}+s b_4^{(0)}+d b_3^{(1)}.
  \]
- Added a proposition proving the local-functional identification between
  Wess--Zumino consistency, local counterterm shifts, and the relative class
  \([a_4^{(1)}]\in H^{1,4}(s\mid d)\).
- Introduced the anti-Hermitian ghost \(\mathsf c\) and the BRST rules
  \(s\mathsf A=\dd\mathsf c+[\mathsf A,\mathsf c]\),
  \(s\mathsf c=-\mathsf c^2\), and \(s\mathsf F=[\mathsf F,\mathsf c]\).
- Derived the first two descent equations from \(sI_6=0\),
  \(I_6=\dd I_5^{(0)}\), and the algebraic Poincare lemma:
  \[
    sI_5^{(0)}=\dd I_4^{(1)},\qquad
    sI_4^{(1)}=\dd I_3^{(2)}.
  \]
- Updated the anomaly chapter dossier.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
