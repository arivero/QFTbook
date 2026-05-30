# Bisognano--Wichmann Dequote Audit

Date: 2026-05-30

## Issue Context

- GitHub issue: #695, foundational reconstruction/AQFT proof debt.
- Local target: Volume XII, Chapter 4, where the Unruh-effect chapter imported
  the general Bisognano--Wichmann theorem as a quoted theorem even though the
  chapter's self-contained proof is the free massive scalar wedge-KMS model.

## Changes Made

- Replaced the general Bisognano--Wichmann `quotedtheorem` block by an explicit
  theorem-boundary remark.
- Stated the mathematical object of the general theorem: the standard pair
  \((\mathcal A(W_R),\Omega)\), its Tomita operator, modular group, and the
  comparison with Lorentz boosts.
- Identified the proof infrastructure required for the full AQFT theorem:
  Tomita--Takesaki modular theory, spectrum-condition analyticity,
  complexified boosts, and wedge locality at imaginary boost angle \(i\pi\).
- Kept the local, self-contained proof obligation in the chapter: the free
  massive scalar wedge-KMS theorem, proved from tube analyticity, the
  \(i\pi\) wedge map, spacelike commutativity, Wick expansion, and
  boundary-value control.
- Updated the chapter dossier so the claim ledger no longer treats the
  external theorem as local proved content.

## Verification Plan

- Check that the old `thm:bisognano-wichmann-boundary` label is absent.
- Re-run the Unruh geometry calculation check.
- Run text and dossier audits.
- Build the monograph and record the resulting page count.
