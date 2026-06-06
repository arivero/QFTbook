# 2026-06-06 issue #597 physical projection bridge audit

## Target

- Volume II, Chapter 20D:
  `sec:instanton-source-kernel-physical-projection` and
  `ca:instanton-source-kernel-physical-projection`.
- Calculation evidence:
  `check_source_kernel_physical_projection_bridge()` in
  `calculation-checks/instanton_physical_amplitude_architecture_checks.py`.

## Scope Judgment

This pass develops the physical-amplitude side of the instanton chapter.  It
does not add moduli-space structure.  The inserted block opens the final map
from an assembled Euclidean instanton source kernel to a physical quantity:
stable-particle pole extraction, spectral-bin/discontinuity projection, OPE
matching, or an infrared-safe inclusive measurement.

The block is meant to prevent a common overclaim: a finite source-kernel number
is not automatically a scattering amplitude, hadronic matrix element,
spectral weight, or real-time rate.  Each physical use requires its own
projection and its own residual budget.

## Re-Audit Notes

- Physics depth: improved.  The pass targets the same kind of subtle
  amplitude-extraction work that makes the original instanton calculation hard:
  source overlaps, pole windows, spectral inversion, continuation, and
  infrared/matching choices.
- Architecture: improved.  It connects the hard assembled coefficient to
  physical observables without treating the observable handoff as a label swap.
- Scope boundary: retained.  The text does not claim a general nonperturbative
  LSZ theorem or solve the continuum instanton integral.
- Directive hygiene: satisfied.  This planning file carries the audit language;
  the TeX remains reader-facing monograph content.

## Evidence Contract

The companion finite check verifies:

- pole-window extraction with source/sink overlaps and excited-state leakage;
- failure of raw source correlators or overlap division alone to define a
  matrix element;
- spectral-bin projection versus Euclidean Stieltjes values and contact
  polynomials;
- one-Euclidean-value inversion failure by two positive spectral measures;
- bridge residual telescope and underbudgeting when pole/bin isolation is
  omitted;
- rejection of colored auxiliary kernels as standalone physical LSZ amplitudes.
