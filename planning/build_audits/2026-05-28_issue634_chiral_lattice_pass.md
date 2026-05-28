# 2026-05-28 Issue #634: Chiral-Lattice Connection Pass

## Scope

Sixth focused development pass on GitHub issue #634 for
`monograph/tex/volumes/volume_ii/chapter19c_standard_model_hybrid_definition.tex`.

This pass develops the connection between the Standard Model hybrid datum and
the chiral-gauge lattice construction problem.

## Manuscript Changes

- Added a section `Chiral Lattice Status of the Electroweak Sector`.
- Defined the finite chiral-gauge regulator datum required for the full
  Standard Model representation content: compact gauge fields, a local
  gauge-covariant Ginsparg--Wilson/overlap-type Dirac operator, chiral
  projectors for the SM representations, a local gauge-invariant determinant
  line phase, Higgs/Yukawa data, and reflection/reconstruction data.
- Proved that local anomaly cancellation and the finite \(SU(2)\) parity
  condition are necessary determinant-line obstruction cancellations, but not
  sufficient for a complete nonperturbative regulator or continuum limit.
- Proved that lattice QCD matrix elements in the hybrid datum do not amount
  to a full nonperturbative Standard Model regulator; they compute
  gauge-invariant QCD matrix elements after electroweak matching.

## Calculation Check

- Extended `calculation-checks/standard_model_anomaly_checks.py` with the
  local and finite obstruction checks used in the chiral-lattice discussion:
  \(SU(3)^3\), \(SU(3)^2U(1)_Y\), \(SU(2)^2U(1)_Y\), \(U(1)_Y^3\),
  gravitational-\(U(1)_Y\), and weak-doublet parity.
- Updated `calculation-checks/README.md` and the chapter dossier.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/standard_model_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/standard_model_anomaly_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full manuscript build completed with a clean log scan and produced
`monograph/tex/main.pdf` with 2348 pages.

## Remaining Issue #634 Work

This pass does not close #634.  The remaining substantial item is the Higgs
vacuum-stability RG/source-chart treatment.
