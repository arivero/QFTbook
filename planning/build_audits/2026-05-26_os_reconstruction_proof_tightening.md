# 2026-05-26 OS Reconstruction Proof Tightening

Scope: foundational proof-depth pass prompted by the requirement that
Osterwalder--Schrader reconstruction be proved clearly in the monograph.

## Manuscript Changes

Volume IV, Chapter 2 now makes two proof obligations explicit.

- Strengthened Proposition `prop:os-ordered-field-closability`: the proposition
  now first proves that ordered Euclidean field insertions preserve the OS
  null space, hence descend to the reflection-positive quotient, and only then
  proves closability from the adjoint-insertion identity.
- Made the ordered-insertion adjoint identity an explicit hypothesis of the
  OS reconstruction theorem for the field labels being reconstructed.
- Rewrote the proof of Theorem `thm:os-reconstruction` as a dependency chain:
  reflection-positive Hilbert quotient; positive-time contraction semigroup
  and nonnegative Hamiltonian; corrected OS-II many-variable analytic route;
  quotient-well-defined field insertions; and Wightman temperedness, locality,
  covariance, and recovery of noncoincident Schwinger functions.

This pass preserves the chapter's treatment of the OS-I error: the faulty
step is the separate-Laplace-to-joint-Laplace assertion, while the corrected
OS-II route uses the linear-growth input to obtain polynomial tube bounds and
tempered Lorentzian boundary values.

## Verification

Completed before commit:

- `python3 calculation-checks/haag_ruelle_fock_inner_product_checks.py`
- `python3 -m py_compile calculation-checks/haag_ruelle_fock_inner_product_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The final build was clean and produced
`monograph/tex/main.pdf` with 1771 pages.
