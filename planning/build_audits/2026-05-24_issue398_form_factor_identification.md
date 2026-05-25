# Issue 398: Electromagnetic Form-Factor Identification

Date: 2026-05-24.

Issue:

- GitHub #398 flagged that identifying the chapter's \((F,G)\) with the
  standard Dirac--Pauli \((F_1,F_2)\) form factors misses an \(i\)-factor and
  sign coming from the mostly-plus gamma convention and the chosen
  \((p+p')^\mu\) basis.

Convention check:

- The chapter uses
  \[
    M^\mu=\gamma^\mu F(k^2)-\frac{\ii}{2m}(p+p')^\mu G(k^2),
    \qquad k=p-p',
  \]
  with on-shell spinors obeying \((\not p-\ii m)u(p)=0\).
- With \(S^{\mu\nu}=-(\ii/4)[\gamma^\mu,\gamma^\nu]\), the on-shell Gordon
  identity gives
  \[
    \bar u(p')\,m^{-1}S^{\mu\nu}k_\nu\,u(p)
    =
    \bar u(p')
    \left(\gamma^\mu+\frac{\ii}{2m}(p+p')^\mu\right)
    u(p).
  \]
- Therefore the Dirac--Pauli basis in these conventions is
  \[
    M^\mu
    =
    \gamma^\mu F_1^{\rm DP}
    +
    \left(\gamma^\mu+\frac{\ii}{2m}(p+p')^\mu\right)F_2^{\rm DP},
  \]
  and coefficient comparison gives
  \[
    F_1^{\rm DP}=F+G,\qquad F_2^{\rm DP}=-G.
  \]

Fix:

- Inserted the displayed Pauli-tensor/Gordon identity before comparing
  coefficients.
- Updated the chapter dossier to record \(F_2^{\rm DP}=-G\), so the computed
  \(G(0)=-\alpha/(2\pi)\) is the standard
  \(F_2^{\rm DP}(0)=+\alpha/(2\pi)\).

Verification to run:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
