# 2026-06-06 issue #769 production master-lane audit

## Target

- Volume II, Chapter 6:
  `ca:production-master-lane-observable-gate`.
- Calculation evidence:
  `check_production_master_lane_observable_gate()` in
  `calculation-checks/generalized_unitarity_reduction_checks.py`.

## Scope Judgment

This pass addresses the loop-amplitude architecture gap rather than adding one
more adjacent identity.  The new monograph block composes four operations that
must all be present for a physical prediction:

- generalized-cut or contour data paired with a master basis;
- differential-equation transport of masters from Euclidean boundary data to a
  physical branch;
- comparison of transported master jumps with an independently normalized
  Cutkosky channel datum;
- real/factorization assembly of the virtual hard function into an
  infrared-safe observable.

The text avoids presenting a new solved integral family.  Its purpose is to
make the production standard explicit: a cut reconstruction is not a physical
prediction until coefficient extraction, master evaluation, channel closure,
and observable assembly have all been checked in one normalization.

## Re-Audit Notes

- Physics depth: improved.  The inserted block is about computing physical
  loop amplitudes and observables, not about a tangential master-integral
  geometry exercise.
- Architecture: improved.  It connects existing finite cells into an ordered
  evaluation lane and names the failure mode of each shortcut.
- Scope boundary: retained.  The block states that the finite model is a
  bookkeeping audit and not a general solution of multi-loop integral families.
- Directive hygiene: satisfied.  Planning/audit language stays in this file
  and the dossier; the TeX block is written as monograph content.

## Evidence Contract

The companion finite check verifies exact rational composition of:

- a nontrivial pairing matrix \(P_{\rho i}\) between cut residues and master
  coefficients;
- two-letter master transport with branch/path data and lower-sector
  inhomogeneity;
- an independent physical channel jump;
- Laurent-pole cancellation between virtual and real/factorization pieces.

Negative controls reject raw cut residues as coefficients, Euclidean master
reuse, branch omission, lower-sector omission, raw-residue channel closure, and
virtual-only observable assembly.
