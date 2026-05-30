# Primary Finite-Transformation Wrapper Pass

Date: 2026-05-30

Related issue: #691

## Scope

This pass continued the semantic theorem-form audit in Volume III, Chapter 6.
The chapter's finite primary transformation theorem was read together with
the elementary-generator list and the tensor-index rewrite.

## Changes

- Kept `Finite transformation law for a primary operator` as a theorem.  Its
  proof integrates the infinitesimal conformal Ward/contact action along a
  one-parameter conformal flow and is the structural result used later.
- Demoted `Elementary finite conformal transformations` from corollary form to
  paragraph-level sign checks.  The translation, dilatation, rotation, and
  special-conformal formulas are useful convention checks, but not a separate
  theorem-family result.
- Demoted `Finite transformation of tensor primaries` from proposition/proof
  form to paragraph-level tensor-index derivation.  The displayed covariant
  and contravariant formulas remain with equation labels; the derivation is
  the direct rewrite of the primary law using \(M_f=\Omega_fR_f\).
- Updated the theorem-form harness so these titles cannot return as
  theorem-family wrappers.
- Updated the Volume III, Chapter 6 dossier.

## Status

This pass removes two wrapper-level items while preserving all mathematical
content and convention checks.  Issue #691 remains open for continued
semantic reading across the remaining theorem/proposition inventory.
