# 2026-05-28 Issue #633: CFT Fixed-Point Trace and RG Pass

## Scope

Reading-based correction to the reopened #633 backlog for Volume III,
Chapter 1, `Fixed Points and Conformal Data`.

The chapter already had careful status language for CFT data, fixed-point
source charts, scale-versus-conformal caveats, RG monotones, and Ising
universality.  The remaining local gap was that several load-bearing
relations were compressed into prose: the flat trace equation, the
virial-improvement criterion, conformal-current conservation, and the
linearized RG relation \(y=D-\Delta\).

## Manuscript Changes

- Added Proposition `prop:cft-opening-flat-trace-equation`, deriving the flat
  source-chart trace identity
  \(T^\mu{}_\mu=\beta_I[O_I]_\mu+\partial_\mu V^\mu\) with contact terms tied
  to the renormalized source chart and the sign convention
  \(\mu\,dg_I/d\mu=\beta_I\).
- Added Proposition `prop:cft-opening-virial-improvement-currents`, proving
  that \(T^\mu{}_\mu=\partial_\mu V^\mu\) gives a conserved dilatation current,
  that \(V^\mu=(D-1)\partial^\mu L+J^\mu\) with \(\partial_\mu J^\mu=0\)
  gives a conserved traceless improved stress tensor, and that the improved
  tensor supplies conserved currents for every conformal Killing vector.
- Added the linearized-RG derivation paragraph deriving \(y_a=D-\Delta_a\)
  from the linearized RG equation and the scaling of
  \(\int d^D x\,O_a\), with a Jordan-block/logarithmic-mixing caveat.  This was
  later demoted from proposition form during the anti-wrapper audit because the
  calculation is a local scaling check rather than theorem-level machinery.

## Calculation Check

- Added `calculation-checks/cft_fixed_point_checks.py`.
- The script verifies the scalar-improvement trace coefficient, the special
  conformal Killing equation in mostly-plus signature, the fact that conformal
  current divergence only depends on the stress-tensor trace, and the finite
  algebra behind \(y=D-\Delta\) and a rank-two Jordan logarithmic block.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/cft_fixed_point_checks.py`
- `python3 -m py_compile calculation-checks/cft_fixed_point_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build and final log scan are clean.  The generated
`monograph/tex/main.pdf` has 2325 pages.
