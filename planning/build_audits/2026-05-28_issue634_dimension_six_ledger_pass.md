# 2026-05-28 Issue #634: Dimension-Six Ledger Pass

## Scope

Fifth focused development pass on GitHub issue #634 for
`monograph/tex/volumes/volume_ii/chapter19c_standard_model_hybrid_definition.tex`.

This pass replaces the earlier brief warning about dimension-six SMEFT bases
with a concrete quotient-space definition and an explicit Warsaw-type
dimension-six operator ledger.

## Manuscript Changes

- Defined the dimension-six quotient \(\mathcal Q_6\) of local gauge-invariant
  dimension-six densities modulo total derivatives and equation-of-motion
  field-coordinate directions.
- Proved that equation-of-motion operators are removed by local field
  redefinitions inside a declared regularized path integral.
- Added a Warsaw-type baryon-number preserving ledger: bosonic, two-fermion,
  and four-fermion operator classes, with explicit representative templates
  and class counts.
- Added the four baryon-violating dimension-six classes and stated their
  \(\Delta B=\Delta L=1\), \(\Delta(B-L)=0\) selection rule.
- Proved the field-content exhaustion statement from engineering dimensions,
  separating the finite Fierz/gauge-contraction basis choice from the
  dimension-counting argument.

## Calculation Check

- Extended `calculation-checks/standard_model_anomaly_checks.py` with exact
  checks for the one-generation Warsaw-type class counts:
  \(15+19+25=59\) baryon-number preserving classes, four
  baryon-violating classes, and the engineering dimension of each allowed
  field-content type.
- Updated `calculation-checks/README.md` and the chapter dossier to record
  the new checks and claim ledger.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/standard_model_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/standard_model_anomaly_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full manuscript build completed with a clean log scan and produced
`monograph/tex/main.pdf` with 2347 pages.

## Remaining Issue #634 Work

This pass does not close #634.  Remaining substantial items include the
chiral-lattice construction connection and the Higgs vacuum-stability
RG/source-chart treatment.
