# 2026-05-24 Issue #340 Wightman to AQFT Closure/Affiliation Audit

## Issue

GitHub issue #340 asked that the Wightman-to-AQFT direction be displayed as
an explicit construction, not only described conceptually.  In particular it
asked for the standard local von Neumann algebra
\[
  \mathcal R_\Phi(\mathcal O)=
  \{\exp(\ii\Phi(f)):\operatorname{supp}f\subset\mathcal O\}''
\]
and the associated closure/affiliation map.

## Edits

- Added an explicit definition of affiliation for self-adjoint unbounded
  operators with a von Neumann algebra.
- Stated explicitly that the passage from bare Wightman fields to a
  Haag--Kastler net is not automatic: essential self-adjointness and strong
  locality of closures are additional hypotheses.
- Displayed the Weyl-unitary construction
  \[
    \mathcal R_\Phi(\mathcal O)=
    \{\exp(\ii tX(h)):
      \operatorname{supp}h\subset\mathcal O,\ h=h^\dagger,\ t\in\mathbb R\}''
  \]
  alongside the spectral-projection construction.
- Proved their equivalence by the spectral theorem.
- Stated that each self-adjoint closure \(X(h)\) with support in
  \(\mathcal O\) is affiliated with \(\mathcal R_\Phi(\mathcal O)\), and with
  larger local algebras by isotony.
- Added a status remark distinguishing this conditional construction from
  model-by-model constructive proofs of Wightman and Haag--Kastler axioms
  from Euclidean measure/OS data.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 748 pages.
