# Issue #640 Theorem-Form Refactor

## Scope

Addressed GitHub issue #640, which asked for theorem-family environments to be
reserved for checkable mathematical claims rather than tautological summaries,
derivation tableaux, or long blocks of setup data whose proof is only an
application of an earlier result.

## Manuscript Changes

- Verified that the three small-form defects had already been repaired in the
  live manuscript:
  - Volume IV, Chapter 3 now states the AQFT field-coordinate passage as
    Remark `rem:aqft-to-wightman-fields`.
  - Volume I, Chapter 18 now presents the Gupta--Bleuler one-particle quotient
    as Construction `cons:gupta-bleuler-one-particle-quotient`, followed by a
    concise proposition for the Fock-space quotient.
  - Volume III, Chapter 7 now has a single `Short Multiplets as Operator
    Equations` section and a collected reference list rather than a duplicate
    summary theorem.
- Refactored the \(\Phi^4_2\) stochastic-quantization assembly in Volume XI,
  Chapter 9: the long analytic input list is now Hypothesis
  `hyp:phi-four-two-spde-assembly-inputs`; Theorem
  `thm:phi-four-two-spde-main-theorem` now states only the assembly conclusion.
- Refactored the finite-sector SPDE model-convergence application in Volume XI,
  Chapter 9: the coordinate-control data are now Hypothesis
  `hyp:spde-finite-sector-coordinate-control-data`; the result has now been
  demoted from theorem-family form to a coordinate-control consequence carrying
  the existing label
  `thm:spde-coordinate-estimates-model-convergence`.
- Refactored the negative-sector \(\Phi^4_3\) model-convergence application in
  Volume XI, Chapter 9: the scale-summed coordinate scheme is now Hypothesis
  `hyp:spde-negative-sector-scale-summed-coordinate-scheme`; the convergence
  result has now been demoted from theorem-family form to a coordinate-control
  consequence carrying the existing label
  `thm:spde-phi-four-three-negative-sector-model-convergence`, and textual
  references now call it a consequence rather than a corollary.
- Refactored the finite-order BPHZ--Wilsonian comparison in Volume II, Chapter
  16: the setup data are now Definition
  `def:finite-order-bphz-wilsonian-matching-context`, the estimates are
  Hypothesis `hyp:finite-order-bphz-wilsonian-matching-estimates`, and Theorem
  `thm:finite-order-bphz-wilsonian-matching` is now the quantitative matching
  statement.  Its proof now follows immediately after the theorem; the
  recursive coordinate-map construction follows the proof.
- Refactored the two Ising universality results in Volume II, Chapter 15: their
  long assumption lists are now Hypotheses
  `hyp:conditional-lattice-to-continuum-universality-data` and
  `hyp:conditional-ising-universality-lattice-to-cft-data`; the theorem
  statements now state only the conditional conclusions.

## Examined And Kept

- Volume III, Chapter 9 `thm:conditional-cft-reconstruction-from-ope` remains a
  theorem: the proof constructs the radial Hilbert space and separated-point
  hierarchy from the OPE datum, and the statement is proportional to the proof.
- Volume XI, Chapter 9 `thm:spde-compact-reconstruction` remains a theorem: it
  is the finite-sector reconstruction theorem with a wavelet construction and
  uniqueness proof.
- Volume XI, Chapter 7 `thm:newton-kantorovich-rg-fixed-point` remains a
  theorem: it is a Banach-space Newton--Kantorovich fixed-point theorem with a
  complete contraction proof.

## Verification

- `git diff --check`
- `tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- exact wrapper regression scan:
  `rg -n -F -e '\\begin{theorem}[Coordinate estimates imply finite-sector model convergence]' -e '\\begin{theorem}[Negative-sector model convergence from scale-summed coordinates]' -e '\\begin{theorem}[Basic unitarity bounds and short multiplets]' -e '\\begin{theorem}[Field coordinates on a local net give Wightman data]' -e '\\begin{theorem}[Gupta--Bleuler quotient is the two-helicity photon Fock space]' monograph/tex/volumes`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

The full build regenerated `monograph/tex/main.pdf` at 2355 pages and the
final build-log scan was clean.
