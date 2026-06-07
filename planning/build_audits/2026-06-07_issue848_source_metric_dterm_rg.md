# 2026-06-07 Issue #848 Source-Metric D-Term RG Audit

## Scope

This pass targets two full-QFT sides of the Hori--Vafa mirror issue: a
protected superpotential and a matched low Hamiltonian do not determine
source-normalized correlators after finite-field `D`-term or measure changes,
and an imported cigar/Liouville reflection formula cannot be used below
`k=1` until its raw gamma-ratio domain and positive normalization branch are
declared.

## Change

Extended `ca:glsm-mirror-dterm-rg-schur-gate` in Volume VII Chapter 09.  The
new paragraph defines the finite low-energy source metric
`Gamma^M_{AB}(E,Omega)` obtained after high-mode Schur elimination.  A
two-source cell shows that the scalar source normalization which matches one
operator leaves the mixed two-point source kernel different.

The same pass repairs the imported cigar reflection target by separating
`nu_raw(k)` from the positive scale `nu_+(k;mu,varrho_ref)`, listing all
special levels `k=1/n`, and replacing the phase-density logarithm by
`log nu_+`.

## Companion

Extended `check_full_mirror_dterm_rg_schur_gate()` in
`calculation-checks/susy_2d_lg_glsm_checks.py`.  The check now verifies:

- the first-source normalization matches the scalar source-resolvent;
- the same scalar normalization leaves the second source row and mixed source
  metric wrong;
- a full finite source-renormalization matrix matches the source metric;
- the mixed source-metric residual is a separate budget item.

Extended `check_cigar_liouville_spectral_data_cell()` in the same companion.
The check now verifies the `nu_raw` sign ledger below `k=1`, rejects the
principal complex power of negative raw `nu`, samples raw `k=1/n` failures,
and uses the positive `nu_+` scale for unitary reflection and phase-density
tests.

## Quality Boundary

This is not a proof of Hori--Vafa mirror equivalence, noncompact `D`-term
rigidity, or the Liouville path-integral derivation of the imported reflection
formula.  It sharpens the admissible-mirror datum by tying omitted
`D`-term/measure data to the source metric measured by two-point correlators
and by requiring a positive reflection-normalization scale before continuous
spectral densities are read off.

## Verification Plan

- Run the focused SUSY GLSM companion and focused harness entry.
- Run Chapter 09 local theorem/display/prose/style audits and TeX leakage scan.
- Run evidence-contract, calculation-inventory, dossier, JSON, and diff checks.
- Run the full Python calculation-check suite and full monograph build before
  committing if the focused pass is clean.

## Verification Result

Completed on 2026-06-07.  The focused SUSY GLSM companion, focused harness
entry, Chapter 09 local audits, TeX leakage scan, evidence-contract audit,
calculation-inventory audit, chapter-dossier audit, full Python
calculation-check suite, and full monograph build/log scan all passed before
staging.  The first monograph rerun caught an overfull display in the repaired
reflection formula; the display was split and the full build/log scan then
passed cleanly.
