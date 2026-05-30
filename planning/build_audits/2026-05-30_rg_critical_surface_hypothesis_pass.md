# RG Critical-Surface Hypothesis Pass

Date: 2026-05-30

Related issues: #505, #691

## Scope

This pass continued the assumption/hypothesis versus theorem/proposition audit
in Volume XI, Chapter 7.  The target was the finite-codimension
critical-surface statement near the local stable-graph theorem.

## Changes

- Demoted `Finite-codimension critical surface` from proposition form to
  paragraph-level derivation, because after the \(C^1\) stable graph and
  transversality hypotheses are supplied the codimension statement is the
  standard submersion/implicit-function consequence.
- Added a paragraph identifying the analytic burden: the earlier
  Lyapunov--Perron theorem proves a Lipschitz graph under the displayed
  contraction hypotheses, while the \(C^1\) submanifold conclusion requires a
  differentiable stable-manifold theorem for the RG Banach map or an
  equivalent model-specific construction of the differentiable graph.
- Kept the submersion/implicit-function argument in prose, so the reader can
  see exactly what is being used without giving the elementary consequence a
  theorem-family wrapper.
- Updated the theorem-form harness so the old proposition title cannot return
  as a theorem-family wrapper.
- Updated the Volume XI, Chapter 7 dossier.

## Status

This pass does not close #505: it clarifies one local piece of the rigorous RG
framework.  Model-specific construction of \(C^1\) stable manifolds, ordinary
short-range scalar reconstruction, and gauge-compatible RG examples remain
open.
