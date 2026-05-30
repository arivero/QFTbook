# 2026-05-30 Semiclassical Curvature Formula Demoted

## Target

- Cross-cutting proof-substance audit, especially GitHub issue #691.
- File:
  `monograph/tex/volumes/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.tex`.

## Finding

The chapter repeated the curvature-squared Euler tensors
\(H^{(1)}_{\mu\nu}\) and \(H^{(2)}_{\mu\nu}\) as a proposition with a proof.
The formulas are necessary for the semiclassical Einstein equation, but in
this chapter the derivation is a local metric-variation calculation already
developed in the point-splitting stress-tensor chapter.  Proposition/proof
presentation made the duplicate formula block look like a new theorem.

## Change

- Replaced the proposition/proof wrapper by a labelled paragraph,
  `Curvature-squared variational formulas`.
- Preserved the displayed formulae, the basic metric-variation identities, the
  Ricci-variation identity, the integrations by parts, and the conservation
  and trace checks.
- Added an explicit sentence saying these are variational identities fixing
  the local gravitational-coordinate normalization, not an additional
  structural theorem.
- Updated the Volume XII chapter dossier.

## Status

This is an anti-wrapper cleanup, not a change of mathematical content.  The
authoritative theorem-level discussion of the finite stress-tensor
renormalization freedom remains in the point-splitting stress-tensor chapter.
