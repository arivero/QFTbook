# 253a/253b No-Skip Coverage Register

This register is the working control for the user's instruction that the core
monograph may deepen and reorganize the 253a and 253b notes but may not skip
their material.  It complements chapter dossiers; it is not reader-facing
monograph prose.

## Coverage Status Labels

- `incorporated`: present in compiled monograph with the source argument
  reconstructed or deepened.
- `partial`: result appears, but a source derivation, example, figure, or
  conceptual distinction still needs repair.
- `deferred-core`: assigned to a later core chapter.
- `moved-noncore`: moved out of the core monograph with a path recorded.
- `needs-audit`: not yet checked page-by-page against the handwritten source.

## Immediate High-Priority Blocks

| Source block | Current status | Control file |
| --- | --- | --- |
| 253a full sequence | needs-audit | Volume I chapter dossiers; this register |
| 253b pages 71--80, generating functionals and 1PI effective action | partial | `planning/chapter_dossiers/volume_ii/chapter09_generating_functionals_1pi_effective_action.md` |
| 253b pages 97--110, 1PI RG | partial | `planning/chapter_dossiers/volume_ii/chapter12_1pi_renormalization_group.md` |
| 253b pages 147--156, Wilsonian effective actions and Polchinski flow | partial | `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md` |
| 253b pages 182--201, QCD one-loop beta function | incorporated | `planning/chapter_dossiers/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_dis.md` |

## Audit Requirements

- For 1PI material, verify that the Legendre transform, background-field
  tadpole-cancellation picture, convexity of the exact Euclidean effective
  action, and relation between exact 1PI vertices and connected functions are
  all present with correct hypotheses.
- For 1PI RG, verify that the scale-dependent field normalization,
  symmetric-subtraction coupling, nearby-scale comparison, logarithmic
  consistency, Callan--Symanzik derivation, and scheme-dependence formula are
  all present and not collapsed into textbook formulas.
- For Wilsonian RG, verify the smooth cutoff covariance, source-supported
  generating functional equality, covariance split, shell field integral,
  Wilson-Polchinski equation, irrelevant-coupling slaving, and continuum-limit
  construction.
- For QCD, the beta-function derivation must retain background-field
  covariance and the determinant coefficient audit; colored gauge-fixed fields
  must not be assigned physical spectral decompositions.

## Next Pass

The next source-coverage pass should promote the three `partial` 253b RG/1PI
entries to `incorporated` or record exact missing items.  The 253a sequence
requires a separate page-by-page register because it controls the logical
order of Kallen--Lehmann, nonperturbative scattering, LSZ, and perturbative
S-matrix calculations.
