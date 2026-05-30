# 2026-05-30 Planar Nested Bethe-Yang Wrapper Pass

## Scope

Anti-wrapper pass on Volume VII, Chapter 13,
`chapter13_planar_n4_asymptotic_bethe_ansatz.tex`, in the planar
\(\mathfrak{su}(2|2)_{\rm c}\) nesting section.

The former proposition `Single-copy nested Bethe--Yang equations` displayed
the closed-chain periodicity equations obtained after the nested scattering
factors had already been constructed.  Its proof transported level-I,
level-II, and level-III excitations around their Zamolodchikov--Faddeev
chains and read off the corresponding products.  This bookkeeping is useful,
but it is not a separate theorem-level result.

## Changes

- Removed the proposition/proof wrapper around the single-copy nested
  Bethe--Yang equations.
- Kept the labelled equation
  `eq:planar-n4-single-copy-nested-bethe-yang`, because later planar
  integrability conventions use it.
- Rewrote the passage as `Single-copy nested Bethe--Yang periodicity`,
  explicitly stating that the equations are closed-chain periodicity
  bookkeeping for already-defined nested scattering factors, not mirror TBA
  and not an additional theorem.
- Updated the chapter dossier and added the old title to
  `tools/audit_theorem_form.py` so it cannot reappear as a theorem-family
  wrapper.

## Status

This continues issue #691.  The edit preserves the useful planar
integrability convention ledger while removing a proposition whose proof did
not contain theorem-level substance.
