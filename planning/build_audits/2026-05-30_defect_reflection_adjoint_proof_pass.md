# 2026-05-30 Defect Reflection-Adjoint Proof Pass

## Scope

This pass continues the proof-substance and anti-wrapper audit for issue
#691.  The target was Volume IX, Chapter 9, `Reflection adjoint of a
topological-defect action`.

## Decision

The statement is retained as proposition-level material.  It is not a
calculation wrapper: it identifies the Hilbert-space adjoint of a bounded
topological-defect action after imposing radial reflection positivity,
existence of shrinking actions on a dense local domain, and bounded extension
to the radial Hilbert completion.

## Manuscript Change

- Replaced the compressed geometric proof by a finite-radius argument.
- Introduced \(\rho_{D,\epsilon}\) and
  \(\rho_{D^\dagger,\epsilon}\) as defect insertions on small spheres.
- Wrote the BPZ pairing as a reflection-positive ball/cylinder correlator.
- Reflected the finite-radius configuration before taking the shrinking
  limit, making explicit that reflection reverses the defect coorientation and
  sends \(D\) to \(D^\dagger\).
- Used topological isotopy only in the complement of the operator insertions.
- Passed to the Hilbert limit on the dense local domain and extended the
  adjoint identity by boundedness.
- Clarified that reflection-invariant defects give self-adjoint operators,
  while unitarity requires the stronger invertibility condition
  \(D^\dagger\otimes D\simeq\mathbf 1\).

## Verification Plan

Run the theorem-form, unnumbered-display-label, negative-scope, text, and
chapter-dossier audits after the edit.  Since the TeX source changed, rebuild
the monograph before committing.
