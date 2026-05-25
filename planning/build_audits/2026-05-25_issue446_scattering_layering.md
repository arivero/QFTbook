# Issue #446 Scattering Layering

## Scope

- GitHub issue #446 reported that the partial fix of issue #3 had left two
  structural duplications:
  - Volume II Chapter 2 still reboxed the LSZ pole-extraction formula already
    proved in Volume I Chapter 13.
  - Volume I Chapter 12 still read as a theorem layer rather than as the
    introductory point-field/Cook-estimate layer feeding the Volume IV
    mathematical Haag--Ruelle theorem.

## Resolution

- Volume II Chapter 2 no longer reboxes the LSZ formula.  Its "LSZ as Pole
  Extraction" section now points to Theorem~\ref{thm:lsz-wave-packet} and
  states only the kernel-use consequence needed in later bound-state,
  resonance, and analyticity chapters.
- Volume I Chapter 12 now explicitly identifies itself as the scalar
  point-field construction and Cook-estimate layer.
- The former internal theorem statement in Volume I Chapter 12 has been
  demoted to Proposition~\ref{prop:haag-ruelle-cook-limits}; the theorem-level
  algebraic-net statement remains
  Theorem~\ref{thm:algebraic-haag-ruelle-scattering} in Volume IV.
- Volume II Chapter 2 now cites the Volume IV theorem as the Haag--Ruelle
  input and uses the Volume I proposition only as the construction model.
- The chapter dossiers and dependency map were updated so the layering is part
  of the project harness.

## Verification Target

Application chapters may use the Haag--Ruelle and LSZ results, but they should
not reintroduce standalone theorem boxes for those results.  The layers are:
Volume IV for theorem-level Haag--Ruelle, Volume I Chapter 12 for the scalar
Cook-estimate model, Volume I Chapter 13 for LSZ, and Volume II Chapter 2 for
kernel notation and applications.
