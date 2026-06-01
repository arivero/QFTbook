# 2026-06-01 Wightman-to-net bridge pass

## Scope

This pass addresses a remaining Volume IV foundational/AQFT proof-debt point:
the comparison from a Wightman field presentation to a represented local net
must not be stated as an automatic implication from the bare Wightman axioms.
The manuscript already had the conditional theorem; this pass adds the
explicit comparison datum and the observable-subnet distinction.

## Manuscript Changes

- `monograph/tex/volumes/volume_iv/chapter01_wightman_fields_and_reconstruction.tex`
  now cross-references the framework-level Wightman presentation definition
  before giving the refined cyclic version.
- `monograph/tex/volumes/volume_iv/chapter03_algebraic_qft_local_nets_and_states.tex`
  adds Definition `def:wightman-to-net-comparison-datum`.
  The datum specifies the Hermitian test-field spaces, self-adjoint closures,
  covariance as equality of closures, strong spectral-projection locality, and
  an observable-subnet prescription.
- The same chapter now explains why exponentials of smeared fields generate
  at most the field-generated net and need not equal the neutral observable
  net.  A finite parity model records the field-net/fixed-point-net
  distinction without pretending to prove a QFT theorem.

## Calculation Check

- Added `calculation-checks/wightman_net_bridge_checks.py`.
- The script checks the finite parity model: odd-field spectral projections
  are exchanged by parity, conditional expectation kills the odd field,
  fixed-point observables are diagonal, adjoining odd spectral projections
  recovers the finite field algebra, and strong locality is a statement about
  commuting spectral projections.

## Verification Plan

- `python3 calculation-checks/wightman_net_bridge_checks.py`
- `python3 -m py_compile calculation-checks/wightman_net_bridge_checks.py`
- `tools/run_calculation_checks.sh --list`
- `git diff --check`
- theorem-form, display-label, negative-scope, text, and chapter-dossier
  audits
- full monograph build before checkpointing

## Issue Status

This narrows GitHub issue #695.  It does not close #695: broader
foundational/AQFT theorem-boundary work remains, especially model-level
interacting examples and remaining structural theorem boundaries.
