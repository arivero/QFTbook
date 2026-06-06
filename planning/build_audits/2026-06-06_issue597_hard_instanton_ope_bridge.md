# 2026-06-06 issue #597 hard instanton OPE bridge audit

## Target

- Volume II, Chapter 20D:
  `sec:instanton-hard-wilsonian-ope-datum`.
- Calculation evidence:
  `check_hard_wilsonian_ope_boundary_flow()` in
  `calculation-checks/instanton_physical_amplitude_architecture_checks.py`.

## Scope Judgment

This pass continues the instanton amplitude lane on the physics side.  It does
not add ADHM, Uhlenbeck, or other moduli-space infrastructure.  The new block
asks what the hard four-source instanton coefficient means as a local QFT
input.

The pass makes the Wilsonian split explicit for the concrete hard benchmark:
the short-size coefficient, boundary flux, long-size remainder, operator
matching, physical matrix element, and projection/sector residuals are
separate objects.

## Re-Audit Notes

- Physics depth: improved.  A hard instanton source coefficient is no longer
  allowed to masquerade as either a direct hadronic amplitude or a completed
  local operator coefficient.
- Architecture: improved.  The existing abstract Wilsonian size split in Ch20
  is now connected to the Ch20D hard four-fermion benchmark.
- Scope boundary: retained.  The pass does not compute a new Pauli-Villars
  determinant constant, prove continuum instanton convergence, or determine a
  hadronic matrix element from QCD.
- Directive hygiene: satisfied.  The issue/audit language is kept in this
  planning file; the TeX remains reader-facing monograph content.

## Evidence Contract

The companion finite check verifies:

- the `SU(3)`, `N_f=2` hard coefficient retains mass dimension `-2`;
- the individual-slot tail gives a nonzero Wilsonian boundary flux;
- the short coefficient and long-size tail have cancelling factorization-scale
  flows in the completed split;
- a source-to-operator basis change leaves the coefficient-matrix-element
  pairing fixed;
- the short coefficient alone is not the physical amplitude;
- omitting the long-size instanton tail underbudgets the physical assembly.
