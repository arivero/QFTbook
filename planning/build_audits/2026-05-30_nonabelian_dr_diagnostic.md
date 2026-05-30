# Nonabelian Doplicher--Roberts Diagnostic Pass

## Scope

- Continued issue #695, the foundational AQFT / quoted-theorem proof-debt
  lane, and issue #691, the theorem-boundary audit.
- Targeted Volume IV, Chapter 4, immediately after the
  Doplicher--Roberts reconstruction theorem boundary.

## Finding

The chapter already had a useful finite pointed
\(\mathbb Z/N\mathbb Z\) diagnostic.  That model explains Abelian charge
grading, but Doplicher--Roberts reconstruction is a compact-group theorem and
must also make clear how nonabelian multiplets are encoded by the sector
category.  Adding a finite nonabelian check improves the theorem boundary
without pretending to reprove the full Tannakian converse.

## Change

- Added a finite \(S_3\) representation-category diagnostic:
  - irreducible characters \(1,\epsilon,V\);
  - tensor products
    \(\epsilon^2=1\), \(\epsilon V=V\),
    \(V^2=1\oplus\epsilon\oplus V\);
  - evaluation \(g\mapsto (D_W(g))_W\) as a tensor natural automorphism of
    the forgetful fiber functor;
  - faithfulness of the standard representation, making the six evaluations
    distinct;
  - Haar averaging as projection onto the trivial isotypic part by matrix
    coefficient orthogonality.
- Extended `calculation-checks/dhr_dr_reconstruction_checks.py` from the
  pointed diagnostic to include exact \(S_3\) representation-law,
  faithfulness, character-ring, and Haar-projection checks.
- Updated the chapter dossier and calculation-check README.

## Verification

- `python3 calculation-checks/dhr_dr_reconstruction_checks.py`

## Status

This strengthens the local Doplicher--Roberts quoted-theorem exposition.  It
does not close #695 because the full DHR/DR, nuclearity/split,
Bisognano--Wichmann, and model-example proof-debt lane remains open.
