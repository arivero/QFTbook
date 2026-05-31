# Build Audit: Stringbook GLSM/Mirror Deepening Pass

Date: 2026-05-31

## Trigger

Xi noted that the QFT monograph still lacked substantial purely-QFT material
from the stringbook appendices, especially the GLSM and mirror-duality
material in Appendix K, and emphasized that any incorporated stringbook topic
must be more self-contained and deeper than the stringbook treatment.

## Source Leads

- Internal convention/source lead:
  `/Users/xiyin/PhysicsLogic/references/stringbook/string notes.tex`,
  Appendix K, especially the charged-chiral mirror and cigar/Liouville
  subsections.
- Local primary-reference sidecars used for scrutiny, not as authority:
  `references/susy_glsm_mirror/hori_vafa_mirror_symmetry_hep-th_0002222.txt`
  and
  `references/susy_glsm_mirror/hori_kapustin_cigar_liouville_hep-th_0104202.txt`.

## Edits

- Strengthened `planning/12_strict_writing_harness.md` with an explicit
  stringbook/classic-reference reconstruction rule: stringbook appendices and
  classic papers are source leads, not hidden proof sources.
- Expanded Volume VII, Chapter 09 with a charged-chiral dual-variable
  development:
  - first-order superspace datum with real `B_i`;
  - twisted-linear constraint from integrating over `Y_i`;
  - Legendre elimination of `B_i`;
  - superspace integration-by-parts giving the `-Q_i^a Sigma_a Y_i`
    twisted `F`-term;
  - exponential vortex datum with its regulator-level proof obligations;
  - elimination of `Y_i` and exact matching to the Coulomb one-loop
    twisted superpotential;
  - finite FI-coordinate shift from vortex coefficient normalization;
  - logarithmic-torus mirror presentation and the `P^{N-1}` critical-point
    ledger.
- Added the cigar/Liouville mirror-chain section as a QFT comparison problem:
  classical quotient metric, gauge-field elimination, dual variables
  `Y,Y_P`, single exponential term, vector constraint `Y+Y_P=0`, resulting
  `N=2` Liouville data, and the theorem-status boundary for full equality
  with the cigar coset QFT.
- Updated the Chapter 09 dossier and calculation-check inventory.

## Verification Intent

The finite convention-sensitive algebra is checked by
`calculation-checks/susy_2d_lg_glsm_checks.py`, now including:

- charged-chiral mirror-variable elimination;
- FI-coordinate shift from vortex coefficient normalizations;
- `P^{N-1}` mirror critical-point simplicity;
- cigar quotient metric coefficients after algebraic elimination of the
  gauge field.

The full QFT theorem remains explicitly bounded: a proof requires a regulator
or reconstruction framework that constructs vortex sectors, determinant
normalizations, local operator maps, topological sectors, and equality of
continuum local algebras/Hilbert spaces.
