# Issue #258 KLN Hypotheses Pass

## Scope

- Oldest active GitHub issue: `#258`, on the KLN paragraph in
  `monograph/tex/volumes/volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex`.
- Required repair: replace the verbal KLN description by a labeled statement
  with explicit hypotheses, including finite-dimensional degenerate
  subspaces, bounded perturbation, and existence of the long-time inclusive
  transition probability.

## Content Added

- Added the theorem "Finite-degeneracy KLN cancellation."
- Stated the Hilbert-space setup:
  an unperturbed Hamiltonian \(H_0\), finite-dimensional degenerate projectors
  \(P_A\) and \(P_B\), and \(d_A=\operatorname{rank}P_A<\infty\),
  \(d_B=\operatorname{rank}P_B<\infty\).
- Stated the perturbative Hamiltonian hypothesis \(H=H_0+V\) with \(V\)
  bounded and self-adjoint, and defined the interaction-picture evolution
  \(U_T\).
- Required existence, after regulators, of the coefficientwise long-time
  inclusive limit
  \[
    \lim_{T\to\infty}
    d_A^{-1}\operatorname{Tr}(P_B U_TP_AU_T^\dagger P_B).
  \]
- Made explicit the KLN cancellation mechanism as unitary regulator-singular
  mixing inside the degenerate subspaces:
  \[
    P_BS_\rho P_A=U_B(\rho)S_{\rm fin}(\rho)U_A(\rho)^\dagger .
  \]
- Proved that the final-state sum and initial-state average cancel the unitary
  degenerate rotations, leaving
  \[
    d_A^{-1}\operatorname{Tr}_{P_B\mathcal H_0}
    (S_{\rm fin}S_{\rm fin}^\dagger).
  \]
- Added a field-theory caveat: relativistic interactions are generally
  unbounded operator-valued distributions and exact massless degeneracy is
  continuous, so the abstract theorem identifies the regulator and
  detector-cell structure needed before taking limits.
- Updated the chapter dossier.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
