# 2026-05-30 Bisognano--Wichmann Proof-Mechanism Pass

## Scope

This pass addresses the foundational/AQFT quoted-theorem proof-debt cluster
for the Bisognano--Wichmann theorem in Volume IV, Chapter 4.  The theorem is
retained as a quoted theorem, but the manuscript now explains the actual
Wightman analytic mechanism rather than treating wedge modular covariance as
a black box.

## Manuscript Change

- Added the Wightman polynomial wedge core `\mathfrak P(W_R)\Omega` and the
  initial Tomita operator `S_{W_R,0}A\Omega=A^*\Omega`.
- Explained why Reeh--Schlieder and separatingness are the domain inputs that
  allow closure of the Tomita operator.
- Displayed the smeared Wightman strip function for polynomial fields under
  the complex boost `\Lambda_R(z)`.
- Recorded the tube-domain input from the spectrum condition for
  `0<Im z<pi`.
- Recorded the locality step at `Im z=pi`, where the complex boost maps the
  right wedge to the left wedge.
- Displayed the `2 pi` KMS boundary relation for the boost automorphism in
  the chapter's KMS convention.
- Identified the polar-decomposition step that recovers the modular
  conjugation from the closed Tomita operator.

## Issue Alignment

- #695: improves the BW part of the foundational quoted-theorem proof debt.
- #691: preserves a genuinely deep theorem while making clear where the proof
  substance lies, rather than leaving a theorem-like assertion floating as an
  unexplained structural import.

## Remaining Proof Debt

This pass does not close #695.  The full issue still includes OS
boundary-value infrastructure, nuclearity/split, Borchers--Wiesbrock,
DHR/DR examples beyond the theorem-boundary clarification, and substantial
interacting-model examples.
