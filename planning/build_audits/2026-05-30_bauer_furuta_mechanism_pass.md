# Bauer-Furuta Mechanism Pass

Date: 2026-05-30

## Scope

This pass advances issue #698 in Volume VIII, Chapter 8.  The target is the
Bauer-Furuta and Furuta theorem boundary in the Donaldson-Seiberg-Witten
comparison chapter.

## Changes

- Added the Sobolev monopole map
  \[
    \mathcal F(b,q)=(d^*b,\ d^+b-\sigma(q)+F_{B_0}^+-\eta^+,\ 
    \not D_{B_0}q+\rho(b)q)
  \]
  and its Fredholm-plus-compact split \(\mathcal F=L+C\).
- Explained how the Weitzenbock estimate gives an isolating ball, how low-mode
  finite-dimensional approximation produces maps between representation
  spheres, and why increasing the cutoff only suspends the stable class.
- Clarified that the ordinary Seiberg-Witten integer is a cohomological image
  of this stable class, not the primary object.
- Added the spin \(\operatorname{Pin}(2)\)-equivariant mechanism behind
  Furuta's \(10/8+2\) inequality: the spin quaternionic structure gives an
  equivariant monopole map, the virtual representation difference records the
  quaternionic Dirac index \(-\sigma/8\) and \(b_2^+\), and the inequality is
  extracted by equivariant stable homotopy.
- Extended the Donaldson/SW calculation check to verify the spin Dirac
  quaternionic-index arithmetic in the K3 and spin elliptic-surface examples.

## Proof-Form Status

The Bauer-Furuta and Furuta statements remain quoted mathematical
infrastructure.  The manuscript no longer leaves them as names: it now exposes
the analytic construction used by the chapter and identifies the exact
equivariant stable-homotopy input that is still external to the monograph's
QFT derivation.
