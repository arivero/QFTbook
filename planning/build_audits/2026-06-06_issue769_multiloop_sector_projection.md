# Issue #769 multi-loop sector projection pass

Date: 2026-06-06.

Scope:

- Chapter: Volume II, Chapter 6, analyticity, crossing, Landau singularities,
  and generalized unitarity.
- New monograph label: `ca:multi-loop-maximal-cut-sector-projection`.
- Companion check:
  `check_multi_loop_maximal_cut_sector_projection()` in
  `calculation-checks/generalized_unitarity_reduction_checks.py`.

Substance audit:

- This is a reconstruction-architecture pass, not another one-loop coefficient
  cell.  It records the multi-loop distinction between a parent maximal cut
  and the sector-reduced master vector.
- The new block shows that numerator terms proportional to parent denominators
  are contact terms for the parent cut but become lower topologies after
  propagator cancellation.
- It separates three operations: fixing the parent leading singularity,
  projecting contact terms onto subtopologies, and reducing those sectors by
  IBP with boundary data.
- It explicitly demotes the shortcut "the maximal cut fixes the coefficient"
  unless lower-sector projections have been proved absent or included.

Negative controls:

- Two numerator representatives can have the same parent maximal cut but
  different lower-sector master projections.
- A lower-sector collapse is valid only sector by sector; it cannot be inferred
  from the parent maximal cut.
- Omitting lower sectors underbudgets the reduced-amplitude comparison unless
  their reduced masters are scaleless or otherwise absent in the declared
  family.

Expected verification:

- Run the focused generalized-unitarity check.
- Run the calculation evidence/inventory audits.
- Run Chapter 6 prose/form-label audits and the full monograph build.
